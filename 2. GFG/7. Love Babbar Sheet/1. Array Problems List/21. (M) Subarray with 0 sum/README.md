
---

# 🔍 Subarray with 0 Sum

**Difficulty:** Medium
**Accuracy:** 39.79%
**Submissions:** 306K+
**Points:** 4
**Average Time:** 20m

---

## 📘 Problem Statement

Given an array of integers, `arr[]`.
Find if there is a **subarray** (of size at least one) with **0 sum**.
Return **true/false** depending upon whether there is a subarray present with 0-sum or not.

---

## 💡 Examples

### Example 1

**Input:**
`arr[] = [4, 2, -3, 1, 6]`

**Output:**
`true`

**Explanation:**
`2, -3, 1` is the subarray with a sum of 0.

---

### Example 2

**Input:**
`arr[] = [4, 2, 0, 1, 6]`

**Output:**
`true`

**Explanation:**
`0` is one of the elements in the array, so there exists a subarray with sum 0.

---

### Example 3

**Input:**
`arr[] = [1, 2, -1]`

**Output:**
`false`

---

## ⚙️ Constraints

```
1 <= arr.size <= 10^4  
-10^5 <= arr[i] <= 10^5  
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

* Paytm
* Adobe

---

## 🏷️ Topic Tags

* Sliding Window
* Hash
* Map
* STL
* Data Structures
* Algorithms

---

## 💬 Related Interview Experiences

* One97 Interview Experience Set 3 (Backend Node.js Developer)
* Adobe Interview Experience for Member of Technical Staff 2

---

## 📚 Related Articles

* [Find If There Is A Subarray With 0 Sum](https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/)

---

---
awesome—here’s an interview-ready pack for **“Subarray with 0 Sum”** in your requested format.

---

# 2) Explanation + step-by-step dry run

## Core idea

Let `pref[i] = arr[0] + arr[1] + ... + arr[i]` (prefix sum).

A subarray `arr[l..r]` has sum **0** iff either:

* `pref[r] == 0` (the subarray starts at index 0), or
* **some prefix value repeats**: `pref[r] == pref[l-1]`.
  The difference of equal prefixes is zero ⇒ the in-between subarray sums to 0.

So we just scan once, keep a **set of seen prefix sums**.
At each step:

* Add current value to `running_sum`.
* If `running_sum == 0` or already in `seen`, return **True**.
* Else add `running_sum` to `seen` and continue.

Time O(n), space O(n).

## Dry run on `arr = [4, 2, -3, 1, 6]`

* start: `seen = {}` , `running_sum = 0`
* i=0, x=4 → `running_sum=4` (not 0, not in set) → add to set → `seen={4}`
* i=1, x=2 → `running_sum=6` (not 0, not in set) → add → `seen={4,6}`
* i=2, x=-3 → `running_sum=3` → add → `seen={4,6,3}`
* i=3, x=1 → `running_sum=4` → **4 is already in `seen`** ⇒ subarray `(i_seen+1..3)` = indices `1..3` → values `[2, -3, 1]` sum to 0 → return **True** ✅

Edge examples:

* `[4, 2, 0, 1, 6]` → the moment you see `0`, running_sum becomes 0 for that element itself ⇒ **True**.
* `[1, 2, -1]` → running sums `1, 3, 2` all unique and none is 0 ⇒ **False**.

---

# 3) Python solutions (brute + optimized), with inline comments

## A) Optimized (hash-set on prefix sums) — most expected

```python
# User function Template for python3
class Solution:
    
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr):
        """
        Use prefix sums: if any prefix repeats or becomes zero -> zero-sum subarray exists.
        Time:  O(n)    -- single pass
        Space: O(n)    -- set of seen prefix sums
        """
        seen_prefix = set()    # stores prefix sums we've seen so far
        running_sum = 0

        for x in arr:          # O(n)
            running_sum += x   # update prefix

            # Case 1: subarray from 0..i has sum 0
            # Case 2: some earlier prefix equals this prefix -> in-between sum 0
            if running_sum == 0 or running_sum in seen_prefix:
                return True

            seen_prefix.add(running_sum)  # remember this prefix for later

        return False  # no zero-sum subarray found
