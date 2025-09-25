# Search Pattern (Rabin–Karp Algorithm)

**Difficulty:** Medium
**Accuracy:** 34.53%
**Submissions:** 80K+
**Points:** 4
**Average Time:** 20m

---

Given two strings:

* A **text** string in which you want to search.
* A **pattern** string that you are looking for within the **text**.

Return all positions (**1-based indexing**) where the **pattern** occurs as a substring in the **text**. If the pattern does not occur, return an empty list.

All characters in both strings are lowercase English letters (**a** to **z**).

---

## Examples

### Example 1

**Input:** `text = "birthdayboy"`, `pattern = "birth"`
**Output:** `[1]`
**Explanation:** The string `"birth"` occurs at index **1** in `text`.

### Example 2

**Input:** `text = "geeksforgeeks"`, `pattern = "geek"`
**Output:** `[1, 9]`
**Explanation:** The string `"geek"` occurs twice in `text`, once starting at index **1** and the other at index **9**.

---

## Constraints

* `1 ≤ text.size() ≤ 5 * 10^5`
* `1 ≤ pattern.size() ≤ text.size()`

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Microsoft

---

## Topic Tags

* Strings
* Pattern Searching
* Data Structures
* Algorithms

---

## Related Articles

* [Rabin Karp Algorithm For Pattern Searching](https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/)

---

---

You’re right—my Rabin–Karp returned **1-based** indices (`i+1`).
Your judge expects **0-based** indices (as in your screenshot: expected `[0]` for `"birthdayboy"` / `"birth"`).
That’s the whole bug (an off-by-one when pushing matches).

Here’s a fixed, clean Rabin–Karp that returns **0-based** positions, plus a tiny toggle if you ever need 1-based later.

---

### Why your output was wrong (quick dry run)

`text="birthdayboy"`, `pattern="birth"`

* First window is `text[0:5] = "birth"`. Hashes match → substring check passes.
* With 1-based push we appended `0+1 = 1` → `[1]` (wrong for your judge).
* Correct is to append `0` → `[0]`.

---

Here’s a Rabin–Karp solution that matches your required format exactly and returns **0-based** indices (as your judge expects).

```python
class Solution:
    def rabinKarp(self, text, pattern):
        n, m = len(text), len(pattern)
        if m == 0 or m > n:
            return []

        # Rolling-hash parameters
        B = 256          # base (covers lowercase ASCII)
        M = 10**9 + 7    # large prime modulus

        # Precompute B^(m-1) % M to remove the leftmost char in O(1)
        power = pow(B, m - 1, M)

        # Initial hashes for pattern and first window in text
        ph = 0  # pattern hash
        th = 0  # text window hash
        for i in range(m):
            ph = (ph * B + ord(pattern[i])) % M
            th = (th * B + ord(text[i])) % M

        res = []

        # Slide over all windows
        for i in range(n - m + 1):
            # On hash match, verify to avoid false positives
            if ph == th and text[i:i + m] == pattern:
                res.append(i)  # return 0-based index

            # Roll the hash: remove left char, add right char
            if i < n - m:
                left = (ord(text[i]) * power) % M
                th = (th - left) % M
                th = (th * B + ord(text[i + m])) % M

        return res
```

**Complexity**

* Time: $O(n + m)$ expected (rolling hash + verification only on hash matches).
* Space: $O(1)$ auxiliary (excluding the output list).


### Corrected Rabin–Karp (0-based)

