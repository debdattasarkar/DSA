# Postfix Evaluation

**Difficulty:** Medium
**Accuracy:** 63.04%
**Submissions:** 121K+
**Points:** 4

---

## Problem Statement

You are given an array of strings `arr[]` that represents a valid arithmetic expression written in **Reverse Polish Notation** (Postfix Notation). Your task is to **evaluate the expression** and return an **integer** representing its value.

**Note:**

* A postfix expression is of the form `operand1 operand2 operator` (e.g., `"a b +"`).
* The **division** operation between two integers **always computes the floor value**, i.e.
  `floor(5 / 3) = 1` and `floor(-5 / 3) = -2`.
* It is guaranteed that the result of the expression and all intermediate calculations will fit in a **32-bit signed integer**.

---

## Examples

### Example 1

**Input:** `arr[] = ["2", "3", "1", "*", "+", "9", "-"]`
**Output:** `-4`
**Explanation:** Converting to infix: `2 + (3 * 1) - 9 = 5 - 9 = -4`.

### Example 2

**Input:** `arr[] = ["2", "3", "^", "1", "+"]`
**Output:** `9`
**Explanation:** Converting to infix: `2 ^ 3 + 1 = 8 + 1 = 9`.

---

## Constraints

* `3 ≤ arr.size() ≤ 10^3`
* `arr[i]` is either an operator from `{"+", "-", "*", "/", "^"}` or an integer in the range **\[-10^4, 10^4]**

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* `Stack`, `Data Structures`

---

## Related Articles

* [Stack Set 4: Evaluation of Postfix Expression](https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/)

---

---

Here’s an interview-ready pack for **Postfix (RPN) Evaluation**.

---

## 2) Explanation + step-by-step dry run

### How postfix works

In Reverse Polish Notation, every operator comes **after** its two operands.
So we can evaluate left→right using a **stack**:

1. If token is a **number**: push it.
2. If token is an **operator**: pop `b` (top), pop `a` (next), compute `a op b`, push result.
3. At the end, the stack has exactly one value → the answer.

Key implementation notes:

* Division here is **floor division** (e.g., `-5 / 3 → -2`). In Python, use `a // b`.
* The operator `^` means **power** (exponent), **not** XOR. Use `a ** b` (or `pow(a, b)`).

### Dry run (Example 1)

`arr = ["2", "3", "1", "*", "+", "9", "-"]`

Stack evolution:

* push 2 → `[2]`
* push 3 → `[2, 3]`
* push 1 → `[2, 3, 1]`
* `*`  → pop 1,3 → 3\*1=3 → push → `[2, 3]`→`[2, 3]`→`[2, 3]` → actually becomes `[2, 3]` then push 3 → `[2, 3]`? clarify: after pop(1,3) compute 3, push → `[2, 3]` becomes `[2, 3]`? Let's rewrite cleanly:

  * before `*`: `[2, 3, 1]`
  * pop b=1, a=3 → a\*b = 3
  * push 3 → stack `[2, 3]`
* `+`  → pop b=3, a=2 → 2+3=5 → push → `[5]`
* push 9 → `[5, 9]`
* `-`  → pop b=9, a=5 → 5-9 = **-4** → push → `[-4]`

Result: **-4**.

### Dry run (Example 2)

`arr = ["2", "3", "^", "1", "+"]`

* push 2 → `[2]`
* push 3 → `[2, 3]`
* `^`  → pop b=3, a=2 → 2\*\*3=8 → push `[8]`
* push 1 → `[8, 1]`
* `+`  → pop b=1, a=8 → 9 → `[9]` → answer **9**.

---

## 3) Python solutions (most-expected + alternative)

### A) Stack-based evaluation (most expected, O(n) time / O(n) space)

```python
class Solution:
    def evaluatePostfix(self, arr):
        """
        Evaluate Reverse Polish Notation.
        Time : O(n)  — single pass, constant work per token
        Space: O(n)  — stack of at most n/2 numbers

        Notes:
          - token '^' means exponent, so use '**'
          - division is FLOOR division: a // b
          - tokens that are not operators are integers (may be negative)
        """
        ops = {"+", "-", "*", "/", "^"}
        st = []

        for tok in arr:
            if tok not in ops:  # number (handles "-3", "42", etc.)
                st.append(int(tok))
                continue

            # pop in the right order: b is top, a is next
            b = st.pop()
            a = st.pop()

            if tok == "+":
                st.append(a + b)
            elif tok == "-":
                st.append(a - b)
            elif tok == "*":
                st.append(a * b)
            elif tok == "/":
                # floor division as per problem statement
                st.append(a // b)
            else:  # tok == "^"  (power, not XOR)
                st.append(a ** b)

        # valid expression guarantees exactly one value remains
        return st[-1]
```

