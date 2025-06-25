Here is the complete README-style conversion for the problem **Second Largest** based on the provided image:

---

# 🥈 Second Largest

**Difficulty:** Easy
**Accuracy:** 26.72%
**Submissions:** 1.1M+
**Points:** 2
**Average Time:** 15m

---

## 🧩 Problem Statement

Given an array of **positive** integers `arr[]`, return the **second largest** element from the array. If the second largest element doesn't exist, then return **-1**.

📌 **Note:** The second largest element should **not be equal** to the largest element.

---

## 🧪 Examples

### Example 1:

```
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
```

### Example 2:

```
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
```

### Example 3:

```
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
```

---

## 📌 Constraints

```
1 ≤ arr.size() ≤ 10⁵
1 ≤ arr[i] ≤ 10⁵
```

---

## 📈 Expected Time Complexity

* Time: **O(n)**
* Auxiliary Space: **O(1)**

---

## 🏷️ Tags

* Arrays
* Sorting
* Interview Preparation

---

Sure! Here's the full breakdown:

---

## ✅ Problem: Second Largest Element

You are given an array `arr[]` of **positive integers**. Your task is to return the **second largest** element from the array.

* If the second largest element doesn’t exist (i.e., all elements are the same), return **-1**.
* Second largest must be **strictly less than** the largest, and must exist in the array.

---

## 🔍 Step-by-Step Explanation + Dry Run

**Approach: One Pass (O(n) Time, O(1) Space)**

### Dry Run Example:

Input: `arr = [12, 35, 1, 10, 34, 1]`

We initialize:

* `first = -1` (to track max)
* `second = -1` (to track second max)

Now traverse:

| i | arr\[i] | first | second | Reason                         |
| - | ------- | ----- | ------ | ------------------------------ |
| 0 | 12      | 12    | -1     | New max found                  |
| 1 | 35      | 35    | 12     | New max found                  |
| 2 | 1       | 35    | 12     | Smaller than both              |
| 3 | 10      | 35    | 12     | Smaller than both              |
| 4 | 34      | 35    | 34     | Between 35 and previous second |
| 5 | 1       | 35    | 34     | Ignored                        |

✅ Result: **34**

---

## ✅ Python Code

```python
class Solution:
    def getSecondLargest(self, arr):
        first = second = -1
        
        for num in arr:
            if num > first:
                second = first  # demote the old max
                first = num
            elif num != first and num > second:
                second = num  # update only if different from max
        
        return second
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int getSecondLargest(vector<int> &arr) {
        int first = -1, second = -1;
        
        for (int num : arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num != first && num > second) {
                second = num;
            }
        }
        
        return second;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    getSecondLargest(arr) {
        let first = -1, second = -1;
        
        for (let num of arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num !== first && num > second) {
                second = num;
            }
        }
        
        return second;
    }
}
```

---

## 💬 Interview Questions and Answers

### Q1. What if all elements are the same?

**A:** Then return `-1`, as second largest does not exist.

### Q2. Can you solve it in O(n) time and O(1) space?

**A:** Yes. We use two variables (`first` and `second`) and one loop.

### Q3. What edge cases did you handle?

**A:**

* All elements same → return `-1`
* Only one element → no second → `-1`
* Multiple max values → skip duplicates

### Q4. Why is sorting not preferred here?

**A:** Sorting is O(n log n). We can find the second largest in a single pass using O(n) time and O(1) space.

---
