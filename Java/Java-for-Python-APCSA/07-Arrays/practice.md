# Chapter 07 Practice — Arrays

默认 array 非 null；题目若未特别说明，先考虑空 array 是否需要处理。修改 array 时用 index loop。

## Level 1 — 5 problems

## Problem 07-01 🟢 Beginner — Create and print
创建 `{2, 4, 6, 8}` 的 int array，用循环打印每项。

## Problem 07-02 🟢 Beginner — Length and endpoints
给定非空 array，打印长度、第一个值和最后一个值。

## Problem 07-03 🟢 Beginner — Sum
给定 int array，计算并打印所有元素总和。

## Problem 07-04 🟢 Beginner — Count positive
给定 int array，打印正数元素的数量。

## Problem 07-05 🟢 Beginner — Add one
给定 int array，把每个元素加一，然后打印修改后的 array。

## Level 2 — 5 problems

## Problem 07-06 🟡 Intermediate — Maximum
给定非空 int array，打印最大元素，不得排序。

## Problem 07-07 🟡 Intermediate — First index
给定 int array 与 target，打印 target 首次出现下标；若缺失打印 -1。

## Problem 07-08 🟡 Intermediate — Reverse print
给定 int array，以反向顺序打印元素，但不要修改原 array。

## Problem 07-09 🟡 Intermediate — Swap endpoints
给定长度至少 2 的 array，交换第一个和最后一个元素，随后打印。

## Problem 07-10 🟡 Intermediate — Average above
给定非空 array，计算其 `double` 平均值，打印大于平均值的元素。

## Level 3 — 3 problems

## Problem 07-11 🔴 Advanced — Second largest distinct
给定至少两个不同值的 array，打印第二大的**不同**值；不得排序。

## Problem 07-12 🔴 Advanced — Adjacent increase
给定 array，统计满足 `arr[i] < arr[i + 1]` 的相邻对数量。

## Problem 07-13 🔴 Advanced — Replace negatives
给定 int array，把所有负数替换为 0，并返回/打印替换数量。

## AP CSA Style — 2 problems

## Problem 07-14 ⭐ AP CSA — Method writing 🧪 Automated
实现 `public static int sumPositive(int[] values)`，只返回大于 0 的元素总和。测试：`python3 run_tests.py 07-14`。

## Problem 07-15 ⭐ AP CSA — Array traversal FRQ
实现 `public static boolean hasConsecutiveDuplicates(int[] values)`，若任意相邻元素相等返回 true，否则 false。
