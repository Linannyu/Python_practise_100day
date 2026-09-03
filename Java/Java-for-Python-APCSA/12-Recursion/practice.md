# Day 12 Lab — Build a Recursive Study Streak Explorer

## 🎯 Lab goal

Use recursion to analyze a sequence without writing a loop in the recursive methods. The Lab reuses arrays, String output, conditions, methods, and the Day 11 idea of reducing a larger problem into smaller pieces.

**Today’s Java:** base case, recursive case, call stack, recursive return values, pre/post recursive work.

**Reuse from Days 01–11:** method contracts, conditions, arrays, String formatting, careful index bounds.

## Mission

Create `RecursiveStreakExplorer.java`. Given:

```java
int[] minutes = {30, 45, 0, 60, 25, 70};
```

Implement these recursive methods. Do not use `for` or `while` inside them:

```java
public static int totalFrom(int[] values, int index)
public static int countActiveFrom(int[] values, int index)
public static int longestActiveStreak(int[] values, int index, int currentStreak)
public static void printCountdown(int n)
```

## Method contracts

- `totalFrom(values, index)` returns values from index through the end.
- `countActiveFrom` counts values greater than 0 from index onward.
- `longestActiveStreak` returns the largest run of values greater than 0, starting its search at index. A day with 0 ends the current streak.
- `printCountdown(3)` prints 3, 2, 1, each on its own line.

## Acceptance checks

1. Every recursive method has a base case before its recursive call.
2. Each recursive call moves `index`, `n`, or the String closer to its base case.
3. No required recursive method contains `for` or `while`.
4. The required three test arrays produce the specified total, active count, and streak length.

## Required test cases

In `main`, run all methods for:

1. `{30, 45, 0, 60, 25, 70}` → total 230, active count 5, longest streak 3;
2. `{0, 0}` → total 0, active count 0, longest streak 0;
3. `{50}` → total 50, active count 1, longest streak 1.

## Design checkpoint

Before coding, write a comment above each method answering:

- What is the smallest input / stopping index?
- What does the method return there?
- Which argument becomes smaller or closer to the end?

## Stretch goal

Write `printReverse(String text)` recursively. It may use `substring(1)`, but it must not build a reversed String with a loop.

## Reflection

Trace `totalFrom({2, 3}, 0)` by hand. Record the base case and each return value in [mistakes.md](../mistakes.md) if your first base case was wrong. Optional focused drills: [Drill Bank](./drills.md).
