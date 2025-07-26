Let’s walk through **Leetcode 88 – Merge Sorted Array**, a frequently asked **Two Pointer** problem involving **in-place merging**.

---

## 🔍 Problem Statement

You are given two sorted integer arrays:

* `nums1` of size `m + n`, where the first `m` elements are valid and the rest are 0 placeholders
* `nums2` of size `n`

> Merge `nums2` into `nums1` as one sorted array, **in-place**.

---

### 🧪 Example

```python
Input: nums1 = [1,2,3,0,0,0], m = 3  
       nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]
```

---

## ✅ Approach: Two Pointers (Start from End)

### 💡 Idea:

To avoid overwriting elements in `nums1`, **merge from the back**:

* Use three pointers:

  * `p1 = m - 1` → end of valid `nums1`
  * `p2 = n - 1` → end of `nums2`
  * `p = m + n - 1` → end of merged array

Compare `nums1[p1]` and `nums2[p2]`, place larger at `nums1[p]`, and move pointers.

---

## 🧑‍💻 Python Code with Inline Comments

```python
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Start from end of both arrays
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge from back to front
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If any elements left in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
```

---

## ⏱ Time and Space Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(m + n) |
| Space  | O(1)     |

---

## 🧠 Dry Run

Input:

```python
nums1 = [1,2,3,0,0,0], m = 3  
nums2 = [2,5,6], n = 3
```

| Step | p1 | p2 | p | nums1          | Action       |
| ---- | -- | -- | - | -------------- | ------------ |
| 1    | 2  | 2  | 5 | \[1,2,3,0,0,6] | 6 → end      |
| 2    | 2  | 1  | 4 | \[1,2,3,0,5,6] | 5 → pos 4    |
| 3    | 2  | 0  | 3 | \[1,2,3,3,5,6] | 3 from nums1 |
| 4    | 1  | 0  | 2 | \[1,2,2,3,5,6] | 2 from nums2 |
| 5    | 1  | -1 | 1 | done           | nums2 empty  |

✅ Final Output: `[1,2,2,3,5,6]`

---

## ❓ Interview Q\&A

| Question                 | Answer                                       |
| ------------------------ | -------------------------------------------- |
| Why merge from the end?  | Avoids overwriting valid elements of `nums1` |
| What if nums2 is empty?  | Nothing changes, nums1 is already valid      |
| Why not use extra space? | Problem requires **in-place merge**          |
| Can we do it from front? | Only with extra space (not allowed here)     |

---

## 🧪 Real-World Applications

* **Merge step** in merge sort
* **Stream merging** in time-series data
* **Merging user logs** from two services

---
