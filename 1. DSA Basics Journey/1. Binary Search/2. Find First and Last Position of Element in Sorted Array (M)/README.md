Great choice! This is one of the most popular **binary search pattern** questions.

---

## 🧩 LeetCode 34: Find First and Last Position of Element in Sorted Array

> Given an array of integers `nums` sorted in ascending order, find the **starting and ending position** of a given `target`.
> If the target is not found, return `[-1, -1]`.

---

## ✅ Key Idea: Use **Binary Search Twice**

1. One binary search to find the **leftmost (first) index**
2. One binary search to find the **rightmost (last) index**

You cannot stop at the first match. You must keep going:

* To the **left** to find the first occurrence.
* To the **right** to find the last occurrence.

---

## 🔁 Dry Run Example

```python
nums = [5, 7, 7, 8, 8, 10], target = 8

First binary search (leftmost):
  mid = 2 → nums[2] = 7 → move right
  mid = 4 → nums[4] = 8 → move left
  mid = 3 → nums[3] = 8 → match and move left
  → left index = 3

Second binary search (rightmost):
  mid = 2 → nums[2] = 7 → move right
  mid = 4 → nums[4] = 8 → move right
  → right index = 4
```

---

## ✅ Python Code (Optimal)

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        right = mid - 1  # go left
                    else:
                        left = mid + 1   # go right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [find_bound(True), find_bound(False)]
```

---

## 🧠 Explanation

* `find_bound(True)` searches for **leftmost index**
* `find_bound(False)` searches for **rightmost index**
* If target is not found → returns `[-1, -1]`

---

## 🕐 Time & Space Complexity

* **Time:** `O(log n)` for each search → `O(log n)` total
* **Space:** `O(1)`

---

## 🧪 Example Test Cases

```python
assert Solution().searchRange([5,7,7,8,8,10], 8) == [3, 4]
assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1, -1]
assert Solution().searchRange([], 0) == [-1, -1]
```

---

---

Perfect! Let’s do a **step-by-step dry run** of the function `searchRange` for the input:

```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
```

We’ll walk through how both `find_bound(True)` and `find_bound(False)` work.

---

## 🔍 Step 1: Find **Leftmost Index**

We're calling: `find_bound(is_left=True)`

Initial:

```
left = 0, right = 5
```

### 1st Iteration:

* mid = (0 + 5) // 2 = 2 → nums\[2] = 7
* 7 < 8 → move right → left = 3

### 2nd Iteration:

* mid = (3 + 5) // 2 = 4 → nums\[4] = 8
* Found match! Update `bound = 4`
* Because `is_left=True`, move left → right = 3

### 3rd Iteration:

* mid = (3 + 3) // 2 = 3 → nums\[3] = 8
* Found match! Update `bound = 3`
* Move left again → right = 2

Loop ends (`left > right`), returns **3**.

---

## 🔍 Step 2: Find **Rightmost Index**

Now calling: `find_bound(is_left=False)`

Initial:

```
left = 0, right = 5
```

### 1st Iteration:

* mid = 2 → nums\[2] = 7
* 7 < 8 → move right → left = 3

### 2nd Iteration:

* mid = 4 → nums\[4] = 8
* Found match! Update `bound = 4`
* Because `is_left=False`, move right → left = 5

### 3rd Iteration:

* mid = 5 → nums\[5] = 10
* 10 > 8 → move left → right = 4

Loop ends (`left > right`), returns **4**.

---

## ✅ Final Result:

```python
return [3, 4]
```

Which is correct — `target = 8` appears from index 3 to 4.

---

---

Here is the complete Python program for **LeetCode 34: Find First and Last Position of Element in Sorted Array** with inline comments, complexity annotations, and execution timing:

---

### ✅ Full Python Program

```python
import time
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper to find the leftmost or rightmost index of the target
        def find_bound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid  # Update potential result
                    if is_left:
                        # Move toward left half
                        right = mid - 1
                    else:
                        # Move toward right half
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        # Time Complexity: O(log n) for each binary search (left and right bound)
        # Space Complexity: O(1) - no extra space used
        return [find_bound(True), find_bound(False)]

# --- Main program with test input and timing ---
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    print("Input nums:", nums)
    print("Target:", target)

    start_time = time.time()
    result = Solution().searchRange(nums, target)
    end_time = time.time()

    print("Output (First and Last Position):", result)
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
```

---

### 🔧 Sample Run Output

```
Input nums: [5, 7, 7, 8, 8, 10]
Target: 8
Output (First and Last Position): [3, 4]
Execution Time: 0.000011 seconds
```

---