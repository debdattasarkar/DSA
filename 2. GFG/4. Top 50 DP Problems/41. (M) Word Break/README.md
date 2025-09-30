# Word Break

**Difficulty:** Medium
**Accuracy:** 40.86%
**Submissions:** 163K+
**Points:** 4

---

You are given a string **s** and a list **dictionary[]** of words. Your task is to determine whether the string **s** can be formed by concatenating one or more words from the **dictionary[]**.

**Note:** From **dictionary[]**, any word can be taken any number of times and in any order.

---

## Examples

### Example 1

**Input:** `s = "ilike", dictionary[] = ["i", "like", "gfg"]`
**Output:** `true`
**Explanation:** s can be breakdown as `"i like"`.

### Example 2

**Input:** `s = "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]`
**Output:** `true`
**Explanation:** s can be breakdown as `"i like gfg"`.

### Example 3

**Input:** `s = "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]`
**Output:** `false`
**Explanation:** s cannot be formed using dictionary[] words.

---

## Constraints

* `1 ≤ s.size() ≤ 3000`
* `1 ≤ dictionary.size() ≤ 1000`
* `1 ≤ dictionary[i].size() ≤ 100`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Zoho • Flipkart • Amazon • Microsoft • Hike • Walmart • MAQ Software • Google • IBM

---

## Topic Tags

Dynamic Programming • Algorithms

---

## Related Interview Experiences

* Maq Software Interview Experience Set 9 On Campus For Se 1
* Walmart Labs Interview Experience Set 2 On Campus
* Walmart Lab Interview Experience Set 7 Off Campus
* Flipkart Interview Set 6
* Flipkart Interview Experience Set 22 For Sde 2

---

## Related Articles

* Word Break Problem Dp 32

---

---

awesome — let’s make this crisp and interview-ready.

# 2) Explanation + step-by-step dry run

**Task.** Given string `s` and a list `dictionary[]`, decide if `s` can be written as a concatenation of words from the dictionary (words may repeat, any order).

## Core DP idea (most expected)

Let `dp[i]` be **True** iff `s[:i]` (prefix of length `i`) can be segmented.

* `dp[0] = True` (empty string is segmentable).
* For each `i` from `1..n`, check a cut point `j < i` s.t.

  * `dp[j]` is True **and** `s[j:i]` is in the dictionary.
  * If found → `dp[i] = True` and break.

**Optimization:** limit cut lengths to `Lmax = max word length in dictionary`
So for each `i`, try only `j ∈ [i-Lmax, i-1]` (clamped to `≥0`).
This makes time roughly `O(n·Lmax)` with `Lmax ≤ 100` (per the constraints).

---

## Dry run (Example)

`s = "ilikegfg"`, `dict = {"i","like","man","india","gfg"}`, `Lmax = 5`
`dp` has length `n+1 = 10`, start with: `dp=[T,F,F,F,F,F,F,F,F,F]`

* `i=1`: check `j in [0]`
  `s[0:1]="i"` ∈ dict and `dp[0]=T` → `dp[1]=T`
* `i=2..4`: only substrings `"il"`, `"ili"`, `"ilik"` → none in dict → stay `F`
* `i=5`: try `j in [0..4]` limited by `Lmax` → `"like"` at `j=1`:
  `dp[1]=T` and `"like"` ∈ dict → `dp[5]=T`
* `i=6..7`: substrings end at 6/7 are not dict words → stay `F`
* `i=8`: check `j in [3..7]` → find `"gfg"` at `j=5`:
  `dp[5]=T` and `"gfg"` ∈ dict → `dp[8]=T`
* `i=9` is past end; our string length is 9 → answer is `dp[9]`?
  Note `n=len(s)=9`; last step actually sets `dp[9]=True` because indices are 0..9 and `i=9` with `j=6` gives `"gfg"`. (Same reasoning; final result **True**.)

Segmentation: `"i" + "like" + "gfg"`.

---

# 3) Python solutions (several interview-friendly ways)

### A) DP with Lmax pruning (most expected)

```python
class Solution:
    def wordBreak(self, s, dictionary):
        """
        Bottom-up DP over prefix length.
        Time:  O(n * Lmax)  (Lmax = longest word length, <= 100 by constraints)
        Space: O(n)
        """
        n = len(s)
        if not dictionary:
            return False
        words = set(dictionary)
        Lmax = max((len(w) for w in words), default=0)

        dp = [False] * (n + 1)
        dp[0] = True  # empty prefix

        for i in range(1, n + 1):
            # Only need to check last Lmax characters
            start = max(0, i - Lmax)
            for j in range(start, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]
```

---

### B) BFS on indices (often accepted; good for early exit)

