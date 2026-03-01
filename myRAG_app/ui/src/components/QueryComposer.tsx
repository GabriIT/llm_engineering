import { FormEvent, useState } from "react";

interface QueryComposerProps {
  disabled: boolean;
  isSending: boolean;
  onSend: (query: string) => Promise<void>;
}

export function QueryComposer({ disabled, isSending, onSend }: QueryComposerProps) {
  const [query, setQuery] = useState("");

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    const trimmed = query.trim();
    if (!trimmed || disabled || isSending) {
      return;
    }
    setQuery("");
    await onSend(trimmed);
  }

  return (
    <form className="query-composer" onSubmit={handleSubmit}>
      <input
        aria-label="Ask a question"
        placeholder="Ask your RAG knowledge base..."
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        disabled={disabled || isSending}
      />
      <button type="submit" disabled={disabled || isSending || !query.trim()}>
        {isSending ? "Sending..." : "Send"}
      </button>
    </form>
  );
}
