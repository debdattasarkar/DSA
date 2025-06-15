Here is the full **README-style explanation** with a **step-by-step dry run** and optimal **in-place solution** for **Leetcode 189 – Rotate Array**, in **Python, C++, and JavaScript** formats.

---

# 🔄 Rotate Array (Leetcode #189)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Math`, `Two Pointers`

---

## 📘 Problem Statement

Given an integer array `nums`, rotate the array to the **right by `k` steps**, where `k` is non-negative.

You must **modify the array in-place**, with **O(1)** extra space.

---

## 🧪 Examples

### Example 1:

```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Steps:**

* Rotate 1 step → \[7,1,2,3,4,5,6]
* Rotate 2 steps → \[6,7,1,2,3,4,5]
* Rotate 3 steps → \[5,6,7,1,2,3,4]

---

### Example 2:

```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

---

## ⚙️ Constraints

* `1 <= nums.length <= 10⁵`
* `-2³¹ <= nums[i] <= 2³¹ - 1`
* `0 <= k <= 10⁵`

---

## 💡 Approach: Reverse Parts of the Array

To rotate right by `k`:

1. **Normalize** `k = k % len(nums)` to handle large `k`.
2. **Reverse the entire array**.
3. **Reverse the first `k` elements**.
4. **Reverse the remaining `n-k` elements**.

---

## 📊 Dry Run

**Input:** `nums = [1,2,3,4,5,6,7]`, `k = 3`

| Step                         | Result             |
| ---------------------------- | ------------------ |
| Reverse full array           | \[7,6,5,4,3,2,1]   |
| Reverse first `k=3` elements | \[5,6,7,4,3,2,1]   |
| Reverse rest (`n-k=4`)       | \[5,6,7,1,2,3,4] ✅ |

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Normalize k

        # Helper function to reverse elements in-place
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse entire array
        reverse(0, n - 1)
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the rest
        reverse(k, n - 1)
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n; // Normalize k

        // Helper lambda to reverse subarray
        auto reverse = [&](int start, int end) {
            while (start < end) {
                swap(nums[start++], nums[end--]);
            }
        };

        reverse(0, n - 1);     // Reverse entire array
        reverse(0, k - 1);     // Reverse first k elements
        reverse(k, n - 1);     // Reverse remaining
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const n = nums.length;
    k %= n; // Normalize k

    const reverse = (start, end) => {
        while (start < end) {
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++;
            end--;
        }
    };

    reverse(0, n - 1);     // Reverse entire array
    reverse(0, k - 1);     // Reverse first k elements
    reverse(k, n - 1);     // Reverse the rest
};
```

---

## ✅ Summary

| Metric           | Value                 |
| ---------------- | --------------------- |
| Time Complexity  | `O(n)`                |
| Space Complexity | `O(1)`                |
| In-place?        | ✅ Yes                 |
| Reversal-based?  | ✅ Best for constraint |

---

Great choice! The **Cyclic Replacement** method (also called **GCD-based rotation**) is a clever, in-place `O(n)` time solution to rotate an array without using extra memory.

---

# 🔁 Cyclic Replacement (GCD-based) – Rotate Array

### 💡 Idea:

We rotate elements in **cycles**, using the **GCD (Greatest Common Divisor)** of `n` and `k` to determine how many independent cycles we need.

---

## 📘 Concept:

To rotate an array `nums` of length `n` by `k` steps to the right:

* Normalize `k = k % n`
* There are `g = gcd(n, k)` cycles.
* In each cycle, we move elements `k` steps forward until we come back to the starting point.

This ensures each element is moved **once**.

---

## 📊 Dry Run

**Input:** `nums = [1,2,3,4,5,6]`, `k = 2`

* `n = 6`, `gcd(6,2) = 2` → 2 cycles

**Cycle 1 (start at index 0):**

```
0 → 2 → 4 → 0
[1→3, 3→5, 5→1] → nums = [5,2,1,4,3,6]
```

**Cycle 2 (start at index 1):**

```
1 → 3 → 5 → 1
[2→4, 4→6, 6→2] → nums = [5,6,1,2,3,4]
```

✅ Final: `[5,6,1,2,3,4]`

---

## 🧠 Why GCD?

* We move each element to `(i + k) % n`
* If you keep rotating one element, you'll eventually return to the starting index
* The number of **distinct cycles** is `gcd(n, k)`

---

## 🐍 Python Code (Cyclic Replacement)

```python
from typing import List
from math import gcd

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        g = gcd(n, k)

        for start in range(g):
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                if start == current:
                    break
```

---

## 💠 C++ Code (Cyclic Replacement)

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        int g = gcd(n, k);

        for (int start = 0; start < g; ++start) {
            int current = start;
            int prev = nums[start];

            do {
                int next = (current + k) % n;
                swap(nums[next], prev);
                current = next;
            } while (start != current);
        }
    }
};
```

---

## 🌐 JavaScript Code (Cyclic Replacement)

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void}
 */