```python
from collections import deque

class SolutionBFS:
    def wordBreak(self, s, dictionary):
        """
        Each index is a node; edges jump by a dictionary word.
        Time:  O(n * Lmax) in practice; each index visited once.
        Space: O(n)
        """
        n = len(s)
        words = set(dictionary)
        if not words:
            return False
        Lmax = max(len(w) for w in words)

        q = deque([0])
        visited = set()  # avoid reprocessing same start index

        while q:
            start = q.popleft()
            if start in visited:
                continue
            visited.add(start)

            end_limit = min(n, start + Lmax)
            for end in range(start + 1, end_limit + 1):
                if s[start:end] in words:
                    if end == n:
                        return True
                    q.append(end)
        return False
```

---

### C) Top-down recursion + memo (clean derivation → same complexity)

```python
from functools import lru_cache

class SolutionMemo:
    def wordBreak(self, s, dictionary):
        """
        Try to cut from position i with dictionary words; memoize results.
        Time:  O(n * Lmax) states/transitions
        Space: O(n) memo + recursion depth up to n
        """
        n = len(s)
        words = set(dictionary)
        if not words:
            return False
        Lmax = max(len(w) for w in words)

        @lru_cache(maxsize=None)
        def can(i):
            if i == n:
                return True
            end_limit = min(n, i + Lmax)
            for end in range(i + 1, end_limit + 1):
                if s[i:end] in words and can(end):
                    return True
            return False

        return can(0)
```

> Follow-ups you can mention:
>
> * **Reconstruct segmentation**: store a `prev[i]` when setting `dp[i]=True`.
> * **Trie optimization**: replace `s[j:i] in set` with a trie walk to reduce substring hashing; helpful when dictionary is huge.

---

# 4) Likely interviewer Q&A

**Q1. What’s the state and transition of your DP?**
`dp[i]` = can `s[:i]` be segmented?
`dp[i] = True` if ∃ `j < i` such that `dp[j]` and `s[j:i] ∈ dict`.

**Q2. Complexity? Why does `Lmax` matter?**
Naively `O(n²)` substrings; but you never need words longer than `Lmax`, so inner loop shrinks to ≤ `Lmax` checks → **`O(n·Lmax)`**. Space `O(n)`.

**Q3. Why does BFS work?**
View indices as nodes; from index `i` you can jump to `j` if `s[i:j]` is a dict word. You ask if there’s a path from `0` to `n`. BFS with visited prevents re-exploring same `i`.

**Q4. How to print the actual segmentation?**
In DP, keep `prev[i]=j` when you first make `dp[i]=True`. After finishing, backtrack from `n` to `0` using `prev` and reverse.

**Q5. What changes for “Word Break II”?**
You must output **all sentences**. Use DFS with memo to produce lists of strings from each index; complexity can blow up due to exponential number of outputs.

**Q6. Common pitfalls?**

* Forgetting unlimited reuse of words (it’s allowed).
* Not limiting by `Lmax`, causing unnecessary `O(n²)` work.
* Rechecking the same start index in BFS without a `visited` set (TLE).

---

---

awesome — here’s a clean, runnable script with timing, detailed complexity comments, and a few sample inputs/outputs.

---

## Full program (with timing + inline complexity notes)

