# Chapter 06 — String

## 🎯 Learning Goals

- 使用 `length`、`charAt`、`substring`、`indexOf`、`equals` 与 `compareTo`；
- 正确计算 String 的下标和切片边界；
- 解释 String immutable；
- 避开 `==` 比文本内容的 AP CSA 陷阱。

---

## 🐍 Python → ☕ Java

```python
name = "Lin"
len(name)
name[0]
name[1:3]
```

```java
String name = "Lin";
name.length();
name.charAt(0);
name.substring(1, 3);
```

Python 的 String 操作多为函数/方括号；Java `String` 是对象，所以常调用方法。

## 1. Core methods

| Python | Java | Result |
|---|---|---|
| `len(s)` | `s.length()` | length |
| `s[i]` | `s.charAt(i)` | `char` |
| `s[a:b]` | `s.substring(a, b)` | b excluded |
| `s.find(x)` | `s.indexOf(x)` | -1 if missing |
| `s.upper()` | `s.toUpperCase()` | new String |
| `s == t` | `s.equals(t)` | content equality |

## 2. Example

```java
public class Main {
    public static void main(String[] args) {
        String word = "computer";
        System.out.println(word.substring(1, 4)); // omp
        System.out.println(word.indexOf("put")); // 3
        System.out.println(word.equals("computer"));
    }
}
```

`compareTo` 小于 0、等于 0、大于 0，分别表示字典序在参数前、相同、在参数后。String immutable：`word.toUpperCase()` 不会修改 `word`，必须赋回。

⚠️ **Common Mistakes**

- `word[0]`，应为 `word.charAt(0)`；
- `word.length`，String 要 `length()`；
- `==`；
- 误以为 `substring(a, b)` 包含 b。

🧠 **AP CSA Notes**：String FRQ 常同时考循环与下标。最后字符永远是 `s.charAt(s.length() - 1)`。

✅ **Before Practice**

- 我能写出最后字符的下标。
- 我能用 `.equals` 比较文字。
- 我知道操作 String 是否会修改原变量。

📝 **Practice**：完成 [Chapter 06 Practice](./practice.md)。
