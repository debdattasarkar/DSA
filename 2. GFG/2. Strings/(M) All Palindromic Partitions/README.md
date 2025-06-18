Here is the full **README-style** documentation for the problem **"All Palindromic Partitions"**, including all examples, constraints, complexities, company tags, topic tags, and links.

---

# All Palindromic Partitions

**Difficulty:** Medium
**Accuracy:** 61.47%
**Submissions:** 25K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given a string `s`, find all possible ways to partition it such that every substring in the partition is a palindrome.

---

## Examples

### Example 1:

**Input:**
`s = "geeks"`
**Output:**
`[[g, e, e, k, s], [g, ee, k, s]]`
**Explanation:**
`[g, e, e, k, s]` and `[g, ee, k, s]` are the only partitions of `"geeks"` where each substring is a palindrome.

### Example 2:

**Input:**
`s = "abcba"`
**Output:**
`[[a, b, c, b, a], [a, bcb, a], [abcba]]`
**Explanation:**
`[a, b, c, b, a]`, `[a, bcb, a]` and `[abcba]` are the only partitions of `"abcba"` where each substring is a palindrome.

---

## Constraints

* $1 \leq s.size() \leq 20$

---

## Expected Complexities

* **Time Complexity:** $O(2^n \cdot n)$
* **Auxiliary Space:** $O(2^n \cdot n)$

---

## Company Tags

* Amazon
* Microsoft
* Facebook

---

## Topic Tags

* Strings
* Dynamic Programming
* Recursion
* Backtracking
* Palindrome
* Data Structures
* Algorithms

---

## Related Articles

