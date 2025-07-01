# 🥸 1. Bisect Module

The `bisect` module is a **powerful binary search utility** built into Python that helps you efficiently insert or find elements in **sorted arrays** — which is incredibly useful in many DSA problems.

---

## 🧠 What is the `bisect` module?

The `bisect` module provides functions for **binary searching** and **inserting** elements in a sorted list.

---

## 📚 Key Functions in `bisect`

Let’s break this down **with intuitive examples** and visuals so it’s crystal clear how `bisect` functions behave and **when to use them**.

---

## ✅ Imagine You Have a Sorted List:

```python
arr = [10, 20, 20, 30]
```

Let’s say you want to **insert `20`** and keep the list sorted.

---

## 🔍 1. `bisect_left(arr, x)`

> Finds **first position** where `x` can be inserted.
> If `x` already exists, it goes **before the first occurrence**.

```python
from bisect import bisect_left
index = bisect_left([10, 20, 20, 30], 20)
print(index)  # Output: 1
```

📌 Result:

* Insert 20 at index 1 (before both 20s)

📦 New list (if you inserted manually):
`[10, 20, 20, 20, 30]`

---

## 🔍 2. `bisect_right(arr, x)`

> Finds **last position** where `x` can be inserted.
> If `x` exists, it goes **after the last occurrence**.

```python
from bisect import bisect_right
index = bisect_right([10, 20, 20, 30], 20)
print(index)  # Output: 3
```

📌 Result:

* Insert 20 at index 3 (after all 20s)

📦 New list:
`[10, 20, 20, 20, 30]`

---

## ⚒️ Summary So Far:

| Function       | Inserts `20` at index | Goes before/after duplicates |
| -------------- | --------------------- | ---------------------------- |
| `bisect_left`  | 1                     | **Before** duplicates        |
| `bisect_right` | 3                     | **After** duplicates         |

---

## 🔧 3. `insort_left(arr, x)`

> Inserts `x` **in-place** using `bisect_left`.

```python
from bisect import insort_left

arr = [10, 20, 20, 30]
insort_left(arr, 20)
print(arr)  # Output: [10, 20, 20, 20, 30]
```

✅ Internally uses `bisect_left` to find where to insert.

---

## 🔧 4. `insort_right(arr, x)`

> Inserts `x` **in-place** using `bisect_right`.

```python
from bisect import insort_right

arr = [10, 20, 20, 30]
insort_right(arr, 20)
print(arr)  # Output: [10, 20, 20, 20, 30]
```

✅ Internally uses `bisect_right` for the position.

---

## 🚀 Visual Comparison

```text
arr = [10, 20, 20, 30]
           ↑     ↑
        left=1  right=3
```

| Use Case                 | Method         | Result Position |
| ------------------------ | -------------- | --------------- |
| Insert before duplicates | `bisect_left`  | Index 1         |
| Insert after duplicates  | `bisect_right` | Index 3         |
| Insert in-place (left)   | `insort_left`  | Index 1         |
| Insert in-place (right)  | `insort_right` | Index 3         |

---

## 🧠 When to Use What?

* Use **`bisect_left`** to find:

  * How many elements are **< x**
  * First position for duplicates

* Use **`bisect_right`** to find:

  * How many elements are **≤ x**
  * Last position for duplicates

* Use **`insort_*`** when you want to **insert while maintaining order**

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
A **step-by-step input/output example** for the **Longest Increasing Subsequence (LIS)** function using `bisect_left`.

---

## ✅ Problem:

Find the **length** of the **Longest Increasing Subsequence** in a list of numbers.

---

### 🔍 Example Input:

```python
nums = [10, 9, 2, 5, 3, 7, 101, 18]
```

---

### ✅ Output:

```
4
```

---

### 🧠 Explanation (LIS steps):

We are building a `dp[]` array such that:

* `dp[i]` stores the **smallest possible tail value** of an increasing subsequence of length `i + 1`.

**Dry Run:**

| num | dp (after processing)        |
| --- | ---------------------------- |
| 10  | \[10]                        |
| 9   | \[9] (replace 10 with 9)     |
| 2   | \[2] (replace 9 with 2)      |
| 5   | \[2, 5]                      |
| 3   | \[2, 3] (replace 5 with 3)   |
| 7   | \[2, 3, 7]                   |
| 101 | \[2, 3, 7, 101]              |
| 18  | \[2, 3, 7, 18] (replace 101) |

📌 Final `dp`: `[2, 3, 7, 18]`
🔢 Length = **4** → So the LIS is of length **4**

Note: the actual LIS is not `[2, 3, 7, 18]` always — `dp` is just used to track the **length**.

---

