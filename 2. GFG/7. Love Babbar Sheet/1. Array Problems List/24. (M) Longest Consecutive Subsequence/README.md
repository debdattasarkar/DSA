Here’s the **complete README-style** conversion of your uploaded image — with no details omitted 👇

---

# 🧩 Longest Consecutive Subsequence

**Difficulty:** Medium
**Accuracy:** 33.0%
**Submissions:** 377K+
**Points:** 4
**Average Time:** 25m

---

## 📘 Problem Statement

Given an array `arr[]` of non-negative integers, find the **length of the longest subsequence** such that the elements in the subsequence are **consecutive integers**.
The **consecutive numbers can be in any order**.

---

## 💡 Examples

### Example 1:

**Input:**
`arr[] = [2, 6, 1, 9, 4, 5, 3]`

**Output:**
`6`

**Explanation:**
The consecutive numbers here are `1, 2, 3, 4, 5, 6`.
These 6 numbers form the longest consecutive subsequence.

---

### Example 2:

**Input:**
`arr[] = [1, 9, 3, 10, 4, 20, 2]`

**Output:**
`4`

**Explanation:**
`1, 2, 3, 4` is the longest consecutive subsequence.

---

### Example 3:

**Input:**
`arr[] = [15, 13, 12, 14, 11, 10, 9]`

**Output:**
`7`

**Explanation:**
The longest consecutive subsequence is `9, 10, 11, 12, 13, 14, 15`,
which has a length of `7`.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10^5  
0 ≤ arr[i] ≤ 10^5
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

`Amazon`, `Microsoft`, `Walmart`

---

## 🏷️ Topic Tags

* Hash
* Data Structures

---

## 💬 Related Interview Experiences

* Walmart Labs Interview Experience Set 2 On Campus

---

## 📚 Related Articles

