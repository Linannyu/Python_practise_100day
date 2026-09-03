# Chapter 09 Practice — Classes & Objects

除非题目另说，class 可与 `Main` 放在同一个文件；仅 `Main` 声明为 public。fields 默认写 private。

## Level 1 — 5 problems

## Problem 09-01 🟢 Beginner — Simple Book
写 `Book` class，含 `private String title`，以及接收 title 的 constructor。在 main 创建并打印 title（可先写 getter）。

## Problem 09-02 🟢 Beginner — Getter
给 `Book` 增加 `public String getTitle()`。

## Problem 09-03 🟢 Beginner — Counter object
写 `Counter`，有 `private int value`（初始 0）和 `increment()`；在 main 调两次并打印 value。

## Problem 09-04 🟢 Beginner — Setter
为 `Counter` 写 `setValue(int value)`，用 `this.value = value`。

## Problem 09-05 🟢 Beginner — Person greeting
写 `Person`，constructor 接收 name，`greet()` 打印 `Hello, <name>!`。

## Level 2 — 5 problems

## Problem 09-06 🟡 Intermediate — Student model
写 `Student`：private name/score、constructor、getters、`isPassing()`（60+）。在 main 测试两名学生。

## Problem 09-07 🟡 Intermediate — Bank balance
写 `BankAccount`，有 balance、`deposit(double amount)` 和 `withdraw(double amount)`；不得让 balance 变负。

## Problem 09-08 🟡 Intermediate — Rectangle
写 `Rectangle`，有 width/height、constructor、`area()` 和 `perimeter()`。

## Problem 09-09 🟡 Intermediate — Static count
写 `Ticket` class，使用 static field 统计已创建 Ticket 数，并提供 static getter。在 main 创建三张票。

## Problem 09-10 🟡 Intermediate — Reference sharing
创建一个 `ArrayList<String>` 或对象变量 a，然后 `b = a`，经 b 修改后打印 a。用注释解释结果。

## Level 3 — 3 problems

## Problem 09-11 🔴 Advanced — Clock
写 `Clock`，保存 hour/minute；constructor 验证 0–23 与 0–59，`tick()` 推进一分钟并正确进位，`toString()` 返回 `HH:MM`。

## Problem 09-12 🔴 Advanced — Quiz question
写 `Question`，有 prompt、answer、`checkAnswer(String response)`；比较文字内容时必须正确。

## Problem 09-13 🔴 Advanced — Immutable-ish point
写 `Point`，private x/y，constructor、getters、`distanceFromOrigin()`；不要提供 setter。解释这如何限制状态改变。

## AP CSA Style — 2 problems

## Problem 09-14 ⭐ AP CSA — Class design FRQ
实现 `Temperature` class：private `double celsius`、constructor、`getCelsius()`、`getFahrenheit()`、`isFreezing()`。在 main 创建 -5 与 20 测试。

## Problem 09-15 ⭐ AP CSA — Method contract
为 `Movie` class 实现 `rate(int stars)`：只接受 1–5，否则不修改当前 rating；再写 `getRating()`。用 main 展示无效评分不改变对象。
