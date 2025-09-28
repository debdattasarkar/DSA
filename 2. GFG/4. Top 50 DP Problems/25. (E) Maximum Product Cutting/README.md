# Maximum Product Cutting

**Difficulty:** Easy
**Accuracy:** 22.67%
**Submissions:** 5K+
**Points:** 2

---

Given a rope of length **N** meters, cut the rope in different parts of **integer lengths** in a way that **maximizes the product of lengths** of all parts. You **must make at least one cut**. Assume that the length of the rope is more than one meter.

---

## Examples

### Example 1

**Input:** `N = 5`
**Output:** `6`
**Explanation:** Maximum obtainable product is `2 * 3`.

### Example 2

**Input:** `N = 2`
**Output:** `1`
**Explanation:** Maximum obtainable product is `1 * 1`.

---

## Your Task

You don't need to read input or print anything. Complete the function **`maxProduct(N)`** which takes **N** as input parameter and **returns the maximum product**.

---

## Expected Complexities

* **Time Complexity:** `O(N^2)`
* **Auxiliary Space:** `O(N)`

---

## Constraints

* `2 ≤ N ≤ 50`

---

## Topic Tags

Dynamic Programming • Algorithms

---

---
# Maximum Product Cutting — crisp guide

## 2) Intuition + dry run

We must cut a rope of length `n` into **integer parts** to **maximize the product** of the parts. The statement also implies **“make at least one cut.”**

### DP idea (the interview-standard)

Let `dp[i]` = **best product** for length `i` **with at least one cut**.

If the first cut is at position `j` (`1 ≤ j < i`), the right piece `(i - j)` can be:

* left **uncut** → product `j * (i - j)` (this guarantees we made a cut), or
* cut **further optimally** → product `j * dp[i - j]`.

So:

```
dp[i] = max over j=1..i-1 of max( j*(i-j), j*dp[i-j] )
```

Base we use for transitions:

* `dp[1] = 1` (a helper value so `j*dp[1]` is valid).
* Many judges also query `n = 1`; they expect the **answer 1**. (Even though typical constraints say `n ≥ 2`.)

### Dry run (n = 5)

We build `dp[2..5]`.

* `dp[1] = 1`
* `i=2`

  * `j=1`: max(`1*1`, `1*dp[1]=1`) = **1** → `dp[2]=1`
* `i=3`

  * `j=1`: max(`1*2`, `1*dp[2]=1`) = **2**
  * `j=2`: max(`2*1`, `2*dp[1]=2`) = **2** → `dp[3]=2`
* `i=4`

  * `j=1`: max(3, 2) = 3
  * `j=2`: max(4, 2) = **4**
  * `j=3`: max(3, 3) = 3 → `dp[4]=4`
* `i=5`

  * `j=1`: max(4, 4) = 4
  * `j=2`: max(6, 4) = **6**
  * `j=3`: max(6, 2) = **6**
  * `j=4`: max(4, 4) = 4 → `dp[5]=6`

Answer for `n=5` is **6** (`2 × 3`).

Edge samples:

* `n=1 → 1` (judge’s expectation)
* `n=2 → 1` (`1×1`)
* `n=3 → 2` (`2×1`)

---

## 3) Python solutions (with interview-style inline comments)

### ✅ A) Tabulation DP (most expected) — `O(n^2)` time, `O(n)` space

```python
# User function Template for python3
class Solution:
    def maxProduct(self, n: int) -> int:
        """
        dp[i] = best product for length i with at least one cut
        Transition:
          dp[i] = max over j=1..i-1 of max( j*(i-j), j*dp[i-j] )
        Time : O(n^2)
        Space: O(n)
        """
        # ---- EDGE CASE (many judges ask n=1 and expect 1) ----
        if n == 1:
            return 1

        dp = [0] * (n + 1)   # O(n) space
        dp[1] = 1            # helper base used in transitions

        # Build from small to large lengths
        for i in range(2, n + 1):           # O(n) iterations
            best = 0
            for j in range(1, i):           # O(i) each -> total O(n^2)
                # option 1: stop cutting right piece now
                # option 2: cut right piece optimally
                best = max(best, j * (i - j), j * dp[i - j])
            dp[i] = best
        return dp[n]
```

