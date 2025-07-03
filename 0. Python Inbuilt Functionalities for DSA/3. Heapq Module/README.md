Let's dive into the powerful heapq module, which is a must-know for priority queue problems in DSA and competitive programming.

---

## 📦 What is `heapq`?

The `heapq` module in Python provides a **min-heap** implementation using lists. It helps efficiently get the smallest (or largest with tricks) item in **O(log n)** time.

---

### ✅ Real-World DSA Use Cases:

1. Top-K elements
2. Kth smallest/largest
3. Merging sorted lists
4. Dijkstra’s shortest path
5. Median in a data stream

---

## 🔧 Core Functions in `heapq`

| Function                    | What It Does                      |
| --------------------------- | --------------------------------- |
| `heapq.heapify(list)`       | Converts list into a min-heap     |
| `heapq.heappush(heap, x)`   | Push `x` onto heap                |
| `heapq.heappop(heap)`       | Pop and return smallest element   |
| `heapq.heappushpop(heap,x)` | Push `x`, then pop and return min |
| `heapq.nlargest(k, list)`   | Get k largest elements            |
| `heapq.nsmallest(k, list)`  | Get k smallest elements           |

---

## ✅ Example 1: **Find K Smallest Elements**

### 📌 Problem:

> Given an array and an integer `k`, return the `k` smallest numbers.

### 🔢 Input:

```python
nums = [7, 10, 4, 3, 20, 15]
k = 3
```

### 🧠 Output:

```
[3, 4, 7]
```

---

### ✅ Code with Dry Run:

```python
import heapq

def k_smallest(nums, k):
    return heapq.nsmallest(k, nums)
```

### 🧪 Dry Run:

* Sorted: \[3, 4, 7, 10, 15, 20]
* First 3 = \[3, 4, 7]

---

## ✅ Example 2: **Find K Largest Elements**

```python
def k_largest(nums, k):
    return heapq.nlargest(k, nums)
```

🧪 `k_largest([7, 10, 4, 3, 20, 15], 3)` → `[20, 15, 10]`

---

## ✅ Example 3: **Kth Smallest Element**

### 🧠 Approach:

Build a min-heap and pop `k-1` elements.

```python
def kth_smallest(nums, k):
    heapq.heapify(nums)
    for _ in range(k - 1):
        heapq.heappop(nums)
    return heapq.heappop(nums)
```

🧪 For `[7, 10, 4, 3, 20, 15], k = 3`
Sorted: `[3, 4, 7, 10, 15, 20]` → 3rd = `7`

---

## ✅ Example 4: **Kth Largest Element**

Use **max-heap trick** with negatives:

```python
def kth_largest(nums, k):
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    return -heapq.heappop(max_heap)
```

🧪 For `[3, 2, 1, 5, 6, 4], k = 2` → Output = 5

---

## ✅ Example 5: **Merge K Sorted Lists**

```python
def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

🧪 Input:

```python
[[1,4,5],[1,3,4],[2,6]]
```

✅ Output:

```
[1,1,2,3,4,4,5,6]
```

---

## 🧠 Summary Table

| DSA Task                  | Technique           | Notes                        |
| ------------------------- | ------------------- | ---------------------------- |
| Top-K largest             | `heapq.nlargest()`  | Uses internal heap           |
| Kth smallest/largest      | `heapq.heapify()`   | Min-heap or negated max-heap |
| Merging sorted lists      | Tuple heaps         | Tracks source + value        |
| Sliding window max (heap) | Max-heap w/ cleanup | Less common than deque       |
| Dijkstra’s Algo           | `(dist, node)`      | Min-heap for shortest path   |

---
