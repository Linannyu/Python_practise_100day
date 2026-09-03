# Day 10 Lab — Add Specialized Study Tasks

## 🎯 Lab goal

Extend yesterday’s object model rather than rewrite it. Use inheritance to give different kinds of study tasks shared data plus specialized behavior.

**Today’s Java:** `extends`, superclass, subclass, `super(...)`, method overriding, `@Override`, polymorphism.

**Reuse from Days 01–09:** classes, private fields, constructors, ArrayList, loops, String reports.

## Mission

Create `TaskHierarchyApp.java` with this class design:

```text
StudyTask
├── CodingTask
└── ReadingTask
```

`StudyTask` stores `title`, `estimatedMinutes`, and completion state. It provides `markComplete()`, `isComplete()`, and `getEstimatedMinutes()`.

- `CodingTask` adds `String language`.
- `ReadingTask` adds `int pages`.
- Both subclasses override `getDescription()`.

## Required behavior

1. Each subclass constructor calls `super(title, estimatedMinutes)`.
2. `CodingTask.getDescription()` returns a line containing its title and language.
3. `ReadingTask.getDescription()` returns a line containing its title and page count.
4. In `main`, store one of each subclass in `ArrayList<StudyTask>`.
5. Loop over the parent-type list and print `getDescription()` for every object.

## Required test

Create a coding task for Java and a reading task for AP CSA. Mark only one complete. Print descriptions and completion state. Confirm that the subclass version of `getDescription()` runs even though your loop variable has type `StudyTask`.

## Acceptance checks

- No duplicated title/minutes/complete fields in subclasses.
- `@Override` compiles on both subclass methods.
- You can explain why `StudyTask task = new CodingTask(...)` is valid.

## Stretch goal

Add `QuizTask extends StudyTask` with a question count and a different description. Do not change the printing loop.

## Reflection

In [mistakes.md](../mistakes.md), explain in one sentence the difference between the reference type (`StudyTask`) and actual object type (`CodingTask`). Optional focused drills: [Drill Bank](./drills.md).
