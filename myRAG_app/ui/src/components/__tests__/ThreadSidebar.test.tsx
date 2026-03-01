import { fireEvent, render, screen } from "@testing-library/react";
import { vi } from "vitest";

import type { ChatThread } from "../../types";
import { ThreadSidebar } from "../ThreadSidebar";

function makeThread(id: string, title: string, updatedAt: string): ChatThread {
  return {
    id,
    title,
    createdAt: updatedAt,
    updatedAt,
    messages: [],
  };
}

describe("ThreadSidebar", () => {
  it("sorts threads by updatedAt and supports select/new", () => {
    const onSelect = vi.fn();
    const onCreate = vi.fn();

    render(
      <ThreadSidebar
        username="alice"
        threads={[
          makeThread("old", "Older", "2026-01-01T10:00:00.000Z"),
          makeThread("new", "Newest", "2026-03-01T12:00:00.000Z"),
        ]}
        activeThreadId={"new"}
        mobileOpen={false}
        onToggleMobile={vi.fn()}
        onCreateThread={onCreate}
        onSelectThread={onSelect}
        onLogout={vi.fn()}
      />,
    );

    const titles = screen.getAllByRole("button", { name: /Newest|Older/ }).map((el) => el.textContent);
    expect(titles[0]).toContain("Newest");
    expect(titles[1]).toContain("Older");

    fireEvent.click(screen.getByRole("button", { name: /\+ New Thread/ }));
    expect(onCreate).toHaveBeenCalledTimes(1);

    fireEvent.click(screen.getByRole("button", { name: /Older/ }));
    expect(onSelect).toHaveBeenCalledWith("old");
  });
});
