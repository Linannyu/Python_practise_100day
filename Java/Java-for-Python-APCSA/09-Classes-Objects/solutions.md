# Chapter 09 — Classes & Objects Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 09-01 — Simple Book

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            System.out.println(new Book("Java").getTitle());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-02 — Getter

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Book book = new Book("Java"); System.out.println(book.getTitle());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-03 — Counter object

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Counter c = new Counter(); c.increment(); c.increment(); System.out.println(c.getValue());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-04 — Setter

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Counter c = new Counter(); c.setValue(8); System.out.println(c.getValue());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-05 — Person greeting

**Level:** Level 1

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            new Person("Lin").greet();
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-06 — Student model

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Student a = new Student("Lin", 80), b = new Student("Ada", 50); System.out.println(a.isPassing()); System.out.println(b.isPassing());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-07 — Bank balance

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            BankAccount a = new BankAccount(10); a.deposit(5); a.withdraw(50); System.out.println(a.getBalance());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-08 — Rectangle

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Rectangle r = new Rectangle(3, 4); System.out.println(r.area()); System.out.println(r.perimeter());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-09 — Static count

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            new Ticket(); new Ticket(); new Ticket(); System.out.println(Ticket.getCount());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-10 — Reference sharing

**Level:** Level 2

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            java.util.ArrayList<String> a = new java.util.ArrayList<>(); a.add("one"); java.util.ArrayList<String> b = a; b.add("two"); System.out.println(a);
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-11 — Clock

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Clock c = new Clock(23, 59); c.tick(); System.out.println(c);
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-12 — Quiz question

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Question q = new Question("2+2?", "4"); System.out.println(q.checkAnswer("4"));
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-13 — Immutable-ish Point

**Level:** Level 3

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Point p = new Point(3, 4); System.out.println(p.distanceFromOrigin());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-14 — Temperature FRQ

**Level:** AP CSA Style

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Temperature t = new Temperature(-5); System.out.println(t.getFahrenheit()); System.out.println(t.isFreezing());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---

## Problem 09-15 — Movie contract

**Level:** AP CSA Style

### Solution

```java
import java.util.*;
public class Main {

    static class Book { private String title; Book(String t) { title = t; } public String getTitle() { return title; } }
    static class Counter { private int value; public void increment() { value++; } public void setValue(int value) { this.value = value; } public int getValue() { return value; } }
    static class Person { private String name; Person(String n) { name = n; } public void greet() { System.out.println("Hello, " + name + "!"); } }
    static class Student { private String name; private int score; Student(String n, int s) { name = n; score = s; } public boolean isPassing() { return score >= 60; } }
    static class BankAccount { private double balance; BankAccount(double b) { balance = b; } public void deposit(double x) { if (x > 0) balance += x; } public void withdraw(double x) { if (x > 0 && x <= balance) balance -= x; } public double getBalance() { return balance; } }
    static class Rectangle { private int width, height; Rectangle(int w, int h) { width = w; height = h; } public int area() { return width * height; } public int perimeter() { return 2 * width + 2 * height; } }
    static class Ticket { private static int count; Ticket() { count++; } public static int getCount() { return count; } }
    static class Clock { private int hour, minute; Clock(int h, int m) { hour = h; minute = m; } public void tick() { minute++; if (minute == 60) { minute = 0; hour = (hour + 1) % 24; } } public String toString() { return String.format("%02d:%02d", hour, minute); } }
    static class Question { private String answer; Question(String p, String a) { answer = a; } public boolean checkAnswer(String response) { return answer.equals(response); } }
    static class Point { private int x, y; Point(int x, int y) { this.x = x; this.y = y; } public double distanceFromOrigin() { return Math.sqrt(x * x + y * y); } }
    static class Temperature { private double celsius; Temperature(double c) { celsius = c; } public double getCelsius() { return celsius; } public double getFahrenheit() { return celsius * 9 / 5 + 32; } public boolean isFreezing() { return celsius <= 0; } }
    static class Movie { private int rating; public void rate(int stars) { if (stars >= 1 && stars <= 5) rating = stars; } public int getRating() { return rating; } }

        public static void main(String[] args) {
            Movie m = new Movie(); m.rate(4); m.rate(9); System.out.println(m.getRating());
        }
    }
```

### Explanation

Fields are private; public or package-visible methods provide the behavior the task requires.

### Python Comparison

Python `self` is made explicit as Java `this`; Java constructors and fields also have declared types and access modifiers.

---
