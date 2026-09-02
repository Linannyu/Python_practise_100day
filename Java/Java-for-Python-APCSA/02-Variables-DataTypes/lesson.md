# Chapter 02 — Variables & Data Types

## 🎯 Learning Goals

- 用 `int`、`double`、`boolean`、`char`、`String` 声明变量；
- 区分 primitive 与 reference 的够用模型；
- 预测算术、比较、逻辑与整数除法的结果；
- 使用 casting 与 `final`。

---

## 🐍 Python → ☕ Java

```python
x = 10
name = "Lin"
price = 3.14
passed = True
```

```java
int x = 10;
String name = "Lin";
double price = 3.14;
boolean passed = true;
```

Python 的名字会随值改变类型；Java 变量先声明类型，之后只能接收兼容的值。

## 1. Core types

| Java type | 值 | 注意 |
|---|---|---|
| `int` | `42` | 整数 |
| `double` | `3.5` | 小数 |
| `boolean` | `true` | 小写 |
| `char` | `'A'` | 一个字符、单引号 |
| `String` | `"A"` | 文本、双引号 |

`int`、`double`、`boolean`、`char` 是 primitive；`String`、array、`ArrayList` 和对象是 reference。先记住：primitive 赋值复制值，reference 赋值通常复制“指向对象的引用”。

## 2. Operators

| Python | Java | 注意 |
|---|---|---|
| `**` | `Math.pow(a, b)` | 返回 `double` |
| `and` / `or` / `not` | `&&` / `||` / `!` | 条件必须是 boolean |
| `x += 1` | `x++` 或 `x += 1` | Java 有 `++` |
| `5 / 2` → `2.5` | `5 / 2` → `2` | 两边皆为 int |

## 3. Example

```java
public class Main {
    public static void main(String[] args) {
        int total = 5 / 2;
        double exact = 5.0 / 2;
        boolean valid = total > 0 && exact < 3;
        System.out.println(total); // 2
        System.out.println(exact); // 2.5
        System.out.println(valid);
    }
}
```

Casting 是明确转换：`(int) 3.9` 得到 `3`（向零截断），不是四舍五入。`final int DAYS = 7;` 表示该变量不能重新赋值。

⚠️ **Common Mistakes**

- `String s = 'hi';`（String 要双引号）；
- 以为 `double d = 5 / 2;` 会变成 2.5；
- 写 Python 的 `True`、`and` 或 `**`；
- 忘记 `Math.pow` 是 `double`。

🧠 **AP CSA Notes**：每次追踪代码都记录变量的**类型和值**。遇到 `/`，先看操作数类型。

✅ **Before Practice**

- 我能为一个值选择合适 Java 类型。
- 我能解释 `5 / 2` 与 `5.0 / 2`。
- 我能写一个 boolean 范围条件。

📝 **Practice**：完成 [Chapter 02 Practice](./practice.md)。
