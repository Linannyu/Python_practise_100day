# Chapter 01 — Java Basics

## 🎯 Learning Goals

学完后，你能：

- 解释 Java、JavaScript、JVM、`.java` 与 `.class` 的区别；
- 写出并运行一个 `Main.java`；
- 读懂 `public static void main(String[] args)`；
- 正确使用 `{ }`、`;`、注释与 `System.out.println`。

---

## 🐍 Python → ☕ Java

```python
print("Hello, Lin!")
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Lin!");
    }
}
```

Python 文件从上到下执行；Java 把代码放进 class，JVM 从约定的 `main` 方法启动。Java 和 JavaScript 是不同语言。

## 1. Java 的运行路径

```text
Main.java → javac → Main.class → JVM → output
```

`.java` 是你编辑的源代码；`.class` 是编译后的字节码；JVM 执行字节码。静态类型和编译会在运行前抓住许多错误。

## 2. 拆解 main

| 部分 | 作用 | Python 连接 |
|---|---|---|
| `public` | 允许 JVM/其他类访问 | 公开入口 |
| `static` | 不需先创建对象 | 类上的工具函数 |
| `void` | 没有返回值 | 未 `return` 的函数 |
| `main` | 程序入口名 | 脚本的起点 |
| `String[] args` | 命令行文字参数 | 参数列表 |

## 3. Syntax map

| Python | Java |
|---|---|
| 缩进建立代码块 | `{ }` 建立代码块 |
| 新行结束语句 | `;` 通常结束语句 |
| `# comment` | `// comment` |
| 多行字符串/注释 | `/* multi-line */` |

## 4. Example

```java
public class Main {
    public static void main(String[] args) {
        // println ends with a new line.
        System.out.println("Java is ready.");
        System.out.print("AP");
        System.out.print(" CSA");
    }
}
```

⚠️ **Common Mistakes**

- 漏掉 `System.out.`、分号或一个花括号；
- 将 public `Main` 存到不是 `Main.java` 的文件；
- 在 `if (...)` 或 `main(...)` 后乱放分号。

🧠 **AP CSA Notes**：能编译不代表逻辑正确；先区分 compile error、runtime error 和 wrong answer。

✅ **Before Practice**

- 我能从零写出 `Main` 外壳。
- 我知道 `print` 与 `println` 的输出差别。
- 我能指出每个花括号关闭的代码块。

📝 **Practice**：完成 [Chapter 01 Practice](./practice.md)。
