# Day 06 Lab — Build a Username Inspector

## 🎯 Lab goal

Build a text-validation report using String methods and loops. You will reuse conditionals and methods while practicing safe indexing.

**Today’s Java:** `length()`、`charAt()`、`substring()`、`indexOf()`、`equals()`、immutable Strings.

**Reuse from Days 01–05:** methods, boolean conditions, loops, counters, early return values.

## Mission

Create `UsernameInspector.java`. Implement:

```java
public static boolean isValidUsername(String username)
public static int countDigits(String username)
public static String initials(String firstName, String lastName)
```

### Valid username rules

A username is valid only if it:

- has 5–12 characters inclusive;
- contains no spaces;
- starts with a letter;
- contains at least one digit.

Use a loop and `charAt` for character checks. Do not use regular expressions or advanced Java.

## Required report

In `main`, inspect `"lin2026"`, `"ab 12"`, and `"student"`. For each, print the username, whether it is valid, and its digit count. Then print initials for `Lin` and `Zhang` as `L.Z.`.

## Acceptance checks

1. `lin2026` is valid with 4 digits.
2. `ab 12` is invalid because it has a space.
3. `student` is invalid because it has no digit.
4. `1lin2026` is invalid because its first character is not a letter.

## Stretch goal

Implement `maskUsername(String username)` that returns the first and last characters with `*` in the middle, such as `l*****6`.

## Reflection

State why `username.equals("admin")` is safer than `username == "admin"`. Optional focused drills: [Drill Bank](./drills.md).
