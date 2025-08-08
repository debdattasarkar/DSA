
---

# **Longest Periodic Proper Prefix**

**Difficulty:** Hard
**Accuracy:** 43.94%
**Submissions:** 587+
**Points:** 8

---

## **Problem Statement**

Given a string **s**, find the length of the **longest periodic proper prefix** of **s**.
If no such prefix exists, return **-1**.

---

### **Definitions**

* A **periodic proper prefix** is a non-empty prefix of **s** (but **not the whole string**) such that **repeating this prefix enough times** produces a string that **starts with s**.

---

## **Examples**

### **Example 1**

**Input:**

```
s = "aaaaaa"
```

**Output:**

```
5
```

**Explanation:**
Repeating the proper prefix `"aaaaa"` forms `"aaaaaaaaaa..."`, which contains `"aaaaa"` as a prefix.
No longer proper prefix satisfies this.

---

### **Example 2**

**Input:**

```
s = "abcab"
```

**Output:**

```
3
```

**Explanation:**
Repeating the proper prefix `"abc"` forms `"abcabc..."`, which contains `"abcab"` as a prefix.
No longer proper prefix satisfies this.

---

### **Example 3**

**Input:**

```
s = "ababd"
```

**Output:**

```
-1
```

**Explanation:**
No proper prefix satisfies the given condition.

---

## **Constraints**

* $1 \leq s.size() \leq 10^5$
* **s** consists of lowercase English alphabets.

---

## **Expected Complexities**

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## **Topic Tags**

* Strings
* Algorithms
* Data Structures
* Hash

---

## **Related Articles**

