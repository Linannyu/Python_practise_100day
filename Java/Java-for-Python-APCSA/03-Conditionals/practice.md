# Chapter 03 Practice — Conditionals

所有分支写 `{ }`，即使暂时只有一行。先想清楚每个边界值该落在哪一支。

## Level 1 — 5 problems

## Problem 03-01 🟢 Beginner — Sign
给定 `int n`，打印 `positive`、`negative` 或 `zero`。

## Problem 03-02 🟢 Beginner — Even label
给定 `int n`，打印 `even` 或 `odd`。

## Problem 03-03 🟢 Beginner — Pass or retry
给定 `int score`，若至少 60 打印 `pass`，否则打印 `retry`。

## Problem 03-04 🟢 Beginner — Teenager
给定 `int age`，打印 boolean：年龄是否在 13 到 19（含）之间。

## Problem 03-05 🟢 Beginner — Exact word
给定 `String answer`，若内容为 `yes` 打印 `accepted`，否则打印 `not accepted`。必须正确比较 String。

## Level 2 — 5 problems

## Problem 03-06 🟡 Intermediate — Letter grade
给定 score，打印 A（90+）、B（80–89）、C（70–79）、D（60–69）或 F。确保条件顺序正确。

## Problem 03-07 🟡 Intermediate — Ticket price
给定 age：小于 5 价格 0；5–12 价格 8；65+ 价格 9；其余价格 12。打印价格。

## Problem 03-08 🟡 Intermediate — Valid rectangle
给定 `int width` 和 `int height`，只有两者都大于 0 才打印 `valid`，否则打印 `invalid`。

## Problem 03-09 🟡 Intermediate — Largest of two
给定两个不同整数，打印较大者。不得使用 `Math.max`。

## Problem 03-10 🟡 Intermediate — Password gate
给定 `String password`，只有内容等于 `java123` 时打印 `welcome`。不要使用 `==`。

## Level 3 — 3 problems

## Problem 03-11 🔴 Advanced — Median of three
给定三个互不相同的 int，打印中间大小的数。不得排序或使用 array。

## Problem 03-12 🔴 Advanced — Leap year rule
给定 year：能被 400 整除，或能被 4 整除但不能被 100 整除时，打印 `leap`；否则 `common`。

## Problem 03-13 🔴 Advanced — Shipping
给定 subtotal 和 boolean member：subtotal 至少 50 或 member 为 true 时免邮；否则运费 6.99。打印最终运费。

## AP CSA Style — 2 problems

## Problem 03-14 ⭐ AP CSA — Method writing
实现 `public static String season(int month)`：12、1、2 为 `winter`；3–5 为 `spring`；6–8 为 `summer`；9–11 为 `fall`；其他返回 `invalid`。

## Problem 03-15 ⭐ AP CSA — Code trace
不运行，追踪 `int x = 8; if (x > 5) { if (x < 8) x++; else x--; }` 的最终 x。再把它写成完整程序验证。
