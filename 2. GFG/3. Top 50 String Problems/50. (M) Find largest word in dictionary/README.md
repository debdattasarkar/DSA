# Find largest word in dictionary

**Difficulty:** Medium
**Accuracy:** 43.54%
**Submissions:** 22K+
**Points:** 4

---

## Problem Statement

Given a string `s` and a string dictionary `d`, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the **smallest lexicographical order**. If there is no possible result, return the **empty string**.

---

## Examples

### Example 1

**Input:**
`d = {"ale", "apple", "monkey", "plea"},  s = "abpcplea"`
**Output:**
`"apple"`
**Explanation:** After deleting `"b"`, `"c"`, `"a"` `s` became `"apple"` which is present in `d`.

---

### Example 2

**Input:**
`d = {"a", "b", "c"},  s = "abpcplea"`
**Output:**
`"a"`
**Explanation:** After deleting `"b"`, `"p"`, `"c"`, `"p"`, `"l"`, `"e"`, `"a"` `s` became `"a"` which is present in `d`.

---

## Expected Time Complexity

`O(n * x)`

## Expected Auxiliary Space

`O(x)` where `x` is the length of the string in `d`.

---

## Constraints

* `1 ≤ n, x ≤ 10^3`

---

## Company Tags

* Walmart
* Google

---

## Topic Tags

* Strings
* Data Structures
* Algorithms

---

## Related Articles

