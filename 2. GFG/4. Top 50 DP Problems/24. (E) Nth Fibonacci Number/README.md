# Nth Fibonacci Number

**Difficulty:** Easy
**Accuracy:** 22.3%
**Submissions:** 374K+
**Points:** 2

---

Given a non-negative integer `n`, your task is to find the **nth Fibonacci number**.

The **Fibonacci sequence** is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`

The Fibonacci sequence is defined as follows:

* `F(0) = 0`
* `F(1) = 1`
* `F(n) = F(n - 1) + F(n - 2)` for `n > 1`

---

## Examples

### Example 1

**Input:** `n = 5`
**Output:** `5`
**Explanation:** The 5th Fibonacci number is 5.

### Example 2

**Input:** `n = 0`
**Output:** `0`
**Explanation:** The 0th Fibonacci number is 0.

### Example 3

**Input:** `n = 1`
**Output:** `1`
**Explanation:** The 1st Fibonacci number is 1.

---

## Constraints

* `0 ≤ n ≤ 30`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Amazon • Microsoft • OYO Rooms • Snapdeal • MakeMyTrip • Goldman Sachs • MAQ Software • Adobe

---

## Topic Tags

Dynamic Programming • Mathematical • Fibonacci • Algorithms

---

## Related Interview Experiences

* Makemytrip Interview Experience Set 11 Developer Position

---

## Related Articles

* Cpp Program For Fibonacci Numbers
* Program For Nth Fibonacci Number

---

---

# Nth Fibonacci — Explanation, Dry Run, and Python Solutions

## 2) Idea & Dry Run

**Definition**

* `F(0) = 0`
* `F(1) = 1`
* `F(n) = F(n-1) + F(n-2)` for `n > 1`

**Key observations**

* The value depends only on the previous **two** values ⇒ we can keep **two variables** and iterate.
* For extra speed, we can use the **fast-doubling** identities to compute in **O(log n)** time.

**Dry run (n = 5)**

Sequence: `0, 1, 1, 2, 3, 5`

Iterative two-var update:

```
a=0, b=1     # F0, F1
i=2: a,b = b, a+b -> 1,1
i=3: a,b = b, a+b -> 1,2
i=4: a,b = b, a+b -> 2,3
i=5: a,b = b, a+b -> 3,5
return b -> 5
```

Edge checks:
`n=0 -> 0`, `n=1 -> 1` (returned directly).

---

## 3) Python solutions (with interview-style inline comments)

### A) Recommended: Iterative with two variables — `O(n)` time, `O(1)` space

```python
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Handle trivial bases in O(1)
        if n <= 1:
            return n

        # Maintain only the last two Fibonacci numbers
        a, b = 0, 1  # a = F(i-2), b = F(i-1)
        # Loop runs (n-1) times -> O(n) time, O(1) space
        for _ in range(2, n + 1):
            a, b = b, a + b  # advance the pair
        return b
```

---

### B) Tabulation (array DP) — simple & explicit, `O(n)` time, `O(n)` space

```python
class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n + 1)       # O(n) space
        dp[1] = 1
        for i in range(2, n + 1):  # O(n) time
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

---

### C) Top-down recursion **with memoization** — `O(n)` time, `O(n)` space

```python
from functools import lru_cache

class Solution:
    def nthFibonacci(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def F(k: int) -> int:
            if k <= 1:
                return k
            # Each state computed once -> O(n)
            return F(k - 1) + F(k - 2)
        return F(n)
```

> (Avoid *plain* recursion without memo — it’s `O(ϕ^n)` and not interview-friendly unless asked for “brute”.)

---

### D) Fast Doubling (divide & conquer) — `O(log n)` time, `O(log n)` space

Uses identities:

* `F(2k)   = F(k) * [2*F(k+1) − F(k)]`
* `F(2k+1) = F(k+1)^2 + F(k)^2`

```python
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Returns (F(n), F(n+1))
        def fib_pair(k: int):
            if k == 0:
                return (0, 1)  # (F0, F1)
            a, b = fib_pair(k // 2)      # a=F(m), b=F(m+1) for m=k//2
            c = a * ((b << 1) - a)       # F(2m)   = F(m)*(2*F(m+1)-F(m))
            d = a * a + b * b            # F(2m+1) = F(m)^2 + F(m+1)^2
            if k % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)        # (F(2m+1), F(2m+2))
        return fib_pair(n)[0]
```

---

## 4) Interview Q&A

**Q1. What’s the simplest optimal solution and its complexity?**
Iterative two-variable DP. **Time:** `O(n)`; **Space:** `O(1)`.

