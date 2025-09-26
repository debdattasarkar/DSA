# Maximum difference of zeros and ones in binary string

**Difficulty:** Medium
**Accuracy:** 53.05%
**Submissions:** 42K+
**Points:** 4

---

## Problem Statement

Given a binary string `S` consisting of `0`s and `1`s. The task is to find the **maximum difference of the number of `0`s and the number of `1`s** (i.e., `(# of 0s) – (# of 1s)`) **in any substring** of the string.

**Note:** In the case of **all `1`s`**, the answer will be **`-1`**.

---

## Examples

### Example 1

**Input:** `S = "11000010001"`
**Output:** `6`
**Explanation:** From index `2` to index `9`, there are `7` zeros and `1` one, so `#0s - #1s = 6`.

---

### Example 2

**Input:** `S = "111111"`
**Output:** `-1`
**Explanation:** `S` contains `1`s only.

---

### Example 2

**Input:** `S = "111111"`
**Output:** `-1`
**Explanation:** `S` contains `1`s only.

---

## Your Task

You do not need to read input or print anything. Complete the function **`maxSubstring()`**, which takes a string `S` as input and **returns an integer** representing the required maximum difference.

---

## Expected Complexities

* **Time Complexity:** `O(|S|)`
* **Expected Auxiliary Space:** `O(1)`

---

## Constraints

* `1 ≤ |S| ≤ 10^5`
* `S` contains `0`s and `1`s only

---

## Topic Tags

* Strings
* Dynamic Programming
* Kadane
* Data Structures
* Algorithms

---

## Related Articles

