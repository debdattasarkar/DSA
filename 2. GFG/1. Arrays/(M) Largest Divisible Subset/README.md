Here is the complete README-style conversion of the problem **"Largest Divisible Subset"**, preserving every detail from the image:

---

# 📘 Largest Divisible Subset

**Difficulty:** Medium
**Accuracy:** 43.71%
**Submissions:** 8K+
**Points:** 4
**Average Time:** 20m

---

## 🧾 Problem Statement

Given an array `arr[]` of distinct positive integers. Your task is to find the **largest subset** such that for every pair of elements `(x, y)` in the subset, **either `x` divides `y` or `y` divides `x`**.

> **Note:**
> If multiple subsets of the same maximum length exist, return the one that is **lexicographically greatest**, after sorting the subset in ascending order.

---

## 📌 Examples

### Example 1:

```
Input: arr[] = [1, 16, 7, 8, 4]
Output: [1, 4, 8, 16]
Explanation: The largest divisible subset is [1, 4, 8, 16], where each element divides the next one. This subset is already the lexicographically greatest one.
```

### Example 2:

```
Input: arr[] = [2, 4, 3, 8]
Output: [2, 4, 8]
Explanation: The largest divisible subset is [2, 4, 8], where each element divides the next one. This subset is already the lexicographically greatest one.
```

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10^3`
* `1 ≤ arr[i] ≤ 10^9`

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n²)
* **Auxiliary Space:** O(n)

---

## 💼 Company Tags

* Bloomberg
* Facebook
* Adobe
* Google
* Amazon
* Apple
* Microsoft
* Yahoo

---

## 🏷️ Topic Tags

* Dynamic Programming
* Sorting
* Arrays

---

## 📚 Related Articles

* [Largest Divisible Subset Array](https://www.geeksforgeeks.org/largest-divisible-subset/)

---
Absolutely! Based on the **correct Python code you shared**, here are the **equivalent implementations** in:

---

### ✅ Python

```python
class Solution:
    def largestSubset(self, arr):
        arr.sort()
        n = len(arr)
        idx, l = n-1, 1
        dp = [(1, None) for _ in range(n)]

        for i in range(n-1, -1, -1):
            li, k = dp[i]
            for j in range(i+1, n):
                if arr[j] % arr[i] == 0:
                    if dp[j][0] + 1 >= li:
                        li = dp[j][0] + 1
                        k = j
            dp[i] = (li, k)
            if li > l:
                idx = i
                l = li

        ans = []
        while idx is not None:
            ans.append(arr[idx])
            idx = dp[idx][1]
        return ans
```

---

### ✅ C++

```cpp
class Solution {
public:
    vector<int> largestSubset(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int n = arr.size();
        vector<pair<int, int>> dp(n, {1, -1}); // {length, next_index}
        int maxLen = 1, startIdx = n - 1;

        for (int i = n - 1; i >= 0; --i) {
            int len = 1, next = -1;
            for (int j = i + 1; j < n; ++j) {
                if (arr[j] % arr[i] == 0) {
                    if (dp[j].first + 1 >= len) {
                        len = dp[j].first + 1;
                        next = j;
                    }
                }
            }
            dp[i] = {len, next};
            if (len > maxLen) {
                maxLen = len;
                startIdx = i;
            }
        }

        vector<int> result;
        while (startIdx != -1) {
            result.push_back(arr[startIdx]);
            startIdx = dp[startIdx].second;
        }
        return result;
    }
};
```

---

### ✅ JavaScript

```javascript
class Solution {
    largestSubset(arr) {
        arr.sort((a, b) => a - b);
        const n = arr.length;
        const dp = Array.from({ length: n }, () => [1, null]);
        let maxLen = 1, startIdx = n - 1;

        for (let i = n - 1; i >= 0; i--) {
            let len = 1, next = null;
            for (let j = i + 1; j < n; j++) {
                if (arr[j] % arr[i] === 0) {
                    if (dp[j][0] + 1 >= len) {
                        len = dp[j][0] + 1;
                        next = j;
                    }
                }
            }
            dp[i] = [len, next];
            if (len > maxLen) {
                maxLen = len;
                startIdx = i;
            }
        }

        const result = [];
        while (startIdx !== null) {
            result.push(arr[startIdx]);
            startIdx = dp[startIdx][1];
        }
        return result;
    }
}
```

---
Here's a set of **mock interview-style questions and answers** related to the **"Largest Divisible Subset"** problem — tailored as it might be in a real coding or system design round:

---

### 🔹 **1. Can you describe what the problem is asking for?**

**Candidate:**
Yes. We're given an array of positive integers, and we need to find the largest subset where for every pair `(Si, Sj)` in the subset, either `Si % Sj == 0` or `Sj % Si == 0`. The result should be the largest possible such subset in size.

---

### 🔹 **2. What's your initial approach to solve this?**

**Candidate:**
A brute force approach would be to generate all subsets and check the divisibility condition for each — which is exponential and not feasible. So instead, I sort the array and use dynamic programming to build the longest valid subset chain from the end.

---

### 🔹 **3. Why do you sort the array first?**

**Candidate:**
Sorting ensures that we can safely check if a larger number is divisible by a smaller one. This helps to naturally form increasing divisible chains without skipping smaller compatible elements.

---

### 🔹 **4. What's stored in your DP structure and why?**

**Candidate:**
I use a `dp` array where each element stores a tuple:
`(length of the longest divisible subset starting from index i, next index in the chain)`
This helps in two ways:

* To build the maximum subset size efficiently.
* To reconstruct the actual subset using the backtracking chain.

---

### 🔹 **5. What's the time and space complexity of your solution?**

**Candidate:**

* **Time complexity:** O(n²) due to the nested loops to check divisibility for every pair.
* **Space complexity:** O(n) to store the DP and reconstruction chain.

---

### 🔹 **6. Could this be optimized further?**

**Candidate:**
There is no known faster algorithm than O(n²) since we must check divisibility pairwise. But space can be slightly optimized by storing only lengths if the subset reconstruction isn't needed.

---

### 🔹 **7. What if all elements in the array are prime?**

**Candidate:**
In that case, no two elements will divide each other, so the answer would be any single element — all are valid size-1 subsets.

---

### 🔹 **8. How does your solution handle duplicates?**

**Candidate:**
Since duplicates are allowed, and all divisibility checks are `arr[j] % arr[i] == 0`, duplicates can be part of the chain. The algorithm will naturally form valid chains with repeated values.

---

### 🔹 **9. How would you test this in production or at scale?**

**Candidate:**

* Start with unit tests: edge cases like size 0, size 1, all primes, all powers of 2.
* Stress test with large arrays (10⁴ elements).
* Log subset length to monitor performance.
* Add checks for sorted input or use memoization to cache divisibility checks if reused.

---

### 🔹 **10. Can you modify your solution to return only the length of the largest subset instead of the subset itself?**

**Candidate:**
Yes. I can remove the tracking of the next index and just keep track of the maximum `dp[i][0]` value across all `i`, which gives me the maximum length.

---

Below are **interview questions** related to the `romanToInt()` function, along with **clear answers** and code references where applicable.

---

## ✅ Function Recap

The function:

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for ch in reversed(s):
            val = roman[ch]
            total += val if val >= prev else -val
            prev = val
        return total
```

