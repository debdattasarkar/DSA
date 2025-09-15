# Closest Strings

**Difficulty:** Easy
**Accuracy:** 27.12%
**Submissions:** 52K+
**Points:** 2

---

## Problem Statement

Given a list of words, `S`, followed by two specific words, `word1` and `word2`, the task is to find the **minimum distance** between the indices of these two words in the list.

**Note:**

* `word1` and `word2` are both in the list.
* There can be multiple occurrences of the words in the list.

---

## Example

### Example 1

**Input:**
`S = {"the", "quick", "brown", "fox", "quick"}`
`word1 = "the"`
`word2 = "fox"`
**Output:** `3`
**Explanation:** Minimum distance between the words `"the"` and `"fox"` is `3`.

### Example 2

**Input:**
`S = {"geeks", "for", "geeks", "contribute", "practice"}`
`word1 = "geeks"`
`word2 = "practice"`
**Output:** `2`
**Explanation:** Minimum distance between the words `"geeks"` and `"practice"` is `2`.

---

## Constraints

* Sum of lengths of words `≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* `Amazon`, `Linkedin`

---

## Topic Tags

* `Strings`, `Sorting`, `Data Structures`, `Algorithms`

---

## Related Interview Experiences

* Linkedin Internship Interview Software Development Engineer

---

## Related Articles

* [Find The Minimum Distance Between The Given Two Words](https://www.geeksforgeeks.org/find-the-minimum-distance-between-the-given-two-words/)

---

---
got it — we’ll follow the **judge convention you hit**:

> **If `word1 == word2`, the answer must be `0`.**

Below is everything you need: clear explanation + dry runs, multiple Python solutions (with inline interview-style comments), and quick Q\&A.

---

## 2) Explanation + step-by-step dry run

### Goal

Given a list of words `s` and two target words `word1`, `word2`, return the **minimum index distance** between any occurrence of `word1` and any occurrence of `word2`.

### Core one-pass idea (O(n), O(1))

Scan once and remember the **last seen index** of each target.

* Keep `last1` (latest index of `word1`) and `last2` (latest index of `word2`), both start at `-1`.
* For each index `i` with word `w = s[i]`:

  * If `w == word1`, set `last1 = i` and, if `last2` is valid, update `ans = min(ans, |i - last2|)`.
  * If `w == word2`, set `last2 = i` and, if `last1` is valid, update `ans = min(ans, |i - last1|)`.
* **Judge rule we’re using:** if `word1 == word2`, return `0` immediately.

Why this works: when you see a new occurrence of one word, the closest opposite occurrence so far is the **most recent** one — thus one scan is sufficient.

#### Dry run A (from the prompt)

`s = ["the","quick","brown","fox","quick"]`, `word1="the"`, `word2="fox"`

* i=0: “the” → `last1=0`, `ans=∞`
* i=1: –
* i=2: –
* i=3: “fox” → `last2=3`, update `ans=min(∞, |3-0|=3)=3`
* i=4: –
  Return **3**.

#### Dry run B

`s = ["geeks","for","geeks","contribute","practice"]`, `word1="geeks"`, `word2="practice"`

* i=0: “geeks” → `last1=0`
* i=1: –
* i=2: “geeks” → `last1=2`
* i=3: –
* i=4: “practice” → `last2=4`, `ans=min(∞, |4-2|=2)=2`
  Return **2**.

#### Dry run C (your failing case / judge rule)

`s = ["qz","jm","dv","ejs","of","ejs","qz"]`, `word1="qz"`, `word2="qz"`

* Since `word1 == word2`, **judge expects 0** → return **0**.

> Note: Some platforms instead ask for the **minimum gap between consecutive occurrences** when the words are equal. That rule would output `6` for Dry run C. Your judge uses the **0** convention — we code to that.

---

## 3) Python solutions (multiple ways)

### A) One-pass (most expected) — **O(n) time, O(1) space**

```python
# User function Template for python3

class Solution:
    def shortestDistance(self, s, word1, word2):
        """
        Single scan with last-seen indices.
        Judge convention: if word1 == word2, return 0.
        Time : O(n)  |  Space : O(1)
        """
        # Judge's rule: same words => distance 0
        if word1 == word2:
            return 0

        last1 = last2 = -1     # last seen indices
        ans = float('inf')

        for i, w in enumerate(s):
            if w == word1:
                last1 = i
                if last2 != -1:                    # we have seen word2 before
                    d = abs(last1 - last2)
                    if d < ans:
                        ans = d
            elif w == word2:
                last2 = i
                if last1 != -1:                    # we have seen word1 before
                    d = abs(last1 - last2)
                    if d < ans:
                        ans = d

        return -1 if ans == float('inf') else ans
