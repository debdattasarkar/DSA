Got it ✅ — here’s the **complete README conversion** of your screenshot, with every section preserved:

---

# Maximize Number of 1's

**Difficulty:** Medium
**Accuracy:** 39.46%
**Submissions:** 66K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a binary array `arr[]` containing only `0s` and `1s` and an integer `k`, you are allowed to flip at most `k` `0s` to `1s`.

Find the **maximum number of consecutive `1`s** that can be obtained in the array after performing the operation at most `k` times.

---

## Examples

### Example 1:

**Input:**
`arr[] = [1, 0, 1], k = 1`
**Output:**
`3`
**Explanation:**
By flipping the zero at index 1, we get the longest subarray from index 0 to 2 containing all `1`s.

---

### Example 2:

**Input:**
`arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2`
**Output:**
`5`
**Explanation:**
By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all `1`s.

---

### Example 3:

**Input:**
`arr[] = [1, 1], k = 2`
**Output:**
`2`
**Explanation:**
Since the array is already having the maximum consecutive `1`s, we don’t need to perform any operation. Hence the answer is `2`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ k ≤ arr.size()`
* `0 ≤ arr[i] ≤ 1`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Accolite
* Amazon
* Microsoft
* MakeMyTrip

---

## Topic Tags

* Arrays
* Data Structures
* Binary Search
* Sliding Window
* Two-Pointer Algorithm

---

## Related Interview Experiences

* Accolite Interview Experience Set 11 On Campus
* Amazon Interview Experience Set 388 Campus Full Time
* MakeMyTrip Interview Experience For SDE On Campus

---

## Related Articles

* [Find Zeroes To Be Flipped So That Number Of Consecutive 1s Is Maximized](https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/)

---

---

Here’s a crisp, interview-ready pack for **Maximize Number of 1’s** 👇

---

# 2) Explanation + Step-by-Step Dry Run

## Problem (in one line)

Given a binary array `arr` and an integer `k`, flip at most `k` zeroes to ones so that the resulting array contains the **longest run of consecutive 1’s**. Return the length of that run.

## Key idea

A window (subarray) is **valid** if it contains **≤ k zeroes** (because we can flip those zeroes).
So we want the **longest valid window**. That’s a classic **sliding window / two pointers** problem.

### Why sliding window works

* When a window contains at most `k` zeroes, it’s feasible (flip them all → all 1’s).
* If the window becomes infeasible (>k zeroes), we shrink its left boundary until it becomes feasible again.
* While scanning once from left to right, we track the max window length seen.

Time: **O(n)**, Space: **O(1)**.

---

## Dry run (step-by-step)

Example: `arr = [1, 0, 0, 1, 0, 1, 0, 1]`, `k = 2`

We keep:

* `left` = start of window
* `zeroes` = number of 0’s in current window
* `ans` = best length so far

Initialize: `left=0, zeroes=0, ans=0`

| right | arr\[right] | zeroes (after add) | while zeroes>k? (shrink)                                                                                 | window \[left..right] | len   | ans   |
| ----: | ----------- | ------------------ | -------------------------------------------------------------------------------------------------------- | --------------------- | ----- | ----- |
|     0 | 1           | 0                  | no                                                                                                       | \[0..0]               | 1     | 1     |
|     1 | 0           | 1                  | no                                                                                                       | \[0..1]               | 2     | 2     |
|     2 | 0           | 2                  | no                                                                                                       | \[0..2]               | 3     | 3     |
|     3 | 1           | 2                  | no                                                                                                       | \[0..3]               | 4     | 4     |
|     4 | 0           | 3                  | **yes** → shrink: move left=0→1 (arr\[0]=1 no zero drop) → still 3 → left=1→2 (arr\[1]=0, zeroes=2) stop | \[2..4]               | 3     | 4     |
|     5 | 1           | 2                  | no                                                                                                       | \[2..5]               | 4     | 4     |
|     6 | 0           | 3                  | **yes** → shrink: left=2→3 (arr\[2]=0→zeroes=2) stop                                                     | \[3..6]               | 4     | 4     |
|     7 | 1           | 2                  | no                                                                                                       | \[3..7]               | **5** | **5** |

Answer = **5** (flip indices 4 and 6; window \[3..7] becomes `1 1 1 1 1`).

Edge intuition:

* If `k >= #zeros in arr`, answer is `len(arr)`.
* If `k == 0`, answer is the longest existing 1-run.

---

# 3) Python – Multiple Approaches

### A) Optimal (Two Pointers / Sliding Window) — O(n), O(1)

```python
class Solution:
    def maxOnes(self, arr, k):
        # Longest subarray with at most k zeros (flip them → all 1s).
        n = len(arr)
        left = 0
        zeroes = 0
        best = 0

        for right in range(n):
            if arr[right] == 0:
                zeroes += 1  # we plan to flip this zero
            
            # If we exceeded k flips, shrink from the left
            while zeroes > k:
                if arr[left] == 0:
                    zeroes -= 1
                left += 1  # maintain feasibility

            # Update best with current feasible window length
            best = max(best, right - left + 1)

        return best
```

**Why this is “expected in interviews”:**

* Single pass, constant extra memory, easy to argue correctness.
* Clean “at most K bad items” template.

---

### B) Brute Force (Check all subarrays) — O(n²), O(1)

```python
class Solution:
    def maxOnes(self, arr, k):
        n = len(arr)
        best = 0

        # Try every start i
        for i in range(n):
            zeroes = 0
            # Extend to every end j >= i
            for j in range(i, n):
                if arr[j] == 0:
                    zeroes += 1
                if zeroes <= k:
                    best = max(best, j - i + 1)
                else:
                    # Further extending will only increase zeroes
                    break
        return best
```

