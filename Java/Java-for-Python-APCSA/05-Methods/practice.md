# Chapter 05 Practice — Methods

对每个 non-void method，自己准备至少三个 test：普通值、边界值、负值或特殊值。方法题写在 `Main` 中，按给定 header 原样实现。

## Level 1 — 5 problems

## Problem 05-01 🟢 Beginner — Greeting method
实现 `public static void greet(String name)`，打印 `Hello, <name>!`。

## Problem 05-02 🟢 Beginner — Double it
实现 `public static int doubleIt(int n)`，返回 n 的两倍。

## Problem 05-03 🟢 Beginner — Absolute difference
实现 `public static int difference(int a, int b)`，返回 a 与 b 的正差；可用 `Math.abs`。

## Problem 05-04 🟢 Beginner — Is positive
实现 `public static boolean isPositive(int n)`，只有 n 大于 0 返回 true。

## Problem 05-05 🟢 Beginner — First character
实现 `public static char firstChar(String s)`，返回第一个字符。假设 s 非空。

## Level 2 — 5 problems

## Problem 05-06 🟡 Intermediate — Average
实现 `public static double average(int a, int b)`，返回精确平均数而非整数除法。

## Problem 05-07 🟡 Intermediate — In range
实现 `public static boolean inRange(int value, int low, int high)`，两端均包含。

## Problem 05-08 🟡 Intermediate — Repeat
实现 `public static String repeat(String word, int times)`，返回 word 连续出现 times 次的 String。times 为 0 时返回空 String。

## Problem 05-09 🟡 Intermediate — Larger
实现 `public static int larger(int a, int b)`，不得调用 `Math.max`。

## Problem 05-10 🟡 Intermediate — Grade label
实现 `public static String gradeLabel(int score)`，返回 A/B/C/D/F。

## Level 3 — 3 problems

## Problem 05-11 🔴 Advanced — Digit count
实现 `public static int digitCount(int n)`，返回 n 的十进制位数；正确处理 0 和负数。

## Problem 05-12 🔴 Advanced — Square 🧪 Automated
实现 `public static int square(int x)`。文件：`work/05-Methods/05-12/Main.java`；运行 `python3 run_tests.py 05-12`。

## Problem 05-13 🔴 Advanced — Palindrome number
实现 `public static boolean isPalindromeNumber(int n)`，判断非负整数的数字是否前后相同，例如 1221 true、123 false。

## AP CSA Style — 2 problems

## Problem 05-14 ⭐ AP CSA — Header contract
实现 `public static int countMultiples(int start, int end, int divisor)`，返回闭区间内 divisor 倍数的数量。可假设 divisor 不为 0。

## Problem 05-15 ⭐ AP CSA — Overload design
写两个 `describe` 方法：一个接收 `int` 并返回 `"number: <n>"`，一个接收 `String` 并返回 `"word: <s>"`。在 main 中调用两者。
