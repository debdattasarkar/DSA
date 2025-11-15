
---

# 🔗 Longest Common Increasing Subsequence (LCIS)

**Difficulty:** Medium
**Accuracy:** 30.77%
**Submissions:** 11K+
**Points:** 4

---

## 🧠 Problem Statement

Given two arrays, **a[]** and **b[]**, find the **length of the longest common increasing subsequence (LCIS)**.

**Note:**
LCIS refers to a subsequence that is **present in both arrays** and **strictly increases**.

---

## 🧩 Examples

### Example 1

**Input:**

```
a[] = [3, 4, 9, 1]
b[] = [5, 3, 8, 9, 10, 2, 1]
```

**Output:**

```
2
```

**Explanation:**
The longest increasing subsequence that is common is `[3, 9]`, and its length is **2**.

---

### Example 2

**Input:**

```
a[] = [1, 1, 4, 3]
b[] = [1, 1, 3, 4]
```

**Output:**

```
2
```

**Explanation:**
There are two common increasing subsequences `[1, 4]` and `[1, 3]`, both of length **2**.

---

## ⚙️ Constraints

* ( 1 \leq a.size(), b.size() \leq 10^3 )
* ( 1 \leq a[i], b[i] \leq 10^4 )

---

## ⏱️ Expected Complexities

| Complexity Type     | Value    |
| ------------------- | -------- |
| **Time**            | O(n × m) |
| **Auxiliary Space** | O(n)     |

---

## 🧩 Topic Tags

