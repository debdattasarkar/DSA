Let's now tackle **Leetcode 162: Find Peak Element**, a classic binary search application — and very popular in interviews like at Amazon, Apple, and Microsoft.

---

## 🧩 Leetcode 162: Find Peak Element

🔗 [Leetcode 162](https://leetcode.com/problems/find-peak-element/)

> A **peak element** is one that is **strictly greater than its neighbors**.
> Given an array `nums`, find a **peak element** and return its index.
> Assume `nums[-1] = -∞` and `nums[n] = -∞`, i.e., **virtual boundaries**.

* A peak may not be unique — return **any** peak index.
* Must be solved in **O(log n)** time.

---

### 🧠 Example

```txt
Input:  nums = [1,2,3,1]
Output: 2   (because 3 > 2 and 3 > 1)

Input:  nums = [1,2,1,3,5,6,4]
Output: 5   (6 > 5 and 6 > 4)
```

---

## ✅ Key Insight

Use **binary search** because:

* If `nums[mid] > nums[mid + 1]` → a **peak lies on the left** (including mid)
* Else → a **peak lies on the right** (excluding mid)

Why? Because the slope direction guides us toward a peak.

---

## ✅ Optimal Binary Search Code (Python)

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # Peak is on the left half (including mid)
                right = mid
            else:
                # Peak is on the right half (excluding mid)
                left = mid + 1

        return left  # or right — they converge to the peak index
```

---

## 🧠 Dry Run for `nums = [1, 2, 1, 3, 5, 6, 4]`

* mid = 3 → nums\[3]=3 < nums\[4]=5 → move right → left = 4
* mid = 5 → nums\[5]=6 > nums\[6]=4 → move left → right = 5
* mid = 4 → nums\[4]=5 < nums\[5]=6 → move right → left = 5

✅ `left == right == 5` → peak = `6`

---

## 🕐 Time and Space Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | `O(log n)` |
| Space  | `O(1)`     |

---

## ✅ Test Cases

```python
assert 2 == Solution().findPeakElement([1, 2, 3, 1])
assert Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
assert Solution().findPeakElement([1]) == 0
assert Solution().findPeakElement([2, 1]) == 0
```

---

---

```python

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = 0, n - 1

        # Step 1: Binary Search Loop
        # Time Complexity: O(log n) — halves the search space each iteration
        # Space Complexity: O(1) — constant space used
        while start <= end:
            mid = (start + end) // 2

            # Step 2: Define neighbors with edge protection
            # Time: O(1) per access
            left = float('-inf') if mid == 0 else nums[mid - 1]
            right = float('-inf') if mid == n - 1 else nums[mid + 1]

            # Step 3: Peak Check
            if nums[mid] >= left and nums[mid] >= right:
                return mid  # Found a peak

            # Step 4: Decide search direction
            elif nums[mid] < right:
                start = mid + 1  # Move to right half
            else:
                end = mid - 1    # Move to left half

        return -1  # This shouldn't happen as a peak is guaranteed

```

Great question! Let’s **compare** both solutions for **Leetcode 162: Find Peak Element** — both are correct, but they differ in **design, elegance, and assumptions**.

---

## ✅ 1. **Your Provided Code (GFG-style Version)**

```python
while start <= end:
    mid = (start + end) // 2
    left = float('-inf') if mid == 0 else arr[mid - 1]
    right = float('-inf') if mid == n - 1 else arr[mid + 1]

    if arr[mid] >= left and arr[mid] >= right:
        return mid
    elif arr[mid] < right:
        start = mid + 1
    else:
        end = mid - 1
```

### ✔️ Pros:

* Handles **edges explicitly** with `-∞` at `arr[-1]` and `arr[n]` (virtual boundaries)
* Fully **generalized**: works for any array size and ensures safe bounds
* You can easily adapt this for **finding all peaks** or customized conditions

### ⚠️ Slight Cons:

* Slightly more verbose (explicit neighbors)
* Uses more conditionals per loop (`if-else` with left/right)

---

## ✅ 2. **Leetcode Official Binary Search Version**

```python
while left < right:
    mid = (left + right) // 2
    if nums[mid] > nums[mid + 1]:
        right = mid
    else:
        left = mid + 1
```

### ✔️ Pros:

* **Elegant and minimal**
* Fewer comparisons — compares only `mid` and `mid + 1`
* Leverages the **slope** nature of the array to always guide toward a peak

### ⚠️ Slight Cons:

* Only safe because of the **virtual -∞** assumption from Leetcode
* Not as readable for beginners

---

## 🔁 Summary Table

| Feature                             | GFG-Style (Your Code)        | Leetcode-Style (Slope Method)        |
| ----------------------------------- | ---------------------------- | ------------------------------------ |
| Explicit edge handling              | ✅ `-inf` for edges           | ❌ Assumes safe access at `mid+1`     |
| Simplicity                          | ❌ More verbose               | ✅ Concise and elegant                |
| Peak detection logic                | General (≥ both neighbors)   | Optimized via slope check            |
| Safe for `n = 1 or 2`               | ✅ Fully safe                 | ✅ Also safe                          |
| Adaptability (e.g., find all peaks) | ✅ Easy to modify             | ❌ Harder to generalize               |
| Iteration direction                 | Based on neighbor comparison | Based on increasing/decreasing slope |
| Time Complexity                     | `O(log n)`                   | `O(log n)`                           |

---

## 👑 Which One to Use?

| Scenario                  | Use Which?                     |
| ------------------------- | ------------------------------ |
| **Interviews (Leetcode)** | ✅ Leetcode-style (fast, clear) |
| **GFG/CP/Pythonic code**  | ✅ Your version (fully safe)    |
| **Variant questions**     | ✅ Your version is flexible     |

---

Here are the **top interview questions and follow-ups** based on **Leetcode 162: Find Peak Element** — often used to test how well you understand binary search in non-traditional settings.

---

## 🔹 Understanding the Problem

### 1. **What is a peak element?**

A peak is any element that is **strictly greater than its neighbors**.
Special cases:

* `nums[0]` is a peak if `nums[0] > nums[1]`
* `nums[n-1]` is a peak if `nums[n-1] > nums[n-2]`

---

### 2. **Can there be multiple peaks?**

Yes. You're only required to **return any one** of them.
For example, `[1,3,2,1,3,2]` has peaks at indices 1 and 4.

---

### 3. **What is the time complexity of your solution?**

* **Binary search version:** `O(log n)`
* **Brute-force version:** `O(n)` (check all neighbors)

---

### 4. **Why does binary search work here if the array is unsorted?**

Because if `nums[mid] > nums[mid+1]`, a **peak must exist on the left side**, including mid.
This is due to the **"slope" property** of the array.

---

## 🔸 Edge Cases

### 5. **What if array length is 1 or 2?**

* `[1]` → return 0
* `[2,1]` → return 0
* `[1,2]` → return 1

✅ Binary search naturally handles these.

---

### 6. **What if all elements are equal?**

Technically, no **strict peak** exists. But the Leetcode definition still treats the first or last element as a peak because of the virtual `-∞` neighbors.

---

## 🔺 Follow-Up Questions

### 7. **How do you return all peak elements?**

Use a linear scan:

```python
for i in range(n):
    if (i == 0 or nums[i] > nums[i-1]) and (i == n-1 or nums[i] > nums[i+1]):
        peaks.append(i)
```

This takes `O(n)` time.

---

### 8. **Can you solve this without using `nums[mid+1]` (to avoid index out-of-bound)?**

Yes. You can check both neighbors:

```python
left = float('-inf') if mid == 0 else nums[mid - 1]
right = float('-inf') if mid == n - 1 else nums[mid + 1]
```

---

### 9. **What if you wanted the first peak (leftmost) or the last (rightmost)?**

The basic binary search returns **any** peak. To find:

* **Leftmost peak**: move `right = mid`
* **Rightmost peak**: modify loop to move `left = mid + 1` more aggressively

---

### 10. **Can this be extended to 2D arrays?**

Yes — that’s **Leetcode 1901: Find a Peak Element in a 2D Grid**.
It uses a **greedy column-wise binary search**, finding a column's max, then checking neighbors.

---

## 🧠 Advanced Thinking Exercise

**“Prove that a peak always exists in any 1D array.”**

* Base case: 1 element → peak
* Any array will rise and fall or flatten — there will be a local max somewhere.

---

---

# Real-World Use Cases

Here are a few **important real-world use cases** of **1D and 2D peak finding**:

---

### ✅ 1. **Image Processing**

* Used to detect **bright spots**, **blobs**, or **corners** in images.
* Example: Finding stars in astronomical images or objects in vision systems.

---

### ✅ 2. **Terrain Analysis**

* Peaks in elevation data represent **mountains or high points** in geographic maps.
* Used in **route planning**, **3D mapping**, or **flood modeling**.

---

### ✅ 3. **Signal & Audio Processing**

* Peaks in 1D signals represent **events**, **beats**, or **spikes**.
* Used in **music beat detection**, **speech analysis**, **seismic activity**.

---

### ✅ 4. **Model Attention Maps (Deep Learning)**

* In attention or heatmaps, peaks show **where a model focuses**.
* Used in **model interpretability** or **explainable AI**.

---

These are widely used in **real-time applications**, and peak-finding is a **fundamental tool** in both research and industry.
