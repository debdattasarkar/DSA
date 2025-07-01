The `bisect` module is a **powerful binary search utility** built into Python that helps you efficiently insert or find elements in **sorted arrays** — which is incredibly useful in many DSA problems.

---

## 🧠 What is the `bisect` module?

The `bisect` module provides functions for **binary searching** and **inserting** elements in a sorted list.

---

## 📚 Key Functions in `bisect`

### 1. `bisect_left(arr, x)`

Returns the index where `x` **should be inserted to keep the list sorted**, and **inserts before duplicates**.

### 2. `bisect_right(arr, x)`

Same as `bisect_left`, but **inserts after duplicates**.

### 3. `insort_left(arr, x)`

Inserts `x` at the correct position using `bisect_left`.

### 4. `insort_right(arr, x)`

Inserts `x` using `bisect_right`.

---

## ✅ Examples

```python
from bisect import bisect_left, bisect_right, insort

arr = [1, 3, 3, 5, 7]

print(bisect_left(arr, 3))   # Output: 1
print(bisect_right(arr, 3))  # Output: 3

insort(arr, 4)               # Insert 4 at the correct position
print(arr)                   # Output: [1, 3, 3, 4, 5, 7]
```

---

## 💡 Real DSA Problems That Use `bisect`

---

### 1. **Count of elements less than or equal to a given value**

**Problem**: For each element in `A`, count how many in `B` are ≤ `A[i]`.

🔧 Use:

```python
b.sort()
for a in A:
    count = bisect_right(b, a)
```
---


## ✅ Problem:

For each element in array **A**, count how many elements in array **B** are **less than or equal to it**.

---

### 🔍 Example:

**Input:**

```python
A = [4, 8, 1]
B = [1, 2, 5, 7]
```

**Explanation:**

* For `4` → B elements ≤ 4: `[1, 2]` → count = **2**
* For `8` → B elements ≤ 8: `[1, 2, 5, 7]` → count = **4**
* For `1` → B elements ≤ 1: `[1]` → count = **1**

**Output:**

```python
[2, 4, 1]
```

---

### ✅ Python Code:

```python
from bisect import bisect_right

A = [4, 8, 1]
B = [1, 2, 5, 7]

B.sort()  # Must be sorted for bisect to work

result = []
for a in A:
    count = bisect_right(B, a)
    result.append(count)

print(result)  # Output: [2, 4, 1]
```

---

### 2. **Longest Increasing Subsequence (LIS) - O(n log n)**

```python
from bisect import bisect_left

def LIS(nums):
    dp = []
    for x in nums:
        i = bisect_left(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)
```

---

### 3. **K-th Smallest Pair Distance**

**Binary Search + bisect** to count how many pairs have distance ≤ `mid`.

---

### 4. **Sliding Window Median (SortedList + bisect)**

Maintain a sorted list of size `k` and use `bisect.insort` and `bisect.bisect_left` to remove efficiently.

---

### 5. **Insert Interval / Merge Intervals**

Find where to insert the new interval using `bisect`.

---

## 🧠 Benefits in DSA

| Feature         | Benefit                                  |
| --------------- | ---------------------------------------- |
| O(log n) search | Much faster than linear scan             |
| Insert in-place | Helps maintain sorted arrays efficiently |
| Built-in        | No need to write your own binary search  |

---

## 📌 Import Reminder:

```python
from bisect import bisect_left, bisect_right, insort_left, insort_right
```

---