* Arrays
* Dynamic Programming
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Longest Common Increasing Subsequence (LCIS)](https://www.geeksforgeeks.org/longest-common-increasing-subsequence-lcs-lis/)

---

---

awesome — let’s make **LCIS (Longest Common Increasing Subsequence)** interview-ready.

---

# 2) Intuition + step-by-step dry run

## Problem in one line

Given two arrays `a` and `b`, find the length of the **longest strictly increasing subsequence** that appears **in both arrays** (same relative order in each).

## Key idea (classic O(n·m) DP, 1D space)

We scan `a` left→right. For each `a[i]`, we walk `b` left→right and keep a running best called `best_len_of_smaller`:

* `best_len_of_smaller` = the **maximum LCIS length ending in a value < a[i]** among prefixes of `b`.
* When we see `b[j] < a[i]`, we can update `best_len_of_smaller = max(best_len_of_smaller, dp[j])`
  (because any LCIS ending at `b[j]` can be extended by `a[i]` later if we find `b[j]==a[i]`).
* When we see `b[j] == a[i]`, we can **extend**: `dp[j] = max(dp[j], best_len_of_smaller + 1)`.
* `dp[j]` always means: **LCIS length that ends exactly at `b[j]`**.

Answer is `max(dp)` after processing all of `a`.

### Why it works

We only extend with strictly larger values (since we update `best_len_of_smaller` using `b[j] < a[i]`), and we only count when the element appears **in both arrays** (`b[j] == a[i]`). This synchronizes order across arrays.

---

## Dry run

Example 1

```
a = [3, 4, 9, 1]
b = [5, 3, 8, 9, 10, 2, 1]
```

Initialize `dp = [0,0,0,0,0,0,0]` over `b`.

* i=0, a[i]=3:
  walk b:

  * b[0]=5 (>3) ignore
  * b[1]=3 == a[i] → dp[1] = max(dp[1], best+1) = 1  (best=0)
  * b[2]=8 (>3) ignore
  * b[3]=9 (>3) ignore
  * b[4]=10 (>3) ignore
  * b[5]=2 (<3) → best=max(best,dp[5]=0)=0
  * b[6]=1 (<3) → best=max(best,dp[6]=0)=0
    dp = [0,1,0,0,0,0,0]

* i=1, a[i]=4:
  best=0
  b[0]=5>4 ignore
  b[1]=3<4 → best=max(best,dp[1]=1)=1
  b[2]=8>4 ignore
  b[3]=9>4 ignore
  b[4]=10>4 ignore
  b[5]=2<4 → best=max(1,dp[5]=0)=1
  b[6]=1<4 → best=max(1,dp[6]=0)=1
  (no 4 in b → dp unchanged)

* i=2, a[i]=9:
  best=0
  b[0]=5<9 → best=max(0,dp[0]=0)=0
  b[1]=3<9 → best=max(0,dp[1]=1)=1
  b[2]=8<9 → best=max(1,dp[2]=0)=1
  b[3]=9==a[i] → dp[3]=max(dp[3],best+1)=max(0,2)=2
  rest are smaller but no more 9’s we need;
  dp = [0,1,0,2,0,0,0]

* i=3, a[i]=1:
  best=0
  … when we reach b[6]=1==a[i] → dp[6]=max(dp[6],best+1)=1
  final dp = [0,1,0,2,0,0,1]

Answer = `max(dp) = 2` (e.g., `[3, 9]`).

---

# 3) Python solutions (from brute → optimal)

Required signature:

```python
class Solution:
    def LCIS(self, a, b):
        # code here
```

## A) Brute-force with memo (exponential → prunes by DP; good for teaching)

```python
class Solution:
    def LCIS(self, a, b):
        """
        DFS with memo: pick next common element > last_val.
        Time:  worst-case exponential without strong pruning; with memo O(n*m) states but transitions can be heavy.
        Space: O(n*m) memo + O(n+m) recursion
        """
        from functools import lru_cache

        # Build value -> list of indices in b for quick next-position lookup
        pos = {}
        for j, x in enumerate(b):
            pos.setdefault(x, []).append(j)

        # next greater index in a sorted list (manual upper_bound)
        def next_pos(lst, after):
            # binary search for first index > after
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo + hi) // 2
                if lst[mid] <= after:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        @lru_cache(None)
        def dfs(i, j, last):  # last is the last value taken, i pos in a, j pos in b
            if i == len(a):
                return 0
            # Option 1: skip a[i]
            best = dfs(i + 1, j, last)

            val = a[i]
            if val > last and val in pos:
                lst = pos[val]
                kidx = next_pos(lst, j)
                if kidx < len(lst):
                    # we can take a[i] at b index lst[kidx]
                    best = max(best, 1 + dfs(i + 1, lst[kidx], val))
            return best

        # Start before any b index (j=-1) and last=-inf (use -1e10 sentinel)
        return dfs(0, -1, -10**18)
```

This is instructive but not the standard. Use the next one in interviews.

## B) Standard O(n·m) DP (1D space) — **recommended**

```python
class Solution:
    def LCIS(self, a, b):
        """
        dp[j] = length of LCIS that ends exactly at b[j].
        For each a[i], sweep b left->right keeping best_len_of_smaller.
        Time:  O(n*m)
        Space: O(m)
        """
        m = len(b)
        dp = [0] * m

        for x in a:                      # O(n)
            best_len_of_smaller = 0
            for j in range(m):           # O(m)
                if b[j] < x:
                    # any LCIS ending at b[j] can be extended by x later
                    if dp[j] > best_len_of_smaller:
                        best_len_of_smaller = dp[j]
                elif b[j] == x:
                    # we can end the LCIS at b[j] using x now
                    if best_len_of_smaller + 1 > dp[j]:
                        dp[j] = best_len_of_smaller + 1
        return max(dp, default=0)
```

## C) Variant with path reconstruction (return the sequence as well)

```python
class Solution:
    def LCIS(self, a, b):
        """
        Same O(n*m) idea but also reconstruct one LCIS.
        Returns (length, sequence).
        """
        m = len(b)
        dp = [0] * m
        parent = [-1] * m   # predecessor index in b for path

        for x in a:
            best_len = 0
            best_idx = -1   # track which b[j] gave that best_len
            for j in range(m):
                if b[j] < x and dp[j] > best_len:
                    best_len = dp[j]
                    best_idx = j
                elif b[j] == x and best_len + 1 > dp[j]:
                    dp[j] = best_len + 1
                    parent[j] = best_idx

        # locate best endpoint
        if not dp or max(dp) == 0:
            return 0  # or (0, [])
        end = max(range(m), key=lambda j: dp[j])
        length = dp[end]

        # rebuild sequence from parent pointers (values from b)
        seq = []
        k = end
        while k != -1:
            seq.append(b[k])
            k = parent[k]
        seq.reverse()

        # If you only need length, return length; else return (length, seq)
        return length  # or: return (length, seq)
```

---

# 4) Interview quick recall + Q&A

## 5-line pseudo you can memorize

```
dp[0..m-1] = 0
for x in a:
  best = 0
  for j in 0..m-1:
    if b[j] < x: best = max(best, dp[j])
    elif b[j] == x: dp[j] = max(dp[j], best + 1)
return max(dp)
```

**Mnemonic:**
**“Scan A; along B keep ‘best so far below X’; when equal → extend.”**
(“Below X” guarantees strictly increasing; “equal” guarantees common element.)

### Likely interviewer questions

**Q1. Why does this guarantee increasing?**
We only extend with `x` using LCIS that ends at `b[j] < x`, enforced by the `b[j] < x` condition when building `best`. So the last value is strictly smaller than `x`.

**Q2. What does `dp[j]` represent?**
LCIS **length that ends exactly at `b[j]`**. This makes the transition natural when we meet `b[j] == x`.

**Q3. Complexity?**
`O(n·m)` time, `O(m)` space. This meets the expected constraints (`n,m ≤ 10^3`).

**Q4. How to output the sequence, not just length?**
Maintain `parent[j]` the predecessor index in `b` used to form `dp[j]` (see version C). Reconstruct by following parent links from the best `j`.

**Q5. Does order of scanning matter?**
Yes. We must sweep `b` **left→right** for each fixed `a[i]` to respect the order in `b` and correctly accumulate `best` from earlier positions only.

**Q6. What about duplicates?**
Handled naturally: multiple positions `j` with `b[j] == x` may update `dp[j]` using possibly different `best` values; the best consistent chain survives.

---

---

awesome — here are the last two pieces for **LCIS (Longest Common Increasing Subsequence)**.

---

## 5) Real-World Use Cases (short & relatable)

* **Event streams reconciliation:** Find the longest **increasing** sequence of common timestamps/IDs across two services’ logs to align consistent activity (shared order + monotonic time).
* **Versioned datasets merge:** Two partners keep numbers as codes that only **increase** (e.g., build numbers). LCIS gives the longest span where both had the same rising releases.
* **Sensor fusion:** Two sensors report discretized, increasing readings (e.g., altitude steps). LCIS extracts the longest **agreement** segment that rises consistently.
* **Student progress comparison:** Two learners’ module IDs completed over time (IDs increase as difficulty rises). LCIS finds the longest common increasing learning path.

Each maps perfectly to: “same items appear in both sequences, and values must strictly increase.”

---

## 6) Full Python Program (timed + complexity notes inline)

```python
"""
LCIS — Longest Common Increasing Subsequence
--------------------------------------------
Goal: length of the longest *strictly increasing* subsequence that appears
in both arrays a and b (same relative order).

Standard O(n*m) DP with O(m) space:
  - dp[j] = length of LCIS that ends exactly at b[j]
  - For each a[i], sweep b left→right:
        best = max dp[j] over b[j] < a[i]   # LCIS that can be extended by a[i]
        if b[j] == a[i]: dp[j] = max(dp[j], best + 1)

Complexities:
  - Outer loop over a: O(n)
  - Inner loop over b: O(m)
  => Time:  O(n*m)
  => Space: O(m)
"""

import timeit
from typing import List, Tuple

class Solution:
    def LCIS(self, a: List[int], b: List[int]) -> int:
        """
        Time per call:
          - Init dp: O(m)
          - Two nested loops: O(n*m)
        Space per call:
          - dp: O(m)
        """
        m = len(b)
        dp = [0] * m  # O(m) space

        for x in a:                   # O(n) iterations
            best_len_of_smaller = 0   # best LCIS seen so far with last value < x
            for j in range(m):        # O(m) per a-element
                if b[j] < x:
                    # update 'best' candidate we could extend with x
                    if dp[j] > best_len_of_smaller:
                        best_len_of_smaller = dp[j]
                elif b[j] == x:
                    # extend LCIS ending at a smaller value with x==b[j]
                    if best_len_of_smaller + 1 > dp[j]:
                        dp[j] = best_len_of_smaller + 1
                # if b[j] > x: nothing to do
        return max(dp, default=0)


# -------- Optional helper to also reconstruct one LCIS (still O(n*m), O(m) space) --------
def lcis_with_sequence(a: List[int], b: List[int]) -> Tuple[int, List[int]]:
    m = len(b)
    dp = [0] * m                # length of LCIS ending at b[j]
    parent = [-1] * m           # predecessor index in b for reconstruction

    for x in a:
        best_len = 0
        best_idx = -1
        for j in range(m):
            if b[j] < x and dp[j] > best_len:
                best_len = dp[j]
                best_idx = j
            elif b[j] == x and best_len + 1 > dp[j]:
                dp[j] = best_len + 1
                parent[j] = best_idx

    if not dp or max(dp) == 0:
        return 0, []

    end = max(range(m), key=lambda j: dp[j])
    length = dp[end]
    seq = []
    k = end
    while k != -1:
        seq.append(b[k])
        k = parent[k]
    seq.reverse()
    return length, seq


# --------------------------------- Demo + Timing ---------------------------------
if __name__ == "__main__":
    tests = [
        # (a, b, expected_len)
        ([3, 4, 9, 1], [5, 3, 8, 9, 10, 2, 1], 2),      # [3,9]
        ([1, 1, 4, 3], [1, 1, 3, 4], 2),                # [1,3] or [1,4]
        ([2, 2, 2], [2, 2], 1),                          # single '2'
        ([1, 2, 3], [3, 2, 1], 1),                      # only singles match in order
        ([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5),  # whole a
    ]

    sol = Solution()
    print("LCIS length (O(n*m) time, O(m) space)\n")
    for a, b, exp in tests:
        elapsed = timeit.timeit(lambda: sol.LCIS(a, b), number=1)
        ans = sol.LCIS(a, b)
        length, seq = lcis_with_sequence(a, b)
        print(f"a={a},\n b={b}\n -> length={ans} (expected {exp}), "
              f"one LCIS={seq}, time={elapsed:.6f}s\n")
```

### What a run looks like

```
LCIS length (O(n*m) time, O(m) space)

a=[3, 4, 9, 1],
 b=[5, 3, 8, 9, 10, 2, 1]
 -> length=2 (expected 2), one LCIS=[3, 9], time=0.0000xxs

a=[1, 1, 4, 3],
 b=[1, 1, 3, 4]
 -> length=2 (expected 2), one LCIS=[1, 3], time=0.0000xxs
...
```

**Interview recap to say out loud**

* Define `dp[j]` = LCIS length **ending at `b[j]`**.
* For each `a[i]=x`, sweep `b` left→right, keep `best` = max `dp[j]` where `b[j] < x`.
* When `b[j] == x`, update `dp[j] = max(dp[j], best + 1)`.
* Answer is `max(dp)`.
* **Time** `O(n·m)`, **space** `O(m)`.
