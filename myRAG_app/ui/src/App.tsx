import { useState } from "react";

import { AuthPanel } from "./components/AuthPanel";
import { QueryComposer } from "./components/QueryComposer";
import { ThreadSidebar } from "./components/ThreadSidebar";
import { ThreadView } from "./components/ThreadView";
import { useAuth } from "./hooks/useAuth";
import { useThreads } from "./hooks/useThreads";
import type { ChatModelOption } from "./types";

export default function App() {
  const { currentUser, register, login, logout } = useAuth();
  const {
    threads,
    activeThread,
    activeThreadId,
    storageWarning,
    isSending,
    createThread,
    selectThread,
    sendQuery,
  } = useThreads(currentUser);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);
  const [selectedModel, setSelectedModel] = useState<ChatModelOption>("gpt-4.1-nano");
  const [answerViewMode, setAnswerViewMode] = useState<"structured" | "raw">("structured");

  if (!currentUser) {
    return <AuthPanel onRegister={register} onLogin={login} />;
  }

  return (
    <div className="app-shell">
      <ThreadSidebar
        username={currentUser}
        threads={threads}
        activeThreadId={activeThreadId}
        mobileOpen={mobileSidebarOpen}
        onToggleMobile={() => setMobileSidebarOpen((open) => !open)}
        onCreateThread={() => {
          createThread();
          setMobileSidebarOpen(false);
        }}
        onSelectThread={(threadId) => {
          selectThread(threadId);
          setMobileSidebarOpen(false);
        }}
        onLogout={logout}
      />

      <main className="chat-main">
        <header className="chat-header">
          <button
            type="button"
            className="mobile-only"
            onClick={() => setMobileSidebarOpen((open) => !open)}
          >
            Threads
          </button>
          <div>
            <h1>{activeThread?.title ?? "myRAG Chat"}</h1>
            <p>Multi-turn RAG assistant with local pseudo-auth and thread history.</p>
          </div>
          <div className="view-toggle" role="group" aria-label="Answer view mode">
            <button
              type="button"
              className={answerViewMode === "structured" ? "active" : ""}
              onClick={() => setAnswerViewMode("structured")}
            >
              Structured
            </button>
            <button
              type="button"
              className={answerViewMode === "raw" ? "active" : ""}
              onClick={() => setAnswerViewMode("raw")}
            >
              Raw
            </button>
          </div>
        </header>

        {storageWarning ? <div className="warning-banner">{storageWarning}</div> : null}

        <ThreadView thread={activeThread} answerViewMode={answerViewMode} />

        <QueryComposer
          disabled={!currentUser}
          isSending={isSending}
          selectedModel={selectedModel}
          onSelectModel={setSelectedModel}
          onSend={sendQuery}
        />
      </main>
    </div>
  );
}
