
---

# 🧮 Operations on Queue

**Difficulty:** Basic
**Accuracy:** 74.33%
**Submissions:** 370+
**Points:** 1

---

## 🔹 Problem Statement

Given a queue of **integers** and **Q** queries, the task is to perform operations on the queue according to the query.

---

## 🔸 Query Types

* `i x` : **adds element `x`** in the queue from rear.
* `r`   : **removes** the **front** element of the queue.
* `h`   : **returns** the **front** element.
* `f y` : **checks if element `y` is present** or not in the queue.
  Return **`true`** if present, else **`false`**.

---

> **Note:** You need to complete the functions `enqueue()`, `dequeue()`, `front()` and `find()` which perform the operations described above.

---

## 🔍 Examples

### Example 1:

```
Input:
Q = 6,
Queries = [[i, 2], [i, 4], [i, 3], [i, 5], [h], [f, 8]]

Output:
2
false

Explanation:
After inserting 2, 4, 3, and 5, the front element (h) is 2.
The element 8 is not in the queue, so the find operation (f, 8) returns false.
```

---

### Example 2:

```
Input:
Q = 4,
Queries = [[i, 3], [i, 4], [r], [f, 3]]

Output:
false

Explanation:
After inserting 3 and 4, removing the front element (r) leaves 4 in the queue.
The element 3 is not in the queue, so the find operation (f, 3) returns false.
```

---

## 📌 Constraints

```
1 ≤ Q ≤ 10³
```

---

## 🏢 Company Tags

* Amazon

---

## 🏷️ Topic Tags

* Queue
* Data Structures

---

---

### 🧠 Step-by-Step Dry Run

For:

```
Q = 6  
Queries = [[i, 2], [i, 4], [i, 3], [i, 5], [h], [f, 8]]
```

Steps:

* i 2 → queue = \[2]
* i 4 → queue = \[2, 4]
* i 3 → queue = \[2, 4, 3]
* i 5 → queue = \[2, 4, 3, 5]
* h   → output = 2 (front of queue)
* f 8 → 8 not in queue → output = false

---

## ✅ Optimized Implementations

### ✅ Python (using list)

```python
class Solution:
    def enqueue(self, q, x):
        q.append(x)  # O(1) insert at rear

    def dequeue(self, q):
        return q.pop(0) if q else -1  # O(n) pop front

    def front(self, q):
        return q[0] if q else -1  # O(1)

    def find(self, q, x):
        return x in q  # O(n)
```

### ✅ Python (optimized with deque)

```python
from collections import deque

class Solution:
    def enqueue(self, q, x):
        q.append(x)  # O(1)

    def dequeue(self, q):
        return q.popleft() if q else -1  # O(1)

    def front(self, q):
        return q[0] if q else -1  # O(1)

    def find(self, q, x):
        return x in q  # O(n)
```

---

### ✅ C++

```cpp
class Solution {
  public:
    void enqueue(queue<int> &q, int x) {
        q.push(x);  // O(1)
    }

    void dequeue(queue<int> &q) {
        if (!q.empty()) q.pop();  // O(1)
    }

    int front(queue<int> &q) {
        return q.empty() ? -1 : q.front();  // O(1)
    }

    bool find(queue<int> q, int y) {
        while (!q.empty()) {
            if (q.front() == y) return true;
            q.pop();
        }
        return false;  // O(n)
    }
};
```

---

### ✅ JavaScript

```javascript
class Solution {
    enqueue(queue, x) {
        queue.push(x); // O(1)
    }

    dequeue(queue) {
        return queue.length > 0 ? queue.shift() : -1; // O(n) due to shift
    }

    front(queue) {
        return queue.length > 0 ? queue[0] : -1;
    }

    find(queue, x) {
        return queue.includes(x); // O(n)
    }
}
```

---

## 💬 Interview FAQs

### Q1: Why use `deque` in Python over a list?

**A:** `list.pop(0)` is O(n), while `deque.popleft()` is O(1). For efficient queue operations, `collections.deque` is preferred.

---

### Q2: What's the time complexity of `.includes()` or `in` operator?

**A:** Both perform linear search: O(n).

---

### Q3: How can we make the `find` operation O(1)?

**A:** Use a hash set (`set()` in Python) to track all inserted values. However, it adds overhead and must be synchronized with the queue.

---

### Q4: What are edge cases to test?

* Operations on an empty queue (e.g., dequeue or front)
* Repeated elements (should still be found)
* Maximum number of operations (stress testing)

---

Here is a **detailed comparison** of the two Python implementations: one using a **list**, the other using **`collections.deque`**.

---

## 🔍 Comparison: `list` vs `deque`

