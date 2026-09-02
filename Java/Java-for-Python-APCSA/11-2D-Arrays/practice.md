# Chapter 11 Practice — 2D Arrays

每一次访问都问自己：这是 row 还是 column？通用遍历的内层上界使用 `grid[row].length`。

## Level 1 — 5 problems

## Problem 11-01 🟢 Beginner — Create grid
创建 `{{1, 2}, {3, 4}}` 的 `int[][]`，打印右下角的值。

## Problem 11-02 🟢 Beginner — Dimensions
给定二维 array grid，打印行数与第 0 行列数。

## Problem 11-03 🟢 Beginner — All cells
用 nested loops 逐行打印二维 array 的每个元素。

## Problem 11-04 🟢 Beginner — Total
计算并打印 grid 中所有 int 的总和。

## Problem 11-05 🟢 Beginner — Count zeros
统计二维 array 中值为 0 的 cell 数量。

## Level 2 — 5 problems

## Problem 11-06 🟡 Intermediate — Row sums
每一行各打印一个总和。确保每行开始前将 sum 设回 0。

## Problem 11-07 🟡 Intermediate — Maximum
给定非空二维 array，返回/打印最大 cell。

## Problem 11-08 🟡 Intermediate — Replace negatives
把 grid 中每个负值改为 0，打印修改后的 grid。

## Problem 11-09 🟡 Intermediate — Diagonal sum
给定正方形矩阵，计算主对角线 `grid[i][i]` 总和。

## Problem 11-10 🟡 Intermediate — Row target
给定 grid 与 target，打印包含 target 的每一行 index；一行只打印一次。

## Level 3 — 3 problems

## Problem 11-11 🔴 Advanced — Column sums
给定矩形 grid，为每列计算一个总和。明确选择列作为外层或以 accumulator array 保存各列。

## Problem 11-12 🔴 Advanced — Neighbor pairs
统计每行中相邻、相等元素对的数量；不要比较每行最后一个元素与下一行第一个元素。

## Problem 11-13 🔴 Advanced — Jagged safe total
给定可能每行长度不同的 grid，写一个仍然安全的总和方法。

## AP CSA Style — 2 problems

## Problem 11-14 ⭐ AP CSA — Method writing
实现 `public static int countAbove(int[][] grid, int threshold)`，返回严格大于 threshold 的 cell 数量。

## Problem 11-15 ⭐ AP CSA — FRQ-style transform
实现 `public static void makeBorderZero(int[][] grid)`，将矩形 grid 的外边框全设为 0，内部保持不变。先处理/判断 top、bottom、left、right 边界。
