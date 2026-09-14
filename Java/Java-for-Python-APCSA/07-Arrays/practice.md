# Day 07 Lab — Build a Score Analyzer
# 第 07 天实验 — 构建成绩分析器

## 🎯 Lab goal / 实验目标

Use a fixed-size array to analyze test scores and produce a useful summary. The Lab combines methods, loops, conditionals, and today’s index-based array rules.

使用一个固定大小的数组来分析考试成绩，并生成一个有用的总结。本实验综合练习 **方法（methods）、循环（loops）、条件语句（conditionals）**，以及今天学习的**基于索引的数组规则**。

**Today’s Java / 今天的 Java：**
- `int[]` — 整数数组
- `.length` — 数组长度
- array indexing — 数组索引
- enhanced `for` — 增强型 for 循环 / for-each
- in-place array modification — 直接修改原数组

**Reuse from Days 01–06 / 复习第 01–06 天：**
- methods with return values — 有返回值的方法
- loop accumulators — 循环累加器
- thresholds — 阈值判断
- formatted reports — 格式化报告

---

## Mission / 任务

Create `ScoreAnalyzer.java`.

创建一个 `ScoreAnalyzer.java` 文件。

Start with / 从下面的数组开始：

```java
int[] scores = {88, 72, 95, 58, 88, 61};
```

Implement these methods / 实现以下方法：

```java
public static int highestScore(int[] scores)
public static int countPassing(int[] scores)
public static int firstScoreAtLeast(int[] scores, int target)
public static void addCurve(int[] scores, int points)
```

### Method meanings / 方法含义

| Method | English | 中文 |
|---|---|---|
| `highestScore` | Find the highest score. | 找出最高分。 |
| `countPassing` | Count scores that are at least 60. | 统计达到 60 分及以上的成绩数量。 |
| `firstScoreAtLeast` | Find the index of the first score that reaches the target. | 找到第一个达到目标分数的成绩的索引。 |
| `addCurve` | Add points to every score without going above 100. | 给每个成绩加分，但不能超过 100。 |

---

## Rules / 规则

- A passing score is at least 60.

  **及格分数是 60 分或以上。**

- `firstScoreAtLeast` returns `-1` if no score reaches target.

  **如果没有任何成绩达到目标分数，`firstScoreAtLeast` 必须返回 `-1`。**

- `addCurve` changes the original array, but no final score may exceed 100.

  **`addCurve` 必须修改原来的数组，而且加分后的成绩不能超过 100。**

- Use `scores.length`, never `scores.length()`.

  **使用 `scores.length`，不要写 `scores.length()`。**

> Remember / 注意：
>
> `length` 是数组的属性，不是方法，所以后面没有 `()`。

---

## Required report and tests / 必须完成的报告和测试

Before curving, print:

在加分之前，打印：

1. highest score — **最高分**
2. passing count — **及格人数/成绩数量**
3. first score at least 90 — **第一个达到 90 分的成绩的索引**

Then apply a 5-point curve.

然后给所有成绩加 **5 分**。

Finally, print the whole updated array.

最后打印更新后的整个数组。

For the provided data:

对于题目提供的数据：

```java
int[] scores = {88, 72, 95, 58, 88, 61};
```

The first score at least 90 is index `2`.

**第一个达到 90 分的成绩是 index `2`。**

After the curve, `95` becomes `100`, not `105`.

**加 5 分以后，95 应该变成 100，而不是 105。**

---

## Additional tests / 额外测试

Also test the following:

还需要测试下面这些情况：

### 1. One-element array / 只有一个元素的数组

```java
int[] scores = {59};
```

Think about:

思考：

- What is the highest score?
- 最高分是多少？
- How many scores are passing?
- 有几个及格？
- What should `firstScoreAtLeast(scores, 90)` return?
- `firstScoreAtLeast(scores, 90)` 应该返回什么？

---

### 2. No score reaches 90 / 没有成绩达到 90