```python
class Solution:
    def rabinKarp(self, text: str, pattern: str, one_based: bool = False):
        n, m = len(text), len(pattern)
        if m == 0 or m > n:
            return []

        # Base and modulus
        B = 256           # covers lowercase safely
        M = 10**9 + 7     # large prime to reduce collisions

        # Precompute B^(m-1) % M for removing the leading char
        power = pow(B, m - 1, M)

        # Hash helpers
        def hval(c): return ord(c)          # map char to int (ASCII)

        # Initial hashes: pattern and text window [0:m]
        ph = 0
        th = 0
        for i in range(m):
            ph = (ph * B + hval(pattern[i])) % M
            th = (th * B + hval(text[i])) % M

        ans = []
        for i in range(n - m + 1):
            # If the hashes match, verify to avoid false positives
            if ph == th and text[i:i + m] == pattern:
                ans.append(i + (1 if one_based else 0))

            # Roll the hash to the next window (unless we're at the end)
            if i < n - m:
                left = (hval(text[i]) * power) % M
                th = (th - left) % M               # remove left char
                th = (th * B + hval(text[i + m])) % M  # add right char

        return ans
```

**Complexity:**

* Time: `O(n + m)` expected (rolling hash + at most `O(k*m)` substring checks where `k` is rare collisions)
* Space: `O(1)` (output list aside)

> If your platform truly wants **1-based** indices (as in some GFG problems), just call `rabinKarp(text, pattern, one_based=True)` or replace `ans.append(i + (1 if one_based else 0))` with `ans.append(i+1)`.

---

### Brute-force (for completeness / interview contrast)

```python
class SolutionBF:
    def rabinKarp(self, text: str, pattern: str):
        n, m = len(text), len(pattern)
        if m == 0 or m > n:
            return []
        out = []
        for i in range(n - m + 1):
            if text[i:i+m] == pattern:   # Python slice compare
                out.append(i)            # 0-based
        return out
```

* Time: `O(n*m)` worst case
* Space: `O(1)`

---

### Tiny step-by-step dry run (hash roll idea)

For `text="birthday"`, `pattern="birth"` (`m=5`)

* Compute `ph = hash("birth")`, `th = hash("birth")` for `text[0:5]`
* `ph == th` and slice equal → record `0`.
* Roll: remove `'b'` (at `i=0`), multiply by `B`, add `'d'` (at `i+m`) → new `th` equals hash for `"irthd"`.
* Continue until end.

---

### Quick interviewer Q&A

* **Q:** Why still verify `text[i:i+m] == pattern` after hash match?
  **A:** To avoid false positives from rare hash collisions.

* **Q:** Why `B=256` and `M=1e9+7`?
  **A:** `B=256` safely spans lowercase ASCII; a large prime modulus reduces collisions and prevents overflow.

* **Q:** How to switch between 0-based and 1-based results?
  **A:** Push `i` for 0-based, `i+1` for 1-based (or keep a `one_based` toggle).

* **Q:** When is brute-force acceptable?
  **A:** Short strings, or when simplicity is preferred and constraints are tiny.

---

---

Here’s a complete, interview-ready **Rabin–Karp** program that returns **0-based** match positions, includes a tiny toggle for 1-based (if your judge requires it), prints outputs for sample inputs, and measures runtime using `timeit`.

