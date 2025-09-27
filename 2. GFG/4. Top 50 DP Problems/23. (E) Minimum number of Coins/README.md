# Minimum number of Coins

**Difficulty:** Easy
**Accuracy:** 51.25%
**Submissions:** 102K+
**Points:** 2

---

Given an **infinite supply** of each denomination of Indian currency **{ 1, 2, 5, 10 }** and a target value **n**. Find the **minimum** number of coins and/or notes needed to make the change for **Rs n**.

---

## Examples

### Example 1

**Input:** `n = 39`
**Output:** `6`
**Explanation:** 39 can be formed using **3** coins of **10** rupees, **1** coin of **5** rupees and **2** coins of **2** rupees so minimum coins required are **6**.

### Example 2

**Input:** `n = 121`
**Output:** `13`
**Explanation:** 121 can be formed using **12** coins of **10** rupees and **1** coin of **1** rupees.

---

## Constraints

* `1 ≤ n ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Visa

---

## Topic Tags

Dynamic Programming • Greedy • Algorithms

---

## Related Articles

* Greedy Algorithm To Find Minimum Number Of Coins

---

---

# Minimum Number of Coins — {1, 2, 5, 10}

## 2) Intuition & Step-by-Step Dry Run

We have infinite coins of denominations **1, 2, 5, 10**. For this specific set, the **greedy** strategy is **optimal**:

1. Take as many `10`s as possible.
2. From the remainder, take as many `5`s as possible.
3. Then `2`s.
4. Whatever remains are `1`s.

Why greedy is optimal here (quick reasoning):

* Any five 1’s can be replaced by one 5 (fewer coins).
* Any two 5’s can be replaced by one 10 (fewer coins).
* Any two 1’s can be replaced by one 2.
  Hence, always prefer the largest denomination available.

### Dry run 1: `n = 39`

* 10s: `39 // 10 = 3` → use 3 tens, remainder `39 % 10 = 9`
* 5s : `9 // 5 = 1`  → use 1 five,  remainder `9 % 5 = 4`
* 2s : `4 // 2 = 2`  → use 2 twos,  remainder `4 % 2 = 0`
* 1s : `0`           → none
  Total coins = `3 + 1 + 2 + 0 = 6` ✅

### Dry run 2: `n = 121`

* 10s: `12`, remainder `1`
* 5s : `0`, remainder `1`
* 2s : `0`, remainder `1`
* 1s : `1`
  Total coins = `12 + 0 + 0 + 1 = 13` ✅

---

## 3) Python solutions (interview-ready, with inline comments)

### A) Greedy with division/modulo — **O(1)** time, **O(1)** space (recommended)

```python
class Solution:
    def findMin(self, n: int) -> int:
        # Handle n = 0 gracefully (though constraints say n >= 1)
        if n <= 0:
            return 0
        
        # Count 10-rupee coins
        c10 = n // 10             # O(1)
        n  %= 10                  # O(1)
        
        # Count 5-rupee coins from remainder
        c5  = n // 5              # O(1)
        n  %= 5                   # O(1)
        
        # Count 2-rupee coins from remainder
        c2  = n // 2              # O(1)
        n  %= 2                   # O(1)
        
        # Remaining are 1-rupee coins
        c1  = n                   # O(1)
        
        # Total coins is sum of counts
        return c10 + c5 + c2 + c1
```

> One-liner equivalent (same logic):
> `return n//10 + (n%10)//5 + (n%5)//2 + (n%2)`

---

### B) Bottom-up DP (generic coin change) — **O(n)** time, **O(n)** space

Useful to demonstrate generality (works for any coin set containing 1).

```python
class SolutionDP:
    def findMin(self, n: int) -> int:
        # dp[x] = minimum coins to make sum x
        # Initialize with +inf; dp[0] = 0 (0 coins to make 0)
        INF = 10**9
        dp = [0] + [INF] * n           # O(n) space
        
        coins = [1, 2, 5, 10]
        for x in range(1, n + 1):      # O(n) outer
            for c in coins:            # 4 coins → O(1) inner
                if x - c >= 0:
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[n]                    # O(1)
```

