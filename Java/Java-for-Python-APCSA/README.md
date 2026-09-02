# Java for Python Programmers — AP CSA Course

这是把原来的 [完整 Java 手册](../Java_for_Python_APCSA.md) 重组而成的“学习 → 编程 → 测试 → 订正”课程。原手册保留不动，作为参考资料；这里是每天实际学习和写代码的地方。

## 学习流程

```text
📖 Lesson → 🧠 Understand → ✍️ Practice → 💻 Code
      → 🧪 Test → 📊 Score → ❌ Mistakes → 🔁 Retry
```

每章请依序完成 `lesson.md`、`practice.md`、自己的 `work/` 文件、测试与 `solutions.md`。先写再看答案；答案不在题目文件中。

## 课程路线

1. [Chapter 01 — Basics](./01-Basics/lesson.md) → [Practice](./01-Basics/practice.md) → [Solutions](./01-Basics/solutions.md)
2. [Chapter 02 — Variables & Data Types](./02-Variables-DataTypes/lesson.md) → [Practice](./02-Variables-DataTypes/practice.md) → [Solutions](./02-Variables-DataTypes/solutions.md)
3. [Chapter 03 — Conditionals](./03-Conditionals/lesson.md) → [Practice](./03-Conditionals/practice.md) → [Solutions](./03-Conditionals/solutions.md)
4. [Chapter 04 — Loops](./04-Loops/lesson.md) → [Practice](./04-Loops/practice.md) → [Solutions](./04-Loops/solutions.md)
5. [Chapter 05 — Methods](./05-Methods/lesson.md) → [Practice](./05-Methods/practice.md) → [Solutions](./05-Methods/solutions.md)
6. [Chapter 06 — String](./06-String/lesson.md) → [Practice](./06-String/practice.md) → [Solutions](./06-String/solutions.md)
7. [Chapter 07 — Arrays](./07-Arrays/lesson.md) → [Practice](./07-Arrays/practice.md) → [Solutions](./07-Arrays/solutions.md)
8. [Chapter 08 — ArrayList](./08-ArrayList/lesson.md) → [Practice](./08-ArrayList/practice.md) → [Solutions](./08-ArrayList/solutions.md)
9. [Chapter 09 — Classes & Objects](./09-Classes-Objects/lesson.md) → [Practice](./09-Classes-Objects/practice.md) → [Solutions](./09-Classes-Objects/solutions.md)
10. [Chapter 10 — Inheritance](./10-Inheritance/lesson.md) → [Practice](./10-Inheritance/practice.md) → [Solutions](./10-Inheritance/solutions.md)
11. [Chapter 11 — 2D Arrays](./11-2D-Arrays/lesson.md) → [Practice](./11-2D-Arrays/practice.md) → [Solutions](./11-2D-Arrays/solutions.md)
12. [Chapter 12 — Recursion](./12-Recursion/lesson.md) → [Practice](./12-Recursion/practice.md) → [Solutions](./12-Recursion/solutions.md)
13. [Chapter 13 — AP CSA Review](./13-APCSA-Review/lesson.md) → [Practice](./13-APCSA-Review/practice.md) → [Solutions](./13-APCSA-Review/solutions.md)

需要快速查语法时，打开 [Python → Java Cheat Sheet](./99-Cheat-Sheet/cheat-sheet.md)。

## 如何写题与运行测试

1. 在 `work/<chapter>/<problem>/Main.java` 新建你的答案，例如 `work/05-Methods/05-12/Main.java`。
2. Java 文件使用 `public class Main`，并按题目要求提供方法或 `main`。
3. 在本目录运行：

```bash
python3 run_tests.py --list
python3 run_tests.py 05-12
```

测试器只编译并运行本课程 `work/` 目录中的指定文件，使用临时目录，不修改你的源代码。带 `🧪 Automated` 标记的题有自动测试；其他题先用题目中的样例和 `solutions.md` 自查。

## 进度与错题

- 在 [PROGRESS.md](./PROGRESS.md) 勾选完成内容，并记录分数。
- 在 [mistakes.md](./mistakes.md) 记录错误、原因和重试日期。特别保留“错误代码 → 为什么错 → 正确规则”。

## AP CSA 范围

课程专注于 primitive types、using objects、boolean expressions、iteration、methods、classes、arrays、ArrayList、2D arrays、inheritance 和 recursion。不引入 Spring、JDBC、Maven、JavaFX、多线程或网络编程等不属于当前目标的内容。
