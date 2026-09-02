# Chapter 04 Practice — Loops

对每一题先说出循环的初始化、条件和更新。除非题目明确要求，否则不要硬编码答案。

## Level 1 — 5 problems

## Problem 04-01 🟢 Beginner — Zero to four
用 `for` 打印 0 到 4，每个一行。

## Problem 04-02 🟢 Beginner — Countdown
用 `while` 打印 5 到 1。

## Problem 04-03 🟢 Beginner — Even numbers
打印 2 到 20（含）的偶数；使用适当 update，不要在每轮都用 if。

## Problem 04-04 🟢 Beginner — Sum to n
给定 `int n`，用循环打印 1 到 n 的总和。

## Problem 04-05 🟢 Beginner — Repeated word
给定 `String word` 和 `int times`，打印 word 共 times 行。

## Level 2 — 5 problems

## Problem 04-06 🟡 Intermediate — Count multiples
给定 n，统计 1 到 n（含）中 3 的倍数数量并打印。

## Problem 04-07 🟡 Intermediate — Digit sum
给定正整数 n，用 `% 10` 与 `/ 10` 计算各位数字之和。例如 407 → 11。

## Problem 04-08 🟡 Intermediate — First multiple
从 1 开始找第一个同时是 7 和 9 倍数的数，打印并用 `break` 结束。

## Problem 04-09 🟡 Intermediate — Skip negatives
给定 `int[] values`，用 enhanced for 打印所有非负值；负数用 `continue` 跳过。

## Problem 04-10 🟡 Intermediate — Product
给定 n，计算 n! 的**循环**版本（n 为非负），并打印结果。

## Level 3 — 3 problems

## Problem 04-11 🔴 Advanced — Count digits
给定非负 n，打印其数字个数；特别正确处理 n 为 0。

## Problem 04-12 🔴 Advanced — Largest even
给定非空 `int[] values`，打印其中最大的偶数；若没有偶数，打印 `none`。

## Problem 04-13 🔴 Advanced — Number pattern
用 nested loops 打印：第一行 `1`，第二行 `1 2`，直到第五行 `1 2 3 4 5`。空格格式一致。

## AP CSA Style — 2 problems

## Problem 04-14 ⭐ AP CSA — Method writing
实现 `public static int sumOdd(int n)`，返回 1 到 n（含）所有奇数之和。若 n 小于 1 返回 0。

## Problem 04-15 ⭐ AP CSA — Trace and repair
解释为何 `for (int i = 0; i <= values.length; i++)` 有 bug；写正确循环并打印 array 每个元素。
