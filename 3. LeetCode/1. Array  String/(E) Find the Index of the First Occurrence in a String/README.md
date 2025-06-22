
---

# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Topics:** Two Pointers, String, String Matching
**Companies:** Frequently asked

---

## Problem Statement

Given two strings `needle` and `haystack`, return the **index of the first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

### Examples:

#### Example 1:

* **Input:**
  `haystack = "sadbutsad"`, `needle = "sad"`
* **Output:**
  `0`
* **Explanation:**
  `"sad"` occurs at index `0` and `6`.
  The first occurrence is at index `0`, so we return `0`.

#### Example 2:

* **Input:**
  `haystack = "leetcode"`, `needle = "leeto"`
* **Output:**
  `-1`
* **Explanation:**
  `"leeto"` did not occur in `"leetcode"`, so we return `-1`.

---

## Constraints:

* `1 <= haystack.length, needle.length <= 10⁴`
* `haystack` and `needle` consist of only lowercase English characters.

---

## Python Code

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Loop through the haystack with a sliding window of length equal to needle
        for i in range(len(haystack) - len(needle) + 1):
            # If the substring from i to i+len(needle) matches, return the index
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1  # If no match is found
```

---

## C++ Code

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int h = haystack.length(), n = needle.length();
        for (int i = 0; i <= h - n; ++i) {
            if (haystack.substr(i, n) == needle)
                return i;
        }
        return -1;
    }
};
```

---

## JavaScript Code

```javascript
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for (let i = 0; i <= haystack.length - needle.length; i++) {
        if (haystack.slice(i, i + needle.length) === needle) {
            return i;
        }
    }
    return -1;
};
```

---

## Step-by-step Dry Run:

**Input:**
`haystack = "sadbutsad"`, `needle = "sad"`

* Slide over:

  1. `"sad"` == `"sad"` → match at index 0 → return `0`

**Input:**
`haystack = "leetcode"`, `needle = "leeto"`

* Slide over:

  1. `"leetc"` ≠ `"leeto"`
  2. `"eetco"` ≠ `"leeto"`
     ...
     No match → return `-1`

---

## Interview Questions You Might Be Asked:

1. **Q:** How would you solve this without using built-in functions?
   **A:** Use a sliding window to compare substrings manually.

2. **Q:** Can you optimize this using KMP algorithm?
   **A:** Yes, KMP (Knuth-Morris-Pratt) preprocesses the needle with prefix function to skip unnecessary comparisons.

3. **Q:** How does time complexity behave in your approach?
   **A:** O(n \* m) in worst case where n = length of haystack, m = length of needle.

---

Here are **both the KMP (Knuth-Morris-Pratt)** and **Rabin-Karp** algorithms implemented in **Python** to solve the **"Find the Index of the First Occurrence in a String"** problem.

---

## ✅ KMP Algorithm (Prefix Table Optimization)

### Time Complexity: `O(n + m)`

* `n` = length of `haystack`, `m` = length of `needle`

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build the prefix table (LPS array)
        lps = [0] * len(needle)
        length = 0  # length of the previous longest prefix suffix

        # Preprocess the pattern (needle)
        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Search the pattern in the text
        i = j = 0  # i for haystack, j for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j  # Match found

            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1  # No match found
```

---

## ✅ Rabin-Karp Algorithm (Hash Rolling)

### Time Complexity: `O(n)` average, `O(nm)` worst-case

* Good for multiple pattern matching or large `needle` values

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        base = 256  # number of characters in the input charset (ASCII)
        mod = 10**9 + 7  # large prime number to mod hash values
        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        # Precompute base^(m-1) % mod
        h = 1
        for _ in range(m - 1):
            h = (h * base) % mod

        # Compute hash of needle and initial window of haystack
        needle_hash = 0
        window_hash = 0
        for i in range(m):
            needle_hash = (base * needle_hash + ord(needle[i])) % mod
            window_hash = (base * window_hash + ord(haystack[i])) % mod

        # Slide the window
        for i in range(n - m + 1):
            if needle_hash == window_hash:
                # Check the actual substring to prevent hash collision
                if haystack[i:i + m] == needle:
                    return i

            if i < n - m:
                # Remove leftmost character and add next character
                window_hash = (window_hash - ord(haystack[i]) * h) % mod
                window_hash = (window_hash * base + ord(haystack[i + m])) % mod
                window_hash = (window_hash + mod) % mod  # handle negative

        return -1
```

---

## ✅ Summary Table

| Algorithm  | Time Complexity | Space | Notes                              |
| ---------- | --------------- | ----- | ---------------------------------- |
| KMP        | O(n + m)        | O(m)  | Good for repeated patterns         |
| Rabin-Karp | O(n) avg        | O(1)  | Hash-based, great for multi-search |

Let me know if you want dry runs or visualization for either!
