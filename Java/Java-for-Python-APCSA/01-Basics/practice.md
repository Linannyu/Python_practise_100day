# Day 01 Lab — Build Your Java Study Card
# 第 01 天实验 — 制作你的 Java 学习卡

## 🎯 Lab Goal
## 🎯 实验目标

Create a first Java program that prints a clean console “study card.”

创建你的第一个 Java 程序，让它在控制台中打印一张整洁的“学习卡”。

This is not about memorizing syntax: the goal is to make a program compile, run, and produce exact output.

这次实验的重点不是死记语法，而是让程序成功编译、运行，并输出完全正确的内容。

### Today's Java
### 今天的 Java

- `class` — 类
- `main` — 主方法 / 程序入口
- `System.out.print()` — 输出但不换行
- `System.out.println()` — 输出并换行
- comments — 注释
- strings — 字符串
- `;` — 分号
- `{ }` — 代码块

### Prior Knowledge Reused
### 复习之前的知识

- Python's `print()` — Python 的 `print()`
- Code runs in order — 代码按照顺序执行

---

## ♻️ Reuse from Earlier Knowledge
## ♻️ 复用之前的知识

Translate the same output plan you would make with Python `print()` into Java statements.

把你以前使用 Python `print()` 时的输出思路转换成 Java 语句。

The difference is Java's required `class` / `main` container and its explicit statement endings.

不同之处在于：Java 要求代码放在 `class` / `main` 结构中，并且语句通常需要使用 `;` 表示结束。

### Python

```python
print("Hello")
print("World")
```

### Java

```java
System.out.println("Hello");
System.out.println("World");
```

---

## 🚀 Mission
## 🚀 实验任务

Create or improve `HelloWorld.java` in this folder.

在这个文件夹中创建或修改 `HelloWorld.java`。

It must display a study card with your name, your known language, and a three-step plan.

程序必须显示一张学习卡，其中包含你的名字、已掌握的编程语言，以及一个三步骤学习计划。

---

## 📋 Required Output Shape
## 📋 要求的输出格式

Use your real name if you wish, but preserve this layout.

你可以使用自己的真实姓名，也可以使用其他名字，但必须保持下面的布局。

```text
====================
Lin's Java Study Card
Known language: Python
1. Read
2. Code
3. Test
====================
```

The output must contain exactly **7 lines**.

输出必须准确包含 **7 行**。

> ⚠️ Do not print an extra blank line after the final line.
>
> ⚠️ 最后一行后面不能额外打印空白行。

---

## ✅ Requirements
## ✅ 实验要求

### 1. Use `public class HelloWorld`
### 1. 使用 `public class HelloWorld`

```java
public class HelloWorld {

}
```

### 2. Use a valid `main` method
### 2. 使用正确的 `main` 方法

```java
public static void main(String[] args) {

}
```

This is where the Java program starts running.

这是 Java 程序开始执行的地方。

### 3. Include one `//` comment
### 3. 至少包含一个 `//` 注释

```java
// Print the top border
// 打印顶部边框
System.out.println("====================");
```

### 4. Use at least one `print`
### 4. 至少使用一次 `print`

```java
System.out.print();
```

`print()` prints text without automatically moving to the next line.

`print()` 输出内容后不会自动换行。

### 5. Use at least four `println` calls
### 5. 至少使用四次 `println`

```java
System.out.println();
```

`println()` prints text and then moves to the next line.

`println()` 输出内容后会自动换到下一行。

### 6. Do not put all output into one multiline String
### 6. 不要把所有输出放进一个多行字符串

Use multiple `print` and `println` statements.

使用多个 `print` 和 `println` 语句。

### 7. No extra blank line
### 7. 不能有额外的空白行

The final output must be exactly the required seven lines.

最终输出必须严格为要求的七行。

---

## 🟢 Start Here
## 🟢 从这里开始