### ✅ Code:

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

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(LIS(nums))  # Output: 4
```

---

---

### 3. **K-th Smallest Pair Distance**

**Binary Search + bisect** to count how many pairs have distance ≤ `mid`.

---

**K-th Smallest Pair Distance** is a classic problem that uses **binary search + bisect** for optimization.

---

## ✅ Problem:

Given an array `nums` and an integer `k`, find the **k-th smallest absolute difference** between any two elements in the array.

---

## 🧪 Example Input:

```python
nums = [1, 3, 1]
k = 1
```

---

### ✅ Expected Output:

```
0
```

---

## 🧠 Explanation:

All pairwise absolute differences:

* |1 - 1| = **0**
* |1 - 3| = 2
* |3 - 1| = 2

All distances: **\[0, 2, 2]**
Sorted distances: **\[0, 2, 2]**

* The **1st smallest** distance is `0`.

---

---

## 🛠️ Dry Run: Binary Search + Bisect Count

### Key idea:

Binary search the answer (distance), and count how many pairs have distance ≤ `mid`.

---

### 🧩 Helper Function: Count pairs with distance ≤ `mid`

```python
from bisect import bisect_right

def count_pairs_within(nums, max_dist):
    count = 0
    for i in range(len(nums)):
        j = bisect_right(nums, nums[i] + max_dist, i + 1)
        count += j - i - 1
    return count
```

---

### 🔁 Binary Search Flow:

```python
nums = [1, 3, 1]
k = 1
nums.sort()  # [1, 1, 3]
```

Binary search over `dist = 0 to (3 - 1) = 2`

#### Step 1:

* mid = 1
* Count pairs with dist ≤ 1 → Only (1, 1) → count = 1
* count ≥ k → try smaller → `high = 1`

#### Step 2:

* mid = 0
* Count pairs with dist ≤ 0 → Only (1, 1) → count = 1
* count ≥ k → `high = 0`

Loop ends → answer = 0 ✅

---

## ✅ Final Code

```python
from bisect import bisect_right

class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)

        def count_pairs(max_dist):
            count = 0
            for i in range(n):
                j = bisect_right(nums, nums[i] + max_dist, i + 1)
                count += j - i - 1
            return count

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
```

---

## ✅ Example Usage

```python
sol = Solution()
print(sol.smallestDistancePair([1, 3, 1], 1))  # Output: 0
```

---

---

# Extract **k-th largest**

Extracting the **k-th largest pair distance** using `bisect` is a twist on the k-th **smallest** version — we can still use **binary search**, but need to tweak the counting logic.

---

## 💡 Problem:

> Given an array `nums` and integer `k`, find the **k-th largest absolute difference** among all unique pairs `(i, j)` where `i < j`.

---

## ✅ Key Observations:

* Total number of pairs = `n * (n - 1) // 2`
* Sort `nums` to make bisect and pair-counting easier.
* Use binary search to find the smallest distance such that **at least (total\_pairs - k + 1)** pairs have distance ≤ `mid`.
  (Because that would make `mid` the **k-th largest** distance)

---

## 🧪 Example:

```python
nums = [1, 3, 6]
k = 1  # Find the **largest** pair distance
```

All distances:

* |1 - 3| = 2
* |1 - 6| = 5
* |3 - 6| = 3

Sorted distances: **\[2, 3, 5]**
Largest (1st) = **5**

✅ Output: `5`

---

## ✅ Python Code using `bisect_right` + binary search:

```python
from bisect import bisect_right

class Solution:
    def kthLargestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        total_pairs = n * (n - 1) // 2

        def count_pairs_within(d):
            count = 0
            for i in range(n):
                j = bisect_right(nums, nums[i] + d, i + 1)
                count += j - i - 1
            return count

        # Binary search for distance
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            count = count_pairs_within(mid)

            # If we have at least (total_pairs - k + 1) pairs ≤ mid,
            # then mid might be the kth LARGEST
            if count >= total_pairs - k + 1:
                high = mid
            else:
                low = mid + 1
        return low
```

---

### 🔁 Dry Run for nums = \[1, 3, 6], k = 1

* Total pairs = 3
* We want 3 - 1 + 1 = 3 pairs with dist ≤ mid
* Binary search gives:

  * mid = 2 → count = 1 (too small)
  * mid = 3 → count = 2 (still small)
  * mid = 5 → count = 3 ✅

---

## ✅ Example Use:

```python
sol = Solution()
print(sol.kthLargestDistancePair([1, 3, 6], 1))  # Output: 5
```

---

# Pairs with sum ≤ x using bisect

Great! Let's tackle the classic problem: **Count the number of pairs (i, j)** such that:

> `nums[i] + nums[j] ≤ x` and `i < j`

