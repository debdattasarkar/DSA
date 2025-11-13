
---

# 🪨 Minimum Cost to Merge Stones

**Difficulty:** Hard
**Accuracy:** 42.28%
**Submissions:** 2K+
**Points:** 8
**Average Time:** 45m

---

## 🧠 Problem Statement

Given an array `stones[]`, where the `i`ᵗʰ element represents the number of stones in the `i`ᵗʰ pile.

In one move, you can **merge exactly `k` consecutive piles** into a single pile, and the cost of this move is equal to the **total number of stones** in these `k` piles.

Determine the **minimum total cost** required to merge all the piles into one single pile.

If it is not possible to merge all piles into one according to the given rules, return **-1**.

---

## 🧩 Examples

### Example 1

**Input:**

```
stones[] = [1, 2, 3], k = 2
```

**Output:**

```
9
```

**Explanation:**
Initially the array looks like `[1, 2, 3]`.

* First, we merge first 2 stones → `[3, 3]` and cost = 1 + 2 = 3.
* Then, we merge remaining stones (3 and 3) → `[6]` and cost = 3 + 3 = 6.

Total cost = 3 + 6 = **9**.

---

### Example 2

**Input:**

```
stones[] = [1, 5, 3, 2, 4], k = 2
```

**Output:**

```
35
```

**Explanation:**
Initially the array looks like `[1, 5, 3, 2, 4]`.

* Merge 1 and 5 → `[6, 3, 2, 4]` with cost = 6
* Merge 3 and 2 → `[6, 5, 4]` with cost = 5
* Merge 5 and 4 → `[6, 9]` with cost = 9
* Merge 6 and 9 → `[15]` with cost = 15

Total cost = 6 + 5 + 9 + 15 = **35**.

---

### Example 3

**Input:**

```
stones[] = [1, 5, 3, 2, 4], k = 4
```

**Output:**

```
-1
```

**Explanation:**
It is **not possible** to merge piles in groups of 4 and end up with exactly 1 pile.
Hence, the answer is **-1**.

---

## ⚙️ Constraints

* ( 1 \leq \text{stones.size()} \leq 30 )
* ( 2 \leq k \leq 30 )
* ( 1 \leq \text{stones[i]} \leq 100 )

---

## ⏱️ Expected Complexities

| Complexity Type     | Value |
| ------------------- | ----- |
| **Time**            | O(n³) |
| **Auxiliary Space** | O(n²) |

---

## 🧩 Topic Tags

* Dynamic Programming
* Algorithms

---

---

Awesome — let’s crack **Minimum Cost to Merge Stones** like an interview pro.

---

## 2) Intuition + Step-by-Step Dry Run

### Problem in one line

You have piles `stones[i]`. In one move you can **merge exactly `k` consecutive piles** into one pile, paying the **sum** of those `k` piles. Find the **minimum total cost** to get **one** pile (or `-1` if impossible).

### Feasibility check (must memorize)

After each merge of `k` piles → pile count drops by **`k-1`**.
Starting from `n` piles and ending at `1` requires:

```
(n - 1) % (k - 1) == 0
```

If false → **impossible** → return `-1`.

### Core DP idea (interval DP)

Let `sum(i, j)` be the total stones in `stones[i..j]` (use prefix sums).
Let `dp[i][j]` be the **minimum cost to merge** the interval `[i..j]` **as much as possible**.

* If the interval length allows it to become **one pile**, we **add** `sum(i, j)` (the final merge cost).
* Otherwise we only combine subintervals toward fewer piles but stop short of the last “make 1 pile” step.

**Transitions**
We can only combine sub-parts at split points stepping by `(k-1)`:

```
dp[i][j] = min over m = i, i+(k-1), i+2*(k-1), ... < j of
           dp[i][m] + dp[m+1][j]

If (j - i) % (k - 1) == 0:
    dp[i][j] += sum(i, j)   # we can compress the current interval to 1 pile now
```