Test an array where every score is below 90.

测试一个所有成绩都低于 90 的数组。

For example:

```java
int[] scores = {50, 60, 75, 89};
```

`firstScoreAtLeast(scores, 90)` should return:

```text
-1
```

---

### 3. Array already contains 100 / 数组中已经有 100

For example:

```java
int[] scores = {80, 100, 95};
```

After a 5-point curve:

加 5 分以后：

```text
85, 100, 100
```

The `100` must stay `100`.

**原本的 100 必须保持为 100。**

---

# Acceptance checks / 检查标准

### 1. Array traversal / 数组遍历

All traversal conditions use:

所有遍历数组的循环条件都应该使用：

```java
i < scores.length
```

Do not use:

```java
i <= scores.length
```

因为最后一个有效 index 是：

```java
scores.length - 1
```

---

### 2. Modify the original array / 修改原数组

`addCurve` must change the caller’s original array.

`addCurve` 必须修改调用它的那个原始数组。

For example:

```java
scores[i] += points;
```

is modifying the actual array element.

例如：

```java
scores[i] += points;
```

是在直接修改数组中的元素。

---

### 3. Maximum score / 最高分限制

No curved score can be greater than `100`.

加分后的任何成绩都不能大于 `100`。

A common approach is:

```java
scores[i] = Math.min(scores[i] + points, 100);
```

意思是：

> 取 `scores[i] + points` 和 `100` 中较小的那个。

---

### 4. No matching target / 没有符合目标的成绩

`firstScoreAtLeast` must return:

```java
-1
```

when no score satisfies the target.

当没有任何成绩达到目标时，必须返回：

```text
-1
```

---

# Stretch goal / 挑战任务

Implement:

```java
public static boolean hasConsecutiveDuplicates(int[] scores)
```

实现：

```java
public static boolean hasConsecutiveDuplicates(int[] scores)
```

The method should report whether adjacent equal scores exist.

这个方法应该判断数组中是否存在**相邻且相等的成绩**。

For example:

```java
int[] scores = {88, 72, 95, 58, 88, 61};
```

There are no consecutive duplicates.

这个数组没有相邻重复的成绩。

But:

```java
int[] scores = {88, 72, 72, 95};
```

has consecutive duplicates because the two `72`s are next to each other.

这个数组存在相邻重复，因为两个 `72` 紧挨着。

---

# Reflection / 思考题

Explain why this code does **not** curve the original array:

解释为什么下面的代码**不会**真正修改原数组：

```java
for (int score : scores) {
    score += 5;
}
```

### Hint / 提示

In an enhanced `for` loop:

在增强型 `for` 循环中：

```java
for (int score : scores)
```

`score` is a variable that receives a value from the array.

`score` 是一个变量，它接收到的是数组中的一个值。

Changing:

```java
score += 5;
```

only changes the local variable `score`.

修改：

```java
score += 5;
```

只会修改这个局部变量 `score`，不会修改数组里的元素。

To modify the original array, use the index:

如果想修改原数组，需要使用索引：

```java
for (int i = 0; i < scores.length; i++) {
    scores[i] += 5;
}
```

Here, `scores[i]` refers directly to an element inside the original array.

这里的 `scores[i]` 直接指向原数组中的一个元素。

---

## Quick vocabulary / 重点词汇

| English | 中文 |
|---|---|
| array | 数组 |
| index | 索引 |
| element | 元素 |
| length | 长度 |
| highest | 最高的 |
| passing score | 及格分数 |
| target | 目标 |
| curve | 加分 / 成绩调整 |
| original array | 原数组 |
| enhanced for loop | 增强型 for 循环 |
| consecutive | 连续的 / 相邻的 |
| duplicate | 重复项 |
| return | 返回 |
| threshold | 阈值 |

---

## Optional focused drills / 可选练习

See the Drill Bank:

查看 Drill Bank：

```text
./drills.md
```
