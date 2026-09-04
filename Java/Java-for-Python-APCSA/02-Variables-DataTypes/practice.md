# Day 02 Lab --- Create a Study Session Receipt

# 第二天实验 --- 创建学习记录收据

## 🎯 Lab goal / 实验目标

Build a receipt that turns study-session data into a useful report. The
program must make Java's types visible: some values are whole numbers,
some are decimal numbers, some are text, and some are true/false.

创建一个收据程序，将学习记录数据转换成一份有用的报告。程序必须体现 Java
的不同数据类型：有些值是整数，有些是小数，有些是文本，还有些是真/假值。

**Today's Java / 今天的 Java：**
`int`、`double`、`boolean`、`String`、arithmetic（算术运算）、`%`、integer
versus decimal division（整数除法与小数除法）、`final`。

**Reuse from Day 01 / 复用第一天内容：** a complete class/main
shell（完整的 class/main 结构）、formatted console
output（格式化控制台输出）、comments（注释）、and exact output
checking（精确输出检查）。

## Mission / 任务

Create `StudyReceipt.java`. Model one study session with these
variables:

创建 `StudyReceipt.java`。使用以下变量表示一次学习记录：

-   learner name (`String`) --- 学习者姓名（`String`）
-   minutes studied (`int`) --- 学习分钟数（`int`）
-   completed exercises (`int`) --- 已完成的练习数量（`int`）
-   target exercises (`int`) --- 目标练习数量（`int`）
-   snack cost (`double`) --- 零食费用（`double`）

Print a receipt that includes total minutes, whether the exercise target
was met, the number of leftover minutes after converting to hours, and
the average minutes per completed exercise.

打印一份收据，包含总学习分钟数、是否达到练习目标、转换成小时后剩余的分钟数，以及每道已完成练习的平均用时。

## Required calculations / 必须完成的计算

For a session of 95 minutes and 4 completed exercises, your program must
show:

对于学习 95 分钟、完成 4 道练习的情况，程序必须显示：

-   `Hours: 1` --- 小时：1
-   `Minutes left: 35` --- 剩余分钟：35
-   `Average minutes per exercise: 23.75` --- 每道练习平均分钟数：23.75

Use `/` and `%`; do not hardcode `1`, `35`, or `23.75`. Store `60` in a
`final int MINUTES_PER_HOUR`.

使用 `/` 和 `%`；不要直接写死 `1`、`35` 或 `23.75`。将 `60` 存储在
`final int MINUTES_PER_HOUR` 中。

## Start here / 从这里开始

``` java
public class StudyReceipt {
    public static void main(String[] args) {
        String learner = "Lin";
        int minutes = 95;
        int completed = 4;
        int target = 3;
        double snackCost = 2.50;

        // TODO: calculate and print the report
        // TODO：计算并打印报告
    }
}
```

## Acceptance checks / 验收检查

1.  Changing `minutes` to 125 gives 2 hours and 5 minutes left.

    将 `minutes` 改为 125 后，应得到 2 小时和 5 分钟剩余。

2.  The average is a decimal, not truncated by integer division.

    平均值必须是小数，不能被整数除法截断。

3.  Changing `completed` to 2 and `target` to 3 makes `Target met`
    false.

    将 `completed` 改为 2、`target` 改为 3 后，`Target met` 应为
    `false`。

4.  Every variable has a type suitable for its value.

    每个变量都必须使用适合其值的数据类型。

## Stretch goal / 拓展目标

Add a `double totalCost` that adds a fixed `double courseFee` to
`snackCost`, then print it.

添加一个 `double totalCost`，将固定的 `double courseFee` 加到
`snackCost` 上，然后打印总费用。

## Reflection / 反思

Write one sentence: why does `(double) minutes / completed` differ from
`minutes / completed`? Use [Drill Bank](./drills.md) only after
completing the Lab.

写一句话：为什么 `(double) minutes / completed` 与 `minutes / completed`
的结果不同？完成实验后才能使用 [Drill Bank](./drills.md)。