```java
public class HelloWorld {
    public static void main(String[] args) {
        // TODO: print the top border
        // TODO: 打印顶部边框

        // TODO: print the five content lines
        // TODO: 打印五行内容

        // TODO: print the bottom border
        // TODO: 打印底部边框
    }
}
```

Replace the `TODO` comments with working Java code.

把 `TODO` 注释替换成真正可以运行的 Java 代码。

---

## 🔍 Acceptance Checks
## 🔍 验收标准

### 1. Compile successfully
### 1. 成功编译

```bash
javac HelloWorld.java
```

There should be no errors.

不能出现任何编译错误。

### 2. Run successfully
### 2. 成功运行

```bash
java HelloWorld
```

The program must print exactly seven lines.

程序必须准确打印 7 行。

### 3. Your name and `Python` must appear
### 3. 必须出现你的名字和 `Python`

```text
Lin's Java Study Card
Known language: Python
```

### 4. Explain `print` vs `println`
### 4. 能解释 `print` 和 `println` 的区别

```java
System.out.print("1. ");
System.out.println("Read");
```

Output:

输出：

```text
1. Read
```

`print()` does not move to a new line. `println()` prints and then moves to the next line.

`print()` 不换行；`println()` 输出后会换行。

---

## ⭐ Stretch Goal
## ⭐ 提高挑战

Add a final line with a literal double quote.

增加一行包含双引号字符的内容。

```text
Motto: "Make it work."
```

Use correct Java escaping:

使用正确的 Java 转义语法：

```java
System.out.println("Motto: \"Make it work.\"");
```

---

## 📝 Reflection
## 📝 实验反思

In `mistakes.md`, record any compile error you saw and the symbol that fixed it.

在 `mistakes.md` 中记录你遇到的编译错误，以及最终解决这个错误的符号。

Example:

例如：

```markdown
## Error 1

Error:
Missing semicolon.

错误：
缺少分号。

Fix:
`;`

解决方法：
`;`

What I learned:
Java statements usually end with a semicolon.

我学到了：
Java 语句通常需要使用分号结束。
```

For short syntax drills after the Lab, use `drills.md`.

完成 Lab 后，可以使用 `drills.md` 进行简短的语法练习。

Answers are available in `solutions.md`.

答案可以在 `solutions.md` 中查看。

---

## 🧠 Today's Java Cheat Sheet
## 🧠 今日 Java 速查表

| Java | English | 中文 |
|---|---|---|
| `class` | class | 类 |
| `main` | main method | 主方法 / 程序入口 |
| `System.out.print()` | print without newline | 输出但不换行 |
| `System.out.println()` | print with newline | 输出并换行 |
| `//` | comment | 单行注释 |
| `String` | string | 字符串 |
| `;` | semicolon | 分号 / 语句结束 |
| `{ }` | braces | 大括号 / 代码块 |
| `\"` | escaped double quote | 转义双引号 |

---

## 🐍 Python vs Java
## 🐍 Python 与 Java 对照

| Concept | Python | Java |
|---|---|---|
| Output | `print("Hello")` | `System.out.println("Hello");` |
| Code block | Indentation | `{ }` |
| Statement ending | Usually no `;` | Usually `;` |
| Program entry | `if __name__ == "__main__":` | `main()` |
| String | `"Hello"` | `"Hello"` |
| Comment | `# comment` | `// comment` |

---

## 🎯 Today's Core Goal
## 🎯 今天的核心目标

```text
Python print()
      ↓
Java System.out.print()
      ↓
Java System.out.println()
      ↓
Understand print vs println
理解 print 和 println 的区别
      ↓
Understand class + main
理解 class + main
      ↓
Compile with javac
使用 javac 编译
      ↓
Run with java
使用 java 运行
```

By the end, you should be able to explain:

完成后，你应该能够解释：

1. What does `class` do? — `class` 是干什么的？
2. Where does the Java program start? — Java 程序从哪里开始执行？
3. What is the difference between `print()` and `println()`? — 两者有什么区别？
4. Why do Java statements usually need `;`? — 为什么通常需要分号？
