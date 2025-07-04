
# Stack implementation using dynamic array (list)

---

## ✅ Full Python Program

```python
class MyStack:

    def __init__(self):
        # Stack is implemented using a list
        self.arr = []

    # Function to push an integer into the stack
    def push(self, data):
        self.arr.append(data)  # O(1) time — append to end of list

    # Function to remove and return the top element from the stack
    def pop(self):
        if not self.arr:
            return -1  # Special case: empty stack
        return self.arr.pop()  # O(1) time — removes last element
```

---

## 🧪 Driver Code

```python
if __name__ == "__main__":
    stack = MyStack()

    # Push elements
    print("Pushing 10")
    stack.push(10)
    print("Pushing 20")
    stack.push(20)
    print("Pushing 30")
    stack.push(30)

    # Pop elements
    print("Popped:", stack.pop())  # Expected: 30
    print("Popped:", stack.pop())  # Expected: 20
    print("Popped:", stack.pop())  # Expected: 10
    print("Popped:", stack.pop())  # Expected: -1 (empty stack)
```

---

## 🧠 Dry Run

### Actions:

```python
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()  → returns 30
stack.pop()  → returns 20
stack.pop()  → returns 10
stack.pop()  → returns -1 (stack empty)
```

### Stack State:

* Initial: `[]`
* After push(10): `[10]`
* After push(20): `[10, 20]`
* After push(30): `[10, 20, 30]`
* After pop(): `[10, 20]`
* After pop(): `[10]`
* After pop(): `[]`
* After pop(): still `[]`, return -1

---

## ⏱ Time & Space Complexity

| Operation | Time Complexity | Space Complexity | Notes                            |
| --------- | --------------- | ---------------- | -------------------------------- |
| `push()`  | O(1)            | O(1)             | append to list                   |
| `pop()`   | O(1)            | O(1)             | pop from end                     |
| Overall   | O(1) per op     | O(n) total       | `n` is number of elements stored |

---

## ✅ Output

```
Pushing 10
Pushing 20
Pushing 30
Popped: 30
Popped: 20
Popped: 10
Popped: -1
```

---

Here is the complete solution for **"Implement Stack using Array"** using both:

1. ✅ **List + pointer**
2. ✅ **`collections.deque`**

With:

* Inline comments
* Proper time and space complexity analysis
* A final **comparison table**

---

## ✅ 1. Solution Using List + Pointer

```python
class MyStack:
    def __init__(self):
        self.stack = []
        self.top = -1  # Points to the top of stack, -1 means empty
        # Time: O(1), Space: O(1)

    def push(self, x):
        self.stack.append(x)   # O(1)
        self.top += 1          # Update top pointer

    def pop(self):
        if self.top == -1:
            return -1          # Stack is empty
        val = self.stack.pop()  # O(1)
        self.top -= 1
        return val
```

---

## ✅ 2. Solution Using `collections.deque`

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()  # Use deque for O(1) append and pop

    def push(self, x):
        self.stack.append(x)  # Add to top of stack (right end)

    def pop(self):
        if not self.stack:
            return -1          # Stack is empty
        return self.stack.pop()  # Remove and return top element
```

---

## 🧪 Driver Code (Common to Both)

```python
if __name__ == "__main__":
    # Example input
    queries = [1, 2, 1, 3, 2, 1, 4, 2]  # Mixed push(2), push(3), pop(), push(4), pop()
    output = []

    stack = MyStack()

    i = 0
    while i < len(queries):
        if queries[i] == 1:
            i += 1
            stack.push(queries[i])
        elif queries[i] == 2:
            output.append(stack.pop())
        i += 1

    print("Output:", ', '.join(map(str, output)))
```

---

## ⏱ Time & Space Complexity Comparison

| Operation       | List + Pointer        | `collections.deque`   |
| --------------- | --------------------- | --------------------- |
| `push(x)`       | O(1)                  | O(1)                  |
| `pop()`         | O(1)                  | O(1)                  |
| Memory Overhead | Slight (manual `top`) | Slight (deque object) |
| Built-in Safety | ❌ Manual top check    | ✅ Handles empty check |
| Pythonic Code   | ⚠️ Verbose            | ✅ Clean & readable    |

---

## ✅ Which One to Use in Interviews?

| Scenario                           | Use                         |
| ---------------------------------- | --------------------------- |
| Asked to implement from scratch    | List + top pointer (manual) |
| Focused on clean, fast code        | `deque`                     |
| Limited operations (push/pop only) | Either is fine              |
| Asked to avoid libraries           | List + pointer              |

---

### Final Verdict:

> 🏆 **Use `deque`** if not restricted — it’s faster to write, clean, and has built-in handling.
> 🧠 **Be ready with list + pointer** logic if asked to build from first principles.

Here’s a complete **time and space complexity analysis** for your `MyStack` implementation using `collections.deque`:

---

## ⏱ Time Complexity

| Operation              | Method Used       | Time Complexity | Explanation                              |
| ---------------------- | ----------------- | --------------- | ---------------------------------------- |
| `push(x)`              | `deque.append(x)` | **O(1)**        | Appends to the end of deque              |
| `pop()`                | `deque.pop()`     | **O(1)**        | Pops from the end of deque               |
| Empty check (`if not`) | `deque` check     | **O(1)**        | `deque` supports fast length and boolean |

---

## 📦 Space Complexity

| Resource       | Space Complexity | Explanation                                             |
| -------------- | ---------------- | ------------------------------------------------------- |
| `self.stack`   | **O(n)**         | Where `n` is the number of elements in the stack        |
| Total overhead | **O(n)**         | Deque is memory-efficient but still stores all elements |

---

## ✅ Why is `deque` preferred?

* **Optimized for both ends**: `append()` and `pop()` on either side are O(1)
* **Avoids list's shifting cost** (like `pop(0)` in regular list)
* Clean, Pythonic, and used widely in **interview and production code**

---

## 🔍 Summary Table

| Feature              | Value                      |
| -------------------- | -------------------------- |
| Push time            | O(1)                       |
| Pop time             | O(1)                       |
| Space usage          | O(n)                       |
| Edge-case safety     | Built-in (empty check)     |
| Best for interviews? | ✅ Yes, unless custom asked |

---
