
---

# 📘 Subarrays With At Most K Distinct Integers

**Difficulty:** Medium
**Accuracy:** 77.82%
**Submissions:** 5K+
**Points:** 4

---

## 🧾 Problem Statement

You are given an array `arr[]` of positive integers and an integer `k`. Your task is to **find the number of subarrays** in `arr[]` where the **count of distinct integers is at most `k`**.

> **Note:** A **subarray** is a **contiguous** part of an array.

---

## 🧪 Examples

### ➤ Example 1:

**Input:**
`arr[] = [1, 2, 2, 3], k = 2`
**Output:**
`9`
**Explanation:**
Subarrays with at most 2 distinct elements are:
`[1]`, `[2]`, `[2]`, `[3]`, `[1, 2]`, `[2, 2]`, `[2, 3]`, `[1, 2, 2]`, `[2, 2, 3]`.

---

### ➤ Example 2:

**Input:**
`arr[] = [1, 1, 1], k = 1`
**Output:**
`6`
**Explanation:**
Subarrays with at most 1 distinct element are:
`[1]`, `[1]`, `[1]`, `[1, 1]`, `[1, 1]`, `[1, 1, 1]`.

---

### ➤ Example 3:

**Input:**
`arr[] = [1, 2, 1, 1, 3, 3, 4, 2, 1], k = 2`
**Output:**
`24`
**Explanation:**
There are 24 subarrays with at most 2 distinct elements.

---

## 📊 Constraints:

* $1 \leq \text{arr.size()} \leq 2 \times 10^4$
* $1 \leq k \leq 2 \times 10^4$
* $1 \leq \text{arr[i]} \leq 10^9$

---

## 📈 Expected Complexities:

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(k)

---

## 🏷️ Topic Tags:

* `sliding-window`
* `Arrays`
* `Data Structures`
* `Algorithms`

---

## 📚 Related Articles:

* [Count Subarrays With At Most K Distinct Elements](https://www.geeksforgeeks.org/count-subarrays-with-at-most-k-distinct-elements/)


---

## ✅ 2. Step-by-Step Explanation and Dry Run

### **Problem: Count the number of subarrays with at most K distinct integers.**

We use the **Sliding Window** approach with a hash map (or frequency map) to count the number of distinct elements in a window.

---

### **Logic**

For each valid window where number of distinct integers is ≤ `k`, every extension from left to right is valid.

We maintain:

* `left` pointer: Start of the window
* `right` pointer: Expands the window
* `freq`: Dictionary or map to track element frequency
* `count`: Total number of valid subarrays

---

### **Dry Run:**

#### Input:

```python
arr = [1, 2, 1, 2, 3], k = 2
```

#### Expected Output:

```text
10
```

#### Process:

| Step | Window `[left:right]` | freq map      | Distinct | Subarrays Added | Total Count |
| ---- | --------------------- | ------------- | -------- | --------------- | ----------- |
| 0    | \[0:0] = \[1]         | {1:1}         | 1        | 1               | 1           |
| 1    | \[0:1] = \[1,2]       | {1:1, 2:1}    | 2        | 2               | 3           |
| 2    | \[0:2] = \[1,2,1]     | {1:2, 2:1}    | 2        | 3               | 6           |
| 3    | \[0:3] = \[1,2,1,2]   | {1:2, 2:2}    | 2        | 4               | 10          |
| 4    | \[0:4] = \[1,2,1,2,3] | {1:2,2:2,3:1} | 3 > k!   | shrink left →   |             |
|      | \[1:4] = \[2,1,2,3]   | {1:1,2:2,3:1} | 3        | shrink again    |             |
|      | \[2:4] = \[1,2,3]     | {1:1,2:1,3:1} | 3        | shrink again    |             |
|      | \[3:4] = \[2,3]       | {2:1,3:1}     | 2        | 2               | 12          |

Final count of valid subarrays = **10**

---

## ✅ 3. Optimized Code Implementations

---

### ✅ Python Implementation

```python
class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        left = 0
        count = 0

        for right in range(len(arr)):
            # If it's a new element, reduce k
            if freq[arr[right]] == 0:
                k -= 1
            freq[arr[right]] += 1

            # Shrink window until distinct <= k
            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1
                left += 1

            # Add number of subarrays ending at `right`
            count += (right - left + 1)

        return count
```

---

### ✅ C++ Implementation

```cpp
class Solution {
  public:
    int countAtMostK(vector<int>& arr, int k) {
        unordered_map<int, int> freq;
        int left = 0, count = 0;

        for (int right = 0; right < arr.size(); ++right) {
            if (freq[arr[right]] == 0)
                k--;
            freq[arr[right]]++;

            while (k < 0) {
                freq[arr[left]]--;
                if (freq[arr[left]] == 0)
                    k++;
                left++;
            }

            count += right - left + 1;
        }
        return count;
    }
};
```

---

### ✅ JavaScript Implementation

```javascript
class Solution {
    countAtMostK(arr, k) {
        let freq = new Map();
        let left = 0, count = 0;

        for (let right = 0; right < arr.length; right++) {
            if (!freq.has(arr[right]) || freq.get(arr[right]) === 0) {
                k--;
            }
            freq.set(arr[right], (freq.get(arr[right]) || 0) + 1);

            while (k < 0) {
                freq.set(arr[left], freq.get(arr[left]) - 1);
                if (freq.get(arr[left]) === 0) {
                    k++;
                }
                left++;
            }

            count += right - left + 1;
        }

        return count;
    }
}
```

---

## ✅ 4. Interview FAQs & Expected Questions

| Question                                                         | Answer                                                                                                 |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **What’s the core idea behind this solution?**                   | It’s a sliding window that tracks the number of distinct elements in the window.                       |
| **Why use sliding window instead of brute-force?**               | Brute-force is O(n²). Sliding window reduces it to O(n) by smartly expanding and shrinking the window. |
| **What data structure did you use to track frequency?**          | Python: `defaultdict`, C++: `unordered_map`, JS: `Map`.                                                |
| **Can you find subarrays with *exactly* k distinct elements?**   | Yes, by calculating `countAtMostK(k) - countAtMostK(k-1)`.                                             |
| **What’s the edge case if k = 0?**                               | No valid subarray. Should return 0.                                                                    |
| **What is the max number of subarrays in an array of length n?** | n \* (n + 1) / 2 (if all subarrays are valid).                                                         |

---