| Operation         | `list` Implementation                         | `deque` Implementation          |
| ----------------- | --------------------------------------------- | ------------------------------- |
| `enqueue()`       | `O(1)` – uses `append()`                      | `O(1)` – uses `append()`        |
| `dequeue()`       | ❌ `O(n)` – uses `pop(0)`, shifts all elements | ✅ `O(1)` – uses `popleft()`     |
| `front()`         | `O(1)` – accesses first element               | `O(1)` – accesses first element |
| `find()`          | `O(n)` – scans list linearly                  | `O(n)` – scans deque linearly   |
| **Space**         | `O(n)` – stores queue as list                 | `O(n)` – stores queue as deque  |
| **Best Use Case** | When `dequeue` is rare                        | When queue ops are frequent     |

---

### 🔧 Time Complexity Summary

| Operation      | List   | Deque    |
| -------------- | ------ | -------- |
| Insert (rear)  | `O(1)` | `O(1)`   |
| Remove (front) | `O(n)` | `O(1)` ✅ |
| Access front   | `O(1)` | `O(1)`   |
| Find element   | `O(n)` | `O(n)`   |

---

### 🧠 Space Complexity

* Both use `O(n)` auxiliary space to store queue elements.
* `deque` has slightly more memory overhead due to internal double-ended structure, but it's negligible for typical use cases.

---

### 🧪 Verdict

| Criteria          | Winner                                             |
| ----------------- | -------------------------------------------------- |
| Performance       | ✅ **`deque`** (due to `O(1)` `popleft`)            |
| Simplicity        | `list` (built-in type, no import)                  |
| Industry-standard | ✅ **`deque`** (used in production code for queues) |

---

### ✅ Recommendation:

Always prefer **`collections.deque`** when implementing a queue in Python for **performance-critical** or **interview** scenarios.

Let's compare the two Python implementations based on their **time and space complexity** for each operation:

---

## ✅ Comparison Table: `list` vs `deque`

| Operation      | `list` Implementation    | `deque` Implementation   | Which is Better? |
| -------------- | ------------------------ | ------------------------ | ---------------- |
| **enqueue(x)** | `q.append(x)` → **O(1)** | `q.append(x)` → **O(1)** | ✅ **Equal**      |
| **dequeue()**  | `q.pop(0)` → **O(n)**    | `q.popleft()` → **O(1)** | ✅ **deque wins** |
| **front()**    | `q[0]` → **O(1)**        | `q[0]` → **O(1)**        | ✅ **Equal**      |
| **find(x)**    | `x in q` → **O(n)**      | `x in q` → **O(n)**      | ✅ **Equal**      |
| **Space**      | O(n) for queue contents  | O(n) for queue contents  | ✅ **Equal**      |

---

## ✅ Summary

### 🔴 Python `list` version:

* ❌ **Major drawback:** `pop(0)` is **O(n)** due to shifting elements
* 🔍 Acceptable for small input sizes or interview toy problems

### 🟢 Python `deque` version:

* ✅ All queue operations (`enqueue`, `dequeue`, `front`) are **O(1)**
* ✅ Best choice for production-level or performance-sensitive code

---

## 🏁 Recommendation

> **Always prefer `collections.deque`** for implementing queues in Python due to consistent **O(1)** time complexity for append and popleft operations, unlike Python lists which suffer from inefficient `pop(0)`.

---

Here is the **full Python program** that uses `collections.deque` for queue operations, with inline comments explaining the **time and space complexities**. It also includes example input and prints the output along with the **measured runtime** using `time.time()`.

---

### ✅ Full Program: Operations on Queue (with `deque`)

```python
import time
from collections import deque

# Start measuring execution time
start_time = time.time()

# Queue operations using deque for optimal performance
class Solution:
    def enqueue(self, q, x):
        # Time: O(1), Space: O(1)
        q.append(x)  # Add element to rear

    def dequeue(self, q):
        # Time: O(1), Space: O(1)
        return q.popleft() if q else -1  # Remove and return front

    def front(self, q):
        # Time: O(1), Space: O(1)
        return q[0] if q else -1  # Peek front

    def find(self, q, x):
        # Time: O(n), Space: O(1)
        return x in q  # Check presence of x

# Sample input
# Q = 6
queries = [("i", 2), ("i", 4), ("i", 3), ("i", 5), ("h",), ("f", 8)]
q = deque()
sol = Solution()

# Store results
outputs = []

# Process each query
for query in queries:
    if query[0] == "i":
        sol.enqueue(q, query[1])
    elif query[0] == "r":
        outputs.append(sol.dequeue(q))
    elif query[0] == "h":
        outputs.append(sol.front(q))
    elif query[0] == "f":
        outputs.append(sol.find(q, query[1]))

# Stop measuring time
end_time = time.time()

# Output results
print("Outputs:", outputs)
print(f"Total Runtime: {end_time - start_time:.6f} seconds")
```

---

### ✅ Sample Input:

```text
Queries = [("i", 2), ("i", 4), ("i", 3), ("i", 5), ("h",), ("f", 8)]
```

### ✅ Output:

```text
Outputs: [2, False]
Total Runtime: ~0.0005 seconds
```

---

### 📊 Complexity Summary:

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Enqueue   | O(1)            | O(1)             |
| Dequeue   | O(1)            | O(1)             |
| Front     | O(1)            | O(1)             |
| Find      | O(n)            | O(1)             |
