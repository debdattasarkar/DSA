
---

## 📘 README Format – 128. Longest Consecutive Sequence

### Difficulty: Medium

**Topics:** Array, Hash Table, Union Find
**Asked by:** Google, Amazon, Facebook

---

### 🔔 Problem Statement

Given an unsorted array of integers `nums`, return the **length** of the **longest consecutive elements sequence**.

⏱️ You must write an algorithm that runs in **O(n)** time.

---

### 🔍 Examples

#### Example 1:

```
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore, its length is 4.
```

#### Example 2:

```
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
```

#### Example 3:

```
Input: nums = [1, 0, 1, 2]
Output: 3
```

---

### ✅ Constraints:

* `0 <= nums.length <= 10⁵`
* `-10⁹ <= nums[i] <= 10⁹`

---

## 🧠 Step-by-Step Explanation

### 🔧 Intuition:

* Use a **set** to store all unique numbers for O(1) lookup.
* For each number, **start a sequence only if it's the beginning** (i.e. `num - 1` is not in the set).
* Then expand the sequence using a loop: `num + 1, num + 2, ...`.

### 🔂 Dry Run:

```
Input: nums = [100, 4, 200, 1, 3, 2]
Set = {100, 4, 200, 1, 3, 2}
Start at 1 (since 0 not in set):
    → 2 → 3 → 4 → length = 4
Skip 2, 3, 4 (because 1 already handled them)
100 → start → length = 1
200 → start → length = 1
Max = 4
```

---

## 🧑‍💻 Optimized Code (All 3 Languages)

---

### ✅ Python

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(n) time & space

        max_len = 0

        for num in num_set:
            # Start only if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                # Expand the streak
                while current + 1 in num_set:
                    current += 1
                    streak += 1

                max_len = max(max_len, streak)

        return max_len
```

---

### ✅ C++

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());  // O(n)
        int max_len = 0;

        for (int num : num_set) {
            if (!num_set.count(num - 1)) { // Start of sequence
                int current = num;
                int streak = 1;

                while (num_set.count(current + 1)) {
                    current++;
                    streak++;
                }

                max_len = max(max_len, streak);
            }
        }

        return max_len;
    }
};
```

---

### ✅ JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const set = new Set(nums); // O(n)
    let maxLen = 0;

    for (let num of set) {
        if (!set.has(num - 1)) {
            let current = num;
            let streak = 1;

            while (set.has(current + 1)) {
                current++;
                streak++;
            }

            maxLen = Math.max(maxLen, streak);
        }
    }

    return maxLen;
};
```

---

## 📊 Time and Space Complexity

| Step                     | Time       | Space       |
| ------------------------ | ---------- | ----------- |
| Convert array to set     | O(n)       | O(n)        |
| Iterate & find sequences | O(n)       | O(1) inside |
| Total                    | ✅ **O(n)** | ✅ **O(n)**  |

---

## ❓ Interview FAQs

### Q1: Why do we only start the sequence when `num - 1` is not in the set?

**A:** To avoid recomputing sequences from the middle. For example, `[1, 2, 3]` — only start at 1.

---

### Q2: Can we sort the array instead?

**A:** Yes, but that gives O(n log n) time. This problem specifically asks for O(n) time, so sorting is not optimal.

---

### Q3: What if the array is empty?

**A:** Return `0` as there are no sequences.

---

### Q4: What if negative numbers are present?

**A:** The logic works fine since it handles all integers in the set.

---

Here's a detailed comparison of the **Brute Force** and **HashMap Index-based** alternatives for solving Leetcode **219. Contains Duplicate II**, including implementations, dry runs, and time/space tradeoffs:

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