```

### B) Two-pointer over positions (collect indices first) — **O(n) time, O(k1+k2) space**

Useful if you want the positions explicitly or will answer multiple queries.

```python
class SolutionTwoPointer:
    def shortestDistance(self, s, word1, word2):
        # Judge's rule
        if word1 == word2:
            return 0

        pos1 = [i for i, w in enumerate(s) if w == word1]
        pos2 = [i for i, w in enumerate(s) if w == word2]
        if not pos1 or not pos2:
            return -1

        i = j = 0
        ans = float('inf')
        # classic merge-like sweep to minimize |pos1[i] - pos2[j]|
        while i < len(pos1) and j < len(pos2):
            ans = min(ans, abs(pos1[i] - pos2[j]))
            if pos1[i] < pos2[j]:
                i += 1
            else:
                j += 1
        return ans
```

### C) Brute force (educational baseline) — **O(n²)**

Compare every index of `word1` with every index of `word2`.

```python
class SolutionBrute:
    def shortestDistance(self, s, word1, word2):
        if word1 == word2:
            return 0  # judge's rule

        idx1 = [i for i, w in enumerate(s) if w == word1]
        idx2 = [i for i, w in enumerate(s) if w == word2]
        if not idx1 or not idx2:
            return -1
        ans = float('inf')
        for i in idx1:
            for j in idx2:
                d = abs(i - j)
                if d < ans:
                    ans = d
        return ans
```

> **If you ever face the other convention** (“same words ⇒ min gap between consecutive occurrences”), just replace the `if word1 == word2: return 0` line with a short consecutive-gap loop.

---

## 4) Interviewer-style Q\&A

**Q1. Why does the one-pass method give the true minimum?**
At index `i`, the closest opposite occurrence to the left is exactly the **most recent** one — any older one is farther. We update at every encounter, so we can’t miss a smaller distance.

**Q2. What’s the complexity?**

* One-pass: **O(n)** time, **O(1)** space.
* Two-pointer: **O(n)** to collect indices + **O(k1+k2)** to sweep; uses extra space for the lists.
* Brute force: up to **O(n²)** comparisons (only for learning/testing).

**Q3. What about `word1 == word2`?**
Conventions differ. Your judge wants **0**; some judges want the **minimum gap between consecutive occurrences**. Clarify which rule is expected before coding.

**Q4. What if one of the words doesn’t appear?**
The prompt usually guarantees both exist; otherwise return **-1** (no valid pair).

**Q5. Is it index distance or count of words in between?**
Index distance (absolute difference of indices). Example with indices 0 and 3 → distance `3` (not `2`).

**Q6. Can this be extended to a stream?**
Yes — keep `last1`, `last2`, and current `ans`. Update in **O(1)** per incoming word.

**Q7. What pitfalls should I watch for?**

* Forgetting the `word1 == word2` rule for the judge you’re on.
* Returning `∞` (no update) — convert to `-1` if needed.
* Off-by-one: distance is `abs(i - j)`, not `abs(i - j) - 1`.

---

---

Absolutely—here’s a **full, runnable Python program** for **Closest Strings** that

* implements the **one-pass O(n) / O(1)** solution (with your judge rule: if `word1 == word2`, return `0`),
* prints **inputs and outputs** for several cases (including the tricky `word1 == word2`),
* and **benchmarks** the solution using `timeit` right in `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Closest Strings (Minimum Index Distance Between Two Words)

We follow the judge rule discussed:
  -> If word1 == word2, distance is 0.

Algorithm (one pass):
  Keep last seen indices of word1 (last1) and word2 (last2).
  Scan the list; whenever you see one word, try to improve the
  answer using the last seen index of the other word.