```python
# Rabin–Karp: find all occurrences of `pattern` in `text`
# Returns 0-based indices by default (toggle to 1-based via one_based=True)

from timeit import timeit


class Solution:
    def rabinKarp(self, text: str, pattern: str, one_based: bool = False):
        """
        Expected time: O(n + m) for rolling hash + a few O(m) verifications on rare collisions.
        Worst-case time: O(n*m) if every window collides (very unlikely with large prime modulus).
        Space: O(1) auxiliary (excluding output list).
        """
        n, m = len(text), len(pattern)

        # ---- Guard rails -----------------------------------------------------
        # O(1) time, O(1) space
        if m == 0 or m > n:
            return []

        # ---- Parameters for rolling hash -------------------------------------
        # O(1) time, O(1) space
        B = 256           # base (covers lowercase ASCII safely)
        M = 10**9 + 7     # large prime modulus to avoid overflow/collisions

        # Precompute B^(m-1) % M for removing the leading char when the window rolls
        # Time: O(log m) via fast pow (Python's pow uses exponentiation by squaring)
        # Space: O(1)
        power = pow(B, m - 1, M)

        # ---- Helper to turn char into an int ---------------------------------
        # O(1) time
        def hval(c): 
            return ord(c)

        # ---- Initial hashes for pattern and the first window text[0:m] -------
        # Time: O(m), Space: O(1)
        ph = 0   # pattern hash
        th = 0   # text window hash
        for i in range(m):
            ph = (ph * B + hval(pattern[i])) % M
            th = (th * B + hval(text[i])) % M

        ans = []  # output indices

        # ---- Slide the window over text, check matches, roll hash ------------
        # Time: O(n - m + 1) windows; each step does O(1) hash math + O(m) verify only on hash match
        for i in range(n - m + 1):
            # Compare hashes; if equal, verify substring (to avoid rare false positives)
            # Time: O(m) only on hash equality (rare)
            if ph == th and text[i:i + m] == pattern:
                ans.append(i + (1 if one_based else 0))

            # Roll the window: remove left char, add next right char
            # Time: O(1), Space: O(1)
            if i < n - m:
                left = (hval(text[i]) * power) % M
                th = (th - left) % M                    # remove left char
                th = (th * B + hval(text[i + m])) % M   # add right char

        return ans


# ----------------------------- Brute Force (reference) -----------------------------
class SolutionBrute:
    def rabinKarp(self, text: str, pattern: str):
        """
        Pure brute force, for comparison.
        Time: O(n*m) worst-case
        Space: O(1) auxiliary (excluding output).
        """
        n, m = len(text), len(pattern)
        if m == 0 or m > n:
            return []
        out = []
        for i in range(n - m + 1):              # O(n)
            if text[i:i + m] == pattern:        # O(m) compare
                out.append(i)                   # 0-based
        return out


# ---------------------------------- Demo / Timing ----------------------------------
if __name__ == "__main__":
    sol = Solution()
    brute = SolutionBrute()

    tests = [
        # (text, pattern, expected 0-based indices)
        ("birthdayboy", "birth", [0]),
        ("geeksforgeeks", "geek", [0, 8]),
        ("aaaaa", "aa", [0, 1, 2, 3]),
        ("abcabcabc", "cab", [2, 5]),
        ("abcdefgh", "xyz", []),
    ]

    print("Rabin–Karp (0-based results):")
    for text, pattern, exp in tests:
        got = sol.rabinKarp(text, pattern)  # 0-based by default
        print(f"text={text!r}, pattern={pattern!r} -> {got}  (expected {exp})")

    # Example if your judge needs 1-based: pass one_based=True
    print("\nRabin–Karp (1-based results) for a single example:")
    print(sol.rabinKarp("geeksforgeeks", "geek", one_based=True))  # -> [1, 9]

    # -------------------- Timing with timeit --------------------
    # We’ll time a slightly larger sample to show expected speed.
    big_text = "geeksforgeeks" * 1000          # length 13,000
    pattern = "geek"                            # length 4

    # Time the optimized Rabin–Karp
    rk_time = timeit(lambda: sol.rabinKarp(big_text, pattern), number=200)
    # Time the brute-force for contrast
    bf_time = timeit(lambda: brute.rabinKarp(big_text, pattern), number=200)

    print("\nTiming on a larger input (200 runs):")
    print(f"Rabin–Karp: {rk_time:.4f} s")
    print(f"Brute force: {bf_time:.4f} s")
```

---

## Real-World Use Cases (just the crucial ones)

1. **Text search in editors / IDEs**
   Fast substring search in documents, logs, and codebases where many queries and large texts are common.

2. **Plagiarism / duplicate detection (pre-filter)**
   Hashing substrings to quickly spot potential matches before doing a precise (but slower) comparison.

3. **Network intrusion / log scanning**
   Real-time scanning of logs or network payloads for known signatures (patterns) with minimal memory.

4. **DNA / protein subsequence scanning (toy scale)**
   When approximate matching or heavy indexing (suffix arrays/trees) is overkill, rolling hashes provide quick exact checks.