---

### C) Simple greedy by repeated subtraction — **O(n)** time, **O(1)** space

This is the “brute but easy to think” version; still correct, but slower.

```python
class SolutionSubtract:
    def findMin(self, n: int) -> int:
        count = 0
        for c in (10, 5, 2, 1):     # try largest to smallest
            while n >= c:           # subtract repeatedly
                n -= c
                count += 1
        return count
```

---

## 4) Interview-style Q&A

**Q1. Why does greedy (10 → 5 → 2 → 1) always yield the minimum here?**
Because this denomination set is **canonical**: any combination using smaller coins can be replaced by fewer larger coins without increasing the count (e.g., `5×1 → 1×5`, `2×5 → 1×10`, `2×1 → 1×2`). Thus, it’s always optimal to take the largest possible coin first.

**Q2. What’s the time/space complexity?**

* Greedy with division/modulo: **O(1)** time, **O(1)** space (constant operations).
* DP (generic): **O(n)** time, **O(n)** space.
* Repeated subtraction: **O(n)** time, **O(1)** space.

**Q3. What if we changed the denominations (e.g., {1, 3, 4})—would greedy still be optimal?**
Not necessarily. For {1, 3, 4}, greedy for `n=6` picks `4+1+1` (3 coins), but optimal is `3+3` (2 coins). That’s why the DP approach is the safe general solution.

**Q4. Do we need to handle `n = 0`?**
Constraints say `n ≥ 1`, but handling `0` gracefully with output `0` is good hygiene.

**Q5. Can we also return the **composition** of coins?**
Yes—keep track of how many of each denomination you took in the greedy method (the counts `c10, c5, c2, c1`) or reconstruct from `dp` by backtracking which coin gave the minimum at each `x`.

**Q6. Why does the problem statement list expected time as O(n)?**
That’s a generic expectation (e.g., for DP). For this fixed canonical set, you can do **better** with O(1) greedy.

---

---

All set! I ran a **full program** that includes three solutions (Greedy O(1), DP O(n), and a simple subtractive greedy O(n)) and printed **inputs, outputs, and best timings** via `timeit`. You can see the console output above.

```python

# Fix the incorrect expected value for n=19 and re-run the report
tests[4]["expected"] = 4
run_and_report()


```

If you want a single interview-ready class with the required signature, use the greedy one:

```python
class Solution:
    def findMin(self, n: int) -> int:
        # Optimal greedy for denominations {10, 5, 2, 1}
        # Time: O(1) — just a few divisions/modulos
        # Space: O(1)
        if n <= 0:
            return 0
        c10 = n // 10; n %= 10
        c5  = n // 5 ; n %= 5
        c2  = n // 2 ; n %= 2
        c1  = n
        return c10 + c5 + c2 + c1
```

### Why greedy is optimal here

For {1,2,5,10} you can always replace smaller coins with fewer larger ones:

* `2×1 → 1×2`, `5×1 → 1×5`, `2×5 → 1×10`.
  So always take the largest denomination first.

### What the full program included

* `SolutionGreedy.findMin` — O(1) and a helper to print the coin **composition** (10s, 5s, 2s, 1s).
* `SolutionDP.findMin` — generic bottom-up coin change DP (O(n) time, O(n) space).
* `SolutionSubtract.findMin` — repeated subtraction version (simple but O(n)).

---

## Real-World Use Cases (the important ones)

1. **ATM / cash register dispensing**
   Compute the *fewest notes/coins* to hand out for a given amount using a canonical set (like {1,2,5,10}). This reduces item count (faster handover, fewer physical pieces).

2. **Vending machines & kiosks**
   Optimal change-making to minimize coins dispensed, reducing hopper usage and reload frequency; canonical Indian denominations match this greedy solution.

3. **Cash logistics & reconciliation**
   Tallying or refilling drawers using minimal pieces for target fund levels (e.g., build ₹n float using the least notes/coins).
