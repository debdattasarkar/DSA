
---

# 🔄 Rotate Array

### 🟡 Difficulty: Medium

**Accuracy:** 37.06%
**Submissions:** 527K+
**Points:** 4
**Average Time:** 20m

---

## 🔍 Problem Statement

Given an array `arr[]`, **rotate the array to the left** (counter-clockwise) by **d** steps, where `d` is a positive integer.
Do the rotation **in place**.

> 💡 Note: Consider the array as **circular**.

---

## 🧪 Examples

### Example 1:

**Input:**
`arr[] = [1, 2, 3, 4, 5]`, `d = 2`
**Output:**
`[3, 4, 5, 1, 2]`
**Explanation:**
After rotating by 2 steps to the left: `[3, 4, 5, 1, 2]`

---

### Example 2:

**Input:**
`arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`, `d = 3`
**Output:**
`[8, 10, 12, 14, 16, 18, 20, 2, 4, 6]`
**Explanation:**
Array after 3-step rotation: `[8, 10, 12, 14, 16, 18, 20, 2, 4, 6]`

---

### Example 3:

**Input:**
`arr[] = [7, 3, 9, 1]`, `d = 9`
**Output:**
`[3, 9, 1, 7]`
**Explanation:**
Since `d > n`, effective rotation = `d % n = 1`

---

## ✅ Constraints

* `1 ≤ arr.size(), d ≤ 10⁵`
* `0 ≤ arr[i] ≤ 10⁵`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 💼 Company Tags

`Amazon`, `Microsoft`, `MAQ Software`

---

## 🧠 Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* Array Rotation
* Complete Guide on Array Rotations
* Cpp Program For Array Rotation
* Java Program For Array Rotation

---

## 🧠 Text Explanation + Step-by-Step Dry Run

### Key Idea: Reverse-based Rotation (In-place, O(n) time and O(1) space)

**Steps:**

1. Reverse the first `d` elements.
2. Reverse the remaining `n - d` elements.
3. Reverse the whole array.

This gives a left rotation by `d`.

---

### Dry Run:

**Input:** `arr = [1, 2, 3, 4, 5]`, `d = 2`
→ `n = 5`

* Step 1: Reverse first `2` → `[2, 1, 3, 4, 5]`
* Step 2: Reverse remaining `3` → `[2, 1, 5, 4, 3]`
* Step 3: Reverse whole array → `[3, 4, 5, 1, 2]` ✅

---

## ✅ Optimized Code Implementations

---

### 🐍 Python

```python
# User function Template for python3

class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # In case d > n

        # Helper to reverse a subarray in-place
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse first d elements
        reverse(0, d - 1)

        # Step 2: Reverse rest of the array
        reverse(d, n - 1)

        # Step 3: Reverse the whole array
        reverse(0, n - 1)
```

```python
#User function Template for python3

class Solution:
    def hcf(self, a, b):
        # Recursive function to compute GCD (Euclidean algorithm)
        return a if b == 0 else self.hcf(b, a % b)  # Time: O(log min(a, b))

    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        """
        Rotate the array arr[] by d elements to the left using the Juggling algorithm.
        Time: O(n), Space: O(1)
        """
        n = len(arr)
        d = d % n  # Normalize d if it's >= n
        sets = self.hcf(n, d)

        for start in range(sets):
            curr = start
            temp = arr[curr]  # Store the first element in the current set

            while True:
                next_idx = (curr + d) % n

                if next_idx == start:
                    break

                arr[curr] = arr[next_idx]  # Move element from next_idx to curr
                curr = next_idx

            arr[curr] = temp  # Place temp in the final position of the cycle
        return arr
```

---

### 💠 C++

```cpp
class Solution {
  public:
    // Function to rotate an array by d elements in counter-clockwise direction.
    void rotateArr(vector<int>& arr, int d) {
        int n = arr.size();
        d = d % n; // handle d > n

        // Helper to reverse a range in-place
        auto reverse = [&](int start, int end) {
            while (start < end) {
                swap(arr[start], arr[end]);
                start++;
                end--;
            }
        };

        // Step 1: Reverse first d elements
        reverse(0, d - 1);

        // Step 2: Reverse the rest
        reverse(d, n - 1);

        // Step 3: Reverse the whole array
        reverse(0, n - 1);
    }
};
```

---

### 🌐 JavaScript

```javascript
// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} d
 */

class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    rotateArr(arr, d) {
        const n = arr.length;
        d = d % n; // handle d > n

        const reverse = (start, end) => {
            while (start < end) {
                [arr[start], arr[end]] = [arr[end], arr[start]];
                start++;
                end--;
            }
        };

        // Step 1: Reverse first d elements
        reverse(0, d - 1);

        // Step 2: Reverse the rest
        reverse(d, n - 1);

        // Step 3: Reverse entire array
        reverse(0, n - 1);
    }
}
```

---

## 💬 Interview Questions & Answers

---

### ❓Q1: Why use the reverse-based approach?

**A:** It achieves in-place rotation in O(n) time and O(1) space. It's optimal for large arrays without extra memory.

---

### ❓Q2: What happens if d > n?

**A:** Rotation is cyclic, so we reduce `d = d % n`.

---

### ❓Q3: Can you use slicing or temporary arrays?

**A:** You can, but that would use O(n) extra space — not allowed if the problem demands in-place modification.

---

### ❓Q4: What if array size is 1?

**A:** No rotation needed. Code handles it as `d % n = 0`.

---

### ❓Q5: Is there a right-rotation version?

**A:** Yes, right rotation by `k` can be done with similar logic:

* Reverse last `k`
* Reverse first `n-k`
* Reverse whole array

---
