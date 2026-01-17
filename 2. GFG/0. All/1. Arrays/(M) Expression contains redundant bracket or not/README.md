# Expression Contains Redundant Bracket or Not

**Difficulty:** Medium
**Accuracy:** 48.71%
**Submissions:** 39K+
**Points:** 4

---

## Problem Statement

You are given a string **`s`** representing a **balanced mathematical expression**.
Your task is to check **whether the expression contains any redundant parentheses or not**.

A **set of parentheses is considered redundant** if:

* The same sub-expression is surrounded by **unnecessary brackets**, or
* There are **multiple brackets** that do not affect the meaning of the expression.

---

## Important Notes

* The expression **may contain** operators: `+`, `-`, `*`, `/`
* The given expression is **valid**
* There are **no white spaces** in the expression

---

## Examples

### Example 1

**Input:**

```
s = "((a+b))"
```

**Output:**

```
true
```

**Explanation:**
`((a+b))` can be reduced to `(a+b)`, so the outer brackets are redundant.

---

### Example 2

**Input:**

```
s = "(a+(b)/c)"
```

**Output:**

```
true
```

**Explanation:**
`(b)` is surrounded by parentheses unnecessarily, so the expression contains redundant brackets.

---

### Example 3

**Input:**

```
s = "(a+b+(c+d))"
```

**Output:**

```
false
```

**Explanation:**
The expression does **not** have any redundant or multiple brackets.

---

## Constraints

