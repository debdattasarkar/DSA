
---

# 📘 219. Contains Duplicate II

## 🧩 Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if there are **two distinct indices** `i` and `j` in the array such that:

* `nums[i] == nums[j]`, and
* `abs(i - j) <= k`.

Otherwise, return `false`.

---

## 🧪 Examples

### Example 1:

```
Input:  nums = [1,2,3,1], k = 3  
Output: true
```

### Example 2:

```
Input:  nums = [1,0,1,1], k = 1  
Output: true
```

### Example 3:

```
Input:  nums = [1,2,3,1,2,3], k = 2  
Output: false
```

---

## 🔒 Constraints

```
1 <= nums.length <= 10⁵  
-10⁹ <= nums[i] <= 10⁹  
0 <= k <= 10⁵
```

---

## 🧠 Dry Run (Sliding Window with Hash Set)

### Example:

Input: `nums = [1,2,3,1], k = 3`

We maintain a **sliding window** of size `k` using a hash set.

* i = 0 → Add 1 to set → `{1}`
* i = 1 → Add 2 to set → `{1, 2}`
* i = 2 → Add 3 to set → `{1, 2, 3}`
* i = 3 → 1 is in set → ✅ duplicate found within range k=3 → return `True`

---

## 🛠 Optimized Code Implementations

### ✅ Python (Hash Set Sliding Window)

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()  # Hash set to maintain sliding window

        for i, num in enumerate(nums):
            if num in seen:
                return True  # Found duplicate within window
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])  # Maintain window of size k

        return False
```

### ✅ C++

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> seen;

        for (int i = 0; i < nums.size(); ++i) {
            if (seen.count(nums[i])) return true;
            seen.insert(nums[i]);
            if (seen.size() > k)
                seen.erase(nums[i - k]);  // Slide window
        }
        return false;
    }
};
```

### ✅ JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const seen = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (seen.has(nums[i])) return true;
        seen.add(nums[i]);
        if (seen.size > k) seen.delete(nums[i - k]);
    }

    return false;
};
```

---

## ⏱ Complexity Analysis

| Component      | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| Sliding window | O(n)            | O(k)             |

* `n` = length of input
* Only the last `k` elements are stored in the set

---

## 📚 Interviewer FAQs & Clarifications

### 1. ❓What if `k = 0`?

> No window allowed → return `False` unless duplicate is at same index, which is not allowed.

### 2. ❓Why use a HashSet?

> Because lookup, insertion, and deletion are O(1) average-case.

### 3. ❓What if the array is huge?

> The algorithm handles arrays up to 10⁵ efficiently due to linear complexity and space limited to k.

### 4. ❓What if k is larger than array size?

> The sliding window adapts and holds up to `min(k, n)` elements.

---


Here's a detailed comparison of the **Brute Force** and **HashMap Index-based** alternatives, including implementations, dry runs, and time/space tradeoffs:

---

## 🔁 1. Brute Force Approach

### 💡 Idea:

For each element, check every next `k` elements to see if a duplicate exists within that range.

---

### ✅ Code (Python):

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, min(i+k+1, n)):
                if nums[i] == nums[j]:
                    return True  # Duplicate found within k distance
        return False
```

---

### 🧠 Dry Run:

`nums = [1, 2, 3, 1], k = 3`

* i = 0, j = 1 → 1≠2
* i = 0, j = 2 → 1≠3
* i = 0, j = 3 → ✅ 1 == 1 → return True

---

### ⏱ Complexity:

| Metric | Value  |
| ------ | ------ |
| Time   | O(n·k) |
| Space  | O(1)   |

✅ Very simple but **inefficient** for large `n` or `k`.

---

## 🧠 2. HashMap (Index Tracking) Approach

### 💡 Idea:

Use a hashmap to store the **last seen index** of each number. If a number appears again, check if the current index minus the last index ≤ `k`.

---

### ✅ Code (Python):

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True  # Found previous occurrence within distance k
            index_map[num] = i  # Update last index

        return False
```

---

### 🧠 Dry Run:

`nums = [1, 2, 3, 1], k = 3`

* i = 0 → store 1 → {1:0}
* i = 1 → store 2 → {1:0, 2:1}
* i = 2 → store 3 → {1:0, 2:1, 3:2}
* i = 3 → 1 in map, 3 - 0 = 3 ≤ 3 → ✅ return True

---

### ⏱ Complexity:

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

✅ Fast and reliable for large inputs.
❗ Might use more space than the sliding set method if `k` is large.

---

## ✅ Summary Comparison

| Feature               | Brute Force   | HashMap Index Tracking |
| --------------------- | ------------- | ---------------------- |
| Time Complexity       | O(n·k)        | O(n)                   |
| Space Complexity      | O(1)          | O(n)                   |
| Handles large inputs? | ❌ No          | ✅ Yes                  |
| Implementation        | Easy to write | Slightly more involved |
| Real-world use        | Inefficient   | Common in interviews   |

---

Here’s a complete breakdown of the **HashSet Sliding Window** approach, including a comparison with the previous methods:

---

## 🚀 3. HashSet Sliding Window Approach

### 💡 Idea:

Use a sliding window of size `k` implemented using a `HashSet`.
As we iterate through `nums`, we:

1. Check if `nums[i]` is already in the set → duplicate within window → ✅ return `True`
2. Add `nums[i]` to the set
3. If window size exceeds `k`, remove `nums[i - k]`

---

### ✅ Python Code:

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True  # Duplicate found within k window
            window.add(nums[i])

            # Maintain window size <= k
            if len(window) > k:
                window.remove(nums[i - k])

        return False
```

---

### 🧠 Dry Run:

Input: `nums = [1, 2, 3, 1], k = 3`

| i | nums\[i] | window (before) | Found? | window (after) |
| - | -------- | --------------- | ------ | -------------- |
| 0 | 1        | {}              | ❌      | {1}            |
| 1 | 2        | {1}             | ❌      | {1, 2}         |
| 2 | 3        | {1, 2}          | ❌      | {1, 2, 3}      |
| 3 | 1        | {1, 2, 3}       | ✅      | return `True`  |

---

### ⏱ Complexity:

| Metric | Value        |
| ------ | ------------ |
| Time   | O(n)         |
| Space  | O(min(n, k)) |

---

### ✅ Summary Comparison Table

| Approach                  | Time   | Space | Handles Large k | Interview Suitability           |
| ------------------------- | ------ | ----- | --------------- | ------------------------------- |
| **Brute Force**           | O(n·k) | O(1)  | ❌ Inefficient   | ❌ Only for brute logic          |
| **HashMap (Index Track)** | O(n)   | O(n)  | ✅               | ✅ Preferred                     |
| **HashSet (Sliding)**     | O(n)   | O(k)  | ✅               | ✅ More optimal for tight bounds |

---

### 🔄 When to Use Which?

* Use **Brute Force** only when `n` and `k` are small (e.g. constraints < 100).
* Use **HashMap** when you need explicit index tracking.
* Use **Sliding Window HashSet** when only values matter, not positions — typically the most memory-efficient.

---
