# Dice throw

**Difficulty:** Medium
**Accuracy:** 36.52%
**Submissions:** 36K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given `n` dice each with `m` faces, find the **number of ways** to get sum `x`, which is the summation of values on each face when all the dice are thrown.

---

## Examples

### Example 1

**Input:** `m = 6, n = 3, x = 12`
**Output:** `25`
**Explanation:** There are 25 total ways to get the sum 12 using 3 dice with faces from 1 to 6.

---

### Example 2

**Input:** `m = 2, n = 3, x = 6`
**Output:** `1`
**Explanation:** There is only 1 way to get the sum 6 using 3 dice with faces from 1 to 2. All the dice will have to land on 2.

---

## Constraints

* `1 ≤ m, n, x ≤ 50`

---

## Expected Complexities

* **Time Complexity:** `O(m * n * x)`
* **Auxiliary Space:** `O(x)`

---

## Company Tags

* Amazon
* Microsoft

---

## Topic Tags

* Mathematical
* Algorithms
* Dynamic Programming
* Arrays

---

## Related Interview Experiences

* Microsoft IDC Internship Interview Experience On Campus

---

## Related Articles

* [Dice Throw DP 30](https://www.geeksforgeeks.org/dice-throw-dp-30/)

---

---

awesome — let’s make **Dice Throw** interview-ready.

---

# 2) Explanation + step-by-step dry run

## Problem recap

You have `n` dice, each with faces `1..m`. Count the **number of ways** to obtain total sum `x` when all dice are thrown.

Basic feasibility:

* If `x < n` (even all 1’s too large) or `x > m*n` (even all m’s too small) ⇒ **0**.

---

## Approach A (canonical DP, most expected)

Let `dp[d][s]` = number of ways to get sum `s` using exactly `d` dice.

Transitions:

* Base: `dp[0][0] = 1` (one way to make 0 with 0 dice), and `dp[0][s>0] = 0`.
* For each die `d = 1..n`, for each `s = 0..x`:

  ```
  dp[d][s] = sum_{face = 1..m} dp[d-1][s - face]   (if s - face >= 0)
  ```

Time `O(n * x * m)`, Space `O(n * x)` (can be reduced to `O(x)`).

### Dry run – Example: `m=6, n=3, x=12`

We fill by dice:

* `d=1`: ways to make `1..6` are 1 each; others 0.
* `d=2`: e.g., `dp[2][7] = dp[1][6]+dp[1][5]+...+dp[1][1] = 6`.
* `d=3`: compute sums up to 18. In particular,

  ```
  dp[3][12] = dp[2][11]+dp[2][10]+dp[2][9]+dp[2][8]+dp[2][7]+dp[2][6]
            = 6+5+4+3+2+5 = 25
  ```

Answer `25` ✅

---

## Approach B (space-optimized DP, 1D)

Use a single array `ways[s]` for “using current number of dice”. For each new die, update `s` **descending**:

```
for d in 1..n:
    next = [0..x]
    for s in 1..x:
        for face in 1..m:
            if s - face >= 0: next[s] += ways[s-face]
    ways = next
```

Still `O(n*m*x)` time, but only `O(x)` space.

---

## Approach C (math / inclusion–exclusion; fastest)

We want the number of integer solutions to

```
y1 + y2 + ... + yn = x,   with 1 ≤ yi ≤ m
```

Let `zi = yi - 1` ⇒ `zi ≥ 0` and `z1 + ... + zn = S = x - n`, with `zi ≤ m-1`.
By inclusion–exclusion, the count is

```
Ways = Σ_{k=0..⌊S/m⌋} (-1)^k * C(n, k) * C(S - k*m + n - 1, n - 1)
     = Σ_{k=0..⌊(x-n)/m⌋} (-1)^k * C(n, k) * C(x - k*m - 1, n - 1)
```

(define `0` if `x` out of range).
For our constraints (`≤ 50`), `math.comb` makes this trivial and very fast.

Check: `m=2, n=3, x=6` ⇒ `S=3`, sum over `k=0..1`:
`C(3,0)C(5,2) - C(3,1)C(3,2) = 10 - 9 = 1` ✅

---

# 3) Python solutions (multiple ways, interview-style)

Signature required:

```python
class Solution:
    def noOfWays(self, m,n,x):
        # code here
```

### A) Canonical DP (clear & expected)

```python
class Solution:
    def noOfWays(self, m, n, x):
        """
        dp[d][s] = ways to reach sum s using exactly d dice.

        Time : O(n * x * m)
        Space: O(n * x)
        """
        # Feasibility shortcut
        if x < n or x > m * n:
            return 0

        # dp with (n+1) x (x+1)
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # one way to make 0 with 0 dice

        for d in range(1, n + 1):
            for s in range(1, x + 1):
                total = 0
                # try all faces 1..m
                for face in range(1, m + 1):
                    if s - face >= 0:
                        total += dp[d - 1][s - face]
                dp[d][s] = total

        return dp[n][x]
```

---

### B) Space-optimized DP (1D array)

```python
class Solution1D:
    def noOfWays(self, m, n, x):
        """
        Rolling DP over sums.
        Time : O(n * x * m)
        Space: O(x)
        """
        if x < n or x > m * n:
            return 0

        ways = [0] * (x + 1)
        ways[0] = 1  # 0 dice -> sum 0

        for _ in range(n):                 # add one die each iteration
            nxt = [0] * (x + 1)
            for s in range(1, x + 1):
                # sum over faces
                # (unrolling / prefix sums could speed this up further)
                for face in range(1, m + 1):
                    if s - face >= 0:
                        nxt[s] += ways[s - face]
            ways = nxt

        return ways[x]
```

*(If you want `O(n*x)` time, you can use a sliding window/prefix-sum over faces, but `m ≤ 50` is already fine.)*

---

### C) Inclusion–Exclusion closed form (fastest, super clean here)

```python
import math

class SolutionMath:
    def noOfWays(self, m, n, x):
        """
        Ways = Σ_{k=0..floor((x-n)/m)} (-1)^k * C(n,k) * C(x - k*m - 1, n - 1),
        valid only if n <= x <= m*n, else 0.

        Time : O(min(n, (x-n)//m)) ~ O(50)
        Space: O(1)
        """
        if x < n or x > m * n:
            return 0

        S = x - n
        maxk = S // m
        ans = 0
        for k in range(0, maxk + 1):
            ans += ((-1) ** k) * math.comb(n, k) * math.comb(x - k * m - 1, n - 1)
        return ans
```

> In an interview: start with **A** (most common), mention **B** (space), then impress with **C** (combinatorial derivation).

---

# 4) Interview Q&A (high-yield)

**Q1. Why does the DP transition work?**
*A:* The last die shows a face `f ∈ [1..m]`; the remaining `n-1` dice must sum to `s-f`. Summing over all faces counts all possibilities.

**Q2. Base cases?**
*A:* `dp[0][0]=1`, `dp[0][s>0]=0`. Also guard with `x < n` or `x > m*n` ⇒ 0.

**Q3. Can we reduce space?**
*A:* Yes—use a 1D array over sums (Approach B), rebuilding a new array per die. Time remains `O(n*m*x)`, space `O(x)`.

**Q4. Any faster than `O(n*m*x)`?**
*A:* With prefix sums, each `dp[d][s]` can be computed in `O(1)` from a sliding window over `m` previous entries, giving `O(n*x)` time. For `m,x ≤ 50` the plain triple loop is fine. The **inclusion–exclusion** formula (Approach C) is fastest asymptotically for small bounds.

**Q5. Derive the inclusion–exclusion formula.**
*A:* Count solutions to `y1+…+yn=x` with `1≤yi≤m`. Set `zi=yi−1`, so `zi≥0`, sum=`S=x−n`, with `zi≤m−1`. Without upper bounds you have `C(S+n−1,n−1)`; subtract those where some `zi≥m` using inclusion–exclusion, yielding
`Σ_{k≥0} (-1)^k C(n,k) C(S - k*m + n - 1, n - 1)` which simplifies to the stated form.

**Q6. What if answers can be huge; do we need modulo?**
*A:* This prompt doesn’t require a modulus, and with `n,m,x ≤ 50` values fit easily in Python `int`. If a modulus is specified, add `% MOD` in transitions (DP) or after each term (math).

**Q7. Edge cases?**
*A:* Small sums (e.g., `x=n` → exactly one way: all 1’s), max sums (`x=m*n` → one way: all m’s), and infeasible ranges (`x<n` or `x>m*n` → 0).

---

---

here’s a **ready-to-run program** for **Dice Throw** that:

* reads `m n x` from stdin,
* computes the number of ways with **three methods**

  1. classic 2-D DP,
  2. space-optimized 1-D DP,
  3. inclusion–exclusion (combinatorics),
* prints answers and **times** each with `timeit.timeit(number=1)`.

I’ve added crisp, interview-style **time/space notes** inline.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Dice Throw: count ways to get sum x with n dice (faces 1..m)
#
# Methods:
#   1) 2-D DP (canonical)         : O(n * x * m) time, O(n * x) space
#   2) 1-D DP (space optimized)   : O(n * x * m) time, O(x) space
#   3) Inclusion–Exclusion (math) : O(min(n, (x-n)//m)) time, O(1) space
#
# Input (stdin):
#   m n x
#
# Output:
#   Answers + per-method timings (ms)
# ------------------------------------------------------------

import sys
import timeit
import math

# -------------------------- Method 1: 2-D DP --------------------------
class Solution2D:
    def noOfWays(self, m: int, n: int, x: int) -> int:
        """
        dp[d][s] = number of ways to get sum s using exactly d dice.

        Base:
          dp[0][0] = 1 (one way to make 0 with 0 dice)
          dp[0][s>0] = 0
        Transition:
          dp[d][s] = sum_{face=1..m} dp[d-1][s-face]  (if s-face >= 0)

        Time  : O(n * x * m) -- triple loop over d, s, face
        Space : O(n * x)     -- dp table (n+1) x (x+1)
        """
        # Quick feasibility: sum must be within [n, m*n]
        if x < n or x > m * n:
            return 0

        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Iterate dice count
        for d in range(1, n + 1):
            # For d dice, sum ranges from d..min(x, d*m)
            s_min = d
            s_max = min(x, d * m)
            for s in range(s_min, s_max + 1):
                total = 0
                # Sum faces; at most m additions
                # (guard s-face >= 0 by limiting face range)
                f_max = min(m, s)  # can't subtract more than s
                for face in range(1, f_max + 1):
                    total += dp[d - 1][s - face]
                dp[d][s] = total

        return dp[n][x]


# -------------------------- Method 2: 1-D DP --------------------------
class Solution1D:
    def noOfWays(self, m: int, n: int, x: int) -> int:
        """
        Rolling DP over sums.
        ways[s] = ways to get sum s with the current number of dice.

        For each new die:
          next[s] = sum_{face=1..m} ways[s-face]

        Time  : O(n * x * m)
        Space : O(x)
        """
        if x < n or x > m * n:
            return 0

        ways = [0] * (x + 1)
        ways[0] = 1  # 0 dice -> sum 0

        for d in range(1, n + 1):
            nxt = [0] * (x + 1)
            s_min = d
            s_max = min(x, d * m)
            for s in range(s_min, s_max + 1):
                f_max = min(m, s)
                # Sum faces in O(m); could be sped up by prefix sums if needed
                total = 0
                for face in range(1, f_max + 1):
                    total += ways[s - face]
                nxt[s] = total
            ways = nxt

        return ways[x]


# ------------------- Method 3: Inclusion–Exclusion --------------------
class SolutionMath:
    def noOfWays(self, m: int, n: int, x: int) -> int:
        """
        Count integer solutions to y1+...+yn = x with 1<=yi<=m.
        Let zi = yi-1 >= 0, sum zi = S = x - n, with zi <= m-1.

        Inclusion–Exclusion over upper bounds:
          Ways = Σ_{k=0..floor(S/m)} (-1)^k * C(n, k) * C(S - k*m + n - 1, n - 1)
               = Σ_{k=0..floor((x-n)/m)} (-1)^k * C(n, k) * C(x - k*m - 1, n - 1)

        Time  : O(min(n, (x-n)//m)) <= O(50) for constraints
        Space : O(1)
        """
        if x < n or x > m * n:
            return 0

        S = x - n
        maxk = S // m
        ans = 0
        for k in range(maxk + 1):
            term = ((-1) ** k) * math.comb(n, k) * math.comb(x - k * m - 1, n - 1)
            ans += term
        return ans


# ------------------------------- I/O ----------------------------------
def _read_params():
    """
    Accepts input as: 'm n x' (space/comma separated).
    """
    data = sys.stdin.read().strip().replace(",", " ").split()
    if len(data) < 3:
        print("Please provide three integers: m n x")
        sys.exit(0)
    m, n, x = map(int, data[:3])
    return m, n, x

def main():
    m, n, x = _read_params()
    print(f"m={m}, n={n}, x={x}\n")

    sol2d = Solution2D()
    sol1d = Solution1D()
    solmt = SolutionMath()

    # --- time each method once and collect results ---
    t2d  = timeit.timeit(lambda: sol2d.noOfWays(m, n, x), number=1)
    a2d  = sol2d.noOfWays(m, n, x)

    t1d  = timeit.timeit(lambda: sol1d.noOfWays(m, n, x), number=1)
    a1d  = sol1d.noOfWays(m, n, x)

    tmt  = timeit.timeit(lambda: solmt.noOfWays(m, n, x), number=1)
    amt  = solmt.noOfWays(m, n, x)

    print("2-D DP         (O(n*x*m) time, O(n*x) space):", a2d)
    print("Time (ms): {:.3f}\n".format(t2d * 1000.0))
    print("1-D DP         (O(n*x*m) time, O(x)   space):", a1d)
    print("Time (ms): {:.3f}\n".format(t1d * 1000.0))
    print("Inclusion-Excl (≈O(50)   time, O(1)   space):", amt)
    print("Time (ms): {:.3f}".format(tmt * 1000.0))

    ok = (a2d == a1d == amt)
    print("\nAll methods agree ✔" if ok else "\nWARNING: Methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 dice_throw.py
6 3 12
```

**Sample output (timings vary):**

```
m=6, n=3, x=12

2-D DP         (O(n*x*m) time, O(n*x) space): 25
Time (ms): 0.330

1-D DP         (O(n*x*m) time, O(x)   space): 25
Time (ms): 0.260

Inclusion-Excl (≈O(50)   time, O(1)   space): 25
Time (ms): 0.050

All methods agree ✔
```

Another quick check:

```bash
python3 dice_throw.py
2 3 6
```

Output:

```
m=2, n=3, x=6

2-D DP         ... : 1
Time (ms): 0.120

1-D DP         ... : 1
Time (ms): 0.105

Inclusion-Excl ... : 1
Time (ms): 0.019

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

* **Board/role-playing game odds:** compute exact counts/probabilities for reaching target sums with various dice (e.g., balance design, fairness checks).
* **Risk assessment & reliability:** sums of bounded discrete events (e.g., number of successes with capped contributions) modeled via dice abstractions.
* **Algorithmic combinatorics / probability teaching:** classic example to introduce DP counting, convolution, and inclusion–exclusion techniques.
