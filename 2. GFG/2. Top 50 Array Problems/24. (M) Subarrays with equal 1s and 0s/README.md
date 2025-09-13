# Subarrays with equal 1s and 0s

**Difficulty:** Medium
**Accuracy:** 57.47%
**Submissions:** 60K+
**Points:** 4
**Average Time:** 60m

---

## Problem

Given an array `arr[]` containing `0`s and `1`s. Count the number of subarrays having **equal number of `0`s and `1`s**.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 0, 0, 1, 0, 1, 1]`
**Output:** `8`
**Explanation:**
The index ranges for the 8 subarrays are:
`(0, 1), (2, 3), (0, 3), (3, 4), (4, 5), (2, 5), (0, 5), (1, 6)`

---

### Example 2

**Input:** `arr[] = [1, 1, 1, 1, 0]`
**Output:** `1`
**Explanation:**
The index range for the subarray is `(3, 4)`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 1`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* Arrays
* Hash
* Data Structures
* prefix-sum

---

## Related Articles

* [Count Subarrays Equal Number 1s 0s](https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/)

---

---

Here’s a clear, interview-ready guide to **“Subarrays with equal 1s and 0s.”**

---

## 2) Intuition + step-by-step dry run

**Goal:** Count subarrays with the **same number of 1s and 0s**.

### Key trick (classic):

Map every `0 → -1`.
Then a subarray has equal 1s and 0s **iff** the sum of that subarray is **0**.

So the problem reduces to: **Count subarrays whose sum is 0.**

### Prefix-sum idea:

Let `pref[i]` be the sum of the mapped array up to index `i`.
For any `l..r`, the subarray sum is `pref[r] - pref[l-1]`.
That equals `0` **iff** `pref[r] == pref[l-1]`.
Therefore, **every pair of equal prefix sums** forms a valid subarray.

We can count pairs in one pass using a hash map:

* Keep a frequency map `freq` of prefix sums seen so far.
* Initialize `freq[0] = 1` (empty prefix).
* As you scan:

  * Add current element (with `0→-1`) to a running `sum`.
  * The number of subarrays ending here with sum 0 is `freq[sum]`.
  * Add `freq[sum]` to the answer, then increment `freq[sum]`.

### Dry run on `arr = [1, 0, 0, 1, 0, 1, 1]`

After mapping: `[+1, -1, -1, +1, -1, +1, +1]`

We maintain `sum`, `freq`, `ans` (start with `freq={0:1}`, `sum=0`, `ans=0`):

| i | val | sum before→after | freq\[sum] before | add to ans | freq\[sum] after |
| - | --- | ---------------- | ----------------- | ---------- | ---------------- |
| 0 | +1  | 0→1              | 0                 | +0         | 1                |
| 1 | -1  | 1→0              | 1                 | +1         | 2                |
| 2 | -1  | 0→-1             | 0                 | +0         | 1                |
| 3 | +1  | -1→0             | 2                 | +2         | 3                |
| 4 | -1  | 0→-1             | 1                 | +1         | 2                |
| 5 | +1  | -1→0             | 3                 | +3         | 4                |
| 6 | +1  | 0→1              | 1                 | +1         | 2                |

`ans = 0+1+0+2+1+3+1 = 8` ✅

---

## 3) Python solutions (brute + optimal)

### A) Optimal — One pass with hashmap (O(n) time, O(n) space)

```python
class Solution:
    def countSubarray(self, arr):
        """
        Count subarrays with equal 1s and 0s.

        Trick: map 0 -> -1. Then we need #subarrays with sum == 0.
        Use prefix-sum + hashmap of frequencies.

        Time:  O(n)  (single pass)
        Space: O(n)  (hashmap of prefix sums)
        """
        freq = {0: 1}      # prefix sum 0 seen once (empty prefix)
        s = 0              # running prefix sum over mapped array
        ans = 0

        for x in arr:      # O(n)
            s += 1 if x == 1 else -1   # map 0->-1, 1->+1

            # if s seen k times before, k subarrays ending here have sum 0
            ans += freq.get(s, 0)

            # record the current prefix sum
            freq[s] = freq.get(s, 0) + 1

        return ans
```

### B) Brute force — Nested loops (O(n²) time, O(1) space)

```python
class SolutionBrute:
    def countSubarray(self, arr):
        """
        Check every subarray and tally if #1s == #0s
        (equivalently mapped sum == 0).

        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        ans = 0
        for i in range(n):            # O(n)
            s = 0
            for j in range(i, n):     # O(n) -> O(n^2) total
                s += 1 if arr[j] == 1 else -1
                if s == 0:
                    ans += 1
        return ans
```

---

## 4) Common Interview Q\&A

**Q1. Why does mapping `0 -> -1` work?**
Because “equal number of 1s and 0s” ⇔ “sum of (+1 for 1, -1 for 0) is 0”. Each 1 cancels a 0.

**Q2. Why does counting equal prefix sums count zero-sum subarrays?**
For any `l..r`, sum is `pref[r] - pref[l-1]`. This equals `0` iff `pref[r] == pref[l-1]`. So every pair of equal prefix sums defines a zero-sum subarray.

**Q3. Why initialize `freq[0] = 1`?**
To count subarrays that start at index `0`. If `pref[r]` becomes 0, that subarray contributes one directly.

**Q4. What are edge cases?**

* All 1s or all 0s ⇒ answer `0`.
* Alternating `1,0,1,0,...` ⇒ many subarrays; algorithm handles it.
* Large `n` (up to `10^5`) ⇒ the O(n) map solution is required.

**Q5. Can this generalize to “equal counts of two specific values a and b”?**
Yes. Map `a -> +1`, `b -> -1`, everything else -> `0` (or ignore), then count zero-sum subarrays.

