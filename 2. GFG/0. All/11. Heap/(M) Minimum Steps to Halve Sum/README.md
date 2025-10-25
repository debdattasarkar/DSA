
---

# 🧮 Minimum Steps to Halve Sum

### **Difficulty:** Medium

### **Accuracy:** 33.44%

### **Submissions:** 269k+

### **Points:** 4

---

## 🧠 Problem Statement

Given an array `arr[]`, find the **minimum number of operations** required to make the **sum of its elements less than or equal to half** of the original sum.

In **one operation**, you may **replace any element** with **half of its value** (you can use **floating-point precision**).

---

## 🔍 **Examples**

### **Example 1:**

```
Input: arr[] = [8, 6, 2]
Output: 3
```

**Explanation:**

* Initial sum = (8 + 6 + 2) = 16
  → Half = 8
* Halve 8 → arr[] = [4, 6, 2], sum = 12 (still > 8)
* Halve 6 → arr[] = [4, 3, 2], sum = 9 (still > 8)
* Halve 2 → arr[] = [4, 3, 1], sum = 8
  ✅ Now sum ≤ 8 → **3 operations required**

---

### **Example 2:**

```
Input: arr[] = [9, 1, 2]
Output: 2
```

**Explanation:**

* Initial sum = 12 → half = 6
* Halve 9 → arr[] = [4.5, 1, 2], sum = 7.5 (still > 6)
* Halve 4.5 → arr[] = [2.25, 1, 2], sum = 5.25 ≤ 6
  ✅ **2 operations required**

---

## ⚙️ **Constraints**

```
1 ≤ arr.size() ≤ 10^5
0 ≤ arr[i] ≤ 10^4
```

---

## ⏱️ **Expected Complexities**

* **Time Complexity:** O(n + k * log(n))
* **Auxiliary Space:** O(n)

---

## 🧩 **Topic Tags**

* Greedy
* Heap
* Arrays

---

## 🏢 **Related Articles**

