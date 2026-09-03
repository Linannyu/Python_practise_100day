# Chapter 13 Practice — AP CSA Review

这一章组合前面知识。做题时像 FRQ 一样：先写方法签名，再设计变量与边界测试，最后测试和记录错题。

## Level 1 — 5 problems

## Problem 13-01 🟢 Beginner — Length triad
写小程序，分别打印 String、int array、ArrayList 的长度，使用各自正确语法。

## Problem 13-02 🟢 Beginner — Average precisely
实现 `average(int[] values)`，返回 double 平均数。假设非空。

## Problem 13-03 🟢 Beginner — Safe String match
实现 `isJava(String language)`，在 language 为 null 时返回 false，否则判断内容是否为 `Java`。

## Problem 13-04 🟢 Beginner — Random die
用 `Random` 创建并打印 1–6 的骰子值；解释为何两端都正确。

## Problem 13-05 🟢 Beginner — Bug labels
为下列错误各写一行注释分类：缺少分号、array 越界、输出错误答案。使用 compile/runtime/logic 三种标签。

## Level 2 — 5 problems

## Problem 13-06 🟡 Intermediate — Positive average
实现 `averagePositive(int[] values)`：只平均正数；没有正数时返回 0.0。

## Problem 13-07 🟡 Intermediate — Student pass list
给定 `ArrayList<Student>`（可自己定义简单 Student），返回及格学生数量。

## Problem 13-08 🟡 Intermediate — Grid row max
实现 `rowMax(int[][] grid, int row)`，返回指定非空行的最大值。

## Problem 13-09 🟡 Intermediate — Word score
实现 `wordScore(String word)`：每个元音 2 分、其他字符 1 分。

## Problem 13-10 🟡 Intermediate — Debug a loop
给出/写一个原本使用 `i <= list.size()` 的 ArrayList 遍历，修正它并解释正确上界。

## Level 3 — 3 problems

## Problem 13-11 🔴 Advanced — Most frequent value
给定 int array，返回出现次数最多的值；若并列，返回最先达到最大次数的值。

## Problem 13-12 🔴 Advanced — Remove failing scores
给定 `ArrayList<Integer>`，从后向前删除所有小于 60 的分数，返回删除数量。

## Problem 13-13 🔴 Advanced — Recursive vowels
实现 `recursiveVowelCount(String s)`，不使用循环。

## AP CSA Style — 2 problems

## Problem 13-14 ⭐ AP CSA — Mini FRQ
实现 `public static int longestIncreasingRun(int[] values)`，返回连续严格递增元素的最长 run 长度；空 array 返回 0。

## Problem 13-15 ⭐ AP CSA — Class + ArrayList FRQ
设计 `Task`（description、complete boolean、markComplete、isComplete）并实现 `countIncomplete(ArrayList<Task> tasks)`。用 main 至少测试三项。