### B) In-place reduction (educational, O(n²) worst-case)

Repeatedly scan the list: when you find an operator with two numbers immediately before it, compute and replace those three tokens by the result. This is simple to understand but repeatedly moves elements → **quadratic**.

```python
class SolutionSlow:
    def evaluatePostfix(self, arr):
        """
        Naive left-to-right reduction by replacing 'a b op' with result.
        Time : O(n^2) worst-case due to list deletions/insertions
        Space: O(1) extra (operates mostly in-place)
        """
        i = 0
        ops = {"+", "-", "*", "/", "^"}
        a = arr[:]  # work on a copy
        while len(a) > 1:
            if i >= 2 and a[i] in ops and a[i-2] not in ops and a[i-1] not in ops:
                x = int(a[i-2]); y = int(a[i-1]); op = a[i]
                if op == "+":    val = x + y
                elif op == "-":  val = x - y
                elif op == "*":  val = x * y
                elif op == "/":  val = x // y    # floor division
                else:            val = x ** y    # exponent
                # replace a[i-2:i+1] with the computed value
                a[i-2:i+1] = [str(val)]
                i = max(i - 2, 0)  # step back to re-check newly formed context
            else:
                i += 1
        return int(a[0])
```

> In interviews: write **A**. Mention pitfalls: using `^` as XOR by mistake, or using truncating division instead of **floor** division.

---

## 4) Interviewer-style Q\&A

**Q1. Why does a stack work perfectly for postfix?**
Because postfix puts each operator **after** its operands, so when an operator appears the operands are the **most recent** numbers seen, i.e., on top of the stack. This yields a single linear pass.

**Q2. What are the time and space complexities?**

* Stack solution: **O(n)** time, **O(n)** space (at most \~n/2 operands on the stack).
* In-place reduction: can degrade to **O(n²)** due to repeated list compaction.

**Q3. How do you handle negative numbers vs the subtraction operator?**
Tokens are strings. If a token equals one of the operator symbols `{"+","-","*","/","^"}`, treat it as operator; otherwise convert with `int(tok)`. So `"-3"` is a number; `"-"` is an operator.

**Q4. Division semantics?**
The problem specifies **floor division for integers** (e.g., `-5 / 3 → -2`). In Python, `//` already does floor division on ints, so use `a // b`.

**Q5. What about overflow?**
The statement guarantees intermediate results fit in 32-bit signed integers, so Python’s big ints won’t overflow anyway.

**Q6. Any operator precedence concerns?**
None. Postfix removes precedence/parentheses ambiguity—the order is explicit by the notation itself.

**Q7. Is `^` exponent or XOR?**
In this problem it is **exponent**. In Python, `^` is bitwise XOR; to exponentiate use `**` or `pow(a, b)`.

---

---

Absolutely — here’s a **full, runnable Python program** that:

* implements the **stack-based O(n)** postfix (RPN) evaluator (with `^` = exponent and integer **floor division**),
* prints **inputs → outputs** for sample cases,
* and **benchmarks** the evaluator using `timeit` right in `main`.

I’ve annotated each step with **time/space complexity** comments.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Postfix (RPN) Evaluation
------------------------
Evaluate a valid arithmetic expression where tokens are strings in Reverse Polish Notation.

Operators supported: +, -, *, /, ^
- Division is FLOOR division on integers (e.g., -5 / 3 -> -2).
- ^ is exponent (NOT XOR). In Python use **.

Let n = number of tokens.
Overall complexities:
  Time  : O(n)  — one left-to-right pass, constant work per token
  Space : O(n)  — stack may hold up to ~n/2 operands