* `1 ≤ |s| ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* Stack
* Strings

---

## Related Articles

* [**Expression Contains Redundant Bracket Not**](https://www.geeksforgeeks.org/expression-contains-redundant-bracket-not/)

---

---

## 2) Text explanation (stack idea)

A bracket pair `( ... )` is **redundant** if inside it there is **no operator** (`+ - * /`).
Examples:

* `(a)` → redundant (no operator)
* `((a+b))` → outer pair redundant (inside outer pair is just `(a+b)` → no operator at that level)
* `(a+(b)/c)` → `(b)` redundant

### Why stack works

Scan characters:

* Push everything except `')'`
* When you see `')'`, pop until `'('`:

  * If you **never popped an operator**, then this pair was redundant → return `True`
  * Pop `'('` and continue

This is **O(n)** and handles nested brackets naturally.

---

## Step-by-step Dry Run

### Example 1: `s = "((a+b))"`

Stack process:

* Read `(` push
* Read `(` push
* Read `a` push
* Read `+` push
* Read `b` push
* Read `)`:

  * pop: `b` (no op)
  * pop: `+` (**op found**)
  * pop: `a`
  * pop: `(` stop → **not redundant**
* Read `)` (outer):

  * pop until `(`:
  * top is `(` immediately? actually stack has only `(` left after last step
  * we popped **0 operators** → redundant ✅ return True

---

### Example 2: `s = "(a+(b)/c)"`

When we hit `)` for `(b)`:

* inside popped: `b` only → no operator → redundant ✅

---

### Example 3: `s = "(a+b+(c+d))"`

* For `(c+d)`: pops include `+` → not redundant
* For outer: pops include `+` (from `a+b+...`) → not redundant
  Return False ✅

---

## 3) Python solutions (easy + interview-expected)

### A) Brute-ish (using repeated simplification) — not recommended

You can repeatedly remove `(x)` patterns, but it’s messy and can become slow. Mention only as idea.

---

### B) Most expected (Stack, O(n)) ✅

```python
class Solution():
    def checkRedundancy(self, s):
        # Stack will store characters of expression
        stack = []

        # Operators that make parentheses meaningful
        operators = set("+-*/")

        for ch in s:
            if ch != ')':
                # Push everything until we find a closing bracket
                stack.append(ch)
            else:
                # We are closing a bracket: check what is inside (...)
                has_operator = False

                # Pop until we reach '('
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    if top in operators:
                        has_operator = True

                # Pop the '(' itself
                if stack:
                    stack.pop()

                # If there was no operator inside, brackets are redundant
                if not has_operator:
                    return True

        return False
```

---

### C) Slight variation: Push only meaningful tokens (still O(n))

Same idea, just clearer intent: store `'('` and operators only.

```python
class Solution():
    def checkRedundancy(self, s):
        stack = []
        operators = set("+-*/")

        for ch in s:
            if ch == '(' or ch in operators:
                stack.append(ch)
            elif ch == ')':
                # If top is '(' => nothing meaningful inside => redundant
                if stack and stack[-1] == '(':
                    return True

                # Pop operators until '('
                while stack and stack[-1] in operators:
                    stack.pop()

                # Pop '('
                if stack and stack[-1] == '(':
                    stack.pop()

        return False
```

---

## 4) Interview memory + expected Q&A

### 5-line pseudo-code template (memorize)

```
for ch in s:
  if ch != ')': push ch
  else:
    seenOp = false; pop until '(' and set seenOp if operator found
    pop '('
    if not seenOp: return true
return false
```

### Mnemonic

**“Close bracket? Look inside: NO OP = REDUNDANT.”**
(or **“Operator inside ⇒ useful; no operator ⇒ useless.”**)

### 60-second recall script

1. “Redundant parentheses are those that don’t change meaning.”
2. “In algebra, a pair `( … )` is useful only if it contains an operator.”
3. “Scan with stack; on `)` pop until `(` and check if any operator existed.”
4. “If none, return True immediately.”
5. “Else continue. O(n) time, O(n) stack.”

---

### Expected interviewer questions (with answers)

**Q1. Why checking only operators is enough?**
A. Parentheses are needed only to enforce operation grouping/precedence; without any operator inside, removing them doesn’t change evaluation.

**Q2. Does it handle nested parentheses like `((a+b))`?**
A. Yes. Inner pair has operator → ok, outer pair sees only a subexpression without operator at that level → redundant.

**Q3. Complexity?**
A. Each character is pushed/popped at most once → `O(n)` time, `O(n)` space.

**Q4. Any tricky edge case?**
A. `(a)` or `((a))` returns True. `(a+b)` returns False. Expression is guaranteed valid/balanced.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Compiler / Interpreter optimization (removing unnecessary parentheses)**

   * While parsing code, compilers simplify expression trees and can remove redundant grouping to reduce AST complexity.

2. **Code formatting / linting tools**

   * Linters/formatters detect and suggest removing unnecessary parentheses to improve readability (e.g., `(x)` or `((a+b))`).

3. **Expression evaluation engines (rules / calculators)**

   * Before evaluating user-entered formulas, systems simplify the expression to avoid extra parsing work and normalize expressions.

4. **Static analysis / refactoring tools**

   * Redundant brackets can be flagged during refactoring to keep expressions clean and prevent confusing nested groupings.

---

## 6) Full Program (timed run + inline complexity + sample I/O)

This runnable program:

* Reads `s` (balanced expression, no spaces)
* Uses stack method `O(n)` time, `O(n)` space
* Prints input, output (`True/False`)
* Prints total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: expression string `s`
  Example:

```
((a+b))
```

If no stdin, demo uses: `s="(a+(b)/c)"` → output `True`

```python
import sys
import time


class Solution():
    def checkRedundancy(self, s):
        """
        Stack-based check for redundant parentheses.
        Time: O(n)  (each char pushed/popped at most once)
        Aux Space: O(n)  (stack in worst case)
        """
        stack = []
        operators = set("+-*/")

        # Step 1: Scan characters once -> O(n)
        for ch in s:
            if ch != ')':
                # Push all chars until we hit ')'
                # Time: O(1) per push, Space: up to O(n)
                stack.append(ch)
            else:
                # Step 2: We close a bracket: check inside (...)
                # If no operator inside, it's redundant
                has_operator = False

                # Pop until '(' -> each char popped once overall => O(n) total
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    if top in operators:
                        has_operator = True

                # Pop the '(' itself
                if stack:
                    stack.pop()

                # If no operator found inside the brackets, redundant
                if not has_operator:
                    return True

        return False


def main():
    # Measure full program runtime (parse + solve + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    if not data:
        # ---------------- DEMO MODE ----------------
        s = "(a+(b)/c)"
    else:
        # ---------------- INPUT MODE ----------------
        # Time: O(n) read, Space: O(n) string
        s = data

    solver = Solution()

    # Solve
    # Time: O(n), Space: O(n)
    answer = solver.checkRedundancy(s)

    print("Input:")
    print("s =", s)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

For `s = "(a+(b)/c)"`
Output: `True` (+ runtime)

---
