

---

# 🧩 Split Array Subsequences

**Difficulty:** Medium
**Accuracy:** 52.86%
**Submissions:** 6K+
**Points:** 4

---

## 📝 Problem Statement

Given a **sorted integer array** `arr[]` and an **integer k**, determine if it is possible to split the array into one or more **consecutive subsequences** such that:

* Each subsequence consists of **consecutive integers** (each number is exactly one greater than the previous).
* Every subsequence has a **length of at least k**.

Return **true** if such a split is possible, otherwise return **false**.

---

## 🧮 Examples

### Example 1

**Input:**

```
arr[] = [2, 2, 3, 3, 4, 5], k = 2
```

**Output:**

```
true
```

**Explanation:**
The array can be split into three subsequences of length `k`:

* `[2, 3]`, `[2, 3]`, `[4, 5]`.

---

### Example 2

**Input:**

```
arr[] = [1, 1, 1, 1], k = 4
```

**Output:**

```
false
```

**Explanation:**
It is impossible to split `arr` into consecutive increasing subsequences of length 4 or more.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10⁵  
1 ≤ arr[i] ≤ 10⁵  
1 ≤ k ≤ arr.size()
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log n) |
| **Auxiliary Space** | O(n)       |

---

## 🏢 Company Tags

Amazon · Google

---

## 🧠 Topic Tags

`Priority-Queue` · `Heap` · `Data Structures`

---

## 🔗 Related Articles

