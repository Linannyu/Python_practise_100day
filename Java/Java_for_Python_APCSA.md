# Java for Python Programmers — AP CSA Edition

> 面向已经会 Python、正在学习 AP Computer Science A（AP CSA）的高中生。
>
> 这不是 Java 语法百科。每一节都从你已经会的 Python 出发，帮助你把同一个想法写成 AP CSA 需要的 Java。

## 如何使用这份手册

- 第一次学习时按章节顺序读，并亲手运行每个 `Main` 示例。
- 已经学过某一章时，直接看该章的“Python → Java”对照和“常见错误”。
- 练习区先自己写；需要时再展开本章末尾的答案。AP CSA 的题目不奖励“看起来像对”，而奖励准确的 Java 细节。
- 除了专门展示类定义的片段外，所有完整 Java 示例都可保存为 `Main.java` 后编译运行：`javac Main.java`，再运行：`java Main`。

## 目录

1. [Java 和 Python 的区别](#1-java-和-python-的区别)
2. [Java 基础语法](#2-java-基础语法)
3. [变量与数据类型](#3-变量与数据类型)
4. [运算符](#4-运算符)
5. [条件语句](#5-条件语句-if--else)
6. [循环](#6-循环-loops)
7. [方法](#7-方法-methods)
8. [String](#8-string)
9. [数组](#9-数组-arrays)
10. [ArrayList](#10-arraylist)
11. [类与对象](#11-类与对象-classes--objects)
12. [static](#12-static)
13. [继承](#13-继承-inheritance)
14. [二维数组](#14-二维数组-2d-arrays)
15. [递归](#15-递归-recursion)
16. [AP CSA 常用类](#16-ap-csa-常用类)
17. [Java 特有概念](#17-java-特有概念)
18. [AP CSA 高频陷阱](#18-ap-csa-高频陷阱)
19. [Python → Java 快速翻译表](#19-python--java-快速翻译表)
20. [AP CSA 学习路线](#20-ap-csa-学习路线)

---

## 1. Java 和 Python 的区别

### Java 是什么？它和 JavaScript 有关系吗？

Java 是一种通用、面向对象的编程语言。AP CSA 用它来考察算法、数据结构和面向对象设计。**Java 和 JavaScript 是两门不同的语言**：名字相似，但语法、运行环境、用途都不同。不要因为会网页里的 JavaScript，就假设 Java 的规则相同。

AP CSA 选择 Java，是因为它的类型、类、对象和库都很明确；考试可以据此考查你是否真正理解程序运行方式。

### 从 Python 的自由写法到 Java 的明确写法

```python
# Python：运行时根据值决定类型
x = 10
x = "ten"       # 合法
```

```java
public class Main {
    public static void main(String[] args) {
        int x = 10;
        // x = "ten";  // 编译错误：x 已声明为 int
        System.out.println(x);
    }
}
```

Python 是**动态类型**：变量的类型可随所赋的值改变。Java 是**静态类型**：先声明变量能保存什么类型，编译器会在运行前检查不合理的用法。多写了类型和分号，但换来许多更早发现的错误。

| 方面 | Python | Java | 对 AP CSA 的含义 |
|---|---|---|---|
| 类型 | 运行时推断 | 编译期通常要声明 | 读题时始终注意变量类型 |
| 代码块 | 缩进 | `{ }` | 少一个花括号会改变逻辑 |
| 语句结尾 | 通常换行 | `;` | 大多数语句必须有分号 |
| 函数入口 | 文件从上到下执行 | 从 `main` 开始 | 先定位 `main` |
| 列表 | 一个 `list` 可混合类型 | `int[]`、`ArrayList<Integer>` 等 | 数组长度和集合方法不同 |
| 字符串 | `str`，可用 `==` 比内容 | `String` 对象，用 `.equals()` | 这是常考陷阱 |

### 编译、JVM、`.java` 与 `.class`

Python 常由解释器执行源代码；现代 Python 也会产生内部字节码，但你通常不需要关心。Java 的常见流程是：

```text
Main.java（人写的源代码）
        ↓ javac 编译器
Main.class（Java 字节码）
        ↓ JVM / Java Virtual Machine
在当前电脑上执行
```

JVM（Java 虚拟机）让同一份 `.class` 字节码可以在不同操作系统的 JVM 上运行。JVM 也会在运行时使用 JIT（just-in-time）等技术优化常用代码。对 AP CSA 来说，只要记住：**编译错误在运行前出现；程序能编译不代表逻辑一定正确。**

### 为什么 Java 程序通常有 `class` 和 `main`？

Java 把代码组织在类中。你可以把类先看成“装着相关数据和行为的蓝图”；本章的 `Main` 是一个最小容器。程序启动时，JVM 寻找约定好的入口：

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Java starts here.");
    }
}
```

`main` 是程序入口，不是 Python 的 `if __name__ == "__main__":` 的逐字翻译，但角色相近：把“直接运行此文件时要做的事”放在这里。

### 常见错误

- 把 Java 当 JavaScript；它们不能互换。
- 以为 Java 会允许 `x` 先是 `int` 后变成 `String`。
- 把 `.class` 当成可随意编辑的源文件；应编辑 `.java` 并重新编译。
- 以为“能运行”就等于“答案正确”；边界条件仍须检查。

### 🧪 Practice

#### Level 1 — 基础

1. 把 Python 的 `score = 95` 写成 Java 声明。
2. `.java` 文件和 `.class` 文件分别是什么？
3. Java 程序通常从哪个方法开始？

#### Level 2 — AP CSA 风格

4. `int count = 3; count = 3.5;` 为什么不能编译？
5. 把 `print("Ready")` 放进一个可运行的 Java `Main` 程序。
6. 判断：类型错误更可能在 Java 的编译期还是 Python 的运行期被发现？

#### Level 3 — Challenge

7. 解释 JVM 如何帮助 Java 跨平台。
8. 写一句话说明为什么 AP CSA 关心静态类型。

<details>
<summary>本章答案、提示与解释</summary>

1. `int score = 95;`——`int` 先固定了可保存的值的种类。
2. `.java` 是可读、可编辑的源代码；`.class` 是编译后的字节码。
3. `public static void main(String[] args)`。
4. `count` 的类型是 `int`，而 `3.5` 是 `double`；不能无损自动放入 `int`。
5. `public class Main { public static void main(String[] args) { System.out.println("Ready"); } }`。
6. Java 编译期；编译器知道声明的类型。
7. `javac` 生成由 JVM 执行的字节码；不同系统各自提供 JVM。
8. 示例：因为变量、参数和返回值类型让程序接口可检查，很多错误可在运行前发现。
</details>

---

## 2. Java 基础语法

先把最常出现的一行拆开。你会反复看到它：

```java
public static void main(String[] args) {
    System.out.println("Hello, AP CSA!");
}
```

| 部分 | 作用 | Python 类比 |
|---|---|---|
| `public` | 其他类也可以访问它 | 没有完全相同的默认关键字；可理解为公开入口 |
| `static` | 方法属于类本身，不需要先创建对象 | 接近 `@staticmethod`，但 Java 语义更常用 |
| `void` | 此方法不返回值 | Python 函数没有 `return` 时返回 `None` |
| `main` | JVM 约定的程序入口名 | 脚本开始执行的位置 |
| `String[]` | 字符串数组类型 | `list[str]` 的一种固定类型版本 |
| `args` | 参数名，保存命令行参数 | 函数参数名 |

### 标点不是装饰

```java
public class Main {              // class：装代码的类；文件名须为 Main.java
    public static void main(String[] args) { // ( ) 放参数，{ 开始代码块
        System.out.println("Hi"); // ; 结束一条语句
        // 单行注释
        /* 多行
           注释 */
    }                             // } 结束 main
}                                 // } 结束 class
```

- `class`：定义一个类。若类是 `public`，文件名须与它完全同名。
- `{ }`：定义代码块，例如类、方法、`if` 或循环的范围；Python 用缩进表达同一层级。
- `( )`：调用方法、传参数、声明方法参数，以及写条件时都会出现。
- `;`：通常结束一条语句；`if (...) {`、方法头和类头后不加。
- `System.out.println(...)`：打印一行并换行；`System.out.print(...)` 不换行。
- `//`：单行注释；`/* ... */`：多行注释。

### Python → Java：最小程序

```python
# Python
print("Hello")
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

Java 看起来较长，是因为它明确写出入口、类和语句边界。随着后面的类与对象章节，这些结构会开始“物有所值”。

**AP CSA 重要程度：极高。** 你必须能读出每个花括号属于谁、每个方法在哪里结束。

### 常见错误

- 写 `print()` 或 `println()`，漏掉 `System.out.`。
- `System.out.println("Hi")` 后漏 `;`。
- 用 Python 的 `#` 注释；Java 要用 `//`。
- 把 `main` 写在 `Main` 类外面。

### 🧪 Practice

#### Level 1 — 基础

1. `System.out.print` 和 `System.out.println` 的区别是什么？
2. Java 单行注释的前缀是什么？
3. 一条赋值语句通常如何结束？

#### Level 2 — AP CSA 风格

4. 写一个完整程序，依次打印 `One` 和 `Two`，每个各占一行。
5. `public class Main` 的 `Main` 和文件名有什么关系？
6. 找错：`if (x > 0); { System.out.println(x); }` 中多出的符号为什么危险？

#### Level 3 — Challenge

7. 用自己的话解释 `void`。
8. 为一个两行的 Java 程序加上一个单行和一个多行注释。

<details>
<summary>本章答案、提示与解释</summary>

1. `print` 不自动换行，`println` 打印后换行。
2. `//`。
3. `;`。
4. 在 `main` 中写两句 `System.out.println(...)`；不要忘记每句的分号。
5. `public class Main` 必须保存在 `Main.java`；大小写也要一致。
6. `if` 后的分号已经结束了条件语句，后面的代码块会无条件执行。
7. `void` 表示调用者不会从该方法得到一个返回值。
8. 示例：`// display greeting` 和 `/* first line\n second line */`；注释不改变执行结果。
</details>

---

## 3. 变量与数据类型

Python 让值“携带类型”；Java 让变量声明“可接收的类型”。

```python
x = 10
name = "Lin"
price = 3.14
student = True
```

```java
public class Main {
    public static void main(String[] args) {
        int x = 10;
        String name = "Lin";
        double price = 3.14;
        boolean student = true;
    }
}
```

| Python 值 | Java 常用类型 | 说明 |
|---|---|---|
| `10` | `int` | AP CSA 中最常用的整数类型 |
| `3.14` | `double` | 带小数的数值 |
| `True` / `False` | `boolean` | Java 必须小写：`true` / `false` |
| `'A'` | `char` | 一个字符，**单引号** |
| `"Lin"` | `String` | 文本，**双引号** |

### Primitive 与 reference：先掌握够用的模型

| 类别 | 常见 AP CSA 类型 | 好记的理解 |
|---|---|---|
| Primitive（基本类型） | `int`、`double`、`boolean`、`char` | 变量直接保存一个简单值 |
| Reference（引用类型） | `String`、array、`ArrayList`、自定义对象 | 变量保存“找到某个对象的引用” |

这不是说引用类型“不存数据”，而是说变量本身不像 `int` 那样直接装数字。这个区别会解释为何 `String` 比较内容用 `.equals()`、为何两个变量可能指向同一个 `ArrayList`。

```java
public class Main {
    public static void main(String[] args) {
        char grade = 'A';
        String word = "A";
        System.out.println(grade); // 一个字符
        System.out.println(word);  // 一个 String 对象
    }
}
```

### 声明、初始化与更新

```java
public class Main {
    public static void main(String[] args) {
        int count;       // 声明：尚未给局部变量值
        count = 1;       // 初始化
        count = count + 1; // 更新
        System.out.println(count);
    }
}
```

局部变量在使用前必须被初始化；Python 会在执行到赋值后才创建名字，Java 编译器会更早阻止“可能还没有值”的用法。

**AP CSA 重要程度：极高。** 类型决定 `/` 的结果、可调用的方法，以及参数是否匹配。

### 常见错误

- 写 `String name = 'Lin';`：`String` 要双引号，单引号只给 `char`。
- 写 `Boolean` 或 `True` 来代替基础类型 `boolean`、`true`。
- 以为 `int` 可以放 `3.5`。
- 在同一个作用域内重复写 `int x = ...;`。

### 🧪 Practice

#### Level 1 — 基础

1. 为年龄 `16` 选择 Java 类型并声明变量。
2. 写一个存储 `"Java"` 的 `String` 变量。
3. `char` 和 `String` 的引号分别是什么？

#### Level 2 — AP CSA 风格

4. 判断 `double d = 5;` 是否可以编译，并说明原因。
5. 判断 `int n = 2.0;` 是否可以编译。
6. 写出 `boolean passed = ...;`，使它表示“分数至少 60”。假设已有 `int score`。

#### Level 3 — Challenge

7. `int a = 4; int b = a; b++;` 后 `a` 和 `b` 各是多少？
8. 在 primitive/reference 模型下，为什么 `String` 不应使用 `==` 比内容？

<details>
<summary>本章答案、提示与解释</summary>

1. `int age = 16;`。
2. `String language = "Java";`。
3. `char` 用 `'A'`；`String` 用 `"A"`。
4. 可以。整数 `5` 可安全提升为 `double` 的 `5.0`。
5. 不可以。`2.0` 是 `double`，不能自动缩窄为 `int`。
6. `boolean passed = score >= 60;`，比较表达式本身产生 `boolean`。
7. `a` 是 `4`，`b` 是 `5`；基本类型赋值复制值。
8. 因为引用变量的 `==` 检查是否为同一个对象，而不保证检查字符内容。
</details>

---

## 4. 运算符

| Python | Java | 意义 / 注意点 |
|---|---|---|
| `+` | `+` | 加法；String 上也可拼接 |
| `-` | `-` | 减法 |
| `*` | `*` | 乘法 |
| `/` | `/` | 两个 `int` 相除会做整数除法 |
| `%` | `%` | 余数 |
| `**` | `Math.pow(a, b)` | 幂；返回 `double` |
| `==` | `==` | primitive 值比较；引用比较身份 |
| `!=` | `!=` | 不等 |
| `>` `<` `>=` `<=` | 相同 | 大小比较 |
| `and` | `&&` | 逻辑且 |
| `or` | `||` | 逻辑或 |
| `not` | `!` | 逻辑非 |

### 整数除法：Python 用户最容易踩的坑

```python
5 / 2       # 2.5
5 // 2      # 2
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(5 / 2);       // 2：两个操作数都是 int
        System.out.println(5.0 / 2);     // 2.5：至少一边是 double
        System.out.println((double) 5 / 2); // 2.5：显式转换
    }
}
```

Java 先看**操作数类型**，再决定 `/` 的类型；不是先看你把结果保存到哪里。下面仍会得到 `2.0`：

```java
double average = 5 / 2;
```

### 自增、复合赋值与短路

```java
public class Main {
    public static void main(String[] args) {
        int x = 3;
        x++;       // 相当于 x = x + 1;，不是 Python 的 x++（Python 没有）
        x += 4;    // 相当于 x = x + 4;
        boolean ok = x > 0 && x < 10;
        System.out.println(ok);
    }
}
```

`&&` 和 `||` 会短路：若左边已能决定结果，右边不必执行。AP CSA 题会利用这一点检查你是否会越界或调用不应发生的方法。

### 常见错误

- 写 `**`；Java 中应使用 `Math.pow`。
- 用 `and`、`or`、`not`。
- 忘记 `5 / 2` 是 `2`。
- 用 `==` 比较两个 `String` 的文字内容。

### 🧪 Practice

#### Level 1 — 基础

1. `17 % 5` 的值是多少？
2. Java 中 Python 的 `and` 对应什么？
3. 把 `x = x + 1` 改写为 Java 的简写。

#### Level 2 — AP CSA 风格

4. `double q = 9 / 4;` 中 `q` 是多少？
5. 写一个表达式判断 `n` 是偶数。
6. 用 Java 写“`score` 在 0 到 100（含）之间”。

#### Level 3 — Challenge

7. 将 `Math.pow(2, 3)` 赋给 `int` 时要注意什么？
8. 为什么 `i < arr.length && arr[i] > 0` 的条件顺序是安全的？

<details>
<summary>本章答案、提示与解释</summary>

1. `2`。
2. `&&`。
3. `x++;`（或 `x += 1;`）。
4. `2.0`：先做 `int / int` 得 `2`，再赋给 `double`。
5. `n % 2 == 0`。
6. `score >= 0 && score <= 100`。
7. 它返回 `double`；若题目保证安全，可写 `(int) Math.pow(2, 3)`，但一般整数幂可用循环避免转换。
8. `&&` 短路；只有 `i` 合法时才访问 `arr[i]`。
</details>

---

## 5. 条件语句：if / else

Python 用冒号和缩进，Java 用圆括号、花括号和 `else if`：

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

```java
public class Main {
    public static void main(String[] args) {
        int score = 84;
        if (score >= 90) {
            System.out.println("A");
        } else if (score >= 80) {
            System.out.println("B");
        } else {
            System.out.println("C");
        }
    }
}
```

- `if (condition)`：`condition` 必须是 `boolean`。
- `else if`：Python `elif` 的 Java 拼写，分成两个词。
- `else`：当前面所有条件为假时运行。
- `{ }`：把多条语句放在一个分支中。即使分支只有一行，初学时也应总写花括号。

Java 不会把整数当真假值：Python 中 `if 1:` 为真，Java 中 `if (1)` 是编译错误。请明确写 `if (count != 0)`。

**AP CSA 重要程度：极高。** 尤其是条件边界和 `else if` 的顺序。

### 常见错误

- 写 `elif`、冒号或用缩进代替花括号。
- 写 `if (score = 90)`；这是赋值，不是比较，应是 `==` 或范围比较。
- 让宽泛条件排在具体条件前，如先 `score >= 60` 再 `score >= 90`。
- 误在 `if (...)` 后加 `;`。

### 🧪 Practice

#### Level 1 — 基础

1. 把 Python `elif` 写成 Java 关键字。
2. 写条件判断 `temperature` 是否小于 0。
3. Java `if` 的条件表达式必须产生哪种类型？

#### Level 2 — AP CSA 风格

4. 写代码：`n` 为偶数打印 `"even"`，否则打印 `"odd"`。
5. 对 `score = 95`，若代码先检查 `score >= 60`，再检查 `score >= 90`，会出现什么问题？
6. 写一个三档票价：年龄 `< 5` 为 0，`<= 12` 为 8，其余为 12。

#### Level 3 — Challenge

7. 为什么 `if (name.equals("Lin"))` 比 `if (name == "Lin")` 更适合比较文字？
8. 写一个不使用 `else`、但只在 `x` 是正奇数时打印 `x` 的条件。

<details>
<summary>本章答案、提示与解释</summary>

1. `else if`。
2. `temperature < 0`。
3. `boolean`。
4. `if (n % 2 == 0) { System.out.println("even"); } else { System.out.println("odd"); }`。
5. `95` 已被第一个条件捕获，永远到不了 `>= 90` 分支；应从最高门槛开始。
6. 依次写 `if (age < 5)`、`else if (age <= 12)`、`else`，边界 5 和 12 恰好只落一个分支。
7. `.equals` 比字符内容；`==` 对引用常问“是否同一对象”。
8. `if (x > 0 && x % 2 != 0) { System.out.println(x); }`。
</details>

---

## 6. 循环 Loops

### `while`：条件为真就重复

```python
while x < 10:
    x += 1
```

```java
public class Main {
    public static void main(String[] args) {
        int x = 0;
        while (x < 10) {
            x++;
        }
        System.out.println(x);
    }
}
```

条件、更新和循环体是否会终止，是同一个问题。Java 的 `x++` 正是 Python `x += 1` 的常见对应。

### `for`：把计数循环的三步放在一行

```python
for i in range(10):
    print(i)
```

```java
public class Main {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
    }
}
```

`for (int i = 0; i < 10; i++)` 的三个部分：

| 部分 | 何时执行 | 含义 |
|---|---|---|
| `int i = 0` | 一次，在开始前 | 初始化计数器 |
| `i < 10` | 每轮开始前 | 继续条件 |
| `i++` | 每轮循环体后 | 更新计数器 |

因此它相当于 Python 的 `range(0, 10, 1)`，打印 0 到 9，**不含** 10。

### `break`、`continue` 与 enhanced for

```java
public class Main {
    public static void main(String[] args) {
        int[] values = {3, -1, 0, 7};
        for (int value : values) { // enhanced for：逐个读取值
            if (value < 0) {
                continue;          // 跳过本轮剩余代码
            }
            if (value == 7) {
                break;             // 立刻退出整个循环
            }
            System.out.println(value);
        }
    }
}
```

Python 的 `for value in values:` 对应 Java 的 enhanced for。它适合读取每个元素；若要改写数组的某个位置、获取下标或倒序，使用普通 `for`。

### 常见错误

- 用 `i <= arr.length`，造成最后一次访问 `arr[arr.length]` 越界。
- 忘记 `i++`，导致无限 `while`/`for` 循环。
- 以为 enhanced for 的 `value` 是数组中可替换的位置；给 `value` 赋值不会修改数组。
- 在循环里修改 `ArrayList` 却没有处理下标变化。

### 🧪 Practice

#### Level 1 — 基础

1. `for (int i = 1; i <= 3; i++)` 打印哪些数？
2. Java 的 `i--` 做什么？
3. `break` 与 `continue` 分别影响什么？

#### Level 2 — AP CSA 风格

4. 写普通 `for` 循环打印数组 `a` 的所有下标。
5. 用 `while` 计算 1 到 5 的和。
6. 用 enhanced for 求 `int[] nums` 的元素总和。

#### Level 3 — Challenge

7. 为什么检查数组元素的循环常写 `i < arr.length` 而不是 `i <= arr.length`？
8. 写一个从 10 倒数到 0（包括 0）的循环。

<details>
<summary>本章答案、提示与解释</summary>

1. `1, 2, 3`。
2. 令 `i` 减一。
3. `break` 结束循环；`continue` 跳到下一轮。
4. `for (int i = 0; i < a.length; i++) { System.out.println(i); }`。
5. 初始化 `int sum = 0, i = 1;`，在 `while (i <= 5)` 中加上 `i` 再 `i++`。
6. `int sum = 0; for (int n : nums) { sum += n; }`。
7. 合法下标是 `0` 到 `arr.length - 1`；`arr.length` 本身不合法。
8. `for (int i = 10; i >= 0; i--) { System.out.println(i); }`。
</details>

---

## 7. 方法 Methods

Python 用 `def` 定义函数。Java 中通常称为 method（方法），因为它写在 class 内；声明还要写访问权限、是否 `static`、返回类型和每个参数的类型。

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

```java
public class Main {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(add(2, 3));
    }
}
```

### 拆解 `public static int add(int a, int b)`

| 部分 | 含义 | Python 对照 |
|---|---|---|
| `public` | 可被其他类调用 | 公开的函数接口 |
| `static` | 属于 `Main` 类，不需要对象 | 类上的工具函数 / `@staticmethod` 的近似 |
| `int` | 这个方法必须返回一个整数 | Python 从 `return` 值推断 |
| `add` | 方法名 | `def add` |
| `int a`, `int b` | 类型 + 参数名 | `a, b` |
| `return` | 结束方法并交回一个值 | 相同概念，但返回值须匹配声明类型 |

**parameter（形参）**是定义处的 `int a`；**argument（实参）**是调用 `add(2, 3)` 中的 `2`、`3`。`void` 方法完成工作但不交回值：

```java
public class Main {
    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    public static void main(String[] args) {
        greet("Lin");
    }
}
```

### Method overloading：同名，不同参数表

Java 可让同一个名字有不同的参数类型或数量；编译器从调用参数决定选哪个。这叫 overload（重载），不是 Python 的“后一个定义覆盖前一个定义”。

```java
public class Main {
    public static int square(int n) {
        return n * n;
    }

    public static double square(double n) {
        return n * n;
    }

    public static void main(String[] args) {
        System.out.println(square(4));
        System.out.println(square(2.5));
    }
}
```

返回类型**单独不同**不能构成重载：`int f()` 和 `double f()` 不可同时存在，因为 `f()` 调用本身无法选定版本。

**AP CSA 重要程度：极高。** FRQ 会要求你按给定的方法签名（method header）编写方法；不要随意改返回类型、参数次序或可见性。

### 常见错误

- 写 Python 的 `def`、冒号和无类型参数。
- `int` 方法某条路径没有 `return`。
- 在 `void` 方法内写 `return value;`。
- 调用时传入类型或参数数量不匹配。

### 🧪 Practice

#### Level 1 — 基础

1. `void` 方法向调用者返回什么？
2. 写一个接收 `int n`、返回 `n + 1` 的方法头。
3. `add(int a, int b)` 中 `a`、`b` 是 parameter 还是 argument？

#### Level 2 — AP CSA 风格

4. 写 `public static boolean isPositive(int n)`。
5. 写一个 `void` 方法 `printStars(int count)`，每行打印一个 `*`。
6. 若方法声明为 `double half(int n)`，`return n / 2;` 有什么问题？

#### Level 3 — Challenge

7. 给 `square` 增加一个接收两个 `int`、返回其和的同名重载是否合理？为什么？
8. 比较 parameter 和 argument，分别给一个例子。

<details>
<summary>本章答案、提示与解释</summary>

1. 不返回值；`void` 方法只是执行动作。
2. `public static int next(int n)`，方法体应 `return n + 1;`。
3. parameter（形参）。
4. `return n > 0;`。
5. 用 `for (int i = 0; i < count; i++)`，循环体中 `System.out.println("*");`。
6. `n / 2` 先做整数除法；应 `return n / 2.0;` 或 `return (double) n / 2;`。
7. 不合理作为“重载”例子：它仍是一个参数的 `int` 方法，和 `square(int)` 有相同参数表，会冲突；方法名、参数列表必须不同。
8. `int n` 是 parameter；调用 `next(9)` 中的 `9` 是 argument。
</details>

---

## 8. String

`String` 在 Java 中是一个对象，不是 Python 内建 `str` 的完全同义替换。最明显的信号是：很多操作写成对象后的方法调用。

```python
name = "Lin"
len(name)       # 3
name[0]         # "L"
name[1:3]       # "in"
name.find("i") # 1
```

```java
public class Main {
    public static void main(String[] args) {
        String name = "Lin";
        System.out.println(name.length());      // 3
        System.out.println(name.charAt(0));     // 'L'
        System.out.println(name.substring(1, 3)); // "in"，末端不包含
        System.out.println(name.indexOf("i")); // 1
    }
}
```

| Python 想法 | Java 写法 | 关键差别 |
|---|---|---|
| `len(s)` | `s.length()` | String 是方法，带 `()` |
| `s[i]` | `s.charAt(i)` | 返回 `char` |
| `s[start:end]` | `s.substring(start, end)` | `end` 不包含 |
| `s[start:]` | `s.substring(start)` | 到结尾 |
| `s.find(x)` | `s.indexOf(x)` | 找不到时都是 `-1` |
| `s.upper()` | `s.toUpperCase()` | Java 方法名不同 |
| `s.lower()` | `s.toLowerCase()` | Java 方法名不同 |
| `s == t` | `s.equals(t)` | Java 必须比较内容 |

### `equals`、`compareTo` 和 `==`

```java
public class Main {
    public static void main(String[] args) {
        String a = new String("hello");
        String b = new String("hello");
        System.out.println(a == b);         // false：不是同一对象
        System.out.println(a.equals(b));    // true：字符内容相同
        System.out.println(a.compareTo(b)); // 0：字典序相同
    }
}
```

`compareTo` 返回负数、0 或正数，分别表示当前 String 在字典序中小于、等于或大于参数。不要死记确切负数；AP CSA 常考的是符号与 `0`。

String 是 immutable（不可变）的：`name.toUpperCase()` 产生新 String，不会修改 `name`。

```java
String name = "Lin";
name.toUpperCase();
System.out.println(name); // 仍是 Lin
name = name.toUpperCase();
```

### 常见错误

- `str.length` 或 `str.length[]`；Java String 要 `str.length()`。
- `name[0]`；使用 `name.charAt(0)`。
- `==` 比较 String 内容。
- 忘记 `substring` 的结束下标不包含。

### 🧪 Practice

#### Level 1 — 基础

1. `"AP CSA".length()` 是多少？
2. 写出读取 `word` 第一个字符的 Java 表达式。
3. 哪个方法把 String 转成小写？

#### Level 2 — AP CSA 风格

4. `String s = "computer"; s.substring(1, 4)` 得到什么？
5. 写条件判断 `word` 是否等于 `"java"`。
6. 找到 `text` 中第一次出现 `"a"` 的下标；若找不到会得到什么？

#### Level 3 — Challenge

7. 写方法体返回字符串 `s` 的最后一个字符。
8. `String s = "hi"; s.toUpperCase();` 后 `s` 是什么？为什么？

<details>
<summary>本章答案、提示与解释</summary>

1. `6`，空格也是字符。
2. `word.charAt(0)`。
3. `toLowerCase()`。
4. `"omp"`，取下标 1、2、3。
5. `word.equals("java")`；若 `word` 可能为 `null`，可写 `"java".equals(word)`。
6. `text.indexOf("a")`；找不到为 `-1`。
7. `return s.charAt(s.length() - 1);`，最后下标是长度减一。
8. 仍是 `"hi"`；String 不可变，必须把返回的新 String 赋回 `s`。
</details>

---

## 9. 数组 Arrays

Python list 能增长、可混合类型；Java array 创建后长度固定，通常保存一种元素类型。它很适合 AP CSA 的“按下标处理一组数据”。

```python
numbers = [1, 2, 3, 4]
numbers[0] = 9
print(len(numbers))
```

```java
public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4};
        numbers[0] = 9;
        System.out.println(numbers.length); // 注意：没有 ()
    }
}
```

### 创建、初始化、访问

```java
public class Main {
    public static void main(String[] args) {
        int[] scores = new int[3]; // {0, 0, 0}
        scores[0] = 90;
        scores[1] = 80;
        scores[2] = 100;

        for (int i = 0; i < scores.length; i++) {
            System.out.println(scores[i]);
        }
    }
}
```

| Python list | Java array |
|---|---|
| `len(numbers)` | `numbers.length` |
| `numbers[i]` | `numbers[i]` |
| `numbers.append(x)` | 无直接对应；数组长度不能增长 |
| 可混合类型（虽不推荐） | 元素类型固定，如 `int[]` |
| `for x in numbers` | `for (int x : numbers)` |

enhanced for 是读取元素的好方式：

```java
for (int number : numbers) {
    System.out.println(number);
}
```

但它没有下标。且下面的 `number = 0` 只改循环变量，不会改数组；要改数组应使用下标循环 `numbers[i] = 0;`。

**AP CSA 重要程度：极高。** 你需要能写遍历、求和、最大值、替换元素和下标边界。

### 常见错误

- 写 `numbers.length()`；数组属性是 `.length`。
- 访问 `numbers[numbers.length]`；最后一个位置是 `numbers.length - 1`。
- 指望数组自动变长。
- 以为 `for (int n : numbers) { n++; }` 能修改数组。

### 🧪 Practice

#### Level 1 — 基础

1. 创建含 `2, 4, 6` 的 `int[]`。
2. 一个长度为 5 的数组最后一个合法下标是多少？
3. 数组长度的 Java 写法是什么？

#### Level 2 — AP CSA 风格

4. 写循环把 `arr` 的每个元素打印出来。
5. 写循环把 `arr` 所有元素加 1。
6. 用 enhanced for 求数组最小值前，为什么要先用一个元素初始化 `min`？

#### Level 3 — Challenge

7. 写代码统计 `arr` 中偶数的数量。
8. 为什么 `new int[4]` 的所有元素开始时是 0，而局部 `int x;` 不能直接打印？

<details>
<summary>本章答案、提示与解释</summary>

1. `int[] values = {2, 4, 6};`。
2. `4`。
3. `arr.length`。
4. `for (int i = 0; i < arr.length; i++) { System.out.println(arr[i]); }`。
5. 用下标：`arr[i] = arr[i] + 1;`；enhanced for 不会改原数组元素。
6. `int min = arr[0];` 给出真实的起点；任意硬编码初值可能在所有数据更大/更小时错误。
7. `int count = 0; for (int n : arr) { if (n % 2 == 0) { count++; } }`。
8. 数组对象创建时会初始化元素；局部变量则必须在使用前被显式赋值。
</details>

---

## 10. ArrayList

当 Python 的 `list` 会不断 `append` 时，Java 中通常应想起 `ArrayList`。它是可增长的对象集合，需要导入并写明元素类型。

```python
numbers = []
numbers.append(10)
numbers.remove(10)  # 按值删除
len(numbers)
```

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(10);
        numbers.remove(0); // Java：这里的 0 是下标，不是值 10
        System.out.println(numbers.size());
    }
}
```

### 拆解创建语句

```java
ArrayList<Integer> numbers = new ArrayList<>();
```

- `ArrayList`：可变长度的列表类。
- `<Integer>`：泛型，告诉 Java 此列表只保存整数对象。基础 `int` 要写成包装类型 `Integer`。
- `new`：创建一个新对象；Python 的 `[]` 也创建了新 list，只是没有写 `new`。
- `ArrayList<>()`：调用构造器；右侧 `<>` 让编译器从左边推断 `Integer`。

| Python list | Java `ArrayList<E>` | 注意 |
|---|---|---|
| `items.append(x)` | `items.add(x)` | 加到末尾 |
| `items[i]` | `items.get(i)` | 访问方法不同 |
| `items[i] = x` | `items.set(i, x)` | 替换方法 |
| `len(items)` | `items.size()` | 带 `()` |
| `items.pop(i)` | `items.remove(i)` | 按下标删除 |
| `items.remove(value)` | `items.remove(Integer.valueOf(value))` | 避免和下标重载混淆 |

### Array vs ArrayList

| 选择 | `int[]` | `ArrayList<Integer>` |
|---|---|---|
| 长度 | 固定 | 可增长/缩小 |
| 长度写法 | `arr.length` | `list.size()` |
| 访问 | `arr[i]` | `list.get(i)` |
| 基础整数 | 直接存 `int` | 使用 `Integer`（自动装箱） |
| AP CSA | 数组题、二维数组 | 常见类库与集合操作题 |

### 常见错误

- 忘记 `import java.util.ArrayList;`。
- 写 `ArrayList<int>`；应为 `ArrayList<Integer>`。
- 把 `remove(3)` 当作删除值 3；若列表是 `Integer`，它优先表示删下标 3。
- 使用 `.length` 或 `[i]`。

### 🧪 Practice

#### Level 1 — 基础

1. 创建空的 `ArrayList<String>`。
2. 向 `names` 末尾添加 `"Ada"`。
3. 读取 `names` 的第 0 个元素。

#### Level 2 — AP CSA 风格

4. `names.size()` 与 `names.length` 哪个正确？
5. 把 `nums` 下标 2 的元素替换为 99。
6. 为什么 `ArrayList<Integer>` 不写成 `ArrayList<int>`？

#### Level 3 — Challenge

7. `ArrayList<Integer> list = [10, 20, 30]` 这种写法为什么错？写出正确创建法。
8. 删除整数值 5（而不是第 5 个位置）的安全写法是什么？

<details>
<summary>本章答案、提示与解释</summary>

1. `ArrayList<String> names = new ArrayList<>();`，并导入 `java.util.ArrayList`。
2. `names.add("Ada");`。
3. `names.get(0)`。
4. `names.size()`；`ArrayList` 的长度是方法。
5. `nums.set(2, 99);`。
6. 泛型只能放引用类型；`Integer` 是 `int` 的包装类型，Java 会常常自动转换。
7. 正确是 `ArrayList<Integer> list = new ArrayList<>();`，随后用三次 `.add(...)`，或 `new ArrayList<>(Arrays.asList(10, 20, 30))`（后者需要导入）。
8. `list.remove(Integer.valueOf(5));`；它强制选择按对象值删除的重载。
</details>

---

## 11. 类与对象 Classes & Objects

Python 和 Java 都使用 class；Java 更强调字段的类型、访问权限和构造器。下面是功能相近的写法：

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello")
```

```java
public class Main {
    public static void main(String[] args) {
        Student student = new Student("Lin", 16);
        student.sayHello();
        System.out.println(student.getName());
    }
}

class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void sayHello() {
        System.out.println("Hello");
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```

### 逐项理解

| Java 概念 | 在例子中 | Python 连接 |
|---|---|---|
| class | `class Student` | `class Student:` |
| object | `new Student(...)` 的结果 | `Student(...)` 创建的实例 |
| field / instance variable | `private String name` | `self.name` |
| constructor | `public Student(...)` | `__init__` |
| instance method | `sayHello()` | `def say_hello(self)` |
| `this` | `this.name = name` | 明确写出的 `self` 角色 |
| `private` | 外部代码不能直接访问字段 | Python 约定的 `_name` 更严格的版本 |
| getter / setter | `getName` / `setAge` | 受控读取/修改属性 |

构造器名必须和类名相同，且没有返回类型（连 `void` 都没有）。`this.name = name;` 左边是对象字段，右边是传入的 parameter。Java 常将字段设为 `private`，再暴露需要的 public 方法；这叫 encapsulation（封装），让对象自己维护合理状态。

### 常见错误

- 把构造器写成 `void Student(...)`；这样它不再是构造器。
- 忘记 `new`：`Student s = Student("Lin", 16);` 错。
- 从 `static main` 直接调用非 static 方法却没有对象。
- 字段名和参数名相同时漏 `this`，结果只是给参数自己赋值。

### 🧪 Practice

#### Level 1 — 基础

1. 在 Java 中创建对象通常使用哪个关键字？
2. `this` 在实例方法/构造器中通常指什么？
3. constructor 的名字必须与什么相同？

#### Level 2 — AP CSA 风格

4. 为 `Book` 写一个有 `private String title` 字段的类框架。
5. 为字段 `pages` 写 getter `getPages`。
6. 为什么推荐把实例字段设为 `private`？

#### Level 3 — Challenge

7. 写构造器，把 `String name` 参数存入同名字段。
8. `Student a = new Student("A", 15); Student b = a;` 后，`a` 和 `b` 有几个 `Student` 对象？

<details>
<summary>本章答案、提示与解释</summary>

1. `new`。
2. 当前这个对象；它类似 Python 中显式传入的 `self`。
3. 类名。
4. `class Book { private String title; }`；在完整 `Main.java` 中它可作为非 public 的第二个类。
5. `public int getPages() { return pages; }`。
6. 封装：外部代码不能任意写入不合理的字段值，类可通过方法验证或控制修改。
7. `public Student(String name) { this.name = name; }`。
8. 一个；`b = a` 复制引用，两者指向同一个对象。
</details>

---

## 12. static

Python 中你可以把工具函数放在模块顶层；Java 的所有方法都在类中。`static` 用来表示成员属于**类本身**，不属于某一个特定对象。

```java
public class Main {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println(Main.add(1, 2));
    }
}
```

`main` 是 static，因为 JVM 启动程序时还没有你创建的 `Main` 对象。`Math.sqrt(9)` 也能直接用类名调用，因为 `sqrt` 是 static 方法。

与之相反，学生打招呼需要“哪个学生”的数据：

```java
public class Main {
    public static void main(String[] args) {
        Student student = new Student("Lin");
        student.sayHello();
    }
}

class Student {
    private String name;

    public Student(String name) {
        this.name = name;
    }

    public void sayHello() {
        System.out.println("Hello, " + name);
    }
}
```

### class variable vs instance variable

```java
class Counter {
    private static int totalCreated = 0; // 所有 Counter 对象共享
    private int value = 0;               // 每个对象各自有一份

    public Counter() {
        totalCreated++;
    }

    public static int getTotalCreated() {
        return totalCreated;
    }
}
```

Python 的 class attribute 和 `@staticmethod` 是有用类比，但不要过度套用：Java 编译器会严格限制 static 方法不能直接使用某个对象的实例字段，因为它不知道“是哪一个对象”。

**AP CSA 重要程度：高。** 能区分 `Class.method()` 与 `object.method()`，并按题目方法头写 `static` 或不写。

### 常见错误

- 在 static 方法中直接写实例字段 `name`。
- 用类名调用实例方法，如 `Student.sayHello()`。
- 以为 `static` 表示“不会改变”；那是 `final` 的概念之一。
- 忘记 `main` 必须是 static。

### 🧪 Practice

#### Level 1 — 基础

1. `static` 方法属于类还是某个对象？
2. `Math.random()` 为什么可以不创建 `Math` 对象？
3. `main` 为什么是 static？

#### Level 2 — AP CSA 风格

4. `Student s = new Student(); s.greet();` 中 `greet` 应是 static 还是实例方法（假设它使用学生姓名）？
5. 写一个 static 方法头：接收两个 `int`，返回较大者。
6. 为什么 static 方法不能直接读取 `private String name` 这样的实例字段？

#### Level 3 — Challenge

7. 一个 `static int count` 被创建的每个对象共享吗？
8. 将 Python 顶层工具函数 `def clamp(x): ...` 放进 Java `Main` 时，通常应声明成什么？

<details>
<summary>本章答案、提示与解释</summary>

1. 类。
2. `random` 是 `Math` 类的 static 方法。
3. JVM 需要在没有现成对象时调用程序入口。
4. 实例方法，因为它依赖“这个学生”的姓名。
5. `public static int max(int a, int b)`；方法体可用 `if` 或 `Math.max`。
6. 它没有 `this`，不知道应该读取哪个对象的 `name`。
7. 是；它属于类，所有对象看到同一份值。
8. 通常是 `public static` 方法，便于 `main` 直接调用。
</details>

---

## 13. 继承 Inheritance

继承让一个新类复用、更具体化另一个类的共同特征。Python 用 `class Dog(Animal):`；Java 用 `extends`。

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof")
```

```java
public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Mochi");
        dog.speak();
    }
}

class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void speak() {
        System.out.println("...");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(getName() + " says Woof");
    }
}
```

| 概念 | Java | Python 连接 |
|---|---|---|
| superclass / parent | `Animal` | `Animal` |
| subclass / child | `Dog extends Animal` | `class Dog(Animal)` |
| inheritance | `extends` | 括号中的父类 |
| overriding（重写） | 同名、同参数表的新实现 | 子类重新定义方法 |
| `super(...)` | 调用父类构造器 | `super().__init__(...)` |
| `super.method()` | 调用父类版本 | `super().method()` |

### 构造器的关键顺序

创建 `Dog` 时，`Animal` 的那部分也必须先正确初始化。因此子类构造器的第一条语句通常是 `super(...)`。如果父类没有无参数构造器，你不能跳过它。

`@Override` 不一定是考试必写的语法，但强烈推荐写：编译器会验证你真的重写了父类方法，而不是拼错了方法名或参数。

AP CSA 要你能读懂“一个 `Animal` 引用实际指向 `Dog`”的多态（polymorphism）代码。例如 `Animal pet = new Dog("Mochi"); pet.speak();` 实际调用的是 `Dog` 的 `speak`。先记住：**引用类型决定你能通过变量调用哪些方法；实际对象类型决定被重写的方法运行哪个版本。**

### 常见错误

- 写 Python 的 `class Dog(Animal)`，而不是 `extends`。
- 子类构造器漏 `super(...)`，尤其父类没有无参构造器时。
- 重写时改变参数列表；这会 overload，不是 override。
- 将 `private` 父类字段直接在子类中访问；应使用 getter 或受保护的设计。

### 🧪 Practice

#### Level 1 — 基础

1. Java 表示继承的关键字是什么？
2. 父类和子类分别也称为什么？
3. `super(...)` 在构造器中做什么？

#### Level 2 — AP CSA 风格

4. 让 `Cat` 继承 `Animal`，写类头。
5. 什么条件下子类的 `draw()` 算重写而不是重载？
6. `Animal a = new Dog("Rex"); a.speak();` 若 `Dog` 重写了 `speak`，运行哪一个？

#### Level 3 — Challenge

7. 为什么父类字段常设为 private，子类通过 getter 使用？
8. 写一个 `Dog` 构造器片段，接收 `String name` 并调用父类构造器。

<details>
<summary>本章答案、提示与解释</summary>

1. `extends`。
2. superclass（父类）和 subclass（子类）。
3. 调用父类构造器来初始化继承来的部分。
4. `class Cat extends Animal { ... }`。
5. 方法名、参数类型和顺序都相同（且返回类型兼容）；只换了实现。
6. `Dog` 的 `speak`，这是动态分派/多态。
7. 保持封装，让父类自己控制字段读取或未来实现；子类不依赖内部存储细节。
8. `public Dog(String name) { super(name); }`。
</details>

---

## 14. 二维数组 2D Arrays

二维数组是“数组的数组”。它非常像 Python 的 list of lists，但 Java 要把元素类型和两个方括号写出来。

```python
matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[1][0])  # 3
```

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2},
            {3, 4}
        };
        System.out.println(matrix[1][0]); // 3
    }
}
```

### 两个长度、两个下标

- `matrix.length`：行数（outer array 的长度）。
- `matrix[row].length`：该行的列数。
- `matrix[row][col]`：先选行，再选该行中的列。

不必假定每行同长；Java 可有 jagged array（参差数组）。因此嵌套循环的内层条件要写 `matrix[row].length`，而不是武断地使用第一行的长度。

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5}, {6}};
        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[row].length; col++) {
                System.out.println(matrix[row][col]);
            }
        }
    }
}
```

### Python → Java 对照

| 操作 | Python | Java |
|---|---|---|
| 行数 | `len(matrix)` | `matrix.length` |
| 某行列数 | `len(matrix[r])` | `matrix[r].length` |
| 元素 | `matrix[r][c]` | `matrix[r][c]` |
| 遍历 | 两层 `for` | 两层 `for`，注意上界 |

**AP CSA 重要程度：极高。** 常见任务：遍历所有格、按行/列求和、查找值、替换满足条件的元素。

### 常见错误

- 写 `matrix.length()`。
- 内层用 `matrix.length`，把行数误当列数。
- 下标顺序混淆，把 `[row][col]` 写反。
- 假设所有行长度相同。

### 🧪 Practice

#### Level 1 — 基础

1. `int[][] a = {{1, 2}, {3, 4}};` 中 `a.length` 是多少？
2. `a[0].length` 是多少？
3. `a[1][0]` 的值是多少？

#### Level 2 — AP CSA 风格

4. 写嵌套循环打印二维数组的每个元素。
5. 写代码求 `grid` 所有元素总和。
6. 如何创建 3 行、4 列的 `int` 二维数组？

#### Level 3 — Challenge

7. 为什么内层循环应写 `c < grid[r].length`？
8. 写代码把 `grid` 所有负数改成 0。

<details>
<summary>本章答案、提示与解释</summary>

1. `2`，有两行。
2. `2`。
3. `3`。
4. 外层 `r < a.length`，内层 `c < a[r].length`，打印 `a[r][c]`。
5. `int sum = 0;`，在双层循环中写 `sum += grid[r][c];`。
6. `int[][] grid = new int[3][4];`。
7. 各行可能长度不同；它精确限制当前行的合法列下标。
8. 在双层循环中：`if (grid[r][c] < 0) { grid[r][c] = 0; }`。
</details>

---

## 15. 递归 Recursion

递归是方法调用自己来解决规模更小的同类问题。Python 和 Java 的思路相同；Java 只是写出类型、花括号和分号。

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
```

```java
public class Main {
    public static void countdown(int n) {
        if (n == 0) {
            return;
        }
        System.out.println(n);
        countdown(n - 1);
    }

    public static void main(String[] args) {
        countdown(3);
    }
}
```

### 每个可靠递归都要有两部分

1. **Base case（基本情况）**：不再递归的停止条件，例如 `n == 0`。
2. **Recursive case（递归情况）**：把问题变小后调用自己，例如 `countdown(n - 1)`。

每个尚未完成的调用都会留在 call stack（调用栈）上，直到更深层调用返回。以阶乘为例：

```java
public class Main {
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        System.out.println(factorial(4)); // 24
    }
}
```

从 `factorial(4)` 向下会得到 `4 * 3 * 2 * 1 * factorial(0)`；基本情况给出 1，返回时逐层完成乘法。

**AP CSA 重要程度：高。** 重点通常是追踪调用、写正确 base case，以及理解返回值如何组合；不要只把递归当“神奇循环”。

### 常见错误

- 没有 base case，或 base case 永远不会到达，导致 `StackOverflowError`。
- 递归调用没有让问题变小，如写 `countdown(n)`。
- `int` 方法的 base case 忘记返回 `int`。
- 将“递归前打印”和“递归后打印”混淆；输出顺序不同。

### 🧪 Practice

#### Level 1 — 基础

1. 递归的两个必需部分是什么？
2. `factorial(0)` 应返回什么？
3. 哪个错误通常意味着递归没有停下来？

#### Level 2 — AP CSA 风格

4. 写一个递归 `sumTo(int n)`，返回 `1 + ... + n`，base case 为 `n == 0`。
5. `countdown(2)` 的输出顺序是什么？
6. 在递归调用**之后**打印 `n`，与之前打印有什么差别？

#### Level 3 — Challenge

7. 追踪 `factorial(3)` 的所有调用和返回。
8. 为什么 `return n + sumTo(n);` 是错误的递归式？

<details>
<summary>本章答案、提示与解释</summary>

1. base case 和能缩小问题的 recursive case。
2. `1`，乘法的单位元。
3. `StackOverflowError`。
4. `if (n == 0) { return 0; } return n + sumTo(n - 1);`。
5. `2`、`1`；到 0 时直接返回，不打印 0。
6. 前打印在向下调用时输出，后打印在调用返回时逆序输出。
7. 调用 3→2→1→0；0 返回 1，1 返回 1，2 返回 2，3 返回 6。
8. 参数没有变小，递归会永远以同一个 `n` 调用自己。
</details>

---

## 16. AP CSA 常用类

这些不是需要背完的“大库”，而是 AP CSA 最常见的工具。读题时先看变量类型，再知道可以调用哪些方法。

### `Math`

`Math` 的方法是 static，用类名调用。

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(Math.abs(-4));   // 4
        System.out.println(Math.max(3, 8)); // 8
        System.out.println(Math.min(3, 8)); // 3
        System.out.println(Math.pow(2, 3)); // 8.0
        System.out.println(Math.sqrt(9));   // 3.0
        System.out.println(Math.random());  // [0.0, 1.0)
    }
}
```

要得到 `[low, high]` 的随机整数，可写：`(int) (Math.random() * (high - low + 1)) + low`。括号、转换和 `+ 1` 都是常考细节。

### `String` 与 `ArrayList`

复习最常用的：

| 类型 | 常用操作 |
|---|---|
| `String` | `length()`、`substring()`、`indexOf()`、`equals()`、`compareTo()`、`charAt()` |
| `ArrayList<E>` | `add()`、`get()`、`set()`、`remove()`、`size()` |

它们都是对象，因此这些调用有圆点和圆括号；但 array 的 `.length` 是例外，它不是方法。

### `Random`

`Random` 是另一种随机数工具。它需要导入、创建对象，且上界**不包含**：

```java
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random generator = new Random();
        int roll = generator.nextInt(6) + 1; // 1 到 6
        System.out.println(roll);
    }
}
```

### `Scanner`

`Scanner` 从标准输入读值。在许多 AP CSA 课堂练习中常见；AP 考试题会明确给出其可用性。注意 `nextInt()` 后若接着 `nextLine()`，要处理留下的换行。

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Name: ");
        String name = input.nextLine();
        System.out.println("Hello, " + name);
    }
}
```

### 常见错误

- 写 `Math math = new Math()`；`Math` 主要通过 static 方法用。
- 忘记 `Random.nextInt(n)` 得到 `0` 到 `n - 1`，不含 n。
- `nextInt()` 后马上 `nextLine()`，读到空字符串。
- 混淆 `ArrayList.size()`、`String.length()`、`array.length`。

### 🧪 Practice

#### Level 1 — 基础

1. `Math.max(4, 9)` 是多少？
2. `Random.nextInt(5)` 的可能值有哪些？
3. `String`、array、`ArrayList` 的长度写法分别是什么？

#### Level 2 — AP CSA 风格

4. 用 `Math.random()` 产生 1 到 10（含）的整数。
5. `generator.nextInt(6) + 1` 为什么是骰子点数？
6. 用 `Scanner` 读取一整行文字应该调用什么？

#### Level 3 — Challenge

7. 为什么 `Math.pow(2, 4)` 的返回类型值得注意？
8. `nextInt()` 后要读取下一整行，常见补救步骤是什么？

<details>
<summary>本章答案、提示与解释</summary>

1. `9`。
2. `0, 1, 2, 3, 4`。
3. `s.length()`、`arr.length`、`list.size()`。
4. `(int) (Math.random() * 10) + 1`。
5. `nextInt(6)` 给 0–5，加一变 1–6。
6. `nextLine()`。
7. 它返回 `double`，即使数学结果恰好为整数。
8. 先调用一次额外的 `input.nextLine()` 消耗当前行末尾的换行，再读真正的文字行。
</details>

---

## 17. Java 特有概念

这一章把 Python 用户常感到“为什么 Java 要我管这个”的概念集中起来。把它们看作 Java 让程序规则更明确的工具。

| 概念 | Java 含义 | Python 类比 / 要点 |
|---|---|---|
| `static` | 属于类，不属于某对象 | 类属性或 staticmethod 的近似 |
| `final` | 变量只能赋值一次 | 接近“不重新绑定这个名字”；不是深度不可变 |
| primitive / reference | 直接值 vs 指向对象的引用 | Python 中多为对象；Java 明确区分 |
| `null` | 没有指向任何对象 | `None` |
| casting | 显式改看作另一数值类型 | `int(3.8)` 的受控对应 |
| autoboxing | `int` 与 `Integer` 的自动转换 | Python 不区分这对类型 |
| `this` | 当前对象 | `self` 的角色 |
| `super` | 父类部分 / 父类方法 | `super()` |
| access modifiers | `public`、`private` 等访问边界 | 比 Python 约定更强制 |
| object reference | 变量可共同指向同一对象 | Python 赋值同样常共享可变对象 |

### `final` 不等于对象不可变

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        final int days = 7;
        // days = 8; // 编译错误

        final ArrayList<String> names = new ArrayList<>();
        names.add("Lin");       // 可以：对象内部可以变
        // names = new ArrayList<>(); // 不可以：引用不能重新指向新列表
    }
}
```

### `null` 与 `NullPointerException`

```java
public class Main {
    public static void main(String[] args) {
        String message = null;
        // System.out.println(message.length()); // NullPointerException
        if (message != null) {
            System.out.println(message.length());
        }
    }
}
```

`null` 只能用于引用类型，不能给 `int`。它表示“目前没有对象”，不是空 String `""`、不是数字 0。调用 `null` 上的方法会出现 `NullPointerException`。

### casting 与 autoboxing

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        double price = 8.9;
        int whole = (int) price; // 8：直接截去小数，不四舍五入

        ArrayList<Integer> values = new ArrayList<>();
        values.add(7);           // autoboxing: int -> Integer
        int x = values.get(0);   // unboxing: Integer -> int
        System.out.println(x);
    }
}
```

### 引用共享：和 Python 可变 list 的别名一样

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();
        a.add("first");
        ArrayList<String> b = a;
        b.add("second");
        System.out.println(a); // [first, second]
    }
}
```

这与 Python 的 `b = a` 对 list 的效果相似；没有复制对象。若题目要求独立副本，必须明确创建。

### 常见错误

- 以为 `final ArrayList` 不能 `.add()`。
- 把 `null` 当成 `""` 或 0。
- 以为 `(int) 3.9` 会四舍五入为 4；实际为 3。
- 以为 `b = a` 会复制列表。

### 🧪 Practice

#### Level 1 — 基础

1. Java 的 `None` 对应什么？
2. `(int) 6.8` 是多少？
3. `this` 通常指向谁？

#### Level 2 — AP CSA 风格

4. `final String s = "hi";` 后能否 `s = "bye"`？
5. `String s = null; s.length();` 有何风险？
6. 为什么 `ArrayList<Integer>` 使用 `Integer`？

#### Level 3 — Challenge

7. `ArrayList<Integer> b = a; b.set(0, 9);` 会不会影响 `a`？
8. `private` 比 Python 的单下划线命名约定多提供了什么？

<details>
<summary>本章答案、提示与解释</summary>

1. `null`。
2. `6`，向零截断。
3. 当前对象。
4. 不能；`final` 变量不能重新赋值。
5. `NullPointerException`，因为没有 String 对象可调用 `length()`。
6. 泛型只接受引用类型；`Integer` 是 `int` 的包装类。
7. 会，若 `a` 和 `b` 由该赋值而来则指向同一列表对象。
8. 编译器强制访问限制；不符合权限的外部访问会编译失败。
</details>

---

## 18. AP CSA 高频陷阱

下面是做选择题、追踪代码和 FRQ 时最值得反复检查的十个点。

| Trap | 容易写成 / 想成 | 正确理解 |
|---|---|---|
| 1. `5 / 2` | `2.5` | 两个 `int` 相除为 `2` |
| 2. String `==` | 比文本内容 | 用 `.equals()` 比内容 |
| 3. 长度 | 都是 `.length()` | array `.length`；String `.length()`；ArrayList `.size()` |
| 4. `i++` | Python 中也可用 | Java 专用的自增写法 |
| 5. `ArrayList<Integer>` | 写 `ArrayList<int>` | 泛型需要包装类 `Integer` |
| 6. 引用与 primitive | `b = a` 一定复制 | 对象变量通常复制引用 |
| 7. off-by-one | `i <= length` | 最后下标为 `length - 1` |
| 8. nested loops | 内层不重置 | 每次外层循环，内层从头运行 |
| 9. integer division | 存到 double 就自动小数除法 | 除法在赋值前已完成 |
| 10. `null` | 像空字符串可调用方法 | 调用方法会 `NullPointerException` |

### 重点追踪示例

```java
public class Main {
    public static void main(String[] args) {
        int total = 0;
        for (int i = 0; i < 3; i++) {
            total += i;
        }
        System.out.println(total); // 0 + 1 + 2 = 3
    }
}
```

不要把循环条件读成“循环到 3”。条件是 `i < 3`，所以 3 从未进入循环体。

### 做 AP CSA 题的 30 秒检查

1. 写下每个变量的**类型和值**，不要只在脑中追踪。
2. 遇到 `/`，先看两边是不是 `int`。
3. 遇到 String，立刻检查是否错误地用了 `==`。
4. 遇到集合，辨别 `.length` / `.length()` / `.size()`。
5. 遇到循环，检查初始值、条件和更新；边界值是否刚好一次。
6. 遇到对象赋值或参数传递，问“是复制对象，还是复制引用？”

### 🧪 Practice

#### Level 1 — 基础

1. `System.out.println(7 / 2);` 输出什么？
2. array、String、ArrayList 分别如何取得长度？
3. `i++` 后 `i` 有何变化？

#### Level 2 — AP CSA 风格

4. `String a = new String("x"); String b = new String("x");` 应用什么表达式检查文字相等？
5. `for (int i = 0; i <= arr.length; i++)` 何时出错？
6. `double d = 11 / 4;` 的值是什么？

#### Level 3 — Challenge

7. `ArrayList<Integer> a = new ArrayList<>(); ArrayList<Integer> b = a; b.add(4);` 后 `a.size()` 是多少？
8. 怎样防止对可能为 `null` 的引用调用方法？

<details>
<summary>本章答案、提示与解释</summary>

1. `3`。
2. `arr.length`、`str.length()`、`list.size()`。
3. 增加 1。
4. `a.equals(b)`。
5. 当 `i == arr.length` 时访问 `arr[i]` 就会越界；条件应为 `< arr.length`。
6. `2.0`；整数除法已先得到 2。
7. `1`，两个变量指向同一 ArrayList。
8. 先用 `if (reference != null)` 检查；或在比较常量文本时让已知非 null 的常量调用 `.equals(reference)`。
</details>

---

## 19. Python → Java 快速翻译表

这一节用于写题前快速校准。它给的是“最常见 AP CSA 对应”，不是说两门语言在所有情境下完全等价。

### 输出、变量与基本类型

| Python | Java |
|---|---|
| `print(x)` | `System.out.println(x);` |
| `print(x, end="")` | `System.out.print(x);` |
| `x = 10` | `int x = 10;` |
| `price = 3.5` | `double price = 3.5;` |
| `ok = True` | `boolean ok = true;` |
| `letter = "A"`（一个字符） | `char letter = 'A';` |
| `name = "Lin"` | `String name = "Lin";` |
| `None` | `null`（只用于引用） |
| `True` / `False` | `true` / `false` |
| `type(x)` | 看声明类型；Java 通常在编译期已知 |
| `x = int(y)` | `int x = (int) y;`（注意截断） |
| `# comment` | `// comment` |

