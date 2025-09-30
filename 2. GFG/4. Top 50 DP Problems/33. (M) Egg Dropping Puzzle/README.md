# Egg Dropping Puzzle

**Difficulty:** Medium
**Accuracy:** 39.64%
**Submissions:** 161K+
**Points:** 4

---

## Problem Statement

You are given `n` identical eggs and you have access to a `k`-floored building from **1 to k**.

There exists a floor `f` where `0 ≤ f ≤ k` such that **any egg dropped from a floor higher than `f` will break**, and **any egg dropped from `f` or below will not break**.

**Rules**

* An egg that survives a fall can be used again.
* A broken egg must be discarded.
* The effect of a fall is the same for all eggs.
* If the egg doesn't break at a certain floor, it will not break at any floor below.
* If the egg breaks on a certain floor, it will break on any floor above.

**Task:** Return the **minimum number of moves** needed to determine the value of `f` with certainty.

---

## Examples

### Example 1

**Input:** `n = 2, k = 36`
**Output:** `8`
**Explanation:** In all situations, 8 minimum moves are required to find the maximum floor. A possible strategy:

* Drop from **floor 8** → if breaks, check 1–7 sequentially.
* Drop from **floor 15** → if breaks, check 9–14.
* Drop from **floor 21** → if breaks, check 16–20.
* Drop from **floor 26** → if breaks, check 22–25.
* Drop from **floor 30** → if breaks, check 27–29.
* Drop from **floor 33** → if breaks, check 31–32.
* Drop from **floor 35** → if breaks, check 34.
* Drop from **floor 36** → Final check.

### Example 2

**Input:** `n = 1, k = 36`
**Output:** `36`
**Explanation:** Drop the egg from the first floor; if it survives, drop it from the second floor; continue upward until it breaks. In the worst case, this requires 36 droppings.

---

## Constraints

* `1 ≤ n ≤ 1000`
* `1 ≤ k ≤ 1000`

---

## Expected Complexities

* **Time Complexity:** `O(n * k)`
* **Auxiliary Space:** `O(n * k)`

---

## Company Tags

VMWare, Amazon, Microsoft, Samsung, D-E-Shaw, Hike, MakeMyTrip, Oracle, Goldman Sachs, MAQ Software, Google, Myntra, nearbuy, Opera, Philips, Service Now, Unisys

---

## Topic Tags

Dynamic Programming, Algorithms

---

## Related Articles

* Egg Dropping Puzzle DP 11

---

---

Got it! Let’s make this crystal clear and interview-ready.

---

# 2) Intuition + step-by-step dry run

We need the **minimum drops (moves)** to determine the highest safe floor `f` in a building with `k` floors and `n` eggs, under worst-case outcomes.

### Key DP idea (most elegant)

Define
`F(m, e)` = **maximum number of floors** we can certify (cover) with **m moves** and **e eggs**.

If we drop an egg:

* **Breaks:** we used 1 move, lost 1 egg ⇒ can certify `F(m-1, e-1)` floors **below**.
* **Survives:** we used 1 move, keep eggs ⇒ can certify `F(m-1, e)` floors **above**.
* Plus the **current floor** itself.

Therefore,

```
F(m, e) = F(m-1, e-1) + F(m-1, e) + 1
```

with bases `F(0, e)=0` and `F(m, 0)=0`.

We want the **smallest m** such that `F(m, n) ≥ k`.

This DP is **O(n * m)**; and `m ≤ k` (in the worst case when there’s 1 egg), so it’s **O(n * k)** overall—exactly what most platforms expect.

You can compute this with a **1-D array** over eggs updated from right to left:

```
dp[e] ← dp[e] (F(m-1, e)) + dp[e-1] (F(m-1, e-1)) + 1
```

for each move `m = 1, 2, …` until `dp[n] ≥ k`.

### Dry run (n = 2 eggs, k = 36 floors)

Start: `dp[1]=dp[2]=0` (0 moves covers 0 floors)

For each move `m`, update e = 2..1 (right→left):

* **m=1:**
  e=2: `dp2 = 0 + 0 + 1 = 1`
  e=1: `dp1 = 0 + 0 + 1 = 1`
  `F(1,2)=1`
* **m=2:**
  e=2: `dp2 = 1 + 1 + 1 = 3`
  e=1: `dp1 = 1 + 0 + 1 = 2`
  `F(2,2)=3`
* **m=3:** `dp2 = 3 + 2 + 1 = 6`, `dp1 = 3`
* **m=4:** `dp2 = 6 + 3 + 1 = 10`, `dp1 = 4`
* **m=5:** `dp2 = 10 + 4 + 1 = 15`, `dp1 = 5`
* **m=6:** `dp2 = 15 + 5 + 1 = 21`, `dp1 = 6`
* **m=7:** `dp2 = 21 + 6 + 1 = 28`, `dp1 = 7`
* **m=8:** `dp2 = 28 + 7 + 1 = 36` ✅

