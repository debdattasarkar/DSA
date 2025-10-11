
---

## 🧩 What is `heapq`?

`heapq` is Python’s **heap queue** module — it implements a **binary heap** using a simple **list** under the hood.

By default, it is a **Min-Heap**, meaning:

> The smallest element is always at the front (`heap[0]`).

You can use it to efficiently get **min**, **max (with negation)**, **k smallest/largest**, or even simulate a **priority queue**.

---

## ⚙️ Importing heapq

```python
import heapq
```

---

## 📘 Core Functions (with examples and time complexities)

---

### 1️⃣ `heapq.heappush(heap, item)`

Add a new item to the heap while keeping it valid.

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print(heap)  # [2, 5, 8] → Min-Heap order
```

✅ **Time Complexity:** O(log n)
✅ **Space:** O(1) extra
Heap now automatically keeps smallest item at top (`heap[0] = 2`).

---

### 2️⃣ `heapq.heappop(heap)`

Remove and return the **smallest** item from the heap.

```python
smallest = heapq.heappop(heap)
print(smallest)  # 2
print(heap)      # [5, 8]
```

✅ **Time:** O(log n)
Removes the root, then re-heapifies.

---

### 3️⃣ `heapq.heappushpop(heap, item)`

Push a new item on the heap, then pop and return the smallest **in one atomic operation**.

```python
heap = [2, 5, 8]
result = heapq.heappushpop(heap, 1)
print(result)  # 1 (pushed 1, popped 1 since it's smallest)
print(heap)    # [2, 5, 8]
```

✅ **Time:** O(log n)
Faster than separate `heappush` + `heappop`.

---

### 4️⃣ `heapq.heapreplace(heap, item)`

Pop and return the smallest element, then push a new item.

```python
heap = [2, 5, 8]
result = heapq.heapreplace(heap, 10)
print(result)  # 2 (smallest popped)
print(heap)    # [5, 10, 8]
```

✅ **Time:** O(log n)
Note: `heapreplace` pops **even if new item is smaller**.

---

### 5️⃣ `heapq.heapify(x)`

Transform a list into a valid Min-Heap, **in-place**.

```python
arr = [9, 3, 7, 1, 8]
heapq.heapify(arr)
print(arr)  # [1, 3, 7, 9, 8] (heapified order)
```

✅ **Time:** O(n) — efficient bottom-up heap construction.
✅ **Space:** O(1)

---

### 6️⃣ `heapq.nsmallest(k, iterable)`

Get the **k smallest elements** efficiently.

```python
nums = [9, 3, 7, 1, 8]
print(heapq.nsmallest(3, nums))  # [1, 3, 7]
```

✅ **Time:** O(n log k)

---

### 7️⃣ `heapq.nlargest(k, iterable)`

Get the **k largest elements** efficiently.

```python
nums = [9, 3, 7, 1, 8]
print(heapq.nlargest(2, nums))  # [9, 8]
```

✅ **Time:** O(n log k)

---

## 💡 Important: Simulating a Max-Heap

`heapq` only supports **Min-Heap** natively.
To use it as a **Max-Heap**, you simply **store negative values**.

```python
nums = [5, 2, 8, 1]
max_heap = []

for n in nums:
    heapq.heappush(max_heap, -n)  # push negatives

print(-max_heap[0])  # 8 (max element)
heapq.heappop(max_heap)
print(-max_heap[0])  # 5 (next max)
```

✅ This trick is used in problems like “Kth Largest Element” or “Running Median”.

---

## ⚡ Typical DSA Use Cases

| Problem Type                     | Heap Function Used                          | Explanation                             |
| -------------------------------- | ------------------------------------------- | --------------------------------------- |
| **Kth smallest/largest element** | `heappush`, `heappop`, `nlargest/nsmallest` | Maintain a heap of size k               |
| **Merging k sorted lists**       | `heapq.merge()` or manual heap              | Always pick smallest current head       |
| **Top K frequent elements**      | `heapq.nlargest()`                          | Use frequency counts                    |
| **Streaming median**             | Two heaps (one max, one min)                | Efficiently balance halves              |
| **Priority scheduling**          | `heappush`/`heappop`                        | Process smallest deadline or cost first |

---

## ⚙️ Example – Find 3rd Smallest Using Heap

```python
import heapq

arr = [7, 10, 4, 3, 20, 15]
k = 3
heap = []

for num in arr:
    heapq.heappush(heap, -num)  # simulate max heap
    if len(heap) > k:
        heapq.heappop(heap)     # remove largest

print(-heap[0])  # 7 → 3rd smallest
```

✅ **Time:** O(n log k)
✅ **Space:** O(k)

---

## 🧠 Quick Memory Trick

| Action                     | Function                | Mnemonic                          |
| -------------------------- | ----------------------- | --------------------------------- |
| Insert into heap           | `heappush`              | “Push in”                         |
| Remove min                 | `heappop`               | “Pop min”                         |
| Create heap from list      | `heapify`               | “Make it a heap”                  |
| Get top k smallest/largest | `nsmallest`, `nlargest` | “n = number of elements you want” |

---