**Q2. Can you do better than `O(n)` time?**
Yes. **Fast doubling** (or matrix exponentiation) computes `F(n)` in **`O(log n)`** time.

**Q3. Why avoid plain recursion without memoization?**
It recomputes the same subproblems exponentially many times (`~ϕ^n` calls), quickly blowing up.

**Q4. What are the base cases and why?**
`F(0)=0`, `F(1)=1`. They anchor the recurrence; for `n≤1`, return `n`.

**Q5. Will Python overflow?**
No. Python integers are arbitrary precision. (If a modulus were required, you’d take `% MOD` at each addition.)

**Q6. Space usage comparisons?**

* Two-var iterative: `O(1)`
* Tabulation: `O(n)` (keeps all states)
* Memoized recursion: `O(n)` for cache and recursion depth
* Fast doubling: `O(log n)` recursion depth

**Q7. How does fast doubling work (intuition)?**
It uses identities for `F(2k)` and `F(2k+1)` to halve the index each recursion, similar to exponentiation by squaring.

---

---

All set — I ran a full program that implements **four** Fibonacci methods, prints results for several inputs, and reports **best timings** using `timeit`. You can scroll up to see the console output.

```python

# Re-run after kernel reset: include all code again and execute.
from functools import lru_cache
import timeit

class SolutionIter:
    def nthFibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

class SolutionTab:
    def nthFibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

class SolutionMemo:
    def nthFibonacci(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def F(k: int) -> int:
            if k <= 1:
                return k
            return F(k-1) + F(k-2)
        return F(n)

class SolutionFastDouble:
    def nthFibonacci(self, n: int) -> int:
        def pair(k: int):
            if k == 0:
                return (0, 1)
            a, b = pair(k // 2)
            c = a * ((b << 1) - a)
            d = a * a + b * b
            if k % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)
        return pair(n)[0]

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"n": 5,  "expected": 5},
    {"n": 0,  "expected": 0},
    {"n": 1,  "expected": 1},
    {"n": 10, "expected": 55},
    {"n": 20, "expected": 6765},
    {"n": 30, "expected": 832040},
]

def run_and_report():
    print("=== Nth Fibonacci — Full Program ===\n")
    it  = SolutionIter()
    tb  = SolutionTab()
    me  = SolutionMemo()
    fd  = SolutionFastDouble()

    for idx, t in enumerate(tests, 1):
        n, exp = t["n"], t["expected"]
        print(f"Test #{idx}: n={n} (expected={exp})")
        r1, t1 = time_call(lambda x: it.nthFibonacci(x), n)
        print(f"  Iterative O(n)        : result={r1}, best={t1:.6f}s")
        r2, t2 = time_call(lambda x: tb.nthFibonacci(x), n)
        print(f"  Tabulation O(n)       : result={r2}, best={t2:.6f}s")
        r3, t3 = time_call(lambda x: me.nthFibonacci(x), n)
        print(f"  Memoized O(n)         : result={r3}, best={t3:.6f}s")
        r4, t4 = time_call(lambda x: fd.nthFibonacci(x), n)
        print(f"  Fast Doubling O(log n): result={r4}, best={t4:.6f}s")
        all_ok = (r1 == r2 == r3 == r4 == exp)
        print(f"  All correct? {all_ok}\n")

run_and_report()

```

If you need a single interview-ready class with the requested signature, the **iterative two-variable** version is perfect:

```python
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Time:  O(n) — one pass from 2..n
        # Space: O(1) — only two variables
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

You can also mention (if asked) that **fast doubling** computes `F(n)` in **O(log n)** time:

```python
class Solution:
    def nthFibonacci(self, n: int) -> int:
        def pair(k: int):
            if k == 0: return (0, 1)
            a, b = pair(k // 2)
            c = a * ((b << 1) - a)     # F(2m)
            d = a*a + b*b              # F(2m+1)
            return (c, d) if k % 2 == 0 else (d, c + d)
        return pair(n)[0]
```

---

## Real-World Use Cases (the heavy hitters)

1. **Algorithmic complexity analysis & interview baselines**
   Fibonacci is a canonical example for DP vs. naive recursion; it trains thinking about overlapping subproblems and state compression.

2. **Fast integer algorithms & number theory**
   Fast doubling is a practical example of divide-and-conquer arithmetic, closely related to matrix exponentiation and used in computations like Pisano periods or Fibonacci hashing.

3. **Financial & modeling sequences**
   Though literal Fibonacci sequences are rare in production, their recurrences mirror many **linear recurrences** in economics, simulations, and time-series models where O(1) state DP or fast exponentiation techniques are essential.