Base: `dp[i][i] = 0` (single pile costs nothing).

This is the standard O(n³) (amortized O(n³/(k-1))) interval DP.

---

### Dry run: `stones = [1, 2, 3]`, `k = 2`

* Feasibility: `(3-1) % (2-1) = 2 % 1 = 0` ✓
* Prefix sums: `pref=[0,1,3,6]`, so `sum(i,j)=pref[j+1]-pref[i]`.

Lengths:

1. Length=2

* `[0..1]`: `dp[0][1] = dp[0][0]+dp[1][1] = 0`. Since `(1-0)%(1)=0`, add `sum(0,1)=3` → `dp=3`.
* `[1..2]`: `dp[1][2] = 0 + 0`, add `sum(1,2)=5` → `dp=5`.

2. Length=3

* `[0..2]`: try split `m=0` and `m=1` (step = k-1 = 1):

  * `m=0`: `dp[0][0]+dp[1][2] = 0 + 5 = 5`
  * `m=1`: `dp[0][1]+dp[2][2] = 3 + 0 = 3`
    → `min=3`
  * Since `(2-0) % 1 == 0`, add `sum(0,2) = 6` → `3 + 6 = 9`.

Answer: **9**, matching the sample (merge 1+2=3 cost 3; then 3+3=6 cost 6; total 9).

---

## 3) Python solutions (teaching → optimal)

Use your requested signature:

```python
class Solution:
    def mergeStones(self, stones, k):
        # code here
```

### A) (Teaching aid) Plain recursion — exponential (don’t use for large n)

Shows the structure; quickly explodes without memoization.

```python
class Solution:
    def mergeStones(self, stones, k):
        from functools import lru_cache

        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        pref = [0]
        for x in stones: pref.append(pref[-1] + x)
        def rng(i, j): return pref[j + 1] - pref[i]

        # Exponential without memo, shown only for concept
        def cost(i, j):
            if i == j: return 0
            best = float('inf')
            # split points step by (k-1)
            m = i
            while m < j:
                best = min(best, cost(i, m) + cost(m + 1, j))
                m += (k - 1)
            if (j - i) % (k - 1) == 0:
                best += rng(i, j)
            return best

        return cost(0, n - 1)
```

### B) Top-down DP (memoized) — **clean & interview friendly**

```python
class Solution:
    def mergeStones(self, stones, k):
        """
        Interval DP with memoization.
        Time  : O(n^3 / (k-1)) in practice (n<=30 fits)
        Space : O(n^2) memo
        """
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        # prefix sums for O(1) range sum
        pref = [0]
        for x in stones:
            pref.append(pref[-1] + x)
        def rng(i, j):  # sum of stones[i..j]
            return pref[j + 1] - pref[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            best = float('inf')
            # Only split at steps of (k-1)
            m = i
            while m < j:
                best = min(best, dp(i, m) + dp(m + 1, j))
                m += (k - 1)
            # If we can compress current interval into 1 pile, pay its sum
            if (j - i) % (k - 1) == 0:
                best += rng(i, j)
            return best

        return dp(0, n - 1)
```

### C) Bottom-up DP — **tabulation** (same logic, explicit loops)

```python
class Solution:
    def mergeStones(self, stones, k):
        """
        Bottom-up interval DP.
        Time  : O(n^3/(k-1)) ~ O(n^3)
        Space : O(n^2)
        """
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        # prefix sums
        pref = [0]
        for x in stones:
            pref.append(pref[-1] + x)
        def rng(i, j): return pref[j + 1] - pref[i]

        # dp[i][j] = min cost to merge stones[i..j] as much as possible
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):          # interval length
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = float('inf')
                # split at steps of (k-1)
                m = i
                while m < j:
                    best = min(best, dp[i][m] + dp[m + 1][j])
                    m += (k - 1)
                if (length - 1) % (k - 1) == 0:  # compress to one pile
                    best += rng(i, j)
                dp[i][j] = best

        return dp[0][n - 1]
```

