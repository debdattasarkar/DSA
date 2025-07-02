Here’s the full README-style writeup based on the provided image and your requirements:

---

# 📘 Problem: Longest Subarray with At Most Two Distinct Integers

---

### 🟡 Difficulty: Medium

**Accuracy:** 47.98%
**Submissions:** 112K+
**Points:** 4
**Average Time:** 30 minutes

---

## 🔍 Problem Statement

Given an array `arr[]` consisting of **positive integers**, your task is to **find the length of the longest subarray** that contains **at most two distinct integers**.

---

## 🧪 Examples

### Example 1:

**Input:**
`arr[] = [2, 1, 2]`
**Output:**
`3`

**Explanation:**
The entire array `[2, 1, 2]` contains at most two distinct integers (2 and 1).
Hence, the length of the longest subarray is `3`.

---

### Example 2:

**Input:**
`arr[] = [3, 1, 2, 2, 2, 2]`
**Output:**
`5`

**Explanation:**
The longest subarray with at most two distinct integers is `[1, 2, 2, 2, 2]`.
So the length is `5`.

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10⁵`
* `1 ≤ arr[i] ≤ 10⁵`

---

## ⏱ Expected Time and Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🧠 Topic Tags

* Two Pointer Algorithm
* Arrays
* Data Structures
* Algorithms
* Sliding Window

---

## 📚 Related Articles

* [Find Length Of The Longest Subarray Containing At Most Two Distinct Integers](https://www.geeksforgeeks.org/find-length-of-the-longest-subarray-containing-atmost-two-distinct-integers)

---

## 🧩 Step-by-Step Explanation

We are to find the **maximum length** of a subarray where the number of **distinct elements is ≤ 2**.

---

### ⚙️ Strategy: Sliding Window + Hash Map

* Use a **two-pointer approach** (`left` and `right`) to represent the sliding window.
* Maintain a **frequency map** (or hashmap) of the elements in the current window.
* If the number of distinct elements exceeds 2, **shrink the window** from the left.
* At each step, update the max window length.

---

### 🔍 Dry Run:

**Input:** `arr = [3, 1, 2, 2, 2, 2]`

| Left | Right | Subarray     | Distinct Count | Valid? | Max Length |
| ---- | ----- | ------------ | -------------- | ------ | ---------- |
| 0    | 0     | \[3]         | 1              | ✅      | 1          |
| 0    | 1     | \[3,1]       | 2              | ✅      | 2          |
| 0    | 2     | \[3,1,2]     | 3              | ❌      | -          |
| 1    | 2     | \[1,2]       | 2              | ✅      | 2          |
| 1    | 3     | \[1,2,2]     | 2              | ✅      | 3          |
| 1    | 4     | \[1,2,2,2]   | 2              | ✅      | 4          |
| 1    | 5     | \[1,2,2,2,2] | 2              | ✅      | **5**      |

✅ Final answer: `5`

---

## ✅ Optimized Code Implementations

---

### 🐍 Python

```python
class Solution:
    def totalElements(self, arr):
        from collections import defaultdict

        left = 0
        max_len = 0
        freq = defaultdict(int)

        for right in range(len(arr)):
            freq[arr[right]] += 1

            # Shrink window if more than 2 distinct
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

### 💠 C++

```cpp
class Solution {
  public:
    int totalElements(vector<int> &arr) {
        unordered_map<int, int> freq;
        int left = 0, max_len = 0;

        for (int right = 0; right < arr.size(); ++right) {
            freq[arr[right]]++;

            while (freq.size() > 2) {
                freq[arr[left]]--;
                if (freq[arr[left]] == 0)
                    freq.erase(arr[left]);
                left++;
            }

            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution {
    totalElements(arr) {
        let left = 0, maxLen = 0;
        const freq = new Map();

        for (let right = 0; right < arr.length; right++) {
            freq.set(arr[right], (freq.get(arr[right]) || 0) + 1);

            while (freq.size > 2) {
                freq.set(arr[left], freq.get(arr[left]) - 1);
                if (freq.get(arr[left]) === 0) {
                    freq.delete(arr[left]);
                }
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
```

---

## 💬 Interview Questions & Answers

---

### ❓Q1. Why is the sliding window technique used here?

**A:** We're looking for the longest contiguous subarray with at most 2 distinct values. A sliding window allows us to track valid ranges efficiently in linear time.

---

### ❓Q2. What is the time and space complexity?

**A:**

* **Time:** O(n)
* **Space:** O(1), since the frequency map holds at most 2 elements at any point.

---

### ❓Q3. What edge cases should be handled?

* Array with all same elements.
* Array with all unique elements (only 2-length windows allowed).
* Array of size 1 or 2.

---

### ❓Q4. Can this be extended to “at most K distinct integers”?

**A:** Yes, just replace the hardcoded `2` with a variable `k` and it becomes a general-purpose sliding window problem for any k.

---

Let me know if you'd like this converted to a Markdown or PDF format, or need a Leetcode-style driver for testing.
