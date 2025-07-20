
---

## 🧩 Leetcode 4: Median of Two Sorted Arrays

🔗 [Leetcode Link](https://leetcode.com/problems/median-of-two-sorted-arrays/)

### 🔸 Problem Statement:

Given two sorted arrays `nums1` and `nums2`, return the **median** of the two sorted arrays.
You must solve the problem in **O(log(min(n, m)))** time complexity.

---

### 🔸 Example:

```python
Input: nums1 = [1, 3], nums2 = [2]  
Output: 2.0

Input: nums1 = [1, 2], nums2 = [3, 4]  
Output: 2.5
```

---

## 🚀 Optimized Strategy: Binary Search on Partition Index

We want to **partition the two arrays** into left and right halves such that:

* All elements on the left ≤ all elements on the right
* And the left and right halves have the **same number of elements (or off by 1)**

We **binary search** on the smaller array to find such a partition.

---

### ✅ Python Code

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
```

---

## 🧠 Time and Space Complexity

| Metric | Value               |
| ------ | ------------------- |
| Time   | `O(log(min(m, n)))` |
| Space  | `O(1)`              |

---

## 🔁 Intuition:

We're finding a "cut" between two sorted arrays such that:

* Left side contains half the total elements
* The largest left element ≤ smallest right element

---

## ✅ Real-World Use Cases

1. **Median in Streaming or Merged Sorted Data**
2. **Balanced Data Sampling**
3. **Quantile Estimation in Databases or Analytics Engines**

---

---

# Why binary search works?

Absolutely! Here's a clear explanation of **why binary search works** in **Leetcode 4: Median of Two Sorted Arrays**.

---

## 🧠 Why Binary Search Works in This Problem

We're given two **sorted arrays**, and we want to find the **median of the combined sorted array**, **without actually merging them**, and in **O(log(min(m, n)))** time.

---

### 🔑 Core Insight

We can think of this problem as:

> "Find a partition point between the two arrays such that all elements on the **left side** are ≤ all elements on the **right side**."

---

### 🧩 Partition Logic

Let’s say:

* `nums1 = [1, 3, 8, 9, 15]`
* `nums2 = [7, 11, 18, 19, 21, 25]`

We want to find some `i` in `nums1` and `j` in `nums2` such that:

```
max(nums1[0..i-1], nums2[0..j-1]) <= min(nums1[i..], nums2[j..])
```

And such that:

```
i + j = (n + m) // 2 → so that left and right halves are balanced
```

---

### 🔍 Why Binary Search?

We know `nums1` is sorted, so we **binary search on its partition index `i`**.

At each step:

* We compute `j = (n + m + 1)//2 - i`
* We compare:

  * `nums1[i-1]` and `nums2[j]`
  * `nums2[j-1]` and `nums1[i]`

If:

```
nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]
```

✅ We've found the correct partition.

If:

```
nums1[i-1] > nums2[j]
```

→ We need to move `i` left (reduce `i`)

If:

```
nums2[j-1] > nums1[i]
```

→ We need to move `i` right (increase `i`)

This binary search is guaranteed to converge in `O(log(min(m, n)))` time.

---

## ⚖️ Balanced Partition Is the Key

We're not doing binary search on values, we're doing binary search on **positions (indices)** of one array to balance the combined left and right halves.

---

## ✅ Why We Always Binary Search the Smaller Array

To keep the time complexity to `O(log(min(n, m))`, we always binary search on the **smaller array**, so that we don't exceed index bounds while computing `j`.

---

## Summary Diagram

```
nums1: [1, 3, 8] | [9, 15]
nums2: [7, 11, 18] | [19, 21, 25]
           ↑             ↑
         left           right
```

* Left half max = `max(8, 18) = 18`
* Right half min = `min(9, 19) = 9`

❌ Not valid → need to adjust partition

Eventually, we find a partition where this condition holds, and then compute the median.

---

---

Yes ✅ — the **binary search on partition approach** used in **LeetCode 4** is the **optimized and most efficient** way to solve this problem under the given constraints.

---

## 🔥 Why This Is the Optimized Solution

| Criterion                    | Explanation                                                 |
| ---------------------------- | ----------------------------------------------------------- |
| **Time Complexity**          | `O(log(min(m, n)))` — fastest possible without merging      |
| **Space Complexity**         | `O(1)` — constant space, no extra array used                |
| **Avoids Full Merge**        | Doesn't require merging arrays or full traversal            |
| **Guaranteed Convergence**   | Binary search guarantees a valid partition within log steps |
| **Handles Odd/Even Lengths** | Works for both total even and odd number of elements        |

---

## 🆚 Slower Alternatives

### ❌ Brute Force:

* Merge the arrays and find the median
* **Time:** `O(m + n)`
* **Space:** `O(m + n)` — inefficient for large inputs

### ❌ Two-pointer approach:

* Same as merge but without creating a merged array
* Still **O(m + n)** time

---

### ✅ Final Verdict:

The **partition-based binary search** is the most optimal solution that meets the requirement of:

> **"Time complexity must be O(log(min(m, n)))"**

---
