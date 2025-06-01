# Bits Counting

## 🧩 Problem Statement

Given an integer `n`, return an array `ans` of size `n + 1`, where each element `i` (0 ≤ i ≤ n) represents the **count of `1`s** in the **binary representation** of `i`.

---

## 🧪 Examples

### Example 1:

**Input:**
`n = 2`
**Output:**
`[0, 1, 1]`
**Explanation:**

```
0 ->  0  → 0 ones  
1 ->  1  → 1 one  
2 -> 10  → 1 one  
```

---

### Example 2:

**Input:**
`n = 5`
**Output:**
`[0, 1, 1, 2, 1, 2]`
**Explanation:**

```
0 ->  0    → 0 ones  
1 ->  1    → 1 one  
2 ->  10   → 1 one  
3 ->  11   → 2 ones  
4 ->  100  → 1 one  
5 ->  101  → 2 ones  
```

---

## 🔍 Constraints

* $0 \leq n \leq 10^5$

---

## ⏱️ Expected Time and Space Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🧠 Approach

This problem is commonly solved using **dynamic programming** with the observation:

```
bits[i] = bits[i >> 1] + (i & 1)
```

Explanation:

* `i >> 1` is `i` divided by 2 (dropping the least significant bit)
* `i & 1` is `1` if `i` is odd (i.e., last bit is 1), `0` otherwise

We use the results of previous calculations to compute the next, avoiding recomputation.

---

## 🚀 Code Implementation

### ✅ Python

```python
class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
```

---

### ✅ C++

```cpp
class Solution {
  public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
};
```

---

### ✅ JavaScript

```javascript
class Solution {
    countBits(n) {
        let ans = new Array(n + 1).fill(0);
        for (let i = 1; i <= n; i++) {
            ans[i] = ans[Math.floor(i / 2)] + (i & 1);
        }
        return ans;
    }
}
```

---

## 🏷️ Tags

`Bit Magic`, `Dynamic Programming`, `Arrays`

---

## 💼 Company Tags

`Bloomberg`, `Facebook`, `Adobe`, `Google`, `Amazon`, `Microsoft`, `Apple`, `Yahoo`, `Nvidia`, `Uber`

---

Here's a complete explanation with a step-by-step dry run and code implementations for **"Bits Counting"**:

---

## 🧠 Text Explanation

The task is to return a list `ans` where `ans[i]` is the number of `1`s in the binary representation of `i` for all `0 <= i <= n`.

### Key Insight:

Use **dynamic programming** with the relation:

```
countBits[i] = countBits[i >> 1] + (i & 1)
```

* `i >> 1`: Equivalent to dividing `i` by 2 (dropping the least significant bit).
* `i & 1`: Checks if the least significant bit is 1 (i.e., `i` is odd).

---

## 🧪 Step-by-Step Dry Run

For `n = 5`:

| i | Binary | i >> 1 | i & 1 | countBits\[i >> 1] | countBits\[i] |
| - | ------ | ------ | ----- | ------------------ | ------------- |
| 0 | 000    | -      | 0     | -                  | 0             |
| 1 | 001    | 0      | 1     | 0                  | 1             |
| 2 | 010    | 1      | 0     | 1                  | 1             |
| 3 | 011    | 1      | 1     | 1                  | 2             |
| 4 | 100    | 2      | 0     | 1                  | 1             |
| 5 | 101    | 2      | 1     | 1                  | 2             |

Final Output: `[0, 1, 1, 2, 1, 2]`

---

## ✅ Python Code (With Inline Comments)

```python
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize result list with zeros
        res = [0] * (n + 1)
        
        # Start from 1 to n
        for i in range(1, n + 1):
            # Use the relation: res[i] = res[i >> 1] + (i & 1)
            res[i] = res[i >> 1] + (i & 1)
        
        return res
```

---

## ✅ C++ Code (With Inline Comments)

```cpp
class Solution {
  public:
    vector<int> countBits(int n) {
        vector<int> res(n + 1, 0);
        
        for (int i = 1; i <= n; i++) {
            // Count bits using previous result
            res[i] = res[i >> 1] + (i & 1);
        }
        
        return res;
    }
};
```

---

## ✅ JavaScript Code (With Inline Comments)

```javascript
class Solution {
    /**
     * @param {number} n
     * @returns {number[]}
     */
    countBits(n) {
        let res = new Array(n + 1).fill(0);

        for (let i = 1; i <= n; i++) {
            // Fill result using previous values
            res[i] = res[i >> 1] + (i & 1);
        }

        return res;
    }
}
```

---

## 🔚 Summary

This problem demonstrates efficient bit manipulation combined with dynamic programming for calculating the number of set bits (`1`s) for all numbers from `0` to `n` in **O(n)** time.

Let me know if you'd like a version using bitwise tricks only or for interview preparation formats.
