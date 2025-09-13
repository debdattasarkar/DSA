# Majority Element

**Difficulty:** Medium
**Accuracy:** 27.82%
**Submissions:** 728K+
**Points:** 4
**Average Time:** 59m

---

## Problem Statement

Given an array `arr[]`. Find the **majority element** in the array. If no majority element exists, return `-1`.

**Note:** A majority element in an array is an element that appears **strictly more than** `arr.size()/2` times in the array.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 1, 2, 1, 3, 5, 1]`
**Output:** `1`
**Explanation:** Since, `1` is present more than `7/2` times, so it is the majority element.

### Example 2

**Input:** `arr[] = [7]`
**Output:** `7`
**Explanation:** Since, `7` is single element and present more than `1/2` times, so it is the majority element.

### Example 3

**Input:** `arr[] = [2, 13]`
**Output:** `-1`
**Explanation:** Since, no element is present more than `2/2` times, so there is no majority element.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 < arr[i] < 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

`Flipkart` `Accolite` `Amazon` `Microsoft` `D-E-Shaw` `Google` `Nagarro` `Atlassian`

---

## Topic Tags

`Arrays` `Searching` `Greedy` `Data Structures` `Algorithms`

---

## Related Interview Experiences

* Amazon Interview Experience Set 187 For Sde1
* Accolite Interview Experience Set 3 On Campus
* Microsoft Interview Experience Set 86 On Campus
* Amazon Interview Experience Set 138 Sde 1
* Amazon Interview Experience Set 155 Campus
* Microsoft Interview Set 24

---

## Related Articles

* **[Majority Element](https://www.geeksforgeeks.org/majority-element/)**


---

---

Here’s a clean, interview-ready guide for the **Majority Element** problem.

---

## 2) Explanation + dry run

**Goal:** Return the element that appears **strictly more than n/2 times** in `arr`, else return `-1`.

### Why Boyer–Moore works (intuition)

* Imagine pairing one occurrence of the (unknown) majority with one occurrence of “not majority”.
* Since the majority occurs > n/2 times, after all possible pair cancellations the majority cannot be fully cancelled—its candidate is what remains.
* We still **must verify** the remaining candidate (because if no majority exists, a candidate will still emerge).

### Dry run (Boyer–Moore)

`arr = [1, 1, 2, 1, 3, 5, 1]` (n = 7)

| i | x | candidate | count | Action                         |
| - | - | --------- | ----- | ------------------------------ |
| 0 | 1 | 1         | 1     | candidate set (count was 0)    |
| 1 | 1 | 1         | 2     | same as candidate → ++         |
| 2 | 2 | 1         | 1     | different → --                 |
| 3 | 1 | 1         | 2     | same → ++                      |
| 4 | 3 | 1         | 1     | different → --                 |
| 5 | 5 | 1         | 0     | different → -- (now 0)         |
| 6 | 1 | 1         | 1     | count=0 → candidate=1, count=1 |

Candidate after pass: **1**.
Verify frequency of 1 in `arr` = 4 (> 7/2 = 3.5) → **answer = 1**.

Edge example with no majority:
`arr = [2, 13]` → candidate emerges (say 13), verification shows freq=1 (≯ n/2=1) → **-1**.

---

## 3) Optimized Python solutions (with interview-style comments)

### A) Boyer–Moore Voting + verification (O(n) time, O(1) space) — **most expected**

```python
class Solution:
    def majorityElement(self, arr):
        # ---- Phase 1: Find a candidate by cancelling different pairs ----
        candidate = None
        count = 0
        for x in arr:
            if count == 0:
                candidate = x        # pick new candidate when counter drops to zero
                count = 1
            elif x == candidate:
                count += 1           # same as candidate → reinforce
            else:
                count -= 1           # different → cancel out

        # ---- Phase 2: Verify the candidate actually is a majority ----
        if candidate is None:
            return -1
        freq = sum(1 for x in arr if x == candidate)
        return candidate if freq > len(arr) // 2 else -1
```

**Why we verify:** Boyer–Moore guarantees a *dominant* candidate if a majority exists, but when **no** majority exists it still yields some value—so we must count once to confirm.

---

### B) Hash map counting (O(n) time, O(n) space) — **brute/easy**

```python
class Solution:
    def majorityElement(self, arr):
        from collections import Counter
        counts = Counter(arr)              # O(n)
        n = len(arr)
        # get the most common item (optional) or just check all
        for val, c in counts.items():      # O(u) where u = unique elements (≤ n)
            if c > n // 2:
                return val
        return -1