### ⚡ B) Greedy / Math (O(1)) — cut into 3’s (with 2’s to fix a remainder 1)

```python
class SolutionGreedy:
    def maxProduct(self, n: int) -> int:
        """
        Cut into as many 3's as possible; if remainder is 1, turn 3+1 into 2+2.
        (Handles 'must cut': n=2->1, n=3->2)
        Time : O(1)
        Space: O(1)
        """
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2

        a, r = divmod(n, 3)          # a=# of 3's, r in {0,1,2}
        if r == 0: return 3 ** a
        if r == 1: return (3 ** (a - 1)) * 4  # use ... + 2 + 2
        return (3 ** a) * 2                   # r == 2
```

### 🧠 C) Top-down recursion + memo (same recurrence) — `O(n^2)` time, `O(n)` space

```python
from functools import lru_cache

class SolutionMemo:
    def maxProduct(self, n: int) -> int:
        """
        Same DP recurrence, written recursively with memoization.
        Time : O(n^2)  (n states; each tries up to n splits)
        Space: O(n)    (memo + recursion depth)
        """
        @lru_cache(maxsize=None)
        def solve(i: int) -> int:
            if i == 1:
                return 1
            best = 0
            for j in range(1, i):
                best = max(best, j * (i - j), j * solve(i - j))
            return best

        return solve(n if n >= 1 else 1)   # be safe on n=0 though not expected
```

### (Optional) Brute recursion (exponential) — rarely asked except to “start simple”

```python
class SolutionBrute:
    def maxProduct(self, n: int) -> int:
        if n == 1: return 1
        best = 0
        for j in range(1, n):
            best = max(best, j * (n - j), j * self.maxProduct(n - j))
        return best
# Time ~ exponential; Space ~ recursion depth O(n)
```

---

## 4) Interview Q&A (short & targeted)

**Q1. How does the DP enforce “at least one cut”?**
In every transition we **first cut** at `j` and multiply by `j`. The other factor is either `(i-j)` (no further cuts) or `dp[i-j]` (further cuts). So a cut at `j` is always made.

**Q2. Why are 3’s optimal in the greedy solution?**
For a fixed sum, product increases when parts are closer to `e≈2.718`. Among integers, `3` dominates; `3+1` is worse than `2+2`. Hence: fill with 3’s; if a remainder `1` appears, convert one `3+1` into `2+2`.

**Q3. Edge values?**

* `n=1 → 1` (some judges query it).
* `n=2 → 1` (`1×1`), `n=3 → 2` (`2×1`).
* For `n≥4`, DP/greedy produce the usual results (`4→4`, `5→6`, …).

**Q4. Complexity?**

* DP tabulation: `O(n^2)` time, `O(n)` space.
* Memoized recursion: `O(n^2)` time, `O(n)` space.
* Greedy math: `O(1)` time/space.

**Q5. How would you return the actual cut pattern?**
In DP, keep a `choice[i]` storing the `j` (and whether you took `(i-j)` or `dp[i-j]`), then backtrack from `n` to list the pieces.

**Q6. Why did some online judges fail on my `if n <= 1: return 0`?**
Because they **test `n=1`** and expect **`1`**. Change the guard to `if n == 1: return 1`.

---

---

Done! I executed a **full, runnable program** that:

* Implements **DP**, **Greedy/Math**, and **Memoized recursion** versions of `maxProduct(n)`.
* Prints **inputs, outputs**, and **best run-times** using `timeit`.
* Verifies that all methods agree (see the console output above).

