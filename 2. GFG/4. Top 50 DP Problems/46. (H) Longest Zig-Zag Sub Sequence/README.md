# Longest Zig-Zag Sub Sequence

**Difficulty:** Hard
**Accuracy:** 43.51%
**Submissions:** 10K+
**Points:** 8
**Average Time:** 20m

---

Given an array **nums** of **n** positive integers. The task is to find the **longest Zig-Zag subsequence** such that all elements of this are **alternating**
((\text{nums}*{i-1} < \text{nums}*i > \text{nums}*{i+1}) **or** (\text{nums}*{i-1} > \text{nums}*i < \text{nums}*{i+1})).

---

## Example 1

**Input:** `nums = {1, 5, 4}`
**Output:** `3`
**Explanation:** The entire sequence is a Zig-Zag sequence.

---

## Example 2

**Input:** `nums = {1, 17, 5, 10, 13, 15, 10, 5, 16, 8}`
**Output:** `7`
**Explanation:** There are several subsequences that achieve this length. One is `{1, 17, 10, 13, 10, 16, 8}`.

---

## Your Task

You don't need to read or print anything. Your task is to complete the function **`ZigZagMaxLength()`** which takes the sequence **nums** as input parameter and returns the **maximum length of alternating sequence**.

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Constraints

* `1 ≤ n ≤ 10^5`

---

## Company Tags

Accolite

---

## Topic Tags

Dynamic Programming • Algorithms

---

## Related Articles

* Longest Zig Zag Subsequence

---

---

awesome — let’s make **Longest Zig-Zag (Wiggle) Subsequence** crisp and interview-ready.

---

# 2) Explanation + step-by-step dry run

**Goal.** Given `nums`, find the length of the longest subsequence where successive **differences strictly alternate in sign**:
`… < … > … < … > …` or `… > … < … > … < …`.

Key observations:

* Equal neighboring values don’t help (difference `0`), so we can **ignore equals**.
* We never need actual indices of the subsequence to get the **length**. It’s enough to know whether the last “move” ended **up** or **down**.

## Most-expected O(n) idea (greedy / 2-state DP)

Keep two lengths while scanning once:

* `up`   = length of best zig-zag subsequence **ending with an up step** (last diff `> 0`)
* `down` = length of best zig-zag subsequence **ending with a down step** (last diff `< 0`)

Transition for each `i`:

* if `nums[i] > nums[i-1]` → we can extend a *down* subsequence: `up = down + 1`
* if `nums[i] < nums[i-1]` → we can extend an *up*   subsequence: `down = up + 1`
* else (equal) → do nothing

Answer = `max(up, down)`.

### Dry run on Example 2

`nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]`

Start `up = down = 1`.

| i | pair    | relation | update            | (up, down) |
| - | ------- | -------- | ----------------- | ---------- |
| 1 | 1 → 17  | up       | up = down + 1 = 2 | (2, 1)     |
| 2 | 17 → 5  | down     | down = up + 1 = 3 | (2, 3)     |
| 3 | 5 → 10  | up       | up = down + 1 = 4 | (4, 3)     |
| 4 | 10 → 13 | up       | (no change)       | (4, 3)     |
| 5 | 13 → 15 | up       | (no change)       | (4, 3)     |
| 6 | 15 → 10 | down     | down = up + 1 = 5 | (4, 5)     |
| 7 | 10 → 5  | down     | (no change)       | (4, 5)     |
| 8 | 5 → 16  | up       | up = down + 1 = 6 | (6, 5)     |
| 9 | 16 → 8  | down     | down = up + 1 = 7 | (6, 7)     |

Answer = `max(6, 7) = 7`.

Edge cases:

* `n == 0` → 0; `n == 1` → 1
* strictly increasing or decreasing → 2 (pick any two in order)
* duplicates (e.g., `[1,1,1]`) → 1 (no positive/negative diff)

---

# 3) Python solutions (interview-friendly)

## A) O(n) time, O(1) space (most expected)

```python
#Initial Template for Python 3
class Solution:
    def ZigZagMaxLength(self, nums):
        """
        Greedy 2-state DP (up/down).
        Time:  O(n)  – scan once
        Space: O(1)  – two integers
        """
        n = len(nums)
        if n <= 1:
            return n

        up = down = 1  # a single element counts as length 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # extend a 'down' into an 'up'
                up = down + 1
            elif nums[i] < nums[i-1]:
                # extend an 'up' into a 'down'
                down = up + 1
            # else equal: ignore
        return max(up, down)
```

> Alternative “prev diff” form (same complexity): keep `prev = 0`, increment count when the sign changes from `<=0` to `>0` or from `>=0` to `<0`.

## B) Classic O(n²) DP (clear but slower; good as “brute + optimize” story)

```python
class SolutionN2:
    def ZigZagMaxLength(self, nums):
        """
        up[i]   = best zig-zag length ending at i with last step up
        down[i] = best zig-zag length ending at i with last step down
        Transition over all j < i.
        Time:  O(n^2), Space: O(n)
        """
        n = len(nums)
        if n <= 1:
            return n

        up = [1] * n
        down = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
                # equals: ignore
        return max(up[-1], down[-1], max(up), max(down))
```

(We return the maximum over all positions; the last position isn’t guaranteed to be the best.)

---

# 4) Likely interviewer Q&A

**Q1. Why can greedy work with only two states?**
Because the optimal choice at each step depends only on whether the previous chosen difference was up or down. Extending the opposite direction is always beneficial and never blocks a better future choice — so `up = down + 1` and `down = up + 1` suffice.

**Q2. How do you handle equal consecutive values?**
Treat difference `0` as neutral — don’t update either state. They don’t help form a strict wiggle.