```

### (Optional) Variant with first/last indices (handy in follow-ups)

```python
def zero_sum_indices(arr):
    """
    Returns one zero-sum subarray's (start, end) indices or None.
    Time: O(n), Space: O(n)
    """
    prefix_to_index = {0: -1}  # handles subarray starting at index 0
    s = 0
    for i, x in enumerate(arr):
        s += x
        if s in prefix_to_index:
            return (prefix_to_index[s] + 1, i)
        prefix_to_index[s] = i
    return None
```

## B) Brute force (educational; not for large n)

```python
class SolutionBrute:
    def subArrayExists(self, arr):
        """
        Try all subarrays and compute sums incrementally.
        Time:  O(n^2)  -- two loops
        Space: O(1)
        """
        n = len(arr)
        for start in range(n):
            cur_sum = 0
            for end in range(start, n):
                cur_sum += arr[end]
                if cur_sum == 0:   # found zero-sum subarray
                    return True
        return False
```

Why not sliding window? Because numbers can be **negative**; expanding/contracting does not strictly increase/decrease the sum, so sliding window guarantees do not hold.

---

# 4) Interview quick-recall + expected Q&A

## 10-second memory hook

* **Mantra:** “**Prefix repeats ⇒ zero in between.**”
* **Skeleton:**
  `sum=0; seen=set(); for x in arr: sum+=x; if sum==0 or sum in seen: return True; seen.add(sum); return False`
* **Complexity:** O(n) time, O(n) space.

## Likely follow-ups (with crisp answers)

**Q1. Why does a repeated prefix imply a zero-sum subarray?**
If `pref[i] == pref[j] (i<j)`, then `arr[i+1..j] = pref[j] - pref[i] = 0`.

**Q2. Do we need to treat the element `0` specially?**
Not separately; when you add `0`, `running_sum` may become 0 at that index and you return **True**.

**Q3. Why not sliding window?**
It works for non-negative arrays. With negatives, sum behavior isn’t monotonic; the window cannot be adjusted greedily.

**Q4. Space optimization?**
You can’t beat O(n) extra in worst case if you need a one-pass solution. Sorting prefixes to find duplicates would be O(n log n) time and O(n) space anyway.

**Q5. How to return the actual subarray indices?**
Map prefix sum → first index seen (initialize `{0: -1}`), and when you see the same prefix again at `j`, return `(first+1, j)`.

**Q6. Edge cases?**
Empty array (not present here), arrays with all positives (only zero if there’s a 0), arrays with many duplicates or large values (use Python int; in fixed-width languages watch for overflow).

---

---

awesome—wrapping up **Subarray with 0 Sum** with the last two pieces you asked for.

---

# 5) Real-World Use Cases (short + interview-friendly)

* **Ledger/Accounting Reconciliation:** detect transactions that net to zero within a range (credits + debits cancel out). A zero-sum subarray flags a fully offset segment.
* **Network/Server Logs Matching:** bursts of requests (+1) and corresponding completions (−1) should cancel within time windows; a zero-sum segment means “all matched.”
* **Inventory/Undo Streams:** operations like add (+q) and remove (−q); a zero-sum subarray shows a block that leaves stock unchanged.
* **Financial PnL Sanity Check:** signed trade PnL deltas summing to zero over a period indicates all gains/losses netted out (useful for debugging pipelines).

These map directly to “prefix differences repeat ⇒ the in-between net is zero.”

---

# 6) Full Python Program (optimized + brute)

Includes:

* The **optimized O(n) set-of-prefix-sums** method (most expected).
* A **brute O(n²)** variant for contrast.
* Sample inputs with printed outputs.
* `timeit` to measure runtime on a larger random array.

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# User function Template for python3 (Optimized solution)
# ------------------------------------------------------------
class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr):
        """
        Logic:
          Maintain running prefix sum S. If S becomes 0 or repeats, there exists
          a subarray with sum 0 (difference of equal prefixes).
        Complexity (step-by-step):
          - Initialize set (O(1) space)
          - Single pass over array: O(n) time
          - Each set lookup/insert: expected O(1)
          Overall: Time O(n), Space O(n)
        """
        seen_prefix = set()      # O(n) worst-case space (holds unique prefixes)
        running_sum = 0          # O(1) space

        for value in arr:        # O(n) iterations
            running_sum += value # O(1) update

            # If a prefix is 0 or repeats, a zero-sum subarray exists.
            #   running_sum == 0      -> subarray [0..i]
            #   running_sum in set    -> subarray (prev_index+1 .. i)
            if running_sum == 0 or running_sum in seen_prefix:  # O(1) expected
                return True

            seen_prefix.add(running_sum)  # O(1) expected

        return False  # No zero-sum subarray found


# ------------------------------------------------------------
# Brute-force solution (educational baseline)
# ------------------------------------------------------------
class SolutionBrute:
    def subArrayExists(self, arr):
        """
        Try all subarrays; keep a rolling sum for each start.
        Complexity:
          - Outer loop over starts: O(n)
          - Inner loop over ends:   O(n) on average
          Overall: Time O(n^2), Space O(1)
        """
        n = len(arr)
        for start in range(n):       # O(n)
            s = 0
            for end in range(start, n):  # O(n) per start
                s += arr[end]        # O(1)
                if s == 0:
                    return True
        return False


# ------------------------------------------------------------
# Optional helper: return indices of one zero-sum subarray (if needed)
# ------------------------------------------------------------
def zero_sum_indices(arr):
    """
    Returns (l, r) indices for one zero-sum subarray or None.
    Complexity: Time O(n), Space O(n)
    """
    prefix_to_index = {0: -1}  # handles subarray starting at index 0
    s = 0
    for i, x in enumerate(arr):
        s += x
        if s in prefix_to_index:
            return (prefix_to_index[s] + 1, i)
        prefix_to_index[s] = i
    return None


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Subarray with 0 Sum ===\n")

    # ---- Sample Inputs (from prompt + extras) ----
    samples = [
        ("Example 1", [4, 2, -3, 1, 6], True),
        ("Example 2", [4, 2, 0, 1, 6], True),
        ("Example 3", [1, 2, -1], False),
        ("Only Positives", [1, 2, 3, 4], False),
        ("Has Zero Alone", [5, 0, 7], True),
        ("Longer Mix", [3, -1, -2, 5, -5, 2, -2, 0, 4], True),
    ]

    fast = Solution()
    slow = SolutionBrute()

    # ---- Print results for samples ----
    for name, arr, expected in samples:
        ans_fast = fast.subArrayExists(arr)
        ans_slow = slow.subArrayExists(arr)
        seg = zero_sum_indices(arr)  # optional, may be None
        print(f"{name}:")
        print(f"  Input:    {arr}")
        print(f"  Fast O(n):   {ans_fast}")
        print(f"  Brute O(n^2):{ans_slow}")
        print(f"  One zero-sum segment indices (if any): {seg}")
        print(f"  Expected: {expected}\n")

    # ---- Timing on a larger random array ----
    seed(7)
    n = 100_000
    # Mix negatives/positives to make the problem meaningful
    big = [randint(-10_000, 10_000) for _ in range(n)]

    # Wrap calls so timeit measures only the function logic.
    t_fast = timeit(lambda: Solution().subArrayExists(big), number=5)
    # Brute-force on 100k would be too slow; time it on a small slice instead.
    small = big[:2000]
    t_slow = timeit(lambda: SolutionBrute().subArrayExists(small), number=1)

    print("=== Timing (seconds) ===")
    print(f"Optimized O(n) on n={n}, runs=5: {t_fast:.4f}s")
    print(f"Brute O(n^2) on n=2000, run=1 : {t_slow:.4f}s")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For each sample, both methods’ outputs are printed plus (optionally) one pair of indices of a zero-sum subarray if it exists.
* The timing section shows the **O(n)** solution is easily scalable; the brute force is shown on a much smaller array to avoid blow-ups.