Here’s the **full README-style conversion** of the image (no details omitted):

---

# 🔁 Minimum Swaps and K Together

**Difficulty:** Medium
**Accuracy:** 26.0%
**Submissions:** 139K+
**Points:** 4

---

## 📘 Problem Statement

Given an array `arr` and a number `k`. One can apply a swap operation on the array any number of times, i.e., choose any two indices `i` and `j (i < j)` and swap `arr[i]`, `arr[j]`.

Find the **minimum number of swaps required** to bring all the numbers **less than or equal to `k`** together, i.e., make them a contiguous subarray.

---

## 💡 Examples

### Example 1

**Input:**
`arr[] = [2, 1, 5, 6, 3], k = 3`

**Output:**
`1`

**Explanation:**
To bring elements `2, 1, 3` together, swap index `2` with `4` (0-based indexing), i.e., element `arr[2] = 5` with `arr[4] = 3` such that the final array will be:
`arr[] = [2, 1, 3, 6, 5]`.

---

### Example 2

**Input:**
`arr[] = [2, 7, 9, 5, 8, 7, 4], k = 6`

**Output:**
`2`

**Explanation:**
To bring elements `2, 5, 4` together, swap index `0` with `2` (0-based indexing) and index `4` with `6` such that the final array will be:
`arr[] = [9, 7, 2, 5, 4, 7, 8]`.

---

### Example 3

**Input:**
`arr[] = [2, 4, 5, 3, 6, 1, 8], k = 6`

**Output:**
`0`

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10^6  
1 ≤ arr[i] ≤ 10^6  
1 ≤ k ≤ 10^6
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Arrays
* Data Structures
* Prefix Sum
* Sliding Window

---

## 📚 Related Articles

* [*Minimum Swaps Required to Bring Elements Less than or Equal to K Together*](https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/)

---

---

awesome — let’s make **“Minimum swaps to bring all elements ≤ k together”** interview-ready.

---

# 2) Concept + step-by-step dry run

## Core idea (why a sliding window works)

* Suppose there are `good` elements = count of numbers `≤ k` in `arr`.
  If we want all good elements to be **contiguous**, the final block must have **length = good**.
* For any window of length `good`, the number of **bad** elements (`> k`) inside it is exactly the number of **misplaced** items we’d need to swap out.
  (Each swap can put one bad out and bring one good in.)
* Therefore, the **minimum swaps** equals the **minimum number of bad elements** among all windows of length `good`.

This yields a clean **O(n)** sliding-window solution.

### Dry run

`arr = [2, 1, 5, 6, 3],  k = 3`

* `good = count(≤3) = 3`  (numbers: 2,1,3)
* Check windows of length 3:

| window (idx) | contents | bad (>3) |
| ------------ | -------- | -------- |
| 0..2         | [2,1,5]  | 1        |
| 1..3         | [1,5,6]  | 2        |
| 2..4         | [5,6,3]  | 2        |

Minimum bad = **1** ⇒ **1 swap** needed (matches example).

Another: `arr = [2,7,9,5,8,7,4], k=6`

* `good = 3` (2,5,4)
* Bad counts over windows of size 3:
  `[2,7,9]→2, [7,9,5]→2, [9,5,8]→2, [5,8,7]→3, [8,7,4]→2`
* Minimum = **2** ⇒ **2 swaps**.

Edge cases:

* If `good == 0` or `good == 1` → answer is `0`.
* If all elements already `≤k` → answer `0`.

---

# 3) Python — optimized & brute, with interview-style comments

## A) Optimized O(n) sliding window (most expected)

