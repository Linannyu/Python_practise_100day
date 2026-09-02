# Mistakes

记录“规则”而不只是“我错了”。每次重做正确后，在条目末尾加上 `Retried: YYYY-MM-DD ✓`。

## Template

### YYYY-MM-DD — Chapter XX — Problem XX-XX

- **My incorrect code / idea:**

```java
// Paste only the relevant lines.
```

- **What happened:** Compile error / wrong output / test failure
- **Why it happened:**
- **Correct rule:**
- **Smallest corrected example:**

```java
// Corrected lines.
```

- **Retry date:**

---

## Example — Off-by-one

### 2026-09-01 — Chapter 04 — Problem 04-07

- **My incorrect code / idea:** `for (int i = 0; i <= arr.length; i++)`
- **What happened:** `ArrayIndexOutOfBoundsException`
- **Why it happened:** I treated length as the final valid index.
- **Correct rule:** An array of length `n` has indices `0` through `n - 1`; a traversal normally uses `i < arr.length`.
- **Smallest corrected example:**

```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

- **Retry date:**
