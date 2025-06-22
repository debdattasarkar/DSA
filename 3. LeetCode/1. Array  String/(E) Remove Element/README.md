
---

# 🧹 Remove Element – Leetcode #27

### 🟢 Difficulty: Easy

**Tags**: `Array`, `Two Pointers`

---

## 🧾 Problem Statement

Given an integer array `nums` and an integer `val`, remove **all occurrences** of `val` in `nums`, **in-place**. The order of the elements can be changed. After removal, return the number of elements in `nums` **which are not equal to** `val`.

Your implementation should:

* Modify the input array such that the first `k` elements do **not** contain `val`.
* The value of `k` should be the count of elements not equal to `val`.
* Elements beyond the first `k` can be anything.
* Do **not** use extra space (O(1) space complexity).

---

## ✅ Constraints

* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`
* `0 <= val <= 100`

---

## 🧪 Examples

### Example 1:

```text
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

### Example 2:

```text
Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
```

---

## 💡 Hints & Insights

### Hint 1:

We don’t need to *remove* an element per se; just overwrite the array **in-place** while skipping the `val`.

### Hint 2:

Use **two pointers**: one for scanning and one for placing non-`val` values.

### Hint 3:

Swap `val` elements to the end and reduce array size logically.

---

## 🧠 Approach

### Method: Two Pointer Overwrite (Single Pass)

1. Initialize a pointer `k = 0` for the position of non-`val` elements.
2. Traverse the array:

   * If current element is not `val`, place it at `nums[k]` and increment `k`.

This ensures the first `k` elements are valid.

---

## 🧑‍💻 Solutions

### ✅ Python

```python
class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer for the next position to place a non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

### ✅ C++

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
```

### ✅ JavaScript

```javascript
class Solution {
    removeElement(nums, val) {
        let k = 0;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] !== val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
}
```

---

## 📊 Dry Run Example

### Input:

```
nums = [0,1,2,2,3], val = 2
```

### Steps:

```
i=0: nums[0]=0 != 2 → nums[0]=0, k=1
i=1: nums[1]=1 != 2 → nums[1]=1, k=2
i=2: nums[2]=2 == 2 → skip
i=3: nums[3]=2 == 2 → skip
i=4: nums[4]=3 != 2 → nums[2]=3, k=3
```

### Output:

```
nums = [0,1,3,_,_], return k = 3
```

---

## 🧪 Custom Judge

The test judge:

* Confirms `k` is correct.
* Checks that the first `k` elements are valid (sorted and compared).
* Ignores elements beyond `k`.

---

Sure! Here's a clear step-by-step dry run explanation, followed by complete solutions in Python, C++, and JavaScript with inline comments.

---

## ✅ Problem: Remove Element (GeeksforGeeks / Leetcode-27)

---

### 📘 Step-by-Step Explanation:

**Goal:** Remove all occurrences of `val` in the array `nums`, in-place, and return the new length `k`.

---

### 📊 Dry Run Example

**Input:**

```
nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
```

We’ll use two pointers:

* `i` → iterates through the array
* `k` → points to the index to place the next non-`val` element

**Steps:**

| i | nums\[i] | val | Action                 | nums (after action)              | k |
| - | -------- | --- | ---------------------- | -------------------------------- | - |
| 0 | 0        | 2   | nums\[0] != val → copy | \[0, \_, \_, \_, \_, \_, \_, \_] | 1 |
| 1 | 1        | 2   | nums\[1] != val → copy | \[0, 1, \_, \_, \_, \_, \_, \_]  | 2 |
| 2 | 2        | 2   | skip                   | \[0, 1, \_, \_, \_, \_, \_, \_]  | 2 |
| 3 | 2        | 2   | skip                   | \[0, 1, \_, \_, \_, \_, \_, \_]  | 2 |
| 4 | 3        | 2   | nums\[4] != val → copy | \[0, 1, 3, \_, \_, \_, \_, \_]   | 3 |
| 5 | 0        | 2   | nums\[5] != val → copy | \[0, 1, 3, 0, \_, \_, \_, \_]    | 4 |
| 6 | 4        | 2   | nums\[6] != val → copy | \[0, 1, 3, 0, 4, \_, \_, \_]     | 5 |
| 7 | 2        | 2   | skip                   | \[0, 1, 3, 0, 4, \_, \_, \_]     | 5 |

**Result:** `k = 5`, first 5 elements of `nums` = `[0, 1, 3, 0, 4]`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for placing the next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Copy valid element forward
                k += 1  # Move to next placement index
        return k  # New length of valid elements
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0; // Tracks new length and insertion point
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k] = nums[i]; // Move valid elements to front
                k++; // Increment length
            }
        }
        return k; // Length of updated array
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0; // Index to place non-val elements
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i]; // Overwrite with valid element
            k++; // Increase count of valid elements
        }
    }
    return k; // New length without val
};
```

---