### 运算与条件

| Python | Java | 注意 |
|---|---|---|
| `a + b` | `a + b` | String 上也可拼接 |
| `a / b` | `a / b` | `int / int` 为整数除法 |
| `a // b` | `a / b`（若两边为 `int`） | Java 没有 `//` 整数除法运算符 |
| `a % b` | `a % b` | 同为取余 |
| `a ** b` | `Math.pow(a, b)` | 返回 `double` |
| `a == b`（数/文字） | primitive 用 `==`；String 用 `a.equals(b)` | 不要 String `==` |
| `a != b` | `a != b` | 引用时比较身份 |
| `a and b` | `a && b` | 两边应是 boolean |
| `a or b` | `a || b` | 两边应是 boolean |
| `not a` | `!a` | |
| `if test:` | `if (test) { ... }` | 条件必须是 boolean |
| `elif test:` | `else if (test) { ... }` | 两个词 |
| `else:` | `else { ... }` | |
| `x += 1` | `x++;` 或 `x += 1;` | `++` 是 Java 写法 |

### 循环

| Python | Java | 注意 |
|---|---|---|
| `while test:` | `while (test) { ... }` | |
| `for i in range(n):` | `for (int i = 0; i < n; i++) { ... }` | 两者都不含 n |
| `for i in range(a, b):` | `for (int i = a; i < b; i++) { ... }` | |
| `for i in range(a, b, step):` | `for (int i = a; i < b; i += step) { ... }` | 需自己处理方向/边界 |
| `for item in items:` | `for (Type item : items) { ... }` | enhanced for |
| `break` | `break;` | 退出循环 |
| `continue` | `continue;` | 跳过当前轮 |