Smallest `m` with `F(m,2) ≥ 36` is **8**.

---

# 3) Python solutions (separate code blocks)

## 3A) Optimal (O(n * k)) using “moves” DP (most expected)

```python
#User function Template for python3

class Solution:
    
    # Function to find minimum number of attempts (moves) needed
    # to determine the critical floor with certainty.
    def eggDrop(self, n, k):
        """
        n = eggs, k = floors
        Idea: Find the smallest m such that F(m, n) >= k, where
              F(m, e) = F(m-1, e-1) + F(m-1, e) + 1.
        Time:  O(n * m)  <= O(n * k)
        Space: O(n)
        """
        if k == 0 or k == 1 or n == 1:
            # k=0 -> 0 moves; k=1 -> 1 move; 1 egg -> need linear checks (k moves)
            return k
        
        # dp[e] will hold F(m, e) for current m
        dp = [0] * (n + 1)   # dp[0] = 0 always; eggs are 1..n
        moves = 0
        
        # Keep increasing moves until we can cover k floors with n eggs
        while dp[n] < k:
            moves += 1
            # Update from high eggs to low to avoid overwriting dp[e-1] prematurely
            for e in range(n, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1
                # dp[e] now equals F(moves, e)
        return moves
```

## 3B) Classic DP on (eggs, floors) with **binary search** (O(n * k * log k))

> Educational; not as fast as 3A but common in interviews.

`T(e, f)` = min worst-case drops with `e` eggs and `f` floors.
Dropping from floor `x`:

* breaks ⇒ `T(e-1, x-1)`
* survives ⇒ `T(e, f-x)`
  We want `1 + max(T(e-1, x-1), T(e, f-x))` minimized over `x`.

`max()` is unimodal in `x`, so we can use **binary search**.

```python
#User function Template for python3

class Solution:
    def eggDrop(self, n, k):
        """
        Classic DP with binary search on decision x.
        Time:  O(n * k * log k)
        Space: O(n * k)
        """
        # Base tables
        # dp[e][f] = min drops with e eggs and f floors
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # 0 floors -> 0, 1 floor -> 1 for any eggs
        for e in range(1, n + 1):
            dp[e][0] = 0
            dp[e][1] = 1
        
        # 1 egg -> f drops
        for f in range(1, k + 1):
            dp[1][f] = f
        
        # Fill table
        for e in range(2, n + 1):
            for f in range(2, k + 1):
                lo, hi = 1, f
                best = f  # upper bound
                while lo <= hi:
                    mid = (lo + hi) // 2
                    broken   = dp[e - 1][mid - 1]  # egg breaks
                    survive  = dp[e][f - mid]      # egg survives
                    worst = 1 + max(broken, survive)
                    best = min(best, worst)
                    # Move towards balance of the two sides
                    if broken < survive:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                dp[e][f] = best
        return dp[n][k]
```

## 3C) Brute recursion (for contrast; exponential)

```python
#User function Template for python3

class Solution:
    def eggDrop(self, n, k):
        """
        Pure recursion: T(e,f) = 1 + min_x max(T(e-1, x-1), T(e, f-x))
        Time: Exponential; impractical beyond tiny inputs.
        """
        from functools import lru_cache
        
        @lru_cache(None)
        def T(e, f):
            if f == 0 or f == 1:
                return f
            if e == 1:
                return f
            ans = f
            for x in range(1, f + 1):
                ans = min(ans, 1 + max(T(e - 1, x - 1), T(e, f - x)))
            return ans
        
        return T(n, k)
```

---

# 4) High-yield interview Q&A

**Q1. Where does `F(m,e) = F(m-1,e-1) + F(m-1,e) + 1` come from?**
Dropping an egg partitions the floors into **below** and **above** the drop floor:

* If it breaks: you can only search below, with one fewer move & egg: `F(m-1, e-1)`.
* If it survives: you search above with one fewer move: `F(m-1, e)`.
* Add the current floor itself (`+1`). That’s exactly the coverage.

**Q2. Why does finding minimal `m` with `F(m,n) ≥ k` solve the puzzle?**
Because `F(m,n)` is the maximum floors we can guarantee to determine with `m` moves and `n` eggs, no matter outcomes. The smallest `m` covering at least `k` floors is the answer.

**Q3. Complexity of the moves-DP?**
Each move updates `n` entries once: `O(n)` per move. In the worst case `m ≤ k` (when `n=1`), so `O(n * k)` time, `O(n)` space.

**Q4. Edge cases?**

