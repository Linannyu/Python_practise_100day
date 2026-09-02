#!/usr/bin/env python3
"""Small local tester for the fixed-signature Java course exercises.

It deliberately tests only a named source under work/ and compiles into a
TemporaryDirectory. No shell is used, source files are never rewritten, and
each Java subprocess has a short timeout.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WORK = ROOT / "work"

TESTS: dict[str, dict[str, object]] = {
    "02-12": {
        "chapter": "02-Variables-DataTypes",
        "tester": """
public class Tester {
    private static int passed = 0, total = 0;
    private static void check(String name, int expected, int got) {
        total++;
        if (expected == got) { passed++; System.out.println("✓ PASS " + name); }
        else { System.out.println("✗ FAIL " + name + " | Expected: " + expected + " | Got: " + got); }
    }
    public static void main(String[] args) {
        check("inside", 5, Main.clamp(5, 0, 10));
        check("low", 0, Main.clamp(-3, 0, 10));
        check("high", 10, Main.clamp(14, 0, 10));
        System.out.println("Score: " + passed + "/" + total);
        if (passed != total) System.exit(1);
    }
}
""",
    },
    "05-12": {
        "chapter": "05-Methods",
        "tester": """
public class Tester {
    private static int passed = 0, total = 0;
    private static void check(String name, int expected, int got) {
        total++;
        if (expected == got) { passed++; System.out.println("✓ PASS " + name); }
        else { System.out.println("✗ FAIL " + name + " | Expected: " + expected + " | Got: " + got); }
    }
    public static void main(String[] args) {
        check("positive", 4, Main.square(2));
        check("zero", 0, Main.square(0));
        check("negative", 9, Main.square(-3));
        System.out.println("Score: " + passed + "/" + total);
        if (passed != total) System.exit(1);
    }
}
""",
    },
    "06-14": {
        "chapter": "06-String",
        "tester": """
public class Tester {
    private static int passed = 0, total = 0;
    private static void check(String name, String expected, String got) {
        total++;
        if (expected.equals(got)) { passed++; System.out.println("✓ PASS " + name); }
        else { System.out.println("✗ FAIL " + name + " | Expected: " + expected + " | Got: " + got); }
    }
    public static void main(String[] args) {
        check("even", "av", Main.middle("java"));
        check("odd", "v", Main.middle("javaa"));
        check("one", "x", Main.middle("x"));
        System.out.println("Score: " + passed + "/" + total);
        if (passed != total) System.exit(1);
    }
}
""",
    },
    "07-14": {
        "chapter": "07-Arrays",
        "tester": """
public class Tester {
    private static int passed = 0, total = 0;
    private static void check(String name, int expected, int got) {
        total++;
        if (expected == got) { passed++; System.out.println("✓ PASS " + name); }
        else { System.out.println("✗ FAIL " + name + " | Expected: " + expected + " | Got: " + got); }
    }
    public static void main(String[] args) {
        check("mixed", 7, Main.sumPositive(new int[]{-2, 0, 3, 4}));
        check("none", 0, Main.sumPositive(new int[]{-5, 0}));
        check("empty", 0, Main.sumPositive(new int[]{}));
        System.out.println("Score: " + passed + "/" + total);
        if (passed != total) System.exit(1);
    }
}
""",
    },
    "12-14": {
        "chapter": "12-Recursion",
        "tester": """
public class Tester {
    private static int passed = 0, total = 0;
    private static void check(String name, int expected, int got) {
        total++;
        if (expected == got) { passed++; System.out.println("✓ PASS " + name); }
        else { System.out.println("✗ FAIL " + name + " | Expected: " + expected + " | Got: " + got); }
    }
    public static void main(String[] args) {
        check("zero", 1, Main.productTo(0));
        check("one", 1, Main.productTo(1));
        check("five", 120, Main.productTo(5));
        System.out.println("Score: " + passed + "/" + total);
        if (passed != total) System.exit(1);
    }
}
""",
    },
}


def list_tests() -> None:
    print("Available automated method tests:")
    for problem, details in TESTS.items():
        print(f"  {problem}  ({details['chapter']})")


def run(problem: str) -> int:
    if problem not in TESTS:
        print(f"Unknown problem: {problem}", file=sys.stderr)
        list_tests()
        return 2
    if shutil.which("javac") is None or shutil.which("java") is None:
        print("COMPILE ERROR: javac/java not found. Install a JDK and try again.", file=sys.stderr)
        return 2

    details = TESTS[problem]
    source = WORK / str(details["chapter"]) / problem / "Main.java"
    if not source.is_file():
        print(f"SOURCE NOT FOUND: create {source.relative_to(ROOT)} first.", file=sys.stderr)
        return 2

    print("=" * 40)
    print("Java Practice Tester")
    print("=" * 40)
    print(f"Chapter: {details['chapter']}")
    print(f"Problem: {problem}")
    with tempfile.TemporaryDirectory(prefix="java-course-test-") as temp_name:
        temp = Path(temp_name)
        shutil.copy2(source, temp / "Main.java")
        (temp / "Tester.java").write_text(str(details["tester"]), encoding="utf-8")
        try:
            compiled = subprocess.run(
                ["javac", "Main.java", "Tester.java"], cwd=temp, text=True,
                capture_output=True, timeout=10,
            )
        except subprocess.TimeoutExpired:
            print("COMPILE ERROR: compilation timed out.")
            return 1
        if compiled.returncode != 0:
            print("COMPILE ERROR")
            print((compiled.stderr or compiled.stdout).strip())
            return 1
        try:
            tested = subprocess.run(
                ["java", "Tester"], cwd=temp, text=True, capture_output=True, timeout=5,
            )
        except subprocess.TimeoutExpired:
            print("FAIL: test timed out (check for an infinite loop/recursion).")
            return 1
        print(tested.stdout.strip())
        if tested.stderr.strip():
            print(tested.stderr.strip(), file=sys.stderr)
        return 0 if tested.returncode == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Java for Python AP CSA method test.")
    parser.add_argument("problem", nargs="?", help="Problem id, for example 05-12")
    parser.add_argument("--list", action="store_true", help="List supported automated tests")
    args = parser.parse_args()
    if args.list:
        list_tests()
        return 0
    if not args.problem:
        parser.print_help()
        return 2
    return run(args.problem)


if __name__ == "__main__":
    raise SystemExit(main())
