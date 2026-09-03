# Day 02 Lab — Create a Study Session Receipt

## 🎯 Lab goal

Build a receipt that turns study-session data into a useful report. The program must make Java’s types visible: some values are whole numbers, some are decimal numbers, some are text, and some are true/false.

**Today’s Java:** `int`、`double`、`boolean`、`String`、arithmetic、`%`、integer versus decimal division、`final`.

**Reuse from Day 01:** a complete class/main shell, formatted console output, comments, and exact output checking.

## Mission

Create `StudyReceipt.java`. Model one study session with these variables:

- learner name (`String`)
- minutes studied (`int`)
- completed exercises (`int`)
- target exercises (`int`)
- snack cost (`double`)

Print a receipt that includes total minutes, whether the exercise target was met, the number of leftover minutes after converting to hours, and the average minutes per completed exercise.

## Required calculations

For a session of 95 minutes and 4 completed exercises, your program must show:

- `Hours: 1`
- `Minutes left: 35`
- `Average minutes per exercise: 23.75`

Use `/` and `%`; do not hardcode `1`, `35`, or `23.75`. Store `60` in a `final int MINUTES_PER_HOUR`.

## Start here

```java
public class StudyReceipt {
    public static void main(String[] args) {
        String learner = "Lin";
        int minutes = 95;
        int completed = 4;
        int target = 3;
        double snackCost = 2.50;

        // TODO: calculate and print the report
    }
}
```

## Acceptance checks

1. Changing `minutes` to 125 gives 2 hours and 5 minutes left.
2. The average is a decimal, not truncated by integer division.
3. Changing `completed` to 2 and `target` to 3 makes `Target met` false.
4. Every variable has a type suitable for its value.

## Stretch goal

Add a `double totalCost` that adds a fixed `double courseFee` to `snackCost`, then print it.

## Reflection

Write one sentence: why does `(double) minutes / completed` differ from `minutes / completed`? Use [Drill Bank](./drills.md) only after completing the Lab.
