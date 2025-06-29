
---

## 🌀 Fast and Slow Pointers Pattern

### 🔍 What is it?

This pattern uses two pointers:

* **Slow pointer**: moves one step at a time.
* **Fast pointer**: moves two steps at a time.

By doing this, fast catches up to slow — this allows you to detect **cycles**, find **midpoints**, or identify **overlapping regions** efficiently.

---

### 🧠 Why use this pattern?

It’s commonly used for:

* **Cycle detection** in linked lists or arrays.
* **Finding the middle** of a list.
* **Partitioning logic** in problems involving traversal with different speeds.
* **Floyd's Tortoise and Hare Algorithm** (a classic example).

---

### 📌 Template (Pseudocode):

```python
slow, fast = 0, 0

while fast < len(array) and fast + 1 < len(array):
    slow += 1
    fast += 2
    
    if array[slow] == array[fast]:
        return True  # or process based on the problem
```

---

### 📘 Examples

#### 1. Find Middle of Linked List

Given a linked list, return its middle node.

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow  # middle node
```

#### 2. Detect Cycle in an Array

Given an array of jumps (positive/negative), detect if a cycle exists.

```python
slow = start_index
fast = start_index

while True:
    slow = arr[slow]
    fast = arr[arr[fast]]
    if slow == fast:
        return True
```


```python

FUNCTION fastAndSlow(dataStructure):
  # initialize pointers (or indices)
  fastPointer = dataStructure.start   # or 0 if the data structure is an array
  slowPointer = dataStructure.start   # or 0 if the data structure is an array
  
  WHILE fastPointer != null AND fastPointer.next != null: 
    # For arrays: WHILE fastPointer < dataStructure.length AND (fastPointer + 1) < dataStructure.length:
    
    slowPointer = slowPointer.next            
    # For arrays: slowPointer = slowPointer + 1
    
    fastPointer = fastPointer.next.next       
    # For arrays: fastPointer = fastPointer + 2
    
    IF fastPointer != null AND someCondition(fastPointer, slowPointer):
      # For arrays: use someCondition(dataStructure[fastPointer], dataStructure[slowPointer]) if needed
      handleCondition(fastPointer, slowPointer)
      BREAK

  # process the result
  processResult(slowPointer)
  # For arrays: processResult(slowPointer) might process dataStructure[slowPointer]

```
---

### ✅ When To Use:

Use Fast & Slow pointers if:

* The problem involves linear traversal with a **possibility of loops** or **middle elements**.
* It asks for meeting points, cycles, or repeated elements in dynamic progression.
* You need to compare values from different positions.

---

### 🌍 Real-World Applications:

* **Cycle detection** in linked data structures.
* **Slow/fast sync** mechanisms in security systems.
* **Multi-rate sampling**, signal processing.
* **Tortoise-Hare race** analogy for concurrency issues.

---
