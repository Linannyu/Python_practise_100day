# Chapter 02 Practice — Variables & Data Types

每题在独立 `Main.java` 中完成。先自己预测表达式类型和值，再运行验证。

## Level 1 — 5 problems

## Problem 02-01 🟢 Beginner — Student data
声明 `String name`、`int age`、`double gpa`、`boolean enrolled`，赋合理值并逐行打印。

## Problem 02-02 🟢 Beginner — Character versus String
声明一个 `char` grade 为 A 和一个 `String` message 为 `Excellent`，打印两者。

## Problem 02-03 🟢 Beginner — Arithmetic
声明 `int a = 17`、`int b = 5`，打印 `+`、`-`、`*`、`/`、`%` 的五个结果，各一行。

## Problem 02-04 🟢 Beginner — Decimal division
让 Java 打印 `17 / 5` 的小数结果。保留 `a`、`b` 为 `int`，只改变表达式。

## Problem 02-05 🟢 Beginner — Boolean range
声明 `int score`，创建 `boolean passing` 表示 score 是否至少 60，并打印它。

## Level 2 — 5 problems

## Problem 02-06 🟡 Intermediate — Temperature conversion
声明整数华氏温度 `fahrenheit`，计算并打印摄氏温度 `double celsius = (fahrenheit - 32) * 5.0 / 9`。

## Problem 02-07 🟡 Intermediate — Even and positive
声明 `int n`，打印一个 boolean，只有当 n 为正偶数时才为 true。

## Problem 02-08 🟡 Intermediate — Power report
声明 `int base` 和 `int exponent`，用 `Math.pow` 打印结果，并解释（以注释写出）为什么结果是 double。

## Problem 02-09 🟡 Intermediate — Cast safely
声明 `double price = 8.99`，用 cast 存储其整数部分，再分别打印原价与整数部分。

## Problem 02-10 🟡 Intermediate — Final days
声明 `final int DAYS_IN_WEEK = 7`，用它计算 5 周有多少天并打印。不要直接写 35。

## Level 3 — 3 problems

## Problem 02-11 🔴 Advanced — Time breakdown
给出总秒数 `int seconds = 3671`，计算并打印小时、剩余分钟、剩余秒数（1、1、11）。使用 `/` 和 `%`。

## Problem 02-12 🔴 Advanced — Bounded value 🧪 Automated
实现 `public static int clamp(int value, int low, int high)`：小于 low 返回 low，大于 high 返回 high，否则返回 value。把类存为 `work/02-Variables-DataTypes/02-12/Main.java`，运行 `python3 run_tests.py 02-12`。

## Problem 02-13 🔴 Advanced — Invoice total
给出 `int quantity`、`double unitPrice` 和 `double discountRate`（如 0.10），计算折扣后的 total。打印一个有意义标签与数值。

## AP CSA Style — 2 problems

## Problem 02-14 ⭐ AP CSA — Trace types
不运行，预测：`double x = 7 / 2 + 0.5;` 中 x 的值。再写程序验证，并用注释解释顺序。

## Problem 02-15 ⭐ AP CSA — Correct declarations
下面每项各写一条**正确 Java 声明**：一个单字符 `Z`、一段文字 `Z`、值为 false 的 boolean、值为 2.75 的 double、值为 27 的 int。
