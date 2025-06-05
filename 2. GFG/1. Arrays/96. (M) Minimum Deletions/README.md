Here is a complete `README.md` in Markdown format based on the problem statement from the provided image:

---

# 🧩 Minimum Deletions to Make a Palindrome

## 📝 Problem Statement

Given a string `s`, write a program to **delete the minimum number of characters** from the string so that the resultant string is a **palindrome**, while maintaining the original order of characters.

### A palindrome:

A string that reads the same forwards and backwards.

---

## 📥 Input

* A single string `s` of lowercase English letters.

## 📤 Output

* An integer representing the minimum number of characters that need to be deleted to make the string a palindrome.

---

## 🔍 Examples

### Example 1

```
Input:  s = "aecbcda"
Output: 2
Explanation: Remove characters 'e' and 'd' to get "acbca", which is a palindrome.
```

### Example 2

```
Input:  s = "geeksforgeeks"
Output: 8
Explanation: 
- Longest palindromic subsequence is "eefee" (length = 5)
- String length = 13
- Minimum deletions = 13 - 5 = 8
```

---

## ✅ Constraints

* `1 <= s.length <= 10^3`

---

## 💡 Approach

To solve this problem:

1. Identify the **Longest Palindromic Subsequence (LPS)** in the string.
2. The **minimum deletions** required = `length of s - length of LPS`.

Use **Dynamic Programming** to find the LPS in `O(n^2)` time.

---

## ⏱️ Complexity

* **Time Complexity**: `O(n^2)`
* **Space Complexity**: `O(n)`

---

## 🏷️ Tags

* Strings
* Dynamic Programming
* Algorithms
* Data Structures

---

## 📚 Related Topics

* [Minimum Number Deletions Make String Palindrome](https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/)

---

Sure! Here's a **detailed explanation with a step-by-step dry run** and **code in Python, C++, and JavaScript**, complete with inline comments.

---

## 🔍 Problem Summary

Given a string `s`, delete the minimum number of characters to make it a palindrome. You **must maintain the order of characters**.

---

## 💡 Explanation & Dry Run

### Key Insight:

We **do not need to actually delete characters**. We need to **find the longest palindromic subsequence (LPS)**.
Then the **minimum deletions = len(s) - len(LPS)**

---

### 🧪 Dry Run:

**Input**: `"aecbcda"`

**Step 1: Find LPS**

We check subsequences like:

* `"a"`, `"c"`, `"bcb"`, `"acbca"`

The **longest palindromic subsequence is `"acbca"`**, length = 5

**Step 2: Calculate minimum deletions**

* Length of string = 7
* LPS length = 5
* Minimum deletions = 7 - 5 = **2**

---

## ✅ Approach

1. Use Dynamic Programming to find the **LPS** of the string.
2. The LPS of a string `s` is the **Longest Common Subsequence (LCS)** between `s` and its reverse.
3. Compute LCS using bottom-up DP.

---

## 🐍 Python Code

```python
class Solution:
    def minDeletions(self, s):
        n = len(s)
        rev = s[::-1]  # reverse the string

        # dp[i][j] = LCS of s[0:i] and rev[0:j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # minimum deletions = total length - LPS length
        return n - dp[n][n]
```

---

## 💻 C++ Code

```cpp
class Solution {
  public:
    int minDeletions(string s) {
        int n = s.size();
        string rev = s;
        reverse(rev.begin(), rev.end());

        // DP table to find LCS of s and reversed s
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == rev[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        return n - dp[n][n]; // total length - length of LPS
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    /**
     * @param {string} s
     * @returns {number}
     */
    minDeletions(s) {
        const n = s.length;
        const rev = s.split('').reverse().join('');

        // Initialize DP table
        const dp = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));

        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (s[i - 1] === rev[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return n - dp[n][n]; // min deletions = total - LPS
    }
}
```

---