> Notes you can say out loud:
>
> * The `(k-1)` step in the split loop is critical; it prunes invalid merge shapes.
> * When interval length allows **1 final pile** → pay `sum(i..j)`; otherwise wait.

---

## 4) Interview quick-recall + Q&A

### 5-line pseudo (memorize this)

```
if (n-1) % (k-1) != 0: return -1
pref = prefix sums
dp[i][i] = 0
for len = 2..n:
  for i..:
    j = i+len-1
    dp[i][j] = min_{m=i, i+k-1, ... < j} dp[i][m] + dp[m+1][j]
    if (len-1) % (k-1) == 0: dp[i][j] += sum(i..j)
return dp[0][n-1]
```

**Mnemonic:**
**“Feasibility first; split by `(k-1)`; add range-sum only when interval can become one pile.”**

### Expected Q&A

**Q1. When is it impossible?**
When `(n-1) % (k-1) != 0`. Each merge reduces pile count by `k-1`; to reach exactly 1 pile, that divisibility must hold.

**Q2. Why only split by `(k-1)`?**
Because after merging subintervals optimally, the number of piles you can produce in each side must align to let you merge them in groups of `k`. Restricting splits to steps of `(k-1)` ensures the counts are merge-compatible.

**Q3. Why do we add `sum(i..j)` only sometimes?**
The cost is charged **only when we actually merge into 1 pile** for the interval. If the current length cannot become 1 pile yet, we’re still “pre-grouping” without paying the final merge cost.

**Q4. Complexity?**
`n ≤ 30`. DP uses `O(n²)` states; each tries `O(n/(k-1))` splits → about **O(n³)** time, **O(n²)** space.

**Q5. What if `k=2`?**
The split step becomes every `1` index (standard interval DP for optimal merging of adjacent segments). Still **O(n³)** with the above DP (though special cases can be faster).

**Q6. Why prefix sums?**
To compute `sum(i..j)` in **O(1)** while DPing — necessary for speed.

---

---

Great wrap-up! Here are (5) crisp, relatable use cases and (6) a complete, runnable Python program (with timing and inline complexity notes) for **Minimum Cost to Merge Stones**.

---

## 5) Real-World Use Cases (short & interviewer-friendly)

* **File chunk consolidation:** Merging `k` adjacent file blocks into a larger block where I/O cost equals the sum of block sizes; you want the minimal total read/write cost to end with one block.
* **Batching micro-services requests:** Every merge executes exactly `k` adjacent requests together with a cost proportional to payload sum; plan batching order to minimize total compute/network cost.
* **Data compaction in LSM trees:** Compact exactly `k` neighboring SSTables at a time; compaction cost ≈ bytes merged. Schedule compaction order to minimize cumulative bytes processed.
* **Audio/video stitching:** Join `k` consecutive clips into one clip; rendering/export cost is additive in durations. Choose merge order to minimize total render time.
* **Manufacturing/assembly:** Combine exactly `k` adjacent components in a line; the energy/cost is proportional to combined weight/material. Optimize total assembly energy.

Each maps to: *merge exactly `k` consecutive units, cost = sum of those `k`; minimize total to one unit, or report impossible.*

---

## 6) Full Program (DP with timing + thorough inline complexity notes)