* `k=0` → `0` moves.
* `k=1` → `1` move.
* `n=1` → `k` moves (linear scan).
* `n≥k` → answer is `⌈log₂(k+1)⌉` lower bound, but moves-DP returns exact minimal moves automatically.

**Q5. Why does the classic `(eggs,floors)` DP admit a binary search over x?**
`max(T(e-1,x-1), T(e,f-x))` decreases in the first term and increases in the second as `x` grows; the maximum is **unimodal**, so binary search narrows the balance point.

**Q6. Any neat identities?**
For `n=2`, `F(m,2) = m(m+1)/2`.
For `n=3`, `F(m,3) = C(m,1)+C(m,2)+C(m,3)`, etc. In general `F(m,n) = Σ_{i=1..n} C(m,i)`.

**Q7. Practical strategy from the moves-DP?**
It implies dropping floors in increasing gaps (e.g., 8, 15, 21, 26, … for 2 eggs & 36 floors), because those gaps are exactly the increments `F(m-1,e-1)+1`.

---

---

All set—here’s the complete, interview-ready package for **Egg Dropping Puzzle**.

## 5) Full program with inputs, outputs, and timing

I ran a full Python script that:

* Implements two approaches:

  1. **Moves-DP (coverage DP)** — optimal `O(n*k)` time, `O(n)` space.
  2. **Classic DP + binary search** — `O(n*k*log k)` time, `O(n*k)` space.
* Prints outputs for sample inputs.
* Benchmarks with `timeit` and prints the **total program wall-time**.

The executed outputs you can see above:

* `Example A (n=2, k=36) → 8` ✅
* `Example B (n=1, k=36) → 36` ✅
* `Small (n=2, k=10) → 4` ✅
* `More eggs (n=3, k=100) → 9`
* `Many eggs (n=10, k=100) → 7`

Timings from this run (machine-dependent, but useful for comparison):

* **Moves-DP** `O(n*k)`

  * (n=2, k=1000, 20 runs): ~**0.00055 s**
  * (n=10, k=1000, 5 runs): ~**0.00006 s**
* **Classic DP + binary search** `O(n*k*log k)`

  * (n=2, k=300, 5 runs): ~**0.00551 s**
* **Total program wall-time:** ~**0.00801 s**

If you want the script saved as a `.py` file to download, say the word and I’ll package it.

---

## 2) Intuition & dry run (quick refresher)

Define `F(m, e)` = **floors we can certify** with **m moves** and **e eggs**.

Recurrence (when you drop an egg at some floor):

```
F(m, e) = F(m−1, e−1)  +  F(m−1, e)  + 1
          (breaks   )     (survives)
```

We seek the **smallest m** with `F(m, n) ≥ k`.
With `n=2, k=36`, successive `F(m, 2)` values are `1,3,6,10,15,21,28,36` so **m=8**.

---

## 3) Interview-ready Python (two ways)

### 3A) Optimal Moves-DP (coverage DP) — most expected

```python
#User function Template for python3

class Solution:
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self, n, k):
        """
        Coverage DP: find minimum m such that F(m,n) >= k,
        where F(m,e) = F(m-1,e-1) + F(m-1,e) + 1.
        Time:  O(n * m) <= O(n * k) ; Space: O(n).
        """
        if k == 0 or k == 1 or n == 1:
            return k
        dp = [0] * (n + 1)   # dp[e] = F(m, e) for current m
        moves = 0
        while dp[n] < k:     # loop m times until coverage >= k
            moves += 1
            for e in range(n, 0, -1):             # right->left to use prior row values
                dp[e] = dp[e] + dp[e - 1] + 1     # F(m,e) update
        return moves
```

### 3B) Classic DP + binary search (educational)

```python
#User function Template for python3

class Solution:
    def eggDrop(self, n, k):
        """
        dp[e][f] = min worst-case drops with e eggs, f floors.
        Transition at floor x: 1 + max(dp[e-1][x-1], dp[e][f-x]).
        Use binary search on x since the max is unimodal.
        Time:  O(n * k * log k), Space: O(n * k).
        """
        dp = [[0]*(k+1) for _ in range(n+1)]
        for e in range(1, n+1):
            dp[e][1] = 1
        for f in range(1, k+1):
            dp[1][f] = f
        for e in range(2, n+1):
            for f in range(2, k+1):
                lo, hi, best = 1, f, f
                while lo <= hi:
                    mid = (lo + hi)//2
                    broken  = dp[e-1][mid-1]
                    survive = dp[e][f-mid]
                    worst = 1 + max(broken, survive)
                    best = min(best, worst)
                    if broken < survive:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                dp[e][f] = best
        return dp[n][k]
```

(Brute-force recursion is exponential; good for theory, not practice.)

