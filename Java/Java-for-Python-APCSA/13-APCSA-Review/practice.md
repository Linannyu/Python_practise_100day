# Day 13 Capstone Lab — Build an AP CSA Study Dashboard

## 🎯 Lab goal

Create a small, complete AP CSA-style program that models study tasks, analyzes score data, and produces a final report. This is an integration Lab: the goal is clear design and correct basic Java, not advanced frameworks.

**Today’s focus:** AP CSA problem decomposition, class design, ArrayList traversal, arrays/2D arrays, methods, edge cases, testing, and debugging.

**Reuse from Days 01–12:** all core course concepts. Pick simple, correct implementations rather than trying to use every feature in one clever expression.

## Mission

Create `StudyDashboard.java`. The program must include:

1. a `StudyTask` class;
2. an `ArrayList<StudyTask>` of at least four tasks;
3. a one-dimensional `int[]` of quiz scores;
4. a two-dimensional `int[][]` of weekly focus minutes;
5. methods that calculate and print a dashboard.

## Minimum `StudyTask` design

```java
private String title;
private int estimatedMinutes;
private boolean complete;

public StudyTask(String title, int estimatedMinutes)
public void markComplete()
public boolean isComplete()
public int getEstimatedMinutes()
public String getTitle()
```

## Required dashboard methods

Use these exact method headers where applicable:

```java
public static int countIncomplete(ArrayList<StudyTask> tasks)
public static int sumPositive(int[] values)
public static double average(int[] values)
public static int totalMinutes(int[][] grid)
public static int longestIncreasingRun(int[] values)
```

`longestIncreasingRun` returns 0 for an empty array; otherwise it returns the longest run of consecutive strictly increasing scores. Example: `{70, 75, 80, 60, 65}` gives 3.

## Required final report

Your main method must print:

```text
=== AP CSA Study Dashboard ===
Incomplete tasks: ...
Remaining estimated minutes: ...
Positive score total: ...
Score average: ...
Longest improving score run: ...
Total focus minutes: ...
```

The values must come from your objects/arrays/methods—not hardcoded output. Mark at least one task complete before printing.

## Test plan

Before you consider the Lab done, test:

1. empty score array for `longestIncreasingRun`;
2. all-negative score values for `sumPositive`;
3. a list where every task is complete;
4. a grid with a short row such as `{20, 30}`;
5. a single-score array for average and run length.

## Acceptance checks — AP CSA submission checklist

- Every given method has the exact name, parameter types, and return type.
- `String` content comparisons use `.equals()`.
- arrays use `.length`; ArrayLists use `.size()`.
- no loop attempts access at `length` / `size`.
- use `double` division for average.
- fields are private and object behavior is called by methods.

## Stretch goal

Add a recursive method `countActiveDays(int[] values, int index)` to report active days without a loop. Keep it separate from the required `longestIncreasingRun` method.

## Reflection

Update [PROGRESS.md](../PROGRESS.md), add your two most useful bugs to [mistakes.md](../mistakes.md), and then choose specific warm-up drills from [Drill Bank](./drills.md) only for skills that still feel weak.
