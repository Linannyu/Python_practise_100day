# Chapter 12 — Recursion

## 🎯 Learning Goals

- 写 base case 与缩小问题的 recursive case；
- 追踪 call stack 与 return 值；
- 区分递归前/后的工作；
- 防止无限递归和错误返回类型。

---

## 🐍 Python → ☕ Java

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
```

```java
public static void countdown(int n) {
    if (n == 0) {
        return;
    }
    System.out.println(n);
    countdown(n - 1);
}
```

递归思路与 Python 相同；Java 额外要求 method header、类型、花括号和分号准确。

## 1. Two non-negotiable parts

- **Base case**：停止并给出最小问题的答案；
- **Recursive case**：调用自己，但让参数更接近 base case。

## 2. Return example

```java
public static int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

`factorial(3)` waits for `3 * factorial(2)`，直到 `factorial(0)` 返回 1；随后调用栈由内到外完成。

## 3. Order matters

```java
public static void downThenUp(int n) {
    if (n == 0) return;
    System.out.println("down " + n);
    downThenUp(n - 1);
    System.out.println("up " + n);
}
```

递归前的输出按向下调用顺序；递归后的输出按返回顺序。

⚠️ **Common Mistakes**

- 无 base case 或永远到不了它；
- 调用 `f(n)` 而不是更小的参数；
- base case return 类型不匹配；
- 将递归步骤写在 `return` 后。

🧠 **AP CSA Notes**：先手动追踪小输入（0、1、2、3），再写 general case；这比直接猜代码可靠。

✅ **Before Practice**

- 我能画出 3 层递归调用。
- 我能识别每次调用问题是否缩小。
- 我能写出 base case 的返回值。

📝 **Practice**：完成 [Chapter 12 Practice](./practice.md)。
