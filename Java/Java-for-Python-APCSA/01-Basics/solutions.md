# Chapter 01 — Basics Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 01-01 — First line

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Hello, Lin!");
    }
}
```

### Explanation

`println` prints the requested text and then a newline.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-02 — Two prints

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Java");
    System.out.println("AP CSA");
    }
}
```

### Explanation

Two `println` calls create two output lines.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-03 — One line together

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.print("Python -> ");
    System.out.println("Java");
    }
}
```

### Explanation

`print` keeps the cursor on the line; `println` finishes it.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-04 — Commented plan

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        // Display a readiness message.
    System.out.println("Ready");
    }
}
```

### Explanation

A `//` comment is ignored by the compiler.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-05 — Block comment

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        /* This program introduces
       a Java learner. */
    System.out.println("Lin is learning Java.");
    }
}
```

### Explanation

`/* ... */` can span lines without affecting output.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-06 — Mini schedule

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("1. Read");
    System.out.println("2. Code");
    System.out.println("3. Test");
    }
}
```

### Explanation

Each statement deliberately owns one line.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-07 — Exact shape

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("***");
    System.out.println("* *");
    }
}
```

### Explanation

String literals preserve the internal space.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-08 — Print versus println

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.print("AP ");
    System.out.println("CSA");
    }
}
```

### Explanation

The first call does not add a newline; the second one does.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-09 — Compile vocabulary

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Source: .java");
    System.out.println("Compiler: javac");
    System.out.println("Bytecode: .class");
    System.out.println("Runtime: JVM");
    }
}
```

### Explanation

This reports the Java source-to-JVM path.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-10 — Minimum compiling program

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Braces and semicolons matter.");
    }
}
```

### Explanation

The class, `main`, braces, parentheses, quotes and semicolon all have a structural role.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-11 — Console card

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Lin");
    System.out.println("Python programmer");
    System.out.println("Future AP CSA student");
    }
}
```

### Explanation

This task needs no variables; literal output is sufficient.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-12 — Escape quote

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("She said \"Java is precise.\"");
    }
}
```

### Explanation

Inside a Java String, `\"` means a literal double quote.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-13 — Backslash

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("C:\\Java\\Main.java");
    }
}
```

### Explanation

A backslash is escaped as `\\` in a String literal.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-14 — Trace formatting

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.print("A");
    System.out.println("B");
    System.out.println("C");
    }
}
```

### Explanation

The precise output is `AB` on the first line, then `C` on the next.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---

## Problem 01-15 — Diagnose

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Start");
    }
}
```

### Explanation

The original `println` statement was missing its required terminating semicolon.

### Python Comparison

Python prints directly; Java puts the print in `main`, inside a class, and ends the statement with `;`.

---
