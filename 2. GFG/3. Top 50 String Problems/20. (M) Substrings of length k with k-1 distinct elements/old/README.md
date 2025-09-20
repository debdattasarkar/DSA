
---

# Substrings of Length K with K-1 Distinct Elements

### 🟡 Difficulty: Medium

**Accuracy:** 57.85%
**Submissions:** 24K+
**Points:** 4
**Average Time:** 15 minutes

---

## 🧩 Problem Statement

Given a string `s` consisting only of lowercase alphabets and an integer `k`, find the **count** of all substrings of length `k` which have exactly **k - 1 distinct characters**.

---

## 🔍 Examples

### Example 1:

**Input:**
`s = "abcc", k = 2`
**Output:**
`1`

**Explanation:**
Possible substrings of length `k = 2` are:

* `ab` → 2 distinct characters
* `bc` → 2 distinct characters
* `cc` → 1 distinct character ✅

Only one valid substring, so count is **1**.

---

### Example 2:

**Input:**
`s = "aabab", k = 3`
**Output:**
`3`

**Explanation:**
Possible substrings of length `k = 3` are:

* `aab` → 2 distinct characters ✅
* `aba` → 2 distinct characters ✅
* `bab` → 2 distinct characters ✅

All these substrings are valid, so the total count is **3**.

---

## 🔒 Constraints

* `1 ≤ s.length ≤ 10⁵`
* `2 ≤ k ≤ 27`

---

## ⏱ Expected Time and Space Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## 💼 Company Tags

* Amazon

---

## 🧠 Topic Tags

* Sliding Window
* Strings
* Data Structures
* Algorithms

---

## 📚 Related Interview Experiences

* Amazon Interview Experience for SDE 1 Full Time Referral 2020

---

## 📖 Related Articles

* [Count Of Substrings Of Length K With Exactly K Distinct Characters](https://www.geeksforgeeks.org/count-substrings-of-length-k-with-k-distinct-characters/)

---

# 📘 Problem: Substrings of Length K with K-1 Distinct Elements

---

## 🔍 Step-by-Step Explanation

**Goal:** Count how many substrings of length `k` in a string `s` have exactly `k - 1` distinct characters.

### ✅ Key Idea:

We use a **sliding window** of size `k`, and for each window, we:

* Count the number of distinct characters.
* If it equals `k - 1`, we increase our result counter.

---

### 🧪 Dry Run

#### Input:

`s = "aabab", k = 3`

#### Substrings of length 3:

1. `"aab"` → Distinct: `{'a', 'b'}` → count = 2 ✅
2. `"aba"` → Distinct: `{'a', 'b'}` → count = 2 ✅
3. `"bab"` → Distinct: `{'b', 'a'}` → count = 2 ✅

👉 All three substrings meet the condition → **Answer = 3**

---

### ⚙️ Sliding Window Optimization:

* We slide the window of size `k` through the string.
* Maintain a **frequency map** (`char_count`) for characters in the current window.
* Use a variable `distinct` to track how many unique characters are in the window.
* As we slide:

  * Remove the character that exits the window.
  * Add the new character that enters.
  * Update the `distinct` count accordingly.

---

## ✅ Optimized Code Implementations

---

### 🐍 Python

```python
class Solution:
    def substrCount(self, s, k):
        from collections import defaultdict

        n = len(s)
        if k > n:
            return 0

        char_count = defaultdict(int)
        distinct = 0
        result = 0

        # Initialize the first window
        for i in range(k):
            if char_count[s[i]] == 0:
                distinct += 1
            char_count[s[i]] += 1

        if distinct == k - 1:
            result += 1

        # Slide the window
        for i in range(k, n):
            left_char = s[i - k]
            right_char = s[i]

            # Remove leftmost character
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                distinct -= 1

            # Add rightmost character
            if char_count[right_char] == 0:
                distinct += 1
            char_count[right_char] += 1

            if distinct == k - 1:
                result += 1

        return result
```

---

### 💠 C++

```cpp
class Solution {
  public:
    int substrCount(string &s, int k) {
        int n = s.size();
        if (k > n) return 0;

        unordered_map<char, int> char_count;
        int distinct = 0, result = 0;

        // First window
        for (int i = 0; i < k; ++i) {
            if (char_count[s[i]] == 0) distinct++;
            char_count[s[i]]++;
        }

        if (distinct == k - 1) result++;

        for (int i = k; i < n; ++i) {
            char left_char = s[i - k];
            char right_char = s[i];

            // Remove old char
            char_count[left_char]--;
            if (char_count[left_char] == 0) distinct--;

            // Add new char
            if (char_count[right_char] == 0) distinct++;
            char_count[right_char]++;

            if (distinct == k - 1) result++;
        }

        return result;
    }
};
```

---

### 🌐 JavaScript

```javascript
class Solution {
    substrCount(s, k) {
        const n = s.length;
        if (k > n) return 0;

        const charCount = new Map();
        let distinct = 0, result = 0;

        // Initialize first window
        for (let i = 0; i < k; i++) {
            if (!charCount.has(s[i])) distinct++;
            charCount.set(s[i], (charCount.get(s[i]) || 0) + 1);
        }

        if (distinct === k - 1) result++;

        for (let i = k; i < n; i++) {
            const leftChar = s[i - k];
            const rightChar = s[i];

            // Remove old char
            charCount.set(leftChar, charCount.get(leftChar) - 1);
            if (charCount.get(leftChar) === 0) {
                charCount.delete(leftChar);
                distinct--;
            }

            // Add new char
            if (!charCount.has(rightChar)) distinct++;
            charCount.set(rightChar, (charCount.get(rightChar) || 0) + 1);

            if (distinct === k - 1) result++;
        }

        return result;
    }
}
```

---

## 📋 Interview Questions & Answers

### ❓Q1. Why do we use a sliding window approach here?

**A:** Because we are dealing with contiguous substrings of fixed length `k`, and sliding window gives us a way to reuse previous computations, reducing time complexity from O(n\*k) to O(n).

---

### ❓Q2. What is the time complexity of your solution?

**A:** O(n), where `n` is the length of the string. Each character is processed at most twice — once when entering and once when leaving the window.

---

### ❓Q3. How do you track the number of distinct characters in a window?

**A:** We maintain a frequency map of characters and increment/decrement a `distinct` counter when a character is added/removed to/from the map.

---

### ❓Q4. What edge cases should be considered?

* `k > s.length` → return 0
* String with all same characters
* String with all unique characters

---

### ❓Q5. Can this be done in constant space?

**A:** No. We need a frequency map which in worst case (26 lowercase letters) takes O(1) space but still uses extra memory.

---
