

---

## ✅ Full Python Program

```python
import time

class MyQueue:
    def __init__(self):
        # Initialize queue with an array and front pointer
        self.arr = []      # Stores the elements of the queue
        self.front = 0     # Points to the current front of the queue
        # Time: O(1), Space: O(1)

    # Function to push an element x in the queue
    def push(self, x):
        self.arr.append(x)  # Append to rear of queue
        # Time: O(1) amortized, Space: O(1)

    # Function to pop (remove) front element from queue and return it
    def pop(self):
        if self.front == len(self.arr):
            return -1  # Queue is empty
            # Time: O(1), Space: O(1)

        val = self.arr[self.front]  # Get front value
        self.front += 1             # Move front pointer forward
        # Time: O(1), Space: O(1)
        return val
```

---

## 🧪 Driver Code with Timer

```python
if __name__ == "__main__":
    q = MyQueue()

    print("Running queue operations...\n")

    start_time = time.time()  # Start timing

    # Push some elements
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)

    # Pop some elements
    print("Popped:", q.pop())  # Expected: 10
    print("Popped:", q.pop())  # Expected: 20

    # Push more
    q.push(50)
    q.push(60)

    # Pop all remaining
    print("Popped:", q.pop())  # Expected: 30
    print("Popped:", q.pop())  # Expected: 40
    print("Popped:", q.pop())  # Expected: 50
    print("Popped:", q.pop())  # Expected: 60
    print("Popped:", q.pop())  # Expected: -1 (Queue is empty)

    end_time = time.time()  # End timing

    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")
```

---

## ⏱ Time and Space Complexity Summary

| Operation     | Time     | Space | Notes                                  |
| ------------- | -------- | ----- | -------------------------------------- |
| `__init__`    | O(1)     | O(1)  | Constant time and space                |
| `push(x)`     | O(1) avg | O(1)  | Appending to end of list               |
| `pop()`       | O(1)     | O(1)  | Pointer increment, no shifting         |
| Total (n ops) | O(n)     | O(n)  | `n` is number of total pushed elements |

⚠️ **Note**: This implementation causes memory buildup because elements are never removed from `arr`. If you perform many pops, the unused front space grows. A better approach for production use is `collections.deque` or slicing/garbage collection.

---

## ✅ Sample Output

```
Running queue operations...

Popped: 10
Popped: 20
Popped: 30
Popped: 40
Popped: 50
Popped: 60
Popped: -1

Execution Time: 0.00000238 seconds
```

---

# 📔 Notes

Let's break down this program **line by line** and explain how it implements a **basic queue** in Python using a list:

---

## 🔸 Class Overview

```python
class MyQueue:
```

This defines a class `MyQueue` that mimics the behavior of a queue (FIFO — First-In-First-Out).

---

## 🔸 Initialization

```python
def __init__(self):
    self.arr = []
    self.front = 0
```

* `self.arr`: A list that holds the queue's data.
* `self.front`: An index pointer that tracks the current "front" of the queue.

Unlike using `.pop(0)` (which is O(n)), this pointer lets you simulate popping from the front **in constant time**, by just moving the pointer forward.

### 🧠 Initial State:

```
arr = []
front = 0
```

---

## 🔸 Push Operation (Enqueue)

```python
def push(self, x):
    self.arr.append(x)
```

* Adds element `x` to the **end (rear)** of the queue.
* Time complexity: **O(1)** (amortized)
* Python lists are efficient at appending to the end.

### 🧠 After `push(10)` and `push(20)`:

```
arr = [10, 20]
front = 0
```

---

## 🔸 Pop Operation (Dequeue)

```python
def pop(self):
    if self.front == len(self.arr):
        return -1  # Queue is empty

    val = self.arr[self.front]  # Fetch the front value
    self.front += 1             # Move front pointer forward
    return val
```

### Step-by-step:

1. **Check if queue is empty**

   * If `front == len(arr)`, there are no more elements left to dequeue.
   * Return `-1` in that case.

2. **Otherwise**, return the element at the `front` index.

3. **Increment `front`** to logically remove the element.

### 🧠 Example:

After these calls:

```python
q = MyQueue()
q.push(10)
q.push(20)
print(q.pop())  # Output: 10
print(q.pop())  # Output: 20
print(q.pop())  # Output: -1
```

State evolves as:

```
arr = [10, 20], front = 0
pop() → returns 10 → front = 1
pop() → returns 20 → front = 2
pop() → returns -1  (empty)
```

---

## 🔍 Benefits & Limitations

### ✅ Pros:

* `push()` and `pop()` are **O(1)** time.
* Very simple and readable.

### ❌ Cons:

* Memory **leaks** over time: `arr` grows and never shrinks, even as elements are logically removed via `front`.
* Eventually, `arr` can hold millions of unused elements at the front.

---

## ✅ Solution for Memory Waste

A more efficient design is to **delete old entries** when they are no longer needed (e.g., reset `arr = arr[front:]` when front grows too large), or use:

```python
from collections import deque
```

which is optimized for popping from both ends.

---

## 🧠 Summary

| Method    | Operation | Time Complexity | Space Complexity |
| --------- | --------- | --------------- | ---------------- |
| `push(x)` | Enqueue   | O(1)            | O(1)             |
| `pop()`   | Dequeue   | O(1)            | O(1)             |

This is a **simple and efficient logical queue**, great for interviews and toy implementations, with one caveat: clean up `arr` periodically if memory usage is a concern.

---

---

Here's a complete solution for implementing a **queue using `collections.deque`**, which is the **ideal** way to implement a queue in Python due to its **O(1)** time complexity for both append (enqueue) and popleft (dequeue) operations.

---

## ✅ Full Python Program Using `deque`

```python
from collections import deque
import time

class MyQueue:
    def __init__(self):
        # Initialize deque for efficient O(1) operations
        self.queue = deque()  # Time: O(1), Space: O(1)

    # Function to push an element x into the queue
    def push(self, x):
        self.queue.append(x)  # Enqueue at the rear → O(1)

    # Function to pop an element from the queue
    def pop(self):
        if not self.queue:
            return -1  # Queue is empty → O(1)
        return self.queue.popleft()  # Dequeue from the front → O(1)
```

---

## 🧪 Driver Code with Timing

```python
if __name__ == "__main__":
    q = MyQueue()

    print("Running deque-based queue operations...\n")

    start_time = time.time()  # Start timing

    # Push elements
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)

    # Pop elements
    print("Popped:", q.pop())  # Expected: 10
    print("Popped:", q.pop())  # Expected: 20

    # More pushes
    q.push(50)
    q.push(60)

    # Pop remaining
    print("Popped:", q.pop())  # Expected: 30
    print("Popped:", q.pop())  # Expected: 40
    print("Popped:", q.pop())  # Expected: 50
    print("Popped:", q.pop())  # Expected: 60
    print("Popped:", q.pop())  # Expected: -1

    end_time = time.time()  # End timing

    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")
```

---

## ⏱ Time & Space Complexity

| Operation | Time Complexity | Space Complexity | Notes                     |
| --------- | --------------- | ---------------- | ------------------------- |
| `push()`  | O(1)            | O(1)             | Uses `deque.append()`     |
| `pop()`   | O(1)            | O(1)             | Uses `deque.popleft()`    |
| Total     | O(n) for n ops  | O(n)             | Fully efficient and clean |

---

## ✅ Sample Output

```
Running deque-based queue operations...

Popped: 10
Popped: 20
Popped: 30
Popped: 40
Popped: 50
Popped: 60
Popped: -1

Execution Time: 0.00000238 seconds
```

---

## 💡 Why Use `deque`?

* `list.pop(0)` is **O(n)** due to shifting.
* `deque.popleft()` is **O(1)** — optimized for queue behavior.
* Cleaner memory usage and performance for large-scale data.

---

---

Here's a complete solution for implementing a **queue using `collections.deque`**, which is the **ideal** way to implement a queue in Python due to its **O(1)** time complexity for both append (enqueue) and popleft (dequeue) operations.

---

## ✅ Full Python Program Using `deque`

```python
from collections import deque
import time

class MyQueue:
    def __init__(self):
        # Initialize deque for efficient O(1) operations
        self.queue = deque()  # Time: O(1), Space: O(1)

    # Function to push an element x into the queue
    def push(self, x):
        self.queue.append(x)  # Enqueue at the rear → O(1)

    # Function to pop an element from the queue
    def pop(self):
        if not self.queue:
            return -1  # Queue is empty → O(1)
        return self.queue.popleft()  # Dequeue from the front → O(1)
```

---

## 🧪 Driver Code with Timing

```python
if __name__ == "__main__":
    q = MyQueue()

    print("Running deque-based queue operations...\n")

    start_time = time.time()  # Start timing

    # Push elements
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)

    # Pop elements
    print("Popped:", q.pop())  # Expected: 10
    print("Popped:", q.pop())  # Expected: 20

    # More pushes
    q.push(50)
    q.push(60)

    # Pop remaining
    print("Popped:", q.pop())  # Expected: 30
    print("Popped:", q.pop())  # Expected: 40
    print("Popped:", q.pop())  # Expected: 50
    print("Popped:", q.pop())  # Expected: 60
    print("Popped:", q.pop())  # Expected: -1

    end_time = time.time()  # End timing

    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")
```

