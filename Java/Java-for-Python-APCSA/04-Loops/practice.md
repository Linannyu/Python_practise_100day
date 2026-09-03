# Day 04 Lab — Analyze a Week of Study Minutes

## 🎯 Lab goal

Use loops to transform a sequence of daily study values into a report. This is the first Lab where you repeatedly apply earlier conditionals inside iteration.

**Today’s Java:** `for`, `while`, enhanced `for`, accumulators, counters, `break`, loop bounds.

**Reuse from Days 01–03:** variables, integer/decimal division, boolean conditions, and clean report formatting.

## Mission

Create `StudyWeekAnalyzer.java`. Begin with:

```java
int[] minutes = {35, 0, 50, 80, 20, 65, 40};
```

Using loops, print a report containing:

1. total minutes;
2. number of active days (more than 0 minutes);
3. number of strong days (at least 60 minutes);
4. exact daily average as a `double`;
5. the first day index with at least 60 minutes, or `-1` if none.

## Rules

- Use an enhanced `for` at least once for total/counting.
- Use an index-based `for` loop to find the first strong day, then `break`.
- Do not use a hardcoded number for the array length.
- Avoid `i <= minutes.length`.

## Expected result for the provided data

```text
Total: 290
Active days: 6
Strong days: 2
Average: 41.42857142857143
First strong day index: 3
```

## Acceptance checks

1. Change all values to 0; first strong day becomes `-1`.
2. Change first value to 60; first strong day becomes 0.
3. Explain why total/length must be cast or use `double` for an exact average.

## Stretch goal

Print each active day as `Day i: <minutes>`. Skip inactive days with `continue`.

## Reflection

For this Lab, record the meaning of `i` at the start of every indexed-loop iteration. Optional focused drills: [Drill Bank](./drills.md).
