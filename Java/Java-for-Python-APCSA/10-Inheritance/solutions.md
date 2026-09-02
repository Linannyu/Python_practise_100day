# Chapter 10 — Inheritance Solutions

> 每一段都是可独立保存为 `Main.java` 并编译的参考答案。先完成练习再展开/阅读本页。

## Problem 10-01 — Animal and Dog

**Level:** Level 1

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Dog("Rex").speak();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-02 — Parent constructor

**Level:** Level 1

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        System.out.println(new Dog("Rex").getName());
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-03 — Cat

**Level:** Level 1

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Cat("Mia").speak();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-04 — Super method

**Level:** Level 1

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Dog("Rex").speakWithParent();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-05 — Inherited getter

**Level:** Level 1

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Dog("Rex").sayName();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-06 — Vehicle

**Level:** Level 2

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Car("Ford").move();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-07 — Employee roles

**Level:** Level 2

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        System.out.println(new Manager("Lin", 100, 20).totalPay());
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-08 — Polymorphism

**Level:** Level 2

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        Animal pet = new Dog("Mochi"); pet.speak();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-09 — Shape area

**Level:** Level 2

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        System.out.println(new Square(4).area());
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-10 — Override check

**Level:** Level 2

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Dog("Rex").speak();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-11 — Account types

**Level:** Level 3

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        SavingsAccount s = new SavingsAccount("Lin", 100, 0.1); s.addInterest(); System.out.println(s.getBalance());
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-12 — Library items

**Level:** Level 3

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        LibraryItem[] a = {new LibraryItem("Book"), new DVD("Movie")}; for (LibraryItem x : a) System.out.println(x.loanPeriod());
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-13 — Constructor chain

**Level:** Level 3

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        new Child();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-14 — Override FRQ

**Level:** AP CSA Style

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        System.out.println(new BonusQuiz(8, 2).getPoints());
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---

## Problem 10-15 — Reference type trace

**Level:** AP CSA Style

### Solution

```java
public class Main {

static class Animal { private String name; Animal(String n) { name = n; } String getName() { return name; } void speak() { System.out.println("..."); } }
static class Dog extends Animal { Dog(String n) { super(n); } @Override void speak() { System.out.println("Woof"); } void speakWithParent() { super.speak(); speak(); } void sayName() { System.out.println(getName()); } }
static class Cat extends Animal { Cat(String n) { super(n); } @Override void speak() { System.out.println("Meow"); } }
static class Vehicle { String brand; Vehicle(String b) { brand = b; } void move() { System.out.println("moves"); } }
static class Car extends Vehicle { Car(String b) { super(b); } @Override void move() { System.out.println(brand + " drives"); } }
static class Employee { String name; double pay; Employee(String n, double p) { name = n; pay = p; } }
static class Manager extends Employee { double bonus; Manager(String n, double p, double b) { super(n, p); bonus = b; } double totalPay() { return pay + bonus; } }
static class Shape { double area() { return 0; } } static class Square extends Shape { double side; Square(double s) { side = s; } @Override double area() { return side * side; } }
static class Account { double balance; Account(String owner, double b) { balance = b; } void deposit(double x) { balance += x; } double getBalance() { return balance; } }
static class SavingsAccount extends Account { double rate; SavingsAccount(String o, double b, double r) { super(o, b); rate = r; } void addInterest() { deposit(balance * rate); } }
static class LibraryItem { LibraryItem(String title) { } int loanPeriod() { return 14; } } static class DVD extends LibraryItem { DVD(String title) { super(title); } @Override int loanPeriod() { return 7; } }
static class Parent { Parent() { System.out.println("Parent"); } } static class Child extends Parent { Child() { System.out.println("Child"); } }
static class Quiz { int points; Quiz(int p) { points = p; } int getPoints() { return points; } } static class BonusQuiz extends Quiz { int bonus; BonusQuiz(int p, int b) { super(p); bonus = b; } @Override int getPoints() { return points + bonus; } }

    public static void main(String[] args) {
        Animal[] pets = {new Dog("D"), new Cat("C")}; for (Animal p : pets) p.speak();
    }
}
```

### Explanation

The subclass uses `extends`; `super(...)` initializes parent state and an overridden method runs according to the object's actual type.

### Python Comparison

Python subclass syntax and Java `extends` both reuse a parent type; Java uses `super(...)` to initialize inherited state.

---
