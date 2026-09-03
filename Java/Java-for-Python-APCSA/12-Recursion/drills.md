# Chapter 12 Practice — Recursion

每题先写 base case，再确认 recursive call 的输入更接近它。用 0、1、2 手动追踪。

## Level 1 — 5 problems

## Problem 12-01 🟢 Beginner — Countdown
实现 `countdown(int n)`，从 n 打印到 1；n 为 0 时停止。

## Problem 12-02 🟢 Beginner — Count up
实现 `countUp(int n)`，打印 1 到 n；提示：recursive call 前后放不同语句会改变顺序。

## Problem 12-03 🟢 Beginner — Sum to n
实现 `sumTo(int n)`，返回 1 到 n 的和，base case 为 0。

## Problem 12-04 🟢 Beginner — Factorial
实现 `factorial(int n)`，假设 n 非负。

## Problem 12-05 🟢 Beginner — Power
实现 `power(int base, int exponent)`，使用递归并假设 exponent 非负。

## Level 2 — 5 problems

## Problem 12-06 🟡 Intermediate — Even sum
实现 `sumEvenTo(int n)`，返回 0 到 n 所有偶数和。

## Problem 12-07 🟡 Intermediate — Digit sum
实现 `digitSum(int n)`，返回非负 n 的每位数字之和。

## Problem 12-08 🟡 Intermediate — String length
不用 `.length()`，实现递归 `recursiveLength(String s)`。允许用 `substring(1)`。

## Problem 12-09 🟡 Intermediate — Count character
实现 `countChar(String s, char target)`，递归统计 target 出现次数。

## Problem 12-10 🟡 Intermediate — Reverse print
实现 `printReverse(String s)`，不构造反转 String，逐个字符反向打印。

## Level 3 — 3 problems

## Problem 12-11 🔴 Advanced — Palindrome
实现递归 `isPalindrome(String s)`，假设小写无空格。比较首尾，递归处理中间部分。

## Problem 12-12 🔴 Advanced — Array sum
实现 `arraySum(int[] values, int index)`，返回从 index 到末尾的元素和；index 等于 length 是 base case。

## Problem 12-13 🔴 Advanced — Binary count
实现 `countBinaryDigits(int n)`，返回正整数 n 的二进制位数；base case 应正确处理 n 小于 2。

## AP CSA Style — 2 problems

## Problem 12-14 ⭐ AP CSA — Method writing 🧪 Automated
实现 `public static int productTo(int n)`，返回 1×2×…×n；`productTo(0)` 返回 1。测试：`python3 run_tests.py 12-14`。

## Problem 12-15 ⭐ AP CSA — Trace order
不运行，追踪 `mystery(3)`：
```java
public static void mystery(int n) {
    if (n == 0) return;
    System.out.print(n + " ");
    mystery(n - 1);
    System.out.print(n + " ");
}
```
再写完整 Main 验证，并解释每个数字为何出现两次。
