# Day 03 Lab — Build a Course Readiness Checker

## 🎯 Lab goal

Create a decision program that gives a learner one clear next action. Practice ordering conditions and correctly combining booleans.

**Today’s Java:** boolean expressions, `if` / `else if` / `else`, `&&`, `||`, String `.equals()`.

**Reuse from Days 01–02:** typed variables, arithmetic output, `final` constants, and exact messages.

## Mission

Create `ReadinessChecker.java`. It reads values already declared in `main`:

- `int completedLabs`
- `int averageScore`
- `boolean hasReviewedMistakes`
- `String goal`

Print exactly one readiness message according to this policy:

| Priority | Rule | Message |
|---|---|---|
| 1 | averageScore is below 60 | `Review basics before moving on.` |
| 2 | reviewed mistakes is false | `Review your mistakes, then retry.` |
| 3 | completedLabs is at least 3 and goal equals `AP CSA` | `Ready for AP CSA practice.` |
| 4 | otherwise | `Keep building your foundation.` |

## Required cases

Test at least these values by changing variables and re-running:

1. `averageScore = 55`, other values positive → first message.
2. `averageScore = 80`, `hasReviewedMistakes = false` → second message.
3. score 80, reviewed true, labs 3, goal `AP CSA` → third message.
4. score 80, reviewed true, labs 2 → fourth message.

## Starter code

```java
public class ReadinessChecker {
    public static void main(String[] args) {
        int completedLabs = 3;
        int averageScore = 80;
        boolean hasReviewedMistakes = true;
        String goal = "AP CSA";

        // TODO: write one ordered if / else if / else chain
    }
}
```

## Acceptance checks

- Exactly one message prints per run.
- Use `goal.equals("AP CSA")`, not `goal == "AP CSA"`.
- The low-score rule wins even if all later rules are also true.

## Stretch goal

Add an invalid-score check: if score is outside 0–100, print `Invalid score.` before every other rule.

## Reflection

Add one mistake entry if you accidentally used `=` or `==` in a String condition. Optional focused drills: [Drill Bank](./drills.md).
