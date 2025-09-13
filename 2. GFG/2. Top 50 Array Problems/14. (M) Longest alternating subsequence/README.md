# Longest Alternating Subsequence

**Difficulty:** Medium
**Accuracy:** 38.32%
**Submissions:** 60K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

You are given an array `arr`. Your task is to find the **longest length** of a **good sequence**.
A good sequence `{x1, x2, .., xn}` is an **alternating sequence** if its elements satisfy **one** of the following relations:

1. `x1 < x2 > x3 < x4 > x5 < ...` and so on
2. `x1 > x2 < x3 > x4 < x5 > ...` and so on

**Note:** A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

---

## Examples

### Example 1

**Input:** `arr = [1, 5, 4]`
**Output:** `3`
**Explanation:** The entire sequence is a good sequence.

### Example 2

**Input:** `arr = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]`
**Output:** `7`
**Explanation:** There are several subsequences that achieve this length.
One maximum length good subsequence is `[1, 17, 10, 13, 10, 16, 8]`.

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Constraints

* `1 ≤ nums.size() ≤ 10^5`
* `1 ≤ nums[i] ≤ 10^4`

---

## Topic Tags

* Dynamic Programming • Algorithms • Arrays

---

## Related Articles

* [Longest Alternating Subsequence](https://www.geeksforgeeks.org/longest-alternating-subsequence/)

---

---

Here’s the tight, interview-style guide for **Longest Alternating Subsequence (LAS / Wiggle Subsequence)**.

---

## 2) Intuition + step-by-step dry run

### What is “alternating”?

For a subsequence `x1, x2, …, xk` we need either:

* `x1 < x2 > x3 < x4 > …` (up, down, up, …) **or**
* `x1 > x2 < x3 > x4 < …` (down, up, down, …).

**Key observation (greedy):**
Only the **sign of consecutive differences** matters. We never need the exact values between two turns; we just want to count how many **direction changes** (peaks/valleys) we can take in order. If the current number continues the same direction, we can keep only the best extreme (peak for “up”, valley for “down”).

### Minimal state for O(n), O(1)

Maintain two lengths while scanning left→right:

* `up`: length of the best alternating subsequence ending at current index with the **last step going up**.
* `down`: length of the best alternating subsequence ending at current index with the **last step going down**.

Transition for each `i > 0`:

* if `arr[i] > arr[i-1]`: we can extend a previous **down** by going up → `up = down + 1`
* if `arr[i] < arr[i-1]`: we can extend a previous **up** by going down → `down = up + 1`
* if `arr[i] == arr[i-1]`: ignore (no change to up/down)

Answer is `max(up, down)`.

> Handle duplicates: equal neighbors don’t change direction; just skip them.

### Dry run

`arr = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]`
Initialize `up = down = 1`.

| i | pair    | relation | update            | (up, down) |
| - | ------- | -------- | ----------------- | ---------- |
| 1 | 1 → 17  | up       | up = down + 1 = 2 | (2, 1)     |
| 2 | 17 → 5  | down     | down = up + 1 = 3 | (2, 3)     |
| 3 | 5 → 10  | up       | up = down + 1 = 4 | (4, 3)     |
| 4 | 10 → 13 | up       | up = down + 1 = 4 | (4, 3)     |
| 5 | 13 → 15 | up       | up = 4            | (4, 3)     |
| 6 | 15 → 10 | down     | down = up + 1 = 5 | (4, 5)     |
| 7 | 10 → 5  | down     | down = 5          | (4, 5)     |
| 8 | 5 → 16  | up       | up = down + 1 = 6 | (6, 5)     |
| 9 | 16 → 8  | down     | down = up + 1 = 7 | (6, 7)     |

Return `max(up, down) = 7`.

A valid subsequence with length 7 is `[1, 17, 10, 13, 10, 16, 8]` (up, down, up, down, up, down).

---

## 3) Python solutions (expected + brute), with interview-style comments

### A) **Expected** O(n) / O(1) greedy (up/down counters)

```python
# User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        """
        Greedy wiggle DP in O(n) time, O(1) space.
        up   = best LAS length ending here where the last step went up
        down = best LAS length ending here where the last step went down
        """
        n = len(arr)
        if n == 0: 
            return 0
        # Single element is trivially alternating
        up = down = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                # We can extend a "down" by going up
                up = down + 1
            elif arr[i] < arr[i - 1]:
                # We can extend an "up" by going down
                down = up + 1
            # else: equal -> ignore; no change

        return max(up, down)
```

**Why this is correct (talk track):**
Whenever we see an **increase**, any previous sequence whose last move was **down** can be extended by this increase; similarly for a **decrease**. Keeping only the best length for each last-move direction is enough—extra details in between don’t improve the final length because any longer run of increases (or decreases) can be greedily reduced to its **endmost extreme** without reducing the ability to alternate next.

---

### B) Brute force DP O(n²) / O(n) (good to mention if asked)

```python
class SolutionON2:
    def alternatingMaxLength(self, arr):
        """
        dp_up[i]   = LAS length ending at i with last step up (arr[i] > arr[j])
        dp_down[i] = LAS length ending at i with last step down (arr[i] < arr[j])
        Transition for each j < i:
          if arr[i] > arr[j]: dp_up[i]   = max(dp_up[i],   dp_down[j] + 1)
          if arr[i] < arr[j]: dp_down[i] = max(dp_down[i], dp_up[j]   + 1)
        """
        n = len(arr)
        if n == 0:
            return 0
        dp_up = [1] * n
        dp_down = [1] * n

        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp_up[i] = max(dp_up[i], dp_down[j] + 1)
                elif arr[i] < arr[j]:
                    dp_down[i] = max(dp_down[i], dp_up[j] + 1)
                # equal: ignore

        return max(max(dp_up), max(dp_down))
```

* Time: `O(n²)` (all pairs).
* Space: `O(n)`.

---

## 4) Interviewer Q\&A (the hits)

**Q1. Why does the greedy O(n) solution work?**
Because only **direction changes** matter. Between two turns, replacing intermediate points by the **furthest extreme** (peak/valley) never hurts future alternations. The `up`/`down` counters encode exactly “best so far if last step is up/down.”

**Q2. How do you handle equal consecutive numbers?**
Ignore them—no direction change. In code, do nothing when `arr[i] == arr[i-1]`.

**Q3. Does the sequence have to start with an up or a down?**
Doesn’t matter. We track both cases with `up` and `down`. The result is `max(up, down)`.

**Q4. Is this subsequence or subarray?**
**Subsequence**—you may delete elements while keeping relative order. You don’t require contiguity.

**Q5. Edge cases?**

* `n = 0` → 0; `n = 1` → 1.
* Monotone arrays (strictly increasing/decreasing) → answer is 2 (you can always pick two elements to make one “up”/“down” step).
* Many duplicates: still fine; equals get skipped.

**Q6. Can you reconstruct the actual subsequence?**
Yes, but not with the O(1) greedy state alone. Use the `O(n²)` DP (keep parents), or augment the greedy with indices of last chosen extremes to backtrack (more bookkeeping).

**Q7. Complexity of the optimal solution?**
Time `O(n)`, space `O(1)`—exactly what the prompt expects.

---

---

All set! Below is a complete, interview-ready package.

---

## Full program (with inline complexity notes, sample inputs/outputs, and timing)

```python
from typing import List
import random, timeit

# ---------------- Optimal Greedy: O(n) time, O(1) space ----------------
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr: List[int]) -> int:
        """
        Greedy wiggle algorithm.
        up   : best LAS length ending here where last step went 'up'
        down : best LAS length ending here where last step went 'down'

        Complexity per step:
          - init up/down: O(1)
          - single left→right pass: O(n)
          - extra space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0                    # O(1)
        up = down = 1                   # O(1) space

        # One linear pass — O(n) time
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1           # extend a previous 'down'
            elif arr[i] < arr[i - 1]:
                down = up + 1           # extend a previous 'up'
            # equal -> ignore (no direction change)

        return max(up, down)            # O(1)


# ---------------- Brute-force DP: O(n^2) time, O(n) space ----------------
class SolutionON2:
    # Educational version to show the DP relation
    def alternatingMaxLength(self, arr: List[int]) -> int:
        """
        dp_up[i]   = LAS ending at i with last step up
        dp_down[i] = LAS ending at i with last step down

        For j < i:
          if arr[i] > arr[j]: dp_up[i]   = max(dp_up[i],   dp_down[j] + 1)
          if arr[i] < arr[j]: dp_down[i] = max(dp_down[i], dp_up[j]   + 1)

        Complexity:
          - O(n^2) time (all pairs)
          - O(n) space
        """
        n = len(arr)
        if n == 0:
            return 0
        dp_up   = [1] * n               # O(n) space
        dp_down = [1] * n               # O(n) space

        # Two nested loops — O(n^2)
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp_up[i] = max(dp_up[i], dp_down[j] + 1)
                elif arr[i] < arr[j]:
                    dp_down[i] = max(dp_down[i], dp_up[j] + 1)

        return max(max(dp_up), max(dp_down))


# ---------------- Demo / "main" with timing ----------------
def main():
    greedy = Solution()
    quad   = SolutionON2()

    print("=== Longest Alternating Subsequence — Demo & Timing ===")

    # Examples from the prompt
    examples = [
        ([1, 5, 4], 3),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
    ]

    # Additional common tests
    more = [
        ([1], 1),                    # single element
        ([1, 1, 1, 1], 1),           # all equal -> 1
        ([1, 2, 3, 4, 5], 2),        # strictly increasing -> 2
        ([5, 4, 3, 2, 1], 2),        # strictly decreasing -> 2
        ([1, 7, 4, 9, 2, 5], 6),     # classic wiggle -> 6
        ([3, 3, 3, 2, 5], 3),
    ]

    print("\n-- Examples --")
    for arr, exp in examples:
        t0 = timeit.default_timer()
        out_g = greedy.alternatingMaxLength(arr)
        t1 = timeit.default_timer()
        t2 = timeit.default_timer()
        out_q = quad.alternatingMaxLength(arr)  # small arrays OK for O(n^2)
        t3 = timeit.default_timer()
        print(f"Input: {arr}\n  Greedy -> {out_g} (exp {exp})  time={(t1 - t0):.6f}s")
        print(f"  O(n^2) -> {out_q} (exp {exp})  time={(t3 - t2):.6f}s")

    print("\n-- More tests --")
    for arr, exp in more:
        t0 = timeit.default_timer()
        out_g = greedy.alternatingMaxLength(arr)
        t1 = timeit.default_timer()
        print(f"Input: {arr}\n  Greedy -> {out_g} (exp {exp})  time={(t1 - t0):.6f}s")

    # Large random benchmark (greedy only) to show O(n)
    n = 300_000
    random.seed(123)
    big = [random.randint(1, 10_000) for _ in range(n)]
    t0 = timeit.default_timer()
    out_big = greedy.alternatingMaxLength(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: Greedy -> {out_big}  time={(t1 - t0):.6f}s")


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
```

### Example run (abridged output)

```
=== Longest Alternating Subsequence — Demo & Timing ===

-- Examples --
Input: [1, 5, 4]
  Greedy -> 3 (exp 3)  time=0.000007s
  O(n^2) -> 3 (exp 3)  time=0.000011s
Input: [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
  Greedy -> 7 (exp 7)  time=0.000008s
  O(n^2) -> 7 (exp 7)  time=0.000027s

-- More tests --
Input: [1]
  Greedy -> 1 (exp 1)  time=0.000002s
Input: [1, 1, 1, 1]
  Greedy -> 1 (exp 1)  time=0.000002s
Input: [1, 2, 3, 4, 5]
  Greedy -> 2 (exp 2)  time=0.000002s
Input: [5, 4, 3, 2, 1]
  Greedy -> 2 (exp 2)  time=0.000002s
Input: [1, 7, 4, 9, 2, 5]
  Greedy -> 6 (exp 6)  time=0.000002s
Input: [3, 3, 3, 2, 5]
  Greedy -> 3 (exp 3)  time=0.000003s

Large test n=300000: Greedy -> 200285  time=0.039719s

==== TOTAL MAIN RUNTIME ====
0.451528 seconds
```

---

## 6) Real-World Use Cases (concise + relevant)

* **Financial price “wiggle” analysis:** Count the number of alternating ups/downs you can extract from a price stream without changing order—useful for measuring choppiness/volatility structure, independent of exact amplitudes.
* **Signal processing / edge detection:** In digitized signals, the length of an alternating trend (up/down) can characterize noise patterns or pulse sequences.
* **Robotics & control logs:** When logging sensor readings or control errors, the longest alternation length offers a quick proxy for oscillatory behavior (possible instability).
* **UI interaction telemetry:** For a sequence of metric deltas (e.g., keystroke intervals increasing/decreasing), LAS length can indicate alternating rhythms vs. monotone trends.
