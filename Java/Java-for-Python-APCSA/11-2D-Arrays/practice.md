# Day 11 Lab — Analyze a Weekly Focus Grid

## 🎯 Lab goal

Treat a two-dimensional array as a schedule: rows are weeks, columns are study days. Build an analyzer with nested loops that reuses methods, conditions, and report design.

**Today’s Java:** `int[][]`, `[row][col]`, `grid.length`, `grid[row].length`, nested loops.

**Reuse from Days 01–10:** methods, loops, accumulators, conditionals, classes/polymorphism as optional context.

## Mission

Create `FocusGridAnalyzer.java`. Use this grid, where each row is one week and each value is minutes studied on a day:

```java
int[][] focus = {
    {30, 45, 0, 60, 25},
    {50, 50, 40, 0, 70},
    {20, 35, 55, 65, 75}
};
```

Implement:

```java
public static int totalMinutes(int[][] grid)
public static int weekTotal(int[][] grid, int row)
public static int countStrongSessions(int[][] grid, int minimum)
public static int firstStrongDayInWeek(int[][] grid, int row, int minimum)
```

## Required report

Print:

1. total course minutes;
2. total for every week;
3. count of sessions at least 60 minutes;
4. the first strong-day index in week 0 with a minimum of 60;
5. a grid where every 0 is replaced with `REST` and every positive number prints as its minute value.

## Rules

- The outer loop iterates rows; the inner loop iterates that row’s columns.
- Write `grid[row].length` for inner loop bounds; do not assume all rows have the same length.
- `firstStrongDayInWeek` returns `-1` when the row has no matching value.
- Keep each method responsible for one result; `main` formats the report.

## Acceptance checks

1. Verify total by manually adding one row, then all rows.
2. Change one row to `{10, 20}`; the program must still run safely.
3. Use a threshold of 100; every first-strong result becomes `-1`.

## Stretch goal

Implement `public static void makeBorderZero(int[][] grid)` on a separate small rectangular grid. Explain why a 1-row or 1-column grid is an edge case worth testing.

## Reflection

Write the difference among `grid.length`, `grid[0].length`, and `grid[row].length`. Optional focused drills: [Drill Bank](./drills.md).
