import type { ChatThread } from "../types";

interface ThreadViewProps {
  thread: ChatThread | null;
}

function formatTime(isoDate: string): string {
  return new Date(isoDate).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

export function ThreadView({ thread }: ThreadViewProps) {
  if (!thread) {
    return (
      <div className="thread-empty">
        <h3>No thread selected</h3>
        <p>Create a new thread from the left panel and start asking questions.</p>
      </div>
    );
  }

  return (
    <div className="thread-view">
      {thread.messages.map((message) => (
        <article key={message.id} className={`bubble ${message.role}`}>
          <header>
            <strong>{message.role === "user" ? "You" : "Assistant"}</strong>
            <time>{formatTime(message.createdAt)}</time>
          </header>
          <p>{message.content}</p>

          {message.role === "assistant" && message.sources && message.sources.length > 0 ? (
            <details>
              <summary>Sources ({message.sources.length})</summary>
              <ul>
                {message.sources.map((source, idx) => (
                  <li key={`${source.source}-${idx}`}>
                    <span>{source.source_name}</span>
                    <small>
                      {source.doc_type}
                      {source.page_number ? ` page=${source.page_number}` : ""}
                      {source.sheet_name ? ` sheet=${source.sheet_name}` : ""}
                    </small>
                  </li>
                ))}
              </ul>
            </details>
          ) : null}
        </article>
      ))}
    </div>
  );
}
