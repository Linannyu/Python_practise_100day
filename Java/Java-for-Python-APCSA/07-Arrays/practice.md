# Day 07 Lab — Build a Score Analyzer

## 🎯 Lab goal

Use a fixed-size array to analyze test scores and produce a useful summary. The Lab combines methods, loops, conditionals, and today’s index-based array rules.

**Today’s Java:** `int[]`, `.length`, array indexing, enhanced `for`, in-place array modification.

**Reuse from Days 01–06:** methods with return values, loop accumulators, thresholds, formatted reports.

## Mission

Create `ScoreAnalyzer.java`. Start with:

```java
int[] scores = {88, 72, 95, 58, 88, 61};
```

Implement these methods:

```java
public static int highestScore(int[] scores)
public static int countPassing(int[] scores)
public static int firstScoreAtLeast(int[] scores, int target)
public static void addCurve(int[] scores, int points)
```

## Rules

- A passing score is at least 60.
- `firstScoreAtLeast` returns `-1` if no score reaches target.
- `addCurve` changes the original array, but no final score may exceed 100.
- Use `scores.length`, never `scores.length()`.

## Required report and tests

Before curving, print highest score, passing count, and first score at least 90. Apply a 5-point curve, then print the whole updated array.

For the provided data, the first score at least 90 is index 2. After the curve, 95 becomes 100, not 100+.

Also test:

- a one-element array `{59}`;
- an array with no score at least 90;
- an array that already contains 100.

## Acceptance checks

1. All traversal conditions use `< scores.length`.
2. `addCurve` changes the caller’s array rather than a loop copy.
3. No curved score is greater than 100.
4. `firstScoreAtLeast` returns `-1` when no score satisfies the target.

## Stretch goal

Implement `hasConsecutiveDuplicates(int[] scores)` and use it to report whether adjacent equal scores exist.

## Reflection

Explain why `for (int score : scores) { score += 5; }` does not curve the original array. Optional focused drills: [Drill Bank](./drills.md).
