# Chapter 08 Practice — ArrayList

所有题先加 `import java.util.ArrayList;`。注意题目所说“按 index”还是“按 value”删除。

## Level 1 — 5 problems

## Problem 08-01 🟢 Beginner — Names list
创建 `ArrayList<String>`，添加三个人名并逐个打印。

## Problem 08-02 🟢 Beginner — Get and size
给定 names，打印 size 和第一个元素。

## Problem 08-03 🟢 Beginner — Replace
给定 names，把 index 1 的元素替换为 `Lin`，随后打印 list。

## Problem 08-04 🟢 Beginner — Remove index
给定至少三项的 `ArrayList<String>`，删除 index 2 的项，打印修改后 list。

## Problem 08-05 🟢 Beginner — Integer total
创建 `ArrayList<Integer>`，添加 3、5、7，用 `get` 求和并打印。

## Level 2 — 5 problems

## Problem 08-06 🟡 Intermediate — Count long words
给定 `ArrayList<String>`，统计长度至少 5 的 word 数量。

## Problem 08-07 🟡 Intermediate — Double values
给定 `ArrayList<Integer>`，使用 `set` 将每个元素替换为两倍。

## Problem 08-08 🟡 Intermediate — Find item
给定 list 和 target String，返回/打印 target 首个 index；不存在为 -1。不得使用 `indexOf`。

## Problem 08-09 🟡 Intermediate — Safe backward removal
给定 `ArrayList<Integer>`，从后向前删除所有负数，打印最终 list。

## Problem 08-10 🟡 Intermediate — Unique append
给定 names 和 candidate，只有当内容相同的名称不存在时才添加 candidate。使用 `.equals`。

## Level 3 — 3 problems

## Problem 08-11 🔴 Advanced — Remove duplicate neighbors
给定排序的 `ArrayList<Integer>`，移除重复项，使每个值只保留一次。允许从后向前遍历。

## Problem 08-12 🔴 Advanced — Move zeros
给定 `ArrayList<Integer>`，保持非零元素原顺序，将所有 0 移到 list 尾部。

## Problem 08-13 🔴 Advanced — Longest word
给定非空 `ArrayList<String>`，返回最长 word；若同长，返回最先出现者。

## AP CSA Style — 2 problems

## Problem 08-14 ⭐ AP CSA — Method writing
实现 `public static int removeShortWords(ArrayList<String> words, int minLength)`，删除长度小于 minLength 的 word，并返回删除数量。必须避免跳过元素。

## Problem 08-15 ⭐ AP CSA — Value versus index
创建 `[1, 2, 3, 2]` 的 `ArrayList<Integer>`，删除**值** 2 的第一次出现，而不是 index 2。打印结果并在注释中说明所用 `remove` 调用。