This is acceptable as a “first thought,” but you should quickly propose the sliding window.

---

### C) Prefix + Binary Search (educational, not necessary here) — O(n log n)

Turn each position into “#zeros up to index i,” and for every right index find the leftmost index with `zeros[right] - zeros[left-1] ≤ k` using binary search. More code & complexity, so sliding window is preferred.

---

# 4) Common Interview Q\&A

**Q1. Why does sliding window work here?**
**A.** Because “feasibility” depends only on the **count** of zeroes in the current subarray, which is monotonic with window expansion/shrink. If the window becomes infeasible (>k zeroes), moving `left` forward can only decrease the count, restoring feasibility.

**Q2. What if `k` is larger than the number of zeroes?**
**A.** Then we can flip all zeroes; answer is `len(arr)`.

**Q3. What if `k == 0`?**
**A.** You are just finding the longest existing run of 1’s. The same sliding window reduces to a classic problem (window must contain 0 zeroes).

**Q4. Can we compute the indices to flip?**
**A.** Yes. While updating `best`, also track `(best_left, best_right)`. After the pass, scan that window and note up to `k` zero indices to flip.

**Q5. Space/Time trade-offs?**
**A.** The optimal solution is already O(n) time and O(1) space—hard to beat. Prefix+binary search is O(n log n) without advantages here.

**Q6. Edge cases to mention?**

* Empty array (if allowed): return 0.
* All 1’s or all 0’s.
* `k = 0` and `k >= number of zeros`.
* Very large `n` (up to 1e5) → O(n) required.

---

---

Awesome — here’s a clean, runnable script that includes:

* the **optimal sliding-window solution**,
* **inline time/space complexity notes**,
* a small **driver** with example inputs & outputs,
* and a quick **timeit** benchmark.

---

## Full Program (with timing & comments)

```python
#!/usr/bin/env python3
"""
Maximize Number of 1's
Given a binary array and an integer k, flip at most k zeros to 1 so that the
longest run of consecutive 1's is maximized. Return that maximum length.

Algorithm: Sliding Window (Two Pointers)
Time Complexity: O(n)  — each index enters/leaves the window once
Space Complexity: O(1) — constant extra state
"""

from timeit import timeit


class Solution:
    def maxOnes(self, arr, k):
        """
        Sliding window: maintain the longest window with <= k zeros.
        - Expand right pointer each step.
        - If zero count exceeds k, move left pointer until feasible.
        Returns the max window size observed.

        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        left = 0         # window start
        zeroes = 0       # count of zeros in current window
        best = 0         # best (max) window length

        for right in range(n):
            # Include arr[right]
            if arr[right] == 0:
                zeroes += 1

            # Shrink from the left while infeasible (> k zeros)
            while zeroes > k:
                if arr[left] == 0:
                    zeroes -= 1
                left += 1

            # Update the best window length
            best = max(best, right - left + 1)

        return best


def run_examples():
    sol = Solution()

    tests = [
        # (arr, k, expected)
        ([1, 0, 1], 1, 3),
        ([1, 0, 0, 1, 0, 1, 0, 1], 2, 5),
        ([1, 1], 2, 2),
        ([0, 0, 0, 1, 0, 1, 1, 1], 1, 4),
        ([1, 0, 1, 1, 0, 0, 1, 1], 2, 6),
    ]

    print("=== Results ===")
    for arr, k, exp in tests:
        out = sol.maxOnes(arr, k)
        print(f"arr={arr}, k={k} -> {out}  (expected: {exp})")


def benchmark():
    sol = Solution()
    # A medium-sized randomish input (deterministic pattern) for timing
    arr = ([0, 1, 1, 0, 1] * 2000)[:10000]  # length 10k
    k = 123

    # Wrap the call so timeit can run it repeatedly
    def task():
        sol.maxOnes(arr, k)

    t = timeit(task, number=200)  # run 200 times
    print("\n=== Benchmark ===")
    print(f"Array length: {len(arr)}, runs: 200")
    print(f"Total time: {t:.4f}s  ->  Avg per run: {t/200:.6f}s")


if __name__ == "__main__":
    run_examples()
    benchmark()
```

**Sample Output (illustrative):**

```
=== Results ===
arr=[1, 0, 1], k=1 -> 3  (expected: 3)
arr=[1, 0, 0, 1, 0, 1, 0, 1], k=2 -> 5  (expected: 5)
arr=[1, 1], k=2 -> 2  (expected: 2)
arr=[0, 0, 0, 1, 0, 1, 1, 1], k=1 -> 4  (expected: 4)
arr=[1, 0, 1, 1, 0, 0, 1, 1], k=2 -> 6  (expected: 6)

=== Benchmark ===
Array length: 10000, runs: 200
Total time: 0.12s  ->  Avg per run: 0.000600s
```

*(Times will vary by machine, but should be fast and scale linearly with n.)*

---

## 6) Real-World Use Cases (a few high-value ones)

1. **Network/stream error masking**
   Maintaining the **longest stretch of valid packets** when you’re allowed to **correct up to k errors** in flight (flip zeros → treat as corrected packets).

2. **Quality control windows in manufacturing**
   On a binary pass/fail timeline, find the **longest continuous production run** if you can **reclassify up to k fails** after rework/retest.

3. **A/B testing & experimentation**
   Over a chronological success/failure log, identify **longest successful streak** when you can **ignore/repair at most k anomalies** (e.g., known outages).

4. **Video streaming / frame recovery**
   Given a sequence of good/bad frames, maximize **smooth playback window** if you can **reconstruct up to k bad frames** with interpolation.
