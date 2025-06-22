Here’s a README-style explanation, including a dry run and full code in **Python**, **C++**, and **JavaScript** with inline comments, based on the Leetcode/GeeksforGeeks-style problem **Remove Duplicates from Sorted Array**.

---

# 🚫 Remove Duplicates from Sorted Array (Leetcode #26)

### 🟢 Difficulty: Easy

**Topics**: `Array`, `Two Pointers`

---

## 🧾 Problem Statement

Given a **sorted** array `nums`, remove duplicates **in-place** such that each unique element appears **only once**. The **relative order** must be maintained.

Return the count `k` of unique elements. The first `k` elements of `nums` should contain the result.

### ⚠️ Constraints:

* `1 <= nums.length <= 30,000`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in **non-decreasing order**

---

## 🧠 Approach

We use the **two-pointer technique**:

* `i` tracks the last placed unique element
* `j` scans through the array

If `nums[j] != nums[i]`, we found a new unique element. Increment `i` and copy `nums[j]` to `nums[i]`.

---

## 🔍 Dry Run Example

**Input:**
`nums = [0, 0, 1, 1, 2, 2, 3, 4, 4]`

### Step-by-step:

| j | nums\[j] | nums\[i] | Action             | nums (in-place)              | i |
| - | -------- | -------- | ------------------ | ---------------------------- | - |
| 1 | 0        | 0        | Duplicate → skip   | \[0, 0, 1, 1, 2, 2, 3, 4, 4] | 0 |
| 2 | 1        | 0        | Unique → i++, copy | \[0, 1, 1, 1, 2, 2, 3, 4, 4] | 1 |
| 3 | 1        | 1        | Duplicate → skip   | \[0, 1, 1, 1, 2, 2, 3, 4, 4] | 1 |
| 4 | 2        | 1        | Unique → i++, copy | \[0, 1, 2, 1, 2, 2, 3, 4, 4] | 2 |
| 5 | 2        | 2        | Duplicate → skip   | \[0, 1, 2, 1, 2, 2, 3, 4, 4] | 2 |
| 6 | 3        | 2        | Unique → i++, copy | \[0, 1, 2, 3, 2, 2, 3, 4, 4] | 3 |
| 7 | 4        | 3        | Unique → i++, copy | \[0, 1, 2, 3, 4, 2, 3, 4, 4] | 4 |
| 8 | 4        | 4        | Duplicate → skip   | \[0, 1, 2, 3, 4, 2, 3, 4, 4] | 4 |

✅ Result: `k = i + 1 = 5`
`nums = [0, 1, 2, 3, 4, _, _, _, _]`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # Last unique element position
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Found a new unique element
                i += 1
                nums[i] = nums[j]  # Move it next to last unique
        return i + 1  # Unique element count
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        int i = 0; // Index of last unique element
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) { // Unique element found
                i++;
                nums[i] = nums[j]; // Move it forward
            }
        }
        return i + 1; // New length
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
var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0;

    let i = 0; // Last unique index
    for (let j = 1; j < nums.length; j++) {
        if (nums[j] !== nums[i]) {
            i++;
            nums[i] = nums[j]; // Move unique element forward
        }
    }
    return i + 1; // Unique count
};
```

---

## ✅ Summary

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`
* Modifies the array in-place using the **two-pointer technique**.
* Preserves the **order of unique elements**.
