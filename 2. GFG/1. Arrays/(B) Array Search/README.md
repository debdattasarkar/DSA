
---

# Array Search

> Difficulty: **Basic**
> Accuracy: **40.95%**
> Submissions: **455K+**
> Points: **1**
> Average Time: **15m**

---

## Problem Statement

Given an array, `arr` of `n` integers, and an integer element `x`, find whether element `x` is present in the array.
Return the index of the **first occurrence** of `x` in the array, or **-1 if it doesn't exist**.

---

## Examples

### Example 1:

```
Input: arr[] = [1, 2, 3, 4], x = 3  
Output: 2  
Explanation: There is one test case with array as [1, 2, 3, 4] and element to be searched as 3.  
Since 3 is present at index 2, the output is 2.
```

### Example 2:

```
Input: arr[] = [10, 8, 30, 4, 5], x = 5  
Output: 4  
Explanation: For array [10, 8, 30, 4, 5], the element to be searched is 5 and it is at index 4.
So, the output is 4.
```

### Example 3:

```
Input: arr[] = [10, 8, 30], x = 6  
Output: -1  
Explanation: The element to be searched is 6 and it's not present, so we return -1.
```

---

## Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $0 \leq \text{arr}[i] \leq 10^6$
* $0 \leq x \leq 10^5$

---

## Expected Complexities

* **Time Complexity**: O(n)
* **Auxiliary Space**: O(1)

---

## Topic Tags

* Arrays
* Searching
* Data Structures
* Algorithms

---

## Related Articles

