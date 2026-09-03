# Day 05 Lab — Turn the Study Analyzer into a Toolkit

## 🎯 Lab goal

Refactor your Day 04 report into small methods with clear contracts. The Lab succeeds when `main` reads like a high-level plan rather than one long algorithm.

**Today’s Java:** method headers, parameters, arguments, return values, `void`, `static`.

**Reuse from Days 01–04:** arrays, loops, conditions, integer division awareness, formatted output.

## Mission

Create `StudyToolkit.java`. Use this data in `main`:

```java
int[] minutes = {35, 0, 50, 80, 20, 65, 40};
```

Implement all four methods below, then call them from `main` to print a report:

```java
public static int totalMinutes(int[] values)
public static int countStrongDays(int[] values, int minimum)
public static double averageMinutes(int[] values)
public static int firstDayAtLeast(int[] values, int minimum)
```

## Method contracts

- `totalMinutes` returns the sum.
- `countStrongDays` returns how many values are at least `minimum`.
- `averageMinutes` returns a double; assume the array is nonempty.
- `firstDayAtLeast` returns the first matching index, otherwise `-1`.

## Required tests in `main`

Test the original array, `{0, 0}`, and `{60}`. For `{60}`, the total is 60, strong-day count at 60 is 1, average is 60.0, and first matching index is 0.

## Acceptance checks

1. Each of the four required methods has the exact stated header.
2. Returning methods use `return`; they do not print the result themselves.
3. `firstDayAtLeast(new int[] {0, 0}, 60)` returns `-1`.
4. `averageMinutes(new int[] {60})` returns `60.0`, not an int.

## Design rules

- Do not print from the three returning methods.
- Do not duplicate loop logic in `main`.
- Keep the method headers exactly as written.
- Add a short comment above each method describing its return value.

## Stretch goal

Add `public static boolean metWeeklyGoal(int[] values, int goal)` and use it in the report.

## Automated method habit

The course tester has a fixed-signature example for this chapter: [Problem 05-12 in Drill Bank](./drills.md). You can run it after creating its separate `work/` file; this Lab itself should be tested through the cases above.

## Reflection

Which logic belongs in a method versus in `main`? Write one answer in [mistakes.md](../mistakes.md) if you made a return/print mix-up.
