
https://github.com/debdattasarkar/DSA/tree/master/3.%20LeetCode/(M)%20Merge%20Sorted%20Array

---

# 🧩 Merge and Sort

**Difficulty:** Basic
**Expected Time Complexity:** O(n log n + m log m)
**Expected Auxiliary Space:** O(n + m)

---

## 📝 Problem Statement

Given two arrays `arr1` and `arr2`, merge them and return a new array sorted in **ascending order** that **contains only unique elements**.

---

## ✅ Examples

### Example 1:

**Input:**
`arr1[] = [11, 1, 8]`
`arr2[] = [10, 11]`

**Output:**
`[1, 8, 10, 11]`

**Explanation:**
Merging arrays gives `[11, 1, 8, 10, 11]`, after removing duplicates and sorting: `[1, 8, 10, 11]`.

---

### Example 2:

**Input:**
`arr1[] = [7, 1, 5, 3, 9]`
`arr2[] = [8, 4, 3, 5, 2, 6]`

**Output:**
`[1, 2, 3, 4, 5, 6, 7, 8, 9]`

**Explanation:**
All elements from both arrays are merged, duplicates removed, and sorted.

---

## 🎯 Constraints

* `1 ≤ arr1.length, arr2.length ≤ 10^4`
* `1 ≤ arr1[i], arr2[i] ≤ 10^9`

---

## 🛠️ Approach

1. Combine both arrays.
2. Remove duplicates using a set.
3. Sort the result.
4. Return the final array.

---

## 💡 Tags

* Arrays
* Merge Sort
* Sorting
* Data Structures
* Algorithms

---

Here’s a complete **text explanation with dry run**, followed by implementations in **Python**, **C++**, and **JavaScript** with **inline comments**.

---

### 🔍 **Problem Understanding**

You are given **two arrays** `arr1` and `arr2`. Your task is to:

1. Merge the two arrays.
2. Remove **duplicate elements**.
3. Sort the final array in **ascending order**.
4. Return the resulting array.

---

### 🧠 Step-by-Step Explanation

Let’s walk through the example:

**Input:**

```
arr1 = [11, 1, 8]
arr2 = [10, 11]
```

#### Step 1: Merge both arrays

```
merged = [11, 1, 8, 10, 11]
```

#### Step 2: Remove duplicates

Convert to a set:

```
unique = {1, 8, 10, 11}
```

#### Step 3: Sort the set

```
sorted_unique = [1, 8, 10, 11]
```

#### Output:

```
[1, 8, 10, 11]
```

---

### ✅ Python Code

```python
# User function Template for python3
class Solution:
    def mergeNsort(self, arr, brr):
        # Step 1: Merge both arrays
        merged = arr + brr
        
        # Step 2: Remove duplicates using set
        unique = set(merged)
        
        # Step 3: Sort the result
        result = sorted(unique)
        
        return result
```

---

### ✅ C++ Code

```cpp
// User function Template for C++
class Solution {
  public:
    vector<int> mergeNsort(vector<int>& a, vector<int>& b) {
        // Step 1: Use set to remove duplicates
        set<int> mergedSet;
        
        // Step 2: Insert all elements from both arrays
        for (int val : a) mergedSet.insert(val);
        for (int val : b) mergedSet.insert(val);
        
        // Step 3: Convert set to vector
        vector<int> result(mergedSet.begin(), mergedSet.end());
        
        return result;
    }
};
```

---

### ✅ JavaScript Code

```javascript
// User function Template for javascript
class Solution {
    mergeNsort(arr1, arr2) {
        // Step 1: Merge arrays
        let merged = arr1.concat(arr2);
        
        // Step 2: Remove duplicates using Set
        let uniqueSet = new Set(merged);
        
        // Step 3: Convert Set to Array and sort it
        let result = Array.from(uniqueSet).sort((a, b) => a - b);
        
        return result;
    }
}
```

---

Here’s how to solve the **"Merge and Sort Unique Elements"** problem using a **min-heap** in Python, C++, and JavaScript with full inline comments and a step-by-step dry run.

---

## ✅ Step-by-Step Explanation (Heap-Based Approach)

We will:

1. Merge both arrays.
2. Use a **set** to remove duplicates.
3. Push all unique elements into a **min-heap**.
4. Pop from the heap to get elements in **ascending order**.

### 🧪 Dry Run

**Input:**

```text
arr1 = [11, 1, 8], arr2 = [10, 11]
```

* Merge: `[11, 1, 8, 10, 11]`
* Unique: `{1, 8, 10, 11}`
* Heapified: `[1, 8, 10, 11]` (min-heap orders smallest at top)
* Output: Pop all → `[1, 8, 10, 11]`

---

## ✅ Python Code (Using `heapq`)

```python
import heapq

class Solution:
    def mergeNsort(self, arr1, arr2):
        # Step 1: Combine both arrays
        combined = arr1 + arr2
        
        # Step 2: Remove duplicates using set
        unique = set(combined)
        
        # Step 3: Convert set to a list and heapify it
        heap = list(unique)
        heapq.heapify(heap)  # O(n)
        
        # Step 4: Pop elements in sorted order
        result = []
        while heap:
            result.append(heapq.heappop(heap))  # O(log n) per pop
        
        return result
```

---

## ✅ C++ Code (Using `priority_queue` with `set`)

```cpp
#include <vector>
#include <set>
#include <queue>

class Solution {
  public:
    vector<int> mergeNsort(vector<int>& a, vector<int>& b) {
        // Step 1: Merge and remove duplicates
        set<int> s(a.begin(), a.end());
        s.insert(b.begin(), b.end());
        
        // Step 2: Min heap using priority_queue with greater<>
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (int num : s) {
            minHeap.push(num);
        }
        
        // Step 3: Extract elements in sorted order
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top());
            minHeap.pop();
        }
        
        return result;
    }
};
```

---

## ✅ JavaScript Code (Using Min-Heap via `PriorityQueue` simulation)

JavaScript has no built-in priority queue, so we simulate it using sort.

```javascript
class Solution {
    mergeNsort(arr1, arr2) {
        // Step 1: Combine both arrays
        let combined = arr1.concat(arr2);

        // Step 2: Use a Set to remove duplicates
        let unique = new Set(combined);

        // Step 3: Convert to array and simulate min-heap using sort
        let heap = Array.from(unique).sort((a, b) => a - b);

        return heap;
    }
}
```

---