```

**Pros:** Dead simple; great for correctness.
**Cons:** Extra memory; not ideal for memory-constrained/streaming settings.

---

### C) Sorting (O(n log n) time, O(1) extra space if in-place)

```python
class Solution:
    def majorityElement(self, arr):
        arr.sort()                         # O(n log n)
        n = len(arr)
        candidate = arr[n // 2]            # median position in sorted array
        # verify candidate (still required)
        # count occurrences of candidate in a single pass
        # (can do binary search range as well, but a pass is fine)
        left = 0
        while left < n and arr[left] < candidate:
            left += 1
        right = left
        while right < n and arr[right] == candidate:
            right += 1
        return candidate if (right - left) > n // 2 else -1
```

**Why median?** If an element occurs > n/2 times, it must occupy the median index after sorting.
**Still verify** because if no majority exists, the middle element isn’t guaranteed to be > n/2.

---

## Complexity summary

* **Boyer–Moore:** Time `O(n)`, Space `O(1)` (plus a verification pass `O(n)` → overall `O(n)`).
* **Hash map:** Time `O(n)`, Space `O(n)`.
* **Sorting:** Time `O(n log n)`, Space `O(1)` extra if in-place.

---

## 4) Interview Q & A

**Q1. What’s the definition of a majority element here?**
A: An element that appears **strictly more than n/2 times**.

**Q2. Can there be more than one majority element?**
A: No. Two different values both appearing > n/2 times would exceed n total.

**Q3. Why does Boyer–Moore work?**
A: Pair every non-candidate with a candidate; those pairs cancel. If a true majority exists, it cannot be fully cancelled and will remain as the final candidate. (Formal proof uses counting arguments.)

**Q4. Do we always need to verify the Boyer–Moore candidate?**
A: Yes. If no majority exists, Boyer–Moore still returns some value—verification ensures correctness.

**Q5. How would you handle a stream of numbers where you can’t store them all?**
A: Keep only the Boyer–Moore `candidate` and `count` while scanning. For verification you’d need a second pass through the stream or an external counting method.

**Q6. How to generalize to “elements occurring more than n/3 times”?**
A: Use the extended Boyer–Moore (a.k.a. Misra–Gries) approach that keeps up to two candidates and counters, then verify counts.

**Q7. What if “majority” was defined as ≥ n/2 instead of > n/2?**
A: Clarify with interviewer. In typical definitions it’s **strictly greater**. If ≥ is required, adjust the final check to `>=`.

**Q8. What about negative numbers or large values?**
A: All methods above work regardless of value range; hash maps handle arbitrary keys.

---

---

Awesome—here’s a **single, runnable Python program** that:

* Implements three solutions (Boyer–Moore, HashMap, Sorting)
* Prints answers for a couple of inputs
* **Times** each approach with `timeit` inline in `__main__`
* Has **inline comments** calling out time/space for each step

---

```python
"""
Majority Element — full program with timing and annotated complexities.

A majority element is an element that appears strictly more than n/2 times.
Return that element if it exists; otherwise return -1.
"""

from collections import Counter
import timeit
from typing import List


class Solution:
    # -------------------------
    # A) Boyer–Moore Voting + VERIFY
    # -------------------------
    def majority_boyer_moore(self, arr: List[int]) -> int:
        """
        Phase-1 (candidate search): O(n) time, O(1) extra space.
          - One pass, maintain (candidate, count). Cancels pairs of different values.
        Phase-2 (verify): O(n) time, O(1) extra space.
          - Count candidate occurrences to confirm > n/2.
        Overall: O(n) time, O(1) space.
        """
        candidate = None
        count = 0

        # ---- Phase 1: candidate search (O(n) time, O(1) space) ----
        for x in arr:
            if count == 0:
                candidate = x   # pick a new candidate
                count = 1
            elif x == candidate:
                count += 1      # reinforce same value
            else:
                count -= 1      # cancel different value

        if candidate is None:   # degenerate empty-list guard (not needed for valid inputs)
            return -1

        # ---- Phase 2: verify (O(n) time, O(1) space) ----
        freq = sum(1 for x in arr if x == candidate)  # full count of candidate
        return candidate if freq > len(arr) // 2 else -1

    # -------------------------
    # B) HashMap counting
    # -------------------------
    def majority_hashmap(self, arr: List[int]) -> int:
        """
        Build frequency map: O(n) time, O(n) space (for distinct keys).
        Scan counts to find > n//2: O(u) (u ≤ n) time, O(1) extra space.
        Overall: O(n) time, O(n) space.
        """
        counts = Counter(arr)  # O(n) time, O(n) space
        n = len(arr)
        for val, c in counts.items():  # O(u) <= O(n)
            if c > n // 2:
                return val
        return -1

    # -------------------------
    # C) Sorting-based check
    # -------------------------
    def majority_sorting(self, arr: List[int]) -> int:
        """
        Sort: O(n log n) time, O(1)–O(n) space depending on sort (CPython Timsort uses O(n) worst-case aux).
        Candidate at middle if majority exists. Verify in O(n).
        Overall: O(n log n) time, O(1)–O(n) space (implementation-dependent).
        """
        if not arr:
            return -1
        arr = arr[:]                 # copy to avoid mutating caller (O(n) time/space for the copy)
        arr.sort()                   # O(n log n)
        n = len(arr)
        candidate = arr[n // 2]      # If a majority exists, it must occupy median position
        # Verify in a single O(n) pass
        freq = sum(1 for x in arr if x == candidate)
        return candidate if freq > n // 2 else -1

    # Default façade (what most platforms expect)
    def majorityElement(self, arr: List[int]) -> int:
        # Prefer Boyer–Moore for O(1) space
        return self.majority_boyer_moore(arr)


# -------------------------
# Demo & Timings
# -------------------------
def _pretty(name: str, value: int) -> str:
    return f"{name:<20} -> {value}"

def bench(func, arr, repeats=2000) -> float:
    """
    Time a function on a *captured* array using timeit's callable form
    to avoid string setup. Returns elapsed seconds.
    - Each call: O(n) or O(n log n) depending on func.
    """
    timer = timeit.Timer(lambda: func(arr))
    return timer.timeit(number=repeats)


if __name__ == "__main__":
    sol = Solution()

    # --------- Example Inputs (from problem prompt style) ---------
    has_majority = [1, 1, 2, 1, 3, 5, 1]   # n=7, majority=1 (appears 4 times)
    no_majority  = [2, 13]                 # n=2, no majority -> -1

    # --------- Correctness prints ---------
    print("Correctness Checks")
    print(_pretty("Boyer–Moore (has)", sol.majority_boyer_moore(has_majority)))
    print(_pretty("Boyer–Moore (none)", sol.majority_boyer_moore(no_majority)))
    print(_pretty("HashMap (has)", sol.majority_hashmap(has_majority)))
    print(_pretty("HashMap (none)", sol.majority_hashmap(no_majority)))
    print(_pretty("Sorting (has)", sol.majority_sorting(has_majority)))
    print(_pretty("Sorting (none)", sol.majority_sorting(no_majority)))
    print()

    # --------- Timing (use a larger array for more stable numbers) ---------
    # Build a large test: 60% of 7s, 40% mixed others -> 7 is majority
    big_arr = [7] * 6000 + [1, 2, 3, 4] * 1000  # size = 6000 + 4000 = 10000

    # For fair comparison, use fresh copies where mutation could occur
    bm_time   = bench(sol.majority_boyer_moore, big_arr, repeats=500)
    hm_time   = bench(sol.majority_hashmap, big_arr, repeats=500)
    sort_time = bench(sol.majority_sorting, big_arr, repeats=200)  # fewer reps (n log n is slower)

    print("Timings on big_arr (n=10,000)")
    print(f"{'Boyer–Moore (O(n), O(1))':<30} {bm_time:.6f} sec (500 runs)")
    print(f"{'HashMap (O(n), O(n))':<30} {hm_time:.6f} sec (500 runs)")
    print(f"{'Sorting (O(n log n))':<30} {sort_time:.6f} sec (200 runs)")
```

### Sample Output (what you’ll see when you run it)

```
Correctness Checks
Boyer–Moore (has)    -> 1
Boyer–Moore (none)   -> -1
HashMap (has)        -> 1
HashMap (none)       -> -1
Sorting (has)        -> 1
Sorting (none)       -> -1

Timings on big_arr (n=10,000)
Boyer–Moore (O(n), O(1))       0.0xxx sec (500 runs)
HashMap (O(n), O(n))           0.0xxx sec (500 runs)
Sorting (O(n log n))           0.0xxx sec (200 runs)
```

(Exact numbers depend on your machine.)

---

## 6) Real-World Use Cases (a few important ones)

1. **Telemetry & majority vote filtering**
   In sensor fusion or distributed logging, multiple noisy readings may be recorded for the “same” event. A majority vote across replicas/sources picks the dominant value quickly with **O(1) memory** using Boyer–Moore.

2. **Network leader detection**
   In systems that snapshot process IDs or heartbeats across shards, discovering whether a single node dominates (>50%) can be done in a single pass to validate quorum or to short-circuit election logic.

3. **Clickstream sanity checks**
   When ingesting session events where a bot may flood with a particular action, checking if any action crosses the >50% threshold acts as a quick anomaly detector without holding the entire frequency map in memory.
