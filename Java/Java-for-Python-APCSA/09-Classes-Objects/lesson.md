# Chapter 09 — Classes & Objects

## 🎯 Learning Goals

- 实现有 private fields、constructor 和 methods 的 class；
- 用 `new` 创建 object；
- 使用 `this`、getter、setter 与 encapsulation；
- 区分 instance member 和 static member。

---

## 🐍 Python → ☕ Java

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

```java
class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

`this` 是当前 object，起到 Python `self` 的角色。constructor 名与 class 名相同，而且没有返回类型。

## 1. Object map

| Concept | Java | Python connection |
|---|---|---|
| field | `private int score` | `self.score` |
| constructor | `public Student(...)` | `__init__` |
| object | `new Student(...)` | `Student(...)` |
| method | `public void study()` | instance method |
| encapsulation | private + public methods | stronger access control |

## 2. Example

```java
public class Main {
    public static void main(String[] args) {
        Book book = new Book("Java");
        book.setPages(300);
        System.out.println(book.getPages());
    }
}

class Book {
    private String title;
    private int pages;
    public Book(String title) { this.title = title; }
    public int getPages() { return pages; }
    public void setPages(int pages) { this.pages = pages; }
}
```

## 3. `static`

`Math.max(2, 3)` is static: it belongs to the class, so no object is needed. `book.getPages()` is instance-based: it needs one particular `Book`. A static method cannot directly access an instance field because it has no `this`.

⚠️ **Common Mistakes**

- writing `void Book(...)` for a constructor;
- omitting `new`;
- forgetting `this.field = field` when names match;
- trying to use instance data directly inside static `main`.

🧠 **AP CSA Notes**：Class design FRQ 关注 fields、constructor、accessor/mutator 和按合同实现方法。

✅ **Before Practice**

- 我能写一个可实例化的 class。
- 我知道访问 field 与调用 method 的区别。
- 我能说明 `a = b` 对 object 变量通常复制什么。

📝 **Practice**：完成 [Chapter 09 Practice](./practice.md)。
