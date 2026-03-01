import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { vi } from "vitest";

import App from "../../App";

describe("App chat flow", () => {
  beforeEach(() => {
    localStorage.clear();
    localStorage.setItem(
      "myrag_users_v1",
      JSON.stringify([{ username: "alice", passwordHash: "hash" }]),
    );
    localStorage.setItem("myrag_current_user_v1", "alice");
    vi.restoreAllMocks();
  });

  it("sends query and renders assistant answer with source", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => ({
        ok: true,
        json: async () => ({
          answer: "Synthetic answer",
          sources: [
            {
              source: "/tmp/doc.pdf",
              source_name: "doc.pdf",
              doc_type: "Certifications",
              page_number: 1,
            },
          ],
          meta: {
            chat_model: "gpt-4.1-nano",
            embedding_model: "text-embedding-3-large",
            k: 8,
            search_type: "mmr",
            elapsed_ms: 12,
          },
        }),
      })),
    );

    render(<App />);

    fireEvent.change(screen.getByLabelText("Ask a question"), {
      target: { value: "What is covered?" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Send" }));

    expect(await screen.findByText("Synthetic answer")).toBeInTheDocument();
    expect(screen.getByText("Sources (1)")).toBeInTheDocument();
  });

  it("shows backend error fallback when request fails", async () => {
    vi.stubGlobal("fetch", vi.fn(async () => ({ ok: false, status: 500, json: async () => ({ detail: "boom" }) })));

    render(<App />);

    fireEvent.change(screen.getByLabelText("Ask a question"), {
      target: { value: "Question" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Send" }));

    await waitFor(() => {
      expect(screen.getByText(/The backend request failed/)).toBeInTheDocument();
    });
  });
});
