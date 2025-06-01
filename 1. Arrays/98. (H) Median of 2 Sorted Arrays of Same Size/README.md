Here's the **README** file content for the **"Median of 2 Sorted Arrays of Same Size"** problem:

---

# 📊 Median of 2 Sorted Arrays of Same Size

## 📝 Problem Statement

Given two sorted arrays `a[]` and `b[]` of equal size, the task is to find and return the **median** of the merged sorted array.

---

## 💡 Examples

### Example 1:

* **Input**:
  `a[] = [-5, 3, 6, 12, 15]`
  `b[] = [-12, -10, -6, -3, 4]`
* **Output**: `0`
* **Explanation**:
  Merged array = `[-12, -10, -6, -5, -3, 3, 4, 6, 12, 15]`
  Median = `(-3 + 3) / 2 = 0`

---

### Example 2:

* **Input**:
  `a[] = [2, 3, 5, 7]`
  `b[] = [10, 12, 14, 16]`
* **Output**: `8.5`
* **Explanation**:
  Merged array = `[2, 3, 5, 7, 10, 12, 14, 16]`
  Median = `(7 + 10) / 2 = 8.5`

---

### Example 3:

* **Input**:
  `a[] = [-5]`
  `b[] = [-6]`
* **Output**: `-5.5`
* **Explanation**:
  Merged array = `[-6, -5]`
  Median = `(-6 + -5) / 2 = -5.5`

---

## 📌 Constraints

* 1 ≤ `a.size()`, `b.size()` ≤ 10⁶
* -10⁶ ≤ `a[i]`, `b[i]` ≤ 10⁶

---

## ⏱️ Time and Space Complexity

* **Time Complexity**: `O(log n)`
* **Auxiliary Space**: `O(1)`

---

## 🏷️ Tags

`Binary Search`, `Arrays`

---

## 🏢 Company Tags

Amazon, Microsoft, Samsung, Google

---

## 📚 Related Articles

* [Median Of Two Sorted Arrays](https://www.geeksforgeeks.org/median-of-two-sorted-arrays/)

---

Here's a complete explanation of the **Median of 2 Sorted Arrays of Same Size** problem along with a step-by-step dry run and implementations in **Python**, **C++**, and **JavaScript**.

---

## 📘 Problem Overview

Given two sorted arrays `a[]` and `b[]` of the same size, find the **median** of the merged sorted array.

* The median is:

  * The middle element if the total number of elements is odd.
  * The average of the two middle elements if the total is even.

You are **not allowed to actually merge the arrays**; the goal is to do this in `O(log n)` time using binary search.

---

## 💡 Concept & Approach

We use **Binary Search** on the smaller array to partition both arrays into left and right halves such that:

* All elements in the left part are less than or equal to all elements in the right part.
* The total number of elements in the left and right parts are equal.

We maintain:

* `i` = partition of array `a`
* `j` = partition of array `b` = `(n + n + 1) // 2 - i`
  (ensures left halves together have one more or equal elements compared to right)

We adjust the partition based on conditions:

* If `a[i-1] > b[j]`, move `high = i - 1`
* Else, move `low = i + 1`

---

## 🧠 Dry Run

Let:

* `a = [2, 3, 5, 7]`, `b = [10, 12, 14, 16]`

### Step-by-Step:

* `n = 4`
* Try binary search on `a`.

Let’s try:

* `i = 2`, `j = 2`
  → `aLeft = 3`, `aRight = 5`
  → `bLeft = 12`, `bRight = 14`

Since `aLeft <= bRight` and `bLeft <= aRight`, it's a correct partition.

So, median = `(max(3,12) + min(5,14)) / 2 = (12 + 5) / 2 = 8.5`

---

## ✅ Python Code

```python
class Solution:
    def medianOf2(self, a, b):
        if len(a) > len(b):
            a, b = b, a  # Ensure a is the smaller array

        n = len(a)
        low, high = 0, n

        while low <= high:
            i = (low + high) // 2
            j = n - i

            aLeft = float('-inf') if i == 0 else a[i - 1]
            aRight = float('inf') if i == n else a[i]
            bLeft = float('-inf') if j == 0 else b[j - 1]
            bRight = float('inf') if j == n else b[j]

            if aLeft <= bRight and bLeft <= aRight:
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0
            elif aLeft > bRight:
                high = i - 1
            else:
                low = i + 1
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    double medianOf2(vector<int>& a, vector<int>& b) {
        if (a.size() > b.size())
            return medianOf2(b, a);

        int n = a.size();
        int low = 0, high = n;

        while (low <= high) {
            int i = (low + high) / 2;
            int j = n - i;

            int aLeft = (i == 0) ? INT_MIN : a[i - 1];
            int aRight = (i == n) ? INT_MAX : a[i];
            int bLeft = (j == 0) ? INT_MIN : b[j - 1];
            int bRight = (j == n) ? INT_MAX : b[j];

            if (aLeft <= bRight && bLeft <= aRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0;
            else if (aLeft > bRight)
                high = i - 1;
            else
                low = i + 1;
        }
        return 0.0; // fallback
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    medianOf2(a, b) {
        if (a.length > b.length) return this.medianOf2(b, a);

        let n = a.length;
        let low = 0, high = n;

        while (low <= high) {
            let i = Math.floor((low + high) / 2);
            let j = n - i;

            let aLeft = (i === 0) ? -Infinity : a[i - 1];
            let aRight = (i === n) ? Infinity : a[i];
            let bLeft = (j === 0) ? -Infinity : b[j - 1];
            let bRight = (j === n) ? Infinity : b[j];

            if (aLeft <= bRight && bLeft <= aRight)
                return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2;
            else if (aLeft > bRight)
                high = i - 1;
            else
                low = i + 1;
        }

        return 0;
    }
}
```

---

