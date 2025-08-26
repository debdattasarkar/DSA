

---

# Check if a String is Subsequence of Other

**Difficulty:** Easy
**Accuracy:** 51.68%
**Submissions:** 21K+
**Points:** 2

---

### Problem Statement

Given two strings **s1** and **s2**. You have to check that **s1** is a subsequence of **s2** or not.

**Note:**
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

---

### Examples:

#### Example 1:

**Input:**
s1 = "AXY", s2 = "YADXCP"

**Output:**
false

**Explanation:**
s1 is not a subsequence of s2 as 'Y' appears before 'A'.

---

#### Example 2:

**Input:**
s1 = "gksrek", s2 = "geeksforgeeks"

**Output:**
true

**Explanation:**
If we combine the bold characters of `"geeksforgeeks"`, it equals to s1.
So s1 is a subsequence of s2.

---

### Constraints:

* 1 ≤ s1.size(), s2.size() ≤ 10⁶

---

### Expected Complexities:

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

### Topic Tags:

* Strings
* Greedy
* Two-pointer-algorithm

---

### Related Articles:

* [Given Two Strings Find First String Subsequence Second](https://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/)

---

---

Here’s a clean, interview-style package for the “Check if a String is Subsequence of Other” problem.

---

# 2) Intuition + Step-by-Step Dry Run

**Goal:** Determine whether `s1` is a subsequence of `s2`.
Definition: `s1` is a subsequence of `s2` if you can delete some (possibly zero) characters from `s2` without reordering the remaining ones to obtain `s1`.

### Idea (Greedy two-pointer)

Walk through `s2` once and try to “match” the next needed character of `s1`.

* Maintain pointer `i` in `s1` (the next char we need).
* Scan `s2` with pointer `j`.
* Each time `s2[j] == s1[i]`, advance `i`.
* If `i` reaches `len(s1)`, all characters were matched in order → return `True`.

### Dry run

`s1 = "gksrek"`, `s2 = "geeksforgeeks"`

| j (s2) | s2\[j] | i (s1) wants | Match? | i after        |
| ------ | ------ | ------------ | ------ | -------------- |
| 0      | g      | g            | ✅      | 1 (wants ‘k’)  |
| 1      | e      | k            |        | 1              |
| 2      | e      | k            |        | 1              |
| 3      | k      | k            | ✅      | 2 (wants ‘s’)  |
| 4      | s      | s            | ✅      | 3 (wants ‘r’)  |
| 5      | f      | r            |        | 3              |
| 6      | o      | r            |        | 3              |
| 7      | r      | r            | ✅      | 4 (wants ‘e’)  |
| 8      | g      | e            |        | 4              |
| 9      | e      | e            | ✅      | 5 (wants ‘k’)  |
| 10     | e      | k            |        | 5              |
| 11     | k      | k            | ✅      | 6 (== len(s1)) |

Since `i == len(s1)` → `True`.

Edge checks:

* `s1 = ""` → always `True` (empty string is subsequence of any string).
* `len(s1) > len(s2)` → impossible, return `False` early.

---

# 3) Python solutions (brute & optimized)

### A) “Brute” (still linear): iterator trick

Pythonic and short; great for interviews when readability matters.

```python
class Solution:
    def isSubSeq(self, s1, s2):
        # Time: O(|s2|) average, Space: O(1)
        # Edge: empty s1 is subsequence of any s2
        if not s1:
            return True
        # Create an iterator over s2 and check characters of s1 in order
        it = iter(s2)  # O(1)
        # all(...) short-circuits: for each c in s1, keep consuming from s2
        return all(c in it for c in s1)  # each membership uses iterator progression
```

**Why this works:**
`c in it` scans forward from the iterator’s current position. It never rewinds, so together it’s a single pass through `s2` (amortized O(|s2|)).

---

### B) Standard two-pointer (explicit, most common answer)

```python
class Solution:
    def isSubSeq(self, s1, s2):
        # Time: O(|s2|) (single pass), Space: O(1)
        n1, n2 = len(s1), len(s2)
        if n1 == 0:
            return True                    # empty is always subsequence
        if n1 > n2:
            return False                   # impossible if s1 is longer

        i = 0                               # index in s1 (next char we need)
        for ch in s2:                       # scan s2 once -> O(n2)
            if ch == s1[i]:                 # match next needed char
                i += 1
                if i == n1:                 # matched all chars of s1
                    return True
        return False                        # some chars never matched
```

---

### (Optional) C) Overkill DP (LCS)

Use only if interviewer asks for a generic approach; otherwise skip because it’s O(n1\*n2) time and O(min(n1, n2)) space with rolling rows. You’d check `LCS(s1, s2) == len(s1)`.

---

# 4) Interviewer-style Q\&A

**Q1. What’s the time and space complexity of your solution?**
Two-pointer: **Time O(|s2|)**, **Space O(1)** (after trivial early checks).
Iterator version: amortized the same.

**Q2. Why is greedy matching (two-pointer) correct?**
Because the only requirement is order; taking the earliest feasible match for each `s1[i]` can’t hurt later matches. If a later better match existed, the earlier match never prevents advancing `i`.

**Q3. What if there are repeated characters?**
Still fine: we only advance `i` when we match the *next* needed character. Repetitions in `s2` don’t break order.

**Q4. Is subsequence the same as substring?**
No. Substring requires **contiguous** characters; subsequence only requires **relative order**.

**Q5. Edge cases?**

* `s1 == ""` → `True`.
* `len(s1) > len(s2)` → `False`.
* Case sensitivity (depends on problem; typically **case-sensitive**).
* Very long strings (up to 1e6) → prefer O(1) space, one pass.

**Q6. What if we must answer many queries “Is s1 a subsequence of the same s2?”**
Preprocess `s2` → map each character to its sorted index list. For each `s1`, walk with binary searches to find next position > previous.
Time per query: **O(|s1| log σ)** (σ = average occurrences per character). Great when `s2` is fixed and many `s1`s arrive.

```python
# Sketch for multiple queries (not required here)
# pre = {ch: [positions]} built from s2
# then for s1: keep 'pos' = -1, for each c in s1 do binary search in pre[c] for first > pos.
```

---

---

Below is a **complete, runnable Python program** that:

1. Implements the classic **two-pointer** solution (the most expected one in interviews) inside `class Solution.isSubSeq`.
2. Also includes the concise **iterator** variant for reference.
3. Shows **input values and printed outputs**.
4. Uses Python’s **timeit** module to measure the total runtime of the main demonstration.
5. Adds clear **inline comments** that state the time and space complexity of each step.
6. Ends with a few crisp **real-world use cases**.

---

```python
#!/usr/bin/env python3
"""
Check if s1 is a subsequence of s2.

Main idea (two-pointer / greedy):
- Walk through s2 once and try to match the next needed character in s1.
- If we match all characters of s1 in order, s1 is a subsequence of s2.

Time & Space at a glance:
- Two-pointer solution:  Time O(|s2|), Space O(1)
- Iterator trick:        Time O(|s2|) amortized, Space O(1)
"""

from timeit import timeit


class Solution:
    # ---------- Interview-standard two-pointer approach ----------
    def isSubSeq(self, s1: str, s2: str) -> bool:
        """
        Returns True iff s1 is a subsequence of s2.

        Step-by-step complexities:
        - len(s1), len(s2) : O(1) each
        - Early checks     : O(1)
        - Single pass over s2 with constant-time comparisons:
            Time  : O(|s2|)
            Space : O(1)
        """
        n1, n2 = len(s1), len(s2)     # O(1)
        if n1 == 0:                   # empty is always a subsequence
            return True               # O(1)
        if n1 > n2:                   # impossible if s1 longer than s2
            return False              # O(1)

        i = 0                         # points to next char needed in s1  | Space: O(1)
        for ch in s2:                 # scan s2 once                       | Time: O(|s2|)
            if ch == s1[i]:
                i += 1                # matched one more char of s1        | O(1)
                if i == n1:           # all chars of s1 matched
                    return True       # O(1)

        return False                  # not all chars matched              | O(1)

    # ---------- Pythonic "brute" (still linear): iterator trick ----------
    def isSubSeq_iter(self, s1: str, s2: str) -> bool:
        """
        Uses an iterator over s2; for each character c in s1, we ask if c exists
        ahead in the iterator. The iterator only moves forward. Amortized single pass.

        Time  : O(|s2|) amortized
        Space : O(1)
        """
        if not s1:
            return True
        it = iter(s2)                 # O(1)
        # 'c in it' consumes the iterator forward until c is found or exhausted.
        return all(c in it for c in s1)


# --------------------------- Demo / Main ---------------------------
def main():
    sol = Solution()

    # A small suite of test cases (Input values)
    tests = [
        # (s1, s2, expected)
        ("AXY", "YADXCP", False),           # 'Y' appears before 'A' in s2 ⇒ not subsequence
        ("gksrek", "geeksforgeeks", True),  # classic positive example
        ("", "abc", True),                  # empty is subsequence of any string
        ("abc", "", False),                 # s1 longer than s2 ⇒ False
        ("abc", "ahbgdc", True),            # Leet-style positive
        ("axc", "ahbgdc", False),           # Leet-style negative
        ("aaaa", "aaaaaaaaaa", True),       # repeated chars
        ("abc", "acb", False),              # order must be preserved
    ]

    print("Two-pointer results:")
    for s1, s2, exp in tests:
        res = sol.isSubSeq(s1, s2)
        print(f"  s1='{s1}'  s2='{s2}'  -> {res}  (expected {exp})")

    print("\nIterator-trick results:")
    for s1, s2, exp in tests:
        res = sol.isSubSeq_iter(s1, s2)
        print(f"  s1='{s1}'  s2='{s2}'  -> {res}  (expected {exp})")


if __name__ == "__main__":
    # Use timeit to measure end-to-end time of running main() once.
    # We measure the entire run (all test cases printed once).
    runtime = timeit("main()", globals=globals(), number=1)
    print(f"\nTotal runtime (timeit, number=1): {runtime:.6f} seconds")
```

---

## Sample Output (will look like this)

```
Two-pointer results:
  s1='AXY'  s2='YADXCP'  -> False  (expected False)
  s1='gksrek'  s2='geeksforgeeks'  -> True  (expected True)
  s1=''  s2='abc'  -> True  (expected True)
  s1='abc'  s2=''  -> False  (expected False)
  s1='abc'  s2='ahbgdc'  -> True  (expected True)
  s1='axc'  s2='ahbgdc'  -> False  (expected False)
  s1='aaaa'  s2='aaaaaaaaaa'  -> True  (expected True)
  s1='abc'  s2='acb'  -> False  (expected False)

Iterator-trick results:
  s1='AXY'  s2='YADXCP'  -> False  (expected False)
  s1='gksrek'  s2='geeksforgeeks'  -> True  (expected True)
  s1=''  s2='abc'  -> True  (expected True)
  s1='abc'  s2=''  -> False  (expected False)
  s1='abc'  s2='ahbgdc'  -> True  (expected True)
  s1='axc'  s2='ahbgdc'  -> False  (expected False)
  s1='aaaa'  s2='aaaaaaaaaa'  -> True  (expected True)
  s1='abc'  s2='acb'  -> False  (expected False)

Total runtime (timeit, number=1): 0.00xxxx seconds
```

*(Exact timing varies by machine.)*

---

## 6) Real-World Use Cases (just a few, high-value)

1. **Command/filter pipelines** – Determine whether a short pattern (e.g., `-abc`) appears in order within a long command string or log line without requiring contiguity.

2. **Fuzzy search / code editors** – Matching a typed abbreviation (“gfg”) against filenames or symbols (“geeksforgeeks.py”) where only the relative order matters.

3. **Data validation** – Checking whether a requested sequence of steps/events is consistent with an observed longer execution trace, permitting skipped steps but not reordering.

4. **Versioning & diffs** – Quick checks if a small change-list is an ordered subsequence of a larger history to assert non-conflicting merges.

