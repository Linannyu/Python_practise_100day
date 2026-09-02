# Python → Java AP CSA Cheat Sheet

| Python idea | Java AP CSA form | Watch for |
|---|---|---|
| `print(x)` | `System.out.println(x);` | semicolon |
| `x = 4` | `int x = 4;` | declare type |
| `True`, `False` | `true`, `false` | lowercase |
| `None` | `null` | reference types only |
| `a and b` / `a or b` / `not a` | `a && b` / `a || b` / `!a` | booleans only |
| `5 / 2` | `5 / 2` | Java result: `2` |
| `5 / 2` | `5.0 / 2` | Java result: `2.5` |
| `x ** y` | `Math.pow(x, y)` | returns `double` |
| `if test:` | `if (test) { ... }` | braces, no colon |
| `elif` | `else if` | two words |
| `for i in range(n):` | `for (int i = 0; i < n; i++)` | excludes `n` |
| `x += 1` | `x++;` or `x += 1;` | no Python `++` |
| `def f(x):` | `public static Type f(Type x) { ... }` | return type |
| `len(s)` | `s.length()` | String: parentheses |
| `s[i]` | `s.charAt(i)` | returns `char` |
| `s[a:b]` | `s.substring(a, b)` | b excluded |
| `s == t` for text | `s.equals(t)` | never String `==` |
| `len(arr)` | `arr.length` | array: no parentheses |
| `arr[i]` | `arr[i]` | last index `length - 1` |
| `items.append(x)` | `list.add(x)` | `ArrayList` |
| `items[i]` | `list.get(i)` | `ArrayList` |
| `len(items)` | `list.size()` | `ArrayList` |
| `class Dog(Animal):` | `class Dog extends Animal {` | inheritance |
| `self.x = x` | `this.x = x;` | instance field |
| `super().__init__(x)` | `super(x);` | subclass constructor |

## Three length forms

```java
text.length();  // String
array.length;   // array
list.size();    // ArrayList
```

## Pre-submit checks

1. Does every statement need a `;`?
2. Are blocks using `{ }`?
3. Is `/` accidentally integer division?
4. Is the String comparison using `.equals()`?
5. Is the loop upper bound `< length`, not `<= length`?
6. Is this an array, String, or ArrayList length call?
