# Day 09 Lab — Model a Study Task as an Object

## 🎯 Lab goal

Move from “parallel variables” to objects that own their own state and behavior. This Lab turns the Day 08 planner into a collection of `StudyTask` objects.

**Today’s Java:** fields, constructor, `this`, instance methods, getters, setters, `private`, `public`, `new`, `static`.

**Reuse from Days 01–08:** String methods, ArrayList, conditions, loops, status reporting.

## Mission

Create `StudyTaskApp.java` containing a `public class StudyTaskApp` and a non-public `StudyTask` class in the same file.

`StudyTask` must have:

```java
private String title;
private int estimatedMinutes;
private boolean complete;

public StudyTask(String title, int estimatedMinutes)
public String getTitle()
public int getEstimatedMinutes()
public boolean isComplete()
public void markComplete()
public void updateEstimate(int minutes)
public String toString()
```

## Behavior rules

- A new task starts incomplete.
- `updateEstimate` changes the estimate only when minutes is positive.
- `toString` returns a readable line such as `[TODO] Read Arrays (25 min)` or `[DONE] Read Arrays (25 min)`.
- Keep fields private; `main` may not write `task.complete = true`.

## Required app behavior

In `main`, put at least three `StudyTask` objects in an `ArrayList<StudyTask>`. Mark one complete. Use an enhanced for loop to print all tasks and count the remaining estimated minutes of incomplete tasks.

## Acceptance checks

1. A negative `updateEstimate(-5)` leaves the old value unchanged.
2. Calling `markComplete()` changes only that object.
3. Two tasks with different titles print different state lines.
4. Your application does not use parallel `ArrayList<String>` / `ArrayList<Integer>` lists.

## Stretch goal

Add a `private static int createdCount` field to `StudyTask` and a public static getter. Explain why this is static rather than an instance field.

## Reflection

Write a short comparison: Python’s `self.title = title` versus Java’s `this.title = title`. Optional focused drills: [Drill Bank](./drills.md).
