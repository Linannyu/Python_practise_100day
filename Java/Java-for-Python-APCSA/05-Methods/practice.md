# Day 05 Lab — Turn the Study Analyzer into a Toolkit
# 第 05 天实验 — 将学习分析器改造成工具包

## 🎯 Lab goal
## 🎯 实验目标

Refactor your Day 04 report into small methods with clear contracts. The Lab succeeds when `main` reads like a high-level plan rather than one long algorithm.

将第 04 天的报告重构成多个具有明确功能说明的小方法。当 `main` 看起来像一个高层次的计划，而不是一大段很长的算法时，就说明本实验成功了。

**Today’s Java:** method headers, parameters, arguments, return values, `void`, `static`.

**今天的 Java：**方法头、参数、实参、返回值、`void`、`static`。

**Reuse from Days 01–04:** arrays, loops, conditions, integer division awareness, formatted output.

**复习并使用第 01–04 天的知识：**数组、循环、条件语句、注意整数除法、格式化输出。

---

## Mission
## 任务

Create `StudyToolkit.java`. Use this data in `main`:

创建一个名为 `StudyToolkit.java` 的文件。在 `main` 中使用以下数据：

```java
int[] minutes = {35, 0, 50, 80, 20, 65, 40};
```

Implement all four methods below, then call them from `main` to print a report:

实现下面的四个方法，然后在 `main` 中调用它们来打印报告：

```java
public static int totalMinutes(int[] values)
public static int countStrongDays(int[] values, int minimum)
public static double averageMinutes(int[] values)
public static int firstDayAtLeast(int[] values, int minimum)
```

---

## Method contracts
## 方法功能说明

### `totalMinutes`

**English:** Returns the sum.

**中文：**返回所有数值的总和。

### `countStrongDays`

**English:** Returns how many values are at least `minimum`.

**中文：**返回有多少个数值大于或等于 `minimum`。

### `averageMinutes`

**English:** Returns a `double`; assume the array is nonempty.

**中文：**返回一个 `double` 类型的平均值；假设数组不为空。

### `firstDayAtLeast`

**English:** Returns the first matching index, otherwise `-1`.

**中文：**返回第一个符合条件的元素的索引；如果没有找到，返回 `-1`。

---

## Required tests in `main`
## `main` 中必须完成的测试

Test the original array, `{0, 0}`, and `{60}`.

测试原始数组、`{0, 0}` 和 `{60}`。

For `{60}`, the total is 60, strong-day count at 60 is 1, average is 60.0, and first matching index is 0.

对于 `{60}`：

- Total / 总和：`60`
- Strong-day count at 60 / minimum 为 60 时的达标天数：`1`
- Average / 平均值：`60.0`
- First matching index / 第一个符合条件的索引：`0`

---

## Acceptance checks
## 验收标准

1. Each of the four required methods has the exact stated header.  
   四个要求的方法都必须使用上面完全一致的方法头。

2. Returning methods use `return`; they do not print the result themselves.  
   有返回值的方法必须使用 `return`，不能在方法内部自己打印结果。

3. `firstDayAtLeast(new int[] {0, 0}, 60)` returns `-1`.  
   `firstDayAtLeast(new int[] {0, 0}, 60)` 必须返回 `-1`。

4. `averageMinutes(new int[] {60})` returns `60.0`, not an int.  
   `averageMinutes(new int[] {60})` 必须返回 `60.0`，而不是整数类型的结果。

---

## Design rules
## 设计规则

- Do not print from the three returning methods.  
  不要在三个有返回值的方法中打印结果。

- Do not duplicate loop logic in `main`.  
  不要在 `main` 中重复编写循环逻辑。

- Keep the method headers exactly as written.  
  方法头必须与题目中写的一模一样。

- Add a short comment above each method describing its return value.  
  在每个方法上方添加一条简短注释，说明该方法返回什么。

---

## Stretch goal
## 提高挑战

Add:

添加：

```java
public static boolean metWeeklyGoal(int[] values, int goal)
```

and use it in the report.

并在报告中调用这个方法。

**English:** This method should return whether the total minutes meet or exceed the weekly goal.

**中文：**这个方法应该返回学习总分钟数是否达到或超过每周目标。

---

## Automated method habit
## 自动化测试习惯

The course tester has a fixed-signature example for this chapter: [Problem 05-12 in Drill Bank](./drills.md).

本章的课程测试器中有一个固定方法签名的例子：[Drill Bank 中的 Problem 05-12](./drills.md)。

You can run it after creating its separate `work/` file; this Lab itself should be tested through the cases above.

创建单独的 `work/` 文件后，你可以运行这个测试器；本实验本身应该使用上面列出的测试案例进行测试。

---

## Reflection
## 反思

Which logic belongs in a method versus in `main`?

哪些逻辑应该放在方法中，哪些逻辑应该放在 `main` 中？

Write one answer in [mistakes.md](../mistakes.md) if you made a return/print mix-up.

如果你把 `return` 和 `print` 混淆了，请在 [mistakes.md](../mistakes.md) 中写下一个反思答案。

### Helpful reflection idea / 反思提示

**English:** Reusable calculations belong in methods. The `main` method should mainly organize the program, call methods, and print the final report.

**中文：**可以重复使用的计算逻辑应该放在方法中。`main` 主要负责组织程序、调用方法，以及打印最终报告。
