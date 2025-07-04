
---

## ✅ Full Program: Stack Using Two Queues (`queue.Queue`)

```python
from queue import Queue
import time

# Create two queues
queue_1 = Queue()  # Primary queue
queue_2 = Queue()  # Helper queue

def push(x):
    """
    Simulates stack push operation using two queues.
    """
    global queue_1, queue_2

    # Step 1: Push new element to queue_2
    queue_2.put(x)
    # Time: O(1), Space: O(1)

    # Step 2: Move all elements from queue_1 to queue_2
    while not queue_1.empty():
        queue_2.put(queue_1.get())
        # Time: O(n), Space: O(1) per move

    # Step 3: Swap queues
    queue_1, queue_2 = queue_2, queue_1
    # Time: O(1), Space: O(1)

def pop():
    """
    Simulates stack pop operation using queue_1.
    """
    global queue_1

    if queue_1.empty():
        return -1  # Stack is empty
        # Time: O(1), Space: O(1)

    return queue_1.get()
    # Time: O(1), Space: O(1)
```

---

## 🧪 Driver Code with Timer and Output

```python
if __name__ == "__main__":
    start_time = time.time()

    # Sample Input Sequence
    push(10)
    push(20)
    push(30)

    print("Popped:", pop())  # Expected: 30
    print("Popped:", pop())  # Expected: 20

    push(40)
    print("Popped:", pop())  # Expected: 40
    print("Popped:", pop())  # Expected: 10
    print("Popped:", pop())  # Expected: -1 (empty)

    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")
```

---

## ✅ Sample Output

```
Popped: 30
Popped: 20
Popped: 40
Popped: 10
Popped: -1

Execution Time: 0.00002956 seconds
```

---

## 🔍 Time and Space Complexity Summary

| Operation     | Time Complexity | Space Complexity | Notes                                    |
| ------------- | --------------- | ---------------- | ---------------------------------------- |
| `push(x)`     | ❗ O(n)          | O(n)             | Moves all old elements to preserve order |
| `pop()`       | ✅ O(1)          | O(1)             | Removes from front of `queue_1`          |
| `empty()`     | O(1)            | O(1)             | Used internally to check for underflow   |
| `Total Space` | O(n)            |                  | Due to queue storage                     |

---

## ⚠️ Interview Notes

* This is a **"Stack using two queues"** pattern.
* Two variations exist:

  1. **Costly push** (this one) → `push = O(n)`, `pop = O(1)`
  2. **Costly pop** → `push = O(1)`, `pop = O(n)`

> ✅ This version is often preferred for better pop performance.

---
