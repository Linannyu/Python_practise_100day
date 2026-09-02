# Automated tests

`run_tests.py` generates a small `Tester.java` in a temporary directory, compiles it with your chosen `work/<chapter>/<problem>/Main.java`, then reports each assertion. It currently covers method-writing tasks whose signatures are deliberately fixed:

- `02-12` — `clamp`
- `05-12` — `square`
- `06-14` — `middle`
- `07-14` — `sumPositive`
- `12-14` — `productTo`

More importantly, use the pattern for your own checks: a method is not complete until it has been tested with normal, boundary, and unusual inputs.
