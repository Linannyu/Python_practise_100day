# Day 08 Lab — Build a Flexible Study Planner

## 🎯 Lab goal

Replace fixed-size data with a growing task list. You will use methods, loops, String comparison, and safe removal while practicing `ArrayList`.

**Today’s Java:** `ArrayList<String>`, `add`、`get`、`set`、`remove`、`size`, `Integer`.

**Reuse from Days 01–07:** methods, String content comparison, conditions, indexed traversal, and report output.

## Mission

Create `StudyPlanner.java` and import `java.util.ArrayList`. In `main`, create a list with:

```text
Read lesson


Write Java code
Review mistakes
```

The empty String represents an accidental blank task.

Implement:

```java
public static void addIfMissing(ArrayList<String> tasks, String task)
public static int removeBlankTasks(ArrayList<String> tasks)
public static int countTasksContaining(ArrayList<String> tasks, String keyword)
```

## Rules

- `addIfMissing` must not add duplicate text; compare text using `.equals()`.
- `removeBlankTasks` removes every `""` and returns the number removed.
- Do not skip an element when removing: iterate backward or carefully control the index.
- `countTasksContaining` uses `indexOf(keyword) >= 0`.

## Required test sequence

1. Try adding `Read lesson` again; size should not grow.
2. Add `Read ArrayList lesson`; size should grow once.
3. Remove blank tasks and print the number removed and remaining list.
4. Count tasks containing `Read`.

## Acceptance checks

- Use `tasks.size()`, not `.length`.
- Use `tasks.get(i)` / `tasks.set(i, value)`, not `[i]`.
- The report still works after the list length changes.

## Stretch goal

Add `moveCompletedToEnd(ArrayList<String> tasks)` for tasks beginning with `DONE:`, preserving other task order.

## Reflection

Write why `remove(2)` and `remove(Integer.valueOf(2))` mean different things on `ArrayList<Integer>`. Optional focused drills: [Drill Bank](./drills.md).
