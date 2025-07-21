Great! Let's explore **LeetCode 153: Find Minimum in Rotated Sorted Array** — a **classic binary search variant** and a top favorite in interviews (Google, Amazon, Facebook).

---

## 🧩 Leetcode 153: Find Minimum in Rotated Sorted Array

🔗 [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

> A sorted array is rotated at some pivot. Find the **minimum element** in O(log n) time.
> **Assume all elements are unique.**

---

### 🧠 Example

```python
Input:  [3,4,5,1,2]
Output: 1

Input:  [1,2,3,4,5]
Output: 1
```

---

## ✅ Key Observation:

In a rotated array:

* One part is **sorted**, the other is **unsorted**
* The **minimum** is the **only element smaller than its previous element** (or the pivot point)

---

## 🔍 Binary Search Strategy:

1. If `nums[mid] > nums[right]`, then min is in the **right half**
2. Else, the min is in the **left half (including mid)**

---

## ✅ Python Code (Optimal Binary Search)

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            
            # The current subarray is already sorted, 
            # the minimum is at the left index
            if nums[left] < nums[right]:
                return nums[left]
            
            # We reach here when we have at least
            # two elements and the current subarray
            # is rotated
            mid = (left + right) // 2
            # The right half is not sorted. So 
            # the minimum element must be in the
            # right half.
            if nums[mid] > nums[right]:
                # min must be to the right
                left = mid + 1
            else:
                # The right half is sorted. Note that in 
                # this case, we do not change right to mid - 1
                # but keep it to mid. As the mid element
                # itself can be the smallest
                # min is in the left half including mid
                right = mid

        return nums[left]
```

---

## 🧠 Dry Run for \[3,4,5,1,2]

* left = 0, right = 4 → mid = 2 → nums\[mid]=5 > nums\[right]=2 → left = mid + 1 = 3
* left = 3, right = 4 → mid = 3 → nums\[mid]=1 < nums\[right]=2 → right = mid = 3
* Now left == right → return `nums[3] = 1`

---

## 🕐 Time and Space Complexity

* **Time:** O(log n)
* **Space:** O(1)

---

## 🧪 Example Tests

```python
assert Solution().findMin([3,4,5,1,2]) == 1
assert Solution().findMin([4,5,6,7,0,1,2]) == 0
assert Solution().findMin([1]) == 1
assert Solution().findMin([2,1]) == 1
```

---

---

Here is the full **step-by-step dry run** for:

---

## ✅ Leetcode 153: Find Minimum in Rotated Sorted Array

**Input:** `nums = [4, 5, 6, 7, 0, 1, 2]`

---

### 🔍 Dry Run Breakdown

| Step | left | right | mid | nums\[mid] | Action                                       |
| ---- | ---- | ----- | --- | ---------- | -------------------------------------------- |
| 1    | 0    | 6     | 3   | 7          | mid > right → min in right half → `left = 4` |
| 2    | 4    | 6     | 5   | 1          | mid < right → min in left half → `right = 5` |
| 3    | 4    | 5     | 4   | 0          | mid < right → min in left half → `right = 4` |

Loop ends when `left == right == 4` → ✅ Minimum = `nums[4] = 0`

---

---
