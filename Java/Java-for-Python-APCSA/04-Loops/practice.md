# Day 04 Lab — Analyze a Week of Study Minutes
# 第 04 天实验 —— 分析一周的学习分钟数

## 🎯 Lab goal / 实验目标

Use loops to transform a sequence of daily study values into a report.  
使用循环，把每天的学习时间转换成一份报告。

This is the first Lab where you repeatedly apply earlier conditionals inside iteration.  
这是第一次在循环中反复使用之前学过的条件判断。

**Today’s Java / 今天的 Java：**

- `for` loop / `for` 循环
- `while` loop / `while` 循环
- enhanced `for` loop / 增强型 `for` 循环
- accumulators / 累加器
- counters / 计数器
- `break`
- loop bounds / 循环边界

**Reuse from Days 01–03 / 复习第 01–03 天：**

- variables / 变量
- integer and decimal division / 整数除法与小数除法
- boolean conditions / 布尔条件
- clean report formatting / 整洁的报告格式

---

## Mission / 任务

Create a file named `StudyWeekAnalyzer.java`.  
创建一个名为 `StudyWeekAnalyzer.java` 的文件。

Begin with this array:  
从下面这个数组开始：

```java
int[] minutes = {35, 0, 50, 80, 20, 65, 40};
```

Using loops, print a report containing:  
使用循环，打印包含以下内容的报告：

1. **Total minutes** / 总分钟数
2. **Number of active days** / 活跃天数，也就是学习时间大于 `0` 的天数
3. **Number of strong days** / 高强度学习天数，也就是学习时间至少为 `60` 的天数
4. **Exact daily average as a `double`** / 使用 `double` 计算精确的每日平均学习时间
5. **First day index with at least 60 minutes, or `-1` if none** / 第一个学习时间至少为 `60` 分钟的日期索引；如果没有，返回 `-1`

---

## Rules / 规则

- Use an enhanced `for` loop at least once for total/counting.  
  至少使用一次增强型 `for` 循环来计算总数或进行计数。

- Use an index-based `for` loop to find the first strong day, then `break`.  
  使用带索引的 `for` 循环寻找第一个高强度学习日，然后使用 `break`。

- Do not use a hardcoded number for the array length.  
  不要把数组长度写死成某个数字。

- Avoid `i <= minutes.length`.  
  不要使用 `i <= minutes.length`。

Use this instead:

```java
i < minutes.length
```

**Why? / 为什么？**

Array indexes start at `0`, so the last valid index is `minutes.length - 1`.  
数组索引从 `0` 开始，所以最后一个有效索引是 `minutes.length - 1`。

---

## Expected result / 预期结果

For the provided data, your program should print:

```text
Total: 290
Active days: 6
Strong days: 2
Average: 41.42857142857143
First strong day index: 3
```

---

## Suggested solution / 参考代码

```java
public class StudyWeekAnalyzer {
    public static void main(String[] args) {
        int[] minutes = {35, 0, 50, 80, 20, 65, 40};

        int total = 0;
        int activeDays = 0;
        int strongDays = 0;

        // Enhanced for loop:
        // Use each value directly instead of using an index.
        // 增强型 for 循环：
        // 直接使用每个值，不需要手动使用索引。
        for (int minute : minutes) {
            total += minute;

            if (minute > 0) {
                activeDays++;
            }

            if (minute >= 60) {
                strongDays++;
            }
        }

        // Cast total to double so the division is exact.
        // 将 total 转换成 double，确保进行小数除法。
        double average = (double) total / minutes.length;

        int firstStrongDayIndex = -1;

        // Index-based for loop:
        // i represents the current array index.
        // 带索引的 for 循环：
        // i 表示当前数组索引。
        for (int i = 0; i < minutes.length; i++) {
            if (minutes[i] >= 60) {
                firstStrongDayIndex = i;
                break;
            }
        }

        System.out.println("Total: " + total);
        System.out.println("Active days: " + activeDays);
        System.out.println("Strong days: " + strongDays);
        System.out.println("Average: " + average);
        System.out.println("First strong day index: " + firstStrongDayIndex);
    }
}
```

---

## Code explanation / 代码解释

### 1. The array / 数组

```java
int[] minutes = {35, 0, 50, 80, 20, 65, 40};
```

This stores seven daily study values.  
这个数组存储了七天的学习时间。

| Index / 索引 | Minutes / 分钟 |
|---:|---:|
| 0 | 35 |
| 1 | 0 |
| 2 | 50 |
| 3 | 80 |
| 4 | 20 |
| 5 | 65 |
| 6 | 40 |

The value `80` is at index `3`, so the first strong day index is `3`.  
`80` 位于索引 `3`，所以第一个高强度学习日的索引是 `3`。

---

### 2. Accumulators / 累加器

```java
int total = 0;
```

`total` starts at `0` and keeps adding each day's minutes.  
`total` 从 `0` 开始，每次加上当天的学习分钟数。

Example / 示例：

```text
0 + 35 + 0 + 50 + 80 + 20 + 65 + 40 = 290
```

---

### 3. Counters / 计数器

```java
int activeDays = 0;
int strongDays = 0;
```

These variables count how many days satisfy each condition.  
这些变量用来统计满足条件的天数。

```java
if (minute > 0) {
    activeDays++;
}
```

This counts days with more than `0` minutes.  
这会统计学习时间大于 `0` 分钟的天数。

```java
if (minute >= 60) {
    strongDays++;
}
```

This counts days with at least `60` minutes.  
这会统计学习时间至少为 `60` 分钟的天数。

---

### 4. Enhanced `for` loop / 增强型 for 循环

```java
for (int minute : minutes) {
    // ...
}
```

Read this as:

