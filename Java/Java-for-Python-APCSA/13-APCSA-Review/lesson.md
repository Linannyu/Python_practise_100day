# Chapter 13 — AP CSA Review

## 🎯 Learning Goals

- 用 AP CSA 的类型、方法和对象模型整合解题；
- 系统追踪代码而不是凭直觉；
- 按 method header 实现 FRQ 风格方法；
- 用测试和错题记录改善下一次答案。

---

## 🐍 Python → ☕ Java

```python
total = sum(x for x in values if x > 0)
```

```java
int total = 0;
for (int x : values) {
    if (x > 0) {
        total += x;
    }
}
```

Python 可以用表达式压缩步骤；AP CSA Java 通常要求你显式展示 accumulator、循环和条件。这正好让阅卷者能评估算法。

## 1. AP CSA problem workflow

1. 圈出 types、return type、parameters 与约束。
2. 写小例子并表格追踪变量值。
3. 选择 traversal：index、enhanced for、nested loop 或 recursion。
4. 对 0、1、空/最小合法输入和边界下标检查。
5. 用题目给定的 header、不要多写不需要的 `main`。

## 2. High-value distinctions

| What you have | Correct form |
|---|---|
| String length | `s.length()` |
| array length | `arr.length` |
| ArrayList length | `list.size()` |
| String contents | `a.equals(b)` |
| random 0–5 | `new Random().nextInt(6)` |
| random 1–6 | `new Random().nextInt(6) + 1` |
| integer average | `(double) sum / count` |

## 3. Debug order

1. **Compile error**：检查 class name、types、semicolons、imports；
2. **Runtime error**：检查 `null`、index、loop bound；
3. **Wrong answer**：用一个小输入逐行追踪；
4. **Repeated mistake**：写入 `mistakes.md`，一周后重做。

## 4. Example FRQ method

```java
public static int countEven(int[] values) {
    int count = 0;
    for (int value : values) {
        if (value % 2 == 0) {
            count++;
        }
    }
    return count;
}
```

这是典型的“初始化 → 遍历 → 条件更新 → return”。保持每一步明显，比聪明但难读的压缩写法更适合 FRQ。

⚠️ **Common Mistakes**

- 不按题目 header 写方法；
- 在 String 上用 `==`；
- 在 array 上用 `length()`；
- 只测试普通输入，不测试边界；
- 看到答案后不写自己的错误规则。

🧠 **AP CSA Notes**：你不需要使用高级 Java；清晰、类型正确、边界正确的基本 Java 就能拿到分。

✅ **Before Practice**

- 我能列出三种 length 写法。
- 我能对 array/ArrayList/String 选择正确 traversal。
- 我会把失败的测试转成一个可复习的 mistake 条目。

📝 **Practice**：完成 [Chapter 13 Practice](./practice.md)。
