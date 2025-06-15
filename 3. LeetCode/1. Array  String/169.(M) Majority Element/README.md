Here is the full **README-style explanation** for **Leetcode 169 – Majority Element**, including a dry run and optimal solutions in **Python, C++, and JavaScript**, all using **Boyer-Moore Voting Algorithm** for `O(n)` time and `O(1)` space.

---

# 🗳️ Majority Element (Leetcode #169)

### 🟢 Difficulty: Easy

**Tags**: `Array`, `Hash Table`, `Divide and Conquer`, `Sorting`, `Counting`

---

## 📘 Problem Statement

Given an array `nums` of size `n`, return the **majority element** — the element that appears **more than ⌊n / 2⌋ times**.

You may **assume that a majority element always exists**.

---

## 🧪 Examples

### Example 1:

```
Input: nums = [3,2,3]
Output: 3
```

### Example 2:

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

---

## ⚙️ Constraints

* `1 <= n <= 5 × 10⁴`
* `-10⁹ <= nums[i] <= 10⁹`
* Majority element **always exists**

---

## 🧠 Optimal Approach: Boyer-Moore Voting Algorithm

We track a `candidate` and a `count`.

### Logic:

* If `count == 0`, we pick the current element as a new candidate.
* If `num == candidate`, we increment `count`.
* Else, decrement `count`.

The majority element survives because its count exceeds all others **combined**.

---

## 📊 Dry Run

**Input:**
`nums = [2, 2, 1, 1, 1, 2, 2]`

| Index | num | candidate | count | Explanation                        |
| ----- | --- | --------- | ----- | ---------------------------------- |
| 0     | 2   | 2         | 1     | Set candidate                      |
| 1     | 2   | 2         | 2     | Same as candidate, increment count |
| 2     | 1   | 2         | 1     | Not same, decrement count          |
| 3     | 1   | 2         | 0     | Not same, decrement count          |
| 4     | 1   | 1         | 1     | Reset candidate                    |
| 5     | 2   | 1         | 0     | Not same, decrement count          |
| 6     | 2   | 2         | 1     | Reset candidate                    |

✅ Output: `2`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num  # Choose new candidate
            count += (1 if num == candidate else -1)

        return candidate
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidate = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;  // Set new candidate
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = 0;
    let candidate = null;

    for (let num of nums) {
        if (count === 0) {
            candidate = num;
        }
        count += (num === candidate) ? 1 : -1;
    }

    return candidate;
};
```

---

## ✅ Summary

| Property         | Value                        |
| ---------------- | ---------------------------- |
| Time Complexity  | `O(n)`                       |
| Space Complexity | `O(1)`                       |
| Approach         | Boyer-Moore Voting Algorithm |

---

Absolutely! Here's the **brute force / hash map version** of the solution for the **Majority Element** problem (Leetcode #169).

---

## 🧠 Brute Force / Hash Map Approach

### 🔍 Idea:

* Count the frequency of each element using a **dictionary** (`hash map`).
* Return the element with frequency > `n // 2`.

---

## ✅ Time and Space

| Metric           | Value                 |
| ---------------- | --------------------- |
| Time Complexity  | `O(n)`                |
| Space Complexity | `O(n)` (for hash map) |

> This is not `O(1)` space like Boyer-Moore, but very intuitive and easy to implement.

---

## 🐍 Python Code (Hash Map)

```python
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        majority = len(nums) // 2

        for num in nums:
            count[num] += 1
            if count[num] > majority:
                return num  # Early return on majority
```

---

## 💠 C++ Code (Unordered Map)

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count;
        int majority = nums.size() / 2;

        for (int num : nums) {
            count[num]++;
            if (count[num] > majority) {
                return num;  // Early exit
            }
        }

        return -1; // Should never reach here if majority always exists
    }
};
```

---

## 🌐 JavaScript Code (Map)

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const count = new Map();
    const majority = Math.floor(nums.length / 2);

    for (let num of nums) {
        count.set(num, (count.get(num) || 0) + 1);
        if (count.get(num) > majority) {
            return num;
        }
    }
};
```

---

## 📌 Summary

* ✅ Very simple and clear logic.
* 🚫 Uses `O(n)` space — so **not optimal** in space but useful for interviews where clarity matters.
