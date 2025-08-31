
# First n Fibonacci

**Difficulty:** Basic
**Accuracy:** 29.92%
**Submissions:** 261K+
**Points:** 1

---

## Problem Statement

Given a number **n**, return an array containing the **first n Fibonacci numbers**.

**Note:** The first two numbers of the series are **0** and **1**.

---

## Examples

### Example 1

**Input:** `n = 5`
**Output:** `[0, 1, 1, 2, 3]`

### Example 2

**Input:** `n = 7`
**Output:** `[0, 1, 1, 2, 3, 5, 8]`

### Example 3

**Input:** `n = 2`
**Output:** `[0, 1]`

---

## Constraints

* `1 <= n <= 30`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Infosys
* Wipro
* TCS
* Accenture

---

## Topic Tags

* Dynamic Programming
* Mathematical
* Algorithms

---

## Related Articles

* Java Fibonacci Series
* Program To Print First N Fibonacci Numbers

---

---

# Fibonacci (0,1,1,2,3,…) — interview guide

## 2) Explanation + step-by-step dry run

We must return the **first `n` Fibonacci numbers starting at 0**:

`F0 = 0, F1 = 1, F(i) = F(i−1) + F(i−2)` for `i ≥ 2`.

### Approach

Use two running variables `(a, b)` that always hold two consecutive Fibonacci numbers. On each step:

1. Append `a` (the current Fibonacci).
2. Update pair to next: `(a, b) = (b, a + b)`.

**Why this is optimal for listing the first `n` values**

* We must output `n` numbers → at least `Θ(n)` work.
* The iterative pair update uses **O(1)** working space and visits each term once → **O(n)** time.

### Dry run (`n = 5`)

Start `a=0, b=1, res=[]`

| step | append `a` | res after append | update `(a,b)` |
| ---- | ---------- | ---------------- | -------------- |
| 1    | 0          | \[0]             | (1, 1)         |
| 2    | 1          | \[0, 1]          | (1, 2)         |
| 3    | 1          | \[0, 1, 1]       | (2, 3)         |
| 4    | 2          | \[0, 1, 1, 2]    | (3, 5)         |
| 5    | 3          | \[0, 1, 1, 2, 3] | (5, 8)         |

Result: `[0, 1, 1, 2, 3]` ✅

---

## 3) Python solutions (expected in interviews)

### A) Canonical iterative (space-optimal) — **recommended**

```python
#User function Template for python3

class Solution:
    # Function to return list containing first n fibonacci numbers (0,1,1,2,...)
    def fibonacciNumbers(self, n):
        # Edge cases
        if n <= 0:
            return []                 # O(1)
        # Iteratively build the list.
        res = []                      # Output list -> O(n) space (unavoidable, we must return n items)
        a, b = 0, 1                   # Current consecutive Fibonacci numbers -> O(1) extra space

        # Produce exactly n numbers -> O(n) time
        for _ in range(n):
            res.append(a)             # Append current term
            a, b = b, a + b           # Move to next pair
        return res
```

**Complexity:** Time `O(n)`; extra space `O(1)` (besides the `O(n)` output list).

---

### B) Generator + list (same complexity, clean style)

```python
def _fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class SolutionGen:
    def fibonacciNumbers(self, n):
        # Still O(n) time and O(n) space for the returned list.
        return list(_fib_gen(n))
```

---

### C) Memoized recursion (educational; not preferred for listing)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def _F(i):                   # 0-based: F(0)=0, F(1)=1
    if i < 2: return i
    return _F(i-1) + _F(i-2)

class SolutionMemo:
    def fibonacciNumbers(self, n):
        # Builds list by querying F(0..n-1); time O(n), cache size O(n).
        return [_F(i) for i in range(n)]
