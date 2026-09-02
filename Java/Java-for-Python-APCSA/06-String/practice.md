# Chapter 06 Practice — String

每题都先写下合法 index 范围：`0` 到 `s.length() - 1`。除非题目说可为 null，否则假设 String 非 null。

## Level 1 — 5 problems

## Problem 06-01 🟢 Beginner — Length
给定 String word，打印它的长度。

## Problem 06-02 🟢 Beginner — Last character
给定非空 String word，打印最后一个字符。

## Problem 06-03 🟢 Beginner — First three
给定至少三个字符的 word，打印前三个字符。

## Problem 06-04 🟢 Beginner — Uppercase
给定 word，打印大写版；随后再打印原 word，展示 String 不可变。

## Problem 06-05 🟢 Beginner — Content match
给定 String command，内容为 `start` 时打印 `go`，否则打印 `wait`。

## Level 2 — 5 problems

## Problem 06-06 🟡 Intermediate — First occurrence
给定 text 和 target，打印 target 第一次出现的 index；若不存在，打印 `missing`。

## Problem 06-07 🟡 Intermediate — Initials
给定 first 与 last，返回/打印形如 `L.A.` 的 initials。

## Problem 06-08 🟡 Intermediate — Remove ends
给定长度至少 2 的 word，打印移除首尾字符后的中间部分。

## Problem 06-09 🟡 Intermediate — Character counter
给定 word 和 char target，用循环统计 target 出现次数。

## Problem 06-10 🟡 Intermediate — Reverse
给定 word，用循环构造并打印其反转文字。

## Level 3 — 3 problems

## Problem 06-11 🔴 Advanced — Vowel count
实现 `public static int countVowels(String text)`，忽略大小写，统计 a/e/i/o/u。

## Problem 06-12 🔴 Advanced — Palindrome text
实现 `public static boolean isPalindrome(String text)`，假设 text 为小写且不含空格。

## Problem 06-13 🔴 Advanced — Word censor
给定 text 和 banned，若 text 包含 banned，打印 `blocked`；否则打印 `allowed`。使用 `indexOf`。

## AP CSA Style — 2 problems

## Problem 06-14 ⭐ AP CSA — Method writing 🧪 Automated
实现 `public static String middle(String s)`：若长度为奇数返回中间一个字符组成的 String；若偶数返回中间两个字符。保证 s 非空。测试：`python3 run_tests.py 06-14`。

## Problem 06-15 ⭐ AP CSA — compareTo trace
写完整程序比较 `"apple".compareTo("banana")` 与 `"cat".compareTo("cat")` 的符号；输出 `before` 或 `same`，不要依赖具体负数。
