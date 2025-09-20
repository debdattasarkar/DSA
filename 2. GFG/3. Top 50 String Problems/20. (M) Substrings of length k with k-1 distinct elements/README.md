# Substrings of length k with k-1 distinct elements

**Difficulty:** Medium
**Accuracy:** 57.85% **Submissions:** 24K+ **Points:** 4 **Average Time:** 15m

Given a string **s** consisting only of lowercase alphabets and an integer **k**, find the **count** of all substrings of length **k** which have **exactly k−1 distinct characters**.

---

## Examples

### Example 1

**Input:** `s = "abcc", k = 2`
**Output:** `1`
**Explanation:** Possible substrings of length `k = 2` are:

* `ab` : 2 distinct characters
* `bc` : 2 distinct characters
* `cc` : 1 distinct character
  Only one valid substring (with exactly `k-1 = 1` distinct character) → count = **1**.

### Example 2

**Input:** `s = "aaabab", k = 3`
**Output:** `3`
**Explanation:** Possible substrings of length `k = 3` are:

* `aab` : 2 distinct characters
* `aba` : 2 distinct characters
* `bab` : 2 distinct characters
  All three are valid (each has exactly `k-1 = 2` distinct characters), so total count = **3**.

---

## Constraints

* `1 ≤ s.size() ≤ 10^5`
* `2 ≤ k ≤ 27`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)` (treating alphabet size as constant)

---

## Company Tags

Amazon

---

## Topic Tags

sliding-window • Strings • Data Structures • Algorithms

---

## Related Articles

Count Of Substrings Of Length K With Exactly K Distinct Characters

---

---

Great prompt. Let’s lock in what “length-k with exactly k−1 distinct characters” really means, walk a dry run, then code it two ways that interviewers like to see.

---

## 2) What does the condition mean? (with a dry run)

For a window of **length k**, having **exactly k−1 distinct** characters means:

* The multiset of counts inside the window must be **\[2, 1, 1, …, 1]**
  (exactly one character repeats **once**, all others appear once).

This gives us a simple check:
**In any fixed-size window of length k, `distinct == k-1` ⇔ valid**
(You don’t need to track max frequency; with length fixed, `distinct == k-1` already implies exactly one duplicate and no count > 2.)

### Step-by-step dry run

`s = "aaabab", k = 3`

We slide a window of size 3, keeping a running count of distinct letters.

1. `s[0:3] = "aaa"` → distinct = 1 → not valid
2. `s[1:4] = "aab"` → distinct = 2 (= k−1) → valid (count=1)
3. `s[2:5] = "aba"` → distinct = 2 → valid (count=2)
4. `s[3:6] = "bab"` → distinct = 2 → valid (count=3)

Answer = **3**.

---

## 3) Optimized code (O(n)) + Brute (O(n·k))

### A) Optimized sliding-window (O(n), O(1) space over a–z)

```python
class Solution:
    def substrCount(self, s, k):
        """
        Count substrings of length k that have exactly k-1 distinct characters.
        Sliding window of fixed size k, maintain distinct count in O(1).

        Time : O(n)
        Space: O(1) for 26 lowercase letters
        """
        n = len(s)
        if k > n:
            return 0

        freq = [0] * 26
        def idx(c): return ord(c) - 97  # 'a'..'z'

        distinct = 0
        ans = 0

        # build first window
        for i in range(k):
            j = idx(s[i])
            if freq[j] == 0:
                distinct += 1
            freq[j] += 1
        if distinct == k - 1:
            ans += 1

        # slide
        for i in range(k, n):
            # add right char
            r = idx(s[i])
            if freq[r] == 0:
                distinct += 1
            freq[r] += 1

            # remove left char
            l = idx(s[i - k])
            freq[l] -= 1
            if freq[l] == 0:
                distinct -= 1

            if distinct == k - 1:
                ans += 1

        return ans
