Here is a complete README in Markdown format based on the provided problem description and constraints:

---

# Sort the Given Array After Applying the Given Equation

## Introduction

This problem focuses on transforming and sorting an array based on a mathematical function. You are given a **sorted array** and coefficients `A`, `B`, and `C` for a **quadratic equation**. The goal is to apply this equation to each element and return the transformed array in sorted order.

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given a sorted array `arr[]` in ascending order and three integers `A`, `B`, and `C`, transform each element `x` in the array using the quadratic function:

```
f(x) = A * x^2 + B * x + C
```

Then return the **transformed array in sorted order**.

---

## Examples

### Example 1

```
Input: arr[] = [-4, -2, 0, 2, 4], A = 1, B = 3, C = 5  
Output: [3, 5, 9, 15, 33]  

Explanation:  
f(x) = 1*x^2 + 3*x + 5  
Transformed values: [9, 3, 5, 15, 33] → Sorted: [3, 5, 9, 15, 33]
```

### Example 2

```
Input: arr[] = [-3, -1, 2, 4], A = -1, B = 0, C = 0  
Output: [-16, -9, -4, -1]

Explanation:  
f(x) = -1*x^2  
Transformed values: [-9, -1, -4, -16] → Sorted: [-16, -9, -4, -1]
```

---

## Constraints

* `1 ≤ arr.length ≤ 10^6`
* `-10^3 ≤ arr[i], A, B, C ≤ 10^3`

---

## Expected Complexity

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(n)

---

## Tags

### Company Tags

`Adobe`

### Topic Tags

`Mathematical`, `Sorting`, `Algorithms`

---

## Related Articles

* [Sort Array Applying Given Equation](#)

---

Here is a **complete explanation**, including a **step-by-step dry run** of the algorithm, followed by **Python, C++, and JavaScript implementations** with inline comments.

---

## 📘 Problem Summary

You are given a sorted array `arr[]` and coefficients `A`, `B`, `C`. You must apply the transformation:

```
f(x) = A*x^2 + B*x + C
```

...to every element `x` in `arr`, then return the transformed array **in sorted order**.

---

## 🧠 Key Insight

### Why is it tricky?

* The input array is already **sorted**, but applying a **quadratic** function could **disrupt** that order.
* A naive approach is to apply the transformation and sort the result — O(n log n).
* However, **we can achieve O(n)** using a **two-pointer approach**, leveraging the properties of the quadratic function.

---

## 🔍 Quadratic Function Behavior

* When **A > 0**, the parabola opens **upwards** (U-shape): smallest values near the **vertex**, largest at the ends.
* When **A < 0**, the parabola opens **downwards** (∩-shape): largest values near the vertex, smallest at ends.

This allows us to:

* Compare values at the two ends of the sorted array.
* Fill the output array from the correct direction based on the sign of `A`.

---

## 🧪 Dry Run Example

**Input:**

```text
arr = [-4, -2, 0, 2, 4], A = 1, B = 3, C = 5
```

**Transformation:**

```text
f(x) = x^2 + 3x + 5
```

**Transformed values (unsorted):**

```text
f(-4)=9, f(-2)=3, f(0)=5, f(2)=15, f(4)=33 → [9, 3, 5, 15, 33]
```

**Sorted output:**

```text
[3, 5, 9, 15, 33]
```

---

## ✅ Python Implementation

```python
class Solution:
    def sortArray(self, arr, A, B, C):
        def f(x):
            return A*x*x + B*x + C

        n = len(arr)
        res = [0]*n
        left, right = 0, n - 1
        idx = n - 1 if A >= 0 else 0  # Fill from end if A ≥ 0, else from start

        while left <= right:
            left_val = f(arr[left])
            right_val = f(arr[right])

            if A >= 0:
                if left_val > right_val:
                    res[idx] = left_val
                    left += 1
                else:
                    res[idx] = right_val
                    right -= 1
                idx -= 1
            else:
                if left_val < right_val:
                    res[idx] = left_val
                    left += 1
                else:
                    res[idx] = right_val
                    right -= 1
                idx += 1

        return res
```

---

## ✅ C++ Implementation

```cpp
class Solution {
  public:
    vector<int> sortArray(vector<int> &arr, int A, int B, int C) {
        auto f = [&](int x) {
            return A*x*x + B*x + C;
        };
        
        int n = arr.size();
        vector<int> res(n);
        int left = 0, right = n - 1;
        int idx = (A >= 0) ? n - 1 : 0;

        while (left <= right) {
            int leftVal = f(arr[left]);
            int rightVal = f(arr[right]);

            if (A >= 0) {
                if (leftVal > rightVal) {
                    res[idx--] = leftVal;
                    left++;
                } else {
                    res[idx--] = rightVal;
                    right--;
                }
            } else {
                if (leftVal < rightVal) {
                    res[idx++] = leftVal;
                    left++;
                } else {
                    res[idx++] = rightVal;
                    right--;
                }
            }
        }

        return res;
    }
};
```

---

## ✅ JavaScript Implementation

```javascript
class Solution {
    sortArray(arr, A, B, C) {
        const f = (x) => A * x * x + B * x + C;

        let n = arr.length;
        let res = new Array(n);
        let left = 0, right = n - 1;
        let idx = A >= 0 ? n - 1 : 0;

        while (left <= right) {
            let leftVal = f(arr[left]);
            let rightVal = f(arr[right]);

            if (A >= 0) {
                if (leftVal > rightVal) {
                    res[idx--] = leftVal;
                    left++;
                } else {
                    res[idx--] = rightVal;
                    right--;
                }
            } else {
                if (leftVal < rightVal) {
                    res[idx++] = leftVal;
                    left++;
                } else {
                    res[idx++] = rightVal;
                    right--;
                }
            }
        }

        return res;
    }
}
```

---

## 🧩 Summary

| Aspect           | Description                              |
| ---------------- | ---------------------------------------- |
| Key technique    | Two-pointer traversal from ends          |
| Optimal time     | O(n)                                     |
| Handles parabola | Both upward (A > 0) and downward (A < 0) |
| Extra space      | O(n) for result array                    |

Let me know if you’d like this code integrated into a web tool or tested against custom input!

