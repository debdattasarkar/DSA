# Minimum Operations

**Difficulty:** Easy
**Accuracy:** 60.02%
**Submissions:** 105K+
**Points:** 2

---

Given a number `n`. Find the **minimum number of operations** required to reach `n` starting from `0`. You have **two operations** available:

* **Double** the number
* **Add one** to the number

---

## Example 1

**Input:** `n = 8`
**Output:** `4`
**Explanation:** `0 + 1 = 1 --> 1 + 1 = 2 --> 2 * 2 = 4 --> 4 * 2 = 8.`

---

## Example 2

**Input:** `n = 7`
**Output:** `5`
**Explanation:** `0 + 1 = 1 --> 1 + 1 = 2 --> 1 + 2 = 3 --> 3 * 2 = 6 --> 6 + 1 = 7.`

---

## Constraints

* `1 <= n <= 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

Dynamic Programming • Greedy • Algorithms

---

## Related Articles

* Minimize Steps To Reach K From 0 By Adding 1 Or Doubling At Each Step

---

---

# Minimum Operations — Explanation, Dry Run, and Python Solutions

## 2) Intuition

We start at **0** and want to reach **n** using only:

1. **+1**
2. **×2**

Two equivalent ways to reason:

### A) Work **backwards** from `n` (greedy)

* If `n` is **even**, the step before it must have been `n/2` (cheapest), so do `n //= 2`.
* If `n` is **odd**, the step before it must have been `n-1`, so do `n -= 1`.
  Repeating until `n == 0` counts the **minimum** steps (classic Dijkstra-on-a-line intuition with unit weights; dividing halves the remaining distance fastest).

### B) Build `n` by **bits** from left to right

Write `n` in binary. To “construct” that number starting at 0:

* For each bit after the first: we **double** once (shift left).
* Whenever the bit is `1`, we also **+1**.
* The total operations = `(#doubles) + (#adds)` = `(bit_length(n) - 1) + popcount(n)`.

Both views give the same answer.

---

## Step-by-step dry runs

### Example 1: `n = 8 (1000₂)`

Backward greedy:

* 8 is even → `8/2 = 4` (1)
* 4 is even → `4/2 = 2` (2)
* 2 is even → `2/2 = 1` (3)
* 1 is odd  → `1-1 = 0` (4)
  **Steps = 4**

Bit view: `bit_length=4`, `popcount=1` → `4-1 + 1 = 4`.

### Example 2: `n = 7 (111₂)`

Backward greedy:

* 7 odd → 6 (1)
* 6 even → 3 (2)
* 3 odd → 2 (3)
* 2 even → 1 (4)
* 1 odd → 0 (5)
  **Steps = 5**

Bit view: `bit_length=3`, `popcount=3` → `3-1 + 3 = 5`.

---

## 3) Python solutions (interview-ready, with inline comments)

### ✅ Recommended: Greedy from `n` to `0` (O(log n), O(1))

```python
# User function Template for python3

class Solution:
    def minOperation(self, n: int) -> int:
        """
        Greedy backwards:
          - if n is even, the previous state must be n//2  (cheapest)
          - if n is odd,  the previous state must be n-1
        Stops at 0; counts steps.

        Time:  O(log n)    (each divide by 2 removes one bit; odd cases are O(popcount))
        Space: O(1)
        """
        steps = 0
        while n > 0:                 # loop runs ≈ bit_length(n) + popcount(n) times
            if n & 1:                # odd?
                n -= 1               # make it even: one operation
            else:
                n >>= 1              # divide by 2: one operation
            steps += 1
        return steps
```

### Bit-math one-liner (same complexity but constant-factor tiny)

```python
class SolutionBitMath:
    def minOperation(self, n: int) -> int:
        """
        Build n from its binary representation:
          operations = (number of doubles) + (number of +1's)
                      = (bit_length - 1) + popcount
        Edge: n=0 -> 0 (constraints say n>=1).
        Time:  O(1) arithmetically, but popcount/bit_length are O(#machine words) ~ O(1).
        Space: O(1)
        """
        if n == 0:
            return 0
        return (n.bit_length() - 1) + n.bit_count()
```

### Brute (for completeness): BFS from 0 to n (O(n))

```python
from collections import deque

class SolutionBFS:
    def minOperation(self, n: int) -> int:
        """
        Unweighted shortest path on states 0..n using edges:
          x -> x+1, x -> 2*x
        Returns minimum steps.
        Time:  O(n) in worst case (visiting each state up to n once)
        Space: O(n)
        """
        if n == 0:
            return 0
        seen = [False] * (n + 1)
        q = deque([(0, 0)])          # (value, steps)
        seen[0] = True

        while q:
            x, d = q.popleft()
            if x == n:
                return d
            # Try +1
            if x + 1 <= n and not seen[x + 1]:
                seen[x + 1] = True
                q.append((x + 1, d + 1))
            # Try *2
            if x * 2 <= n and not seen[x * 2]:
                seen[x * 2] = True
                q.append((x * 2, d + 1))
        return -1  # unreachable for n>=0
```

---

## 4) Interview Q&A

