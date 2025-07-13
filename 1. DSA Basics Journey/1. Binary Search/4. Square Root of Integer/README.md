The "Square Root of Integer" problem on **LeetCode** is:

---

## 🧩 **LeetCode 69: Sqrt(x)**

**🔗 Link:** [https://leetcode.com/problems/sqrtx](https://leetcode.com/problems/sqrtx)

### 📄 Problem Statement:

> Given a non-negative integer `x`, return the **integer part** of its square root.
> In other words, return ⌊ √x ⌋ (the floor of the square root).

* You must not use any built-in exponent functions like `pow` or `sqrt`.

Here is the extracted text from the image:

---

**Given a positive integer `n`, find its square root.**
If `n` is not a perfect square, then return **floor** of √n.

---

### Examples:

**Input:** `n = 4`
**Output:** `2`
**Explanation:** The square root of 4 is 2.

**Input:** `n = 11`
**Output:** `3`
**Explanation:** The square root of 11 lies in between 3 and 4, so the floor of the square root is 3.


---

## 🧠 Example

| Input | Output | Explanation             |
| ----- | ------ | ----------------------- |
| x = 4 | 2      | 2 \* 2 = 4              |
| x = 8 | 2      | 2 \* 2 = 4 < 8 < 3 \* 3 |

---

## ✅ Optimal Solution (Binary Search)

You’re searching for the **greatest integer `mid`** such that `mid * mid ≤ x`.

---

### ✅ Python Code with Inline Comments

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0) = 0, sqrt(1) = 1

        left, right = 1, x // 2  # We never need to search above x//2
        ans = 1

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                ans = mid      # store possible result
                left = mid + 1
            else:
                right = mid - 1

        return ans  # best floor value found
```

---

### 🧪 Test Cases

```python
assert Solution().mySqrt(0) == 0
assert Solution().mySqrt(1) == 1
assert Solution().mySqrt(4) == 2
assert Solution().mySqrt(8) == 2
assert Solution().mySqrt(16) == 4
assert Solution().mySqrt(100) == 10
```

---

### 🕐 Time and Space Complexity

* **Time Complexity:** `O(log x)`
* **Space Complexity:** `O(1)`

---

Here’s your full run of **LeetCode 69: Sqrt(x)** with:

### ✅ Execution Summary

* **Input:** `15`
* **Output:** `3` → because `3² = 9 ≤ 15` and `4² = 16 > 15`
* **Time:** `0.000005 seconds`

---

### 🔍 Step-by-Step Dry Run

```
Initial: left=1, right=7

Checking mid=4, square=16
→ 16 > 15 → move left → right = 3

Checking mid=2, square=4
→ 4 < 15 → move right → left = 3

Checking mid=3, square=9
→ 9 < 15 → move right → left = 4
```

Loop ends: `left=4 > right=3` → Best floor = `3`

---