Big-O:
  n := len(s)
  • Time  : O(n) single pass
  • Space : O(1) extra (just a few integers)
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -----------------------------------------------------------------------------
# User function Template for python3
# -----------------------------------------------------------------------------
class Solution:
    def shortestDistance(self, s: List[str], word1: str, word2: str) -> int:
        """
        Returns the minimum index distance between any occurrence of word1 and word2.

        Steps (each step annotated with local time/space):
          A) Same-word judge rule: if word1 == word2 -> 0          (O(1) time / O(1) space)
          B) Initialize last1, last2, ans                          (O(1) / O(1))
          C) Single scan over s:
             - At each i, update last1/last2 if a target is found  (O(1) each)
             - If counterpart exists, update ans using abs diff    (O(1) each)
             Total for loop                                        (O(n) / O(1))
          D) Convert 'no update' case to -1                        (O(1) / O(1))

        Overall: Time O(n), Space O(1).
        """
        # A) Judge rule: identical words -> distance 0.
        if word1 == word2:
            return 0

        # B) Init last seen positions; -1 means "not seen yet".
        last1 = last2 = -1
        ans = float("inf")

        # C) One pass through the words.
        for i, w in enumerate(s):
            # When we see word1, try to pair with most recent word2.
            if w == word1:
                last1 = i
                if last2 != -1:
                    d = abs(last1 - last2)
                    if d < ans:
                        ans = d
            # When we see word2, try to pair with most recent word1.
            elif w == word2:
                last2 = i
                if last1 != -1:
                    d = abs(last1 - last2)
                    if d < ans:
                        ans = d

        # D) If 'ans' never updated, return -1. Otherwise return min distance.
        return -1 if ans == float("inf") else ans


# -----------------------------------------------------------------------------
# Demo: explicit sample runs (shows input values and outputs)
# -----------------------------------------------------------------------------
def demo_on_samples() -> None:
    """
    Show correctness on several cases (including the 'same-word' judge rule).
    Each call is O(n); the total work here is small.
    """
    samples = [
        # From problem examples
        (["the", "quick", "brown", "fox", "quick"], "the", "fox", 3),
        (["geeks", "for", "geeks", "contribute", "practice"], "geeks", "practice", 2),

        # Your judge rule case: same words -> 0
        (["qz", "jm", "dv", "ejs", "of", "ejs", "qz"], "qz", "qz", 0),

        # Misc checks
        (["a", "b", "a", "c", "b", "a"], "a", "b", 1),
        (["alpha", "beta", "gamma"], "gamma", "alpha", 2),
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for s, w1, w2, expected in samples:
        out = sol.shortestDistance(s, w1, w2)  # O(n)
        print(f"s     = {s}")
        print(f"word1 = {w1!r}, word2 = {w2!r}")
        print(f"Output  : {out}")
        print(f"Expected: {expected}")
        print("-" * 60)


# -----------------------------------------------------------------------------
# Benchmark with timeit (measures full function run time)
# -----------------------------------------------------------------------------
def _bench_once(words: List[str], w1: str, w2: str) -> None:
    """Single timed invocation (O(n) work)."""
    Solution().shortestDistance(words, w1, w2)


def benchmark() -> None:
    """
    Build a sizeable random test and time the one-pass algorithm.

    Data prep (outside timing):
      - n words sampled from a vocabulary; most words will be noise.
      - word1 and word2 are picked from the vocabulary (ensures presence).
    Timed region:
      - Each run calls shortestDistance once (O(n) time).
    """
    rng = random.Random(2025)
    n = 100_000                       # size of list
    vocab = ["w"+str(i) for i in range(500)]  # vocabulary of 500 distinct words
    words = [rng.choice(vocab) for _ in range(n)]
    w1, w2 = rng.choice(vocab), rng.choice(vocab)
    # Ensure both appear at least once to avoid -1 in pathological cases.
    words[rng.randrange(n)] = w1
    words[rng.randrange(n)] = w2

    runs = 5
    total = timeit.timeit(lambda: _bench_once(words, w1, w2), number=runs)

    print("=== Benchmark (one-pass O(n)) ===")
    print(f"n (words) : {n}")
    print(f"word1     : {w1!r}, word2: {w2!r}")
    print(f"runs      : {runs}")
    print(f"total (s) : {total:.6f}")
    print(f"avg/run s : {total / runs:.6f}")
    print("-" * 60)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> None:
    # 1) Show sample inputs & outputs
    demo_on_samples()

    # 2) Benchmark with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Log Analysis / Incident Triage**
   Find the minimum time gap (by index or timestamp order) between two log event types—e.g., *“AUTH\_FAIL”* and *“LOCKOUT”*—to detect rapid sequences.

2. **NLP / Document Processing**
   In tokenized text, compute the minimal distance between two keywords to estimate contextual closeness or build features for IR/relevance models.

3. **Code Intelligence**
   For token streams (identifiers, keywords), measure proximity between important tokens (e.g., *“open”* and *“close”*) to infer pairing quality or detect anomalies.

4. **Monitoring Pipelines**
   In event streams, track how closely certain events cluster (e.g., *“error”* vs. *“retry”*) as a health metric; a short minimum distance may indicate flakiness.

