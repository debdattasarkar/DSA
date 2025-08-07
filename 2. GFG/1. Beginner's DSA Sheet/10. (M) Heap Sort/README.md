
---

# 🧮 Heap Sort

**Difficulty**: Medium
**Accuracy**: 53.06%
**Submissions**: 125K+
**Points**: 4
**Average Time**: 20 minutes

---

## 🧾 Problem Statement

Given an array `arr[]`, the task is to **sort the array elements using Heap Sort**.

---

## 🧪 Examples

### Example 1:

**Input**:
`arr[] = [4, 1, 3, 9, 7]`
**Output**:
`[1, 3, 4, 7, 9]`
**Explanation**:
After sorting using Heap Sort, elements will be in order as `1, 3, 4, 7, 9`.

---

### Example 2:

**Input**:
`arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`
**Output**:
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
**Explanation**:
After sorting using Heap Sort, elements will be in ascending order.

---

### Example 3:

**Input**:
`arr[] = [2, 1, 5]`
**Output**:
`[1, 2, 5]`
**Explanation**:
Heap Sort arranges the elements as `1, 2, 5`.

---

## 📚 Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `1 ≤ arr[i] ≤ 10^6`

---

## 📈 Expected Complexities

* **Time Complexity**: O(n log n)
* **Auxiliary Space**: O(1)

---

## 🏷️ Company Tags

`Amazon`, `Microsoft`, `Samsung`, `24*7 Innovation Labs`, `Oracle`, `Visa`, `Intuit`, `SAP Labs`, `Belzabar`

---

## 🧩 Topic Tags

* Sorting
* Heap
* Data Structures
* Algorithms

---

## 💼 Related Interview Experiences

* Intuit Interview Experience Set 7 (3–5 Years Experienced)

---

## 📖 Related Articles