### 方法与类

| Python | Java | 注意 |
|---|---|---|
| `def add(a, b):` | `public static int add(int a, int b) {` | 返回类型必须写出 |
| `return value` | `return value;` | 必须匹配方法返回类型 |
| 无 `return` 的函数 | `public static void method(...) { ... }` | `void` 不返回值 |
| `class Student:` | `class Student { ... }` | Java class 用花括号 |
| `def __init__(self, x):` | `public Student(Type x) { ... }` | 构造器无返回类型 |
| `self.x = x` | `this.x = x;` | |
| `Student("Lin")` | `new Student("Lin")` | 用 `new` 创建对象 |
| `obj.method()` | `obj.method();` | Java 语句常加分号 |
| `@staticmethod` | `static` 方法 | 不依赖某个对象 |
| `class Dog(Animal):` | `class Dog extends Animal {` | 继承 |
| `super().__init__(x)` | `super(x);` | 子类构造器第一条语句 |

### String

| Python | Java |
|---|---|
| `len(s)` | `s.length()` |
| `s[i]` | `s.charAt(i)` |
| `s[start:end]` | `s.substring(start, end)` |
| `s[start:]` | `s.substring(start)` |
| `s.find(part)` | `s.indexOf(part)` |
| `s.upper()` | `s.toUpperCase()` |
| `s.lower()` | `s.toLowerCase()` |
| `s == "yes"` | `s.equals("yes")` |
| `s < t`（字典序） | `s.compareTo(t) < 0` |
| `s in text` | `text.indexOf(s) >= 0` |
| `s = s.upper()` | `s = s.toUpperCase();` |

