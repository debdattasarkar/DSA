# 🧶 Remove the Balls

---

## 📝 Problem Statement

You are given two arrays: `color[]` and `radius[]`, representing a sequence of balls:

* `color[i]` is the color of the i-th ball.
* `radius[i]` is the radius of the i-th ball.

### 🎯 Rule:

If two **consecutive** balls have the **same color and radius**, remove them both. Repeat this process **until no more such pairs exist**.

### 🔁 Output:

Return the **number of balls remaining** after all possible removals.

---

## 💡 Examples

### Example 1:

```
Input:
color[] = [2, 3, 5]
radius[] = [3, 3, 5]

Output:
3

Explanation:
All 3 balls have different colors and radius. So, nothing is removed.
```

---

### Example 2:

```
Input:
color[] = [2, 2, 5]
radius[] = [3, 3, 5]

Output:
1

Explanation:
The first two balls are identical in color and radius.
They are removed as a pair. Only one ball remains.
```

---

## ✅ Constraints

* `1 ≤ color.length = radius.length ≤ 10⁵`
* `1 ≤ color[i], radius[i] ≤ 10⁹`

---

## ⏱ Expected Time and Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🧰 Topic Tags

* Stack
* Data Structures

---

## 📚 Related Articles

* [Length Of Array After Removing Consecutive Balls](#)

---

Here’s the complete **step-by-step explanation with a dry run**, followed by **Python, C++, and JavaScript implementations** with inline comments for the **“Remove the Balls”** problem:

---

## ✅ **Text Explanation**

We’re given two lists: `color[]` and `radius[]`, each representing a ball. If **two consecutive balls** have **the same color and same radius**, they are **removed** as a pair. We must repeat this process **until no more such adjacent pairs exist**, and return the **number of balls left**.

---

## 🧠 **Approach (Using Stack)**

We’ll use a **stack** to simulate the removal process:

1. For each ball `(color[i], radius[i])`:

   * If the top of the stack matches the current ball, pop the stack (remove both).
   * Else, push the current ball on the stack.
2. After processing all balls, the stack contains the remaining balls.
3. Return the stack size.

---

## 🧪 **Step-by-Step Dry Run**

### Example:

```text
Input: 
color  = [2, 2, 3, 3, 2]
radius = [3, 3, 5, 5, 2]

Step-by-step:
Stack = []

1. Push (2,3)           => Stack: [(2,3)]
2. (2,3) == Top         => Pop     → Stack: []
3. Push (3,5)           => Stack: [(3,5)]
4. (3,5) == Top         => Pop     → Stack: []
5. Push (2,2)           => Stack: [(2,2)]

Final stack: [(2,2)] → Answer: 1
```

---

## 🐍 Python Code

```python
#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        stack = []

        for c, r in zip(color, radius):
            if stack and stack[-1] == (c, r):
                # Found a matching consecutive pair; remove it
                stack.pop()
            else:
                # Otherwise, push the current ball
                stack.append((c, r))

        # Remaining balls count is the size of the stack
        return len(stack)
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int findLength(vector<int> &color, vector<int> &radius) {
        stack<pair<int, int>> stk;

        for (int i = 0; i < color.size(); ++i) {
            pair<int, int> ball = {color[i], radius[i]};
            if (!stk.empty() && stk.top() == ball) {
                stk.pop(); // Remove matching pair
            } else {
                stk.push(ball); // Add new ball to stack
            }
        }

        return stk.size(); // Remaining balls
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    findLength(color, radius) {
        let stack = [];

        for (let i = 0; i < color.length; i++) {
            let current = [color[i], radius[i]];

            if (
                stack.length > 0 &&
                stack[stack.length - 1][0] === current[0] &&
                stack[stack.length - 1][1] === current[1]
            ) {
                stack.pop(); // Remove matching consecutive pair
            } else {
                stack.push(current); // Add new ball
            }
        }

        return stack.length; // Number of remaining balls
    }
}
```

---