```

> Note: Naïve recursion **without** memoization is `O(φ^n)` and is usually rejected in interviews. Mention it only to contrast why memoization/iteration is better.

---

## 4) Likely interviewer Q\&A

**Q1. What are the time/space complexities to return the first `n` Fibonacci numbers?**
**A.** Time `O(n)`. Output alone is `n` items. Working space can be `O(1)` using the iterative pair-update; the returned list is `O(n)`.

**Q2. Why not use plain recursion?**
**A.** Naïve recursion recomputes the same subproblems exponentially (`O(φ^n)` calls). Memoization fixes it to `O(n)`, but iteration is simpler and uses less overhead.

**Q3. The judge expects `0 1 1 2 3 ...` but I printed `1 1 2 3 5 ...`. What changed?**
**A.** That’s an **indexing convention** difference. Use 0-based Fibonacci with `a, b = 0, 1` and append `a` each step.

**Q4. How do you handle huge `n` or huge values?**
**A.** Python integers are arbitrary-precision. For other languages use big-int libraries, or if only values modulo `M` are needed, compute `(a+b) % M`. If you only need the single `n`-th term, **fast doubling** gives `O(log n)`, but to list the **first n** terms total time is still `Θ(n)`.

**Q5. Can we output without storing the entire list?**
**A.** Yes—use a **generator** to stream values. But if the function must **return a list**, you necessarily store `n` items.

---

---

Here you go—everything inline, executed, and timed.

* The program implements:

  * **Iterative** Fibonacci (0-based) — optimal for this task.
  * **Naive recursion** (for contrast; exponential).
  * **Memoized recursion** (also `O(n)`, but with recursion overhead).
* It prints outputs for the sample inputs `n=5`, `n=7`, `n=2`, and benchmarks the three approaches at `n=30`.
* The **TOTAL MAIN RUNTIME** is printed using `timeit.default_timer()`.

```python

# Re-run the inline program so outputs are visible
from typing import List
import timeit

class Solution:
    def fibonacciNumbers(self, n: int) -> List[int]:
        if n <= 0:
            return []
        res: List[int] = []
        a, b = 0, 1
        for _ in range(n):
            res.append(a)
            a, b = b, a + b
        return res

    def fibonacciNumbers_naive(self, n: int) -> List[int]:
        def F(i: int) -> int:
            if i < 2:
                return i
            return F(i-1) + F(i-2)
        return [F(i) for i in range(n)]

    def fibonacciNumbers_memo(self, n: int) -> List[int]:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def F(i: int) -> int:
            if i < 2:
                return i
            return F(i-1) + F(i-2)
        return [F(i) for i in range(n)]

def main():
    sol = Solution()
    print("=== First n Fibonacci — Demo ===")
    tests = [5, 7, 2]
    for n in tests:
        ans = sol.fibonacciNumbers(n)
        print(f"Input: n = {n}\nOutput:", ans, "\n")

    n_cmp = 30
    t0 = timeit.default_timer()
    res_iter = sol.fibonacciNumbers(n_cmp)
    t1 = timeit.default_timer()

    t2 = timeit.default_timer()
    res_memo = sol.fibonacciNumbers_memo(n_cmp)
    t3 = timeit.default_timer()

    t4 = timeit.default_timer()
    res_naive = sol.fibonacciNumbers_naive(n_cmp)
    t5 = timeit.default_timer()

    print(f"n = {n_cmp} timing (single run):")
    print(f"  Iterative O(n):         {(t1 - t0):.6f}s")
    print(f"  Memoized recursion O(n):{(t3 - t2):.6f}s")
    print(f"  Naive recursion ~exp:   {(t5 - t4):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (just the essentials)

* **Algorithmic interviews / DP warm-ups:** Fibonacci is the canonical example for demonstrating recursion vs memoization vs iteration and time/space trade-offs.
* **Financial modeling (toy growth curves):** Use Fibonacci-like recurrences to illustrate compounding and recursive relations.
* **Computer graphics / tiling / combinatorics:** Fibonacci counts ways to tile strips with dominos, count certain lattice paths, etc.—handy for DP pattern recognition.
* **Data structures education:** Showcase generator patterns, streaming output, and big-integer handling (Python) vs overflow considerations (other languages).

Want me to add judge-style printing (space-separated on one line) or a version that reads `n` from `stdin`?
