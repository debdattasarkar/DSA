
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
