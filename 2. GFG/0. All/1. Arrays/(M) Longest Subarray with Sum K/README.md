
---

# 📘 Longest Subarray with Sum K

### 🟡 Difficulty: Medium

**Accuracy:** 24.64%
**Submissions:** 676K+
**Points:** 4

---

## 🔍 Problem Statement

Given an array `arr[]` containing integers and an integer `k`, your task is to find the **length of the longest subarray** where the **sum of its elements is equal to `k`**.

If there is no subarray with sum equal to `k`, return `0`.

---

## 🧪 Examples

### Example 1:

**Input:**
`arr[] = [10, 5, 2, 7, 1, -10]`, `k = 15`
**Output:** `6`
**Explanation:**
Subarrays with sum = 15:

* `[5, 2, 7, 1]`
* `[10, 5]`
* `[10, 5, 2, 7, 1, -10]`

The longest has length `6`.

---

### Example 2:

**Input:**
`arr[] = [-5, 8, -14, 2, 4, 12]`, `k = -5`
**Output:** `5`
**Explanation:**
Only subarray with sum = -5 is `[-5, 8, -14, 2, 4]` → length = 5

---

### Example 3:

**Input:**
`arr[] = [10, -10, 20, 30]`, `k = 5`
**Output:** `0`
**Explanation:**
No subarray with sum = 5 is present.

---

## 📌 Constraints

* `1 ≤ arr.size() ≤ 10⁵`
* `-10⁴ ≤ arr[i] ≤ 10⁴`
* `-10⁹ ≤ k ≤ 10⁹`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## 🧠 Topic Tags

* Arrays
* Hash
* Map
* Data Structures
* Algorithms
* Prefix Sum

---

## 📚 Related Articles

* [Longest Sub Array Sum K](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)

---

## 📘 Step-by-Step Explanation

### ✅ Key Idea: Prefix Sum + Hash Map

* Keep track of cumulative prefix sum at each index.
* Use a hash map to store **first occurrence** of each prefix sum.
* If `prefix_sum - k` is seen before, then a subarray with sum `k` exists between that index and the current index.

---

## 🔍 Dry Run

### Input:

`arr = [10, 5, 2, 7, 1, -10], k = 15`

| Index                                                           | Element | Prefix Sum | First Occurrence Map      | Max Length      |
| --------------------------------------------------------------- | ------- | ---------- | ------------------------- | --------------- |
| 0                                                               | 10      | 10         | {10: 0}                   | 0               |
| 1                                                               | 5       | 15         | {10: 0, 15: 1}            | 2 (15-0)        |
| 2                                                               | 2       | 17         | {10: 0, 15: 1, 17: 2}     | 2               |
| 3                                                               | 7       | 24         | {10: 0, ..., 24: 3}       | 2               |
| 4                                                               | 1       | 25         | {10: 0, ..., 25: 4}       | 2               |
| 5                                                               | -10     | 15         | Already exists at index 1 | max(2, 5-1) = 4 |
| → But we must keep earliest index only                          |         |            |                           |                 |
| ✅ Final max = **6** when the whole array from 0–5 is considered |         |            |                           |                 |

---

## ✅ Optimized Code Solutions

---

### 🐍 Python

```python
# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum = 0
        sum_map = {}
        max_len = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            if prefix_sum - k in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum - k])

            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i  # Store first occurrence only

        return max_len
```

---

### 💠 C++

```cpp
class Solution {
  public:
    int longestSubarray(vector<int>& arr, int k) {
        unordered_map<int, int> sum_map;
        int prefix_sum = 0, max_len = 0;

        for (int i = 0; i < arr.size(); ++i) {
            prefix_sum += arr[i];

            if (prefix_sum == k)
                max_len = i + 1;

            if (sum_map.find(prefix_sum - k) != sum_map.end())
                max_len = max(max_len, i - sum_map[prefix_sum - k]);

            if (sum_map.find(prefix_sum) == sum_map.end())
                sum_map[prefix_sum] = i;
        }

        return max_len;
    }
};
```

---

### 🌐 JavaScript

```javascript
// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Solution {
    longestSubarray(arr, k) {
        let prefixSum = 0;
        let maxLen = 0;
        const sumMap = new Map();

        for (let i = 0; i < arr.length; i++) {
            prefixSum += arr[i];

            if (prefixSum === k) {
                maxLen = i + 1;
            }

            if (sumMap.has(prefixSum - k)) {
                maxLen = Math.max(maxLen, i - sumMap.get(prefixSum - k));
            }

            if (!sumMap.has(prefixSum)) {
                sumMap.set(prefixSum, i);
            }
        }

        return maxLen;
    }
}
```

---

## 💬 Interview Q\&A

---

### ❓Q1. Why use prefix sum and a hash map?

**A:** Prefix sum allows us to track cumulative totals. By checking if `prefix_sum - k` was seen earlier, we can determine whether a subarray summing to `k` exists between those indices in O(1) time using the hash map.

---

### ❓Q2. Why store the first occurrence of a prefix sum?

**A:** To ensure we get the **longest subarray**, we want the **earliest** index where the prefix sum occurred.

---

### ❓Q3. What if all elements are negative?

**A:** The algorithm still works correctly — it will still find valid subarrays summing to `k`.

---

### ❓Q4. Can this be done without a map?

**A:** Only if all elements are positive. In that case, a sliding window can be used. But since this question includes negative numbers, prefix sum + map is the optimal strategy.

---

### ❓Q5. What's the time and space complexity?

* **Time:** `O(n)`
* **Space:** `O(n)` (for the prefix sum hash map)

---
