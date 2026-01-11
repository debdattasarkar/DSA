# Minimum Window Subsequence

**Difficulty:** Medium
**Accuracy:** 49.43%
**Submissions:** 16K+
**Points:** 4
**Average Time:** 45m

---

## Problem Statement

You are given two strings, **s1** and **s2**.
Your task is to find the **smallest substring in s1** such that **s2 appears as a subsequence** within that substring.

### Conditions

1. The characters of **s2** must appear **in the same order** within the chosen substring of **s1** (not necessarily contiguous).
2. If there are multiple valid substrings of the **same minimum length**, return the one that appears **first in s1**.
3. If no such substring exists, return an **empty string**.

### Note

Both strings contain **only lowercase English letters**.

---

## Examples

### Example 1

**Input:**
`s1 = "geeksforgeeks", s2 = "eksrg"`

**Output:**
`"eksforg"`

**Explanation:**
`"eksforg"` satisfies all required conditions.
`s2` is a subsequence of `"eksforg"` and it is the smallest and leftmost among all possible valid substrings of `s1`.

---

### Example 2

**Input:**
`s1 = "abcdebdde", s2 = "bde"`

**Output:**
`"bcde"`

**Explanation:**
`"bcde"` and `"bdde"` are two substrings of `s1` where `s2` occurs as a subsequence, but `"bcde"` appears first, so we return it.

---

### Example 3

**Input:**
`s1 = "ad", s2 = "b"`

**Output:**
`""`

**Explanation:**
There is no substring of `s1` in which `s2` appears as a subsequence.

---

## Constraints

* 1 ≤ `s1.length` ≤ 10<sup>4</sup>
* 1 ≤ `s2.length` ≤ 50

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

Where:

* `n` = length of `s1`
* `m` = length of `s2`

---

## Topic Tags

* Dynamic Programming
* Arrays
* two-pointer-algorithm

---

## Related Articles

* **Minimum Window Subsequence**


---

---

## 2) Text explanation (what we need)

We want the **smallest substring of `s1`** such that **`s2` is a subsequence** of that substring.

* **Subsequence** means: characters of `s2` appear in order, not necessarily contiguous.
* If multiple smallest windows exist, return the **leftmost** one.
* If impossible, return `""`.

This is different from “minimum window substring” (which is about character counts). Here it’s about **order**.

---

## Step-by-step Dry Run (classic example)

### Example

`s1 = "abcdebdde"`, `s2 = "bde"`

We’ll use the most expected approach: **forward match + backward shrink**.

### Forward scan to find a full subsequence

* Start `i=0` (s1), `j=0` (s2)
* Move `i` until matching `s2[j]`

Walk:

* i=0 'a' vs 'b' → no
* i=1 'b' matches 'b' → j=1
* i=2 'c' need 'd' → no
* i=3 'd' matches 'd' → j=2
* i=4 'e' matches 'e' → j=3 (done!)

So we found a window ending at `end=4`.

### Backward shrink to make it minimal

Now shrink from `end=4` backwards to find earliest start:

* j = 2 (pointing to last char in s2 = 'e')
* i = 4
* i=4 'e' matches 'e' → j=1
* i=3 'd' matches 'd' → j=0
* i=2 'c' no
* i=1 'b' matches 'b' → j=-1 stop

Start becomes `i+1 = 1`. Window = `s1[1..4] = "bcde"` length 4.

Continue scanning after start+1 (standard trick) to find next windows; another valid is `"bdde"` but same length 4 and `"bcde"` is leftmost, so answer remains `"bcde"`.

---

## 3) Python solutions (easy + interview-expected)

### A) Easy/Brute (generate windows) — not recommended for constraints

Try all substrings and check if `s2` is subsequence.
**Time:** O(n³) worst-ish (n² windows × O(n) check)
**Space:** O(1)

Good only as a “baseline explanation”, not for implementation at n=1e4.