```python
"""
Minimum Cost to Merge Stones
----------------------------
We have piles 'stones[i]'. One operation merges EXACTLY k consecutive piles into one,
paying the SUM of the k piles. Minimize total cost to end with ONE pile, or return -1
if impossible.

Core facts:
- After each merge, pile count decreases by (k - 1).
- Feasible iff (n - 1) % (k - 1) == 0.

Approach: Interval DP (top-down with memo) + prefix sums.
  dp(i, j) = min cost to merge stones[i..j] "as much as possible".
  We only ADD rng(i,j) (the sum) when this interval can be compressed to ONE pile:
      if (j - i) % (k - 1) == 0: dp(i, j) += rng(i, j)
  Splits are restricted to m = i, i+(k-1), i+2*(k-1), ... < j
  to ensure pile counts stay merge-compatible.

Complexities (n ≤ 30 fits easily):
- States: O(n^2)
- Each state tries O(n / (k-1)) splits  → ~ O(n^3) time
- Memo table: O(n^2) space
"""

import timeit
from functools import lru_cache
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
        Interval DP with memoization.

        Step-by-step complexity:
          - Feasibility check: O(1)
          - Prefix sums: O(n) time, O(n) space
          - DP states: O(n^2); each state tries O(n/(k-1)) splits
            -> Total time ~ O(n^3) (good for n ≤ 30)
          - Memo cache: O(n^2) space

        Returns:
          Minimum total cost (int), or -1 if impossible.
        """
        n = len(stones)
        # ----- Feasibility: must be able to reach exactly one pile -----
        if (n - 1) % (k - 1) != 0:  # O(1)
            return -1

        # ----- Prefix sums for O(1) interval sums -----
        pref = [0] * (n + 1)  # O(n) space
        for i, x in enumerate(stones, 1):       # O(n) time
            pref[i] = pref[i - 1] + x

        def rng(i: int, j: int) -> int:
            """Sum of stones[i..j] in O(1) time."""
            return pref[j + 1] - pref[i]

        # ----- Memoized interval DP -----
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            """
            Min cost to merge interval [i..j] as far as possible.
            Space: stored in LRU cache (O(n^2) entries).
            """
            if i == j:
                return 0  # single pile → no cost

            best = float("inf")

            # Split points step by (k-1) to keep pile counts compatible.
            m = i
            while m < j:
                best = min(best, dp(i, m) + dp(m + 1, j))
                m += (k - 1)

            # If this interval can be compressed to ONE pile now, pay its sum.
            if (j - i) % (k - 1) == 0:
                best += rng(i, j)

            return best

        return dp(0, n - 1)


# ------------------------------- Demo & Timing -------------------------------
if __name__ == "__main__":
    tests = [
        # (stones, k, expected)
        ([1, 2, 3], 2, 9),
        ([1, 5, 3, 2, 4], 2, 35),
        ([1, 5, 3, 2, 4], 4, -1),
        ([3, 2, 4, 1], 2, 20),      # classic LC sample
        ([3, 5, 1, 2, 6], 3, 25),   # classic LC sample
    ]

    solver = Solution()
    print("Minimum Cost to Merge Stones (interval DP, O(n^3) / O(n^2))\n")

    for stones, k, expected in tests:
        # Time the full function call once (includes all DP work)
        elapsed = timeit.timeit(lambda: solver.mergeStones(stones, k), number=1)
        ans = solver.mergeStones(stones, k)
        print(f"stones={stones}, k={k} -> {ans} (expected {expected}), time={elapsed:.6f}s")
```

### What you’ll see on run (example)

```
Minimum Cost to Merge Stones (interval DP, O(n^3) / O(n^2))

stones=[1, 2, 3], k=2 -> 9 (expected 9), time=0.0000xxs
stones=[1, 5, 3, 2, 4], k=2 -> 35 (expected 35), time=0.0000xxs
stones=[1, 5, 3, 2, 4], k=4 -> -1 (expected -1), time=0.0000xxs
stones=[3, 2, 4, 1], k=2 -> 20 (expected 20), time=0.0000xxs
stones=[3, 5, 1, 2, 6], k=3 -> 25 (expected 25), time=0.0000xxs
```

**Interview one-liner** to remember:

> “Check feasibility `(n−1)%(k−1)==0`. Do interval DP; split only every `(k−1)`; add `rangeSum` when the interval can shrink to **one** pile.”
