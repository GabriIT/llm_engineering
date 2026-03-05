export type Role = "user" | "assistant";
export type ChatModelOption = "gpt-4.1-nano" | "qwen3:latest" | "llama3.2:latest";

export interface AuthUser {
  username: string;
  passwordHash: string;
}

export interface SourceRef {
  source: string;
  source_name: string;
  doc_type: string;
  page_number?: number;
  sheet_name?: string;
}

export interface StructuredAnswer {
  prompt: string;
  bullets: string[];
  answer_text: string;
}

export interface ThreadMessage {
  id: string;
  role: Role;
  content: string;
  createdAt: string;
  structured?: StructuredAnswer;
  sources?: SourceRef[];
}

export interface ChatThread {
  id: string;
  title: string;
  createdAt: string;
  updatedAt: string;
  messages: ThreadMessage[];
}

export interface QueryMeta {
  chat_model: string;
  embedding_model: string;
  k: number;
  search_type: "similarity" | "mmr";
  elapsed_ms: number;
}

export interface QueryResponse {
  answer: string;
  structured?: StructuredAnswer;
  sources: SourceRef[];
  meta: QueryMeta;
}