```python
class Solution:
    def minWindow(self, s1, s2):
        # Helper: check if s2 is subsequence of text
        def is_subsequence(text, pattern):
            j = 0
            for ch in text:
                if j < len(pattern) and ch == pattern[j]:
                    j += 1
            return j == len(pattern)

        n = len(s1)
        best = ""
        best_len = float("inf")

        for start in range(n):
            for end in range(start, n):
                window_len = end - start + 1
                if window_len >= best_len:
                    break
                if is_subsequence(s1[start:end+1], s2):
                    best = s1[start:end+1]
                    best_len = window_len
                    break

        return best
```

---

### B) Most expected (Two pointers: forward match + backward shrink)

This is a standard interview approach and passes well in practice.

**Idea**

* Scan forward to match entire `s2`.
* Once matched, scan backward to shrink to minimum start for that end.
* Record best window; repeat.

**Time:** Typically close to `O(n*m)` in worst case, often faster in practice
**Space:** `O(1)`

```python
class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        if m == 0:
            return ""
        if n < m:
            return ""

        best_start = -1
        best_len = float("inf")

        i = 0  # pointer for s1
        while i < n:
            # ---------- Forward: find an end where s2 fully matches ----------
            j = 0  # pointer for s2
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:   # matched all of s2
                        break
                i += 1

            if j < m:
                break  # no more possible matches

            end = i  # s1[end] is where we completed matching s2

            # ---------- Backward: shrink to minimum start for this end ----------
            j = m - 1
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            start = i + 1  # minimal start index for this window

            window_len = end - start + 1
            if window_len < best_len:
                best_len = window_len
                best_start = start

            # ---------- Move i to next position after start to search next window ----------
            i = start + 1

        if best_start == -1:
            return ""
        return s1[best_start:best_start + best_len]
```

---

### C) DP approach (matches expected complexity O(n*m))

DP commonly appears in editorials and is very “correctness-friendly”.

**DP meaning**
Let `dp[i][j]` = the **start index** in `s1` of a window ending at `i` that contains `s2[:j+1]` as subsequence.
If impossible, `dp[i][j] = -1`.

We can optimize to 1D.

**Time:** `O(n*m)`
**Space:** `O(m)` (optimized)

```python
class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        if m == 0:
            return ""
        if n < m:
            return ""

        # dp[j] = start index of window ending at current i that matches s2[:j+1]
        # -1 means impossible
        dp = [-1] * m

        best_len = float("inf")
        best_start = -1

        for i in range(n):
            # Update dp from right to left to avoid overwriting dp[j-1] too early
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    if j == 0:
                        dp[j] = i  # single char match starts here
                    else:
                        dp[j] = dp[j - 1]  # extend previous subsequence
            # If dp[m-1] is valid, we have a window ending at i
            if dp[m - 1] != -1:
                start = dp[m - 1]
                window_len = i - start + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = start

        return "" if best_start == -1 else s1[best_start:best_start + best_len]
```

---

## 4) Interview: quick recall + expected Q&A

### How to remember quickly (mnemonic)

**“MATCH → SHRINK → SAVE”**

* MATCH `s2` as subsequence by scanning forward
* SHRINK window backward to minimal start
* SAVE best answer, continue

### 5-line pseudo-code template

```
best = INF
scan i forward to match all s2 (j hits m)
when matched at end=i: walk i backward with j=m-1 to find start
update best window [start..end]
set i = start+1 and repeat
```

### 60-second recall script (what you say)

1. “We need min substring where s2 is a subsequence (order matters).”
2. “I scan s1 forward to find a position where I can match all of s2.”
3. “Once matched, I walk backward to shrink the start as much as possible.”
4. “Record the smallest/leftmost window and continue from start+1.”
5. “This runs around O(n*m) worst-case, uses O(1) space.”

---

## Expected interviewer Q&A

**Q1. How is this different from minimum window substring?**
A. That one matches character counts (anagram-like). Here `s2` must appear **in order** as a subsequence.

