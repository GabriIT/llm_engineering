import {
  getThreadsForUser,
  getUsers,
  hashPassword,
  saveThreadsForUser,
  saveUsers,
} from "./storage";

describe("storage service", () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it("isolates threads per user", () => {
    saveThreadsForUser("alice", [
      {
        id: "a1",
        title: "Alice thread",
        createdAt: "2026-01-01T00:00:00.000Z",
        updatedAt: "2026-01-01T00:00:00.000Z",
        messages: [],
      },
    ]);

    saveThreadsForUser("bob", [
      {
        id: "b1",
        title: "Bob thread",
        createdAt: "2026-01-01T00:00:00.000Z",
        updatedAt: "2026-01-01T00:00:00.000Z",
        messages: [],
      },
    ]);

    expect(getThreadsForUser("alice").threads).toHaveLength(1);
    expect(getThreadsForUser("alice").threads[0].title).toBe("Alice thread");
    expect(getThreadsForUser("bob").threads[0].title).toBe("Bob thread");
  });

  it("recovers from malformed thread payload", () => {
    localStorage.setItem("myrag_threads_v1:alice", "{bad-json");

    const result = getThreadsForUser("alice");
    expect(result.threads).toEqual([]);
    expect(result.recoveredFromCorruption).toBe(true);
  });

  it("persists and reads users", () => {
    saveUsers([{ username: "alice", passwordHash: "h" }]);
    expect(getUsers()).toEqual([{ username: "alice", passwordHash: "h" }]);
  });

  it("falls back when crypto.subtle is unavailable", async () => {
    const originalCrypto = globalThis.crypto;
    Object.defineProperty(globalThis, "crypto", { value: undefined, configurable: true });
    try {
      const one = await hashPassword("secret");
      const two = await hashPassword("secret");
      expect(one).toBe(two);
      expect(one.startsWith("fallback-")).toBe(true);
    } finally {
      Object.defineProperty(globalThis, "crypto", { value: originalCrypto, configurable: true });
    }
  });
});
