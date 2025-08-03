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

Here's a detailed comparison of the four provided solutions for **finding the second largest distinct element** in an array:

---

### ✅ **1. Optimal Single-Pass without Sorting or Extra Structures**

```python
def secondLargest(arr):
    if len(arr) < 2:
        return -1

    largest = second = -1

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second
```

**Pros**:

* ✅ Time Complexity: **O(n)**
* ✅ Space Complexity: **O(1)**
* ✅ No sorting, no extra memory
* ✅ Clean and direct logic
* ✅ Handles duplicates

**Cons**:

* ❌ Might be slightly less intuitive to beginners due to dual tracking

✅ **Recommended in interviews** for optimality and simplicity.

---

### ⚙️ **2. Sort-Based with `set()` for Uniqueness**

```python
class Solution:
    def getSecondLargest(self, n):
        n = list(set(n))  # Remove duplicates
        if len(n) < 2:
            return -1
        n.sort(reverse=True)
        return n[1]
```

**Pros**:

* ✅ Very **readable and short**
* ✅ Correct due to deduplication

**Cons**:

* ❌ Time Complexity: **O(n log n)** due to sorting
* ❌ Uses extra space for `set`

🔸 **Good for clarity**, but **not optimal**.

---

### 🔁 **3. Two-buffer Manual Tracking**

```python
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        buff = arr[:2]
        if buff[0] < buff[1]:
            buff[0], buff[1] = buff[1], buff[0]

        for i in range(2, len(arr)):
            if buff[0] == arr[i]:
                continue
            if buff[1] < arr[i]:
                buff[1] = arr[i]
                if buff[0] < buff[1]:
                    buff[0], buff[1] = buff[1], buff[0]

        return -1 if buff[0] == buff[1] else buff[1]
```

**Pros**:

* ✅ Works correctly
* ✅ Time Complexity: **O(n)**

**Cons**:

* ❌ Verbose
* ❌ Fragile on edge cases
* ❌ Less readable due to buffer manipulation

🟡 **Valid but not elegant or optimal**.

---

### 🧪 **4. Variation with Sorted Buffer**

```python
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1

        buff = arr[:2]
        buff.sort(reverse=True)

        for i in range(2, len(arr)):
            if buff[0] == arr[i]:
                continue
            if buff[1] < arr[i]:
                buff[1] = arr[i]
                buff.sort(reverse=True)

        return -1 if buff[1] == buff[0] else buff[1]
```

**Pros**:

* ✅ Works for many cases
* ✅ Logic is clear

**Cons**:

* ❌ Unnecessarily uses `sort()` inside loop ⇒ **O(n log k)** inefficiency
* ❌ Still depends on initial 2 elements without checks for uniqueness

🔸 **Readable but inefficient. Avoid using `sort()` repeatedly inside loop.**

---

### ✅ Final Verdict

| Version           | Time         | Space   | Clarity   | Optimal |
| ----------------- | ------------ | ------- | --------- | ------- |
| **1. Pure O(n)**  | ✅ O(n)       | ✅ O(1)  | ✅ Good    | ✅ Best  |
| **2. Set + Sort** | ❌ O(n log n) | ❌ Extra | ✅ Best    | ❌       |
| 3. Manual Buffer  | ✅ O(n)       | ✅ O(1)  | ❌ Verbose | ✅       |
| 4. Sort-in-Loop   | ❌ O(n log k) | ✅ O(1)  | ✅         | ❌       |

---

### ✅ Recommended: **First Approach** (`secondLargest` function)

Use it in interviews to showcase both performance and correctness.