**Q1. Why does the backward greedy (divide when even, minus one when odd) give an optimal solution?**
Because with unit-cost operations and nonnegative states, whenever `n` is even, reaching `n` from `n/2` takes **1** step, while any path via `n-1` would require at least **2** steps to get back to `n` (…→ `n-1` → `2*(n-1)` ≥ `n`). So dividing by 2 is never worse. When `n` is odd, you **must** do `-1` once to become even. This monotone choice is optimal at each step.

**Q2. What’s the complexity?**
The loop runs once per bit (for divides) plus once per set bit (for subtracts): `O(bit_length(n) + popcount(n)) = O(log n)` time, `O(1)` space.

**Q3. Can you express the answer in closed form?**
Yes. For `n > 0`:
`min_ops(n) = (bit_length(n) - 1) + popcount(n)`.

**Q4. Why does the bit formula work?**
Construct `n` from MSB to LSB:

* First set bit requires a `+1` from 0.
* For each remaining bit position, you **double** once; if that bit is `1`, you **+1** once.
  Total = doubles `(bit_length - 1)` + number of +1’s `(popcount)`.

**Q5. Any edge cases?**

* `n = 1` → `1` (`0 → 1`).
* `n = 0` (if allowed) → `0`.
* Large `n` fits fine (Python ints are unbounded).

**Q6. If the starting number were 1 instead of 0, would the formula change?**
Yes: from 1 you already have the MSB; you’d need `bit_length(n) - 1` doubles plus `(popcount(n) - 1)` adds (for remaining 1-bits), so total `bit_length(n) + popcount(n) - 2`.

---

---

Here’s a complete, runnable program (above) that:

* Implements three versions: **Greedy**, **Bit-math**, and **BFS**.
* Prints **inputs, outputs**, and **best times** using `timeit`.
* Includes inline comments pointing out **time and space complexity** for each step.

```python

# Re-run after kernel reset: include all code again and execute.
from collections import deque
import timeit

class SolutionGreedy:
    def minOperation(self, n: int) -> int:
        steps = 0
        while n > 0:
            if n & 1:
                n -= 1
            else:
                n >>= 1
            steps += 1
        return steps

class SolutionBitMath:
    def minOperation(self, n: int) -> int:
        if n == 0:
            return 0
        return (n.bit_length() - 1) + n.bit_count()

class SolutionBFS:
    def minOperation(self, n: int) -> int:
        if n == 0:
            return 0
        seen = [False] * (n + 1)
        q = deque([(0, 0)])
        seen[0] = True
        while q:
            x, d = q.popleft()
            if x == n:
                return d
            nx = x + 1
            if nx <= n and not seen[nx]:
                seen[nx] = True
                q.append((nx, d + 1))
            nx = x * 2
            if nx <= n and not seen[nx]:
                seen[nx] = True
                q.append((nx, d + 1))
        return -1

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"n": 8, "expected": 4},
    {"n": 7, "expected": 5},
    {"n": 1, "expected": 1},
    {"n": 2, "expected": 2},
    {"n": 123456, "expected": None},
    {"n": 10**6, "expected": None},
]

def run_and_report():
    print("=== Minimum Operations — Full Program ===\n")
    greedy = SolutionGreedy()
    bitm   = SolutionBitMath()
    bfs    = SolutionBFS()

    for idx, t in enumerate(tests, 1):
        n, exp = t["n"], t["expected"]
        if exp is None:
            exp = bitm.minOperation(n)
        print(f"Test #{idx}: n={n}")

        r1, t1 = time_call(lambda x: greedy.minOperation(x), n)
        print(f"  Greedy     : result={r1}, expected={exp}, best={t1:.6f}s")

        r2, t2 = time_call(lambda x: bitm.minOperation(x), n)
        print(f"  Bit-Math   : result={r2}, expected={exp}, best={t2:.6f}s")

        if n <= 50000:
            r3, t3 = time_call(lambda x: bfs.minOperation(x), n)
            print(f"  BFS        : result={r3}, expected={exp}, best={t3:.6f}s")
        else:
            print("  BFS        : skipped (n too large for O(n) BFS)")

        print(f"  All OK? {r1 == r2 == exp}\n")

run_and_report()


```

If you only need the interview-ready class with the requested signature, use the greedy one:

```python
#User function Template for python3

class Solution:
    def minOperation(self, n: int) -> int:
        # Greedy from n to 0: even -> n//=2, odd -> n-=1
        # Time:  O(log n); Space: O(1)
        steps = 0
        while n > 0:
            if n & 1:   # odd
                n -= 1
            else:       # even
                n >>= 1
            steps += 1
        return steps
```

You can also cite the compact bit formula:

```python
# O(1) bit-math version
ops = (n.bit_length() - 1) + n.bit_count()
```

---

## Real-World Use Cases (the important ones)

* **Instruction scheduling & codegen:** modeling minimal steps to synthesize a constant using shifts and increments (`<<1` and `+1`)—common in compiler peephole optimizations.
* **Protocol / counter updates:** deriving minimal operations for counters that permit doubling and increment (e.g., exponential backoff + bump).
* **Energy/time budgeting in embedded systems:** estimating least number of micro-ops where hardware offers a fast “double” and a cheap “+1”.

If you want, I can add a small stdin/stdout driver or extend tests to random values for quick stress checks.