```python

from functools import lru_cache
import timeit

class SolutionDP:
    def maxProduct(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            best = 0
            for j in range(1, i):
                best = max(best, j * (i - j), j * dp[i - j])
            dp[i] = best
        return dp[n]

class SolutionGreedy:
    def maxProduct(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2
        a, r = divmod(n, 3)
        if r == 0: return 3**a
        if r == 1: return (3**(a-1)) * 4
        return (3**a) * 2

class SolutionMemo:
    def maxProduct(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def solve(i: int) -> int:
            if i == 1: return 1
            best = 0
            for j in range(1, i):
                best = max(best, j*(i-j), j*solve(i-j))
            return best
        return solve(1 if n < 1 else n)

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"n": 1,  "expected": 1},
    {"n": 2,  "expected": 1},
    {"n": 3,  "expected": 2},
    {"n": 4,  "expected": 4},
    {"n": 5,  "expected": 6},
    {"n": 8,  "expected": None},
    {"n": 10, "expected": None},
    {"n": 25, "expected": None},
    {"n": 50, "expected": None},
]

def run_and_report():
    print("=== Maximum Product Cutting — Full Program ===\n")
    dp   = SolutionDP()
    gr   = SolutionGreedy()
    memo = SolutionMemo()

    for idx, t in enumerate(tests, 1):
        n, exp = t["n"], t["expected"]
        if exp is None:
            exp = gr.maxProduct(n)
        print(f"Test #{idx}: n={n} | expected={exp}")
        r1, t1 = time_call(lambda x: dp.maxProduct(x), n)
        print(f"  DP O(n^2)       : result={r1}, best={t1:.6f}s")
        r2, t2 = time_call(lambda x: gr.maxProduct(x), n)
        print(f"  Greedy O(1)     : result={r2}, best={t2:.6f}s")
        r3, t3 = time_call(lambda x: memo.maxProduct(x), n)
        print(f"  Memo O(n^2)     : result={r3}, best={t3:.6f}s")
        print(f"  All agree? {r1 == r2 == r3 == exp}\n")

run_and_report()

```

Below is the **interview-ready** DP solution in the requested signature, plus alternatives.

---

### Interview-ready DP (expected `O(n^2)` solution)

```python
#User function Template for python3
class Solution:
    def maxProduct(self, n: int) -> int:
        """
        dp[i] = best product for rope length i with at least one cut.
        Transition:
          dp[i] = max over j=1..i-1 of max( j*(i-j), j*dp[i-j] )
        Time : O(n^2)  (double loop)
        Space: O(n)    (dp array)
        """
        # Some judges pass n=1 and expect 1 (even if constraints often say n>=2)
        if n == 1:
            return 1

        dp = [0] * (n + 1)   # O(n) space
        dp[1] = 1            # helper base for transitions

        for i in range(2, n + 1):          # O(n)
            best = 0
            for j in range(1, i):          # O(i) per i  => O(n^2) total
                # Option 1: stop cutting right piece now
                # Option 2: cut right piece optimally
                best = max(best, j * (i - j), j * dp[i - j])
            dp[i] = best

        return dp[n]
```

### Fast alternative (math/greedy, O(1))

```python
class SolutionGreedy:
    def maxProduct(self, n: int) -> int:
        # Cut into as many 3’s as possible; if remainder is 1, use 2+2.
        # Time/Space: O(1)
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2
        a, r = divmod(n, 3)
        if r == 0: return 3**a
        if r == 1: return (3**(a-1)) * 4
        return (3**a) * 2
```

### Recurrence, top-down with memo (clear logic)

```python
from functools import lru_cache

class SolutionMemo:
    def maxProduct(self, n: int) -> int:
        # Time: O(n^2), Space: O(n)
        @lru_cache(maxsize=None)
        def solve(i: int) -> int:
            if i == 1:
                return 1
            best = 0
            for j in range(1, i):
                best = max(best, j*(i-j), j*solve(i-j))
            return best
        return solve(1 if n < 1 else n)
```

---

## Real-World Use Cases (the important ones)

* **Budget / resource partitioning:** When a total budget (time, CPU quota, ad spend) is split into integer chunks and overall payoff multiplies across chunks (e.g., independent success probabilities), cutting into 3-ish sized parts approximates the **max product** strategy.

* **Reliability engineering:** Allocating discrete redundant units across independent subsystems where **system reliability is multiplicative** across stages. Integer constraints make this problem directly relevant.

* **Throughput of multi-stage workflows:** If stage performance multiplies to overall throughput, distributing limited discrete workers/machines across stages to **maximize product** mirrors this rope-cutting optimization.

If you want, I can extend the program to also print an **optimal cut composition** (e.g., counts of 3’s and 2’s) using either the greedy math or backtracking from the DP.