* [Longest Periodic Proper Prefix](https://www.geeksforgeeks.org/longest-periodic-proper-prefix/)

---

---

# Longest Periodic Proper Prefix — Explanation + Python solutions

You’re given a string `s`.
Return the **length of the longest proper prefix** `p` (`p != s`) such that **repeating `p`** infinitely would produce a string that **starts with `s`**.

Equivalently: find the largest `t (1 ≤ t < n)` such that `t` is a **period** of `s`, i.e.

```
for all i in [t .. n-1]:  s[i] == s[i - t]
```

If none exists, return `-1`.

---

## Intuition

* If `t` is a period, then the suffix `s[t:]` must equal the prefix `s[:n-t]`.
  That’s exactly the **Z-algorithm** condition: `Z[t] ≥ n - t`.
* Another view (KMP): If `b` is a **border** length (a length where prefix==suffix), then `t = n - b` is a period.
  Among all positive borders, the **smallest** border (smallest `b > 0`) yields the **largest** `t`.

---

## Dry run (short & surgical)

### Example 1

`s = "abcab"`, `n = 5`

Z array (positions 0..4):

* `Z[0]=0` (by convention)
* `Z[1]=0, Z[2]=0`
* `Z[3]=2`  ← since `s[3:] = "ab"` equals `s[:2] = "ab"`
* `Z[4]=0`

Scan `t` from `n-1=4` down to `1`:

* `t=4`: need `Z[4] ≥ 1`? 0 ≥ 1 → no
* `t=3`: need `Z[3] ≥ 2`? 2 ≥ 2 → yes ⇒ **answer = 3**

Indeed, the prefix of length 3 is `"abc"`. Repeating `"abc"` gives `"abcabc..."`, which starts with `"abcab"`.

### Example 2

`s = "aaaaaa"`, `n = 6`

Z array: `Z = [0,5,4,3,2,1]`
Scan from `t=5` down:

* `t=5`: need `Z[5] ≥ 1`? 1 ≥ 1 → yes ⇒ **answer = 5**

Prefix `"aaaaa"` repeated is `"aaaaaaaa..."`, which starts with `"aaaaaa"`.

### Example 3

`s = "ababd"`, `n = 5`

Z array: likely `Z = [0,0,3,0,0]`? (crucially `Z[3] < 2`, `Z[2] < 3`)
Scanning `t=4..1` gives no success ⇒ **answer = -1**.

---

## Solutions (what interviewers expect)

### 1) Brute force (simple, but O(n²))

Try `t` from `n-1` down to `1`, check period property directly.

```python
class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n <= 1:
            return -1  # no proper prefix exists
        
        # Try biggest candidate period t from n-1 down to 1
        for t in range(n - 1, 0, -1):
            ok = True
            # Check s[t:] == s[:n-t]
            for i in range(t, n):
                if s[i] != s[i - t]:
                    ok = False
                    break
            if ok:
                return t
        return -1
```

* **Time:** worst-case `O(n²)` (e.g., for many equal chars).
* **Space:** `O(1)`.

---

### 2) Optimal using **Z-algorithm** (cleanest O(n))

Compute the Z-array in `O(n)`. Then the longest period is the largest `t` such that `Z[t] ≥ n - t`.

```python
class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n <= 1:
            return -1
        
        # --- Z-function in O(n) ---
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        
        # Find the largest t < n with Z[t] >= n - t
        for t in range(n - 1, 0, -1):
            if z[t] >= n - t:
                return t
        return -1
```

* **Time:** `O(n)`
* **Space:** `O(n)` for the Z array.

---

### 3) Optimal using **KMP prefix-function (π / LPS)** — border-chain trick (also O(n))

A period `t` is valid iff `n - t` is a **border** (`prefix == suffix` of that length).
The **largest** `t` equals `n - (smallest positive border)`.
We get all borders by walking the `π` chain: `b = π[n-1]`, then `b = π[b-1]`, etc.
The last non-zero `b` encountered is the **smallest positive border**.

```python
class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n <= 1:
            return -1
        
        # --- Build prefix-function (pi) in O(n) ---
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        
        # Walk down the border chain to find the smallest positive border
        b = pi[-1]
        if b == 0:
            return -1  # no positive border -> no period
        while pi[b - 1] > 0:
            b = pi[b - 1]
        
        # largest period = n - (smallest positive border)
        return n - b
```

* **Time:** `O(n)`
* **Space:** `O(n)` for `pi`.

> Sanity:
>
> * `"abcab"` → `pi = [0,0,0,1,2]`. Borders chain: 2 → 0, smallest positive border = 2 ⇒ ans = 5 - 2 = 3.
> * `"aaaaaa"` → borders chain: 5→4→3→2→1 (smallest is 1) ⇒ ans = 6 - 1 = 5.
> * `"ababd"` → `pi[-1]=0` ⇒ no border ⇒ -1.

Pick **Z** or **KMP**—both are standard, linear, and interview-acceptable.

---

## Common interviewer Q\&A

**Q1. What’s the difference between “string is a repetition of a prefix” and this problem?**
**A.** Repetition requires the **whole string** to be made of copies of a prefix (i.e., `n % period == 0`).
Here we only need the string to be a **prefix** of infinite repetitions—divisibility is **not required**.
Example: `"abcab"` has period `3` but `5 % 3 ≠ 0`; still valid here.

**Q2. Why does `Z[t] ≥ n - t` characterize a period?**
**A.** Because it says the **suffix starting at `t`** matches the **prefix** for length `n - t`, i.e., `s[t:] == s[:n-t]`, the exact period condition.

**Q3. How does KMP help?**
**A.** KMP’s `π` (LPS) array gives **borders** (prefix = suffix).
`n - t` being a border ⇔ `t` is a period.
The biggest `t` corresponds to the **smallest positive border**.

**Q4. What’s returned for length-1 strings?**
**A.** No proper prefix exists, so `-1`.

**Q5. Edge cases to mention?**

* All characters same → answer is `n-1`.
* No repetition pattern at all → `-1`.
* Mixed but periodic prefix near the end → ensure scan from right to left to pick **longest** `t`.

---

---

Here’s a **self‑contained, runnable Python program** for **Longest Periodic Proper Prefix** that:

* Implements the **optimal Z‑Algorithm** version in `getLongestPrefix` (what I recommend in interviews).
* Also includes **KMP (π/LPS)** and a **brute-force checker** for completeness and sanity tests.
* Prints **inputs & outputs** and benchmarks using `timeit`.

```python
#!/usr/bin/env python3
"""
Problem: Longest Periodic Proper Prefix

Return the largest t (1 <= t < n) such that repeating the prefix s[:t]
infinitely would produce a string that starts with s.
If no such t exists, return -1.
"""

from timeit import timeit

class Solution:
    # ------------------------------------------------------------
    # Optimal solution using Z-Algorithm  — O(n) time, O(n) space
    # ------------------------------------------------------------
    def getLongestPrefix(self, s: str) -> int:
        """
        Z-algorithm builds z[i] = LCP(s, s[i:]) in O(n).
        A period t is valid iff z[t] >= n - t  (suffix starting at t equals prefix).
        We scan t from n-1 down to 1 to get the largest period.

        Time:
            - Build Z array: O(n)
            - Scan from n-1..1: O(n)
            Overall O(n)

        Space:
            - Z array of size n: O(n)
        """
        n = len(s)
        if n <= 1:
            # No proper prefix exists for length <= 1  — O(1) time/space
            return -1

        # Build Z array — O(n) time, O(n) space
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            # Inside-box copy — O(1)
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            # Explicit comparisons — each char visited amortized O(1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            # Update [l, r] box — O(1)
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        # Find the largest t < n with z[t] >= n - t  — O(n)
        for t in range(n - 1, 0, -1):
            if z[t] >= n - t:
                return t
        return -1

    # ------------------------------------------------------------
    # Also provide KMP (prefix function / LPS)  — O(n) time, O(n) space
    # ------------------------------------------------------------
    def getLongestPrefix_kmp(self, s: str) -> int:
        """
        If b is a border (prefix==suffix length b), then t = n - b is a period.
        The largest t corresponds to the smallest positive border.
        """
        n = len(s)
        if n <= 1:
            return -1

        # Build prefix function (pi) — O(n) time, O(n) space
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j

        b = pi[-1]
        if b == 0:
            return -1
        while pi[b - 1] > 0:
            b = pi[b - 1]
        return n - b

    # ------------------------------------------------------------
    # Brute force checker — O(n^2) time, O(1) space
    # ------------------------------------------------------------
    def getLongestPrefix_bruteforce(self, s: str) -> int:
        """
        Try periods t from n-1 down to 1; check s[t:] == s[:n-t].
        """
        n = len(s)
        if n <= 1:
            return -1

        for t in range(n - 1, 0, -1):  # O(n) candidates
            ok = True
            for i in range(t, n):      # O(n) comparisons per candidate
                if s[i] != s[i - t]:
                    ok = False
                    break
            if ok:
                return t
        return -1


# -----------------------------
# Demo + Benchmark with timeit
# -----------------------------
def main():
    sol = Solution()

    tests = [
        "abcab",      # answer 3  (repeat 'abc')
        "aaaaaa",     # answer 5  (repeat 'a' * 1)
        "ababd",      # answer -1 (not periodic prefix)
        "abcabcabcx", # answer 3
        "abcdabc",    # answer 4? No → check: "abcd" repeat gives "abcdabcd...", starts with "abcdabc" → yes ⇒ 4
        "a",          # answer -1
        "zzzzzzzzzz", # answer 9
    ]

    print("===== Outputs (Optimal Z-Algorithm) =====")
    for s in tests:
        ans = sol.getLongestPrefix(s)
        print(f"s = {s!r:12} -> longest periodic proper prefix length = {ans}")

    # Quick cross-check with KMP and brute on small inputs
    print("\n===== Sanity check (KMP vs Z vs Brute on small cases) =====")
    smalls = ["abcab", "aaaaaa", "ababd", "aba", "ababa", "abcdabc", "xyzxyzx"]
    for s in smalls:
        z_ans = sol.getLongestPrefix(s)
        k_ans = sol.getLongestPrefix_kmp(s)
        b_ans = sol.getLongestPrefix_bruteforce(s)
        print(f"{s!r:10} -> Z:{z_ans}  KMP:{k_ans}  Brute:{b_ans}")

    # ----------------- Benchmark with timeit -----------------
    # We benchmark only the optimal method on a moderately long string.
    big = ("abcde" * 2000) + "abcd"   # length ~ 10004; longest period should be 5
    n_runs = 200  # adjust if your machine is slow/fast

    def bench():
        sol.getLongestPrefix(big)

    t = timeit(bench, number=n_runs)
    print(f"\nTimeit: ran optimal getLongestPrefix {n_runs} times on len={len(big)}; "
          f"total time = {t:.4f}s  (~{t/n_runs:.6f}s per run)")

if __name__ == "__main__":
    main()
```

### What the program prints

* For each example `s`, it prints the **length of the longest periodic proper prefix** using the optimal Z‑Algorithm.
* It then **cross‑checks** Z vs KMP vs Brute on small cases (they should match).
* Finally, it runs a **`timeit` benchmark** on a larger string and reports the total and per‑run time.

### Why this is interview‑friendly

* The Z‑Algorithm solution is **linear** time and easy to justify:
  “A period `t` means `s[t:] == s[:n-t]` — exactly `Z[t] ≥ n - t`.”
* The KMP (π / LPS) variant is also linear and shows breadth.
* The brute‑force checker is handy for validating your optimized code on samples.

---

---

Here are **the most important real-world use cases** of the **Longest Periodic Proper Prefix** problem — you don’t need to remember all possible ones, just these few which actually come up in practice:

---

## 1. **String Pattern Matching (KMP-like Preprocessing)**

* **Why**: In algorithms like **Knuth–Morris–Pratt (KMP)**, finding the longest border (prefix = suffix) or a periodic prefix is part of preprocessing to enable **O(n)** pattern matching.
* **Example**: Searching for `"abab"` in a long text can skip re-checking certain positions by knowing that `"ab"` is both a prefix and suffix.
* **Industry relevance**: Used in **text editors, search engines, bioinformatics DNA sequence matching**.

---

## 2. **Data Compression (LZ-family, Run-length detection)**

* **Why**: Detecting repeating prefixes allows recognizing **periodic patterns** and compressing them efficiently.
* **Example**: `"abcabcabc..."` can be stored as `"abc"` + repetition count.
* **Industry relevance**: **Gzip, LZ77, LZ78, PNG image compression**.

---

## 3. **Bioinformatics – DNA & Protein Repeat Detection**

* **Why**: Biological sequences often have repeating patterns that have biological significance (e.g., tandem repeats).
* **Example**: `"ATGATGATG"` → periodic prefix `"ATG"`.
* **Industry relevance**: Used in **gene analysis, mutation detection, evolutionary biology**.

---

## 4. **Plagiarism & Similarity Detection**

* **Why**: Detecting repeated structured phrases can help find **templated or boilerplate text** reused across documents.
* **Example**: `"This is the same introThis is the same intro"` → detect `"This is the same intro"` as repeating.
* **Industry relevance**: **Academic plagiarism checkers, code duplication detection tools**.

---

## 5. **Music / Signal Processing – Loop Detection**

* **Why**: In audio or signal data, identifying repeating periodic segments is useful for **loop detection** and compression.
* **Example**: Detect `"drum loop"` pattern repeated multiple times in a track.
* **Industry relevance**: **DAWs (Digital Audio Workstations)**, **speech recognition preprocessing**.

---

