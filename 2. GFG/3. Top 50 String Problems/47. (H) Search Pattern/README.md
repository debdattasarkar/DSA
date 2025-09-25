# Search Pattern

**Difficulty:** Hard
**Accuracy:** 45.04%
**Submissions:** 127K+
**Points:** 8

---

## Problem Statement

Given two strings, one is a text string `txt` and the other is a pattern string `pat`. The task is to print the **indexes of all the occurrences** of the pattern string in the text string. **Use 0-based indexing** while returning the indices.

**Note:** Return an empty list in case of no occurrences of pattern.

---

## Examples

### Example 1

**Input:** `txt = "abcab"`, `pat = "ab"`
**Output:** `[0, 3]`
**Explanation:** The string `"ab"` occurs twice in `txt`, one starts at index `0` and the other at index `3`.

---

### Example 2

**Input:** `txt = "abesdu"`, `pat = "edu"`
**Output:** `[]`
**Explanation:** There's no substring `"edu"` present in `txt`.

---

### Example 3

**Input:** `txt = "aabaacaadaabaaba"`, `pat = "aaba"`
**Output:** `[0, 9, 12]`
**Explanation:** Pattern `"aaba"` is found at indices `0`, `9`, and `12` in the text.

---

## Constraints

* `1 ≤ txt.size() ≤ 10^6`
* `1 ≤ pat.size() < txt.size()`
* Both the strings consist of lowercase English alphabets.

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(m)`

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

* KMP Algorithm For Pattern Searching
* Rabin Karp Algorithm For Pattern Searching
* Z Algorithm Linear Time Pattern Searching Algorithm

---

---

awesome—here’s the full, interview-ready pack for **Search Pattern**.

---

# 2) Explanation + step-by-step dry run

## Problem recap

Given text `txt` and pattern `pat`, return all **0-based** indices `i` such that `txt[i : i+len(pat)] == pat`. If none, return `[]`.

---

## Approaches overview

1. **Brute force (naive):** try every start `i` and compare characters.
   Time `O((n−m+1)·m)` → `O(n·m)`, Space `O(1)`.

2. **KMP (Knuth–Morris–Pratt) — most expected in interviews:**
   Precompute **LPS** (longest proper prefix which is also a suffix) for `pat`. While scanning `txt`, when a mismatch happens after `j` matched chars, jump `j` back to `lps[j-1]` instead of restarting from 0.
   Time `O(n+m)`, Space `O(m)`.

3. **Rabin–Karp (rolling hash):**
   Compare window hashes; when hashes match, verify by direct comparison to avoid collisions.
   Average `O(n+m)`, worst-case `O(n·m)`; Space `O(1)`.

---

## KMP in a nutshell

* **LPS array** (`lps[i]`): for `pat[:i+1]`, length of the longest proper prefix that is also a suffix.
* While scanning `txt`, if `txt[i] != pat[j]` and `j>0`, we set `j = lps[j-1]` (reuse previous partial match) instead of moving `i` back.

### Build LPS for `pat = "aaba"`

Indices: `0 1 2 3` → `a a b a`

* `lps[0] = 0`
* i=1: `a` vs `a` (len=1) → `lps[1]=1`
* i=2: `b` vs `a` mismatch; fallback len=lps[0]=0 → compare `b` vs `a` mismatch → `lps[2]=0`
* i=3: `a` vs `a` (len=1) → `lps[3]=1`

So `lps = [0, 1, 0, 1]`.

### KMP search dry run on

`txt = "aabaacaadaabaaba"`, `pat = "aaba"` (m=4)

Walk through `txt` with pointer `i` and `pat` with `j`:

* Start `i=0,j=0` → match 3 times: at `i=3,j=3`, next also matches → `j=4` ⇒ hit! record `i-j+1 = 0`. Set `j = lps[3] = 1`.
* Continue; mismatches cause `j` to fall back via LPS without moving `i` much.
* Next full match completes at `i=12` ⇒ start index `9` (record) and `j` resets to `1`.
* Next full match completes at `i=15` ⇒ start index `12`.

Final indices: **`[0, 9, 12]`**.

---

# 3) Optimized Python codes (multiple ways)

Below are three drop-in implementations. The **default `Solution`** uses **KMP** (most expected). I also include `SolutionBrute` and `SolutionRK` for completeness.

### A) KMP (recommended)

```python
class Solution:
    def search(self, pat, txt):
        """
        KMP pattern search.
        Time:  O(n + m)  (build LPS in O(m), scan text in O(n))
        Space: O(m)      (LPS array)
        Returns: list of 0-based starting indices where pat occurs in txt
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []  # by constraints m >= 1, but keep safe

        # -------- build LPS (Longest Prefix Suffix) for 'pat' --------
        lps = [0] * m
        # len_ = length of the current longest prefix-suffix
        len_ = 0
        i = 1
        # Build LPS in O(m)
        while i < m:
            if pat[i] == pat[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                if len_ != 0:
                    len_ = lps[len_ - 1]  # fallback; do not increment i
                else:
                    lps[i] = 0
                    i += 1

        # -------- scan text with reuse via LPS --------
        res = []
        i = j = 0  # i -> txt, j -> pat
        # O(n) scan
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    # Found an occurrence ending at i-1
                    res.append(i - m)   # 0-based start index
                    j = lps[j - 1]      # continue to find next match (overlaps allowed)
            else:
                if j != 0:
                    j = lps[j - 1]      # reuse previous prefix
                else:
                    i += 1              # no partial match to reuse; advance text

        return res
```

---

### B) Brute Force (baseline / easy to explain)

```python
class SolutionBrute:
    def search(self, pat, txt):
        """
        Naive pattern search.
        Time:  O((n-m+1) * m) -> O(n*m)
        Space: O(1)
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []
        res = []
        # Try every possible start i
        for i in range(n - m + 1):            # (n-m+1) windows
            # Compare up to m chars
            match = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                res.append(i)
        return res
