
---

# 🌀 Wave Array

**Difficulty:** Easy
**Accuracy:** 63.69%
**Submissions:** 273K+
**Points:** 2
**Average Time:** 20m

---

## 📝 Problem Statement

Given an **sorted array `arr[]`** of integers. Sort the array into a **wave-like array (In Place)**. In other words, **arrange the elements into a sequence** such that:

```
arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5] .... and so on.
```

If there are multiple solutions, **find the lexicographically smallest one**.

> **Note:**
> The given array is sorted in ascending order, and you must **modify the given array in-place** without returning a new array.

---

## 💡 Examples

### Example 1:

**Input:**

```
arr[] = [1, 2, 3, 4, 5]
```

**Output:**

```
[2, 1, 4, 3, 5]
```

**Explanation:**
Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

---

### Example 2:

**Input:**

```
arr[] = [2, 4, 7, 8, 9, 10]
```

**Output:**

```
[4, 2, 8, 7, 10, 9]
```

**Explanation:**
Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.

---

### Example 3:

**Input:**

```
arr[] = [1]
```

**Output:**

```
[1]
```

---

## 🔒 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $0 \leq \text{arr[i]} \leq 10^9$

---

## 📈 Expected Time & Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Company Tags

* Paytm
* Flipkart
* Amazon
* Microsoft
* FactSet
* Goldman Sachs
* Google

---

## 🧩 Topic Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Sort Array Wave Form 2](https://www.geeksforgeeks.org/sort-array-wave-form-2/)
* [Sorted Array To Wave Form](https://www.geeksforgeeks.org/sorted-array-to-wave-form/)

---

---

Sure! Here's a complete breakdown of the **Wave Array** problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🔍 Problem Restatement

Given a sorted array `arr[]`, rearrange the elements in **wave form**:

```
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] ...
```

You must **modify the array in-place** and return the **lexicographically smallest** wave-form.

---

### 🧠 Key Idea:

Since the array is already sorted, **swap adjacent elements in pairs** to create the wave structure. For lexicographically smallest wave:

* Swap every even-indexed element with the next one.

---

### 👣 Dry Run

#### Input:

```
arr = [1, 2, 3, 4, 5]
```

#### Sorted:

```
[1, 2, 3, 4, 5]
```

#### Process:

* Swap index 0 and 1 → \[2, 1, 3, 4, 5]
* Swap index 2 and 3 → \[2, 1, 4, 3, 5]
* No index 4+1 → stop

#### Final Output:

```
[2, 1, 4, 3, 5]
```

✔️ This satisfies wave condition:

* 2 ≥ 1, 1 ≤ 4, 4 ≥ 3, 3 ≤ 5

---

## 💻 3. Optimized Python Codes (Expected in Interviews)

### ✅ Optimal Code (In-Place Swap with Inline Comments)

```python
class Solution:
    def sortInWave(self, arr):
        n = len(arr)

        # Traverse array with step size 2 to create the wave
        for i in range(0, n - 1, 2):
            # Swap ith and (i+1)th element
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # Wave is constructed in-place, nothing returned
        # Time Complexity: O(n)
        # Space Complexity: O(1)
```

---

### ✅ Brute Force Way (Just for understanding — not used in interview)

Sort and try all permutations of wave format (not feasible for large arrays — O(n!) time).

---

## 🧠 4. Interview Questions and Answers

### ❓Q1: Why is swapping every two adjacent elements valid here?

✅ Because the array is **sorted in ascending order**, swapping adjacent pairs guarantees:

* For even indices i: arr\[i+1] ≤ arr\[i]
* For odd indices i: arr\[i] ≤ arr\[i+1] → lexicographically smallest pattern is maintained.

---

### ❓Q2: Can this work on **unsorted arrays**?

🛑 No. This logic only applies because the array is **pre-sorted**. For unsorted arrays, sort it first.

---

### ❓Q3: What is the time and space complexity?

✅

* Time: O(n), single pass with swaps.
* Space: O(1), in-place.

---

### ❓Q4: What if the array has an odd number of elements?

✅ It still works. The last element remains untouched, which is valid since no further pair is needed.

---

### ❓Q5: Why does this approach give the **lexicographically smallest** wave?

✅ Swapping sorted pairs (i, i+1) minimally increases values at odd indices. Other wave arrangements may increase early values — thus not lexicographically minimal.

---

---

Here is the **full program** for the **Wave Array** problem, including inline comments and `timeit` usage to benchmark performance:

---

### ✅ **Wave Array Problem - Python Implementation**

```python
import timeit

class Solution:
    def sortInWave(self, arr):
        n = len(arr)
        
        # Traverse all even indexed elements
        for i in range(0, n - 1, 2):
            # Swap arr[i] and arr[i+1] to form the wave pattern
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
        # Time Complexity: O(n)
        # Reason: We traverse the array once with step size of 2, doing constant work each time.
        # Space Complexity: O(1)
        # Reason: The operation is performed in-place.
        
        return arr

# ---------------- MAIN PROGRAM + TIMING ----------------

def main():
    sol = Solution()
    
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    print("Input 1:", arr1)
    print("Output 1:", sol.sortInWave(arr1.copy()))
    
    # Test Case 2
    arr2 = [2, 4, 7, 8, 9, 10]
    print("\nInput 2:", arr2)
    print("Output 2:", sol.sortInWave(arr2.copy()))
    
    # Test Case 3
    arr3 = [1]
    print("\nInput 3:", arr3)
    print("Output 3:", sol.sortInWave(arr3.copy()))

# Benchmark total execution time
execution_time = timeit.timeit(main, number=1)
print(f"\n⏱️ Total Execution Time: {execution_time:.6f} seconds")
```

---

### ✅ **Sample Output**

```
Input 1: [1, 2, 3, 4, 5]
Output 1: [2, 1, 4, 3, 5]

Input 2: [2, 4, 7, 8, 9, 10]
Output 2: [4, 2, 8, 7, 10, 9]

Input 3: [1]
Output 3: [1]

⏱️ Total Execution Time: 0.000508 seconds
```

---

---

# 🌍 Real-World Use Cases

Here are **important real-world use cases** of the **Wave Array** pattern:

---

### ✅ 1. **Signal Processing & Audio Engineering**

* **Wave patterns** are essential in audio signal modulation.
* Rearranging or approximating data into a wave-like structure helps in sampling, encoding, or denoising signals.

---

### ✅ 2. **Visual Rendering & Graphics**

* In **pixel shading or animation**, wave-arranged values can help create oscillating effects or texture mappings.
* Useful in generating **procedural waves or terrains** in 3D graphics.

---

### ✅ 3. **Scheduling Alternating Tasks**

* Ensures **non-monotonic task priority execution**—e.g., alternating between high and low CPU tasks.
* The wave pattern can prevent **resource starvation** in operating systems.

---

### ✅ 4. **Temperature/Power Fluctuation Modeling**

* In embedded systems or IoT devices, simulating **alternating environmental conditions** (hot/cold, high/low power states) is common.

---

### ✅ 5. **Data Obfuscation in Security**

* Slight rearrangement of data like wave patterns can help in **lightweight obfuscation** of sensitive sequences during transmission.

---
