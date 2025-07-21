Let’s deep dive into **LeetCode 33: Search in Rotated Sorted Array** — a classic and frequently asked binary search problem at companies like Google, Amazon, and Facebook.

---

## 🧩 Problem: LeetCode 33 — Search in Rotated Sorted Array

🔗 [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array)

> You are given a **sorted array** that has been **rotated at an unknown pivot**, and a `target` value.
> Return the index of the target if it exists, or `-1` if it doesn't.

* Must run in **O(log n)** time.

---

### 🧠 Example

```txt
Input:  nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input:  nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

---

## ✅ Key Idea: Modified Binary Search

At any point, **at least one half (left or right) is sorted**.
Check which half is sorted and **narrow the search** accordingly.

---

### 🧠 Step-by-Step Logic:

1. Compute `mid = (left + right) // 2`
2. If `nums[mid] == target`: return `mid`
3. Check which half is sorted:

   * **Left sorted:** `nums[left] <= nums[mid]`

     * If `nums[left] <= target < nums[mid]`: search left
     * Else: search right
   * **Right sorted:** `nums[mid] <= nums[right]`

     * If `nums[mid] < target <= nums[right]`: search right
     * Else: search left

---

## ✅ Python Code with Comments

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in left half
                else:
                    left = mid + 1   # Target is in right half

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in right half
                else:
                    right = mid - 1  # Target is in left half

        return -1  # Target not found
```

---

## 🧪 Example Dry Run

```python
nums = [4,5,6,7,0,1,2], target = 0

left = 0, right = 6
mid = 3 → nums[3] = 7
→ Left half is sorted (4 ≤ 7), but 0 < 4 → search right → left = 4

mid = 5 → nums[5] = 1
→ Right half is sorted (1 ≤ 2), but 0 < 1 → search left → right = 4

mid = 4 → nums[4] = 0 → match → return 4
```

---

## 🕐 Time & Space Complexity

* **Time:** `O(log n)`
* **Space:** `O(1)`

---

Here’s the full **binary search with dry run and timer** for:

### ✅ LeetCode 33: Search in Rotated Sorted Array

---

### 🧪 Input:

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

---

### 🔍 Dry Run Steps:

1. **mid = 3**, nums\[3] = 7
   → Left half \[0:3] is sorted
   → 0 not in \[4,7] → search right → `left = 4`

2. **mid = 5**, nums\[5] = 1
   → Left half \[4:5] is sorted
   → 0 in \[0,1] → search left → `right = 4`

3. **mid = 4**, nums\[4] = 0
   ✅ Target found at index 4

---

### ✅ Output:

```
Output (Index of Target): 4
Execution Time: 0.000144 seconds
```

---

---

Here’s the full **binary search with dry run and timer** for:

### ✅ LeetCode 33: Search in Rotated Sorted Array

---

### 🧪 Input:

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

---

### 🔍 Dry Run Steps:

1. **mid = 3**, nums\[3] = 7
   → Left half \[0:3] is sorted
   → 0 not in \[4,7] → search right → `left = 4`

2. **mid = 5**, nums\[5] = 1
   → Left half \[4:5] is sorted
   → 0 in \[0,1] → search left → `right = 4`

3. **mid = 4**, nums\[4] = 0
   ✅ Target found at index 4

---

### ✅ Output:

```
Output (Index of Target): 4
Execution Time: 0.000144 seconds
```

---


```python
import time
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(f"Checking mid={mid}, nums[mid]={nums[mid]}")

            if nums[mid] == target:
                print("Target found at index", mid)
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                print(f"Left half [{left}:{mid}] is sorted.")
                if nums[left] <= target < nums[mid]:
                    print("Target in left half → moving right to mid - 1")
                    right = mid - 1
                else:
                    print("Target not in left half → moving left to mid + 1")
                    left = mid + 1
            else:
                print(f"Right half [{mid}:{right}] is sorted.")
                if nums[mid] < target <= nums[right]:
                    print("Target in right half → moving left to mid + 1")
                    left = mid + 1
                else:
                    print("Target not in right half → moving right to mid - 1")
                    right = mid - 1

        print("Target not found.")
        return -1

# --- Main driver with input and timing ---
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    print("Input nums:", nums)
    print("Target:", target)

    start_time = time.time()
    result = Solution().search(nums, target)
    end_time = time.time()

    print("\nOutput (Index of Target):", result)
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
```

---

---

Here are the **most common interview questions and follow-ups** for **LeetCode 33: Search in Rotated Sorted Array**, designed to test depth in binary search logic, edge cases, and variant handling.

---

## 🔹 Understanding the Problem

### 1. **Why does binary search still work in a rotated array?**

> Because **at least one half is always sorted**.
> Binary search logic is adjusted to first **identify the sorted half**, and then decide which side the target lies in.

---

### 2. **How do you determine if the left or right half is sorted?**

Check:

```python
if nums[left] <= nums[mid]:
    # Left half is sorted
else:
    # Right half is sorted
```

---

### 3. **What is the time and space complexity of your solution?**

* **Time:** `O(log n)` — standard binary search behavior.
* **Space:** `O(1)` — no recursion or extra structures.

---

## 🔸 Edge Cases

### 4. **What happens if the array is not rotated?**

> The entire array is sorted.
> Binary search still works correctly using the same logic.

---

### 5. **What if the target is not present?**

> Your logic should exit when `left > right`, and return `-1`.

---

### 6. **What if the array has only one element?**

> Handle it naturally:

```python
if nums[0] == target:
    return 0
else:
    return -1
```

---

## 🔺 Follow-Up Questions

### 7. **How would you modify your code to handle arrays with duplicates?**

(This leads to **Leetcode 81: Search in Rotated Sorted Array II**)

* You may have cases like:

  ```python
  nums = [2,5,6,0,0,1,2], target = 0
  ```
* When duplicates are involved, you might need to shrink both ends:

  ```python
  if nums[left] == nums[mid] == nums[right]:
      left += 1
      right -= 1
  ```

---

### 8. **How would you find the pivot (index of smallest element)?**

> This is asked often in follow-up:

* For `[4,5,6,7,0,1,2]`, pivot index = 4 (value = 0)

```python
def findPivot(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left
```

---

### 9. **Can you split the problem into:**

* First: Find the pivot (rotation index)
* Second: Run binary search in the appropriate half

> This is a clean two-step solution (used in follow-up variants like “Minimum in Rotated Array” or “Search in Rotated Sorted Array II”).

---

### 10. **What changes if array contains negative numbers?**

> Nothing changes — binary search logic doesn’t rely on value signs, just comparisons.

---

---

# 🌍 Real-World Use Cases

Here are a few **very important real-world use cases** of the **Search in Rotated Sorted Array** pattern:

---

### ✅ 1. **Database Indexing with Partitioned Data**

* Data split into rotated chunks (e.g. time-based shards).
* Fast lookup needed on **semi-ordered data structures** like circular buffers.

---

### ✅ 2. **Operating Systems – Circular Memory Buffers (Ring Buffers)**

* Logs, audio streams, or packets stored in **rotated arrays**.
* Efficient search or retrieval in such buffers uses this logic.

---

### ✅ 3. **Search Optimization in Fault-Tolerant Systems**

* Systems may **restart mid-stream**, rotating data.
* Searching in partially rotated logs or cache arrays mimics this problem.

---

These use cases arise where **data is mostly sorted**, but rotation, wrapping, or segmentation introduces complexity — and **binary search on rotated data** becomes ideal.
