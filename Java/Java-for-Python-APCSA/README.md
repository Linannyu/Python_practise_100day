# Java for Python Programmers — AP CSA Course

这是从原始 [完整 Java 手册](../Java_for_Python_APCSA.md) 重组出的每日学习项目。原手册保留不动；课程把学习改为连续的“读一章 → 实现一个 Lab → 测试 → 记录错题”流程。

## 每日学习流程

```text
📖 Lesson → 🧠 Plan → 💻 Build today’s Lab → 🧪 Test cases
      → ❌ Record mistakes → 🔁 Repair → 🧩 Targeted drills (optional)
```

每章的 `practice.md` 现在是一个**每日主 Lab**，不再是零散题目清单。下一天的 Lab 会复用此前知识并增加当天概念；例如 Day 07 的 Score Analyzer 复用 methods/loops，同时学习 arrays。

原有 15 道小题完整保存在各章 `drills.md`；只在热身、修复某个弱点或加练时使用。对应参考答案仍在 `solutions.md`。

查看完整顺序与知识复用关系：[Daily Lab Roadmap](./LABS.md)。

## 课程路线

| Day | Lesson | Main Lab | Optional drills |
|---|---|---|---|
| 01 | [Basics](./01-Basics/lesson.md) | [Java Study Card](./01-Basics/practice.md) | [Drills](./01-Basics/drills.md) |
| 02 | [Variables & Data Types](./02-Variables-DataTypes/lesson.md) | [Study Session Receipt](./02-Variables-DataTypes/practice.md) | [Drills](./02-Variables-DataTypes/drills.md) |
| 03 | [Conditionals](./03-Conditionals/lesson.md) | [Course Readiness Checker](./03-Conditionals/practice.md) | [Drills](./03-Conditionals/drills.md) |
| 04 | [Loops](./04-Loops/lesson.md) | [Study Week Analyzer](./04-Loops/practice.md) | [Drills](./04-Loops/drills.md) |
| 05 | [Methods](./05-Methods/lesson.md) | [Study Toolkit](./05-Methods/practice.md) | [Drills](./05-Methods/drills.md) |
| 06 | [String](./06-String/lesson.md) | [Username Inspector](./06-String/practice.md) | [Drills](./06-String/drills.md) |
| 07 | [Arrays](./07-Arrays/lesson.md) | [Score Analyzer](./07-Arrays/practice.md) | [Drills](./07-Arrays/drills.md) |
| 08 | [ArrayList](./08-ArrayList/lesson.md) | [Flexible Study Planner](./08-ArrayList/practice.md) | [Drills](./08-ArrayList/drills.md) |
| 09 | [Classes & Objects](./09-Classes-Objects/lesson.md) | [StudyTask Object](./09-Classes-Objects/practice.md) | [Drills](./09-Classes-Objects/drills.md) |
| 10 | [Inheritance](./10-Inheritance/lesson.md) | [Specialized Study Tasks](./10-Inheritance/practice.md) | [Drills](./10-Inheritance/drills.md) |
| 11 | [2D Arrays](./11-2D-Arrays/lesson.md) | [Weekly Focus Grid](./11-2D-Arrays/practice.md) | [Drills](./11-2D-Arrays/drills.md) |
| 12 | [Recursion](./12-Recursion/lesson.md) | [Recursive Streak Explorer](./12-Recursion/practice.md) | [Drills](./12-Recursion/drills.md) |
| 13 | [AP CSA Review](./13-APCSA-Review/lesson.md) | [AP CSA Study Dashboard](./13-APCSA-Review/practice.md) | [Drills](./13-APCSA-Review/drills.md) |

需要快速查语法时，打开 [Python → Java Cheat Sheet](./99-Cheat-Sheet/cheat-sheet.md)。

## 编译、测试与答案

每个 Lab 都指定推荐的 `.java` 文件名，通常直接写在该章节目录中。和你已有的 [HelloWorld.java](./01-Basics/HelloWorld.java) 一样，公开 class 名必须与文件名一致。

```bash
# Example: compile and run Day 01
cd 01-Basics
javac HelloWorld.java
java HelloWorld
```

某些固定签名的 Drill 提供自动方法测试；在课程根目录运行：

```bash
python3 run_tests.py --list
python3 run_tests.py 05-12
```

测试器只会编译并运行 `work/` 中的指定答案，使用临时目录，不改写你的源代码。Lab 的首选验证方式是每页列出的 acceptance checks；完成后才看 `solutions.md`。

## 进度与错题

- 在 [PROGRESS.md](./PROGRESS.md) 勾选 Lesson、Lab、测试、复盘与可选 Drill。
- 在 [mistakes.md](./mistakes.md) 记录“错误代码 → 原因 → 正确规则 → 重试日期”。

## AP CSA 范围

课程专注于 primitive types、using objects、boolean expressions、iteration、methods、classes、arrays、ArrayList、2D arrays、inheritance 和 recursion。不引入 Spring、JDBC、Maven、JavaFX、多线程或网络编程等不属于当前目标的内容。
