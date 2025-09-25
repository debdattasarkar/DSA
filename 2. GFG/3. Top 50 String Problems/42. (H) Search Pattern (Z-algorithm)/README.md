# Search Pattern (Z-algorithm) 🧩

**Difficulty:** Hard
**Accuracy:** 51.7%
**Submissions:** 13K+
**Points:** 8

Given two strings, one is a text string `txt` and the other is a pattern string `pat`. The task is to return the **indexes of all the occurrences** of the pattern string in the text string. **Use 0-based indexing** while returning the indices.
**Note:** Return an empty list in case of no occurrences of pattern.

---

## Examples

**Input:** `txt = "geeksforgeeks"`, `pat = "geek"`
**Output:** `[0, 8]`
**Explanation:** The pattern `"geek"` occurs at **Index 0** (characters 0–3) and **Index 8** (characters 8–11).

---

**Input:** `txt = "abesdu"`, `pat = "edu"`
**Output:** `[]`
**Explanation:** There's no substring `"edu"` present in `txt`.

---

## Constraints

* `1 ≤ txt.size() ≤ 10^5`
* `1 ≤ pat.size() ≤ txt.size()`
* Both the strings consist of lowercase English alphabets.

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* `Microsoft`

---

## Topic Tags

* `Strings` • `Pattern Searching` • `Data Structures` • `Algorithms`

---

## Related Articles

[Z Algorithm Linear Time Pattern Searching Algorithm](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/)

---

---

Here’s a crisp, interview-ready package for **Search Pattern (Z-algorithm)**.

---

## 2) Explanation + step-by-step dry run

### Goal

Return all 0-based indices `i` in `txt` where `txt[i : i+len(pat)] == pat`.

### Z-algorithm idea (why it’s fast)

1. Build `S = pat + sep + txt`, where `sep` is a character that **can’t** appear in either string (for lowercase inputs we can safely use `'{'`).
2. Compute the **Z array** for `S`. `Z[i]` = length of the longest substring starting at `i` that matches the prefix of `S`.
3. Every position `i` where `Z[i] == len(pat)` indicates a full match of `pat` starting at:

   ```
   start_in_txt = i - (len(pat) + 1)
   ```

   (subtract pattern length and separator).

### Dry run (txt = "geeksforgeeks", pat = "geek")

* `pat = "geek"` (m = 4), `txt = "geeksforgeeks"` (n = 13).
* `S = "geek{geeksforgeeks"`.
* Z array over `S` compares each suffix of `S` with the prefix `"geek{..."`

  * At index `i = 5` (`S[5]` points at `'g'` of `txt`), we find `Z[5] = 4` (matches `"geek"`).
    → start = `5 - (4 + 1) = 0`
  * Later at `i = 13`, `Z[13] = 4` again.
    → start = `13 - 5 = 8`
* Output: `[0, 8]`.

---

## 3) Optimized codes (multiple ways)

### A) Z-algorithm (linear time, most expected here)

```python
class Solution:
    def search(self, txt, pat):
        # Edge cases
        if not pat or len(pat) > len(txt):
            return []
        
        # Separator not in lowercase 'a'-'z' (safe per constraints)
        sep = '{'
        S = pat + sep + txt
        
        # ---- Z-array computation: O(|S|)
        n = len(S)
        Z = [0] * n
        L = R = 0  # current Z-box [L, R]
        
        for i in range(1, n):
            if i <= R:
                # Use previously computed values when inside Z-box
                Z[i] = min(R - i + 1, Z[i - L])
            # Extend by direct comparisons
            while i + Z[i] < n and S[Z[i]] == S[i + Z[i]]:
                Z[i] += 1
            # Update Z-box if we extended past R
            if i + Z[i] - 1 > R:
                L, R = i, i + Z[i] - 1
        
        # ---- Collect matches
        m = len(pat)
        ans = []
        for i in range(m + 1, n):  # positions inside txt region
            if Z[i] == m:
                ans.append(i - (m + 1))  # convert to index in txt
        return ans
```

**Why it’s good:**