var rotate = function(nums, k) {
    const n = nums.length;
    k %= n;

    const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);

    const g = gcd(n, k);

    for (let start = 0; start < g; start++) {
        let current = start;
        let prev = nums[start];

        do {
            const next = (current + k) % n;
            [nums[next], prev] = [prev, nums[next]];
            current = next;
        } while (start !== current);
    }
};
```

---

## ✅ Summary

| Feature          | Description                         |
| ---------------- | ----------------------------------- |
| Time Complexity  | `O(n)` (every element moved once)   |
| Space Complexity | `O(1)` (in-place)                   |
| Best for         | Interview, low-level rotation logic |
| Insight          | Uses **GCD** to track cycles        |

---

Absolutely! Let's now walk through the **brute force** and **auxiliary array** versions of the **Rotate Array (Leetcode #189)** problem.

These versions are **not in-place**, but they are intuitive and good for understanding the core idea before optimizing.

---

# 🐢 Brute Force / Auxiliary Array Approach

---

## 💡 Idea

Create a new array `result` of the same size, and for each index `i` in the original array:

* Place `nums[i]` at index `(i + k) % n` in the result.

Then copy `result` back to `nums` (if required in-place).

---

## 📊 Dry Run

**Input:**

```text
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
```

**Steps:**

| i | nums\[i] | New index `(i + k) % n` | result                       |
| - | -------- | ----------------------- | ---------------------------- |
| 0 | 1        | (0+3)%7 = 3             | \[\_, \_, \_, 1, \_, \_, \_] |
| 1 | 2        | 4                       | \[\_, \_, \_, 1, 2, \_, \_]  |
| 2 | 3        | 5                       | \[\_, \_, \_, 1, 2, 3, \_]   |
| 3 | 4        | 6                       | \[\_, \_, \_, 1, 2, 3, 4]    |
| 4 | 5        | 0                       | \[5, \_, \_, 1, 2, 3, 4]     |
| 5 | 6        | 1                       | \[5, 6, \_, 1, 2, 3, 4]      |
| 6 | 7        | 2                       | \[5, 6, 7, 1, 2, 3, 4] ✅     |

---

## 🐍 Python Code (Auxiliary Array)

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        result = [0] * n

        for i in range(n):
            result[(i + k) % n] = nums[i]

        # Copy back to original array
        for i in range(n):
            nums[i] = result[i]
```

---

## 💠 C++ Code (Auxiliary Array)

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            result[(i + k) % n] = nums[i];
        }

        // Copy back to original
        for (int i = 0; i < n; i++) {
            nums[i] = result[i];
        }
    }
};
```

---

## 🌐 JavaScript Code (Auxiliary Array)

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void}
 */
var rotate = function(nums, k) {
    const n = nums.length;
    k %= n;

    const result = new Array(n);

    for (let i = 0; i < n; i++) {
        result[(i + k) % n] = nums[i];
    }

    for (let i = 0; i < n; i++) {
        nums[i] = result[i];  // copy back
    }
};
```

---

## ✅ Summary

| Feature            | Description               |
| ------------------ | ------------------------- |
| Time Complexity    | `O(n)`                    |
| Space Complexity   | `O(n)` — uses extra array |
| In-place?          | ❌ No                      |
| Easy to Implement? | ✅ Very beginner-friendly  |

---

Would you like a visual comparison of all 3 methods (reversal, cyclic, brute force)? Or an interview-focused recap sheet?

✅ Let's go with both: a **Visual Comparison Table** + an **Interview-Focused Recap Sheet** for **Leetcode 189 – Rotate Array**.

---

# 📊 Visual Comparison of All 3 Rotation Methods

| Feature              | 🔁 Reversal Method          | 🔄 Cyclic Replacement       | 🐢 Brute Force / Aux Array    |
| -------------------- | --------------------------- | --------------------------- | ----------------------------- |
| **Idea**             | Reverse full + parts        | Move elements in cycles     | Place in new array, copy back |
| **Time Complexity**  | `O(n)`                      | `O(n)`                      | `O(n)`                        |
| **Space Complexity** | `O(1)` (in-place)           | `O(1)` (in-place)           | `O(n)` (uses extra array)     |
| **Stable?**          | No (doesn’t preserve order) | Yes                         | Yes                           |
| **Ease of Coding**   | Easy                        | Medium (requires GCD logic) | Very Easy                     |
| **Mutates Original** | ✅ Yes                       | ✅ Yes                       | ✅ Yes                         |
| **Use Case**         | Fast & in-place rotation    | In-place & advanced         | Educational / fallback method |

---

# 💼 Interview Recap Sheet: Rotate Array

### 🔹 Problem:

> Rotate an array `nums` of length `n` to the right by `k` steps in-place.

---

### ✅ Solutions Overview

#### 1. **Reverse Method** – Best Tradeoff

```python
# reverse(nums)
# reverse(nums[0:k])
# reverse(nums[k:n])
```

* Time: `O(n)`
* Space: `O(1)`
* Most used in interviews due to simplicity + performance.

---

#### 2. **Cyclic Replacement** – Advanced In-place

```python
# For gcd(n, k) cycles
# Move elements by (i + k) % n
```

* Time: `O(n)`
* Space: `O(1)`
* Use when interviewers expect deep array knowledge or GCD logic.

---

#### 3. **Brute Force / Extra Array** – Teaching Tool

```python
# Place nums[i] at (i + k) % n in new array
# Copy back to nums
```

* Time: `O(n)`
* Space: `O(n)`
* Simple to code but fails in strict "O(1) space" constraints.

---

### 🔹 Edge Case Handling

* Normalize: `k %= n` to handle large rotations
* Small array? Use brute force for clarity.
* For optimal: Go with **Reverse** unless interviewer asks for “do it without reverse”.

---

### 🧠 Interview Tips

* Mention **three** approaches quickly.
* Code the **reversal method** unless otherwise requested.
* For `follow-up: O(1) space?`, immediately shift to **reversal or cyclic**.
* Be ready to explain **GCD-based cycles** if prompted for in-place alternatives.

---