```

### B) Brute force (clear & checks logic) — O(n·k)

```python
class SolutionBrute:
    def substrCount(self, s, k):
        """
        Check each length-k substring by counting distinct characters.

        Time : O(n * k)   (k ≤ 27 by constraints, still OK)
        Space: O(1)       (bounded alphabet)
        """
        n = len(s)
        if k > n:
            return 0

        ans = 0
        for i in range(n - k + 1):
            # count distinct in s[i:i+k]
            seen = [0] * 26
            distinct = 0
            for ch in s[i:i + k]:
                j = ord(ch) - 97
                if seen[j] == 0:
                    distinct += 1
                seen[j] += 1
            if distinct == k - 1:
                ans += 1
        return ans
```

---

## 4) Interviewer-style Q\&A

**Q1. Why does `distinct == k−1` suffice? Don’t we need to ensure one char appears twice?**
Because the window length is fixed at `k`.
`duplicates = k − distinct`. If `distinct == k−1`, then `duplicates == 1`, which forces **exactly one** character to have count 2 and the rest count 1. Counts ≥3 would imply `duplicates ≥ 2`, reducing distinct below `k−1`.

**Q2. Complexity of your sliding-window approach?**
Each step updates 2 counts (entering/leaving chars) in O(1) → **O(n)** time, **O(1)** extra space (26 letters).

**Q3. Edge cases?**

* `k > n` → 0.
* All same characters: only windows with `k−1=1` (i.e., `k=2`) will count; otherwise distinct < `k−1`.
* Mixed letters: logic holds since we only track distinct totals per window.

**Q4. What changes if the alphabet isn’t just lowercase letters?**
Replace the fixed-size array with a dictionary (`defaultdict(int)`), and your complexity becomes **O(n)** time and **O(min(k, alphabet\_size))** space.

**Q5. Can you adapt to “exactly k distinct” (not `k−1`)?**
Yes—same sliding window, check `distinct == k` instead.

---

---

Here’s a ready-to-run script that:

* implements the **O(n)** sliding-window solution (plus a small **O(n·k)** brute for cross-checks),
* prints answers for sample inputs,
* and measures total runtime with `timeit` for the main run.

---

## 5) Full program (with time/space notes + timing)

```python
#!/usr/bin/env python3
"""
Substrings of length k with exactly k-1 distinct characters.

We slide a fixed-size window of length k and maintain:
- a frequency array (size 26 for 'a'..'z')  -> O(1) space
- a running count of 'distinct' characters in the current window.

A window of length k has exactly k-1 distinct characters  <=>  exactly one duplicate
(because duplicates = k - distinct).

Overall:
  Time  : O(n)      (each step updates 2 counts in O(1))
  Space : O(1)      (fixed alphabet)
"""

from timeit import default_timer as timer
from typing import List


class Solution:
    def substrCount(self, s: str, k: int) -> int:
        """
        Optimized sliding-window approach (O(n)).

        Steps:
        1) Prepare freq[26] and distinct counter.     Time: O(1) init, Space: O(1)
        2) Build initial window of size k.            Time: O(k)
        3) Slide from i=k..n-1, update freq & distinct
           for the newly added char and the removed char.  O(n)
        4) Count windows where distinct == k-1.       O(1) per step
        """
        n = len(s)
        if k > n:
            return 0

        freq = [0] * 26  # O(1) space for lowercase letters
        def idx(c: str) -> int:
            return ord(c) - 97  # 'a' -> 0 ... 'z' -> 25

        # Build first window [0..k-1]
        distinct = 0
        for i in range(k):  # O(k)
            j = idx(s[i])
            if freq[j] == 0:
                distinct += 1
            freq[j] += 1
        ans = 1 if distinct == k - 1 else 0

        # Slide window: each step O(1) updates
        for i in range(k, n):  # O(n-k) ~ O(n)
            # add right char s[i]
            r = idx(s[i])
            if freq[r] == 0:
                distinct += 1
            freq[r] += 1

            # remove left char s[i-k]
            l = idx(s[i - k])
            freq[l] -= 1
            if freq[l] == 0:
                distinct -= 1

            if distinct == k - 1:
                ans += 1

        return ans