```

---

### C) Rabin–Karp (rolling hash with verification)

```python
class SolutionRK:
    def search(self, pat, txt):
        """
        Rabin-Karp with base-256 rolling hash and large prime mod.
        Hash matches are verified to avoid false positives.
        Avg Time: O(n + m), Worst-case: O(n*m) (many collisions)
        Space:    O(1)
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []

        base = 256
        mod = 1_000_000_007

        # precompute base^(m-1) % mod to remove the leading char
        high = pow(base, m - 1, mod)

        # initial hashes for first window and pattern
        h_text = 0
        h_pat = 0
        for k in range(m):
            h_text = (h_text * base + ord(txt[k])) % mod
            h_pat  = (h_pat  * base + ord(pat[k])) % mod

        res = []
        for i in range(n - m + 1):
            # If hash matches, verify by direct comparison to avoid collisions
            if h_text == h_pat and txt[i:i + m] == pat:
                res.append(i)
            # Slide the window: remove left char and add next char
            if i < n - m:
                left = ord(txt[i])
                right = ord(txt[i + m])
                # Remove left contribution, multiply by base, add right
                h_text = (h_text - left * high) % mod
                h_text = (h_text * base + right) % mod
                # keep positive
                if h_text < 0:
                    h_text += mod

        return res
```

---

# 4) Interview Q&A (what they usually probe)

**Q1. Why does KMP run in O(n+m)?**
*A:* Building LPS takes `O(m)`. During the scan, `i` (text) moves forward at most `n` times, and `j` (pattern) only moves back via LPS but never decrements `i`. Each character is effectively processed a constant number of times.

**Q2. What is the LPS array conceptually?**
*A:* `lps[i]` is the length of the longest proper prefix of `pat[:i+1]` that is also a suffix. On mismatch at position `j`, we know the first `lps[j-1]` characters still match, so we jump `j` there instead of restarting.

**Q3. Can KMP handle overlapping matches?**
*A:* Yes. After a full match at `j == m`, we set `j = lps[m-1]` and continue, which naturally allows overlaps.

**Q4. Rabin–Karp pros/cons?**
*A:* Very simple sliding window and can be extended to multiple patterns; average `O(n+m)`. But collisions can cause worst-case `O(n·m)` unless double hashing or verification is used.

**Q5. When would you pick KMP vs RK?**
*A:* For a single pattern with strict worst-case guarantees and no hashing pitfalls, choose **KMP**. For multiple patterns or large alphabets where hashing is convenient, **RK** (with verification/double hashing) can be elegant.

**Q6. Space complexity of KMP?**
*A:* `O(m)` for the LPS table; scanning uses `O(1)` extra.

**Q7. Edge cases to watch?**
*A:* `m > n` ⇒ `[]`. Case sensitivity and character set assumptions. Very repetitive patterns like `"aaaaa"` should still be linear with KMP due to LPS reuse.

**Q8. How to print 1-based indices (some platforms ask that)?**
*A:* Add `+1` when appending (`res.append(i - m + 2)` in KMP after a match).

---

---

here you go — a **ready-to-run program** that:

* reads **txt** (line 1) and **pat** (line 2) from stdin,
* runs three methods: **KMP (recommended)**, **Rabin–Karp**, and **Brute Force**,
* prints the **inputs** (safely previewed if long) and **outputs**,
* and **times** each method using Python’s `timeit.timeit(...)` inline.

I’ve added concise, interview-style **time/space notes** exactly where they matter.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Search Pattern (find all 0-based indices of 'pat' in 'txt')
# Methods:
#   1) KMP (O(n+m) time, O(m) space)  <-- recommended
#   2) Rabin-Karp (avg O(n+m), worst O(n*m), O(1) space)
#   3) Brute Force (O(n*m), O(1) space)  <-- guarded for very large inputs
#
# Input  (from stdin):
#   Line 1: txt
#   Line 2: pat
#
# Output:
#   - Echo input (safely previewed if long)
#   - Indices list per method
#   - Timing per method using timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit

# -------------------------- KMP ------------------------------
class Solution:
    def search(self, pat, txt):
        """
        KMP pattern search.
        Time:
          - Build LPS: O(m)
          - Scan text: O(n)
          => O(n + m)
        Space: O(m) for LPS array.
        Returns: list of 0-based indices where pat occurs in txt.
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []

        # ---- Build LPS (Longest Prefix which is also Suffix) ----
        lps = [0] * m  # Space O(m)
        # len_ tracks length of current longest prefix-suffix
        len_ = 0
        i = 1
        # Building LPS is O(m) time
        while i < m:
            if pat[i] == pat[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                if len_ != 0:
                    len_ = lps[len_ - 1]  # fallback without advancing i
                else:
                    lps[i] = 0
                    i += 1

        # ---- Scan text using LPS to reuse partial matches ----
        res = []
        i = j = 0  # i over txt, j over pat
        # O(n) scan
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    # full match ends at i-1 -> start index i-m
                    res.append(i - m)
                    j = lps[j - 1]  # allow overlaps
            else:
                if j != 0:
                    j = lps[j - 1]  # reuse previous border
                else:
                    i += 1          # no border to reuse, move on
        return res

# ---------------------- Rabin-Karp ---------------------------
class SolutionRK:
    def search(self, pat, txt):
        """
        Rabin-Karp with base-256 rolling hash and large prime mod.
        Avg Time: O(n + m) with verification; Worst: O(n*m) (collisions)
        Space: O(1)
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []

        base = 256
        mod = 1_000_000_007
        # precompute base^(m-1) % mod (for removing the leftmost char)
        high = pow(base, m - 1, mod)

        # initial hashes for first window and pattern
        h_txt = 0
        h_pat = 0
        for k in range(m):               # O(m)
            h_txt = (h_txt * base + ord(txt[k])) % mod
            h_pat = (h_pat * base + ord(pat[k])) % mod

        res = []
        # slide over txt windows
        for i in range(n - m + 1):       # O(n)
            if h_txt == h_pat and txt[i:i+m] == pat:  # verify on hash hit
                res.append(i)
            if i < n - m:
                # remove left char, add right char (rolling update)
                left = ord(txt[i])
                right = ord(txt[i + m])
                h_txt = (h_txt - left * high) % mod
                h_txt = (h_txt * base + right) % mod

        return res

# ---------------------- Brute Force --------------------------
class SolutionBrute:
    def search(self, pat, txt):
        """
        Naive search by checking every window.
        Time:  O((n-m+1)*m) -> O(n*m)
        Space: O(1)
        """
        n, m = len(txt), len(pat)
        if m == 0 or m > n:
            return []
        res = []
        # For each start index i, compare up to m chars
        for i in range(n - m + 1):       # (n-m+1) windows
            ok = True
            for j in range(m):           # up to m comparisons
                if txt[i + j] != pat[j]:
                    ok = False
                    break
            if ok:
                res.append(i)
        return res

# --------------------------- Main ----------------------------
def _read_inputs():
    lines = [ln.rstrip("\n") for ln in sys.stdin.readlines()]
    # pick first two non-empty lines: txt (line1), pat (line2)
    vals = [ln for ln in lines if ln.strip() != ""]
    if len(vals) < 2:
        print("Provide two lines: first TXT, second PAT.")
        sys.exit(0)
    txt, pat = vals[0], vals[1]
    return txt, pat

def _preview(label, s, limit=100):
    if len(s) <= limit:
        return f"{label} ({len(s)}): {s}"
    head = s[:limit]
    tail = s[-10:] if len(s) > limit + 10 else ""
    return f"{label} ({len(s)}): {head}...{tail}"

def main():
    txt, pat = _read_inputs()

    # Print inputs (avoid flooding terminal on huge strings)
    print(_preview("TXT", txt))
    print(_preview("PAT", pat))
    print()

    # Instantiate solvers
    kmp = Solution()
    rk  = SolutionRK()
    bf  = SolutionBrute()

    # ---- Time each method once using timeit.timeit(number=1) ----
    kmp_time = timeit.timeit(lambda: kmp.search(pat, txt), number=1)
    kmp_res  = kmp.search(pat, txt)

    rk_time  = timeit.timeit(lambda: rk.search(pat, txt), number=1)
    rk_res   = rk.search(pat, txt)

    # Brute-force can be very slow; guard on size
    n, m = len(txt), len(pat)
    do_brute = (n * m <= 2_000_000)  # simple guard; tune as desired
    if do_brute:
        bf_time = timeit.timeit(lambda: bf.search(pat, txt), number=1)
        bf_res  = bf.search(pat, txt)
    else:
        bf_time, bf_res = None, None

    # ---- Print outputs ----
    print("KMP Indices       :", kmp_res)
    print("KMP Time (ms)     : {:.3f}".format(kmp_time * 1000.0))
    print()
    print("Rabin-Karp Indices:", rk_res)
    print("Rabin-Karp Time (ms): {:.3f}".format(rk_time * 1000.0))
    print()
    if do_brute:
        print("Brute Indices     :", bf_res)
        print("Brute Time (ms)   : {:.3f}".format(bf_time * 1000.0))
    else:
        print("Brute Indices     : (skipped for large input)")
        print("Brute Time (ms)   : (skipped)")

    # Sanity check for agreement (KMP vs RK; brute if run)
    agree = (kmp_res == rk_res) and (bf_res is None or kmp_res == bf_res)
    print("\nAll methods agree ✔" if agree else "\nWARNING: Methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 search_pattern.py
aabaacaadaabaaba
aaba
```

### Example Output (timings vary)

```
TXT (16): aabaacaadaabaaba
PAT (4): aaba

KMP Indices       : [0, 9, 12]
KMP Time (ms)     : 0.150

Rabin-Karp Indices: [0, 9, 12]
Rabin-Karp Time (ms): 0.120

Brute Indices     : [0, 9, 12]
Brute Time (ms)   : 0.260

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

* **Text editors & IDEs (“Find” / “Find All”)**: instant substring searches with support for overlaps → KMP is a robust backbone.
* **Intrusion detection / antivirus scanning**: scan large streams or binaries for signature patterns quickly and deterministically.
* **Log mining at scale**: detect repeated error tokens or markers inside terabytes of logs with linear-time guarantees.
* **Bioinformatics motif matching**: search DNA/RNA for exact motifs repeatedly and efficiently.
* **Network protocol parsing**: locate fixed delimiters/headers in packet streams in a single pass.