* [Given A String Print All Possible Palindromic Partition](https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/)
* [Print Palindromic Partitions String](https://www.geeksforgeeks.org/print-palindromic-partitions-string/)

---

Sure! Here's a complete explanation with step-by-step dry run, followed by **optimized backtracking + palindrome checking** code in **Python**, **C++**, and **JavaScript**, as expected in technical interviews.

---

### 🔍 Problem Explanation

Given a string `s`, find **all possible partitions** of the string such that **each substring** in the partition is a **palindrome**.

A **palindromic partition** splits the string into parts where **each part reads the same forward and backward**.

---

### 🧠 Approach (Backtracking)

1. Start from index `0`, explore all possible substrings `s[0:i]`.
2. If a substring is a palindrome:

   * Include it in the current path.
   * Recurse for the remaining string.
   * Backtrack and remove the last substring to try the next possibility.
3. If the end of string is reached, store the current partition.
4. Return all such paths.

---

### ✅ Time and Space Complexity

* **Time Complexity**: $O(2^n \cdot n)$
  There are $2^n$ partitions possible, and checking each partition's palindrome takes $O(n)$ time.

* **Auxiliary Space**: $O(n)$ recursion + $O(2^n \cdot n)$ output space.

---

### 🧪 Dry Run

**Input:** `s = "aab"`
**Palindrome partitions:**

* \["a", "a", "b"]
* \["aa", "b"]

Step-by-step:

1. `""` → `"a"` → is palindrome → go deeper
2. `"a"` → `"a"` → is palindrome → go deeper
3. `"a", "a"` → `"b"` → is palindrome → save \["a", "a", "b"]
4. backtrack → try `"aa"` → is palindrome → go deeper
5. `"aa"` → `"b"` → is palindrome → save \["aa", "b"]
6. Done.

---

### 🐍 Python Code

```python
class Solution:
    def palinParts(self, s):
        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if isPalindrome(part):
                    path.append(part)
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result
```

---

### 💠 C++ Code

```cpp
class Solution {
public:
    bool isPalindrome(const string &s, int l, int r) {
        while (l < r)
            if (s[l++] != s[r--]) return false;
        return true;
    }

    void backtrack(string &s, int start, vector<string> &path, vector<vector<string>> &res) {
        if (start == s.size()) {
            res.push_back(path);
            return;
        }
        for (int end = start; end < s.size(); ++end) {
            if (isPalindrome(s, start, end)) {
                path.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1, path, res);
                path.pop_back();
            }
        }
    }

    vector<vector<string>> palinParts(string &s) {
        vector<vector<string>> res;
        vector<string> path;
        backtrack(s, 0, path, res);
        return res;
    }
};
```

---

### 🌐 JavaScript Code

```javascript
class Solution {
    palinParts(s) {
        const res = [];

        const isPalindrome = (str) => {
            let l = 0, r = str.length - 1;
            while (l < r) {
                if (str[l++] !== str[r--]) return false;
            }
            return true;
        };

        const backtrack = (start, path) => {
            if (start === s.length) {
                res.push([...path]);
                return;
            }

            for (let end = start + 1; end <= s.length; end++) {
                const part = s.substring(start, end);
                if (isPalindrome(part)) {
                    path.push(part);
                    backtrack(end, path);
                    path.pop();
                }
            }
        };

        backtrack(0, []);
        return res;
    }
}
```

---


Great! Here's a detailed **set of interviewer questions along with ideal answers** for the **All Palindromic Partitions** problem, just as you’d want to answer in a technical interview:

---

### ✅ 1. **What is a palindrome?**

**Answer:**
A palindrome is a string that reads the same forward and backward. For example, `"aba"` and `"aa"` are palindromes, but `"ab"` is not.

---

### ✅ 2. **What does it mean to partition a string?**

**Answer:**
It means breaking the string into substrings such that the concatenation of all substrings gives the original string. For example, `"aab"` can be partitioned as `["a", "a", "b"]`, or `["aa", "b"]`.

---

### ✅ 3. **Why is backtracking a suitable approach here?**

**Answer:**
Because we need to try all possible partitions and check whether each partition is valid (i.e., all parts are palindromes). Backtracking allows us to explore each possibility and undo choices if they don’t lead to a valid result.

---

### ✅ 4. **What is the base case in your recursion?**

**Answer:**
When the start index reaches the end of the string (`index == len(s)`), it means we’ve formed a valid partition, so we add it to the result.

---

### ✅ 5. **What is the time complexity of your solution?**

**Answer:**
The time complexity is `O(2^n * n)`:

* There are `2^n` ways to partition a string of length `n` (each character can be the start of a new substring or not).
* For each partition, checking if substrings are palindromes can take `O(n)` time.

---

### ✅ 6. **Can this be optimized with dynamic programming?**

**Answer:**
Yes. We can cache results of palindrome checks in a 2D `dp` table `dp[i][j] = True` if `s[i:j+1]` is a palindrome. This avoids recomputing palindromic substrings.

---

### ✅ 7. **What edge cases should we test?**

**Answer:**

* `"aab"` – multiple valid partitions
* `"aaa"` – many repeated palindromes
* `"abc"` – all characters are single palindrome parts
* `""` – empty string (return `[[]]` or `[]` depending on spec)
* `"a"` – one character is trivially a palindrome

---

### ✅ 8. **What if the string length is very large?**

**Answer:**
For `n > 20`, the exponential time complexity becomes impractical. We can then:

* Use iterative DP
* Return only counts instead of lists
* Return only one valid partition

---

### ✅ 9. **How do you prove your solution is correct and optimal?**

**Answer:**

* It explores all valid partitions using DFS + backtracking.
* Only palindromic substrings are allowed at each stage.
* It avoids redundant substring generation via memoization if needed.

---

### ✅ 10. **How would you test this in production?**

**Answer:**

* Write unit tests for known inputs and edge cases.
* Log recursion depth to ensure no stack overflows.
* Use a fuzzer to generate random palindromic strings to verify output.
* If using memoization, test cache hits/misses.

---

### ✅ 11. **Would an iterative solution be better than recursion?**

**Answer:**
Recursion is natural here because of the tree-like structure of decisions. Iterative solutions using stacks are possible but more verbose and harder to manage for partitioning problems.

---

### ✅ 12. **Give a dry run for `"aab"`**

**Answer:**

```
Start with index 0:
  "a" is palindrome
    -> check "a" from index 1
      "a" is palindrome
        -> check "b" from index 2
          "b" is palindrome → [“a”, “a”, “b”]
      "ab" is not
  "aa" is palindrome
    -> check "b" from index 2
      "b" is palindrome → [“aa”, “b”]
  "aab" is not a palindrome

Result: [["a", "a", "b"], ["aa", "b"]]
```

---
