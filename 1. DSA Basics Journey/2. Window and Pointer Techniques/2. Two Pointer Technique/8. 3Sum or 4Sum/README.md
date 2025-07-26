Let's explore **3Sum (LC 15)** and **4Sum (LC 18)** — classic problems solved using the **Two Pointer** technique after **sorting**, with some extensions.

---

## 🔷 Leetcode 15 – 3Sum

### 🔍 Problem

> Find all unique triplets in the array which gives the sum of zero.

### 🧪 Example

```python
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

---

## ✅ Optimal Approach: Sort + Two Pointer

### 💡 Idea:

1. **Sort** the array
2. **Fix one number**, then use **two pointers** to find the remaining two

---

## 🧑‍💻 Python Code for 3Sum

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
```

### ⏱ Complexity

| Metric | Value                   |
| ------ | ----------------------- |
| Time   | O(n²)                   |
| Space  | O(1) or O(k) for result |

---

## 🔷 Leetcode 18 – 4Sum

### 🔍 Problem

> Find all unique quadruplets `[a, b, c, d]` such that `a + b + c + d == target`.

### 🧪 Example

```python
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

---

## ✅ Approach: Sort + 2 Loops + Two Pointer

### 💡 Strategy:

* Fix first two indices in nested loops
* Use two pointers for the other two values
* Skip duplicates at each step

---

## 🧑‍💻 Python Code for 4Sum

```python
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # skip duplicates
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res
```

### ⏱ Complexity

| Metric | Value                   |
| ------ | ----------------------- |
| Time   | O(n³)                   |
| Space  | O(1) or O(k) for result |

---

## 🔍 Interview FAQs

| Question                            | Answer                                                 |
| ----------------------------------- | ------------------------------------------------------ |
| Why sort first?                     | Allows skipping duplicates & enables two-pointer logic |
| How to avoid duplicates?            | Skip repeated elements in all loops and pointers       |
| Can we use a hashset?               | Possible for brute force, but less efficient           |
| Can this be extended to 5Sum, 6Sum? | Yes, recursively (k-Sum generalization)                |

---

## 🌍 Real-World Applications

* **Financial auditing**: Detecting groups of transactions that cancel each other out
* **Security analysis**: Finding sets of log entries or signals that neutralize
* **Game development**: Validating group-based resource or damage systems

---