```python
# User function Template for python3
class Solution:
    def minSwap(self, arr, k):
        """
        Minimum swaps to group all elements <= k into a contiguous subarray.
        Idea: Let 'good' be count of elements <= k.
              Slide a window of length 'good'; in each window count how many 'bad' (>k).
              The minimum 'bad' over all windows equals the minimum swaps required.
        Time  : O(n)
        Space : O(1)
        """
        n = len(arr)
        # 1) Count how many elements are <= k (these should end up together)
        good = sum(1 for x in arr if x <= k)
        if good <= 1:
            return 0  # nothing to group or single item

        # 2) Count bad (>k) in the first window of size 'good'
        bad = sum(1 for i in range(good) if arr[i] > k)
        min_swaps = bad

        # 3) Slide the window across the array; update 'bad' in O(1)
        left = 0
        for right in range(good, n):
            # include new element at 'right'
            if arr[right] > k:
                bad += 1
            # exclude old element at 'left'
            if arr[left] > k:
                bad -= 1
            left += 1
            # track the minimum bad seen
            if bad < min_swaps:
                min_swaps = bad

        return min_swaps
```

## B) Brute force O(n²) (for understanding, not preferred)

For each starting index, count bads inside the length-`good` window anew.

```python
class SolutionBrute:
    def minSwap(self, arr, k):
        """
        Naive: For every window of size 'good', recount bads.
        Time  : O(n^2)
        Space : O(1)
        """
        n = len(arr)
        good = sum(1 for x in arr if x <= k)
        if good <= 1:
            return 0
        min_swaps = float('inf')
        for start in range(0, n - good + 1):
            bad = 0
            for i in range(start, start + good):
                if arr[i] > k:
                    bad += 1
            min_swaps = min(min_swaps, bad)
        return 0 if min_swaps == float('inf') else min_swaps
```

---

# 4) Interview quick-recall + expected Q&A

## 10-second memory hook

* **Mantra:** “**Window size = #≤k; answer = min bads in any such window**.”
* **Skeleton in words:** count `good` → first window’s `bad` → slide, update `bad` in O(1) → min.

## Likely follow-ups (crisp answers)

**Q1. Why does the min bads equal min swaps?**
Each swap can move **one bad out** of the target window and **one good in**. So the least changes needed equals the number of bads currently inside the best window.

**Q2. Complexity?**
Optimized: **O(n)** time (one pass after counting), **O(1)** extra space.

**Q3. What if elements can be negative or arbitrary?**
Doesn’t matter — the rule is based on `≤ k`, not value sign. Sliding window is over positions, not sums.

**Q4. Do we actually perform swaps?**
No, we only count the minimum required; we don’t need to output a sequence.

**Q5. Edge cases?**

* `good` in `{0,1}` → `0`.
* All elements `≤ k` → `0`.
* `k` smaller than every element → `0` (since `good=0`).

**Q6. Can we adapt to “bring all elements **< k** together”?**
Yes — just change predicate to `< k` when counting good/bad.

---

## Tiny “5 lines” you can say before coding

```
good = count(x<=k)
bad = count(arr[0:good] where x>k)
ans = bad
for r in good..n-1:
    bad += (arr[r]>k) - (arr[r-good]>k)
    ans = min(ans, bad)
return ans
```

That’s the whole algorithm you can rebuild in **under 30 seconds** in any language.

---

---

## 5) Real-World Use Cases (short, interview-friendly)

* **Cache/layout compaction:** move all “hot” items (score ≤ k ms latency, or size ≤ k KB) together in memory to improve cache locality; count the *minimum* relocations.
* **Ticket/queue triage:** group low-severity tickets (priority ≤ k) into one contiguous board lane with minimum moves.
* **Network QoS batching:** batch packets whose size ≤ k into the same frame/window with minimal reshuffles.
* **Warehouse picking:** cluster small/light items (weight ≤ k) into one zone with the fewest swaps of bin positions.

All map directly to: *count “good” (≤ k), slide a window of that size, minimize “bad” (> k) inside it → that count equals minimum swaps.*

---

## 6) Full Python Program

