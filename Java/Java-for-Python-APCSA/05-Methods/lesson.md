# Chapter 05 — Methods

## 🎯 Learning Goals

- 从 Python `def` 写出 Java method header；
- 区分 parameter、argument、return value 与 `void`；
- 写可复用的 static 方法；
- 识别 overload 与正确的返回路径。

---

## 🐍 Python → ☕ Java

```python
def add(a, b):
    return a + b
```

```java
public static int add(int a, int b) {
    return a + b;
}
```

Java 需要声明返回类型和每个 parameter 的类型。定义里的 `a`、`b` 是 parameters；`add(2, 3)` 里的 2、3 是 arguments。

## 1. Header map

| 部分 | 含义 |
|---|---|
| `public` | 其他 class 可以调用 |
| `static` | 直接从 `Main` 调用，不需要对象 |
| `int` | 必须返回 int |
| `add` | 方法名 |
| `(int a, int b)` | parameter 列表 |

## 2. `void` 与 return

```java
public static void greet(String name) {
    System.out.println("Hello, " + name);
}
```

`void` 方法不交回一个值。非 void 方法的每条可能路径都应产生匹配类型的 `return`。

## 3. Example

```java
public class Main {
    public static boolean isEven(int n) {
        return n % 2 == 0;
    }

    public static void main(String[] args) {
        System.out.println(isEven(8));
    }
}
```

Java 可 overload：同名但 parameter **数量或类型**不同。不能只靠不同返回类型重载。

⚠️ **Common Mistakes**

- Python 风格 `def` 或漏类型；
- `int` 方法某分支没有 `return`；
- 以为 `void` 方法可以 `return 3;`；
- 方法调用参数顺序或类型不匹配。

🧠 **AP CSA Notes**：FRQ 给出的 method header 是合同。不要改变 method name、返回类型或 parameter 顺序。

✅ **Before Practice**

- 我能按题目签名写方法。
- 我能区分“打印”与“返回”。
- 我能为方法设计 0、正数、负数等测试。

📝 **Practice**：完成 [Chapter 05 Practice](./practice.md)。