**Q2. Why backward shrinking gives minimum window for that end?**
A. Because we keep the required subsequence order while moving left as far as possible until removing any more would break the subsequence.

**Q3. Why set `i = start + 1` after finding a window?**
A. To search for another window that starts later but might be shorter or equally short but earlier; it ensures progress and avoids missing candidates.

**Q4. Complexity?**
A. Two-pointer method is typically efficient; worst-case around `O(n*m)`. DP is guaranteed `O(n*m)`.

**Q5. Edge cases?**
A. If `s2` not subsequence of `s1` → return `""`. If multiple same-length windows, keep the first found (leftmost).

If you want next: I can add (5) real-world use cases, (6) full timed program, and a sketchnote like your previous problems.

---

---

## 5) Real-World Use Cases (few, very interviewer-relatable)

1. **Log / event stream troubleshooting (find smallest time span containing an ordered sequence)**

   * You have logs in time order (`s1`), and you want the **shortest segment** that contains an ordered pattern of events (`s2`) like: `login → search → purchase`.

2. **User journey / funnel analytics**

   * Given a user’s clickstream, find the smallest session window where they performed steps in order (e.g., `view → add_to_cart → checkout`).

3. **Bioinformatics (ordered motif inside a small region)**

   * Find the smallest DNA/RNA region where a motif appears **as a subsequence** (order preserved, gaps allowed).

4. **Document processing / compliance**

   * Find the smallest snippet of a document containing an ordered set of keywords (in order), allowing other words in between.

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This full runnable program:

* Reads `s1` and `s2`
* Finds the **minimum window subsequence** using the **forward match + backward shrink** approach (most interview-friendly)
* Prints input, output, and total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: `s1`
* Line 2: `s2`

If no stdin, demo uses:

* `s1 = "abcdebdde"`
* `s2 = "bde"`
  Expected output: `"bcde"`

```python
import sys
import time


class Solution:
    def minWindow(self, s1, s2):
        """
        Two-pointer approach: forward match + backward shrink.
        Time: Worst-case ~O(n * m) in bad cases, usually efficient in practice
        Auxiliary Space: O(1)
        """
        n, m = len(s1), len(s2)
        if m == 0 or n == 0 or n < m:
            return ""

        best_start = -1
        best_len = float("inf")

        i = 0  # pointer for s1

        # Outer loop ensures i always moves forward overall
        while i < n:
            # ---------------- Forward scan to match whole s2 ----------------
            # Time: up to O(n) across iterations, worst-case can contribute to O(n*m)
            j = 0  # pointer for s2
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:  # matched all of s2
                        break
                i += 1

            if j < m:
                break  # can't match s2 anymore

            end = i  # current window ends here (inclusive)

            # ---------------- Backward shrink to get minimal start ----------------
            # Walk backwards and match s2 from end to start
            # Time: O(window length) for this match
            j = m - 1
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            start = i + 1  # minimal start for this end

            # Update best answer (tie handled by "first found" due to strict <)
            window_len = end - start + 1
            if window_len < best_len:
                best_len = window_len
                best_start = start

            # Move i to next position after start to continue searching
            # Time: O(1)
            i = start + 1

        if best_start == -1:
            return ""
        return s1[best_start: best_start + best_len]


def main():
    # Measure full program runtime (parse + solve + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().splitlines()
    data = [line.strip() for line in data if line.strip()]

    if len(data) >= 2:
        s1 = data[0]
        s2 = data[1]
    else:
        # ---------------- DEMO MODE ----------------
        s1 = "abcdebdde"
        s2 = "bde"

    solver = Solution()

    # Solve
    # Time: ~O(n*m) worst-case, Aux Space: O(1)
    answer = solver.minWindow(s1, s2)

    print("Input:")
    print("s1 =", s1)
    print("s2 =", s2)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

**Input:** `s1="abcdebdde"`, `s2="bde"`
**Output:** `bcde` (+ runtime)

---
