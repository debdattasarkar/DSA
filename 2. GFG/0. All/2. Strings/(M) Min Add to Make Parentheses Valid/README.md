# Min Add to Make Parentheses Valid

**Difficulty:** Medium
**Accuracy:** 70.12%
**Submissions:** 7K+
**Points:** 4

---

## Problem Statement

You are given a string `s` consisting only of the characters `'('` and `')'`. Your task is to determine the **minimum** number of parentheses (either `'('` or `')'`) that must be inserted at any positions to make the string `s` a **valid parentheses string**.

A parentheses string is considered **valid** if:

1. Every opening parenthesis `'('` has a corresponding closing parenthesis `')'`.
2. Every closing parenthesis `')'` has a corresponding opening parenthesis `'('`.
3. Parentheses are properly nested.

---

## Examples

### Example 1

**Input:** `s = "(()("`
**Output:** `2`
**Explanation:** There are two unmatched `'('` at the end, so we need to add two `')'` to make the string valid.

### Example 2

**Input:** `s = ")))"`
**Output:** `3`
**Explanation:** Three `'('` need to be added at the start to make the string valid.

### Example 3

**Input:** `s = ")()()"`
**Output:** `1`
**Explanation:** The very first `')'` is unmatched, so we need to add one `'('` at the beginning.

---

## Constraints

* `1 ≤ s.size() ≤ 10^5`
* `s[i] ∈ { '(', ')' }`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon, Microsoft, TCS, Adobe, IBM

---

## Topic Tags

Stack, Strings, Data Structures

---

## Related Articles

* Minimum Number Of Parentheses To Be Added To Make It Valid


---

---

Here’s a crisp, interview-ready guide for **Min Add to Make Parentheses Valid**.

---

## 2) Intuition + Step-by-Step Dry Run

### Core idea

We only need to count how many parentheses are **unmatched**.

* Keep a `balance` = number of unmatched `'('` seen so far.
* Scan left → right:

  * If char is `'('`: `balance += 1`
  * If char is `')'`:

    * If `balance > 0`: we can match one open → `balance -= 1`
    * Else: this `')'` is **unmatched** → we must insert one `'('` → `need += 1`
* At the end, any remaining `balance` open parentheses need `balance` closing `')'`.
* **Answer = `need + balance`**

This is optimal: every `')'` with no available `'('` necessarily needs one `'('` inserted; every leftover `'('` needs a `')'` appended.

### Dry run

#### Example A: `s = "(()("`

* i=0 `'('`: balance=1, need=0
* i=1 `'('`: balance=2, need=0
* i=2 `')'`: balance=1, need=0  (matched one)
* i=3 `'('`: balance=2, need=0
  End: need=0, balance=2 ⇒ **answer = 2** (add two `')'`)

#### Example B: `s = ")))"`

* i=0 `')'`: balance=0 → need=1 (insert `'('`)
* i=1 `')'`: balance=0 → need=2
* i=2 `')'`: balance=0 → need=3
  End: balance=0 ⇒ **answer = 3**

#### Example C: `s = ")()()"`

* i=0 `')'`: need=1, balance=0
* i=1 `'('`: balance=1, need=1
* i=2 `')'`: balance=0, need=1
* i=3 `'('`: balance=1, need=1
* i=4 `')'`: balance=0, need=1
  End: **answer = 1** (add one `'('` at front)

---

## 3) Python solutions (what interviewers expect)

### ✅ Optimal O(n) time, O(1) space (counter method)

```python
class Solution:
    def minParentheses(self, s: str) -> int:
        """
        Single pass counter.
        Time  : O(n)  (one scan)
        Space : O(1)  (two integers)
        """
        balance = 0  # unmatched '('
        need = 0     # number of '(' we must insert for unmatched ')'
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    need += 1
        # 'need' covers extra ')', 'balance' covers extra '('
        return need + balance
```

### Alternative 1: Stack simulation (clear but uses O(n) extra space)

```python
class SolutionStack:
    def minParentheses(self, s: str) -> int:
        """
        Use a stack to cancel '()' pairs.
        Time  : O(n)
        Space : O(n) in worst case (all '(' or all ')')
        """
        st = []
        for ch in s:
            if ch == '(':
                st.append(ch)
            else:  # ')'
                if st and st[-1] == '(':
                    st.pop()  # matched a pair
                else:
                    st.append(ch)  # unmatched ')'
        return len(st)  # each item left needs one insertion
```

### “Brute” idea (easy to explain, inefficient): Repeated removal of pairs

```python
class SolutionBrute:
    def minParentheses(self, s: str) -> int:
        """
        Repeatedly delete matched '()' until none remain,
        then answer is the leftover length.
        Time  : O(n^2) worst-case (each pass linear, many passes)
        Space : O(n) for intermediate strings
        """
        prev = None
        while prev != s:
            prev = s
            s = s.replace("()", "")
        return len(s)
```

> In interviews, lead with the **O(n)/O(1)** counter method; mention the stack version as a clear equivalent if asked; the “remove '()' pairs” brute is just for completeness.

---

## 4) Interviewer-style Q\&A

**Q1. Why is the counter solution correct and minimal?**
Every time we see an unmatched `')'`, the only fix is to add one `'('` before it → `need += 1`. After the scan, each remaining unmatched `'('` (tracked by `balance`) needs one `')'`. This counts the **minimum** required inserts.

