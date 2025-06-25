
---

# 392. Is Subsequence

**Difficulty**: Easy
**Topics**: Two Pointers, Dynamic Programming
**Companies**: Frequently asked in FAANG

---

### Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

---

### Definition

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters **without disturbing the relative positions** of the remaining characters.

For example:

* `"ace"` is a subsequence of `"abcde"` ✅
* `"aec"` is **not** a subsequence of `"abcde"` ❌

---

### Examples

**Example 1**:

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2**:

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

---

### Constraints:

* `0 <= s.length <= 100`
* `0 <= t.length <= 10^4`
* `s` and `t` consist only of lowercase English letters.

---

### Follow-up

Suppose there are lots of incoming `s`, say `s1`, `s2`, ..., `sk` where `k >= 10^9`, and you want to check one by one to see if `t` has its subsequence.
In this scenario, how would you change your code?

---

Here is the complete explanation, dry run, and code in Python, C++, and JavaScript for **Leetcode 392. Is Subsequence**, followed by possible **interview questions and answers**.

---

## 🔍 Problem Summary

Given two strings `s` and `t`, check whether `s` is a subsequence of `t`. A **subsequence** means the characters in `s` appear in `t` in the same relative order, but not necessarily contiguously.

---

## ✅ Step-by-Step Explanation with Dry Run

### Example:

```
s = "abc"
t = "ahbgdc"
```

### Dry Run (Two-pointer technique):

1. Pointer `i = 0` (points to s), `j = 0` (points to t)
2. Compare `s[0] = 'a'` with `t[0] = 'a'` → match → `i = 1`, `j = 1`
3. Compare `s[1] = 'b'` with `t[1] = 'h'` → no match → `j = 2`
4. Compare `s[1] = 'b'` with `t[2] = 'b'` → match → `i = 2`, `j = 3`
5. Compare `s[2] = 'c'` with `t[3] = 'g'` → no match → `j = 4`
6. Compare `s[2] = 'c'` with `t[4] = 'd'` → no match → `j = 5`
7. Compare `s[2] = 'c'` with `t[5] = 'c'` → match → `i = 3` (end of `s`)

✅ All characters in `s` matched in order → return `True`.

---

## 💡 Time and Space Complexity

* **Time Complexity**: O(n), where n = length of `t`
* **Space Complexity**: O(1), constant space used

---

## 🔠 Python Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move on in s if match found
            j += 1      # always move in t
        return i == len(s)  # if i reached end, s is subsequence
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) i++; // match found, move in s
            j++;                   // always move in t
        }
        return i == s.length();    // true if all s matched
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let i = 0, j = 0;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) i++; // move in s if match
        j++;                    // always move in t
    }
    return i === s.length;      // true if all s matched
};
```

---

## 🎯 Common Interview Questions & Answers

### Q1: What is the difference between a **subsequence** and a **substring**?

**A**: A substring requires characters to be contiguous, while a subsequence allows characters to be selected while preserving relative order, not necessarily contiguity.

---

### Q2: Can this be solved using dynamic programming?

**A**: It can be, but that would be overkill for this problem. A greedy two-pointer solution suffices and is optimal in time and space.

---

### Q3: How would you handle **multiple `s` queries** with the same `t` (Follow-up)?

**A**: Preprocess `t` using a hashmap of character positions (binary search on indices). This allows each `s` to be checked in O(m log n), where m = len(s), n = len(t). Use a trie or indexed map for optimization.

---

### Q4: Can this be done recursively?

**A**: Yes. Base case: if `s` is empty → return `True`; if `t` is empty → return `False`; otherwise, check first char match and recurse.

---
