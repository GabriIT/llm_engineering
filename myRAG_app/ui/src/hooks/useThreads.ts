import { useEffect, useMemo, useState } from "react";

import { queryRag } from "../services/api";
import {
  getActiveThreadId,
  getThreadsForUser,
  saveThreadsForUser,
  setActiveThreadId,
} from "../services/storage";
import type { ChatModelOption, ChatThread, QueryResponse, ThreadMessage } from "../types";

const ERROR_FALLBACK =
  "The backend request failed. Please retry. Check API server and network connectivity.";

function newId(): string {
  if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
    return crypto.randomUUID();
  }
  return `id-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function nowIso(): string {
  return new Date().toISOString();
}

function makeTitle(question: string): string {
  const clean = question.trim().replace(/\s+/g, " ");
  if (!clean) {
    return "New Thread";
  }
  return clean.length > 48 ? `${clean.slice(0, 48)}...` : clean;
}

function sortThreads(threads: ChatThread[]): ChatThread[] {
  return [...threads].sort(
    (a, b) => new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime(),
  );
}

function upsertThread(threads: ChatThread[], updatedThread: ChatThread): ChatThread[] {
  const rest = threads.filter((thread) => thread.id !== updatedThread.id);
  return sortThreads([updatedThread, ...rest]);
}

function newThread(): ChatThread {
  const now = nowIso();
  return {
    id: newId(),
    title: "New Thread",
    createdAt: now,
    updatedAt: now,
    messages: [],
  };
}

function toHistory(messages: ThreadMessage[]): Array<{ role: "user" | "assistant"; content: string }> {
  return messages.map((message) => ({ role: message.role, content: message.content }));
}

export function useThreads(username: string | null) {
  const [threads, setThreads] = useState<ChatThread[]>([]);
  const [activeThreadId, setActiveThreadIdState] = useState<string | null>(null);
  const [storageWarning, setStorageWarning] = useState<string | null>(null);
  const [isSending, setIsSending] = useState(false);

  useEffect(() => {
    if (!username) {
      setThreads([]);
      setActiveThreadIdState(null);
      setStorageWarning(null);
      return;
    }

    const loaded = getThreadsForUser(username);
    const orderedThreads = sortThreads(loaded.threads);
    setThreads(orderedThreads);

    const storedActive = getActiveThreadId(username);
    const defaultActive = storedActive && orderedThreads.some((t) => t.id === storedActive)
      ? storedActive
      : orderedThreads[0]?.id ?? null;
    setActiveThreadIdState(defaultActive);

    if (loaded.recoveredFromCorruption) {
      setStorageWarning(
        "Thread storage was corrupted and has been reset for this user.",
      );
    } else {
      setStorageWarning(null);
    }
  }, [username]);

  useEffect(() => {
    if (!username) {
      return;
    }
    saveThreadsForUser(username, threads);
  }, [username, threads]);

  useEffect(() => {
    if (!username || !activeThreadId) {
      return;
    }
    setActiveThreadId(username, activeThreadId);
  }, [username, activeThreadId]);

  const activeThread = useMemo(
    () => threads.find((thread) => thread.id === activeThreadId) ?? null,
    [activeThreadId, threads],
  );

  function createThread(): string {
    const thread = newThread();
    setThreads((prev) => upsertThread(prev, thread));
    setActiveThreadIdState(thread.id);
    return thread.id;
  }

  function selectThread(threadId: string): void {
    setActiveThreadIdState(threadId);
  }

  async function sendQuery(questionInput: string, chatModel: ChatModelOption): Promise<void> {
    const question = questionInput.trim();
    if (!question || !username || isSending) {
      return;
    }

    setIsSending(true);

    const existingThread = activeThreadId
      ? threads.find((thread) => thread.id === activeThreadId) ?? null
      : null;

    const baseThread = existingThread ?? newThread();
    const userMessage: ThreadMessage = {
      id: newId(),
      role: "user",
      content: question,
      createdAt: nowIso(),
    };

    const priorHistory = toHistory(baseThread.messages);

    const withUserMessage: ChatThread = {
      ...baseThread,
      title: baseThread.messages.length === 0 ? makeTitle(question) : baseThread.title,
      updatedAt: nowIso(),
      messages: [...baseThread.messages, userMessage],
    };

    setActiveThreadIdState(withUserMessage.id);
    setThreads((prev) => upsertThread(prev, withUserMessage));

    try {
      const response: QueryResponse = await queryRag({
        question,
        history: priorHistory,
        chat_model: chatModel,
        username,
        thread_id: withUserMessage.id,
      });
      const assistantMessage: ThreadMessage = {
        id: newId(),
        role: "assistant",
        content: response.answer,
        createdAt: nowIso(),
        structured: response.structured,
        sources: response.sources,
      };

      const completedThread: ChatThread = {
        ...withUserMessage,
        updatedAt: nowIso(),
        messages: [...withUserMessage.messages, assistantMessage],
      };
      setThreads((prev) => upsertThread(prev, completedThread));
    } catch (error) {
      const assistantMessage: ThreadMessage = {
        id: newId(),
        role: "assistant",
        content:
          error instanceof Error && error.message ? `${ERROR_FALLBACK}\n${error.message}` : ERROR_FALLBACK,
        createdAt: nowIso(),
      };
      const failedThread: ChatThread = {
        ...withUserMessage,
        updatedAt: nowIso(),
        messages: [...withUserMessage.messages, assistantMessage],
      };
      setThreads((prev) => upsertThread(prev, failedThread));
    } finally {
      setIsSending(false);
    }
  }

  return {
    threads,
    activeThread,
    activeThreadId,
    storageWarning,
    isSending,
    createThread,
    selectThread,
    sendQuery,
  };
}
