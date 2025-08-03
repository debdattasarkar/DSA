Here is a README in Markdown format based on the content of the fifth uploaded image:

---

# Longest Palindromic Substring

## Introduction

The **Longest Palindromic Substring** problem is a classic string manipulation challenge where the task is to find the longest substring within a given string that reads the same forward and backward. If multiple substrings with the same maximum length exist, the one with the **least starting index** should be returned.

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

* A **substring** is a contiguous sequence of characters within a string.
* A **palindrome** is a string that reads the same forwards and backwards. Formally, `s` is palindromic if `reverse(s) == s`.

If multiple longest palindromic substrings exist, return the one that starts earliest.

---

## Examples

### Example 1

```
Input: s = "aaaabbaaa"  
Output: "aabbaa"  
Explanation: The longest palindrome in the string is "aabbaa".
```

### Example 2

```
Input: s = "geeks"  
Output: "ee"  
Explanation: The longest palindrome in the string is "ee".
```

---

## Constraints

* `1 ≤ |s| ≤ 10^4`

---

## Expected Complexity

* **Time Complexity**: O(n²)
* **Auxiliary Space**: O(1)

---

## Tags

### Company Tags

`Zoho`, `Accolite`, `Amazon`, `Microsoft`, `Samsung`, `MakeMyTrip`, `Visa`, `Walmart`, `Qualcomm`, `Groupon`

### Topic Tags

`Strings`, `Data Structures`, `Dynamic Programming`

---

## Related Content

* **Interview Experiences**:

  * Accolite Interview Experience Set 4 On Campus
  * Samsung Research Institute Bangalore Srib Intern
  * Amazon Interview Experience Set 412 SDE 1

* **Article**: [Longest Palindromic Substring](#)

---

Here’s a full **text explanation with dry run** and **Python / C++ / JavaScript code** for the **Longest Palindromic Substring** problem shown in the image.

---

## 🔍 Problem Summary

Given a string `s`, return the **longest palindromic substring**. A palindrome reads the same forwards and backwards.

* If multiple such substrings exist, return the one with the **least starting index**.
* Substring must be **contiguous**.

---

## 🧠 Idea: Expand Around Center

For every character (and every gap between characters), treat it as a **potential center** of a palindrome and expand outwards while characters match.

### Time Complexity: O(n²)

### Space Complexity: O(1)

---

## 🔄 Dry Run

**Input:** `s = "aaaabbbaa"`

* Check centers:

  * Center at index 3 (char `'a'`) → expand: `aabbaaa` → not a palindrome
  * Center at indices 3 & 4 (double `'b'`) → expand: `"aabbbaa"` → ✅
* Longest palindrome found: `"aabbbaa"`

---

## ✅ Python Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i in range(len(s)):
            # Odd-length palindromes
            l1, r1 = self.expandAroundCenter(s, i, i)
            # Even-length palindromes
            l2, r2 = self.expandAroundCenter(s, i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    string longestPalindrome(string s) {
        int start = 0, end = 0;

        for (int i = 0; i < s.size(); i++) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i + 1);
            int len = max(len1, len2);

            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        return s.substr(start, end - start + 1);
    }

    int expand(string& s, int left, int right) {
        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    longestPalindrome(s) {
        let start = 0, end = 0;

        for (let i = 0; i < s.length; i++) {
            let [l1, r1] = this.expand(s, i, i);
            let [l2, r2] = this.expand(s, i, i + 1);

            if (r1 - l1 > end - start) {
                start = l1;
                end = r1;
            }

            if (r2 - l2 > end - start) {
                start = l2;
                end = r2;
            }
        }

        return s.slice(start, end + 1);
    }

    expand(s, left, right) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return [left + 1, right - 1];
    }
}
```

---

## 📌 Final Notes

* We explore both odd and even length palindromes by checking single and double character centers.
* This avoids needing a full DP table and stays optimal for up to 10⁴ characters.
