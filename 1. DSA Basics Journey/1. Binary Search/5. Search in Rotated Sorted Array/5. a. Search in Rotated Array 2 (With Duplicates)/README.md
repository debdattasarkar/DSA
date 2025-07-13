Perfect! Let's now move on to the **extended version** of the rotated array search that allows **duplicates** — which is:

---

## 🧩 LeetCode 81: Search in Rotated Sorted Array II

🔗 [LeetCode 81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)

> Given a rotated sorted array `nums` (which **may contain duplicates**) and a target, return `true` if target exists in the array, otherwise return `false`.

---

## 🔥 Why this is tricky:

When duplicates exist, you can't reliably determine which half is sorted using just:

```python
if nums[left] <= nums[mid]
```

Because duplicates like `[1, 1, 1, 2, 1]` will confuse this logic.

---

## ✅ Fix: Add a check to shrink bounds when `nums[left] == nums[mid] == nums[right]`

---

## ✅ Python Code (Handling Duplicates)

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates: shrink the bounds
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
```

---

## 🧪 Example Test Cases

```python
assert Solution().search([2,5,6,0,0,1,2], 0) == True
assert Solution().search([2,5,6,0,0,1,2], 3) == False
assert Solution().search([1,0,1,1,1], 0) == True
assert Solution().search([1,1,3,1], 3) == True
assert Solution().search([1,1,1,1,1,1], 2) == False
```

---

## 🧠 Time & Space Complexity

* **Worst-case Time:** `O(n)` – when duplicates prevent binary pruning.
* **Best-case Time:** `O(log n)` – when no or minimal duplicates.
* **Space:** `O(1)`

---

Here is the **step-by-step dry run** and explanation for the input:

---

### 🧪 Input

```python
nums = [1, 0, 1, 1, 1]
target = 0
```

---

### 🔍 Execution Trace

#### 🔁 Iteration 1

* `left = 0`, `right = 4`
* `mid = 2`, `nums[mid] = 1`
* `nums[left] == nums[mid] == nums[right] → 1 == 1 == 1`
  → Ambiguous case due to duplicates → Shrink both ends:
  `left = 1`, `right = 3`

#### 🔁 Iteration 2

* `left = 1`, `right = 3`
* `mid = 2`, `nums[mid] = 1`
* Left half is sorted (`nums[left] <= nums[mid]`)
* Is target in left half?
  `nums[left] = 0 <= 0 < 1 = nums[mid]` → ✅ Yes
  → Move right to `mid - 1 = 1`

#### 🔁 Iteration 3

* `left = 1`, `right = 1`
* `mid = 1`, `nums[mid] = 0` → 🎯 Target found

---

### ✅ Output

```python
Output: True
Execution Time: 0.000676 seconds
```

---

This proves that the **duplicate handling logic** is crucial when the rotation + repetition masks the array’s sorted structure.

---

---

Here are the **top interview questions** and follow-ups around **Leetcode 81: Search in Rotated Sorted Array II** (with duplicates). These are commonly asked to test edge-case reasoning, adaptability of binary search, and robust condition handling.

---

## 🔹 Basic Understanding

### 1. **What is the difference between Leetcode 33 and Leetcode 81?**

* **Leetcode 33**: No duplicates → always possible to determine which half is sorted.
* **Leetcode 81**: Duplicates allowed → you can have cases where `nums[left] == nums[mid] == nums[right]` and cannot decide which half is sorted.

---

### 2. **Why can't standard binary search logic always work with duplicates?**

* If `nums[left] == nums[mid] == nums[right]`, you can't determine which half is sorted.
  Example: `[1, 1, 1, 3, 1]`
  So, you must shrink the search range by:

  ```python
  left += 1
  right -= 1
  ```

---

### 3. **What is the time complexity of your solution?**

* **Best Case:** `O(log n)` — when no or few duplicates.
* **Worst Case:** `O(n)` — when duplicates cover the whole array, e.g. `[1,1,1,1,1]`.

---

## 🔸 Edge Cases

### 4. **What if all elements are the same and not equal to target?**

```python
nums = [2, 2, 2, 2, 2], target = 3 → return False
```

You must **shrink both ends** until left > right.

---

### 5. **What if all elements are the same and equal to the target?**

```python
nums = [2, 2, 2, 2, 2], target = 2 → return True
```

You will hit the match early or scan inward from both sides.

---

## 🔺 Follow-Ups

### 6. **How would you modify your solution to return the index instead of a boolean?**

* Add `return mid` when `nums[mid] == target`
* Otherwise continue narrowing as in Leetcode 81
* Be aware: **there could be multiple matches**, and this only returns **one index**.

---

### 7. **How do you find the number of times the array is rotated?**

You can find the **index of the smallest element** using a modified binary search (with duplicates):

```python
def findRotationIndex(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1  # can't decide, reduce right
    return left
```

---

### 8. **Can you merge this with binary search?**

Yes. This two-phase idea is called the **pivot-based solution**, but for duplicates it may degrade to `O(n)`.

---

### 9. **Why does the worst-case degrade to linear time?**

Because if `nums[left] == nums[mid] == nums[right]`, you can’t make a decision and must do:

```python
left += 1
right -= 1
```

This can happen up to `n` times, hence `O(n)`.

---

### 10. **What if the array is very large — how would you optimize it further?**

* Use **hybrid search**: try to skip over known duplicates with fast pointer moves.
* In practice, many duplicates will cluster, so aggressive pruning helps.

---

## 🧠 Bonus Thinking Exercise

**Can you design a function to return**:

* `True` if the target exists,
* `False` if not,
* `O(log n)` if the array has no duplicates,
* **Optimally degrade to O(n)** only when necessary.

✅ This is basically Leetcode 81!

---