* Time: `O(n + m)`
* Space: `O(n + m)` for `S` and `Z`.
* Typical interview “Z-algorithm pattern search” solution.

---

### B) KMP (prefix function / LPS) – another optimal classic

```python
class Solution:
    def search(self, txt, pat):
        if not pat or len(pat) > len(txt):
            return []
        
        # Build LPS (Longest Prefix Suffix) array for pat
        def build_lps(p):
            lps = [0] * len(p)
            j = 0
            for i in range(1, len(p)):
                while j > 0 and p[i] != p[j]:
                    j = lps[j - 1]
                if p[i] == p[j]:
                    j += 1
                    lps[i] = j
            return lps
        
        lps = build_lps(pat)
        res = []
        i = j = 0  # i over txt, j over pat
        
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == len(pat):
                    res.append(i - j)  # match ends at i-1
                    j = lps[j - 1]     # continue searching
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return res
```

**Why it’s good:**

* Time: `O(n + m)`, Space: `O(m)`.
* Very common in interviews; shows mastery of prefix-function thinking.

---

### C) Naïve sliding window (simple but slower)

```python
class Solution:
    def search(self, txt, pat):
        m, n = len(pat), len(txt)
        if m == 0 or m > n:
            return []
        out = []
        for i in range(n - m + 1):
            # Compare the window with pattern
            if txt[i:i+m] == pat:
                out.append(i)
        return out
```

**Why it’s still useful:**

* Clear and easy to code.
* Time: `O(n*m)` worst-case, Space: `O(1)` (ignoring output).

---

## 4) Interview Q&A (typical discussion points)

**Q1. Why does the Z-algorithm work for pattern search?**
Because `Z[i]` tells how many characters from the **global prefix** match starting at `i`. With `S = pat + sep + txt`, every position in `txt` is compared against the prefix `pat`. If `Z[i]` equals `len(pat)`, we found a full match.

**Q2. How do you choose the separator `sep`?**
Pick a character that’s guaranteed not to appear in either string. With constraints limited to lowercase letters, `'{'` (ASCII 123) is safe. More generally, scan and pick any missing character.

**Q3. What’s the complexity of Z vs KMP?**
Both are linear: `O(n + m)`. Z uses an auxiliary concatenated string; KMP uses an LPS array.

**Q4. What if the pattern is empty or longer than the text?**

* Empty pattern: in many APIs you might return all positions or `[]`. Here we return `[]` per typical competitive-programming expectations unless otherwise specified.
* Pattern longer than text: return `[]`.

**Q5. Can Z return false positives due to hash or anything probabilistic?**
No. Z is purely character comparisons. (You’re thinking of Rabin-Karp hashing—different algorithm.)

**Q6. Space considerations?**
Z stores `S` and `Z` ⇒ `O(n + m)`. KMP stores `lps` ⇒ `O(m)`.

**Q7. When would you prefer KMP over Z (or vice-versa)?**

* If you already have a robust `lps` template, KMP is concise.
* If you need **other** prefix-matching queries on the same string, Z is often more natural.

---

---

Awesome — here’s a **complete, runnable program** for the Z-algorithm version of pattern search, with:

* rich inline comments (including per-step time/space notes),
* a small driver (`__main__`) that prints example inputs/outputs, and
* a quick runtime measurement using `time.perf_counter()`.

You can paste this into a file and run it directly.