---

## 🎯 Common Interview Questions & Answers

---

### 🔸 Q1: **What is the time and space complexity of your solution?**

**A**:

* **Time Complexity**: O(n), where n is the length of the input string.
* **Space Complexity**: O(1), since the mapping dictionary size is fixed (7 symbols).

---

### 🔸 Q2: **Why do you traverse the string from right to left?**

**A**:
Because Roman numerals subtract when a smaller numeral appears *before* a larger one (e.g., `IV` = 4).

* By traversing from **right to left**, we can check if the **current value** is less than the **previous one** (to the right).
* This allows us to easily subtract when needed without looking ahead.

---

### 🔸 Q3: **Can you implement the reverse — Integer to Roman?**

**A**: Yes, using a greedy subtraction approach:

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        val_sym = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = ""
        for val, sym in val_sym:
            while num >= val:
                res += sym
                num -= val
        return res
```

---

### 🔸 Q4: **Can you validate if a Roman numeral is valid?**

**A**:
Validation includes checking for:

* No more than 3 repetitions (`XXXX` is invalid)
* Subtractive patterns (`IL` is invalid, only `IV`, `IX`, `XL`, etc. are allowed)

**Idea**: Use regular expression or build a finite automaton.

---

### 🔸 Q5: **Can you do it without reversing the string?**

**A**:
Yes, using left-to-right traversal with a look-ahead:

```python
def romanToInt(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total
```

---

### 🔸 Q6: **What design changes would you make to support extended Roman numerals (> 3999)?**

**A**:
Introduce a way to handle overlined letters representing 1000× multiplier. For example:

* An overlined `V̄` = 5000
* Can be simulated using a `__` prefix (`__V`) or added in a mapping.

---

### 🔸 Q7: **Which DSA pattern does this problem follow?**

**A**:
Reverse traversal + comparison with previous element (similar to two-pointer or greedy pattern), optimized for Roman numeral rules.

---

### 🔸 Q8: **How would you test this function?**

**A**:
Test basic, subtractive, and edge cases:

```python
assert romanToInt("III") == 3
assert romanToInt("IV") == 4
assert romanToInt("IX") == 9
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994
assert romanToInt("MMMCMXCIX") == 3999
```

---

### 🔸 Q9: **What if the input is lowercase or invalid characters?**

**A**:
Enhance with input validation:

```python
if any(ch not in roman for ch in s.upper()):
    raise ValueError("Invalid Roman numeral")
```

---

### 🔸 Q10: **Can you make it object-oriented (OOP style)?**

**A**:

```python
class RomanConverter:
    def __init__(self):
        self.roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    def to_integer(self, s: str) -> int:
        total = 0
        prev = 0
        for ch in reversed(s):
            val = self.roman[ch]
            total += val if val >= prev else -val
            prev = val
        return total
```

---
