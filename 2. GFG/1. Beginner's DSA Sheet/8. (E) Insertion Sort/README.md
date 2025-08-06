
---

# 🧮 Insertion Sort

**Difficulty:** Easy
**Accuracy:** 66.61%
**Submissions:** 244K+
**Points:** 2
**Average Time:** 15 mins

---

### 📝 Problem Statement

Given an array `arr[]` of positive integers, your task is to **complete the `insertsort()` function**, which implements the **insertion sort** algorithm.

---

### 🔢 Examples

#### Example 1:

**Input:**
`arr[] = [4, 1, 3, 9, 7]`
**Output:**
`[1, 3, 4, 7, 9]`
**Explanation:**
The sorted array will be `[1, 3, 4, 7, 9]`.

---

#### Example 2:

**Input:**
`arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`
**Output:**
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
**Explanation:**
The sorted array will be `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.

---

#### Example 3:

**Input:**
`arr[] = [4, 1, 9]`
**Output:**
`[1, 4, 9]`
**Explanation:**
The sorted array will be `[1, 4, 9]`.

---

### 📊 Constraints

* `1 ≤ arr.size() ≤ 1000`
* `1 ≤ arr[i] ≤ 1000`

---

### ⏱️ Expected Time & Space Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(1)`

---

### 🏢 Company Tags

* Microsoft
* MAQ Software
* Juniper Networks
* Cisco
* Accenture
* Dell
* Veritas
* Grofers

---

### 🏷️ Topic Tags

* Sorting
* Algorithms

---

### 🧪 Related Interview Experiences

* Veritas Interview Experience Set 2 Campus

---

### 📚 Related Articles

* [Insertion Sort Algorithm](https://www.geeksforgeeks.org/insertion-sort/)

---

---

Certainly! Let's go step-by-step:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 💡 **Insertion Sort Logic:**

Insertion Sort builds the final sorted array one item at a time.
At each iteration, it removes one element from the input, finds the location it belongs in the sorted part, and inserts it there.

* Think of sorting playing cards in your hand: You pick one card at a time and insert it into the correct position.

### 🔁 Algorithm Steps:

1. Start from the second element (index 1), treat the first element as sorted.
2. Compare current element with all elements before it.
3. Shift elements one position to the right to make space.
4. Insert current element at the correct position.

---

### 🧪 Dry Run Example

#### Input:

```python
arr = [4, 1, 3, 9, 7]
```

#### Iteration-wise Changes:

* i=1 → key=1
  compare with 4 → 1 < 4 → shift 4
  insert 1 → `[1, 4, 3, 9, 7]`

* i=2 → key=3
  compare with 4 → 3 < 4 → shift 4
  compare with 1 → 3 > 1 → insert 3 → `[1, 3, 4, 9, 7]`

* i=3 → key=9
  9 > 4 → no shifting needed → `[1, 3, 4, 9, 7]`

* i=4 → key=7
  7 < 9 → shift 9
  7 > 4 → insert 7 → `[1, 3, 4, 7, 9]`

---

## ✅ 3. Optimized Python Code (Insertion Sort)

```python
class Solution:
    def insertionSort(self, arr):
        """
        Performs insertion sort on the given array.

        Time Complexity: O(n^2) in worst case (when array is reverse sorted)
                         O(n) in best case (when already sorted)
        Space Complexity: O(1) - In-place sorting
        """
        n = len(arr)
        for i in range(1, n):
            key = arr[i]  # Current element to place correctly
            j = i - 1
            # Move elements greater than key to one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            # Place key after the last smaller element
            arr[j + 1] = key
```

---

## ✅ 4. Interview Questions & Answers

### 💬 Q1: What is the worst-case time complexity of Insertion Sort?

**A:** O(n²) when the array is sorted in reverse order.

---

### 💬 Q2: What is the best-case time complexity?

**A:** O(n), when the array is already sorted.

---

### 💬 Q3: Is insertion sort stable?

**A:** Yes, insertion sort is stable because it does not swap equal elements.

---

### 💬 Q4: Why would you use insertion sort over other algorithms?

**A:**

* Simple to implement.
* Efficient for **small** datasets.
* Useful for **nearly sorted** arrays.
* Stable and in-place (no extra memory needed).

---

### 💬 Q5: Can insertion sort be used in real-time systems?

**A:** Yes, due to its simplicity and low overhead, it can be used in systems where simplicity is more important than efficiency for large inputs.

---

---

Here is the **complete Python program** for **Insertion Sort** including:

* Inline **comments**
* **Time and space complexity** for each step
* **Input** and **output**
* Timing using `time` module

---

### ✅ Code

```python
import time

class Solution:
    def insertionSort(self, arr):
        """
        Sorts the given array in-place using Insertion Sort.

        Time Complexity:
            - Best Case (Already Sorted): O(n)
            - Worst/Average Case: O(n^2)
        
        Space Complexity:
            - O(1): In-place sorting, no extra space used.
        """
        n = len(arr)
        for i in range(1, n):
            key = arr[i]  # Element to insert into the sorted part
            j = i - 1

            # Shift larger elements one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # Insert the key in correct location
            arr[j + 1] = key


# ---------------- Main Program -------------------

if __name__ == "__main__":
    # Sample input
    input_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Input array:", input_arr)

    # Create solution instance
    solution = Solution()

    # Start timer
    start_time = time.time()

    # Run insertion sort
    solution.insertionSort(input_arr)

    # End timer
    end_time = time.time()

    # Output sorted array
    print("Sorted array:", input_arr)
    
    # Output runtime
    print(f"Time taken to run insertion sort: {(end_time - start_time):.6f} seconds")
```

---

### ✅ Sample Input & Output

```python
Input array: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Sorted array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Time taken to run insertion sort: 0.000013 seconds
```

---

---

# 🌍 Real-World Use Cases

Here are some **real-world use cases** where **Insertion Sort** is **practically useful**, despite its $O(n^2)$ complexity in the average and worst case:

---

### 🔹 1. **Small Dataset Sorting (Embedded Systems)**

* **Why?** Simpler code, no extra memory usage.
* **Where?**

  * Microcontrollers, IoT devices.
  * Sorting sensor readings, e.g., last 10 temperature readings.

---

### 🔹 2. **Nearly Sorted Data**

* **Why?** Insertion sort runs in **O(n)** time for nearly sorted arrays.
* **Where?**

  * Updating sorted lists like attendance logs, leaderboards, etc.
  * Online algorithms that keep sorted data after every new insertion.

---

### 🔹 3. **Hybrid Sorting Algorithms (e.g., Timsort)**

* **Why?** Fast for small chunks (Timsort switches to insertion sort for small segments).
* **Where?**

  * Built-in Python `sort()` and Java’s `Arrays.sort()` for small segments.
  * Split large arrays and use insertion sort for individual segments (base case of recursion).

---

### 🔹 4. **Teaching/Training Tool**

* **Why?** It is conceptually simple and easy to debug.
* **Where?**

  * Used to teach algorithm design, stability in sorting, and complexity analysis.

---

### 🔹 5. **Auto-Completion Systems**

* **Why?** Keeps short suggestion lists sorted with frequent inserts.
* **Where?**

  * Code editors, search engines (for top-10 suggestions).

---