```python
"""
Search Pattern (Z-algorithm)
----------------------------

Given two strings: text (txt) and pattern (pat), return *all* 0-based indices
where pat occurs in txt. If none occur, return [].

This file includes:
- Z-algorithm solution in the required class/method signature:
    class Solution:
        def search(self, txt, pat): ...
- A tiny main() that demonstrates inputs/outputs and
  prints a simple wall-clock runtime for the whole search.

Why Z?
- Linear time O(n + m) and simple to adapt for "pattern in text" by
  building S = pat + sep + txt and computing Z over S.

Notation below:
- n := len(txt), m := len(pat), N := len(S) = n + m + 1
"""

from time import perf_counter


class Solution:
    def search(self, txt: str, pat: str):
        """
        Return all 0-based starting indices where `pat` occurs in `txt`.

        Steps:
        1) Build S = pat + sep + txt.              # Time: O(n + m), Space: O(n + m)
        2) Compute Z array for S.                   # Time: O(n + m), Space: O(n + m)
        3) For i in S, if Z[i] == m, record match  # Time: O(n),     Space: O(1) (excluding output)

        Total time:  O(n + m)
        Total space: O(n + m)
        """
        # ---- Guard cases (O(1))
        if not pat or len(pat) > len(txt):
            return []

        # Pick a separator that we guarantee does not appear in txt/pat.
        # With constraints restricted to lowercase, '{' (ASCII 123) is safe.
        sep = '{'

        # ---- Build the concatenated string S (O(n + m) time/space)
        S = pat + sep + txt
        N = len(S)

        # ---- Compute Z array in O(N)
        # Z[i] = length of the longest substring starting at i that matches the prefix of S
        Z = [0] * N
        L = R = 0  # current [L, R] Z-box

        # Z[0] is always 0 by convention for this problem
        for i in range(1, N):
            # If i is inside the current Z-box, initialize Z[i] from the mirrored value
            if i <= R:
                Z[i] = min(R - i + 1, Z[i - L])

            # Try to extend the match greedily
            while i + Z[i] < N and S[Z[i]] == S[i + Z[i]]:
                Z[i] += 1

            # If we extended past R, update the Z-box
            if i + Z[i] - 1 > R:
                L, R = i, i + Z[i] - 1

        # ---- Extract matches (O(n))
        m = len(pat)
        base = m + 1  # skip the pattern + separator region
        ans = []
        for i in range(base, N):
            # If the prefix length equals m, we found a full match at txt index (i - base)
            if Z[i] == m:
                ans.append(i - base)
        return ans


def _pretty_print_case(txt: str, pat: str, result):
    print(f"txt = {txt!r}")
    print(f"pat = {pat!r}")
    print(f"matches (0-based) = {result}")
    print("-" * 40)


def main():
    sol = Solution()

    # --- Demo test cases (from statement + a classic overlapping example)
    cases = [
        ("geeksforgeeks", "geek"),  # -> [0, 8]
        ("abesdu", "edu"),          # -> []
        ("aaaaa", "aa"),            # -> [0, 1, 2, 3]
    ]

    # Run once and print outputs
    print("Outputs:")
    for txt, pat in cases:
        res = sol.search(txt, pat)
        _pretty_print_case(txt, pat, res)

    # --- Quick timing: measure total time to run all above queries a few thousand times
    loops = 5000
    start = perf_counter()
    for _ in range(loops):
        for txt, pat in cases:
            sol.search(txt, pat)
    elapsed = perf_counter() - start

    print(f"Ran {len(cases)} queries x {loops:,} loops "
          f"(total calls: {len(cases) * loops:,}) in {elapsed:.4f} s")


if __name__ == "__main__":
    main()
```

### Sample run (what you should see)

```
Outputs:
txt = 'geeksforgeeks'
pat = 'geek'
matches (0-based) = [0, 8]
----------------------------------------
txt = 'abesdu'
pat = 'edu'
matches (0-based) = []
----------------------------------------
txt = 'aaaaa'
pat = 'aa'
matches (0-based) = [0, 1, 2, 3]
----------------------------------------
Ran 3 queries x 5,000 loops (total calls: 15,000) in 0.0XYZ s
```

---

## 6) Real-World Use Cases (just the most important)

1. **“Find All” in editors & IDEs**
   Searching a pattern across large files/projects with near-linear performance.

2. **DNA/RNA motif search**
   Identifying occurrences of short motifs within long genomic sequences.

3. **Cybersecurity / IDS**
   Matching known malicious signatures (substrings) inside network payloads/logs.

4. **Plagiarism & duplicate detection (exact-match stage)**
   Fast exact substring hits before heavier semantic checks.

5. **Log mining & observability**
   Extracting positions of key tokens across huge logs to drive alerts or metrics.

