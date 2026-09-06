# Day 03 Lab — Build a Course Readiness Checker
# 第 3 天实验 —— 创建课程准备度检查器

## 🎯 Lab goal / 实验目标

Create a decision program that gives a learner one clear next action. Practice ordering conditions and correctly combining booleans.

创建一个决策程序，根据学习者的情况给出一个明确的下一步行动。练习**条件的优先顺序**以及正确组合布尔值。

**Today’s Java / 今天的 Java：**
- Boolean expressions / 布尔表达式
- `if` / `else if` / `else`
- `&&`
- `||`
- String `.equals()`

**Reuse from Days 01–02 / 复习第 1–2 天：**
- Typed variables / 类型化变量
- Arithmetic output / 算术运算输出
- `final` constants / `final` 常量
- Exact messages / 精确输出指定消息

---

## Mission / 任务

Create `ReadinessChecker.java`.

创建一个名为 `ReadinessChecker.java` 的 Java 文件。

It reads values already declared in `main`:

它会读取 `main` 中已经声明的变量：

```java
int completedLabs;
int averageScore;
boolean hasReviewedMistakes;
String goal;
```

Print exactly one readiness message according to this policy.

根据下面的规则，**每次运行只输出一条准备度消息**。

| Priority / 优先级 | Rule / 规则 | Message / 输出消息 |
|---|---|---|
| 1 | `averageScore` is below 60 / `averageScore` 小于 60 | `Review basics before moving on.` |
| 2 | `hasReviewedMistakes` is `false` / `hasReviewedMistakes` 为 `false` | `Review your mistakes, then retry.` |
| 3 | `completedLabs` is at least 3 **and** `goal` equals `"AP CSA"` / `completedLabs` 至少为 3，**并且** `goal` 等于 `"AP CSA"` | `Ready for AP CSA practice.` |
| 4 | Otherwise / 其他情况 | `Keep building your foundation.` |

### Important / 重要

The rules must be checked **in order**.

必须**按照优先级顺序**检查规则。

If the score is below 60, the first message must print even if all later rules are also true.

如果分数低于 60，即使后面的规则也满足，**仍然必须输出第一条消息**。

---

## Required cases / 必测情况

Test at least these values by changing variables and re-running.

至少通过修改变量并重新运行，测试下面四种情况。

### Case 1 / 情况 1

```java
averageScore = 55;
```

Other values positive / 其他值满足后面的条件。

**Expected output / 预期输出：**

```text
Review basics before moving on.
```

### Case 2 / 情况 2

```java
averageScore = 80;
hasReviewedMistakes = false;
```

**Expected output / 预期输出：**

```text
Review your mistakes, then retry.
```

### Case 3 / 情况 3

```java
averageScore = 80;
hasReviewedMistakes = true;
completedLabs = 3;
goal = "AP CSA";
```

**Expected output / 预期输出：**

```text
Ready for AP CSA practice.
```

### Case 4 / 情况 4

```java
averageScore = 80;
hasReviewedMistakes = true;
completedLabs = 2;
```

**Expected output / 预期输出：**

```text
Keep building your foundation.
```

---

## Starter code / 起始代码

```java
public class ReadinessChecker {
    public static void main(String[] args) {
        int completedLabs = 3;
        int averageScore = 80;
        boolean hasReviewedMistakes = true;
        String goal = "AP CSA";

        // TODO: write one ordered if / else if / else chain
        // TODO: 编写一个有顺序的 if / else if / else 条件链
    }
}
```

---

## Acceptance checks / 验收检查

- [x] Exactly one message prints per run.  
      每次运行只输出一条消息。

- [x] Use `goal.equals("AP CSA")`, not `goal == "AP CSA"`.  
      使用 `goal.equals("AP CSA")`，不要使用 `goal == "AP CSA"`。

- [x] The low-score rule wins even if all later rules are also true.  
      即使后面的规则也满足，低分规则仍然优先。

- [x] Use `&&` to combine the labs and goal conditions.  
      使用 `&&` 组合实验数量和目标条件。

---

## Stretch goal / 提高任务

Add an invalid-score check: if the score is outside 0–100, print `Invalid score.` before every other rule.

添加一个无效分数检查：如果分数不在 0–100 范围内，先输出 `Invalid score.`，再检查其他规则。

**Example / 示例：**

```java
if (averageScore < 0 || averageScore > 100) {
    System.out.println("Invalid score.");
} else if (averageScore < 60) {
    System.out.println("Review basics before moving on.");
}
```

Here, `||` means **OR / 或者**.

这里的 `||` 表示**或者**。

---

## Reflection / 反思

Add one mistake entry if you accidentally used `=` or `==` in a String condition.

如果你不小心在 String 条件中使用了 `=` 或 `==`，请记录一个错误。

### Mistake entry / 错误记录

- **Mistake / 错误：**
- **Why it was wrong / 为什么错误：**
- **Correct version / 正确写法：**
- **What I learned / 我学到了什么：**

### Example / 示例

```java
goal.equals("AP CSA")
```

Use `.equals()` to compare String values.

比较 String 的内容时，使用 `.equals()`。

---

## Optional focused drills / 可选专项练习

See the [Drill Bank](./drills.md).

查看 [Drill Bank](./drills.md)。
