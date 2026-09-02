# Chapter 10 — Inheritance

## 🎯 Learning Goals

- 用 `extends` 建立 superclass/subclass；
- 在子类构造器中使用 `super(...)`；
- 正确 override method；
- 追踪多态调用。

---

## 🐍 Python → ☕ Java

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

```java
class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Woof");
    }
}
```

`extends` 表示 Dog 继承 Animal 的可访问行为；`@Override` 让编译器检查你真正在重写。

## 1. Constructor chain

```java
class Animal {
    public Animal(String name) { }
}
class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
}
```

父类没有无参 constructor 时，子类必须显式选择合适的 `super(...)`，而它须是 constructor 的第一条语句。

## 2. Override vs overload

| Situation | Result |
|---|---|
| same name + same parameters in subclass | override |
| same name + different parameters | overload (not override) |
| `super.speak()` | parent implementation |

## 3. Example

```java
public class Main {
    public static void main(String[] args) {
        Animal pet = new Dog();
        pet.speak();
    }
}
class Animal { public void speak() { System.out.println("..."); } }
class Dog extends Animal { public void speak() { System.out.println("Woof"); } }
```

Reference type `Animal` decides accessible methods; actual object `Dog` decides which overridden `speak` runs.

⚠️ **Common Mistakes**

- Python `class Dog(Animal)` syntax；
- wrong `super` constructor arguments；
- changing parameters and calling it overriding；
- accessing a parent `private` field directly.

🧠 **AP CSA Notes**：重点不是复杂 class hierarchy，而是 constructor、method overriding 和 runtime dispatch。

✅ **Before Practice**

- 我能指出 parent 与 child class。
- 我能写 `super(...)`。
- 我能预测 overridden method output。

📝 **Practice**：完成 [Chapter 10 Practice](./practice.md)。
