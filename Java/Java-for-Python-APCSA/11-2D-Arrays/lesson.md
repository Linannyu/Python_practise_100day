# Chapter 11 — 2D Arrays

## 🎯 Learning Goals

- 创建和读取 `int[][]`；
- 区分行数、当前行列数和元素；
- 用 nested loops 遍历二维表；
- 处理 row/column 边界与不规则行。

---

## 🐍 Python → ☕ Java

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
```

```java
int[][] matrix = {{1, 2}, {3, 4}};
System.out.println(matrix[1][0]);
```

两门语言都是先 row 后 column。Java 中 `matrix.length` 是行数；`matrix[row].length` 是那一行的列数。

## 1. Nested traversal

```java
for (int row = 0; row < matrix.length; row++) {
    for (int col = 0; col < matrix[row].length; col++) {
        System.out.println(matrix[row][col]);
    }
}
```

每次外层循环，内层 `col` 都从 0 重新开始。这正对应 Python 两层 `for`。

## 2. Rectangular and jagged

```java
int[][] rows = {{1, 2, 3}, {4}, {5, 6}};
```

Java 允许不同长度的行；所以通用代码不能把 `matrix[0].length` 当作每行长度。

## 3. Example: row total

```java
public class Main {
    public static void main(String[] args) {
        int[][] grid = {{1, 2}, {3, 4}};
        for (int row = 0; row < grid.length; row++) {
            int sum = 0;
            for (int col = 0; col < grid[row].length; col++) {
                sum += grid[row][col];
            }
            System.out.println(sum);
        }
    }
}
```

⚠️ **Common Mistakes**

- `grid.length()`；
- 将 `grid.length` 误作列数；
- 把 `[row][col]` 写反；
- 将 `sum` 放在错误的循环层级。

🧠 **AP CSA Notes**：2D array FRQ 常要求访问所有元素、计算 row/column value 或修改符合条件的格子。

✅ **Before Practice**

- 我能解释两个 `.length`。
- 我能写内层使用当前 row 长度的循环。
- 我能选择 cell、row 或 whole grid 的 accumulator 范围。

📝 **Practice**：完成 [Chapter 11 Practice](./practice.md)。
