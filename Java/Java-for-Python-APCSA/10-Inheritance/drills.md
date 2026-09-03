# Chapter 10 Practice — Inheritance

每个子类 constructor 先考虑父类需要怎样初始化。若重写 method，写 `@Override`。

## Level 1 — 5 problems

## Problem 10-01 🟢 Beginner — Animal and Dog
写 `Animal` class，含 `speak()` 打印 `...`；写 `Dog extends Animal`，重写为 `Woof`。

## Problem 10-02 🟢 Beginner — Parent constructor
让 `Animal` 有接收 name 的 constructor；让 `Dog` constructor 用 `super(name)`。

## Problem 10-03 🟢 Beginner — Cat
加 `Cat extends Animal`，重写 `speak()` 为 `Meow`。在 main 创建并调用。

## Problem 10-04 🟢 Beginner — Super method
在 `Dog.speak()` 中先调用 `super.speak()`，再打印 `Woof`。

## Problem 10-05 🟢 Beginner — Inherited getter
让父类保存 private name 和 `getName()`；子类使用 getter 打印自己的 name。

## Level 2 — 5 problems

## Problem 10-06 🟡 Intermediate — Vehicle
写 `Vehicle`（brand、getBrand、move）；写 `Car extends Vehicle`，重写 move 输出 `<brand> drives`。

## Problem 10-07 🟡 Intermediate — Employee roles
写 `Employee`（name、pay）和 `Manager extends Employee`（额外 bonus）；Manager 实现 `totalPay()`。

## Problem 10-08 🟡 Intermediate — Polymorphism
把 `Animal pet = new Dog("Mochi")` 放 main，调用 `pet.speak()`；用注释说明为何 Dog version 运行。

## Problem 10-09 🟡 Intermediate — Shape area
写 `Shape` 的 `area()` 返回 0；`Square extends Shape` 保存 side 并重写 area。

## Problem 10-10 🟡 Intermediate — Override check
故意把一个 child method 参数改错，观察/解释 `@Override` 如何帮助发现问题；再修复。

## Level 3 — 3 problems

## Problem 10-11 🔴 Advanced — Account types
写 `Account`（owner、balance、deposit）；`SavingsAccount` 增加 rate 和 `addInterest()`，使用继承来的 balance 的安全接口设计。

## Problem 10-12 🔴 Advanced — Library items
写 `LibraryItem`（title、loanPeriod() 返回 14）与 `DVD`（重写 loanPeriod 返回 7）；用父类引用的 array/list 调用。

## Problem 10-13 🔴 Advanced — Constructor chain trace
写 Parent/Child，各 constructor 打印一条文字；在 main 创建 Child，解释输出顺序。

## AP CSA Style — 2 problems

## Problem 10-14 ⭐ AP CSA — Override FRQ
实现 `Quiz` 的 `getPoints()` 返回 points；实现 `BonusQuiz extends Quiz`，额外保存 bonus 并重写 getPoints 返回 points + bonus。设计合理 constructor。

## Problem 10-15 ⭐ AP CSA — Reference type trace
写 `Animal[] pets = {new Dog(...), new Cat(...)}`，用循环调用 speak。解释变量的 reference type 和 object type 各负责什么。