* [Find Largest Word Dictionary Deleting Characters Given String](https://www.geeksforgeeks.org/find-largest-word-dictionary-deleting-characters-given-string/)

---

---

awesome—let’s make this one interview-ready.

---

# 2) Explanation + step-by-step dry run

## Problem recap

You’re given a string `S` and a dictionary `d` (list of words).
Goal: return the **longest** word in `d` that’s a **subsequence** of `S`.
If multiple words share the maximum length, return the **lexicographically smallest** among them.
If none match, return `""`.

> A word `w` is a subsequence of `S` if you can delete some characters from `S` (without reordering the rest) to obtain `w`.

---

## Approaches

### A) Two-pointer check per word (simple & common)

For each word `w` in `d`, walk both `S` and `w` with two pointers.
If `w[j] == S[i]`, advance `j`; always advance `i`.
If `j` reaches `len(w)`, then `w` is a subsequence.

* Time: `O(|S|)` per word ⇒ `O(|S| * |d|)` (worst).
* Space: `O(1)`.

### B) Preprocess `S` into a “next occurrence” table (faster if many words)

Build `next_pos[i][c]` = index of the first occurrence of character `c` **at or after** position `i` in `S` (or `-1` if none).
Then to test a word `w`, start from `pos = 0` and for each char `ch` jump to `pos = next_pos[pos][ch] + 1`. If at any step you get `-1`, `w` is not a subsequence.

* Preprocessing: `O(26 * |S|)` time, `O(26 * |S|)` space.
* Each word check: `O(len(w))`.
* Total: `O(26|S| + Σ len(w))`.

### Tie-breaking

Maintain a current best `best`.
Replace `best` with a candidate `w` when:

* `len(w) > len(best)`, or
* `len(w) == len(best)` **and** `w < best` (lexicographically smaller).

---

## Dry run (Example 1)

`S = "abpcplea"`, `d = {"ale","apple","monkey","plea"}`

Using two-pointer:

* `"ale"`: match `a`(S[0]) → `l`(S[3]) → `e`(S[7]) ⇒ subsequence (len 3). `best = "ale"`.
* `"apple"`: `a`(0) → `p`(2) → `p`(3) → `l`(5) → `e`(7) ⇒ subsequence (len 5). `best = "apple"`.
* `"monkey"`: fails quickly (chars not found in order).
* `"plea"`: `p`(2) → `l`(5) → `e`(7) → `a`(?) must come **after** 7, but only `a` at 0 ⇒ fail.
  Answer: `"apple"`.

---

# 3) Python solutions (multiple ways, interview-friendly)

All follow the required signature:

```python
#User function Template for python3
class Solution:
    def findLongestWord (ob, S, d):
        # code here 
```

## A) Simple two-pointer scan per word (clean & expected)

```python
#User function Template for python3
class Solution:
    def findLongestWord (ob, S, d):
        """
        Check each dictionary word with a two-pointer subsequence test.
        Time:  O(|S| * |d|) worst-case (each word scans S once)
        Space: O(1)
        """
        def is_subseq(word: str, s: str) -> bool:
            i = j = 0
            n, m = len(s), len(word)
            # walk s; advance j when we match word[j]
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == m

        best = ""
        for w in d:
            if is_subseq(w, S):
                # choose longer; on tie choose lexicographically smaller
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best
```

## B) Optimized with “next occurrence” automaton (great when |d| is big)

```python
#User function Template for python3
class SolutionNext:
    def findLongestWord (ob, S, d):
        """
        Precompute next_pos table: next_pos[i][c] = first index >= i where char c occurs, else -1.
        Checking each word becomes O(len(word)).
        Time:  O(26*|S| + sum(len(word) for word in d))
        Space: O(26*|S|)
        """
        n = len(S)
        A = 26
        # next_pos has n+1 rows; row n is all -1 (no chars after end)
        next_pos = [[-1]*A for _ in range(n+1)]
        # Fill from the end; copy row i+1 then set S[i]
        for i in range(n-1, -1, -1):
            # copy previous row (O(26))
            nxt = next_pos[i+1][:]
            nxt[ord(S[i]) - 97] = i
            next_pos[i] = nxt

        def is_subseq(word: str) -> bool:
            pos = 0  # current index in S we can start matching from
            for ch in word:
                idx = next_pos[pos][ord(ch) - 97]
                if idx == -1:
                    return False
                pos = idx + 1
                if pos > n:  # optional safety
                    return False
            return True

        best = ""
        for w in d:
            if is_subseq(w):
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best
```

## C) Early-exit heuristic: sort dictionary by desirability, pick first subsequence

```python
#User function Template for python3
class SolutionSorted:
    def findLongestWord (ob, S, d):
        """
        Heuristic: sort by (-length, lex) then return first w that is a subsequence.
        Works well in practice; worst-case still O(|S|*|d|).
        """
        def is_subseq(word: str, s: str) -> bool:
            i = j = 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == m

        # longest first; for equal length, lexicographically smallest first
        d_sorted = sorted(d, key=lambda w: (-len(w), w))
        for w in d_sorted:
            if is_subseq(w, S):
                return w
        return ""
```

> In an interview, mention A first (simple & correct), then briefly note B as an optimization when the dictionary is large or reused many times.

---

# 4) Interview Q&A (the ones they usually probe)

**Q1. How do you test if a word is a subsequence of `S`?**
*A:* Use two pointers over `S` and the word. Advance the word pointer on matches; if it reaches the end, it’s a subsequence. `O(|S|)` time, `O(1)` space.

**Q2. How do you break ties between words of the same length?**
*A:* Choose the **lexicographically smallest**. In code:
`if len(w) > len(best) or (len(w) == len(best) and w < best): best = w`.

**Q3. Can you improve over `O(|S| * |d|)`?**
*A:* Yes. Precompute a “next occurrence” table for `S` in `O(26|S|)` and then check each word in `O(len(word))`. Total `O(26|S| + Σ len(word))`.

**Q4. What if we repeatedly get queries on the same `S` with different dictionaries?**
*A:* Build the `next_pos` automaton once and reuse it across queries—huge savings.

**Q5. Edge cases?**
*A:*

* If no word matches, return `""`.
* Duplicates in `d` don’t matter—comparison keeps the best.
* Empty strings in `d` are valid subsequences of any `S` but will lose to any nonempty match unless all fail.

**Q6. Space/time trade-offs?**
*A:* The automaton uses `O(26|S|)` memory (good for lowercase only). For arbitrary Unicode, switch to a hashmap per row or to the two-pointer method.

**Q7. Why sort `d` by (-len, lex) in approach C?**
*A:* It lets us early-exit once we find the first match—the one we’d return anyway—often saving many checks in practice.

---

---

perfect — here’s a **ready-to-run, interview-style program** for **“Find largest word in dictionary (by deleting chars)”** that:

* reads inputs,
* solves the task **three ways** (baseline two-pointer, sorted early-exit, and “next-occurrence automaton”),
* prints outputs, and
* **times each** using `timeit`.

I’ve included tight **time/space complexity notes** inline.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Find largest word in dictionary by deleting characters of S
#
# Return the longest word in d that is a subsequence of S.
# If multiple have the same length, return the lexicographically
# smallest. If none, return "".
#
# Methods:
#   1) Two-pointer check per word (baseline; expected in interviews)
#   2) Early-exit: sort d by (-len, lex) and return first match
#   3) Next-occurrence automaton on S (fast when |d| is large)
#
# Input (stdin):
#   Line 1: S
#   Line 2: Either
#           - integer M (number of words), followed by lines of words
#             (space/comma separated) until M words are read, OR
#           - the dictionary words directly (space/comma separated)
#
# Output:
#   - Echo input preview
#   - Answer from each method
#   - Per-method timing via timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit

# -------------------- User-function Template ----------------
class Solution:
    def findLongestWord (ob, S, d):
        """
        Baseline: scan each dictionary word with a two-pointer subsequence test.
        Tie-break: prefer longer, then lexicographically smaller.

        Time:  O(|S| * |d|) worst case
               (each word may scan S once with two pointers)
        Space: O(1) beyond input
        """
        def is_subseq(word: str, s: str) -> bool:
            # Two-pointer check in O(|s|) time, O(1) space
            i = j = 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == m

        best = ""
        for w in d:
            if is_subseq(w, S):
                # Update if strictly longer, or same length but lexicographically smaller
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best


# ------------------ Early-exit (sorted dictionary) ----------
class SolutionSorted:
    def findLongestWord (ob, S, d):
        """
        Sort dictionary by desirability: longer first, then lexicographically
        smaller. Return the first word that is a subsequence.

        Time:  O(|d| log |d|) for sort + O(Σ checked |S|) for checks
               Worst is still O(|S| * |d|) but often much faster in practice.
        Space: O(|d|) for sort
        """
        def is_subseq(word: str, s: str) -> bool:
            i = j = 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == m

        # Longest first; tie -> lexicographically smallest first
        d_sorted = sorted(d, key=lambda w: (-len(w), w))
        for w in d_sorted:
            if is_subseq(w, S):
                return w
        return ""


# ----------- Next-occurrence automaton (preprocess S) --------
class SolutionNext:
    def findLongestWord (ob, S, d):
        """
        Precompute next_pos[i][c] = first index >= i where char c occurs, else -1.
        Then checking a word is O(len(word)) by jumping through S with next_pos.

        Preprocess:  O(26 * |S|) time, O(26 * |S|) space  (lowercase assumption)
        Query cost:  O(len(word))
        Total:       O(26|S| + Σ len(word))
        """
        n = len(S)
        A = 26
        # next_pos has n+1 rows; row n is all -1 (no chars after end)
        next_pos = [[-1] * A for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            # copy row i+1 (O(26)) then set S[i]
            row = next_pos[i + 1][:]
            row[ord(S[i]) - 97] = i
            next_pos[i] = row

        def is_subseq(word: str) -> bool:
            pos = 0
            for ch in word:
                idx = next_pos[pos][ord(ch) - 97]
                if idx == -1:
                    return False
                pos = idx + 1
                if pos > n:
                    return False
            return True

        best = ""
        for w in d:
            if is_subseq(w):
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best


# ----------------------------- I/O ---------------------------
def _read_inputs():
    lines = [ln.strip() for ln in sys.stdin.readlines() if ln.strip() != ""]
    if not lines:
        print("Please provide input.\nExample:\nabpcplea\nale apple monkey plea")
        sys.exit(0)

    S = lines[0]
    d = []

    # Flexible parsing for dictionary:
    # If the second non-empty line is an integer M, read until we collect M words.
    # Otherwise, treat the next line as the words (space/comma separated).
    if len(lines) >= 2:
        second = lines[1]
        try:
            M = int(second)
            idx = 2
            while idx < len(lines) and len(d) < M:
                tokens = lines[idx].replace(",", " ").split()
                d.extend(tokens)
                idx += 1
            d = d[:M]
        except ValueError:
            d = second.replace(",", " ").split()
    return S, d

def _preview(label, s, limit=80):
    if isinstance(s, list):
        # preview first few words
        joined = " ".join(s[:10])
        more = "" if len(s) <= 10 else f" ... (+{len(s)-10} more)"
        return f"{label} ({len(s)}): {joined}{more}"
    if len(s) <= limit:
        return f"{label} ({len(s)}): {s}"
    return f"{label} ({len(s)}): {s[:limit]}...{s[-10:]}"


# ----------------------------- Main --------------------------
def main():
    S, d = _read_inputs()
    print(_preview("S", S))
    print(_preview("d", d))
    print()

    base = Solution()
    sorted_solver = SolutionSorted()
    next_solver = SolutionNext()

    # Time each solution once via timeit.timeit(number=1)
    t_base = timeit.timeit(lambda: base.findLongestWord(S, d), number=1)
    ans_base = base.findLongestWord(S, d)

    t_sorted = timeit.timeit(lambda: sorted_solver.findLongestWord(S, d), number=1)
    ans_sorted = sorted_solver.findLongestWord(S, d)

    t_next = timeit.timeit(lambda: next_solver.findLongestWord(S, d), number=1)
    ans_next = next_solver.findLongestWord(S, d)

    print("Two-pointer (baseline) answer :", ans_base)
    print("Time (ms): {:.3f}".format(t_base * 1000.0))
    print()
    print("Sorted early-exit answer     :", ans_sorted)
    print("Time (ms): {:.3f}".format(t_sorted * 1000.0))
    print()
    print("Next-occurrence answer       :", ans_next)
    print("Time (ms): {:.3f}".format(t_next * 1000.0))

    agree = (ans_base == ans_sorted == ans_next)
    print("\nAll methods agree ✔" if agree else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
# Example 1 (dictionary on one line)
python3 find_largest_word.py
abpcplea
ale apple monkey plea
```

**Output (timings vary):**

```
S (8): abpcplea
d (4): ale apple monkey plea

Two-pointer (baseline) answer : apple
Time (ms): 0.110

Sorted early-exit answer     : apple
Time (ms): 0.073

Next-occurrence answer       : apple
Time (ms): 0.060

All methods agree ✔
```

```bash
# Example 2 (M then words)
python3 find_largest_word.py
abpcplea
3
a b c
```

**Output:**

```
S (8): abpcplea
d (3): a b c

Two-pointer (baseline) answer : a
Time (ms): 0.055

Sorted early-exit answer     : a
Time (ms): 0.038

Next-occurrence answer       : a
Time (ms): 0.036

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

1. **Type-ahead / autocomplete:** given the user’s typed characters `S`, pick the longest dictionary entry that can be formed as a subsequence (with tie-breaks), or use the automaton to score many candidates fast.

2. **Command palette / fuzzy finders (IDE, CLI tools):** quickly verify whether a command/file path matches typed letters in order; “next-occurrence” tables accelerate massive candidate sets.

3. **Accessibility / T9-like input:** map reduced key sequences to valid dictionary words where characters appear in order (subsequence), prioritizing longest/readable options.

4. **DNA/protein motif search (exact order, gaps allowed):** check presence of motifs as subsequences in long sequences repeatedly; precomputing jumps speeds up many queries.