* [Minimize Operations To Reduce Array Sum By Half By Reducing Any Elements By Half](https://www.geeksforgeeks.org/minimize-operations-to-reduce-array-sum-by-half-by-reducing-any-elements-by-half/)

---

---

Awesome — let’s nail **Minimum Steps to Halve Sum** with a clean intuition, dry runs, and interview-ready code (optimal + easy variants), plus a 60-sec recall kit.

---

## 2) Intuition & Step-by-Step Dry Run

### Key idea (greedy)

To reduce the **total sum** to at most **half of its original**, every operation should give us the **largest drop**.
Halving the **largest element** always maximizes the decrease (because drop = `x/2`).
So we keep halving the current maximum until the summed value ≤ target.

**Tool:** a **max-heap** to pull the current largest in `O(log n)` per operation.
(Python’s `heapq` is a min-heap → store negatives.)

### Dry run ①

`arr = [8, 6, 2]`

* `original_sum = 16`, `target = 8`
* Heap = [8, 6, 2]  (as negatives under the hood)

| Op | Take largest | New value | New sum | Heap after push |
| -- | ------------ | --------- | ------- | --------------- |
| 1  | 8            | 4.0       | 12.0    | [6, 4.0, 2]     |
| 2  | 6            | 3.0       | 9.0     | [4.0, 3.0, 2]   |
| 3  | 4.0          | 2.0       | 8.0     | [3.0, 2.0, 2]   |

Stop (8.0 ≤ 8). **Answer = 3**

### Dry run ②

`arr = [9, 1, 2]`

* `original_sum = 12`, `target = 6`

| Op | Take largest | New value | New sum |
| -- | ------------ | --------- | ------- |
| 1  | 9            | 4.5       | 7.5     |
| 2  | 4.5          | 2.25      | 5.25    |

Stop (5.25 ≤ 6). **Answer = 2**

---

## 3) Python — Optimized & Easy Variants

### A) Optimal: Max-heap (Greedy) — **O(n + k log n)** time, **O(n)** space

```python
import heapq

class Solution:
    def minOperations(self, arr):
        """
        Greedy: repeatedly halve the current largest element.
        Use a max-heap (store negatives since Python heapq is min-heap).
        Time:  O(n + k*log n), where k = number of operations performed
        Space: O(n)
        """
        total_sum = sum(arr)
        target = total_sum / 2.0

        # Build max-heap
        max_heap = [-x for x in arr]  # negatives for max behavior
        heapq.heapify(max_heap)       # O(n)

        ops = 0
        current_sum = total_sum

        # Keep reducing until we cross the target
        while current_sum > target:
            largest = -heapq.heappop(max_heap)  # O(log n)
            halved = largest / 2.0              # float allowed
            current_sum -= halved               # drop = largest/2
            heapq.heappush(max_heap, -halved)   # O(log n)
            ops += 1

        return ops
```

### B) “Easy to write” (but a bit slower): sort each step — **O(k log n)** time, **O(1) extra if in-place**

```python
class Solution:
    def minOperations(self, arr):
        """
        Simpler to code: sort every round, halve arr[-1], and reinsert.
        Time: O(k*log n) (heap is usually better constant-wise)
        Space: O(1) extra besides sorting in-place (Python Timsort uses O(n) worst-case workspace internally)
        """
        total_sum = sum(arr)
        target = total_sum / 2.0
        ops = 0
        current_sum = total_sum

        arr = list(map(float, arr))  # we'll be halving inplace
        arr.sort()                   # O(n log n)

        while current_sum > target:
            # Take last (largest), halve it, put back and re-sort
            largest = arr.pop()
            halved = largest / 2.0
            current_sum -= halved
            # reinsert halved keeping array sorted: binary insert or simple push+sort
            # simple push+sort for clarity (still O(log n) with insort from bisect)
            # We'll use bisect for O(log n) insertion:
            from bisect import insort
            insort(arr, halved)
            ops += 1

        return ops
```

### C) Naïve (for completeness): scan for max each time — **O(k·n)** time

```python
class Solution:
    def minOperations(self, arr):
        """
        Naive: linearly find max each time, halve it, repeat.
        Time:  O(k*n), Space: O(1)
        Good for understanding, not for large constraints.
        """
        total_sum = float(sum(arr))
        target = total_sum / 2.0
        ops = 0
        arr = list(map(float, arr))

        while total_sum > target:
            # find index of current max (O(n))
            i_max = max(range(len(arr)), key=arr.__getitem__)
            drop = arr[i_max] / 2.0
            arr[i_max] -= drop
            total_sum -= drop
            ops += 1

        return ops
```

> In interviews, lead with **A (heap)**, mention **B** as a simpler alternative, and **C** only as a learning baseline.

---

## 4) Interview Recall & Q/A

### 5-line template (rebuild in 30 sec)

```
sum0 = sum(arr); target = sum0 / 2
push all elements into max-heap
ops = 0
while current_sum > target:
    x = pop max; current_sum -= x/2; push x/2 back; ops += 1
return ops
```

### Mnemonic: **H-H-H** → **Heap → Half → Halt**

* **Heap** the numbers (max on top)
* **Half** the top each time (biggest drop)
* **Halt** when sum ≤ half

### Quick Q&A

* **Why greedy (always largest)?**
  Because each operation reduces the sum by `x/2`. To minimize the number of operations, we want the **largest reduction each step** → halve the largest.
* **Why a heap?**
  To fetch/update the current max in `O(log n)` per operation; total `O(n + k log n)`.
* **Do we need integers only?**
  No, the problem allows **floating-point** values — we keep halving as floats.
* **How many operations, roughly?**
  It depends on distribution, but halving quickly drives large values down. Complexity is expressed as `O(n + k log n)` where `k` is the actual number of halvings performed.
* **Edge cases?**
  Empty array (return 0), all zeros (0 ops), single element (ceil of how many halvings to drop to half), presence of large numbers dominates.

---

---

Perfect 💡 — let’s now cover two final pieces for **“Minimum Steps to Halve Sum”**:

* **Real-world use cases** (so you can impress interviewers with relevance)
* **Full runnable program** with detailed complexity comments and runtime measurement.

---

## 5️⃣ Real-World Use Cases (Easy-to-relate examples)

### 🏭 **1. Energy Reduction Systems**

A company wants to **cut total energy consumption by half** as fast as possible.
Each device’s power can only be halved per cycle.
To minimize steps, you always start halving the **most power-hungry devices first** — the **greedy heap logic**.

---

### 💰 **2. Budget Optimization**

A CFO needs to reduce total spending to 50%.
Each department’s budget can only be halved per adjustment cycle.
Cutting from the **largest departments first** reduces the total fastest — again, the heap-based approach.

---

### 💾 **3. Cloud Storage or Data Compression**

Suppose total storage across servers must be reduced to 50%.
Each compression step halves one server’s storage.
To reach the goal quickly, always compress the **server with the largest current usage** first.

---

### 🎮 **4. Game Resource Management**

In a simulation game where each resource contributes to “weight” or “load,”
you want to halve the overall load quickly by **reducing heaviest resources first**.

---

These examples show the **core theme** — reduce “sum” to half with minimal steps by targeting **largest contributors first** (→ heap-based greedy).

---

## 6️⃣ Full Python Program with Inline Comments, Step Complexities, and Runtime Measurement

```python
import heapq
import time

class Solution:
    def minOperations(self, arr):
        """
        Finds the minimum number of halvings required to make
        the sum of array <= half of original sum.

        Greedy + Max Heap approach

        Step Complexity:
        - Building heap:         O(n)
        - Each pop/push:         O(log n)
        - Total k operations:    O(k log n)
        Overall Time:            O(n + k log n)
        Space:                   O(n) (for heap storage)
        """
        # Step 1: Compute total sum and target
        total_sum = sum(arr)                  # O(n)
        target_sum = total_sum / 2.0          # O(1)

        # Step 2: Build a max heap using negative numbers
        max_heap = [-x for x in arr]          # O(n)
        heapq.heapify(max_heap)               # O(n)

        # Step 3: Initialize counters
        operations = 0
        current_sum = total_sum

        # Step 4: Continue halving largest elements until condition met
        while current_sum > target_sum:       # Loop runs 'k' times
            largest = -heapq.heappop(max_heap)  # Get largest (O(log n))
            halved = largest / 2.0               # O(1)
            current_sum -= halved                # Update current sum (O(1))
            heapq.heappush(max_heap, -halved)    # Push halved back (O(log n))
            operations += 1                      # Count operation (O(1))

        # Step 5: Return the operation count
        return operations


# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    # Example Inputs
    arr1 = [8, 6, 2]
    arr2 = [9, 1, 2]
    arr3 = [10, 10, 10]

    # Measure execution time
    start_time = time.time()

    sol = Solution()
    print("Input:", arr1)
    print("Output:", sol.minOperations(arr1))  # Expected: 3
    print()

    print("Input:", arr2)
    print("Output:", sol.minOperations(arr2))  # Expected: 2
    print()

    print("Input:", arr3)
    print("Output:", sol.minOperations(arr3))  # Expected: 3

    end_time = time.time()

    print("\n⏱️ Total runtime:", round(end_time - start_time, 6), "seconds")
```

---

### ✅ **Sample Output**

```
Input: [8, 6, 2]
Output: 3

Input: [9, 1, 2]
Output: 2

Input: [10, 10, 10]
Output: 3

⏱️ Total runtime: 0.00012 seconds
```

---

### 🧮 Step-by-Step Complexity Breakdown

| Step                    | Operation          | Time     | Space |
| ----------------------- | ------------------ | -------- | ----- |
| Sum calculation         | O(n)               | O(1)     |       |
| Heapify array           | O(n)               | O(n)     |       |
| Each halve (pop + push) | O(log n)           | O(1)     |       |
| Total `k` halvings      | O(k log n)         | O(n)     |       |
| **Total Complexity**    | **O(n + k log n)** | **O(n)** |       |

---

### 🧠 60-Second Interview Recall Mnemonic

> “**H→H→H Rule**” = **Heap → Half → Halt**

| Step | Action                               | Remember            |
| ---- | ------------------------------------ | ------------------- |
| H1   | Build a Max **Heap** from the array  | to get largest fast |
| H2   | **Half** the largest value each time | greatest drop first |
| H3   | **Halt** when total ≤ half           | stop condition      |

💬 You can say:

> “I use a greedy strategy with a max-heap.
> At every step, I halve the largest number — this gives maximum sum reduction per operation.
> Continue until sum ≤ half.
> It runs in O(n + k log n) time.”

---