* [Split Array Into Consecutive Subsequences Of Size K Or More](https://www.geeksforgeeks.org/split-array-into-consecutive-subsequences-of-size-k-or-more/)

---

---

## 2) Intuition + Step-by-Step Dry Run

### Problem recap (in my own words)

Given a **sorted** array `arr` and an integer `k`, can we partition the array into one or more subsequences such that:

* each subsequence is **consecutive** (e.g., `x, x+1, x+2, …`), and
* each subsequence has **length ≥ k**?

Return `True` if possible, else `False`.

### Key greedy insight (classic and optimal)

Process numbers left→right. For each number `x`, **prefer to extend** a subsequence that is currently waiting for `x` (this keeps existing subsequences alive).
If no subsequence needs `x`, try to **start a brand-new subsequence of length `k`** beginning at `x` by consuming `x+1, …, x+k-1`.
If you can’t extend and can’t start, the answer is `False`.

To implement this:

* `freq[x]` – how many `x` are still unused.
* `need[y]` – how many subsequences are **waiting for** `y` to be appended next (i.e., they currently end at `y-1`).

Algorithm when seeing `x`:

1. If `freq[x] == 0` → already used; continue.
2. Use one `x` (`freq[x] -= 1`).
3. If `need[x] > 0`: extend one subsequence → `need[x] -= 1`, `need[x+1] += 1`.
4. Else: try to **start** a new subsequence of length **exactly k** now (it may get **extended later**, so requirement “≥ k” is satisfied). Check `freq[x+1]..freq[x+k-1]` are all positive; if not → `False`. If yes → decrement each, and set `need[x+k] += 1` (that new subsequence will next need `x+k`).

If we finish the loop without failing, return `True`.

This is the same greedy proof idea as LeetCode 659 (“Split Array into Consecutive Subsequences”), generalized from k=3 to arbitrary **k ≥ 1**.

---

### Dry run (given example)

`arr = [2, 2, 3, 3, 4, 5], k = 2`

Initial:
`freq = {2:2, 3:2, 4:1, 5:1}`, `need = {}`

* `x=2`: `freq[2]→1`. `need[2]=0`, so try to **start** length-2 seq: check `freq[3]>0` ✔.
  Use `3`: `freq[3]→1`. Mark next need `need[4] += 1`. (We created `[2,3]` needing `4` next)
* `x=2`: `freq[2]→0`. `need[2]=0`, start length-2: check `freq[3]>0` ✔.
  Use `3`: `freq[3]→0`. `need[4] += 1` again. (Another `[2,3]` needing `4`)
* `x=3`: `freq[3]==0` → skip.
* `x=3`: skip.
* `x=4`: `freq[4]→0`. `need[4]=2` → **extend** one: `need[4]→1`, `need[5]→1`.
* `x=5`: `freq[5]→0`. `need[5]=1` → **extend**: `need[5]→0`, `need[6]→1`.

No failures → **True** (three subsequences: `[2,3]`, `[2,3]`, and one that was `[2,3]` extended with `4,5` across steps—lengths are ≥ 2).

---

## 3) Python — Optimized Greedy (O(n)) and Heap Alternative (O(n log n))

### A) ✅ Optimized Greedy (frequency + need) — **most expected in interviews**

```python
from collections import Counter, defaultdict

class Solution:
    def isPossible(self, arr, k):
        """
        Greedy:
          - freq[x]: counts of unused x
          - need[y]: how many subsequences currently need y next
        For each x in sorted arr:
          1) if possible, extend a waiting subsequence ending at x-1
          2) else, try to start a new subsequence of length k starting at x
          3) else, fail
        Time  : O(n) average (hash ops), Space : O(n)
        """
        if k <= 1:
            return True  # any singletons suffice

        freq = Counter(arr)           # counts of remaining
        need = defaultdict(int)       # how many subseqs want this next value

        for x in arr:
            if freq[x] == 0:
                continue  # already consumed

            # consume current x
            freq[x] -= 1

            # 1) prefer to extend an existing subsequence needing x
            if need[x] > 0:
                need[x] -= 1
                need[x + 1] += 1
                continue

            # 2) otherwise, try to start a new subsequence of length k at x
            can_start = True
            for nxt in range(x + 1, x + k):
                if freq[nxt] <= 0:
                    can_start = False
                    break
            if not can_start:
                return False

            # consume x+1..x+k-1 to form a new length-k chain
            for nxt in range(x + 1, x + k):
                freq[nxt] -= 1
            # this new chain now needs x+k next
            need[x + k] += 1

        return True
```

**Why this is optimal and safe:**

* Extending existing subsequences first avoids leaving them too short.
* Starting only when you can commit `k` elements ensures each new chain immediately meets the minimum length; later you may extend freely (requirement is “≥ k”, not “= k”).

---

### B) Alternative: Map of Min-Heaps by last value (O(n log n))

* Keep `heaps[last_value] = min-heap of lengths` of subsequences ending at `last_value`.
* For each `x`:

  * if there exists a heap at `x-1`, pop the **shortest** subsequence and push back with length+1 into heap at `x`.
  * else start new subsequence of length 1 at `x`.
* At the end, **verify every subsequence length ≥ k**.

```python
import heapq
from collections import defaultdict

class Solution:
    def isPossible(self, arr, k):
        """
        Heaps approach:
          heaps[v] keeps lengths of subseqs ending at v (min-heap).
          Always extend the shortest possible subsequence first.
        Time : O(n log n) due to heap ops
        Space: O(n)
        """
        if k <= 1:
            return True

        heaps = defaultdict(list)  # last_value -> min-heap of lengths

        for x in arr:  # arr must be sorted
            if heaps.get(x - 1):
                # extend the shortest subseq that ends at x-1
                length = heapq.heappop(heaps[x - 1])
                heapq.heappush(heaps[x], length + 1)
            else:
                # start a new subseq of length 1
                heapq.heappush(heaps[x], 1)

        # all subsequences formed must be length >= k
        for h in heaps.values():
            if h and h[0] < k:  # smallest in this heap
                return False
        return True
```

> This version is simpler to reason about but slightly slower. In interviews, mention it, but **prefer the greedy `freq+need`**.

---

## 4) Interview “How to remember” + Q&A

### 5-Line Pseudocode (memorize this)

```
count freq of every x
for x in arr:
    if freq[x]==0: continue
    use one x
    if need[x]>0: need[x]-=1; need[x+1]+=1   # extend
    else:
        check freq[x+1..x+k-1] > 0           # can start?
        if not: return False
        consume x+1..x+k-1; need[x+k]+=1
return True
```

**Mnemonic:** **“Count → Extend → StartK → Fail.”**
Say it as you code: **Count**, try to **Extend**, else **Start K**, otherwise **Fail**.

---

### Common questions & crisp answers

* **Q: Why must we extend first?**
  **A:** If we start new chains greedily while a chain is waiting to be extended, we risk leaving the waiting chain too short (< k). Extending first preserves feasibility.

* **Q: Why can we start with exactly k elements (not more)?**
  **A:** The requirement is **length ≥ k**. Starting with exactly k guarantees the minimum; later numbers can extend it naturally.

* **Q: What if the array isn’t sorted?**
  **A:** We must sort first: `O(n log n)`. The greedy proof relies on processing in ascending order.

* **Q: Time/space complexity of the optimal approach?**
  **A:** `O(n)` average time with hash maps; `O(n)` space for `freq`/`need`.

* **Q: Edge cases?**

  * `k <= 1` → always `True`.
  * Repeated numbers are fine; they form/extend multiple chains.
  * Long gaps (missing `x+i`) cause immediate `False` at “StartK” check.

* **Q: Difference vs. the classic k=3 problem?**
  **A:** Same greedy, but when starting a new chain, instead of consuming `x+1,x+2`, consume `x+1..x+k-1` and set `need[x+k] += 1`.

---

---

Awesome — let’s finish **Split Array Subsequences (min length ≥ k)** with crisp, relatable use cases and a complete, runnable Python program (with timing + complexity notes inline).

---

## 5) Real-World Use Cases (easy to pitch in interviews)

* **Scheduling consecutive shifts / classes:** Assign employees (numbers = days) into **consecutive-day rosters** where each roster must be at least `k` days long.
* **Seating/booking contiguous seats:** Split a sorted list of seat indices into **contiguous seat blocks** of size at least `k`.
* **Consecutive version rollouts / sprints:** Group release versions (sorted) into **consecutive sprint groups** where each sprint group must contain ≥ `k` versions.
* **Serial-number batching / QA lots:** Partition consecutive serials into **contiguous QA lots** with minimum size `k`.

These map exactly to “make consecutive subsequences, each size ≥ k”.

---

## 6) Full Program (with inline complexity notes + timing)

```python
#!/usr/bin/env python3
"""
Split Array into Consecutive Subsequences (each length >= k)
Greedy solution with freq/need maps (optimal & interview-standard).

Algorithm (Greedy):
  - freq[x]: how many x are still unused.
  - need[y]: how many subsequences are currently waiting for y next (they end at y-1).
  - For each x (in sorted order already given):
      • If freq[x]==0: continue (already consumed in a previous step).
      • Consume one x: freq[x] -= 1        # O(1)
      • Prefer EXTEND: if need[x] > 0: need[x]-=1; need[x+1]+=1    # O(1)
      • Else START: check freq[x+1..x+k-1] all > 0                 # O(k)
            - If any missing → return False
            - Else consume x+1..x+k-1 (k-1 operations) and need[x+k] += 1
  - If we finish without failing → True

Time Complexity:
  - Each element is consumed once in EXTEND or START: O(n)
  - START check scans k-1 points; HOWEVER each number is consumed a constant
    number of times overall → still O(n) total expected with hash lookups.
  - If you want the tight statement used in many editorials: O(n) average.
Space Complexity: O(n) for freq and need dicts.

Note: arr must be sorted. If not, sort first (O(n log n)).
"""

from collections import Counter, defaultdict
from time import perf_counter
import timeit
import random
from typing import List


class Solution:
    def isPossible(self, arr: List[int], k: int) -> bool:
        """
        Return True if arr can be split into one or more consecutive subsequences
        with each subsequence having length >= k, else False.

        Parameters:
            arr (List[int]): already sorted non-empty list of integers
            k   (int)     : minimum subsequence length (k >= 1)

        Returns:
            bool
        """
        # Edge: If k <= 1, any element alone is ok → always True.  O(1)
        if k <= 1:
            return True

        # freq: counts of remaining numbers; need: counts of next numbers wanted
        # Build freq in O(n) time & O(n) space
        freq = Counter(arr)
        need = defaultdict(int)

        # Process left → right (arr is sorted). Each loop is O(1) average.
        for x in arr:
            if freq[x] == 0:
                # This number already got consumed while starting/extending
                continue

            # Consume one x — O(1)
            freq[x] -= 1

            # 1) Prefer to EXTEND an existing chain waiting for x — O(1)
            if need[x] > 0:
                need[x] -= 1
                need[x + 1] += 1   # that chain now expects x+1 next
                continue

            # 2) Else, try to START a new chain of length exactly k at x
            #    We must have x+1..x+k-1 available now — O(k) check+consume
            can_start = True
            for nxt in range(x + 1, x + k):
                if freq[nxt] <= 0:
                    can_start = False
                    break
            if not can_start:
                return False

            # Consume the k-1 numbers after x to form a new chain length k
            for nxt in range(x + 1, x + k):
                freq[nxt] -= 1

            # This new chain of length k now "expects" x+k next (may extend later)
            need[x + k] += 1

        # If we never failed, all numbers could be arranged correctly
        return True


# --------------------------- Demo & Timing --------------------------- #

def run_demo():
    sol = Solution()

    tests = [
        # From the prompt
        {"arr": [2, 2, 3, 3, 4, 5], "k": 2, "expect": True},
        {"arr": [1, 1, 1, 1],       "k": 4, "expect": False},

        # Edge-ish
        {"arr": [1, 2, 3, 3, 4, 5], "k": 3, "expect": True},   # classic possible
        {"arr": [1, 2, 3, 4, 4, 5], "k": 3, "expect": False},  # not enough for 2nd chain
        {"arr": [10],               "k": 1, "expect": True},   # k = 1 always True
        {"arr": [1, 2, 3, 4, 5],    "k": 5, "expect": True},   # single chain
        {"arr": [1, 2, 4, 5],       "k": 2, "expect": True},   # [1,2], [4,5]
        {"arr": [1, 2, 4, 6],       "k": 2, "expect": False},  # cannot form both pairs
    ]

    print("=== Sample I/O ===")
    for t in tests:
        arr, k, expect = t["arr"], t["k"], t["expect"]
        start = perf_counter()
        got = sol.isPossible(arr, k)
        dur = (perf_counter() - start) * 1e6
        print(f"arr={arr}, k={k} -> {got} (expected {expect})   [{dur:.1f} µs]")
    print("-" * 60)

    # Random big test to show timing
    random.seed(7)
    n = 200_000
    # Build a multiset where consecutive runs exist with mild repetitions
    base = []
    for v in range(1, 50_001):
        cnt = 4 if v % 5 else 2      # some frequency pattern
        base.extend([v] * cnt)
        if len(base) >= n:
            break
    arr_big = base[:n]               # already sorted
    k_big = 3

    sol = Solution()
    avg_time = timeit.timeit(
        stmt="sol.isPossible(arr_big, k_big)",
        number=3,
        globals={"sol": sol, "arr_big": arr_big, "k_big": k_big}
    ) / 3.0
    print(f"Average time over 3 runs for n={len(arr_big)}: {avg_time:.3f} s")

    print("\nComplexity recap:")
    print("  Build freq/need: O(n) time, O(n) space")
    print("  Greedy loop    : O(n) average time")
    print("  Total          : O(n) average (O(n log n) if a sort were needed)")
    print("  Space          : O(n)")


if __name__ == "__main__":
    run_demo()
```

### What the sample section prints (illustrative)

```
=== Sample I/O ===
arr=[2, 2, 3, 3, 4, 5], k=2 -> True (expected True)   [… µs]
arr=[1, 1, 1, 1], k=4 -> False (expected False)       [… µs]
arr=[1, 2, 3, 3, 4, 5], k=3 -> True (expected True)   [… µs]
arr=[1, 2, 3, 4, 4, 5], k=3 -> False (expected False) [… µs]
arr=[10], k=1 -> True (expected True)                 [… µs]
arr=[1, 2, 3, 4, 5], k=5 -> True (expected True)      [… µs]
arr=[1, 2, 4, 5], k=2 -> True (expected True)         [… µs]
arr=[1, 2, 4, 6], k=2 -> False (expected False)       [… µs]
------------------------------------------------------------
Average time over 3 runs for n=200000: 0.xxx s

Complexity recap:
  Build freq/need: O(n) time, O(n) space
  Greedy loop    : O(n) average time
  Total          : O(n) average (O(n log n) if a sort were needed)
  Space          : O(n)
```

---

### One-liner to say in the interview

> “I’ll keep `freq` of unused numbers and `need` of the next numbers subsequences are waiting for. For each `x`, I **extend** a waiting subsequence if possible; otherwise I **start** a new subsequence by consuming `x+1..x+k-1`. If I can’t extend or start, return False. This greedy runs in **O(n)** average time and **O(n)** space (sorting makes it O(n log n) if needed).”

---
