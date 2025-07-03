
---

## 🧾 Problem: 1. Two Sum

**Difficulty:** Easy
**Topics:** Array, Hash Table
**Companies:** Frequently asked (FAANG)

---

### 🧠 Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they **add up to `target`**.

* You **may not** use the same element twice.
* You can return the answer in **any order**.
* **Exactly one solution** is guaranteed to exist.

---

### 🔍 Examples

**Example 1**

```
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]
Explanation: nums[0] + nums[1] == 9 → 2 + 7 = 9
```

**Example 2**

```
Input: nums = [3,2,4], target = 6  
Output: [1,2]
```

**Example 3**

```
Input: nums = [3,3], target = 6  
Output: [0,1]
```

---

### 🔒 Constraints

* 2 ≤ `nums.length` ≤ 10⁴
* -10⁹ ≤ `nums[i]`, `target` ≤ 10⁹
* **Only one valid answer exists**

---

### 💡 Hints from Leetcode

* Try brute force for completeness, then optimize.
* Fix one number `x`, search for `target - x`.
* Use a **hashmap** to track complements for O(1) lookup.

---

## 🪜 Step-by-Step Dry Run

Let’s dry run `nums = [3,2,4]`, `target = 6`

| i | num | target - num | Seen Hashmap   | Result                                |
| - | --- | ------------ | -------------- | ------------------------------------- |
| 0 | 3   | 3            | `{}`           | —                                     |
|   |     |              | `{3: 0}`       | —                                     |
| 1 | 2   | 4            | `{3: 0}`       | —                                     |
|   |     |              | `{3: 0, 2: 1}` | —                                     |
| 2 | 4   | 2            | `{3: 0, 2: 1}` | ✅ Found 2 at index 1 → return \[1, 2] |

---

## ✅ Optimized Code (HashMap) – O(n)

---

### 🐍 Python

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}  # Stores num → index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]  # Return indices
            index_map[num] = i  # Store index of current num
```

---

### 💠 C++

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map; // num → index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.count(complement)) {
                return {map[complement], i}; // Found match
            }
            map[nums[i]] = i;
        }
        return {}; // Should never reach here
    }
};
```

---

### 🌐 JavaScript

```javascript
var twoSum = function(nums, target) {
    let map = {};  // num → index

    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (map.hasOwnProperty(complement)) {
            return [map[complement], i];  // Found the pair
        }
        map[nums[i]] = i;
    }
};
```

---

## 🧮 Time and Space Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(n)** |

* We iterate once, storing at most n keys in hashmap.

---

## 🎤 Interview Q\&A

**Q1: Why is a hashmap better than nested loops?**
A: Nested loops → O(n²). Hashmap lookup is O(1), so total is O(n).

---

**Q2: What if multiple answers exist?**
A: Problem guarantees **exactly one answer**. Otherwise, you'd need to consider all valid pairs.

---

**Q3: Can the input be modified?**
A: No need. Our hashmap approach works without modifying the array.

---

**Q4: What if nums contains duplicates?**
A: It's okay, since we return **indices**, not values, and only one valid pair is guaranteed.

---

**Q5: Can you do it in-place?**
A: Not without sacrificing O(n) time. In-place sort + two-pointer works **only** if the result is values (not indices), but here we need original positions.

---