"""

from __future__ import annotations
import random
import timeit
from typing import List


# --------------------------------------------------------------------
# User function Template for python3
# --------------------------------------------------------------------
class Solution:
    def evaluatePostfix(self, arr: List[str]) -> int:
        """
        Evaluate Reverse Polish Notation using a stack.

        Per-step complexities in the loop:
          - Token test / push number: O(1) time, O(1) extra space
          - On operator: pop 2 (O(1)), compute (O(1)), push result (O(1))
        Entire loop across n tokens => O(n) time. The stack uses O(n) space worst-case.
        """
        st: List[int] = []                  # O(1) init
        ops = {"+", "-", "*", "/", "^"}     # O(1) init

        for tok in arr:                     # O(n) iterations
            if tok not in ops:
                # number (handles negatives like "-13")
                st.append(int(tok))         # O(1)
                continue

            # operator: pop in correct order (b is top, a under it)
            b = st.pop()                    # O(1)
            a = st.pop()                    # O(1)

            if tok == "+":
                st.append(a + b)            # O(1)
            elif tok == "-":
                st.append(a - b)            # O(1)
            elif tok == "*":
                st.append(a * b)            # O(1)
            elif tok == "/":
                # FLOOR division as per statement; Python // already floors on ints
                st.append(a // b)           # O(1)
            else:  # '^' exponent
                st.append(a ** b)           # O(1)

        # valid expression -> exactly one value remains
        return st[-1]                       # O(1)


# --------------------------------------------------------------------
# Demo: sample runs printing input values and outputs
# --------------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    samples = [
        (["2", "3", "1", "*", "+", "9", "-"], -4),
        (["2", "3", "^", "1", "+"], 9),
        (["4", "-2", "/"], -2),              # 4 // -2 = -2
        (["-5", "3", "/"], -2),              # floor division: -5 // 3 = -2
    ]
    print("=== Sample Runs ===")
    for arr, expected in samples:
        out = sol.evaluatePostfix(arr)       # O(n) per call
        print(f"Input : {arr}")
        print(f"Output: {out}  | Expected: {expected}")
        print("-" * 60)


# --------------------------------------------------------------------
# Benchmark with timeit (measures the full function runtime)
# --------------------------------------------------------------------
def _bench_once(expr: List[str]) -> None:
    Solution().evaluatePostfix(expr)         # O(n)

def _make_random_rpn(operands: int, rng: random.Random) -> List[str]:
    """
    Build a random, VALID RPN expression with the given number of operands.
    Uses operators from {+, -, *, /} to keep values in reasonable range.
    Complexity: O(operands) tokens generated (~2*operands - 1).
    """
    nums_left = operands
    ops_left = operands - 1
    depth = 0
    expr: List[str] = []
    while nums_left or ops_left:
        # push number if we must (depth<2) or with some bias; else push operator
        if nums_left and (depth < 2 or rng.random() < 0.6):
            # keep numbers small to avoid huge intermediate values
            val = rng.randint(-50, 50)
            # avoid zero to reduce accidental divide-by-zero; still allowed sometimes
            if val == 0:
                val = 1
            expr.append(str(val))
            nums_left -= 1
            depth += 1
        else:
            # choose operator (avoid ^ in the benchmark to keep values bounded)
            op = rng.choice(("+", "-", "*", "/"))
            expr.append(op)
            ops_left -= 1
            depth -= 1
    return expr

def benchmark() -> None:
    rng = random.Random(2025)
    # create one decent-sized expression (within constraints, <= 1000 tokens)
    expr = _make_random_rpn(operands=600, rng=rng)  # ~1199 tokens
    runs = 200
    total = timeit.timeit(lambda: _bench_once(expr), number=runs)

    print("=== Benchmark (stack evaluator) ===")
    print(f"Tokens : {len(expr)}")
    print(f"Runs   : {runs}")
    print(f"Total  : {total:.6f} s")
    print(f"Avg/run: {total / runs:.6f} s")
    print("-" * 60)


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (key ones)

1. **Expression engines / calculators:**
   Many interpreters compile infix to **postfix** (or bytecode) and then evaluate via a stack — simple and fast (no precedence parsing at runtime).

2. **Stack virtual machines (e.g., JVM-style, PostScript, Forth):**
   Execution model is stack-based RPN; operators consume operands from the stack and push results.

3. **Database / query optimizers:**
   Boolean and arithmetic predicates are often converted to postfix or DAGs for efficient evaluation/execution planning.

4. **Compilers / assemblers:**
   During code generation or constant folding, expressions are converted to postfix to simplify evaluation and register allocation reasoning.
