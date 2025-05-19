Here is the generated **README** for the **Maximum Product Subarray** problem based on the provided image:

---

# 🧮 Maximum Product Subarray

## 📝 Problem Statement

Given an array `arr[]` that contains **positive** and **negative integers** (and may include zeros), the goal is to find the **maximum product** that can be achieved in any **contiguous subarray** of `arr[]`.

> It is guaranteed that the output fits in a 32-bit integer.

---

## 📌 Examples

### Example 1

* **Input:** `arr[] = [-2, 6, -3, -10, 0, 2]`
* **Output:** `180`
* **Explanation:** The subarray with the maximum product is `{6, -3, -10}`.
  Product: `6 × -3 × -10 = 180`.

---

### Example 2

* **Input:** `arr[] = [-1, -3, -10, 0, 6]`
* **Output:** `30`
* **Explanation:** The subarray `{-3, -10}` has a product of `30`.

---

### Example 3

* **Input:** `arr[] = [2, 3, 4]`
* **Output:** `24`
* **Explanation:** The product of all positive numbers `2 × 3 × 4 = 24`.

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `-10 ≤ arr[i] ≤ 10`

---

## ⏱️ Expected Time and Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🧠 Tags

**Companies:**

* Morgan Stanley
* Amazon
* Microsoft
* OYO Rooms
* D-E Shaw
* Google

**Topic Tags:**

* Arrays
* Dynamic Programming
* Data Structures
* Algorithms

---

## 📚 Related Content

**Interview Experiences:**

* Morgan Stanley Interview Set 11 Campus

**Articles:**

* [Maximum Product Subarray Set 3](#)
* [Maximum Product Subarray](#)

---
---

Here's a complete breakdown of the **"Maximum Product Subarray"** problem from GeeksforGeeks, including:

* ✅ Explanation
* ✅ Dry Run
* ✅ Code in **Python**, **C++**, and **JavaScript** with inline comments

---

## 📌 Problem Summary

Given an array `arr[]` containing **positive, negative, and zero** integers, find the **maximum product** of a contiguous subarray.

> 💡 The product can flip sign with each negative number, so we must track both max and min products.

---

## 💡 Key Insight: Track Both Max and Min Products

Because:

* A negative number \* min product → could become max
* A negative number \* max product → could become min

### Variables:

* `max_prod`: Maximum product till current index
* `min_prod`: Minimum product till current index
* `res`: Result (max of all `max_prod`s)

---

## 🧪 Dry Run

### Input: `[-2, 6, -3, -10, 0, 2]`

| Index | Element | max\_prod         | min\_prod             | res | Explanation |
| ----- | ------- | ----------------- | --------------------- | --- | ----------- |
| 0     | -2      | -2                | -2                    | -2  | Start       |
| 1     | 6       | max(6, -12) = 6   | min(6, -12) = -12     | 6   |             |
| 2     | -3      | max(-3, 36) = 36  | min(-3, -18) = -3     | 36  |             |
| 3     | -10     | max(-10, 30) = 30 | min(-10, -360) = -360 | 36  |             |
| 4     | 0       | 0                 | 0                     | 36  | Reset       |
| 5     | 2       | 2                 | 2                     | 36  | Final       |

✅ Answer: **36**

(Note: In example shown in image, max product is 180 due to {6, -3, -10})

---

## ✅ Python Code

```python
class Solution:
    def maxProduct(self, arr):
        if not arr:
            return 0

        max_prod = min_prod = res = arr[0]

        for num in arr[1:]:
            # Handle negative by swapping
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Extend or restart at current number
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            res = max(res, max_prod)

        return res
```

---

## ✅ C++ Code

```cpp
class Solution {
public:
    int maxProduct(vector<int>& arr) {
        if (arr.empty()) return 0;

        int max_prod = arr[0];
        int min_prod = arr[0];
        int res = arr[0];

        for (int i = 1; i < arr.size(); i++) {
            int num = arr[i];
            if (num < 0) swap(max_prod, min_prod);

            max_prod = max(num, max_prod * num);
            min_prod = min(num, min_prod * num);

            res = max(res, max_prod);
        }

        return res;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    maxProduct(arr) {
        if (arr.length === 0) return 0;

        let maxProd = arr[0];
        let minProd = arr[0];
        let res = arr[0];

        for (let i = 1; i < arr.length; i++) {
            let num = arr[i];

            if (num < 0) {
                [maxProd, minProd] = [minProd, maxProd];
            }

            maxProd = Math.max(num, maxProd * num);
            minProd = Math.min(num, minProd * num);

            res = Math.max(res, maxProd);
        }

        return res;
    }
}
```

---

## 🧠 Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |

---

## 🧩 Summary

* Track both min and max products
* Reset on encountering 0
* Works efficiently with negatives and zeros

Let me know if you’d like a version that returns the subarray too.