* [Artiklinked List11](https://www.geeksforgeeks.org/arbitlinked-list11/)
* [CPP Program For Heap Sort](https://www.geeksforgeeks.org/cpp-program-for-heap-sort/)
* [Heap Sort](https://www.geeksforgeeks.org/heap-sort/)

---

---

Sure! Let's break this into the required parts:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🎯 Problem:

You are given an array `arr[]`. You need to sort it using **Heap Sort**.

### 🧠 Heap Sort Concept:

Heap Sort works in **two major phases**:

1. **Build a Max Heap** from the input array.
2. **Extract the maximum element** from the heap one by one and place it at the end of the array (heap shrinking).

**Max Heap Property**: Each parent node is greater than or equal to its children.

### 🔍 Dry Run

Let's dry run `arr = [4, 1, 3, 9, 7]`.

#### Phase 1: Build Max Heap (Bottom-up)

We start from the last non-leaf node `i = n//2 - 1 = 1`:

* Heapify index 1 → `[4, 9, 3, 1, 7]` (9 swapped with 1)
* Heapify index 0 → `[9, 7, 3, 1, 4]` (9 bubble to root)

**Heap built**: `[9, 7, 3, 1, 4]`

#### Phase 2: Sort by Extracting Max

1. Swap `arr[0]` with `arr[4]` → `[4, 7, 3, 1, 9]`
   Heapify(0, size=4) → `[7, 4, 3, 1, 9]`

2. Swap `arr[0]` with `arr[3]` → `[1, 4, 3, 7, 9]`
   Heapify(0, size=3) → `[4, 1, 3, 7, 9]`

3. Swap `arr[0]` with `arr[2]` → `[3, 1, 4, 7, 9]`
   Heapify(0, size=2) → `[3, 1, 4, 7, 9]`

4. Swap `arr[0]` with `arr[1]` → `[1, 3, 4, 7, 9]`

**Final Sorted Array**: `[1, 3, 4, 7, 9]`

---

## ✅ 3. Optimized Python Code (Standard Interview Format)

```python
class Solution:
    def heapify(self, arr, n, i):
        # Maintain max heap property for subtree rooted at index i
        largest = i       # Initialize largest as root
        left = 2 * i + 1  # left child
        right = 2 * i + 2 # right child

        # If left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            self.heapify(arr, n, largest)  # Recursively heapify the affected subtree

    def heapSort(self, arr):
        n = len(arr)

        # Step 1: Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Step 2: One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)         # Heapify the reduced heap
```

---

## ✅ 4. Common Interview Questions & Answers

### Q1. **What is the time complexity of Heap Sort?**

* **Build Heap**: O(n)
* **Extract elements**: O(n log n)
* So, total time: **O(n log n)**

### Q2. **What is the space complexity?**

* In-place sort, so **O(1)** auxiliary space.

### Q3. **Is Heap Sort a stable sorting algorithm?**

* **No**, it is **not stable** (equal elements might change order).

### Q4. **What is the best case of Heap Sort?**

* Even best-case is **O(n log n)** unlike QuickSort which is O(n²) worst-case.

### Q5. **Where is Heap Sort used in real-world?**

* It is used where **memory usage matters**, or in **embedded systems**.
* Also used in **priority queues**, **schedulers**, **streaming k-largest elements**, etc.

---

---

Here is the **full program** for **Heap Sort** with **inline comments**, **input/output**, and **execution timing** using `timeit`.

---

### ✅ **Program: Heap Sort with Full Explanation**

```python
import timeit

class Solution:
    def heapify(self, arr, n, i):
        """
        Heapify subtree rooted at index i.
        Time Complexity: O(log n) per call
        Space Complexity: O(1)
        """
        largest = i           # Initialize largest as root
        left = 2 * i + 1      # Left child index
        right = 2 * i + 2     # Right child index

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        """
        Perform heap sort in-place.
        Time Complexity: O(n log n)
        Space Complexity: O(1) extra space
        """
        n = len(arr)

        # Step 1: Build max heap (bottom-up)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Step 2: Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Move max to end
            self.heapify(arr, i, 0)          # Heapify reduced heap

        return arr

# -------------------------------
# Main driver to test with input
# -------------------------------
def main():
    # Input array
    input_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Original Array:", input_array)

    # Create solution object
    sol = Solution()

    # Measure time taken for heap sort
    start_time = timeit.default_timer()
    sorted_array = sol.heapSort(input_array.copy())
    end_time = timeit.default_timer()

    # Print sorted result
    print("Sorted Array:", sorted_array)

    # Time taken
    print("Time Taken (seconds):", round(end_time - start_time, 6))

main()
```

---

### 🧠 Time and Space Complexity Breakdown

| Step                | Description                | Time Complexity                | Space Complexity |
| ------------------- | -------------------------- | ------------------------------ | ---------------- |
| Building Max Heap   | Bottom-up heapify          | O(n)                           | O(1)             |
| Heapify during sort | Re-heapify on each removal | O(log n) per item → O(n log n) | O(1)             |
| Total               | Heapify + Sort             | **O(n log n)**                 | **O(1)**         |

---

### ✅ Sample Output

```
Original Array: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Sorted Array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Time Taken (seconds): 0.000067
```

---

---

# 🌍 Real-World Use Cases

Here are a few **very important real-world use cases of Heap Sort** or **heap-based logic**, which are frequently discussed in interviews and seen in production systems:

---

### ✅ 1. **Priority Queue Implementation**

* **Use Case:** Scheduling systems (like OS job schedulers), Dijkstra’s shortest path, or task queues.
* **Why Heap:** A min-heap or max-heap allows efficient insertion and extraction of the highest/lowest priority task in **O(log n)** time.
* **Example:** Python’s `heapq` module uses a binary heap for priority queues.

---

### ✅ 2. **Top K Elements in a Stream**

* **Use Case:** Find the top 10 trending search queries or top K largest/smallest numbers in real-time from a massive data stream.
* **Why Heap:** A **min-heap of size K** helps maintain top K elements in **O(log K)** time per insertion.
* **Example:** Google Trends or YouTube's trending videos list.

---

### ✅ 3. **Median in a Data Stream**

* **Use Case:** Real-time analytics like computing the median of continuously incoming numbers (e.g., stock prices).
* **Why Heap:** Use **two heaps** (max-heap for left half and min-heap for right half) to get median in **O(1)** and maintain structure in **O(log n)**.
* **Example:** Financial platforms and telemetry monitoring systems.

---

### ✅ 4. **Heapsort in Memory-Constrained Environments**

* **Use Case:** Embedded systems or hardware-level sorting with strict space constraints.
* **Why Heap:** Heap sort is **in-place** and requires only **O(1)** extra space, unlike Merge Sort.
* **Example:** Sorting sensor data in IoT devices.

---

### ✅ 5. **Event Simulation Systems**

* **Use Case:** Handling events in simulation (e.g., traffic flow, CPU process scheduling).
* **Why Heap:** Maintain a **priority queue of upcoming events** sorted by time or priority.
* **Example:** Discrete event simulators, game engines.

---