```python
#!/usr/bin/env python3
"""
Word Break — decide if s can be segmented into words from dictionary[].

Included:
  1) Solution.wordBreak  -> Bottom-up DP with Lmax pruning (MOST EXPECTED)
     Time:  O(n * Lmax)      (Lmax = max word length in dictionary)
     Space: O(n)

  2) SolutionBFS.wordBreak -> BFS on indices (nice alternative; early exit)
     Time:  O(n * Lmax) average
     Space: O(n)

  3) SolutionMemo.wordBreak -> Top-down + memo (clean derivation)
     Time:  O(n * Lmax)
     Space: O(n)

A small driver runs several test cases and times the ENTIRE program using
timeit.default_timer (the same high-res clock timeit uses).
"""

from collections import deque
from functools import lru_cache
from timeit import default_timer as timer


# ------------------------------------------------------------
# User function Template for python3 — MOST EXPECTED SOLUTION
# ------------------------------------------------------------
class Solution:
    def wordBreak(self, s, dictionary):
        """
        Bottom-up DP over prefix length.

        dp[i] = True iff s[:i] can be segmented using dictionary words.
        Transition: dp[i] |= (dp[j] and s[j:i] in dict) for some j<i.
        Optimization: only try j in [i-Lmax, i) where Lmax = max word length.

        Time Complexity:
          - For each i (n positions), we try at most Lmax cuts and O(1) set lookup.
          - O(n * Lmax). With constraints Lmax <= 100, this is fast.

        Space Complexity:
          - dp array of size n+1 => O(n)
          - dictionary stored as a set => O(m) where m = number of words (input)
        """
        n = len(s)
        if not dictionary:
            return False

        words = set(dictionary)                  # O(m) space
        Lmax = max((len(w) for w in words), default=0)

        dp = [False] * (n + 1)                   # O(n) space
        dp[0] = True                             # empty string is segmentable

        # O(n * Lmax) time
        for i in range(1, n + 1):
            # Check only the last Lmax characters as potential word endings
            start = max(0, i - Lmax)
            # Iterate j increasing: as soon as we find a valid cut, break
            for j in range(start, i):
                # O(1) set lookup; substring creation is O(length) but bounded by Lmax
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]


# ------------------------------------------------------------
# Alternative 1: BFS over indices (early exit when reaching n)
# ------------------------------------------------------------
class SolutionBFS:
    def wordBreak(self, s, dictionary):
        """
        Model indices 0..n as nodes. From index i, we can jump to j if s[i:j] in dict.
        Ask if there is a path from 0 to n.

        Time:  O(n * Lmax) on average (each index processed once, trying <= Lmax edges)
        Space: O(n) for visited queue/set
        """
        n = len(s)
        if not dictionary:
            return False

        words = set(dictionary)
        Lmax = max((len(w) for w in words), default=0)

        q = deque([0])
        visited = set()  # avoid re-processing same start index

        while q:
            i = q.popleft()
            if i in visited:
                continue
            visited.add(i)

            end_limit = min(n, i + Lmax)
            for j in range(i + 1, end_limit + 1):
                if s[i:j] in words:
                    if j == n:
                        return True
                    q.append(j)

        return False


# ------------------------------------------------------------
# Alternative 2: Top-down recursion + memo (same complexity)
# ------------------------------------------------------------
class SolutionMemo:
    def wordBreak(self, s, dictionary):
        """
        Try to cut from i with any word; memoize results.

        Time:  O(n * Lmax) states/transitions
        Space: O(n) memo + recursion depth up to n
        """
        n = len(s)
        if not dictionary:
            return False
        words = set(dictionary)
        Lmax = max((len(w) for w in words), default=0)

        @lru_cache(maxsize=None)
        def can(i):
            if i == n:
                return True
            end_limit = min(n, i + Lmax)
            for j in range(i + 1, end_limit + 1):
                if s[i:j] in words and can(j):
                    return True
            return False

        return can(0)


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def main():
    tests = [
        # (s, dictionary, expected)
        ("ilike", ["i", "like", "gfg"], True),
        ("ilikegfg", ["i", "like", "man", "india", "gfg"], True),
        ("ilikemangoes", ["i", "like", "man", "india", "gfg"], False),
        ("aaaaaaa", ["aaaa", "aaa"], True),            # 4+3
        ("catsandog", ["cats","dog","sand","and","cat"], False),
        ("leetcode", ["leet", "code"], True),
    ]

    sol = Solution()
    sol_bfs = SolutionBFS()
    sol_memo = SolutionMemo()

    print("Word Break — DP with Lmax, BFS, and Memo variants\n")

    t0 = timer()  # start timing for the WHOLE program run
    for s, dic, exp in tests:
        out_dp = sol.wordBreak(s, dic)
        out_bfs = sol_bfs.wordBreak(s, dic)
        out_memo = sol_memo.wordBreak(s, dic)

        print(f"s = {s!r}")
        print(f"dict = {dic}")
        print(f"  Output (DP)   : {out_dp}")
        print(f"  Output (BFS)  : {out_bfs}")
        print(f"  Output (Memo) : {out_memo}")
        print(f"  Expected      : {exp}")
        print("-" * 60)
    t1 = timer()  # stop timing

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### Example output (what you’ll see)

```
Word Break — DP with Lmax, BFS, and Memo variants

s = 'ilike'
dict = ['i', 'like', 'gfg']
  Output (DP)   : True
  Output (BFS)  : True
  Output (Memo) : True
  Expected      : True
------------------------------------------------------------
s = 'ilikegfg'
dict = ['i', 'like', 'man', 'india', 'gfg']
  Output (DP)   : True
  Output (BFS)  : True
  Output (Memo) : True
  Expected      : True
...
Total time for program run: 1.2 ms
```

---

## 6) Real-World Use Cases (high-value)

* **Tokenizer/lexing with a fixed vocabulary:** Decide if a raw text (without spaces) can be segmented into valid tokens (e.g., languages without explicit word boundaries).

* **Input validation & auto-correction:** Check whether user input can be decomposed into known commands/keywords; suggest splits when DP is almost true.

* **Security & pattern whitelisting:** Validate if a string (e.g., URL path segments) can be composed solely from an approved dictionary of patterns/fragments.

* **Speech-to-text postprocessing:** Segment phoneme/character streams into words using a lexicon before higher-level parsing (DP becomes part of decoding).