### array 与 `ArrayList`

| Python | Java array | Java `ArrayList` |
|---|---|---|
| `numbers = [1, 2, 3]` | `int[] numbers = {1, 2, 3};` | `ArrayList<Integer> n = new ArrayList<>();` |
| `len(items)` | `arr.length` | `list.size()` |
| `items[i]` | `arr[i]` | `list.get(i)` |
| `items[i] = x` | `arr[i] = x` | `list.set(i, x)` |
| `items.append(x)` | 无（长度固定） | `list.add(x)` |
| `items.pop(i)` | 无直接对应 | `list.remove(i)` |
| `for x in items:` | `for (int x : arr)` | `for (Integer x : list)` |
| 二维：`m[r][c]` | `matrix[r][c]` | 通常先学习 array 版本 |

### 必背的“三种长度”

```java
String text = "Java";
int[] array = {1, 2, 3};
ArrayList<Integer> list = new ArrayList<>();

text.length(); // 方法：String
array.length;  // 属性：array
list.size();   // 方法：ArrayList
```

### 写 Java 前的翻译清单

1. 这个 Python 变量在 Java 中应是什么类型？
2. 这是一条语句吗？若是，结尾是否需要 `;`？
3. Python 缩进块是否已转换成 `{ }`？
4. 这是 String、array 还是 ArrayList？长度和索引写法是否正确？
5. 有 `/` 时，至少一个操作数是否需要是 `double`？
6. 比较 String 时，是否用了 `.equals()`？