* [Longest Consecutive Subsequence](https://www.geeksforgeeks.org/longest-consecutive-subsequence/)

---

---
awesome—let’s make **Longest Consecutive Subsequence** interview-ready.

---

# 2) Explanation + step-by-step dry run

## Problem in one line

Given an array `arr[]` (any order, duplicates allowed), return the **length** of the longest set of **consecutive integers** that can be formed from its elements (order in array doesn’t matter).

## Key idea (most expected)

Use a **hash set** so we can test membership in O(1).
A number is the **start of a run** iff `(x-1)` is **not** present.
From every start, count upward `x, x+1, x+2, ...` while present, track the longest run.

* Time: **O(n)** (each element visited a constant number of times)
* Space: **O(n)** (the set)

### Why it works

We only expand from **starts**. Every element belongs to exactly one run and is expanded at most once.

## Dry run

`arr = [2, 6, 1, 9, 4, 5, 3]`
`S = {1,2,3,4,5,6,9}`

* x=2: `1` in S ⇒ not a start.
* x=6: `5` in S ⇒ not a start.
* x=1: `0` not in S ⇒ **start**. Count: 1,2,3,4,5,6 ⇒ length = 6 → `best=6`.
* x=9: `8` not in S ⇒ start. Count: 9 ⇒ length = 1 → `best=6`.

Answer = **6**.

Edge checks:

* `[1,9,3,10,4,20,2]` → starts at 1 → run 1..4 length 4.
* `[15,13,12,14,11,10,9]` → start 9 → run 9..15 length 7.
* Duplicates? They don’t matter; sets collapse them.

---

# 3) Python solutions (brute + optimized), with clear names & comments

### A) Optimized Hash-Set (O(n)) — **most expected**

```python
# User function Template for python3
class Solution:
    
    # arr[] : the input array
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        """
        Hash-set approach: Expand only from starts (x-1 not present).
        Time : O(n) average   (each element checked a constant number of times)
        Space: O(n)           (set of unique numbers)
        """
        if not arr:
            return 0
        
        values = set(arr)  # unique numbers; duplicates collapse
        
        best_len = 0
        for x in values:
            # Start of a consecutive run iff (x-1) is not present
            if (x - 1) not in values:
                y = x
                # Count upward while numbers are present
                while y in values:
                    y += 1
                # Run is [x, y-1] -> length:
                best_len = max(best_len, y - x)
        
        return best_len
```

---

### B) Sorting (simple & reliable) — **O(n log n)**

```python
class SolutionSort:
    def longestConsecutive(self, arr):
        """
        Sort, then scan counting streaks (skip duplicates).
        Time : O(n log n)  (sorting dominates)
        Space: O(1) or O(n) depending on sort implementation
        """
        n = len(arr)
        if n == 0:
            return 0
        
        arr.sort()
        best_len = 1
        cur_len = 1
        
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                # duplicate: ignore
                continue
            if arr[i] == arr[i - 1] + 1:
                # consecutive: extend the streak
                cur_len += 1
            else:
                # gap: reset streak
                best_len = max(best_len, cur_len)
                cur_len = 1
        
        best_len = max(best_len, cur_len)
        return best_len
```

---

### C) (Optional) Map with visited (avoids recount) — also **O(n)**

Sometimes asked as a variation: mark starts and walk once.

```python
class SolutionVisited:
    def longestConsecutive(self, arr):
        """
        Mark each unique number as unvisited; explore runs once.
        Time : O(n)
        Space: O(n)
        """
        vis = {x: False for x in set(arr)}
        best = 0
        
        for x in vis.keys():
            if not vis[x]:
                # Expand downwards to find the true start
                lo = x
                while (lo - 1) in vis and not vis[lo - 1]:
                    lo -= 1
                # Count upwards once
                length = 0
                y = lo
                while y in vis and not vis[y]:
                    vis[y] = True
                    length += 1
                    y += 1
                best = max(best, length)
        return best
```

---

# 4) Interview “fast recall” + expected Q&A

## 10-second memory hook

* **Mantra:** “**Set + Starts only.**”
* **One-liner:**
  `S=set(arr); for x in S: if x-1 not in S: grow x.. while in S; keep max.`
* **Complexity:** **O(n)** time, **O(n)** space.

## Likely follow-ups (crisp answers)

**Q1. Why check `x-1` not in set?**
That ensures `x` is the **first** element of a run; we only expand from starts so each number is counted at most once.

**Q2. What about duplicates?**
`set(arr)` removes them. Duplicates shouldn’t inflate the streak length.

**Q3. What if negatives or large numbers?**
Works the same; membership is O(1). Constraints happen to be non-negative here but algorithm is general.

**Q4. Time and space?**
Hash-set: **O(n)** time average, **O(n)** space.
Sorting: **O(n log n)** time, **O(1)/O(n)** space depending on language/implementation.

**Q5. Can we do it purely in O(1) space?**
Not in general without modifying input heavily and risking O(n log n) sorting cost or losing O(n) time.

**Q6. Edge cases?**
Empty array → 0; single value → 1; all identical → 1; already consecutive → `n`.

---

---

---

# 5) Real-World Use Cases (short, interview-friendly)

* **User/login streaks:** compute the longest consecutive-day streak for engagement or rewards (each day = integer date key).
* **Sensor uptime windows:** given timestamps (day indices) the device reported, find the longest consecutive window of healthy operation.
* **Order/Inventory reconciliation:** detect longest run of consecutive invoice IDs or SKU serials that arrived without gaps (helps find missing records).
* **Version/build numbering:** longest block of consecutive builds that passed CI to assess pipeline reliability.

Each maps directly to “presence set + longest consecutive run”.

---

# 6) Full Python Program

Includes:

* **Optimized O(n)** hash-set method (expand only from starts) — what interviewers expect.
* **Sorting O(n log n)** method for completeness.
* Sample inputs with printed **input → output**.
* `timeit` micro-benchmarks on a large random list.

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# User function Template for python3 (MOST EXPECTED IN INTERVIEWS)
# ------------------------------------------------------------
class Solution:
    # arr[] : the input array
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        """
        Hash-set 'starts-only' approach.

        Complexity notes per step:
          1) Build set of unique values: O(n) time, O(n) space.
          2) For each x in set (<= n):
               - O(1) check if (x-1) not in set  -> start of a run.
               - Count upward y=x.. while y in set:
                 Each element is touched at most once across all runs.
             Total pass: O(n).
          Overall: Time O(n), Space O(n).
        """
        if not arr:
            return 0

        values = set(arr)  # Step 1: O(n) time, O(n) space
        best_len = 0

        # Step 2: iterate unique values
        for x in values:
            # Start only from numbers that have no predecessor in the set.
            if (x - 1) not in values:  # O(1)
                y = x
                # Grow the run upward. Across all starts this is O(n) total.
                while y in values:      # O(1) membership each time
                    y += 1
                best_len = max(best_len, y - x)
        return best_len


# ------------------------------------------------------------
# Alternative: Sorting solution (simple, but O(n log n))
# ------------------------------------------------------------
class SolutionSort:
    def longestConsecutive(self, arr):
        """
        Sort then scan, skipping duplicates.

        Steps:
          - Sort: O(n log n) time.
          - Single pass to count streaks: O(n).
          Overall: O(n log n) time, O(1) extra (besides sorter).
        """
        n = len(arr)
        if n == 0:
            return 0

        arr.sort()                # O(n log n)
        best_len = 1
        cur_len = 1

        for i in range(1, n):     # O(n)
            if arr[i] == arr[i-1]:
                continue          # skip dup
            if arr[i] == arr[i-1] + 1:
                cur_len += 1      # extend streak
            else:
                best_len = max(best_len, cur_len)
                cur_len = 1       # reset streak
        best_len = max(best_len, cur_len)
        return best_len


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Longest Consecutive Subsequence ===\n")

    # ---- Sample test cases (include prompt examples) ----
    samples = [
        ("Example 1", [2, 6, 1, 9, 4, 5, 3], 6),
        ("Example 2", [1, 9, 3, 10, 4, 20, 2], 4),
        ("Example 3", [15, 13, 12, 14, 11, 10, 9], 7),
        ("All same",  [5, 5, 5, 5], 1),
        ("Empty",     [], 0),
        ("Random",    [100, 4, 200, 1, 3, 2], 4),
    ]

    opt = Solution()
    srt = SolutionSort()

    for name, arr, expected in samples:
        out_opt = opt.longestConsecutive(arr[:])
        out_srt = srt.longestConsecutive(arr[:])
        print(f"{name}:")
        print(f"  Input:     {arr}")
        print(f"  Optimized: {out_opt}")
        print(f"  Sorting:   {out_srt}")
        print(f"  Expected:  {expected}")
        print(f"  Match?     {out_opt == expected == out_srt}\n")

    # ---- Benchmark on a larger input with timeit ----
    seed(7)
    n = 200_000
    # Generate values within constraint range with duplicates
    big = [randint(0, 100_000) for _ in range(n)]

    # Wrap to isolate function work for timeit
    t_opt = timeit(lambda: Solution().longestConsecutive(big), number=3)
    t_srt = timeit(lambda: SolutionSort().longestConsecutive(big[:]), number=3)

    print("=== Timing (seconds) on n = 200,000 (3 runs each) ===")
    print(f"Optimized O(n):     total {t_opt:.4f}s  | avg/run {(t_opt/3):.4f}s")
    print(f"Sorting  O(n log n): total {t_srt:.4f}s | avg/run {(t_srt/3):.4f}s")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For each sample, both methods produce the same length and a `Match? True`.
* The timing section contrasts the **O(n)** set method against the **O(n log n)** sorting method on a large array.

