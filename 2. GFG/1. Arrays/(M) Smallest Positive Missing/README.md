

---

# 📘 Problem: Smallest Positive Missing

**Difficulty**: Medium
**Accuracy**: 25.13%
**Submissions**: 436K+
**Points**: 4

---

## 📝 Problem Statement

You are given an integer array `arr[]`. Your task is to find the **smallest positive number** that is **missing** from the array.

> **Note**:
>
> * Positive numbers start from **1**.
> * The array can contain **negative integers** as well.

---

## 💡 Examples

### Example 1:

**Input**: `arr[] = [2, -3, 4, 1, 1, 7]`
**Output**: `3`
**Explanation**: Smallest positive missing number is `3`.

---

### Example 2:

**Input**: `arr[] = [5, 3, 2, 5, 1]`
**Output**: `4`
**Explanation**: Smallest positive missing number is `4`.

---

### Example 3:

**Input**: `arr[] = [-8, 0, -1, -4, -3]`
**Output**: `1`
**Explanation**: There is no positive number, so the smallest missing is `1`.

---

## ✅ Constraints

* `1 ≤ arr.size() ≤ 10⁵`
* `-10⁶ < arr[i] < 10⁶`

---

## 🔍 Expected Complexities

* **Time Complexity**: `O(n)`
* **Auxiliary Space**: `O(1)`

---

## 🏷️ Topic Tags

* Arrays
* Searching
* Data Structures
* Algorithms

---

## 🏢 Company Tags

* Accolite
* Amazon
* Samsung
* Snapdeal

---

## 📚 Related Interview Experiences

* Amazon Interview Experience Set 264 – Experienced for SDE1
* Samsung Interview Experience Set 21 – Campus
* Snapdeal Interview Experience Set 17 – SDET
* Amazon Interview Experience 220 – On Campus
* Accolite Interview Experience Set 4 – On Campus

---

## 📖 Related Articles

* [Find The Smallest Positive Number Missing From An Unsorted Array](https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/)

---

---

Sure! Let’s go step by step for the **“Smallest Positive Missing Number”** problem.

---

## 📘 Problem Recap

You're given an array `arr[]` that may contain negative and positive integers. Your task is to find the **smallest positive integer (≥1)** that is **not present** in the array.

---

## 🔍 Text Explanation with Step-by-Step Dry Run

### 🎯 Goal:

Find the **smallest positive integer (starting from 1)** missing from the array in **O(n)** time and **O(1)** space.

---

### 🔧 Optimized Approach: Index Mapping / In-Place Hashing

* Ignore values ≤ 0 and values > n (where n = len(arr)) as they can't be answers.
* Mark the presence of a number by setting `arr[val-1]` to `-abs(arr[val-1])` if possible.
* Then, the first index with a positive number means the missing number is `index + 1`.

---

### 🧪 Dry Run

#### Input:

`arr = [3, 4, -1, 1]`

#### Step 1: Clean non-useful numbers

Only focus on range `1` to `n`, so ignore negatives and values > 4.

→ `[3, 4, -1, 1]` stays as is.

#### Step 2: Mark presence

* 3 → mark index 2 → `arr = [3, 4, -1, -1]`
* 4 → mark index 3 → `arr = [3, 4, -1, -1]`
* -1 → ignore
* 1 → mark index 0 → `arr = [-3, 4, -1, -1]`

Final: `arr = [-3, 4, -1, -1]`

#### Step 3: First positive index = 1 → missing = `1+1 = 2`

✅ **Output: 2**

---

## ✅ Optimized Python Code (Expected in Interviews)

```python
import time

class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Replace non-positive and >n numbers with a placeholder
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1  # ignore these numbers

        # Step 2: Mark the presence
        for i in range(n):
            num = abs(arr[i])
            if 1 <= num <= n:
                if arr[num - 1] > 0:
                    arr[num - 1] = -arr[num - 1]

        # Step 3: First missing index
        for i in range(n):
            if arr[i] > 0:
                return i + 1  # index+1 is missing

        return n + 1  # if all 1..n are present

# ---------- Main Program with Time Test ----------

if __name__ == "__main__":
    arr = [2, -3, 4, 1, 1, 7]
    start = time.time()
    sol = Solution()
    result = sol.missingNumber(arr.copy())  # Pass a copy if you need original array
    end = time.time()

    print("Input:", arr)
    print("Smallest missing positive number:", result)
    print("Execution Time: {:.6f} seconds".format(end - start))
```

---

## ⏱ Time and Space Complexity

| Step                | Time     | Space    |
| ------------------- | -------- | -------- |
| Input cleaning      | O(n)     | O(1)     |
| In-place marking    | O(n)     | O(1)     |
| Scanning for result | O(n)     | O(1)     |
| **Total**           | **O(n)** | **O(1)** |

---

## 🧪 Brute Force Version (Not preferred in interviews)

```python
class Solution:
    def missingNumber(self, arr):
        s = set(arr)
        i = 1
        while True:
            if i not in s:
                return i
            i += 1
```

* **Time**: O(n)
* **Space**: O(n)
* **Use**: Good for explanation or Pythonic solutions, not optimal for large n.

---

## 💬 Interviewer Q\&A

### ❓ Q1: Why do we use `arr[val-1] = -abs(...)` instead of `-1`?

**A**: To mark presence *while preserving information*. `-abs()` ensures idempotent marking.

---

### ❓ Q2: Why replace values ≤0 or >n with `n+1`?

**A**: We’re only interested in 1 to n. Values outside this range can't be the smallest missing positive.

---

### ❓ Q3: Can this be done without modifying the original array?

**A**: Yes, but you'll need O(n) extra space (set, hash, etc). This violates the space constraint.

---

### ❓ Q4: What if all numbers from 1 to n exist?

**A**: The answer must be `n+1`, the smallest number beyond the range.

---

### ❓ Q5: Can we use counting sort or sorting?

**A**: Sorting would take O(n log n), which is not optimal. This violates the required O(n) time.

---

## 🌍 Real-World Use Cases

* **Database ID management**: Finding smallest unused ID.
* **Task Queues**: Scheduling smallest unassigned task index.
* **Memory/Page Allocation**: Determining first unallocated block/index.
* **Test Case/Slot Management**: Fill the first available number.
* **Game Mechanics**: Allocating first missing position/unit in sequence.

---