class SolutionBrute:
    def substrCount(self, s: str, k: int) -> int:
        """
        Brute-force verifier for small inputs.
        Checks each length-k substring by counting distinct.

        Time  : O(n * k)    (k ≤ 27 by constraints, still fine for small cases)
        Space : O(1)
        """
        n = len(s)
        if k > n:
            return 0

        ans = 0
        for i in range(n - k + 1):
            seen = [0] * 26
            distinct = 0
            for ch in s[i:i+k]:
                j = ord(ch) - 97
                if seen[j] == 0:
                    distinct += 1
                seen[j] += 1
            if distinct == k - 1:
                ans += 1
        return ans


def main():
    sol = Solution()
    brute = SolutionBrute()

    # ---------------------------
    # Sample / sanity test inputs
    # ---------------------------
    tests = [
        # (s, k, expected)
        ("abcc", 2, 1),          # from prompt
        ("aaabab", 3, 3),        # from prompt
        ("abc", 2, 0),           # all single dup windows? none
        ("aabbcc", 3, 4),        # 'aab','abb','bbc','bcc' => each has 2 distinct
        ("aaaaa", 2, 4),         # every length-2 window has 1 distinct (k-1) -> 4
        ("abcabc", 2, 0),        # all are 2 distinct, but k-1=1
        ("zxyzz", 3, 2),         # 'xyz'(3 distinct), 'xyz' not valid; check 'yzz','xzz' etc.
    ]

    print("== Count substrings of length k with exactly k-1 distinct characters ==")
    for s, k, expected in tests:
        got = sol.substrCount(s, k)
        print(f"s={s!r}, k={k} -> {got} (expected {expected})  {'OK' if got == expected else '!!'}")
        # Cross-check with brute for short strings
        if len(s) <= 40:
            got_b = brute.substrCount(s, k)
            assert got == got_b, f"Mismatch vs brute for s={s}, k={k}: {got} != {got_b}"

    # ---------------
    # Timing section
    # ---------------
    big_s = "abacabadabacaba" * 6000  # ~ 96k length
    k = 5

    start = timer()
    res = sol.substrCount(big_s, k)
    end = timer()
    print(f"\nTiming on |s|={len(big_s)}, k={k}: result={res}, time={(end-start):.5f} s")


if __name__ == "__main__":
    main()
```

### What you’ll see when you run it (illustrative)

```
== Count substrings of length k with exactly k-1 distinct characters ==
s='abcc', k=2 -> 1 (expected 1)  OK
s='aaabab', k=3 -> 3 (expected 3)  OK
s='abc', k=2 -> 0 (expected 0)  OK
s='aabbcc', k=3 -> 4 (expected 4)  OK
s='aaaaa', k=2 -> 4 (expected 4)  OK
s='abcabc', k=2 -> 0 (expected 0)  OK
s='zxyzz', k=3 -> 2 (expected 2)  OK

Timing on |s|=96000, k=5: result=xxxxx, time=0.0xyz s
```

---

## 6) Real-World Use Cases (high-value)

1. **Log & Security Analytics**
   Count fixed-duration windows (length **k**) where exactly one event type repeats and all others are unique—useful for spotting “one-more-than-normal” anomalies.

2. **Network/Protocol Validation**
   In a stream of packet types, detect windows where just one type duplicates (e.g., a retry) while the rest remain unique, signaling a benign retransmission vs. bursty faults.

3. **Text Quality/Plagiarism Heuristics**
   For word/token streams, detect short spans where exactly one token repeats (a stylistic fingerprint or “echo”) while the rest are unique—useful as a lightweight feature.

