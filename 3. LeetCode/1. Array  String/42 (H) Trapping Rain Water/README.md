
---

# 🌧️ 42. Trapping Rain Water

### 🔴 Difficulty: Hard

**Topics**: `Array`, `Two Pointers`, `Dynamic Programming`, `Stack`, `Monotonic Stack`
**Companies**: Featured in several top tech interviews.

---

## 📘 Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

## 🧪 Examples

### Example 1

```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Explanation**:
The elevation map can be visualized as bars where the blue shaded region represents water.
In this example, 6 units of rainwater are trapped in valleys between bars.

```
Elevation:      █ █     █ █     █   █ █ █
Water Trapped:    █ █ █   █ █ █   █
                  ↑       ↑       ↑
Total = 6 units
```

### Example 2

```
Input:  height = [4,2,0,3,2,5]
Output: 9
```

**Explanation**:
In this example, water is trapped between bars at several valleys, totaling 9 units.

---

## 🧮 Constraints

* `n == height.length`
* `1 <= n <= 2 * 10⁴`
* `0 <= height[i] <= 10⁵`

---

## ✅ Summary

You are required to calculate the total amount of rainwater trapped between bars based on an elevation map. The bars can trap water if a bar is lower than bars on both sides. Several optimal approaches exist (using stacks or two pointers) that work in linear time and constant space.

---

Here's the complete **text explanation**, **step-by-step dry run**, and **optimized code with inline comments** for **Leetcode 42 – Trapping Rain Water**, in **Python**, **C++**, and **JavaScript**, along with **commonly asked interview questions**.

---

## 📘 Problem Summary

Given an array `height[]` representing an elevation map, compute how much water can be trapped after raining.

---

## ✅ Key Constraints

* Width of each bar = 1
* Each element in `height` is non-negative
* Trapped water only depends on the *left max* and *right max* boundaries of each bar

---

## 🧠 Optimal Two Pointer Approach (O(n) Time, O(1) Space)

* Maintain two pointers: `left` and `right`
* Track `left_max` and `right_max` as you move inward
* Water trapped at each position is `min(left_max, right_max) - height[i]`

---

## 🧪 Dry Run

### Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`

### Expected Output: `6`

```
left=0, right=11
left_max=0, right_max=1

i = 2 → height = 0, left_max = 1, right_max = 2
Water = min(1,2) - 0 = 1 ✅
...
i = 5 → height = 0, left_max = 2, right_max = 3
Water = min(2,3) - 0 = 2 ✅
...
i = 6 → height = 1, left_max = 2, right_max = 3
Water = 1 ✅
...
→ Total = 6
```

---

## 💬 Common Interviewer Questions

**Q1:** Can you solve this using O(n) time and O(1) space?
**A1:** Yes, using two pointers and dynamically tracking `left_max` and `right_max`.

**Q2:** Why does it work to use the min of `left_max` and `right_max`?
**A2:** Because water trapped at position `i` is limited by the shorter of the two walls surrounding it.

**Q3:** Can you explain when to move `left` vs `right`?
**A3:** Always move the pointer with the **smaller height**, since it is the limiting factor.

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # update left wall
                else:
                    water += left_max - height[left]  # trap water
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # update right wall
                else:
                    water += right_max - height[right]  # trap water
                right -= 1

        return water
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int left_max = 0, right_max = 0, water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max)
                    left_max = height[left];
                else
                    water += left_max - height[left];
                left++;
            } else {
                if (height[right] >= right_max)
                    right_max = height[right];
                else
                    water += right_max - height[right];
                right--;
            }
        }
        return water;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let left = 0, right = height.length - 1;
    let leftMax = 0, rightMax = 0, water = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax)
                leftMax = height[left];
            else
                water += leftMax - height[left];
            left++;
        } else {
            if (height[right] >= rightMax)
                rightMax = height[right];
            else
                water += rightMax - height[right];
            right--;
        }
    }
    return water;
};
```

---

## ✅ Summary

| Metric           | Value                |
| ---------------- | -------------------- |
| Time Complexity  | `O(n)`               |
| Space Complexity | `O(1)`               |
| Strategy         | Two pointers, Greedy |

---

Yes, absolutely! The code you've shared is a **stack-based solution** for the **Trapping Rain Water** problem (Leetcode 42), and it's a valid and well-known approach that also works in **O(n) time** and **O(n) space**.

```python

from collections import deque

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Get length of input array
        n = len(height)
        
        # Initialize stack to store indices of bars
        stack = deque()
        
        # Variable to accumulate total trapped water
        out = 0
        
        # Iterate over each block
        for i in range(n):
            # While stack is not empty and current height is greater than top of stack
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                # Pop the top element (this is the bottom of the water container)
                lower_height = height[stack[-1]]
                stack.pop()

                # If stack becomes empty, no left boundary exists
                if len(stack) == 0:
                    break

                # Now the stack's new top is the left boundary
                left = stack[-1]
                
                # Width between left and right boundary, minus the bottom block
                dist = i - left - 1

                # Height of water is limited by the shorter of the two walls
                bounded_height = min(height[i], height[left]) - lower_height

                # Water volume = width * bounded_height
                out += dist * bounded_height

            # Push current index onto the stack
            stack.append(i)

        # Return the total trapped water
        return out
```

---

## ✅ How It Works (Stack-Based)

* This method uses a **monotonic decreasing stack** to track the indices of elevation bars.
* When we find a height **greater than the top of the stack**, it means a **right boundary** is found — so we pop the middle (bottom) and compute trapped water between this and the new top (left boundary).

---

## 🔍 Dry Run on Example

**Input:** `arr = [0,1,0,2,1,0,1,3,2,1,2,1]`

At each point, the stack stores indices of **descending heights**. When a new taller height is found, we start popping and compute:

* **bounded height**: `min(height[left], height[right]) - height[middle]`
* **width**: `right - left - 1`
* Multiply them to get trapped water in that section.

---

## ✅ Characteristics

| Feature       | Stack-Based Solution             |
| ------------- | -------------------------------- |
| Time          | `O(n)`                           |
| Space         | `O(n)` due to stack              |
| Suitable when | Visualizing "valleys" directly   |
| Optimal?      | ✅ Yes, like two-pointer approach |

---

## 🧠 Interview Comparison

| Strategy    | Pros                           | Cons                                |
| ----------- | ------------------------------ | ----------------------------------- |
| Two-Pointer | O(1) space, intuitive for flow | Less visual, needs care with bounds |
| Stack-Based | Intuitive for valleys          | Uses O(n) stack memory              |

---

## ✅ Verdict

Your provided implementation is:

* ✔️ Correct
* 💡 Optimal (linear time)
* 🔄 Easy to convert into Python/C++/JavaScript

---