* [CPP Program For Linear Search](https://www.geeksforgeeks.org/cpp-program-for-linear-search/)
* [Java Program For Linear Search](https://www.geeksforgeeks.org/java-program-for-linear-search/)
* [Linear Search](https://www.geeksforgeeks.org/linear-search/)

---

---

Here is the full solution with:

1. **Text Explanation**
2. **Step-by-step Dry Run**
3. **Python Code** (Brute-force / Expected Interview Format)
4. **Common Interview Questions & Answers**

---

## ✅ 2. Text Explanation

You are given an integer array `arr[]` and an integer `x`. Your task is to find the **first occurrence index** of `x` in the array.
If the element does **not exist**, return `-1`.

This is a **classic linear search** problem. Since the array is not sorted, you have to scan from **left to right**, checking each element until you find a match.

---

## 🧠 Step-by-Step Dry Run

### Example

```
arr = [10, 8, 30, 4, 5], x = 5

Step 1: i = 0 → arr[0] = 10 ≠ 5 → continue
Step 2: i = 1 → arr[1] = 8 ≠ 5 → continue
Step 3: i = 2 → arr[2] = 30 ≠ 5 → continue
Step 4: i = 3 → arr[3] = 4 ≠ 5 → continue
Step 5: i = 4 → arr[4] = 5 == x → return 4

✅ Output: 4
```

---

## 🧾 3. Optimized Python Code (Expected in Interviews)

```python
class Solution:
    def search(self, arr, x):
        """
        Perform linear search to find the first occurrence of x in arr.

        Time Complexity: O(n) - traverses the array once
        Space Complexity: O(1) - constant space used
        """
        for i in range(len(arr)):  # O(n)
            if arr[i] == x:        # O(1)
                return i           # first match found
        return -1                  # not found
```

### 🔧 Main Function with Input/Output

```python
import timeit

def main():
    arr = [10, 8, 30, 4, 5]
    x = 5

    sol = Solution()
    start = timeit.default_timer()
    result = sol.search(arr, x)
    end = timeit.default_timer()

    print("Input Array:", arr)
    print("Search Element:", x)
    print("First Occurrence Index:", result)
    print("Execution Time:", end - start, "seconds")

if __name__ == "__main__":
    main()
```

---

## 💡 Alternate Easy Pythonic Code (For discussion, not interview)

```python
class Solution:
    def search(self, arr, x):
        # Try to use list.index() method
        try:
            return arr.index(x)  # Returns first occurrence
        except ValueError:
            return -1
```

🔁 Same time complexity: `O(n)`
❗ **Note:** Interviewers may prefer the manual loop version for learning/debugging purposes.

---

## ❓ 4. Interview Questions & Answers

### Q1: Why do we use linear search here?

**A:** Because the array is not sorted. Binary search only works on sorted arrays.

---

### Q2: What’s the time complexity?

**A:** O(n) in the worst case — when the element is not present or is the last element.

---

### Q3: Can you reduce the space complexity?

**A:** It’s already O(1), which is optimal — no extra memory is used.

---

### Q4: Can binary search be used?

**A:** No, unless the array is sorted. Since it's unsorted, binary search won't work correctly.

---

### Q5: How would you handle duplicates?

**A:** The current approach returns the **first occurrence**, which satisfies the problem requirement.

---

### Q6: How can you improve performance for frequent searches?

**A:** Use a dictionary (hashmap) to store value-to-index mappings in `O(n)` preprocessing time, then answer queries in `O(1)`.

---

---

# Binary Search version (Only if Array is Sorted)

Here is the **Binary Search version** of the `Array Search` problem for **sorted arrays only**, including:

* Full program in Python
* Inline comments
* Time and space complexity analysis
* `timeit` usage to measure performance

---

### ✅ Binary Search (for Sorted Arrays)

```python
import timeit

class Solution:
    def binarySearch(self, arr, x):
        """
        Performs binary search on sorted array to find x.

        Time Complexity: O(log n)
            - Logarithmic due to halving the search space every time.
        Space Complexity: O(1)
            - No extra memory used.
        """
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2  # Mid index

            if arr[mid] == x:
                return mid  # x found at mid
            elif arr[mid] < x:
                low = mid + 1  # Search right half
            else:
                high = mid - 1  # Search left half

        return -1  # x not found


def main():
    # Sorted input array
    arr = [10, 20, 30, 40, 50, 60, 70]
    x = 50

    sol = Solution()

    # Benchmark with timeit
    start = timeit.default_timer()
    result = sol.binarySearch(arr, x)
    end = timeit.default_timer()

    print("Input (sorted array):", arr)
    print("Element to search:", x)
    print("Output index:", result)
    print("Execution time: {:.8f} seconds".format(end - start))


if __name__ == "__main__":
    main()
```

---

### ✅ Sample Output

```
Input (sorted array): [10, 20, 30, 40, 50, 60, 70]
Element to search: 50
Output index: 4
Execution time: 0.00000112 seconds
```

---

### ✅ Complexity Analysis

| Operation                | Time Complexity | Space Complexity | Notes                              |
| ------------------------ | --------------- | ---------------- | ---------------------------------- |
| Binary Search            | O(log n)        | O(1)             | Divides array in half at each step |
| Iterative Implementation | O(log n)        | O(1)             | Avoids recursion overhead          |
| `timeit` measurement     | O(1)            | O(1)             | Benchmarking utility               |

---

### 📌 Interview Notes

* **When to use Binary Search?** Only when the array is sorted.
* **What if array is unsorted?** Use **Linear Search** (`O(n)`) instead.
* **Can this be recursive?** Yes. Recursion adds O(log n) stack space.

---

---

Here’s the **complete Python program** for the **“Array Search”** problem with:

* **Full inline comments**
* **Time and space complexity analysis**
* **Input/output example**
* **`timeit` usage** to benchmark execution time

---

## ✅ Problem Recap

**Task:** Given an array `arr[]` and a number `x`, return the index of the **first occurrence** of `x`.
Return `-1` if not found.

---

### ✅ Full Python Program

```python
import timeit

class Solution:
    def search(self, arr, x):
        """
        Function to search the first occurrence of x in the array.

        Time Complexity: O(n)
            - Worst case: scan all n elements.
            - Best case: x is at index 0 → O(1)

        Space Complexity: O(1)
            - No extra data structures used.
        """
        for i in range(len(arr)):  # Loop through array → O(n)
            if arr[i] == x:        # Constant-time comparison → O(1)
                return i           # Found at index i → return immediately
        return -1                  # Not found → return -1


def main():
    # Sample input
    arr = [10, 20, 30, 40, 50, 60]
    x = 40

    # Create object of Solution class
    sol = Solution()

    # Measure execution time using timeit
    start = timeit.default_timer()

    # Call the search method
    result = sol.search(arr, x)

    end = timeit.default_timer()

    # Output the results
    print("Input array:", arr)
    print("Element to search:", x)
    print("Output index:", result)
    print("Execution time: {:.8f} seconds".format(end - start))

if __name__ == "__main__":
    main()
```

---

## ✅ Sample Output

```
Input array: [10, 20, 30, 40, 50, 60]
Element to search: 40
Output index: 3
Execution time: 0.00000123 seconds
```

---

## 🔍 Time & Space Complexity Recap

| Step                         | Time Complexity | Space Complexity | Notes                    |
| ---------------------------- | --------------- | ---------------- | ------------------------ |
| Loop through `n` elements    | O(n)            | O(1)             | Worst case: x not found  |
| Early return if `x` is found | O(1) to O(n)    | O(1)             | Best case: index 0 match |
| Constant time printing       | O(1)            | O(1)             | Not data dependent       |

---