**Q6. What about memory constraints?**
The hashmap stores up to `n+1` distinct prefix sums in the worst case ⇒ O(n) extra space.

---

---

Below is a **complete, runnable Python program** for **“Subarrays with equal 1s and 0s”** using the optimal prefix-sum + hashmap technique. I’ve included:

* **Inline time/space complexity comments** beside each step,
* A couple of **sample inputs & outputs**, and
* A small **timeit** harness to report how long the program run took.

> The optimal method is $O(n)$ time and $O(n)$ extra space.
> (I also include a tiny brute-force validator for small arrays only.)

```python
from typing import List
import timeit
import random

# ============================================================
# Optimal Solution: Prefix-sum + HashMap  (O(n) time, O(n) space)
# ============================================================

class Solution:
    def countSubarray(self, arr: List[int]) -> int:
        """
        Count subarrays with equal number of 1s and 0s.

        Idea:
          - Map 0 -> -1 and 1 -> +1.
          - Then we need the number of subarrays whose sum == 0.
          - Use prefix sums + a hashmap of frequencies of seen prefix sums.
            If a prefix sum 's' has been seen 'k' times before, there are
            'k' subarrays ending here with total sum 0.

        Time Complexity:  O(n)   (single pass over the array)
        Space Complexity: O(n)   (hashmap can hold up to n+1 distinct sums)
        """
        freq = {0: 1}       # O(1) space now; prefix-sum 0 seen once (empty prefix)
        s = 0               # O(1) running prefix sum
        ans = 0             # O(1) answer accumulator

        # Single pass — O(n)
        for x in arr:
            # Map step is O(1)
            s += 1 if x == 1 else -1   # convert 0->-1, 1->+1

            # Lookup current prefix sum: expected O(1) average
            ans += freq.get(s, 0)      # all previous equal sums form zero-sum subarrays

            # Update frequency: O(1) average
            freq[s] = freq.get(s, 0) + 1

        return ans


# ============================================================
# Brute Force (for tiny validation only): O(n^2) time, O(1) space
# ============================================================

class SolutionBrute:
    def countSubarray(self, arr: List[int]) -> int:
        """
        Brute force: try all subarrays and check if mapped sum is zero.

        Time Complexity:  O(n^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        ans = 0
        for i in range(n):            # O(n)
            s = 0
            for j in range(i, n):     # O(n) -> O(n^2)
                s += 1 if arr[j] == 1 else -1
                if s == 0:
                    ans += 1
        return ans


# ============================================================
# Demo / Timing Harness
# ============================================================

def run_case(name: str, arr: List[int], solver) -> None:
    """
    Run one test case, print input, output and time.

    For the optimal solver:
      - Time per call:  O(n)
      - Extra space:    O(n)
    """
    t0 = timeit.default_timer()
    ans = solver.countSubarray(arr)
    t1 = timeit.default_timer()
    print(f"{name}:")
    print("  arr:", arr)
    print("  countSubarray:", ans)
    print(f"  Elapsed: {(t1 - t0):.6f}s\n")


def main():
    print("=== Subarrays with equal 1s and 0s — Examples & Timing ===\n")

    fast = Solution()
    slow = SolutionBrute()  # for correctness checks on small inputs

    # ------------------ Examples from the prompt ------------------
    ex1 = [1, 0, 0, 1, 0, 1, 1]  # expected 8
    ex2 = [1, 1, 1, 1, 0]        # expected 1

    run_case("Example 1 (optimal)", ex1, fast)
    run_case("Example 1 (brute)",   ex1, slow)

    run_case("Example 2 (optimal)", ex2, fast)
    run_case("Example 2 (brute)",   ex2, slow)

    # ------------------ Quick random tiny validation ------------------
    def rand01(n: int) -> List[int]:
        # Random 0/1 list — O(n)
        return [random.randint(0, 1) for _ in range(n)]

    tiny = rand01(20)
    ans_fast = fast.countSubarray(tiny)
    ans_slow = slow.countSubarray(tiny)
    print("Random tiny validation:")
    print("  arr:", tiny)
    print("  optimal:", ans_fast, " brute:", ans_slow, " -> equal?", ans_fast == ans_slow, "\n")

    # ------------------ Larger performance demo (optimal only) ------------------
    # Build a bigger random input (n up to 100_000 to reflect constraints).
    n = 100_000
    big = rand01(n)

    t0 = timeit.default_timer()
    _ = fast.countSubarray(big)     # O(n)
    t1 = timeit.default_timer()
    print(f"Large input (n={n}) optimal elapsed: {(t1 - t0):.6f}s")


if __name__ == "__main__":
    program_start = timeit.default_timer()
    main()
    program_end = timeit.default_timer()
    print("\n==== TOTAL PROGRAM TIME ====")
    print(f"{(program_end - program_start):.6f}s")
```

### What you’ll see when you run it

* The program will print the two **example arrays**, their **counts**, and timing for each.
* It will do a tiny **random validation** (optimal vs brute).
* Then it runs a **large input** once using the optimal algorithm and prints the elapsed time.
* Finally, it prints the **total program time**.

---

## 6) Real-World Use Cases (the essentials)

* **Binary telemetry parity checks:** In streams of binary flags (success/failure, up/down), count segments where positives equal negatives to understand stability intervals.
* **A/B experiment balance windows:** In a 0/1 conversion log, find how many time windows are balanced (equal conversions and non-conversions).
* **Network packet analysis:** For encoded binary signals, count balanced subsegments (equal highs and lows) which can indicate synchronization or framing patterns.
* **Financial tick up/down streaks:** Convert up-ticks to 1 and down-ticks to 0, count balanced intervals to detect mean-reversion phases.