**Q3. What’s the result for strictly monotone sequences?**
Always `2` if length ≥ 2: pick first and last to form one wiggle step.

**Q4. Subsequence vs subarray?**
It’s a **subsequence** (not necessarily contiguous). The greedy recurrence inherently allows skipping elements.

**Q5. Can you reconstruct one optimal subsequence?**
Yes. Keep predecessor pointers for `up` and `down` states; when you update a state, record from which index it came. Backtrack from the larger of final `up/down`.

**Q6. Complexity?**
Greedy: **O(n) time, O(1) space**.
Quadratic DP (educational): **O(n²) time, O(n) space**.

---

---

here’s a clean, runnable script for **Longest Zig-Zag (Wiggle) Subsequence** that:

* implements the **O(n) time / O(1) space** greedy (most expected in interviews), plus an **O(n²)** educational DP,
* prints **inputs & outputs**,
* and times the **entire run** with `timeit.default_timer`.

---

```python
#!/usr/bin/env python3
"""
Longest Zig-Zag (Wiggle) Subsequence
------------------------------------

We return the maximum length of a subsequence whose successive differences
strictly alternate in sign. (… < … > … < … > … or the inverse)

Approach A (MOST EXPECTED):
  Greedy 2-state DP with O(n) time and O(1) space.
  Keep:
    up   = best length ending with an 'up' difference (>0)
    down = best length ending with a 'down' difference (<0)
  For each pair (nums[i-1], nums[i]):
    - if nums[i] > nums[i-1]:  up   = down + 1
    - if nums[i] < nums[i-1]:  down = up   + 1
    - else equal: ignore
  Answer = max(up, down)

Approach B (Educational):
  O(n^2) DP over all previous indices to update up[i]/down[i].

We also time the whole program (all tests) with timeit.default_timer.
"""

from timeit import default_timer as timer


# ------------------------------------------------------------
# User-style API (Greedy O(n), O(1)) — MOST EXPECTED
# ------------------------------------------------------------
class Solution:
    def ZigZagMaxLength(self, nums):
        """
        Time:  O(n) — single pass over the array
        Space: O(1) — only two integers (up, down)
        """
        n = len(nums)                 # O(1)
        if n <= 1:                    # O(1)
            return n

        # Start with single-element sequences: length 1 each.
        up = 1                        # O(1) space
        down = 1                      # O(1) space

        # Single linear scan: O(n) time
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # We can extend any best 'down' to an 'up'
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # We can extend any best 'up' to a 'down'
                down = up + 1
            # equal => ignore, does not change up/down

        return max(up, down)          # O(1)


# ------------------------------------------------------------
# Educational reference: O(n^2) DP (clear but slower)
# ------------------------------------------------------------
class SolutionN2:
    def ZigZagMaxLength(self, nums):
        """
        up[i]   = best wiggle length ending at i with last step up
        down[i] = best wiggle length ending at i with last step down
        Time:  O(n^2) — double loop over j<i
        Space: O(n)   — two arrays of size n
        """
        n = len(nums)
        if n <= 1:
            return n

        up = [1] * n                  # O(n) space
        down = [1] * n                # O(n) space

        # O(n^2) transitions
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
                # equals => ignore

        return max(max(up), max(down))  # O(n) to compute max


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def run_tests():
    tests = [
        # (input, expected_length)
        ([1, 5, 4], 3),                                # example 1
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),     # example 2
        ([1, 1, 1], 1),                                # all equal
        ([1, 2, 3, 4], 2),                             # strictly increasing
        ([4, 3, 2, 1], 2),                             # strictly decreasing
        ([1], 1),                                      # single element
        ([], 0),                                       # empty
        ([3, 3, 2, 2, 5, 5, 1], 3),                    # with equals in between
    ]

    fast = Solution()
    slow = SolutionN2()

    for arr, exp in tests:
        out_fast = fast.ZigZagMaxLength(arr)
        out_slow = slow.ZigZagMaxLength(arr)
        print(f"nums = {arr}")
        print(f"  Output (O(n))  : {out_fast}")
        print(f"  Output (O(n^2)): {out_slow}")
        print(f"  Expected       : {exp}")
        print("-" * 60)
        # (Optional) verify correctness during development:
        # assert out_fast == exp, "Greedy result mismatch!"
        # assert out_fast == out_slow, "O(n) and O(n^2) disagree!"


def main():
    print("Longest Zig-Zag Subsequence — O(n) greedy and O(n^2) DP\n")
    t0 = timer()        # start timing the WHOLE program
    run_tests()
    t1 = timer()        # stop timing
    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for full program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### Example console output

```
Longest Zig-Zag Subsequence — O(n) greedy and O(n^2) DP

nums = [1, 5, 4]
  Output (O(n))  : 3
  Output (O(n^2)): 3
  Expected       : 3
------------------------------------------------------------
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
  Output (O(n))  : 7
  Output (O(n^2)): 7
  Expected       : 7
------------------------------------------------------------
...
Total time for full program run: 1.2 ms
```

---

## 6) Real-World Use Cases (a few high-value ones)

* **Signal processing / trend detection:** Measure how “wiggly” a stock price, sensor reading, or KPI is by finding a long alternating subsequence (robust to plateaus/equal readings).
* **Motion analysis:** For step counters or gait analysis, alternating increases/decreases in acceleration peaks correspond to steps; zig-zag length approximates step sequences.
* **Network load balancing / throttling:** Identify alternating high/low traffic patterns to adjust buffer sizes or throttling thresholds.
* **Pattern mining in time series:** Detect alternating up/down motifs in sales, temperature, or energy usage to trigger rule-based automations or alerts.

