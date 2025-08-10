
---

# Palindrome SubStrings

**Difficulty:** Hard
**Accuracy:** 45.8%
**Submissions:** 51K+
**Points:** 8
**Average Time:** 30m

---

## Problem Statement

Given a string **s**, count all **palindromic sub-strings** present in the string.
The length of the palindromic sub-string must be **greater than or equal to 2**.

---

### Note:

* A substring is **palindromic** if it reads the same forwards and backwards.

---

## Examples

**Example 1:**

```
Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings (of length > 1) are: "aba", "aa", "baab".
```

**Example 2:**

```
Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings (of length > 1) are: "aa", "aa", "aaa".
```

**Example 3:**

```
Input: s = "abbaeae"
Output: 4
Explanation: All palindromic substrings (of length > 1) are: "bb", "abba", "eae", "aea".
```

---

## Constraints:

* $2 \leq s.size() \leq 5 \times 10^3$

---

## Expected Complexities:

* **Time Complexity:** $O(n^2)$
* **Auxiliary Space:** $O(1)$

---

## Company Tags:

* Morgan Stanley
* Amazon
* Ola Cabs
* SAP Labs

---

## Topic Tags:

* Strings
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Interview Experiences:

* Ola Interview Experience Set 11 Internship

---

## Related Articles:

* [Count Palindrome Sub Strings String Set 2](https://www.geeksforgeeks.org/count-palindrome-sub-strings-string-set-2/)

---

---

Alright—let’s nail this one cleanly and interview‑style.
Goal: count **all palindromic substrings of length ≥ 2** in `s` (occurrences, not unique).

---

# 2) Explanation + step‑by‑step dry run

### Key idea

A palindrome mirrors around its **center**.

* Odd length palindromes have one center (e.g., `aba` → center at `b`).
* Even length palindromes have a “gap” center (e.g., `abba` → center between the two `b`s).

If we expand from every possible center as long as the characters match, we can count every palindromic substring exactly once.

We only need to **skip length‑1 palindromes** (the single letters), because the problem wants length ≥ 2.

### Dry run on `s = "abbaeae"`

Indices: `0 1 2 3 4 5 6`
Chars : `a b b a e a e`

We expand around **every** center:

* Odd centers `(i,i)`

  * `(0,0)` → `"a"` (len 1 only) → contributes 0
  * `(1,1)` → `"b"`, try expand `"bba"`? No (`s[0]!=s[2]`) → 0
  * `(2,2)` → `"b"`, try `"abb a"`? No (`s[1]!=s[3]`) → 0
  * `(3,3)` → `"a"`; expand to `"b a b"`? `s[2]==s[4]?` `b` vs `e` → no; 0
  * `(4,4)` → `"e"`; expand to `"a e a"`? yes (`s[3]==s[5]`), length 3 → **+1** (`"aea"`). Next expand to `"b a e a b"`? `s[2]==s[6]?` `b` vs `e` → stop.
  * `(5,5)` → `"a"`; expand to `"e a e"`? yes (`s[4]==s[6]`), length 3 → **+1** (`"eae"`). Next expand further? left=3,right=7 stop.
  * `(6,6)` → `"e"` → 0

* Even centers `(i,i+1)`

  * `(0,1)` → `"ab"` not palindrome → 0
  * `(1,2)` → `"bb"` palindrome length 2 → **+1**. Try expand to `"abba"`? yes (`s[0]==s[3]`), length 4 → **+1**. Try further? out of bounds → stop.
  * `(2,3)` → `"ba"` not palindrome → 0
  * `(3,4)` → `"ae"` no → 0
  * `(4,5)` → `"ea"` no → 0
  * `(5,6)` → `"ae"` no → 0

Total = `{"bb","abba","aea","eae"} = 4`, which matches the example.

---

# 3) Implementations (brute force + optimized)

### A) Brute force (clear but slow) — O(n³)

Check every substring `s[i:j+1]` (with `j-i+1 >= 2`) by two‑pointer palindrome test.

```python
class Solution:
    def countPS(self, s):
        # Brute force: try all substrings and check palindrome
        n = len(s)
        if n < 2:
            return 0
        
        def is_palin(l, r):
            # Two-pointer check: O(length)
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        count = 0
        # Try all substrings of length >= 2 → O(n^2) substrings
        for i in range(n):
            for j in range(i + 1, n):  # ensures length >= 2
                if is_palin(i, j):     # O(n) check
                    count += 1
        return count
```

* **Time:** O(n³) in the worst case (n² substrings × O(n) check).
* **Space:** O(1) extra.

---

### B) Optimized (center expansion) — O(n²), O(1) space

Expand around every center (odd and even), counting only length ≥ 2.

```python
class Solution:
    def countPS(self, s):
        n = len(s)
        if n < 2:
            return 0
        
        def expand(l, r):
            # Expands while s[l..r] is a palindrome
            # Counts only substrings with length >= 2
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:
                    cnt += 1
                l -= 1
                r += 1
            return cnt
        
        total = 0
        for i in range(n):
            # Odd-length palindromes centered at i
            total += expand(i, i)
            # Even-length palindromes centered between i and i+1
            total += expand(i, i + 1)
        return total
```

* **Why O(n²)?** There are `2n-1` centers and each expansion moves `l` and `r` at most `O(n)` times across all centers.
* **Space:** O(1).

> (Optional note for interviews) There is an O(n) algorithm—**Manacher’s**—but it’s more complex to implement. Center expansion is the standard “good enough” choice and passes comfortably for |s| ≤ 5e3.

---

# 4) Interview Q\&A (quick hits)

**Q1. Are we counting unique palindromic substrings or all occurrences?**
**A.** All **occurrences**. For `s = "aaa"`, the answer is 3: `"aa"(0..1)`, `"aa"(1..2)`, and `"aaa"(0..2)`.

**Q2. Why check both odd and even centers?**
**A.** Because even‑length palindromes (like `"abba"`) have a center **between** two characters; odd palindromes (like `"aba"`) center **on** a character.

**Q3. Can we do better than O(n²)?**
**A.** Yes—**Manacher’s algorithm** runs in O(n) and gives the radius of the longest palindrome at every position. From those radii you can count palindromes. But it’s lengthy and error‑prone; center expansion is preferred in interviews unless O(n) is specifically required.

**Q4. Any common off‑by‑one mistakes?**
**A.** Forgetting to exclude length‑1 palindromes. In center expansion, we simply start counting only when `r - l + 1 >= 2`.

**Q5. What about constraints with Unicode/case?**
**A.** This task treats the string “as is”. If needed, you can normalize case (e.g., `s.lower()`) and handle Unicode carefully, but not required here.

**Q6. Why not DP with a table?**
**A.** DP is also O(n²) time & O(n²) space: `dp[l][r] = s[l]==s[r] and (r-l<3 or dp[l+1][r-1])`. It’s fine but uses more memory than center expansion and is slower in practice.

---

---

Here’s the classic **DP** approach too.

# DP approach (O(n²) time, O(n²) space)

### Idea

Let `dp[l][r]` mean: `s[l..r]` is a palindrome.
Transition:

* Base cases

  * Single char: `dp[i][i] = True` (we **won’t** count these)
  * Two chars: `dp[i][i+1] = (s[i] == s[i+1])`
* For length ≥ 3:
  `dp[l][r] = (s[l] == s[r]) and dp[l+1][r-1]`

Count every time `dp[l][r]` is `True` **and** `(r-l+1) ≥ 2`.

```python
class Solution:
    def countPS(self, s):
        n = len(s)
        if n < 2:
            return 0

        # dp[l][r] == True if s[l..r] is a palindrome
        dp = [[False] * n for _ in range(n)]
        count = 0

        # length 1 substrings are palindromes, but we don't count them
        for i in range(n):
            dp[i][i] = True

        # length 2 substrings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1  # length 2, so count it

        # length >= 3
        for length in range(3, n + 1):            # window size
            for l in range(0, n - length + 1):
                r = l + length - 1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    count += 1

        return count
```

### Complexity

* **Time:** O(n²) — we fill an n×n table once.
* **Space:** O(n²) for the DP table.

### When to choose DP vs. Center Expansion?

* **DP** is easy to reason about when you also need to *reconstruct* palindromes or answer range queries later.
* **Center expansion** is simpler, O(1) space, and usually faster in practice for just counting.

---

---

Here’s the **interview Q\&A set** tailored for the **DP version** of the Palindromic Substrings problem:

---

## **Interview Questions & Answers**

### **Q1. What is the key idea behind your DP approach?**

**A:**
We use a 2D boolean DP table `dp[l][r]` where each entry tells us whether the substring `s[l..r]` is a palindrome.
We fill this table bottom-up:

* Single-character substrings are trivially palindromes.
* Two-character substrings are palindromes if both characters are equal.
* For length ≥ 3, a substring is a palindrome if its first and last characters match **and** the substring in between (`s[l+1..r-1]`) is also a palindrome.

---

### **Q2. Why do we need DP when a center expansion solution exists in O(1) space?**

**A:**
DP is useful when:

* We need to **reconstruct** palindromic substrings, not just count them.
* We have **multiple queries** asking if `s[l..r]` is a palindrome.
* The center expansion method is optimal for just counting but does not store results for reuse.
  DP trades extra memory (O(n²)) for the ability to answer such queries instantly.

---

### **Q3. What is the time and space complexity of your DP approach?**

**A:**

* **Time Complexity:** O(n²) because we fill an `n×n` table, and each cell takes O(1) to compute.
* **Space Complexity:** O(n²) for storing the boolean DP table.
  This is acceptable for `n ≤ 5000` in theory, but practically, for `n` above \~3000, memory becomes a bottleneck.

---

### **Q4. Can the space complexity be optimized?**

**A:**
Yes. For counting purposes, we don’t actually need the entire 2D table at once:

* If we fill the table diagonally (from shorter substrings to longer ones), we could reduce it to O(n) space by only storing the previous row/diagonal results.
* However, reconstructing palindromes would still require O(n²) storage.

---

### **Q5. What’s the difference between this problem and “Longest Palindromic Substring”?**

**A:**

* **This problem:** Count **all** palindromic substrings of length ≥ 2.
* **Longest Palindromic Substring:** Find the single longest palindrome (max length) within the string.
  Both can use similar DP or center expansion logic, but the termination condition and goal differ.

---

### **Q6. Could you solve this problem in O(n) time?**

**A:**
Yes, using **Manacher’s algorithm**, which finds longest palindromes centered at each position in O(n) time.
However, adapting it to count **only length ≥ 2** substrings needs careful handling of radius values.

---

---

Awesome—let’s wrap this up cleanly:

# Side‑by‑side: Center Expansion vs DP vs Manacher’s (for counting palindromic substrings, length ≥ 2)

| Method               | Core idea                                                                                                                                                            |      Time |     Space | When to prefer                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------: | --------: | ----------------------------------------------------------------------------------------------- |
| **Center Expansion** | Expand around every character and every gap (odd & even centers). Each expansion that keeps equality yields one palindrome.                                          | **O(n²)** |  **O(1)** | Fast in practice, super simple, no extra memory, you only need the count.                       |
| **DP (table)**       | `dp[l][r] = (s[l]==s[r]) AND (r-l<2 OR dp[l+1][r-1])`, fill from shorter to longer substrings, count `dp[l][r]` where `r-l+1 ≥ 2`.                                   | **O(n²)** | **O(n²)** | When you also need to answer many “is s\[l..r] palindrome?” queries or reconstruct palindromes. |
| **Manacher’s**       | Linear‑time radii arrays: `d1` for odd, `d2` for even. Total palindromes = `sum(d1)+sum(d2)`. For length ≥ 2, subtract `n` for single letters ⇒ `sum(d1)+sum(d2)-n`. |  **O(n)** |  **O(n)** | Best asymptotics; great for very long strings. A bit trickier to code/remember.                 |

---

# Quick dry run (Center Expansion) on `"abbae"`

Centers (0‑based):

* Odd at `i=2` (“b**b**a”): expand → `"bb"`? That’s even; check even next.
* Even between `i=1` and `i=2`: `"bb"` ✓ (count=1), expand outward → `"abba"` ✓ (count=2), expand again → stop.
* Others don’t produce new palindromes ≥ 2.
  **Answer = 2** (“bb”, “abba”).

---

# Full program (Python) with all three methods + inline complexity notes + `timeit` benchmarking

```python
#!/usr/bin/env python3
"""
Count palindromic substrings of length >= 2 using:
1) Center Expansion  (O(n^2) time, O(1) space)
2) DP table          (O(n^2) time, O(n^2) space)
3) Manacher's algo   (O(n)   time, O(n)   space)

Includes a small main that prints results and times each method with timeit.
"""

from timeit import timeit
from typing import List

class Solution:
    # ------------------------------------------------------------
    # 1) Center Expansion
    # Time: O(n^2) worst-case (e.g., "aaaaa..."), Space: O(1)
    # ------------------------------------------------------------
    def countPS_center(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0  # no substrings of length >= 2

        def expand(l: int, r: int) -> int:
            # Expand while palindrome; count only when length >= 2
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:
                    cnt += 1
                l -= 1
                r += 1
            return cnt

        total = 0
        for i in range(n):
            # odd-length centers: start at (i, i)
            total += expand(i, i)
            # even-length centers: start at (i, i+1)
            total += expand(i, i + 1)
        return total

    # ------------------------------------------------------------
    # 2) Dynamic Programming table
    # dp[l][r] is True iff s[l..r] is palindrome
    # Fill by increasing substring length
    # Time: O(n^2), Space: O(n^2)
    # ------------------------------------------------------------
    def countPS_dp(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [[False] * n for _ in range(n)]  # O(n^2) space
        count = 0

        # length = 1 (single chars): palindromes, but we DON'T count them
        for i in range(n):
            dp[i][i] = True

        # length = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1  # length=2 palindromes

        # length >= 3
        for L in range(3, n + 1):             # O(n)
            for l in range(0, n - L + 1):     # O(n) per L
                r = l + L - 1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    count += 1
        return count

    # ------------------------------------------------------------
    # 3) Manacher's Algorithm
    # Returns #pal substrings with length >= 2
    # Time: O(n), Space: O(n)
    # ------------------------------------------------------------
    def countPS_manacher(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # d1[i] = number of odd-length palindromes centered at i (including length 1)
        d1 = [0] * n
        l = r = 0
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            k -= 1
            if i + k > r:
                l, r = i - k, i + k

        # d2[i] = number of even-length palindromes centered between i-1 and i
        d2 = [0] * n
        l = r = 0
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            k -= 1
            if i + k > r:
                l, r = i - k - 1, i + k

        # Total pal substrings (all lengths) = sum(d1) + sum(d2)
        # Remove the n single-char palindromes to get length >= 2
        return (sum(d1) + sum(d2)) - n


# -------------------------- Demo / Benchmark --------------------------
def demo_and_time(strings: List[str], repeats: int = 5) -> None:
    sol = Solution()

    for s in strings:
        print(f"\nInput: {s!r}  (n={len(s)})")

        # Compute once to show correctness
        c_center = sol.countPS_center(s)
        c_dp     = sol.countPS_dp(s)
        c_man    = sol.countPS_manacher(s)

        print(f"Counts (length ≥ 2) -> Center: {c_center}, DP: {c_dp}, Manacher: {c_man}")

        # Sanity check: center vs DP vs Manacher should match
        if not (c_center == c_dp == c_man):
            print("WARNING: methods disagree!")

        # Benchmark with timeit (report total time across `repeats` runs)
        t_center = timeit(lambda: sol.countPS_center(s), number=repeats)
        t_dp     = timeit(lambda: sol.countPS_dp(s),     number=repeats)
        t_man    = timeit(lambda: sol.countPS_manacher(s), number=repeats)

        print(f"Time over {repeats} runs:")
        print(f"  Center    : {t_center:.6f}s   # O(n^2) time, O(1) space")
        print(f"  DP        : {t_dp:.6f}s   # O(n^2) time, O(n^2) space")
        print(f"  Manacher  : {t_man:.6f}s   # O(n) time, O(n) space")


if __name__ == "__main__":
    # A few representative test cases
    tests = [
        "abbae",          # from the dry run -> 2 ("bb","abba")
        "aaa",            # 3 pal substrings >=2: "aa"(0-1),"aa"(1-2),"aaa"
        "abaaeae",        # mix of odds/evens
        "abc",            # 0
        "aaaaa",          # many overlaps (worst-case for O(n^2) methods)
    ]
    demo_and_time(tests, repeats=7)
```

### Notes on the program

* Every function has comments that state **time** and **space** complexity right above it.
* `demo_and_time` prints **counts** for each method (they should match) and then times each method using `timeit`.
* `repeats` controls the number of runs for a coarser, more stable timing on your machine.

---

---

Here are a few **important real-world use cases** for *counting palindromic substrings (length ≥ 2)*:

---

**1. DNA / RNA sequence analysis**

* **Why:** Palindromic nucleotide patterns (like restriction enzyme recognition sites) are biologically significant because they can be binding points for proteins or markers for genetic editing.
* **Example:** Detecting `"GAATTC"` (EcoRI site) and other inverted repeats in genome data.

---

**2. Data compression & pattern mining**

* **Why:** Palindromes indicate repetitive patterns that can be encoded more efficiently.
* **Example:** Preprocessing text before applying Lempel–Ziv compression to identify mirrored blocks for better compression ratio.

---

**3. Natural Language Processing (NLP)**

* **Why:** In linguistic studies or cryptography, palindromic structures may carry stylistic, cultural, or encoded meaning.
* **Example:** Detecting symmetric word sequences in poetry or secret messages.

---

**4. Error detection in transmitted data**

* **Why:** Some communication protocols avoid certain palindromic bit patterns because they can cause synchronization issues.
* **Example:** A data pre-check to ensure no unwanted mirrored patterns exist in a binary stream.

---

**5. Cybersecurity & pattern matching in logs**

* **Why:** Palindromic patterns in malicious payloads or logs might indicate obfuscated command sequences.
* **Example:** Malware signatures containing repeated mirrored byte sequences.

---

---

---

Here’s a clear mapping from each **real‑world use case** to the **best algorithm** (Center Expansion, DP, or Manacher’s), plus why and when to reconsider.

---

## Which algorithm fits which use case?

| Use case                                                                          | Best pick                                                                | Why this one                                                                                                                                    | When to reconsider                                                                                                                                                             |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DNA / RNA sequence analysis** (large genomes; many queries)                     | **Manacher’s (O(n))**                                                    | Genomic strings are huge (10⁶–10⁹ bases). Linear time and linear space are crucial; center expansion (O(n²)) will time out.                     | If you also need **per‑interval palindromicity queries** later, precompute Manacher for counts + keep auxiliary structures; or switch to DP only if the string is small (≤5k). |
| **Data compression & pattern mining** (preprocessing large text/byte streams)     | **Manacher’s (O(n))**                                                    | You want speed and a single pass per block; Manacher gives total count fast and is streaming‑friendly (blockwise).                              | If blocks are *tiny* (≲ 2–3k), **Center** is simpler and often fast enough.                                                                                                    |
| **Natural Language Processing (NLP)** (poetry, stylometry)                        | **Center Expansion (O(n²), O(1) space)**                                 | Texts are usually short/medium; center expansion is very simple, no memory blow‑up, and often faster in practice than DP for just counting.     | If you need to **reconstruct all palindromic substrings** or answer many `isPal(l,r)?` queries → **DP**. For very long corpora / streaming → **Manacher**.                     |
| **Error detection in transmitted data** (bit streams; avoid palindromic patterns) | **Manacher’s (O(n))**                                                    | You may run this repeatedly on long frames/streams; linear time is ideal and predictable.                                                       | If you only scan **very small frames** and need quick prototyping, **Center** is acceptable.                                                                                   |
| **Cybersecurity / log signature matching** (malware patterns)                     | **Center Expansion (O(n²))** for short logs; **Manacher** for large logs | Logs/snippets are often short → Center is simple and has O(1) space. For long consolidated logs or batch pipelines, **Manacher** scales better. | **DP** only if you must **cache palindromicity** for many future subrange checks (investigations).                                                                             |

---

## One‑line heuristics (to decide fast)

* **Need raw speed on long strings?** → **Manacher’s**.
* **Just counting, strings not huge, want simple code & O(1) space?** → **Center Expansion**.
* **Also need to answer many “is s\[l..r] palindrome?” or reconstruct palindromes?** → **DP** (table).
* **Memory constrained?** Avoid **DP**; prefer **Center** (O(1) space) or **Manacher** (O(n) space).

---

## Practical sizes & picks

* **n ≤ 2–3k:** Center Expansion is usually fastest to write and plenty fast.
* **n ≈ 5k–100k:** Manacher’s gives robust performance; Center may start dragging on worst‑case strings like `"aaaa…a"`.
* **n > 100k / streaming:** Manacher’s (blockwise), or rolling pipeline that aggregates counts.

---

## Pitfalls to keep in mind

* **Center Expansion:** Don’t forget to **exclude length‑1** palindromes when counting; check both **odd and even** centers.
* **DP:** O(n²) space can be a show‑stopper beyond a few thousand characters; use only when you truly need table answers.
* **Manacher’s:** Implementation is a bit fiddly—track **odd (`d1`)** and **even (`d2`)** radii separately; final count ≥2 is `sum(d1)+sum(d2)-n`.