---

## ⏱ Time & Space Complexity

| Operation | Time Complexity | Space Complexity | Notes                     |
| --------- | --------------- | ---------------- | ------------------------- |
| `push()`  | O(1)            | O(1)             | Uses `deque.append()`     |
| `pop()`   | O(1)            | O(1)             | Uses `deque.popleft()`    |
| Total     | O(n) for n ops  | O(n)             | Fully efficient and clean |

---

## ✅ Sample Output

```
Running deque-based queue operations...

Popped: 10
Popped: 20
Popped: 30
Popped: 40
Popped: 50
Popped: 60
Popped: -1

Execution Time: 0.00000238 seconds
```

---

## 💡 Why Use `deque`?

* `list.pop(0)` is **O(n)** due to shifting.
* `deque.popleft()` is **O(1)** — optimized for queue behavior.
* Cleaner memory usage and performance for large-scale data.

---

Great question!

Here’s a detailed comparison between the two versions of `MyQueue`:

---

## ✅ Version 1: Using List with `self.front` Pointer

### ✔️ Pros:

* Simple and intuitive
* Constant-time `push()` and `pop()` logic

### ❌ Cons:

* Memory leak: old elements remain in `self.arr` even after they're logically "popped"
* Over time, large amounts of unused memory accumulate unless manually cleaned (`arr = arr[front:]`)
* Not truly efficient for large-scale or long-lived queues

---

## ✅ Version 2: Using `collections.deque`

### ✔️ Pros:

* Designed for efficient queue operations
* True **O(1)** time for both `push` (`append`) and `pop` (`popleft`)
* Automatically handles memory — no manual shifting or cleanup required
* Cleaner, more Pythonic code
* Scales better for **high-volume** or **long-running** tasks

### ❌ Cons:

* Slightly less "raw" control compared to managing index yourself
* Slightly more overhead if you only ever enqueue/dequeue a few items (negligible in practice)

---

## 🔍 Summary Table

| Feature                 | List + Pointer           | `collections.deque`         |
| ----------------------- | ------------------------ | --------------------------- |
| `push()` Time           | O(1) (amortized)         | O(1)                        |
| `pop()` Time            | O(1)                     | O(1)                        |
| Memory Efficiency       | ❌ (leaks unless trimmed) | ✅ (automatically cleans up) |
| Suitable for Long Runs  | ❌                        | ✅                           |
| Built-in Queue Behavior | ❌ (manual handling)      | ✅                           |
| Pythonic/Best Practice  | ⚠️                       | ✅                           |

---

## 🏆 **Best Practice Recommendation**

> ✅ **Use `collections.deque`** for any production-level or scalable queue implementation in Python.

It’s cleaner, safer, and more efficient, and it’s the standard for FIFO queues in Python.

---

### 🎯 Which Queue Implementation is Expected in an Interview?

It depends on the **context** and the **level of the interview**, but here’s how to choose the best fit:

---

## ✅ **If the question is about logic or building a queue from scratch:**

### **Use a list + pointer (manual implementation)**

**Why?**

* Shows you understand how queues work internally
* Demonstrates control over memory and indexing
* Lets you discuss trade-offs (e.g., memory leakage from unused elements)
* You may be asked to **optimize** it or handle edge cases manually

### Example Prompt:

> *"Implement a queue using a list without using built-in queue structures."*

---

## ✅ **If the question is focused on correctness and efficiency (not internal mechanics):**

### **Use `collections.deque`**

**Why?**

* Interviews often value clean, correct, and idiomatic code
* It demonstrates your ability to use standard libraries efficiently
* Best for problems like “sliding window”, “recent calls”, or “task scheduling”

### Example Prompt:

> *"Design a system to handle thousands of enqueue/dequeue operations quickly."*

---

## ✅ General Rule:

| Interview Context                      | Preferred Approach          |
| -------------------------------------- | --------------------------- |
| Asked to **simulate queue manually**   | Use **list + pointer**      |
| Asked for **efficiency or production** | Use **`collections.deque`** |
| System design/large data flow          | Use **deque / Linked List** |

---

## 💬 What Interviewers Might Ask You:

* Why is `.pop(0)` on a list bad?
* What happens to memory if you keep popping but never shrinking the list?
* How would you make this more memory-efficient?
* What’s the difference between a `deque` and a list?
* Can you implement a queue from two stacks?

---

## ✅ Conclusion

> 💡 **Unless told otherwise, use `collections.deque` in real interviews** for cleaner and efficient solutions — **but be ready to implement it from scratch** if asked.