> For each `minute` value inside `minutes`...  
> 对于 `minutes` 中的每一个 `minute` 值……

You do not need to write an index.  
你不需要手动写索引。

For example, the loop receives these values one by one:

```text
35
0
50
80
20
65
40
```

---

### 5. Exact average / 精确平均值

```java
double average = (double) total / minutes.length;
```

The total is `290`, and the array length is `7`.

```text
290 / 7 = 41.42857142857143
```

If both sides are integers, Java performs integer division:

```java
int result = 290 / 7;
System.out.println(result);
```

Output:

```text
41
```

But we want the decimal result. Therefore, convert one side to `double`:

```java
double average = (double) 290 / 7;
```

Output:

```text
41.42857142857143
```

**Important / 重点：**

You can cast either side:

```java
(double) total / minutes.length
```

or:

```java
total / (double) minutes.length
```

Both produce an exact decimal average.

---

### 6. Finding the first strong day / 寻找第一个高强度学习日

```java
int firstStrongDayIndex = -1;
```

We start with `-1` because it means:

> No strong day has been found yet.  
> 目前还没有找到高强度学习日。

Then we check the array from left to right:

```java
for (int i = 0; i < minutes.length; i++) {
    if (minutes[i] >= 60) {
        firstStrongDayIndex = i;
        break;
    }
}
```

The loop checks:

```text
Index 0 → 35 → not strong
Index 1 → 0  → not strong
Index 2 → 50 → not strong
Index 3 → 80 → strong
```

At index `3`, the condition is true:

```java
firstStrongDayIndex = 3;
```

Then:

```java
break;
```

stops the loop immediately.

**Why use `break`? / 为什么使用 `break`？**

Because we only need the **first** strong day, not every strong day.  
因为我们只需要找到**第一个**高强度学习日，而不是所有高强度学习日。

---

## Acceptance checks / 验收检查

### Check 1: All values are zero / 检查 1：所有值都为 0

Change the array to:

```java
int[] minutes = {0, 0, 0, 0, 0, 0, 0};
```

Expected important result:

```text
Total: 0
Active days: 0
Strong days: 0
Average: 0.0
First strong day index: -1
```

Why is the index `-1`?  
为什么索引是 `-1`？

Because no value is at least `60`.  
因为没有任何一个值达到 `60`。

---

### Check 2: First value is 60 / 检查 2：第一个值为 60

Change the array to:

```java
int[] minutes = {60, 0, 0, 0, 0, 0, 0};
```

Expected important result:

```text
First strong day index: 0
```

The first value is at index `0`.  
第一个值位于索引 `0`。

---

### Check 3: Explain the cast / 检查 3：解释类型转换

Answer this question:

> Why must `total` or `minutes.length` be cast to `double` for an exact average?  
> 为什么要把 `total` 或 `minutes.length` 转换成 `double`，才能得到精确的平均值？

Suggested answer / 参考答案：

> Because `total` and `minutes.length` are integers. If both operands are integers, Java performs integer division and removes the decimal part. Casting one operand to `double` makes Java perform decimal division.

中文：

> 因为 `total` 和 `minutes.length` 都是整数。如果两个操作数都是整数，Java 会执行整数除法并去掉小数部分。把其中一个操作数转换成 `double`，Java 就会执行小数除法。

---

## Stretch goal / 拓展目标

Print each active day like this:

```text
Day 0: 35
Day 2: 50
Day 3: 80
Day 4: 20
Day 5: 65
Day 6: 40
```

Skip inactive days with `continue`.  
使用 `continue` 跳过不活跃的日期。

Example / 示例：

```java
for (int i = 0; i < minutes.length; i++) {
    if (minutes[i] == 0) {
        continue;
    }

    System.out.println("Day " + i + ": " + minutes[i]);
}
```

### How `continue` works / `continue` 的作用

When the value is `0`, `continue` skips the rest of the current iteration and moves to the next iteration.  
当值为 `0` 时，`continue` 会跳过本次循环剩余的代码，直接进入下一次循环。

---

## Reflection / 反思

For this Lab, record the meaning of `i` at the start of every indexed-loop iteration.  
在本次实验中，记录每次带索引循环开始时 `i` 的含义。

For this loop:

```java
for (int i = 0; i < minutes.length; i++) {
    // ...
}
```

Write a reflection table like this:

| Iteration / 循环次数 | Value of `i` / `i` 的值 | Meaning of `i` / `i` 的含义 |
|---:|---:|---|
| 1 | 0 | `i` is the index of the first day. / `i` 是第一天的索引。 |
| 2 | 1 | `i` is the index of the second day. / `i` 是第二天的索引。 |
| 3 | 2 | `i` is the index of the third day. / `i` 是第三天的索引。 |
| 4 | 3 | `i` is the index of the fourth day. / `i` 是第四天的索引。 |

For the first-strong-day loop, explain:

> At the start of each iteration, `i` represents the current array index being checked.  
> 每次循环开始时，`i` 表示当前正在检查的数组索引。

---

## Optional focused drills / 可选专项练习

See the Drill Bank: `./drills.md`  
请查看练习题库：`./drills.md`

Possible practice questions / 练习问题：

1. What is the difference between `for` and enhanced `for`?  
   普通 `for` 和增强型 `for` 有什么区别？

2. Why does array indexing start at `0`?  
   为什么数组索引从 `0` 开始？

3. What happens if you use `i <= minutes.length`?  
   如果使用 `i <= minutes.length` 会发生什么？

4. What is the purpose of an accumulator?  
   累加器的作用是什么？

5. What is the difference between `break` and `continue`?  
   `break` 和 `continue` 有什么区别？

6. Why is `-1` useful when searching for an index?  
   在查找索引时，为什么 `-1` 很有用？
