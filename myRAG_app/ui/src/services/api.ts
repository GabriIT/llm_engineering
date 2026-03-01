import type { QueryResponse, Role } from "../types";

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

export async function fetchHealth(): Promise<{ status: string; collection: string; db_path: string }> {
  const response = await fetch(apiUrl("/api/health"));
  if (!response.ok) {
    throw new Error(`Health check failed (${response.status})`);
  }
  return (await response.json()) as { status: string; collection: string; db_path: string };
}