---

## 20. AP CSA 学习路线

下面的顺序是从“会 Python 的人最容易迁移的部分”走向“AP CSA 更看重的 Java 思维”。每阶段不要只看懂示例；至少能不看资料写出一两个小方法，才进入下一步。

```text
Java Basics
    ↓
Variables
    ↓
Conditionals
    ↓
Loops
    ↓
Methods
    ↓
String
    ↓
Arrays
    ↓
ArrayList
    ↓
Classes & Objects
    ↓
Inheritance
    ↓
2D Arrays
    ↓
Recursion
    ↓
AP CSA Practice
```

| 阶段 | 学什么 | Python 用户特别注意 | 何时算掌握 | 推荐练习 |
|---|---|---|---|---|
| 1. Java Basics | class、`main`、打印、分号、花括号 | 不再从文件顶端直接执行 | 能从零写可运行 `Main` | 输出形状、读编译错误 |
| 2. Variables | `int`、`double`、`boolean`、`String`、`char` | 每个变量先写类型；`true` 小写 | 能预测每个表达式类型 | 声明/修正类型题 |
| 3. Conditionals | 比较、`&&`、`||`、`if/else` | 不可把数字当 boolean | 能处理临界值和互斥分支 | 评分、票价、范围判断 |
| 4. Loops | `while`、普通 `for`、enhanced for | 手动写起点/终点/步长 | 能避免 off-by-one 和无限循环 | 累加、计数、搜索 |
| 5. Methods | 参数、返回值、`void`、签名 | 类型和 `return` 必须匹配 | 能按指定签名写方法 | 数字/字符串小方法 |
| 6. String | `charAt`、`substring`、`equals` | 不用 `==` 比内容 | 能追踪下标和子串边界 | 密码检查、字符统计 |
| 7. Arrays | 创建、索引、遍历、修改 | 固定长度；`.length` 无括号 | 能写遍历/最大值/替换 | FRQ 风格 array traversal |
| 8. ArrayList | `add/get/set/remove/size` | 是对象；用 `Integer` | 能安全增删并追踪下标 | 成绩/待办列表 |
| 9. Classes & Objects | 字段、构造器、方法、封装 | `this` 类似 `self`；要 `new` | 能实现一个小 class | `Student`、`Book`、`Clock` |
| 10. Inheritance | `extends`、`super`、override | 类层级要读出方法来源 | 能判断重写调用 | `Animal` / `Dog` 追踪 |
| 11. 2D Arrays | 双层循环、行列长度 | 两层下标都要有边界 | 能按行列访问和修改 | 网格求和、表格搜索 |
| 12. Recursion | base case、recursive case、调用栈 | 思路与 Python 相同，类型更明确 | 能手动追踪并补完递归 | 阶乘、字符串递归 |
| 13. AP CSA Practice | 选择题、代码追踪、FRQ | 严格按方法头和题目合同写 | 能在计时下解释、设计、实现 | 历年题 / 课堂 FRQ |