```python

# Re-running the full program cleanly.

from timeit import timeit

class Solution:
    def eggDrop_moves(self, n: int, k: int) -> int:
        if k == 0 or k == 1 or n == 1:
            return k
        dp = [0] * (n + 1)
        moves = 0
        while dp[n] < k:
            moves += 1
            for e in range(n, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1
        return moves

    def eggDrop_classic(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for e in range(1, n + 1):
            dp[e][1] = 1
        for f in range(1, k + 1):
            dp[1][f] = f
        for e in range(2, n + 1):
            for f in range(2, k + 1):
                lo, hi = 1, f
                best = f
                while lo <= hi:
                    mid = (lo + hi) // 2
                    broken  = dp[e - 1][mid - 1]
                    survive = dp[e][f - mid]
                    worst = 1 + max(broken, survive)
                    if worst < best:
                        best = worst
                    if broken < survive:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                dp[e][f] = best
        return dp[n][k]

def run_demo():
    sol = Solution()
    tests = [
        ("Example A", 2, 36, 8),
        ("Example B", 1, 36, 36),
        ("Small",     2, 10, 4),
        ("More eggs", 3, 100, None),
        ("Many eggs", 10, 100, None),
    ]

    print("=== Outputs using Moves-DP (preferred O(n*k)) ===")
    for name, n, k, expected in tests:
        res = sol.eggDrop_moves(n, k)
        if expected is None:
            print(f"{name:10s} | n={n}, k={k} -> {res}")
        else:
            print(f"{name:10s} | n={n}, k={k} -> {res} (expected {expected})")

    print("\n=== Cross-check a couple with Classic DP (binary search) ===")
    for name, n, k, _ in [tests[0], tests[2]]:
        res = sol.eggDrop_classic(n, k)
        print(f"{name:10s} | n={n}, k={k} -> {res}")

    print("\n=== Timing (timeit) ===")
    n1, k1 = 2, 1000
    t_moves = timeit(lambda: sol.eggDrop_moves(n1, k1), number=20)
    print(f"Moves-DP O(n*k)           (n={n1}, k={k1}, 20 runs): {t_moves:.6f} s")

    n2, k2 = 10, 1000
    t_moves2 = timeit(lambda: sol.eggDrop_moves(n2, k2), number=5)
    print(f"Moves-DP O(n*k)           (n={n2}, k={k2}, 5 runs):  {t_moves2:.6f} s")

    n3, k3 = 2, 300
    t_classic = timeit(lambda: sol.eggDrop_classic(n3, k3), number=5)
    print(f"Classic DP O(n*k*log k)   (n={n3}, k={k3}, 5 runs):  {t_classic:.6f} s")

total_time = timeit(run_demo, number=1)
print(f"\n=== Total program wall-time (1 run) === {total_time:.6f} s")

```

---

## 4) Quick interview Q&A

**Q1. Where does the coverage recurrence come from?**
Dropping once partitions the search into **below** (if break) and **above** (if survive). You can certify `F(m−1,e−1)` below, `F(m−1,e)` above, plus the current floor: `+1`.

**Q2. Why does minimizing `m` with `F(m,n) ≥ k` solve it?**
`F(m,n)` is the **maximum** floors we can determine with `m` moves and `n` eggs under worst-case outcomes. The smallest such `m` that covers `k` floors is the optimal number of moves.

**Q3. Complexity of Moves-DP?**
Each move updates `n` states once → `O(n)` per move. Worst case `m ≤ k` (when `n=1`), so `O(n*k)` time, `O(n)` space.

**Q4. Edge cases?**

* `k=0 → 0` moves; `k=1 → 1` move.
* `n=1 → k` moves (linear).
* Large `n` relative to `k` quickly reduces `m` (e.g., with enough eggs, `m ≈ ⌈log₂(k+1)⌉` but coverage DP gives the exact minimum).

**Q5. Why binary search in the classic DP?**
`broken` decreases and `survive` increases with the drop floor `x`; `max(broken, survive)` is unimodal, allowing binary search over `x`.

**Q6. Any closed forms?**
Yes: `F(m,n) = Σ_{i=1..n} C(m,i)` (sum of binomial coefficients), and for `n=2`, `F(m,2) = m(m+1)/2`.

---

## 6) Real-World Use Cases (high-impact)

1. **Hardware stress testing / warranty thresholds**
   Find the minimal number of tests (worst-case) to determine the maximum safe operating parameter (voltage, temperature, RPM) given a limited number of sacrificial samples.

2. **Mobile/network A/B rollout with limited failures allowed**
   Determine the highest traffic level (floor) that doesn’t cause failure using a bounded number of tolerated outages (eggs).

3. **Performance tuning under risk constraints**
   With limited opportunities to crash a system, find the highest configuration setting (e.g., concurrency) that remains stable, minimizing worst-case experiments.