**Q2. What’s the complexity?**
Counter solution is **O(n) time**, **O(1) space**. Stack solution is **O(n) time**, **O(n) space**. The replacement brute is **O(n²)** worst-case.

**Q3. Edge cases?**

* Empty string ⇒ 0
* All `'('` (e.g., `"(((("`) ⇒ need `len(s)` `')'`.
* All `')'` (e.g., `"))))"`) ⇒ need `len(s)` `'('`.
* Mixed patterns starting with `')'` or ending with `'('`.

**Q4. Can this extend to multiple types of brackets?**
Yes—keep counts/stack per bracket type or use a mapping with a stack. For the “minimum insertions” version, the counter trick only works directly for a **single** bracket type; for multiple types, use a stack.

**Q5. Can we also produce the corrected string?**
Yes—either build it as you go (inserting as needed) or do a second pass after counting to place the minimal insertions.

---

---

Below is a complete, runnable program for **“Min Add to Make Parentheses Valid”** that:

* Implements the required API `class Solution.minParentheses(self, s)`
* Shows **inputs → outputs**
* Annotates **time and space complexity** right where the work happens
* Benchmarks the full run using **timeit**

---

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Min Add to Make Parentheses Valid

Given a string s consisting only of '(' and ')', return the minimum number of
parentheses to insert anywhere so that the string becomes valid.

Optimal approach:
  Scan once, track:
    - balance: unmatched '(' seen so far
    - need    : number of '(' we must add to fix unmatched ')'

Overall complexities:
  Time  : O(n)   (single pass)
  Space : O(1)   (two integers + output integer)
"""

from __future__ import annotations
import random
import timeit
from typing import List


# =========================
# Core solution (O(n) / O(1))
# =========================
class Solution:
    def minParentheses(self, s: str) -> int:
        """
        Single linear pass with two counters.

        Per character:
          - '('  -> balance += 1                   # O(1) time, O(1) space
          - ')':
                if balance > 0: balance -= 1       # matches a previous '('
                else:           need += 1          # we must add '('

        At end:
          result = need + balance
          (need fixes extra ')'; balance fixes extra '(')

        Total:
          Time  : O(n)  — iterate s once
          Space : O(1)  — constant counters
        """
        balance = 0  # unmatched '('
        need = 0     # how many '(' we must add for unmatched ')'

        # ---- O(n): single pass over s ----
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    need += 1

        # Remaining balance '(' each needs one ')'
        return need + balance


# =========================
# (Optional) Stack version
# =========================
def stack_min_add(s: str) -> int:
    """
    Clear alternative using a stack.

    Time  : O(n)   (push/pop per character)
    Space : O(n)   (worst-case stack: all '(' or all ')')
    """
    st: List[str] = []
    for ch in s:
        if ch == '(':
            st.append(ch)
        else:  # ')'
            if st and st[-1] == '(':
                st.pop()        # cancel a pair
            else:
                st.append(ch)   # unmatched ')'
    return len(st)              # each leftover char needs one insert


# =========================
# Demo with sample inputs
# =========================
def demo() -> None:
    sol = Solution()
    samples = [
        "(()(",      # -> 2
        ")))",       # -> 3
        ")()()",     # -> 1
        "(((",       # -> 3
        "()",        # -> 0
        "",          # -> 0
        "())(()",    # -> 2
    ]

    print("=== Sample Runs ===")
    for s in samples:
        print(f"s = {s!r}")
        out = sol.minParentheses(s)   # O(n)
        print(f"min inserts = {out}")
        # sanity against stack version for small cases
        assert out == stack_min_add(s)
        print("-" * 36)


# =========================
# Benchmark with timeit
# =========================
def _bench_once(n: int, seed: int = 7) -> None:
    # Build a random parentheses string of length n
    random.seed(seed)
    s = "".join(random.choice("()") for _ in range(n))
    sol = Solution()
    sol.minParentheses(s)   # measure full call

def benchmark() -> None:
    sizes = [10_000, 50_000, 100_000]   # adjust if needed
    runs = 5
    print("=== Benchmark (timeit) ===")
    for n in sizes:
        total = timeit.timeit(lambda: _bench_once(n), number=runs)
        print(f"n={n:>6} | runs={runs} | total={total:.4f}s | avg/run={total/runs:.4f}s")
    print("-" * 36)


# =========================
# Main driver
# =========================
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

1. **Code editors / IDEs (auto-fix hints)**
   When typing expressions, editors can suggest the **minimum number of parentheses to insert** (or auto-insert) to make an expression syntactically valid.

2. **Compilers / Linters / Formatters**
   Before parsing, a quick linear pass can detect and report minimal fixes for unmatched parentheses in code, config files, or DSLs—useful for **error recovery** and **prettification** tools.

3. **Query builders (SQL/NoSQL) & Calculators**
   User-entered expressions often miss parentheses. Computing the **minimal insertion count** drives UX prompts like “add 2 closing parens to run this query”.

4. **Template & macro languages**
   Lightweight validators for template engines (e.g., `(... )` delimiters) can quickly detect how many delimiters are missing to safely evaluate a template.
