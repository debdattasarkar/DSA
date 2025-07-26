Let's dive into **Leetcode 11 – Container With Most Water**, a **classic Two Pointer problem** for maximizing area between two lines.

---

## 🔍 Problem Statement

> You are given an array `height[]` where each element represents the height of a vertical line on the x-axis.
> Find **two lines** that together with the x-axis form a container that holds the **most water**.

Return the **maximum area** of water the container can store.

---

### 🧪 Example:

```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

**Explanation**:

* Choose height\[1]=8 and height\[8]=7 → width=7
* Area = min(8,7) \* 7 = 49

---

## ✅ Intuition

We want to **maximize the area = width × min(height\[i], height\[j])**.

---

## 💡 Approach: Two Pointer Technique

### Strategy:

* Place two pointers `left = 0` and `right = n - 1`
* Calculate area between them
* Move the pointer with **smaller height** inward (since only increasing height can help)

---

## 🧑‍💻 Python Code (With Inline Comments)

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate width and height
            width = right - left
            ht = min(height[left], height[right])
            area = width * ht

            # Update max area if needed
            max_area = max(max_area, area)

            # Move pointer with smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

## ⏱ Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧠 Dry Run

Input: `[1,8,6,2,5,4,8,3,7]`

| Left                                                              | Right | Width | minHeight | Area | Max Area |
| ----------------------------------------------------------------- | ----- | ----- | --------- | ---- | -------- |
| 0                                                                 | 8     | 8     | 1         | 8    | 8        |
| 1                                                                 | 8     | 7     | 7         | 49   | 49 ✅     |
| 1                                                                 | 7     | 6     | 3         | 18   | 49       |
| ...                                                               | ...   | ...   | ...       | ...  | ...      |
| → Best pair is `height[1]=8` and `height[8]=7` → area = `7*7=49`. |       |       |           |      |          |

---

## ❓ Interview Questions & Clarifications

| Question                      | Answer                                                      |
| ----------------------------- | ----------------------------------------------------------- |
| Why not try all pairs?        | That’s O(n²); two-pointer gives O(n)                        |
| Why move the shorter pointer? | Because the taller one can't increase area if shorter stays |
| Can we use stack here?        | Not optimal here                                            |
| Can heights be zero?          | Yes — treated like 0-height line                            |

---

## 🧪 Real-World Use Cases

* **Flood prediction**: Max water a terrain slice can store between two hills
* **Reservoir design**: Maximize stored volume between physical boundaries
* **Image histogram segmentation** (edge detection)

---
