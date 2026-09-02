# Chapter 02 — Variables & Data Types Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 02-01 — Student data

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        String name = "Lin"; int age = 16; double gpa = 3.8; boolean enrolled = true;
    System.out.println(name); System.out.println(age); System.out.println(gpa); System.out.println(enrolled);
    }
}
```

### Explanation

The declarations make each stored kind explicit.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-02 — Character versus String

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        char grade = 'A'; String message = "Excellent";
    System.out.println(grade); System.out.println(message);
    }
}
```

### Explanation

`char` has one character and single quotes; `String` has text and double quotes.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-03 — Arithmetic

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int a = 17, b = 5;
    System.out.println(a + b); System.out.println(a - b); System.out.println(a * b); System.out.println(a / b); System.out.println(a % b);
    }
}
```

### Explanation

Both operands are int, so `/` produces 3 and `%` produces the remainder 2.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-04 — Decimal division

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int a = 17, b = 5;
    System.out.println((double) a / b);
    }
}
```

### Explanation

Casting one operand before division changes the operation to double division.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-05 — Boolean range

**Level:** Level 1

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int score = 82; boolean passing = score >= 60;
    System.out.println(passing);
    }
}
```

### Explanation

A comparison already evaluates to a boolean.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-06 — Temperature conversion

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int fahrenheit = 68; double celsius = (fahrenheit - 32) * 5.0 / 9;
    System.out.println(celsius);
    }
}
```

### Explanation

`5.0` prevents accidental integer division.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-07 — Even and positive

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int n = 12; boolean result = n > 0 && n % 2 == 0;
    System.out.println(result);
    }
}
```

### Explanation

The two required conditions combine with `&&`.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-08 — Power report

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int base = 2, exponent = 5; double result = Math.pow(base, exponent);
    System.out.println(result);
    }
}
```

### Explanation

`Math.pow` returns double even when the mathematical result is whole.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-09 — Cast safely

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        double price = 8.99; int whole = (int) price;
    System.out.println(price); System.out.println(whole);
    }
}
```

### Explanation

Casting to int truncates toward zero.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-10 — Final days

**Level:** Level 2

### Solution

```java
public class Main {

    public static void main(String[] args) {
        final int DAYS_IN_WEEK = 7; int days = 5 * DAYS_IN_WEEK;
    System.out.println(days);
    }
}
```

### Explanation

`final` prevents a new assignment to the variable name.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-11 — Time breakdown

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int seconds = 3671; int hours = seconds / 3600; seconds %= 3600; int minutes = seconds / 60; seconds %= 60;
    System.out.println(hours); System.out.println(minutes); System.out.println(seconds);
    }
}
```

### Explanation

Division takes a whole unit; remainder keeps the unused part.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-12 — Clamp

**Level:** Level 3

### Solution

```java
public class Main {
    public static int clamp(int value, int low, int high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

    public static void main(String[] args) {
        System.out.println(clamp(14, 0, 10));
    }
}
```

### Explanation

The method preserves values inside the closed range and snaps only out-of-range values.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-13 — Invoice total

**Level:** Level 3

### Solution

```java
public class Main {

    public static void main(String[] args) {
        int quantity = 3; double unitPrice = 12.5, discountRate = 0.10;
    double total = quantity * unitPrice * (1 - discountRate);
    System.out.println("Total: " + total);
    }
}
```

### Explanation

The decimal rate is retained by using double arithmetic.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-14 — Trace types

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        double x = 7 / 2 + 0.5; System.out.println(x);
    }
}
```

### Explanation

`7 / 2` becomes int 3 before adding 0.5, so x is 3.5.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---

## Problem 02-15 — Correct declarations

**Level:** AP CSA Style

### Solution

```java
public class Main {

    public static void main(String[] args) {
        char letter = 'Z'; String text = "Z"; boolean no = false; double decimal = 2.75; int number = 27;
    System.out.println(letter + " " + text + " " + no + " " + decimal + " " + number);
    }
}
```

### Explanation

Each literal matches the declared type.

### Python Comparison

Python usually infers a value's type at runtime; Java states the variable and parameter types before use.

---