We’ll use **`bisect_right`** for this, which gives a very clean and efficient solution when the array is **sorted**.

---


---

## 🧩 Problem Statement

**Input:**

* An array `nums`
* An integer `x`

**Goal:**
Count the number of **unique pairs** `(i, j)` where:

* `i < j`
* `nums[i] + nums[j] ≤ x`

---

### ✅ Key Idea

1. **Sort the array**.
2. For every `nums[i]`, use `bisect_right()` to find the **largest index `j`** where `nums[i] + nums[j] ≤ x`.
3. For each index `i`, count how many `j > i` satisfy the condition.

---

## ✅ Python Code Using `bisect_right`

```python
from bisect import bisect_right

def count_pairs_with_sum_leq_x(nums, x):
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n):
        # max value nums[j] can be so that nums[i] + nums[j] ≤ x
        target = x - nums[i]
        j = bisect_right(nums, target)

        # j is 1 past the last valid index; subtract i+1 to exclude same/previous
        valid_pairs = max(0, j - i - 1)
        count += valid_pairs

    return count
```

---

### 🧪 Example

```python
nums = [1, 3, 5, 2]
x = 6
```

**Sorted**: `[1, 2, 3, 5]`
Valid pairs:

* (1,2)=3
* (1,3)=4
* (1,5)=6
* (2,3)=5

✅ Total = **4 pairs**

```python
print(count_pairs_with_sum_leq_x([1, 3, 5, 2], 6))  # Output: 4
```

---

## 🧠 Time Complexity

* `O(n log n)` for sorting
* `O(n log n)` for the bisect loop

✅ **Total = O(n log n)** — fast and scalable

---

---

### 4. **Sliding Window Median (SortedList + bisect)**

Maintain a sorted list of size `k` and use `bisect.insort` and `bisect.bisect_left` to remove efficiently.

---

## 🧩 Problem: Sliding Window Median

> Given an array `nums` and integer `k`, return the **median of every sliding window of size `k`**.

---

### ✅ Key Idea

We maintain a sorted window of size `k`. For each new element:

1. **Insert** it into the window in sorted order using `bisect.insort()`.
2. **Remove** the outgoing element using `bisect.bisect_left()` + `del`.
3. Get the **median** from the middle of the window.

---

### ⚡ Tools from `bisect`:

```python
from bisect import insort, bisect_left
```

* `insort(window, x)`: inserts `x` in sorted position.
* `bisect_left(window, x)`: finds index of `x` to remove it efficiently.

---

## ✅ Python Code

```python
from bisect import insort, bisect_left

def sliding_window_median(nums, k):
    window = []
    medians = []

    for i, num in enumerate(nums):
        insort(window, num)  # Insert new element into window

        if i >= k:
            # Remove the element sliding out of the window
            out_elem = nums[i - k]
            idx = bisect_left(window, out_elem)
            del window[idx]

        if i >= k - 1:
            # Get the median
            if k % 2 == 1:
                medians.append(float(window[k // 2]))
            else:
                mid = k // 2
                medians.append((window[mid - 1] + window[mid]) / 2)

    return medians
```

---

### 🧪 Example

```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_median(nums, k))
```

**Output:**

```
[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

---

## 🧠 Time Complexity:

* `O(n log k)`:

  * Each insertion/removal is `O(log k)`
  * Done `n` times

---

---

### 5. **Insert Interval / Merge Intervals**

Find where to insert the new interval using `bisect`.

---

Let's walk through both:

---

## 🧩 1. Insert Interval

### 🔍 Problem:

> You are given a list of **non-overlapping intervals** sorted by start time.
> Insert a new interval and **merge if necessary**, so the result remains sorted and non-overlapping.

---

### ✅ Example

**Input:**

```python
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
```

**Output:**

```python
[[1, 5], [6, 9]]
```

**Explanation:**

* \[1, 3] and \[2, 5] overlap → merge to \[1, 5]
* \[6, 9] remains unchanged

---

## ✅ Python Code

```python
def insert(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # 1. Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2. Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # 3. Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

---

## 🧩 2. Merge Intervals

### 🔍 Problem:

> Given a list of **intervals**, merge all overlapping intervals.

---

### ✅ Example

**Input:**

```python
intervals = [[1, 4], [2, 5], [7, 9]]
```

**Output:**

```python
[[1, 5], [7, 9]]
```

**Explanation:**

* \[1, 4] and \[2, 5] overlap → merge to \[1, 5]
* \[7, 9] is disjoint → keep as is

---

## ✅ Python Code

```python
def merge(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = result[-1][1]

        if start <= last_end:
            # Overlap → merge
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])

    return result
```

---
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