* [Maximum Difference Zeros Ones Binary String](https://www.geeksforgeeks.org/maximum-difference-zeros-ones-binary-string/)

---

---

awesome — let’s nail **Maximum difference of zeros and ones in a binary string**.

---

# 2) Explanation + step-by-step dry run

## Problem

For any substring `S[l..r]`, compute `(# of '0') - (# of '1')`. Return the **maximum** possible value over all substrings. If the string has **no '0'** (i.e., all `1`s), return **-1**.

## Key idea (Kadane’s trick)

Map each character to a numeric gain:

* `'0'` → `+1`  (helps the score)
* `'1'` → `-1`  (hurts the score)

Now our task becomes: **maximum subarray sum** on this transformed array.
Use **Kadane’s algorithm** in `O(n)` time, `O(1)` space.

If the best sum `best <= 0`, that means taking any substring never yields a positive advantage of zeros over ones ⇒ return `-1` (matches the “all 1s” note and also the general case where ones dominate everywhere).

### Dry run on `S = "11000010001"`

Transform: `1 1 0 0 0 0 1 0 0 0 1` → `-1 -1 +1 +1 +1 +1 -1 +1 +1 +1 -1`

Kadane (track `cur`=current sum, `best`=max so far):

|  i |  ch | val | cur = max(val, cur+val) |  best |
| -: | :-: | :-: | :---------------------: | :---: |
|  0 |  1  |  -1 |            -1           |   0   |
|  1 |  1  |  -1 |            -1           |   0   |
|  2 |  0  |  +1 |      1 (start here)     |   1   |
|  3 |  0  |  +1 |            2            |   2   |
|  4 |  0  |  +1 |            3            |   3   |
|  5 |  0  |  +1 |            4            |   4   |
|  6 |  1  |  -1 |            3            |   4   |
|  7 |  0  |  +1 |            4            |   4   |
|  8 |  0  |  +1 |            5            |   5   |
|  9 |  0  |  +1 |            6            |   6   |
| 10 |  1  |  -1 |            5            | **6** |

Answer = **6** (matches the statement: from index 2 to 9 there are 7 zeros and 1 one → 6).

Edge example `S="111111"` → transformed all `-1`. Kadane’s `best <= 0` ⇒ return **-1**.

---

# 3) Python solutions (optimized + alternatives)

Required signature:

```python
#User function Template for python3
class Solution:
    def maxSubstring(self, S):
        # code here
```

## ✅ Most expected: Kadane’s algorithm (O(n) time, O(1) space)

```python
#User function Template for python3
class Solution:
    def maxSubstring(self, S: str) -> int:
        """
        Map '0' -> +1, '1' -> -1 and run Kadane to get the max subarray sum.
        If the best sum <= 0 (e.g., all '1's), return -1.
        Time  : O(n)  -- one pass
        Space : O(1)  -- constant extra space
        """
        best = 0           # best sum found so far
        cur = 0            # current subarray sum

        for ch in S:
            val = 1 if ch == '0' else -1
            # Either start new at val or extend previous (Kadane)
            cur = max(val, cur + val)
            best = max(best, cur)

        return best if best > 0 else -1
```

---

## Alternative 1: Prefix-sum + min-prefix (also O(n)/O(1))

Idea: Let `pref[i]` be sum of mapped values up to `i`. For each `i`, the best substring ending at `i` is `pref[i] - min_prefix_so_far`. Track the max of that.

```python
class SolutionPrefix:
    def maxSubstring(self, S: str) -> int:
        """
        Prefix-sum method:
          best = max_i (pref[i] - min_pref_so_far_before_i)
        Time  : O(n)
        Space : O(1)
        """
        pref = 0
        min_pref = 0
        best = float('-inf')

        for ch in S:
            pref += (1 if ch == '0' else -1)
            best = max(best, pref - min_pref)
            min_pref = min(min_pref, pref)

        return best if best > 0 else -1
```

---

## Alternative 2: Brute force (educational; O(n²))

Sum for every substring using a running count; OK only for small inputs.

```python
class SolutionBrute:
    def maxSubstring(self, S: str) -> int:
        """
        Try all substrings; keep running zero/one counts.
        Time  : O(n^2)
        Space : O(1)
        """
        n = len(S)
        best = float('-inf')
        for i in range(n):
            zeros = ones = 0
            for j in range(i, n):
                if S[j] == '0': zeros += 1
                else:           ones  += 1
                best = max(best, zeros - ones)
        return best if best > 0 else -1
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why does mapping `'0'->+1`, `'1'->-1` work?**
Because `sum(mapped)` over a substring equals `(#0) - (#1)` for that substring—the exact score we want to maximize.

**Q2. Why Kadane’s algorithm?**
After mapping, the problem is exactly “maximum subarray sum”, which Kadane solves in `O(n)` with `O(1)` space by deciding at each index whether to start fresh or extend.

**Q3. Why return -1 for all `1`s? What about general negatives?**
If every character is `1`, all mapped values are `-1`, so the best subarray sum ≤ 0. The problem statement explicitly asks for `-1` in this case; the same logic extends: if best ≤ 0, it means no substring has more `0`s than `1`s, so return `-1`.

**Q4. Edge cases?**

* Single char: `"0"` → 1; `"1"` → -1.
* Very large strings (up to `1e5`) → Kadane/Prefix methods are linear and pass.
* Strings with ties (best = 0) still return `-1` as required (no advantage).

**Q5. Can we also return the indices of the optimal substring?**
Yes. While running Kadane, track where a new subarray starts when `val > cur+val`, and update `(bestL, bestR)` whenever `best` improves.

**Q6. Why not sliding window?**
Window size is not fixed; we need a variable-length subarray that maximizes a sum which may include negatives—this is exactly the maximum subarray problem, not a fixed-window problem.

---

---

here’s a **ready-to-run program** for **“Maximum difference of zeros and ones in a binary string”** that:

* reads a binary string `S` from stdin,
* solves it with **Kadane (recommended)**, **Prefix-min**, and **Brute** (guarded for tiny inputs),
* prints the **answers** and **times** them using `timeit.timeit(number=1)`,
* includes clear inline comments calling out **time/space complexity**.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Maximum difference of zeros and ones in a binary string
# Task: maximize (# of '0') - (# of '1') over all substrings.
#
# Core trick:
#   Map '0' -> +1, '1' -> -1, then find maximum subarray sum.
#
# Implementations:
#   1) Kadane's algorithm (recommended)     : O(n) time, O(1) space
#   2) Prefix-sum + min-prefix (equivalent) : O(n) time, O(1) space
#   3) Brute force (educational)            : O(n^2) time, O(1) space
#
# Input (stdin):
#   One line containing the binary string S
#
# Output:
#   - Echo of S and its length
#   - Result from each method (brute is skipped for large n)
#   - Per-method timing (ms) using timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit


# ------------------------ Method 1: Kadane (O(n)/O(1)) ------------------------
class SolutionKadane:
    def maxSubstring(self, S: str) -> int:
        """
        Map '0' -> +1 and '1' -> -1 and run Kadane.
        Time  : O(n)  -- one pass across S
        Space : O(1)  -- a few integers
        """
        best = 0   # best sum seen so far
        cur  = 0   # current subarray sum
        # Iterate once through S (O(n))
        for ch in S:
            val = 1 if ch == '0' else -1  # O(1)
            # Kadane transition: either start fresh at val or extend
            cur = max(val, cur + val)     # O(1)
            best = max(best, cur)         # O(1)
        # If best <= 0, there is no substring with more 0s than 1s
        return best if best > 0 else -1


# --------------- Method 2: Prefix-sum + min-prefix (O(n)/O(1)) ---------------
class SolutionPrefix:
    def maxSubstring(self, S: str) -> int:
        """
        Maintain prefix sums of mapped values and the minimum prefix so far.
        best = max(pref[i] - min_pref_before_i).
        Time  : O(n)
        Space : O(1)
        """
        pref = 0
        min_pref = 0
        best = float('-inf')
        for ch in S:                                 # O(n)
            pref += (1 if ch == '0' else -1)         # O(1)
            best = max(best, pref - min_pref)        # O(1)
            min_pref = min(min_pref, pref)           # O(1)
        return best if best > 0 else -1


# --------------------------- Method 3: Brute (O(n^2)) -------------------------
class SolutionBrute:
    def maxSubstring(self, S: str) -> int:
        """
        Try all substrings S[i..j] and track #0 - #1 with running counts.
        Time  : O(n^2)  -- double loop; inner work is O(1) per extension
        Space : O(1)
        """
        n = len(S)
        best = float('-inf')
        for i in range(n):                 # O(n)
            zeros = ones = 0
            for j in range(i, n):          # O(n)  -> total O(n^2)
                if S[j] == '0':
                    zeros += 1             # O(1)
                else:
                    ones += 1              # O(1)
                best = max(best, zeros - ones)
        return best if best > 0 else -1


# -------------------------------- I/O helpers --------------------------------
def _read_S():
    data = sys.stdin.read()
    if not data:
        print("Please provide a binary string on stdin.")
        sys.exit(0)
    # Pick the first non-empty line
    for ln in data.splitlines():
        ln = ln.strip()
        if ln:
            return ln
    return ""


def _preview(s, limit=80):
    return s if len(s) <= limit else s[:limit] + "..."


# ----------------------------------- main ------------------------------------
def main():
    S = _read_S()
    n = len(S)
    print(f"S (len={n}): \"{_preview(S)}\"\n")

    kad = SolutionKadane()
    pre = SolutionPrefix()
    brt = SolutionBrute()

    # Time each method once using timeit; compute result again to print clearly.
    t_k = timeit.timeit(lambda: kad.maxSubstring(S), number=1)
    a_k = kad.maxSubstring(S)

    t_p = timeit.timeit(lambda: pre.maxSubstring(S), number=1)
    a_p = pre.maxSubstring(S)

    # Brute guard: keep runtime reasonable for demonstration
    brute_enabled = n <= 4000  # ~8M inner steps worst-case; adjust as desired
    if brute_enabled:
        t_b = timeit.timeit(lambda: brt.maxSubstring(S), number=1)
        a_b = brt.maxSubstring(S)
        brute_line = f"{a_b}\nTime (ms): {t_b * 1000.0:.3f}"
    else:
        brute_line = "(skipped for large n)"

    print("Kadane O(n)/O(1)               :", a_k)
    print("Time (ms): {:.3f}\n".format(t_k * 1000.0))

    print("Prefix-min O(n)/O(1)           :", a_p)
    print("Time (ms): {:.3f}\n".format(t_p * 1000.0))

    print("Brute O(n^2) (educational)     :", brute_line)

    # Simple agreement check when brute ran
    if brute_enabled:
        print("\nAll methods agree ✔" if (a_k == a_p == a_b) else "\nWARNING: methods disagree!")
    else:
        print("\nAgreement (Kadane vs Prefix):", "✔" if a_k == a_p else "❌")


if __name__ == "__main__":
    main()
```

### How to run

```
python3 max_diff_zeros_ones.py
11000010001
```

**Example output (timings vary by machine):**

```
S (len=11): "11000010001"

Kadane O(n)/O(1)               : 6
Time (ms): 0.050

Prefix-min O(n)/O(1)           : 6
Time (ms): 0.045

Brute O(n^2) (educational)     : 6
Time (ms): 0.310

All methods agree ✔
```

---

## 6) Real-World Use Cases (short & important)

1. **Network/telemetry anomaly windows**
   When one event is “good” (+1) and the other is “bad” (−1), find the time window with the largest net advantage.

2. **A/B log analysis / conversions**
   Treat desired events as +1 and undesired as −1 to locate the period with the strongest surplus of desired outcomes.

3. **Bioinformatics signal extraction**
   In binary-encoded sequences (presence/absence), find the contiguous segment with the strongest bias toward the target bit.

4. **Trading rule backtests (toy)**
   Encode up/down days as ±1; the maximum subarray identifies the streak with maximal net gains (illustrative, not a full strategy).