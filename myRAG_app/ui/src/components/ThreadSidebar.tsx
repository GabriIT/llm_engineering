import type { ChatThread } from "../types";

interface ThreadSidebarProps {
  username: string;
  threads: ChatThread[];
  activeThreadId: string | null;
  mobileOpen: boolean;
  onToggleMobile: () => void;
  onCreateThread: () => void;
  onSelectThread: (threadId: string) => void;
  onLogout: () => void;
}

function formatUpdatedAt(isoDate: string): string {
  const date = new Date(isoDate);
  return date.toLocaleString();
}

export function ThreadSidebar({
  username,
  threads,
  activeThreadId,
  mobileOpen,
  onToggleMobile,
  onCreateThread,
  onSelectThread,
  onLogout,
}: ThreadSidebarProps) {
  const sorted = [...threads].sort(
    (a, b) => new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime(),
  );

  return (
    <aside className={`sidebar ${mobileOpen ? "open" : ""}`}>
      <div className="sidebar-top">
        <h2>Threads</h2>
        <button type="button" className="mobile-only" onClick={onToggleMobile}>
          Close
        </button>
      </div>

      <div className="sidebar-user">
        <div>
          <span className="label">Signed in</span>
          <strong>{username}</strong>
        </div>
        <button type="button" onClick={onLogout}>
          Logout
        </button>
      </div>

      <button type="button" className="new-thread" onClick={onCreateThread}>
        + New Thread
      </button>

      <ul className="thread-list">
        {sorted.map((thread) => (
          <li key={thread.id}>
            <button
              type="button"
              className={thread.id === activeThreadId ? "thread-item active" : "thread-item"}
              onClick={() => onSelectThread(thread.id)}
            >
              <span className="thread-title">{thread.title}</span>
              <span className="thread-time">{formatUpdatedAt(thread.updatedAt)}</span>
            </button>
          </li>
        ))}
      </ul>
    </aside>
  );
}
