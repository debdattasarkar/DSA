# Smallest Subarray with Sum Greater than X

## Problem Statement

Given a number `x` and an array of integers `arr`, find the **smallest subarray** with sum **greater than the given value** `x`. If such a subarray does not exist, return `0`.

---

## Examples

### Example 1

**Input**:

```
x = 51  
arr[] = [1, 4, 45, 6, 0, 19]
```

**Output**:

```
3
```

**Explanation**:
The smallest subarray with sum greater than 51 is `[4, 45, 6]`. Length = 3.

---

### Example 2

**Input**:

```
x = 100  
arr[] = [1, 10, 5, 2, 7]
```

**Output**:

```
0
```

**Explanation**:
There is no subarray with sum greater than 100.

---

## Constraints

* $1 \leq \text{arr.size}, x \leq 10^5$
* $0 \leq \text{arr}[i] \leq 10^4$

---

## Expected Time and Space Complexity

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(1)

---

## Topics

* Arrays
* Sliding Window
* Data Structures

---

## Related Articles

* [Minimum Length Subarray Sum Greater Given Value](https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/)

---

## Companies

This problem is frequently asked by:

* Accolite
* Amazon
* Goldman Sachs
* Google
* Facebook

---

Here's a complete **text explanation**, **step-by-step dry run**, and implementations in **Python**, **C++**, and **JavaScript** with inline comments for the **Smallest Subarray with Sum Greater than X** problem.

---

## 🔍 **Text Explanation**

We aim to find the **smallest contiguous subarray** whose sum is **strictly greater** than a given integer `x`.

### ✅ **Approach: Sliding Window Technique**

1. Initialize variables: `start = 0`, `end = 0`, `curr_sum = 0`, `min_len = ∞`.
2. Expand the window by moving `end` and add `arr[end]` to `curr_sum`.
3. While `curr_sum > x`, update `min_len` and try shrinking the window by incrementing `start` and subtracting `arr[start]` from `curr_sum`.
4. Return `min_len` if found, else return `0`.

---

## 🧮 **Step-by-Step Dry Run**

### Input

```text
x = 51
arr = [1, 4, 45, 6, 0, 19]
```

### Execution Trace:

```
start=0, end=0, curr_sum=1
start=0, end=1, curr_sum=5
start=0, end=2, curr_sum=50
start=0, end=3, curr_sum=56 -> > 51
  → min_len = 4
  → shrink window: curr_sum=55, start=1
  → shrink window: curr_sum=51, start=2
start=3, end=4, curr_sum=57 -> > 51
  → min_len = 3
  → shrink: curr_sum=12, start=3
```

### Result: `3` (subarray `[4, 45, 6]`)

---

## 🐍 Python Code

```python
class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        start = 0
        curr_sum = 0
        min_len = float('inf')

        for end in range(n):
            curr_sum += arr[end]

            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1

        return min_len if min_len != float('inf') else 0
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int smallestSubWithSum(int x, vector<int>& arr) {
        int n = arr.size();
        int start = 0, curr_sum = 0, min_len = INT_MAX;

        for (int end = 0; end < n; end++) {
            curr_sum += arr[end];

            while (curr_sum > x) {
                min_len = min(min_len, end - start + 1);
                curr_sum -= arr[start++];
            }
        }

        return (min_len == INT_MAX) ? 0 : min_len;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    /**
     * @param {number[]} arr
     * @param {number} x
     * @return {number}
     */
    smallestSubWithSum(arr, x) {
        let n = arr.length;
        let start = 0, curr_sum = 0, min_len = Infinity;

        for (let end = 0; end < n; end++) {
            curr_sum += arr[end];

            while (curr_sum > x) {
                min_len = Math.min(min_len, end - start + 1);
                curr_sum -= arr[start++];
            }
        }

        return min_len === Infinity ? 0 : min_len;
    }
}
```

---

Let me know if you’d like the unit test cases or to convert it to class-based structure for integration!
