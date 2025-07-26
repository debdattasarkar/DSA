Let’s go step-by-step through **Leetcode 167 – Two Sum II: Input Array Is Sorted**, solved using the **Two Pointer Technique**.

---

## 🔍 Problem Statement

> Given a **1-indexed sorted array** of integers `numbers` and a target integer `target`, return the indices of the two numbers such that they add up to `target`.

* The answer must be returned as a list: `[index1, index2]` (1-based).
* There is **exactly one solution**.

---

## 🧪 Example

```python
Input: numbers = [2, 7, 11, 15], target = 9  
Output: [1, 2]
```

Because `numbers[0] + numbers[1] = 2 + 7 = 9`.

---

## ✅ Approach: Two Pointers (Left + Right)

### 💡 Strategy:

* Since the array is sorted:

  * Start with two pointers: `left = 0`, `right = n-1`
  * Calculate `sum = numbers[left] + numbers[right]`

    * If `sum == target`, return the indices
    * If `sum < target`, move `left` forward
    * If `sum > target`, move `right` backward

---

## 🧑‍💻 Python Code with Inline Comments

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Convert 0-based to 1-based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []  # Should never reach here due to problem guarantee
```

---

## ⏱ Time and Space Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(1)  |

---

## 🧠 Dry Run

Input:

```python
numbers = [2, 7, 11, 15], target = 9
```

| Step | Left | Right | numbers\[left] | numbers\[right] | Sum | Action               |
| ---- | ---- | ----- | -------------- | --------------- | --- | -------------------- |
| 1    | 0    | 3     | 2              | 15              | 17  | Too big → move right |
| 2    | 0    | 2     | 2              | 11              | 13  | Too big → move right |
| 3    | 0    | 1     | 2              | 7               | 9   | ✅ Match found        |

---

## ❓ Interview Q\&A

| Question                                                  | Answer                                           |
| --------------------------------------------------------- | ------------------------------------------------ |
| Why is this more efficient than brute-force?              | Because we only scan once: O(n) instead of O(n²) |
| What property enables two-pointer usage here?             | The array is **sorted**                          |
| Can this be extended to more than 2 elements (e.g. 3Sum)? | Yes, sort and fix one element → then apply 2-ptr |
| What if array had duplicates?                             | Doesn’t matter — we only need one valid pair     |

---

## 🧪 Real-World Use Cases

* **Transaction matching**: Find two transactions adding up to a known total
* **Time-bound processing**: Allocate two resources to exactly fit a time slot
* **Price matching**: Find two items whose prices sum up to a target budget

---
