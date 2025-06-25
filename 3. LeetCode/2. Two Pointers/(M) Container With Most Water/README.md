
---

# 11. Container With Most Water

**Level**: Medium
**Topics**: `Array`, `Two Pointers`, `Greedy`

---

You are given an integer array `height` of length `n`.
There are `n` vertical lines drawn such that the two endpoints of the `iᵗʰ` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

📌 **Notice**: You may not slant the container.

---

### Example 1:

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation:
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2:

```
Input: height = [1,1]
Output: 1
```

---

### ✅ Constraints:

* `n == height.length`
* `2 <= n <= 10⁵`
* `0 <= height[i] <= 10⁴`

---

### 💡 Hints

**Hint 1**:
If you simulate the problem, it will be `O(n²)` which is not efficient.

**Hint 2**:
Try to use **two pointers**.
Set one pointer to the left and one to the right of the array.
Always move the pointer that points to the **lower** line.

**Hint 3**:
How can you calculate the amount of water at each step?

---

## ✅ 1. Text Explanation with Step-by-Step Dry Run

### 🔍 **Problem Summary**

You're given an array `height[]` where each value represents the height of a vertical line at position `i`.
You must **choose two lines** such that they, along with the x-axis, **form a container that can hold the most water**.
The area is calculated as:

```
area = min(height[i], height[j]) * (j - i)
```

---

### 🔧 **Optimized Approach: Two-Pointer Technique**

* Place one pointer at the start (`left = 0`) and one at the end (`right = n-1`)
* Calculate the area and update `max_area`
* Move the pointer pointing to the **shorter line** inward (because the area is limited by the shorter line)

---

### 🧪 Dry Run for `height = [1,8,6,2,5,4,8,3,7]`:

| left | right | height\[left] | height\[right] | width | area | max\_area |
| ---- | ----- | ------------- | -------------- | ----- | ---- | --------- |
| 0    | 8     | 1             | 7              | 8     | 8    | 8         |
| 1    | 8     | 8             | 7              | 7     | 49   | 49        |
| 1    | 7     | 8             | 3              | 6     | 18   | 49        |
| 1    | 6     | 8             | 8              | 5     | 40   | 49        |
| 1    | 5     | 8             | 4              | 4     | 16   | 49        |
| 1    | 4     | 8             | 5              | 3     | 15   | 49        |
| 1    | 3     | 8             | 2              | 2     | 4    | 49        |
| 1    | 2     | 8             | 6              | 1     | 6    | 49        |
| 1    | 1     | -             | -              | -     | -    | **49**    |

---

## ✅ 2. Code Implementations

### 🔸 Python

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area between lines at left and right
            width = right - left
            h = min(height[left], height[right])
            area = h * width
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

### 🔹 C++

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxArea = 0;

        while (left < right) {
            int h = min(height[left], height[right]);
            int width = right - left;
            maxArea = max(maxArea, h * width);

            // Move the shorter side inward
            if (height[left] < height[right])
                left++;
            else
                right--;
        }

        return maxArea;
    }
};
```

---

### 🔸 JavaScript

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0, right = height.length - 1;
    let maxArea = 0;

    while (left < right) {
        let h = Math.min(height[left], height[right]);
        let width = right - left;
        maxArea = Math.max(maxArea, h * width);

        // Move the pointer pointing to the smaller height
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
};
```

---

## ✅ 3. Interview Questions and Answers

### 📌 Q1. Why do we use the two-pointer approach?

**A:** Because a brute force `O(n^2)` solution would check all pairs, which is too slow. The two-pointer approach brings the time complexity to `O(n)` by narrowing down the range and always moving the shorter side inward.

---

### 📌 Q2. Why move the shorter height pointer?

**A:** The amount of water is constrained by the shorter height. To potentially find a taller boundary (which could increase area), we move the pointer at the shorter wall.

---

### 📌 Q3. Can height be negative or zero?

**A:** Per constraints, `height[i]` is non-negative. A height of `0` contributes no area but can be part of the two-pointer scanning.

---

### 📌 Q4. What if there are multiple answers?

**A:** Only the **maximum area** is required, not the indices, so we keep updating the maximum found.

---
