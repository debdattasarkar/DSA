# Longest Common Prefix of Strings

**Difficulty:** Easy
**Accuracy:** 29.52%
**Submissions:** 312K+
**Points:** 2
**Average Time:** 15m

---

## Problem

Given an array of strings `arr[]`, return the **longest common prefix** among every string present in the array.
If there’s **no** prefix common to **all** the strings, return `""` (empty string).

---

## Examples

### Example 1

**Input:** `arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]`
**Output:** `"gee"`
**Explanation:** `"gee"` is the longest common prefix in all the given strings.

### Example 2

**Input:** `arr[] = ["hello", "world"]`
**Output:** `""`
**Explanation:** There’s no common prefix in the given strings.

---

## Constraints

* `1 ≤ |arr| ≤ 10^3`
* `1 ≤ |arr[i]| ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n * min(|arr[i]|))`, where `n` is the number of strings
* **Auxiliary Space:** `O(min(|arr[i]|))`

---

## Company Tags

* VMWare
* Microsoft
* Google

---

## Topic Tags

* Arrays
* Strings
* Data Structures

---

## Related Articles

* *[Longest Common Prefix Using Word By Word Matching](https://www.geeksforgeeks.org/longest-common-prefix-using-word-by-word-matching/)*

---

---

Here’s a crisp, interview-style toolkit for **Longest Common Prefix (LCP)**.

---

## 2) Intuition + Step-by-Step Dry Run

**Goal.** The LCP is the longest string that is a **prefix** of every string in `arr`.

**Key ideas used by common methods**

* If a character position `i` differs in any string, the LCP ends at `i-1`.
* If you sort the strings lexicographically, only the **first** and **last** can differ the most. Their LCP equals the LCP of the whole set.

### Dry run (vertical/character scan)

`arr = ["geeksforgeeks", "geeks", "geek", "geezer"]`

1. Find the shortest length: `minLen = 4` (from `"geek"`).
2. Compare column by column (index `i`):

   * `i=0`: all have `'g'` → keep.
   * `i=1`: all have `'e'` → keep.
   * `i=2`: all have `'e'` → keep.
   * `i=3`: chars are `'k','k','k','z'` → mismatch at `"geezer"[3]='z'`.
     Stop. LCP = `"gee"`.

---

## 3) Optimized Python solutions (with inline interview-style commentary)

### A) Horizontal scan (simple & reliable)

* Start with the first string as the candidate prefix; shrink it until it prefixes every string.
* Time: `O(total characters)` worst-case ≈ `O(n * L)`
* Space: `O(1)` extra.

```python
"""
#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # Edge cases
        if not arr:
            return ""
        if len(arr) == 1:
            return arr[0]
        
        # 1) Take the first string as the current prefix
        prefix = arr[0]
        
        # 2) Reduce prefix until it prefixes each next string
        for s in arr[1:]:
            # While s doesn't start with prefix, chop off last char
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:  # early exit: no common prefix
                    return ""
        
        return prefix
```

### B) Brute/Vertical scan (character by character)

* Compare characters at each index across all strings up to the shortest length.
* Time: `O(n * minLen)`
* Space: `O(1)`.

```python
"""
#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return ""
        # Limit comparisons to the shortest string
        min_len = min(len(s) for s in arr)
        i = 0
        
        # Compare column-by-column
        while i < min_len:
            ch = arr[0][i]
            for s in arr[1:]:
                if s[i] != ch:
                    return arr[0][:i]  # stop at first mismatch
            i += 1
        
        # All min_len characters matched
        return arr[0][:min_len]
```

### C) Sort + compare first and last (very popular in interviews)

* Sort strings; only first and last can differ most. Compute their LCP.
* Time: `O(n log n + L)`
* Space: `O(1)` extra (ignoring sort’s internal memory).

```python
"""
#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return ""
        arr.sort()  # lexicographic
        first, last = arr[0], arr[-1]
        
        # LCP of first and last is the answer
        i, limit = 0, min(len(first), len(last))
        while i < limit and first[i] == last[i]:
            i += 1
        return first[:i]
```

### D) Binary search on length (when strings are very long)

* Binary search length `L` and check if all strings start with the first `L` chars of `arr[0]`.
* Time: `O(n * log(minLen))` checks over prefixes
* Space: `O(1)`.

```python
"""
#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return ""
        
        def ok(L: int) -> bool:
            prefix = arr[0][:L]
            return all(s.startswith(prefix) for s in arr)
        
        lo, hi = 0, min(len(s) for s in arr)
        # Binary search the maximum valid L
        while lo < hi:
            mid = (lo + hi + 1) // 2  # bias to the right
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return arr[0][:lo]
```

> **Which approach to pick?**
>
> * Most interviewers accept **Horizontal scan** or **Sort + first/last** because they’re short, clear, and pass all constraints.
> * Use **Binary search** when strings are extremely long and you want fewer character comparisons.

---

## 4) Quick Interview Q\&A

**Q1. What if there’s an empty string in the array?**
**A.** The answer must be `""`—no non-empty prefix can be common to all strings if one string is empty.

**Q2. Why does comparing the first and last string after sorting work?**
**A.** Sorting groups strings with the same prefixes together. The pair with the maximum possible divergence is the lexicographic **first** and **last** strings; any mismatch they have must also bound the LCP of the whole set.

**Q3. What are the time and space costs of common methods?**

* Horizontal/Vertical scan: `O(n * L)` time, `O(1)` space.
* Sort + first/last: `O(n log n + L)` time, `O(1)` extra space (besides sort).
* Binary search on length: `O(n * log L)` time, `O(1)` space.

**Q4. How would you handle Unicode / case sensitivity?**
**A.** Decide with the interviewer whether to normalize (e.g., `.lower()`, NFC/NFD normalization) before processing.

**Q5. How to adapt this to find the longest common **suffix**?**
**A.** Reverse every string, run any LCP algorithm, then reverse the result.

**Q6. What if the input list is extremely large (streamed)?**
**A.** Use the **horizontal scan** and continuously shrink the current prefix as each new string arrives (stream-friendly, O(1) space beyond the current prefix).

---

---

Awesome—here’s a clean, end-to-end package for **Longest Common Prefix (LCP)** that includes an explanation, multiple interview-ready solutions, and a full runnable program that prints results and measures runtime with `timeit`.

---

# 2) Text explanation + step-by-step dry run

**Problem recap**
Given an array of strings `arr`, return the longest string that is a prefix of **every** string. Return `""` if none exists.

**Key insights**

1. If a character at position `i` differs for any string, the LCP ends at `i-1`.
2. The LCP can never be longer than the shortest string.
3. Sorting puts “closest” strings (lexicographically) at the ends; the LCP of the entire array equals the LCP of the first and last strings after sorting.

**Dry run (vertical scanning)**
Input: `["geeksforgeeks", "geeks", "geek", "geezer"]`

* `minLen = 4` (length of `"geek"`)
* Compare column by column:

| i | chars in all strings | all equal? | prefix so far |
| - | -------------------- | ---------- | ------------- |
| 0 | `g g g g`            | yes        | `"g"`         |
| 1 | `e e e e`            | yes        | `"ge"`        |
| 2 | `e e e e`            | yes        | `"gee"`       |
| 3 | `k k k z`            | **no**     | stop at `i=3` |

Answer: `"gee"`.

---

# 3) Optimized Python solutions (with interview-style comments)

```python
"""
# User function template
class Solution:
    def longestCommonPrefix(self, arr):
        # Choose one of the strategies below (A–D).
        return self.lcp_vertical(arr)

    # A) Horizontal scan — shrink a running prefix
    # Time: O(n * L)   [LCP checks across n-1 strings]
    # Space: O(1)
    def lcp_horizontal(self, arr):
        if not arr:
            return ""
        if len(arr) == 1:
            return arr[0]
        prefix = arr[0]
        for s in arr[1:]:
            # Shrink prefix until s starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    # B) Vertical scan — compare column by column
    # Time: O(n * minLen)
    # Space: O(1)
    def lcp_vertical(self, arr):
        if not arr:
            return ""
        min_len = min(len(s) for s in arr)
        i = 0
        while i < min_len:
            ch = arr[0][i]
            # All strings must have the same char at column i
            for s in arr[1:]:
                if s[i] != ch:
                    return arr[0][:i]
            i += 1
        return arr[0][:min_len]

    # C) Sort + first/last — LCP of the whole array equals LCP(first, last)
    # Time: O(n log n + L)
    # Space: O(1) extra (ignoring sorting’s internal memory)
    def lcp_sort_first_last(self, arr):
        if not arr:
            return ""
        arr = list(arr)     # don’t mutate caller’s list
        arr.sort()
        first, last = arr[0], arr[-1]
        i = 0
        limit = min(len(first), len(last))
        while i < limit and first[i] == last[i]:
            i += 1
        return first[:i]

    # D) Binary search on length — good when strings are very long
    # Time: O(n * log minLen)
    # Space: O(1)
    def lcp_binary_search_length(self, arr):
        if not arr:
            return ""
        def ok(L: int) -> bool:
            p = arr[0][:L]
            return all(s.startswith(p) for s in arr)

        lo, hi = 0, min(len(s) for s in arr)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return arr[0][:lo]
```

**When to pick which**

* **Vertical scan** is usually the simplest and fastest for random small/medium inputs.
* **Horizontal scan** is intuitive; great when the first string is already a good prefix.
* **Sort + first/last** shines when strings are short but count is large (sorting dominates).
* **Binary search length** can be better when strings are very long (e.g., thousands of chars).

---

# 4) Interview Q\&A

**Q1. Why does “sort + first/last” work?**
After sorting, strings that differ earliest in lexicographic order become far apart; the global LCP must be a prefix common to both the first and the last strings—if any string breaks the prefix, one of those two will also break it.

**Q2. What is the lower bound for the answer length?**
`0`. The LCP cannot be longer than the shortest string (`minLen`).

**Q3. Can we do better than O(n \* minLen)?**
Asymptotically for exact LCP of arbitrary strings, no. The binary-search method reduces comparisons to `log(minLen)` rounds but still touches `n` strings per round.

**Q4. How do you handle empty strings?**
If any string is empty, the LCP is `""`.

**Q5. Streaming scenario?**
Maintain a running prefix and shrink it as each new string arrives (horizontal scan).

---

# 5) Full runnable program with timing (prints inputs, outputs, and timeit)

> Paste this into a file and run. It prints results for a few test sets and benchmarks each method using `timeit`.

```python
from timeit import timeit

class Solution:
    # A) Horizontal Scan (Shrink a running prefix)
    # Time: O(n * L)   [n = number of strings, L = length checked per comparison]
    # Space: O(1)
    def lcp_horizontal(self, arr):
        if not arr:
            return ""
        if len(arr) == 1:
            return arr[0]
        prefix = arr[0]
        for s in arr[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    # B) Vertical Scan (Compare column-by-column up to shortest length)
    # Time: O(n * minLen)
    # Space: O(1)
    def lcp_vertical(self, arr):
        if not arr:
            return ""
        min_len = min(len(s) for s in arr)
        i = 0
        while i < min_len:
            ch = arr[0][i]
            for s in arr[1:]:
                if s[i] != ch:
                    return arr[0][:i]
            i += 1
        return arr[0][:min_len]

    # C) Sort + First/Last (LCP equals LCP(first, last) after sort)
    # Time: O(n log n + L)
    # Space: O(1) extra (ignoring sorting’s internal memory)
    def lcp_sort_first_last(self, arr):
        if not arr:
            return ""
        arr = list(arr)  # avoid mutating caller's array
        arr.sort()
        first, last = arr[0], arr[-1]
        i = 0
        limit = min(len(first), len(last))
        while i < limit and first[i] == last[i]:
            i += 1
        return first[:i]

    # D) Binary Search on Length (when strings are very long)
    # Time: O(n * log minLen)
    # Space: O(1)
    def lcp_binary_search_length(self, arr):
        if not arr:
            return ""
        def ok(L: int) -> bool:
            prefix = arr[0][:L]
            return all(s.startswith(prefix) for s in arr)

        lo, hi = 0, min(len(s) for s in arr)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return arr[0][:lo]


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (["geeksforgeeks", "geeks", "geek", "geezer"], "Expected: 'gee'"),
        (["hello", "world"], "Expected: ''"),
        (["interspecies", "interstellar", "interstate"], "Expected: 'inters'"),
        (["a"], "Expected: 'a'"),
        (["", "blank", "blue"], "Expected: ''"),
    ]

    print("=== Outputs ===")
    for arr, note in tests:
        print(f"Input: {arr}")
        print("horizontal:", sol.lcp_horizontal(arr))         # O(n*L), O(1)
        print("vertical  :", sol.lcp_vertical(arr))           # O(n*minLen), O(1)
        print("sorted    :", sol.lcp_sort_first_last(arr))    # O(n log n + L), O(1)
        print("binsearch :", sol.lcp_binary_search_length(arr))  # O(n log minLen), O(1)
        print(note)
        print("-" * 50)

    # Timing each approach on a moderate-size dataset
    big = ["interstellar", "interstate", "internet", "internal", "interval",
           "interlink", "intermix", "intermediate", "inter", "international"] * 200

    print("=== Timing on repeated dataset (length =", len(big), ") ===")
    # Use timeit to measure the full function call repeatedly
    t_h = timeit(lambda: sol.lcp_horizontal(big), number=200)
    t_v = timeit(lambda: sol.lcp_vertical(big), number=200)
    t_s = timeit(lambda: sol.lcp_sort_first_last(big), number=200)
    t_b = timeit(lambda: sol.lcp_binary_search_length(big), number=200)

    print(f"Horizontal scan   : {t_h:.6f} s (200 runs)")
    print(f"Vertical scan     : {t_v:.6f} s (200 runs)")
    print(f"Sort first/last   : {t_s:.6f} s (200 runs)")
    print(f"Binary-search len : {t_b:.6f} s (200 runs)")
```

> When you run the script, it will print outputs for the sample tests and the `timeit` timings (exact numbers vary by machine).

---

# 6) Real-World Use Cases (a few important ones)

* **Autocomplete / command suggestions** – Find the shared prefix of candidate strings to show grayed-out completions or narrow search.
* **File path deduplication** – Compute common root paths when grouping or compressing hierarchical file listings.
* **Network routing / URL prefix matching** – Shared prefixes indicate common subtrees in tries or routing tables.
* **Data compression** – Prefix sharing helps build tries/prefix trees and reduces repeated headers.