### 建议的节奏

1. 每学一章：读对照 → 输入并运行示例 → 独立完成本章 8 题。
2. 每两到三章：写一个 30–60 行的小程序，例如猜数字、成绩统计或文字分析器。
3. 从 Arrays 开始：练习“先用英文/中文写算法步骤，再翻译成 Java”。这会直接帮助 FRQ。
4. 从 Classes 开始：仔细区分“类定义要写什么”和“main 中如何创建、调用对象”。
5. 进入真题时：先做代码追踪与短方法，再做完整 FRQ；每次订正都记录是类型、边界、引用还是 String 错误。

### 开始做 AP CSA FRQ 前的自检

- 我能解释 `int / int` 与 `double / int` 的结果吗？
- 我能在不查资料时写 `for (int i = 0; i < arr.length; i++)` 吗？
- 我能说明 `arr.length`、`list.size()`、`str.length()` 的区别吗？
- 我会用 `.equals()` 比较 String 吗？
- 我能按给定 header 写一个有正确返回值的方法吗？
- 我能解释 `new`、constructor、`this` 和引用共享吗？
- 我能写 nested loop 与递归的 base case 吗？

如果其中某项还不稳，不必急着刷很多题；回到对应章节，先做一个能运行的小例子。对已经会 Python 的你来说，最难的往往不是算法，而是把熟悉的想法准确地写成 Java 的规则。掌握这些规则后，AP CSA 代码会变得非常可预测。

---

## 附录：一份可运行的综合小例子

这个小程序把类型、方法、String、ArrayList、对象和循环放在一起。请先读，再尝试自己修改为统计及格学生数。

```java
import java.util.ArrayList;

public class Main {
    public static int countPassing(ArrayList<Student> students) {
        int count = 0;
        for (Student student : students) {
            if (student.getScore() >= 60) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        students.add(new Student("Lin", 94));
        students.add(new Student("Ada", 58));

        System.out.println("Passing: " + countPassing(students));
    }
}

class Student {
    private String name;
    private int score;

    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public int getScore() {
        return score;
    }
}
```

输出为 `Passing: 1`。这里 `students` 是 `ArrayList<Student>`，循环变量 `student` 是每个 `Student` 对象；`getScore()` 返回一个 `int`，所以可以直接与 60 比较。这种“读类型 → 调方法 → 写遍历”的思路，就是 AP CSA 阅读和 FRQ 写作的核心。