* Optimized **O(n)** sliding window (most expected).
* Brute-force **O(n²)** (for comparison).
* Demo on the sample cases + timing with `timeit`.

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# Optimized solution: sliding window (most expected in interviews)
# ------------------------------------------------------------
class Solution:
    def minSwap(self, arr, k):
        """
        Minimum swaps to bring all elements <= k together.
        Idea:
          - Let 'good' = count(x <= k).
          - Over every window of length 'good', the number of elements > k
            equals how many are misplaced. The minimum such count is the answer.
        Complexity:
          - Counting 'good':     O(n)
          - First window 'bad':  O(good) <= O(n)
          - Slide windows:       O(n) total (O(1) update)
          => Time  O(n), Space O(1)
        """
        n = len(arr)
        good = sum(1 for x in arr if x <= k)     # O(n)
        if good <= 1:
            return 0  # already grouped or nothing to group

        # Count 'bad' (>k) in the first window of size 'good' -- O(good)
        bad = sum(1 for i in range(good) if arr[i] > k)
        min_swaps = bad

        # Slide the window across the array; each step is O(1)
        left = 0
        for right in range(good, n):
            if arr[right] > k:   # entering element
                bad += 1
            if arr[left] > k:    # leaving element
                bad -= 1
            left += 1
            if bad < min_swaps:
                min_swaps = bad

        return min_swaps


# ------------------------------------------------------------
# Brute-force baseline: O(n^2)
# ------------------------------------------------------------
class SolutionBrute:
    def minSwap(self, arr, k):
        """
        For each window of size 'good', recount bad (>k) from scratch.
        Time:  O(n^2) worst case, Space: O(1)
        """
        n = len(arr)
        good = sum(1 for x in arr if x <= k)
        if good <= 1:
            return 0
        ans = float("inf")
        for start in range(0, n - good + 1):
            bad = 0
            for i in range(start, start + good):
                if arr[i] > k:
                    bad += 1
            if bad < ans:
                ans = bad
        return 0 if ans == float("inf") else ans


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Minimum Swaps and K Together ===\n")

    samples = [
        # (name, arr, k, expected)
        ("Ex1", [2, 1, 5, 6, 3], 3, 1),
        ("Ex2", [2, 7, 9, 5, 8, 7, 4], 6, 2),
        ("Ex3", [2, 4, 5, 3, 6, 1, 8], 6, 0),
        ("AllGood", [1, 2, 2, 3], 3, 0),
        ("NoneGood", [7, 8, 9], 3, 0),
    ]

    fast = Solution()
    slow = SolutionBrute()

    for name, arr, k, expected in samples:
        res_fast = fast.minSwap(arr[:], k)
        res_slow = slow.minSwap(arr[:], k)
        print(f"{name}: arr={arr}, k={k}")
        print(f"  Optimized O(n) : {res_fast}")
        print(f"  Brute O(n^2)   : {res_slow}")
        print(f"  Expected       : {expected}")
        print(f"  Match?         : {res_fast == res_slow == expected}\n")

    # --------- Timing on a larger array ---------
    seed(17)
    n = 400_000
    k = 500_000
    big = [randint(1, 1_000_000) for _ in range(n)]

    t_fast = timeit(lambda: Solution().minSwap(big, k), number=3)
    # Brute is far too slow for n=400k; show scale on a small slice
    small = big[:3000]
    t_slow = timeit(lambda: SolutionBrute().minSwap(small, k), number=1)

    print("=== Timing (seconds) ===")
    print(f"Optimized O(n)   on n={n}, runs=3: total {t_fast:.4f}s | avg {(t_fast/3):.4f}s/run")
    print(f"Brute O(n^2)     on n={len(small)}, run=1: {t_slow:.4f}s")


if __name__ == "__main__":
    run_demo()
```

**What you’ll see when you run it**

* For every sample, both methods return the same number of swaps and `Match? True`.
* The timing section shows the linear sliding-window scales smoothly, while brute is only viable on tiny arrays.

---

### 10-second recall line (before coding)

> **“Window size = #≤k; answer = min count of >k inside any such window ⇒ O(n) sliding window.”**
