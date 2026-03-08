import type {
  ChatModelOption,
  QueryResponse,
  Role,
  ThreadMessageApi,
  ThreadSummaryApi,
} from "../types";

interface HistoryMessage {
  role: Role;
  content: string;
}

interface RetrievalOptions {
  k?: number;
  search_type?: "similarity" | "mmr";
  fetch_k?: number;
  lambda_mult?: number;
  doc_type?: string;
  source_contains?: string;
}

interface QueryRequest {
  question: string;
  history?: HistoryMessage[];
  retrieval?: RetrievalOptions;
  chat_model?: ChatModelOption;
  username?: string;
  thread_id?: string;
}

interface CreateThreadRequest {
  username: string;
  thread_id?: string;
  title?: string;
}

interface CreateThreadResponse {
  thread: ThreadSummaryApi;
}

interface RenameThreadRequest {
  username: string;
  title: string;
}

interface RenameThreadResponse {
  thread: ThreadSummaryApi;
}

interface DeleteThreadResponse {
  deleted: boolean;
  thread_id: string;
}

interface ListThreadsResponse {
  threads: ThreadSummaryApi[];
}

interface GetThreadMessagesResponse {
  thread: ThreadSummaryApi;
  messages: ThreadMessageApi[];
}

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "").replace(/\/+$/, "");

function apiUrl(path: string): string {
  if (!API_BASE_URL) {
    return path;
  }
  return `${API_BASE_URL}${path}`;
}

const DEFAULT_RETRIEVAL: Required<
  Pick<RetrievalOptions, "k" | "search_type" | "fetch_k" | "lambda_mult">
> = {
  k: 8,
  search_type: "mmr",
  fetch_k: 40,
  lambda_mult: 0.35,
};

export async function queryRag(payload: QueryRequest): Promise<QueryResponse> {
  const requestPayload: QueryRequest = {
    ...payload,
    retrieval: {
      ...DEFAULT_RETRIEVAL,
      ...(payload.retrieval ?? {}),
    },
  };

  const response = await fetch(apiUrl("/api/rag/query"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestPayload),
  });

  if (!response.ok) {
    let detail = "Unknown server error";
    try {
      const json = (await response.json()) as { detail?: unknown };
      if (typeof json.detail === "string") {
        detail = json.detail;
      } else if (json.detail && typeof json.detail === "object") {
        detail = JSON.stringify(json.detail);
      }
    } catch {
      detail = response.statusText || detail;
    }
    throw new Error(`Query failed (${response.status}): ${detail}`);
  }

  return (await response.json()) as QueryResponse;
}

export async function listThreads(username: string, limit = 50): Promise<ThreadSummaryApi[]> {
  const response = await fetch(
    apiUrl(`/api/threads?username=${encodeURIComponent(username)}&limit=${limit}`),
  );
  if (!response.ok) {
    let detail = "Unknown server error";
    try {
      const json = (await response.json()) as { detail?: unknown };
      if (typeof json.detail === "string") {
        detail = json.detail;
      } else if (json.detail && typeof json.detail === "object") {
        detail = JSON.stringify(json.detail);
      }
    } catch {
      detail = response.statusText || detail;
    }
    throw new Error(`List threads failed (${response.status}): ${detail}`);
  }
  const payload = (await response.json()) as ListThreadsResponse;
  return payload.threads ?? [];
}

export async function createThread(payload: CreateThreadRequest): Promise<ThreadSummaryApi> {
  const response = await fetch(apiUrl("/api/threads"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    let detail = "Unknown server error";
    try {
      const json = (await response.json()) as { detail?: unknown };
      if (typeof json.detail === "string") {
        detail = json.detail;
      } else if (json.detail && typeof json.detail === "object") {
        detail = JSON.stringify(json.detail);
      }
    } catch {
      detail = response.statusText || detail;
    }
    throw new Error(`Create thread failed (${response.status}): ${detail}`);
  }
  const json = (await response.json()) as CreateThreadResponse;
  return json.thread;
}

export async function getThreadMessages(
  username: string,
  threadId: string,
  limit = 500,
): Promise<GetThreadMessagesResponse> {
  const response = await fetch(
    apiUrl(
      `/api/threads/${encodeURIComponent(threadId)}/messages?username=${encodeURIComponent(username)}&limit=${limit}`,
    ),
  );
  if (!response.ok) {
    let detail = "Unknown server error";
    try {
      const json = (await response.json()) as { detail?: unknown };
      if (typeof json.detail === "string") {
        detail = json.detail;
      } else if (json.detail && typeof json.detail === "object") {
        detail = JSON.stringify(json.detail);
      }
    } catch {
      detail = response.statusText || detail;
    }
    throw new Error(`Get thread messages failed (${response.status}): ${detail}`);
  }
  return (await response.json()) as GetThreadMessagesResponse;
}

export async function renameThread(
  threadId: string,
  payload: RenameThreadRequest,
): Promise<ThreadSummaryApi> {
  const response = await fetch(apiUrl(`/api/threads/${encodeURIComponent(threadId)}`), {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    let detail = "Unknown server error";
    try {
      const json = (await response.json()) as { detail?: unknown };
      if (typeof json.detail === "string") {
        detail = json.detail;
      } else if (json.detail && typeof json.detail === "object") {
        detail = JSON.stringify(json.detail);
      }
    } catch {
      detail = response.statusText || detail;
    }
    throw new Error(`Rename thread failed (${response.status}): ${detail}`);
  }
  const payloadJson = (await response.json()) as RenameThreadResponse;
  return payloadJson.thread;
}

export async function deleteThread(username: string, threadId: string): Promise<DeleteThreadResponse> {
  const response = await fetch(
    apiUrl(`/api/threads/${encodeURIComponent(threadId)}?username=${encodeURIComponent(username)}`),
    {
      method: "DELETE",
    },
  );
  if (!response.ok) {
    let detail = "Unknown server error";
    try {
      const json = (await response.json()) as { detail?: unknown };
      if (typeof json.detail === "string") {
        detail = json.detail;
      } else if (json.detail && typeof json.detail === "object") {
        detail = JSON.stringify(json.detail);
      }
    } catch {
      detail = response.statusText || detail;
    }
    throw new Error(`Delete thread failed (${response.status}): ${detail}`);
  }
  return (await response.json()) as DeleteThreadResponse;
}

export async function fetchHealth(): Promise<{
  status: string;
  collection: string;
  db_path: string;
  thread_memory_enabled?: boolean;
  thread_memory_ready?: boolean;
}> {
  const response = await fetch(apiUrl("/api/health"));
  if (!response.ok) {
    throw new Error(`Health check failed (${response.status})`);
  }
  return (await response.json()) as {
    status: string;
    collection: string;
    db_path: string;
    thread_memory_enabled?: boolean;
    thread_memory_ready?: boolean;
  };
}
