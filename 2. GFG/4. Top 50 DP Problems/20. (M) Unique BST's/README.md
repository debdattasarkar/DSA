# Unique BST's

**Difficulty:** Medium
**Accuracy:** 30.57%
**Submissions:** 85K+
**Points:** 4

---

Given an integer. Find how many **structurally unique binary search trees** are there that stores the values from **1 to that integer (inclusive)**.

---

## Examples

### Example 1

**Input:** `n = 2`
**Output:** `2`
**Explanation:** for `n = 2`, there are 2 unique BSTs.

### Example 2

**Input:** `n = 3`
**Output:** `5`
**Explanation:** for `N = 3`, there are 5 possible BSTs.

---

## Constraints

* `1 <= n <= 19`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Amazon • Microsoft • Samsung • Twitter

---

## Topic Tags

Dynamic Programming • Binary Search Tree • Data Structures • Algorithms

---

## Related Articles

* [Number Of Unique Bst With A Given Key Dynamic Programming](https://www.geeksforgeeks.org/number-of-unique-bst-with-a-given-key-dynamic-programming/)

---

---

# Unique BSTs — Explanation, Dry Run, and Python Solutions

## 2) Idea & Reasoning

If you place key `i` (1…n) at the root of a BST, then:

* the **left** subtree must be a BST built from the `i-1` smaller keys,
* the **right** subtree must be a BST built from the `n-i` larger keys.

Let `F(n)` be the number of unique BSTs on `n` keys. Then for a fixed root `i`,
the number of trees is `F(i-1) * F(n-i)`. Summing over all roots:

[
F(n) ;=; \sum_{i=1}^{n} F(i-1)\cdot F(n-i), \qquad F(0)=1,, F(1)=1
]

This is the **Catalan** recurrence; `F(n)` equals the `n`-th Catalan number.

### Step-by-step dry run (n = 3)

We fill `dp[0..n]`.

* `dp[0] = 1` (empty tree), `dp[1] = 1`.
* `dp[2] = dp[0]dp[1] + dp[1]dp[0] = 1*1 + 1*1 = 2`.
* `dp[3] = dp[0]dp[2] + dp[1]dp[1] + dp[2]dp[0]`
  `= 1*2 + 1*1 + 2*1 = 5`.

So for `n=3` there are **5** structurally unique BSTs.

---

## 3) Python solutions (with interview-style inline comments)

All methods implement the requested signature:

```python
# User function Template for python3
class Solution:
    # Function to return the total number of possible unique BST.
    def numTrees(self, n):
        # pick one of the implementations below
        ...
```

### A) Bottom-up DP (most common in interviews) — O(n²) time, O(n) space

```python
class Solution:
    # Function to return the total number of possible unique BST.
    def numTrees(self, n: int) -> int:
        # dp[k] = number of unique BSTs with k nodes
        dp = [0] * (n + 1)           # O(n) space
        dp[0] = dp[1] = 1            # base cases

        # For each size k, consider all choices of the root i (1..k)
        for k in range(2, n + 1):    # O(n) iterations
            total = 0
            for i in range(1, k + 1):                # O(k) each -> total O(n^2)
                total += dp[i - 1] * dp[k - i]       # combine left & right
            dp[k] = total

        return dp[n]
```

### B) Top-down with memoization — O(n²) time, O(n) memo

```python
from functools import lru_cache

class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def F(k: int) -> int:
            if k <= 1:
                return 1
            # sum over roots: left size = i-1, right size = k-i
            return sum(F(i - 1) * F(k - i) for i in range(1, k + 1))  # O(k)

        return F(n)  # total states k=0..n => O(n^2) time, O(n) space for memo
```

### C) Combinatorics (Catalan via binomial) — O(n) time, O(1) space

Catalan number:

[
C_n ;=; \frac{1}{n+1}\binom{2n}{n}
]

Use integer-safe multiplication to avoid floating point.

```python
import math

class Solution:
    def numTrees(self, n: int) -> int:
        # Python’s math.comb gives exact integer binomial coefficients
        return math.comb(2 * n, n) // (n + 1)   # O(1) math, overall O(n) due to comb implementation
```

### D) Catalan via multiplicative recurrence — O(n), O(1)

[
C_{0}=1,\quad C_{k+1} = C_k \cdot \frac{2(2k+1)}{k+2}
]

```python
class Solution:
    def numTrees(self, n: int) -> int:
        c = 1  # C_0
        for k in range(0, n):                  # O(n)
            c = c * 2 * (2 * k + 1) // (k + 2)  # stays integer at every step
        return c
```

> For `1 ≤ n ≤ 19`, all methods are safe; Python ints handle big values.

---

## 4) Interview Q&A

**Q1. Why does the DP recurrence work?**
Because choosing the root `i` partitions the keys into two independent sets:
`i-1` smaller keys (left subtree) and `n-i` larger keys (right subtree). The total number for that root is the product of possibilities, and we sum over all roots.

**Q2. What are the base cases and why?**
`F(0) = 1` (empty tree counts as one way) and `F(1) = 1`. These anchor the recurrence.

**Q3. Time/space complexity?**
Bottom-up or memoized DP: `O(n^2)` time (double loop) and `O(n)` space (one array).
Catalan via binomial or recurrence: `O(n)` time, `O(1)` extra space.

**Q4. Is the value of `F(n)` the Catalan number? Which one?**
Yes, `F(n)` is the `n`-th **Catalan** number. `C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42, …`

**Q5. Can you construct the actual trees?**
Yes, with a separate DP that generates structures: for each `k` and chosen root `i`, combine every left structure of size `i-1` and right structure of size `k-i`. That’s exponential in output size; counting is much cheaper.

**Q6. Why don’t node labels matter?**
In a BST with keys `1..n`, **inorder traversal is fixed (sorted)**; only the **shape** matters. Any set of keys `1..n` induces the same family of shapes, so the count depends only on `n`.

**Q7. How would you avoid overflow in languages without big ints?**
Use 64-bit where `n ≤ 19` fits, or compute via the multiplicative Catalan recurrence, simplifying with gcd at each step; or use big integer libraries.

**Q8. Relationship to other problems?**
Catalan numbers count many structures: valid parentheses strings of length `2n`, triangulations of polygons, ways to fully parenthesize products, etc.

---

---

All set! The program above:

* Implements **four** versions of `numTrees(n)` (DP, memoized, binomial Catalan, multiplicative Catalan).
* Prints **inputs, outputs**, and **best run-times** via `timeit`.
* Includes inline comments explaining **time and space complexity** for each step.

```python

# Re-run after kernel reset: include all code again and execute.
from functools import lru_cache
import math
import timeit

#User function Template for python3
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for k in range(2, n + 1):
            total = 0
            for i in range(1, k + 1):
                total += dp[i - 1] * dp[k - i]
            dp[k] = total
        return dp[n]

class SolutionMemo:
    def numTrees(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def F(k: int) -> int:
            if k <= 1:
                return 1
            return sum(F(i - 1) * F(k - i) for i in range(1, k + 1))
        return F(n)

class SolutionBinom:
    def numTrees(self, n: int) -> int:
        return math.comb(2 * n, n) // (n + 1)

class SolutionMul:
    def numTrees(self, n: int) -> int:
        c = 1
        for k in range(0, n):
            c = c * 2 * (2 * k + 1) // (k + 2)
        return c

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"n": 1, "expected": 1},
    {"n": 2, "expected": 2},
    {"n": 3, "expected": 5},
    {"n": 5, "expected": 42},
    {"n": 10, "expected": 16796},
    {"n": 19, "expected": 1767263190},
]

def run_and_report():
    print("=== Unique BSTs — Full Program with Timings ===\n")
    sol_dp   = Solution()
    sol_mem  = SolutionMemo()
    sol_bin  = SolutionBinom()
    sol_mul  = SolutionMul()

    for idx, t in enumerate(tests, 1):
        n, exp = t["n"], t["expected"]
        print(f"Test #{idx}: n={n} (expected={exp})")
        r1, t1 = time_call(lambda x: sol_dp.numTrees(x), n)
        print(f"  Bottom-up DP       : result={r1}, time={t1:.6f}s")
        r2, t2 = time_call(lambda x: sol_mem.numTrees(x), n)
        print(f"  Memoized (Top-Down): result={r2}, time={t2:.6f}s")
        r3, t3 = time_call(lambda x: sol_bin.numTrees(x), n)
        print(f"  Binomial Catalan   : result={r3}, time={t3:.6f}s")
        r4, t4 = time_call(lambda x: sol_mul.numTrees(x), n)
        print(f"  Multiplicative     : result={r4}, time={t4:.6f}s")
        all_same = (r1 == r2 == r3 == r4 == exp)
        print(f"  All correct? {all_same}\n")

run_and_report()


```

If you need a single interview-ready implementation with the requested template, use the **bottom-up DP**:

```python
#User function Template for python3

class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self, n: int) -> int:
        # dp[k] = number of unique BSTs with k nodes
        dp = [0] * (n + 1)     # Space: O(n)
        dp[0] = dp[1] = 1      # Base cases (empty and single node)

        # For each size k, try every node i as the root.
        # Time: sum_{k=2..n} k = O(n^2)
        for k in range(2, n + 1):
            total = 0
            for i in range(1, k + 1):
                total += dp[i - 1] * dp[k - i]   # left * right
            dp[k] = total

        return dp[n]
```

---

## Real-World Use Cases (the big ones)

* **Counting binary search index shapes:**
  Estimating possible BST shapes (Catalan counts) helps analyze search tree shape variety and average-case behaviors in indexing structures.

* **Compiler parsing / parenthesization:**
  Number of ways to fully parenthesize an expression with `n+1` factors equals the `n`-th Catalan number—same sequence as unique BSTs—important in parsing/grammar ambiguity analysis.

* **Catalan-class combinatorics:**
  Unique BSTs ↔ valid parentheses strings, monotonic lattice paths without crossing, polygon triangulations—shows up in DP counting, randomized testing, and combinatorial enumeration.
