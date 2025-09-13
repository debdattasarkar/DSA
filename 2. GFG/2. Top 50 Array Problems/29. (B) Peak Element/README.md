# Peak element

**Difficulty:** Basic
**Accuracy:** 38.86%
**Submissions:** 550K+
**Points:** 1
**Average Time:** 30m

---

Given an array `arr[]` where no two adjacent elements are same, find the **index of a peak element**.
An element is considered to be a **peak** if it is greater than its adjacent elements (if they exist).
If there are multiple peak elements, return index of any one of them.

The output will be **"true"** if the index returned by your function is correct; otherwise, it will be **"false"**.

**Note:** Consider the element **before the first** element and the element **after the last** element to be negative infinity.

---

## Examples

### Example 1

**Input:** `arr = [1, 2, 4, 5, 7, 8, 3]`
**Output:** `true`
**Explanation:** `arr[5] = 8` is a peak element because `arr[4] < arr[5] > arr[6]`.

### Example 2

**Input:** `arr = [10, 20, 15, 2, 23, 90, 80]`
**Output:** `true`
**Explanation:** `arr[1] = 20` and `arr[5] = 90` are peak elements because `arr[0] < arr[1] > arr[2]` and `arr[4] < arr[5] > arr[6]`.

### Example 3

**Input:** `arr = [1, 2, 3]`
**Output:** `true`
**Explanation:** `arr[2]` is a peak element because `arr[1] < arr[2]` and `arr[2]` is the last element, so it has negative infinity to its right.

---

## Constraints

* `1 < arr.size() ≤ 10^6`
* `-2^31 ≤ arr[i] ≤ 2^31 - 1`

---

## Expected Complexities

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* `Accolite`, `Amazon`, `Visa`, `Adobe`, `Google`

---

## Topic Tags

* `Arrays`, `Searching`, `Data Structures`, `Algorithms`

---

## 📚 Related Interview Experiences

* [Amazon Interview Experience Set 257 Off Campus](https://www.geeksforgeeks.org/amazon-interview-experience-set-257-off-campus/)

---

## 📄 Related Articles

* [Find A Peak In A Given Array](https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/)

---

---

Here’s your complete solution to the **Peak Element** problem in four parts:

---

## 📘 1. Text Explanation

A **peak element** in an array is an element that is **strictly greater** than its neighbors. You need to return **any one** such index.

### Special Conditions:

* The first element has only the right neighbor.
* The last element has only the left neighbor.
* Elements before the first and after the last are considered `-∞` (negative infinity).

---

## 🔍 2. Step-by-Step Dry Run

### Input:

```python
arr = [10, 20, 15, 2, 23, 90, 80]
```

### Binary Search-based Dry Run:

* `start = 0`, `end = 6`

* `mid = (0 + 6) // 2 = 3 → arr[3] = 2`
  → `arr[3] < arr[4]`, so peak must be in **right half**.

* `start = 4`, `end = 6`

* `mid = (4 + 6) // 2 = 5 → arr[5] = 90`
  → `arr[5] > arr[4]` and `arr[5] > arr[6]`
  ✅ Found a **peak** at index 5 → return 5

---

## ✅ 3. Optimized Python Solutions

---

### 🔹 Brute Force (Not recommended in interviews unless explicitly asked)

```python
class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        for i in range(n):
            left = float('-inf') if i == 0 else arr[i - 1]
            right = float('-inf') if i == n - 1 else arr[i + 1]
            if arr[i] > left and arr[i] > right:
                return i  # Peak element found
        return -1
```

* ⏱ Time: O(n)
* 🧠 Space: O(1)

---

### 🔸 Optimized Binary Search (Interview Preferred — O(log n))

```python
class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2

            # Get neighbors safely
            left = float('-inf') if mid == 0 else arr[mid - 1]
            right = float('-inf') if mid == n - 1 else arr[mid + 1]

            # Check peak condition
            if arr[mid] >= left and arr[mid] >= right:
                return mid
            elif arr[mid] < right:
                start = mid + 1  # Move right
            else:
                end = mid - 1    # Move left

        return -1
```

* ⏱ Time: O(log n)
* 🧠 Space: O(1)

---

## 🧠 4. Interview Questions & Answers

---

### ❓ Q1: Why is binary search applicable here?

**A:** Because we can discard half of the array each time:

* If `arr[mid] < arr[mid+1]`, then a peak **must** exist on the right.
* If `arr[mid] < arr[mid-1]`, then a peak **must** exist on the left.

---

### ❓ Q2: Can there be multiple peaks?

**A:** Yes. The problem allows returning **any one** of them.

---

### ❓ Q3: What are edge cases?

* Single-element array → It is always a peak
* Increasing array → Last element is the peak
* Decreasing array → First element is the peak

---

### ❓ Q4: What’s the difference between this and "maximum element"?

**A:** The **maximum element** must be the greatest overall.
A **peak** is only required to be greater than its immediate neighbors.

---

### ❓ Q5: What if adjacent elements are equal?

**A:** The problem states **no two adjacent elements are the same**, so this case won't happen.

---

Here is the **full Python program** for the **Peak Element** problem using your provided binary search code, complete with:

* ✅ **Inline comments** explaining each step
* ✅ **Time and space complexity** per operation
* ✅ A working **test input and output**
* ✅ `time.time()` to record total execution time

---

```python
import time

class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        start, end = 0, n - 1

        # Step 1: Binary Search Loop
        # Time Complexity: O(log n) — halves the search space each iteration
        # Space Complexity: O(1) — constant space used
        while start <= end:
            mid = (start + end) // 2

            # Step 2: Define neighbors with edge protection
            # Time: O(1) per access
            left = float('-inf') if mid == 0 else arr[mid - 1]
            right = float('-inf') if mid == n - 1 else arr[mid + 1]

            # Step 3: Peak Check
            if arr[mid] >= left and arr[mid] >= right:
                return mid  # Found a peak

            # Step 4: Decide search direction
            elif arr[mid] < right:
                start = mid + 1  # Move to right half
            else:
                end = mid - 1    # Move to left half

        return -1  # This shouldn't happen as a peak is guaranteed

# ---------- 🧪 Example Execution and Timing ----------

if __name__ == "__main__":
    # Example input array
    arr = [10, 20, 15, 2, 23, 90, 80]

    print("Input Array:", arr)

    # Start timer
    start_time = time.time()

    sol = Solution()
    peak_index = sol.peakElement(arr)

    # End timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Output result
    print("Output (Peak Index):", peak_index)
    print("Peak Element Value:", arr[peak_index] if peak_index != -1 else None)
    print("Execution Time: {:.6f} seconds".format(elapsed_time))
```

---

### ✅ Sample Output:

```
Input Array: [10, 20, 15, 2, 23, 90, 80]
Output (Peak Index): 5
Peak Element Value: 90
Execution Time: 0.0000XX seconds
```

---

### 🔍 Complexity Summary

| Step                    | Time Complexity | Space Complexity |
| ----------------------- | --------------- | ---------------- |
| Binary Search (`while`) | O(log n)        | O(1)             |
| Neighbor Check          | O(1)            | O(1)             |
| **Total**               | **O(log n)**    | **O(1)**         |

---

---


