export type Role = "user" | "assistant";

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

export interface ThreadMessage {
  id: string;
  role: Role;
  content: string;
  createdAt: string;
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
  sources: SourceRef[];
  meta: QueryMeta;
}
