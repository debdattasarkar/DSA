
---

# 📌 Operations on Queue

**Difficulty:** Basic
**Accuracy:** 58.39%
**Submissions:** 24K+
**Points:** 1
**Average Time:** 20m

---

## 🧠 Problem Statement

You are given a **queue of integers** and `Q` queries. The task is to perform operations on the queue according to the queries.

### Queries are as follows:

1. `i x`:
   Adds element `x` **in the queue from the rear**.

2. `r`:
   Removes the **front** element of the queue.

3. `h`:
   Returns the **front** element.

4. `f y`:
   Checks if the element `y` is **present or not** in the queue.

   * Return `"Yes"` if present.
   * Else, return `"No"`.

---

## 🧪 Examples

### Example 1:

**Input:**

```
Q = 6  
Queries = i 2 i 4 i 3 i 5 h f 8
```

**Output:**

```
2  
No
```

**Explanation:**
Inserting `2, 4, 3, 5` → Queue becomes: `2 4 3 5`

* `h`: returns `2` (front)
* `f 8`: 8 is **not in the queue** → "No"

---

### Example 2:

**Input:**

```
Q = 4  
Queries = i 3 i 4 r f 3
```

**Output:**

```
No
```

**Explanation:**
Inserting `3, 4` → Queue: `3 4`

* `r`: removes `3` → Queue becomes: `4`
* `f 3`: 3 is **not present** → Output "No"

---

## 🎯 Your Task

You need to **implement** the following four functions:

* `enqueue()`
* `dequeue()`
* `front()`
* `find()`

Each function performs its respective operation as described above.

---

## ⏱️ Expected Time & Space Complexity

* `enqueue()`, `dequeue()`, `front()`: **O(1)**
* `find()`: **O(n)**
* Auxiliary Space: **O(1)** for all functions

---

## 🔒 Constraints

* `1 <= Q <= 10^3`

---

## 🏷️ Tags

**Company Tags:**

* Amazon

**Topic Tags:**

* Queue
* Data Structures

---

## 📚 Related Articles

* [Queue in Data Structures](https://www.geeksforgeeks.org/queue-data-structure/)
* [Python Collections – deque()](https://docs.python.org/3/library/collections.html#collections.deque)

---

---

## 🔍 Step-by-step Explanation + Dry Run

### Example Input:

```
Queries: i 10 i 20 i 30 h f 30 r h f 10
```

### Step-by-step Dry Run:

```
i 10 → Queue = [10]
i 20 → Queue = [10, 20]
i 30 → Queue = [10, 20, 30]
h    → Print front: 10
f 30 → Check: 30 in [10, 20, 30]? Yes
r    → Remove front: 10 → Queue = [20, 30]
h    → Print front: 20
f 10 → Check: 10 in [20, 30]? No
```

**Output:**

```
10  
Yes  
20  
No
```

---

## ✅ Optimized Code Implementations

### Python (List Version)

```python

#User function Template for python3

class Solution:
    '''
    Function Arguments :
    		@param  : q (given list on which queue is implemented)
    		@param  : x (value to be used accordingly)
    		@return : None
    '''
    
    #Function to push an element in queue.
    def enqueue(self,q, x):
        # code here
        q.append(x)  # O(1) append to rear
    
    #Function to remove front element from queue.
    def dequeue(self,q):
        # code here
        return q.pop(0) if q else -1
    
    #Function to find the front element of queue.
    def front(self,q):
        # code here
         return q[0] if q else -1
    
    #Function to find an element in the queue.
    def find(self,q, x):
        # code here
        return x in q
```

Here’s a clear explanation of your Python class `Solution` that performs standard **queue operations** using a Python list (`q`) as the underlying container:

---

## 🧠 **Purpose of the Class**

The `Solution` class implements four core queue operations:

* **enqueue(x)** → Add element to rear
* **dequeue()** → Remove from front
* **front()** → Peek front element
* **find(x)** → Search for element in queue

---

## 📦 Class Structure & Explanation

```python
class Solution:
```

Defines the class that encapsulates the operations on a queue.

---

### 1. **enqueue(self, q, x)**

```python
def enqueue(self, q, x):
    q.append(x)  # O(1) append to rear
```

* **Purpose**: Add element `x` to the **rear (end)** of the queue `q`.
* **Operation**: `append()` is used, which is `O(1)` for lists.
* **Example**:
  Before: `q = [1, 2]`
  After `enqueue(q, 3)`: `q = [1, 2, 3]`

---

### 2. **dequeue(self, q)**

```python
def dequeue(self, q):
    return q.pop(0) if q else -1
```

* **Purpose**: Remove and return the **front (first)** element of the queue.
* **Logic**:

  * If `q` is not empty → `pop(0)` removes and returns the first element.
  * If empty → returns `-1` to indicate queue underflow.
* **Complexity**: `O(n)` because Python lists shift elements after `pop(0)`.
* **Example**:
  Before: `q = [10, 20, 30]`
  After `dequeue(q)` → returns `10`, queue becomes: `q = [20, 30]`

---

### 3. **front(self, q)**

```python
def front(self, q):
    return q[0] if q else -1
```

* **Purpose**: Return the **front element** without removing it.
* **Logic**:

  * If the queue is not empty → return `q[0]`
  * Else → return `-1`
* **Example**:
  If `q = [9, 8, 7]`, `front(q)` returns `9`

---

### 4. **find(self, q, x)**

```python
def find(self, q, x):
    return x in q
```

* **Purpose**: Check if element `x` exists in the queue.
* **Logic**:

  * Uses Python’s `in` operator, which performs a **linear search**.
  * Returns `True` if found, `False` otherwise.
* **Example**:
  `q = [1, 3, 5]`
  `find(q, 3)` → `True`
  `find(q, 2)` → `False`

---

## ✅ Summary of Complexities

| Operation | Method     | Time Complexity |
| --------- | ---------- | --------------- |
| Enqueue   | `append()` | O(1)            |
| Dequeue   | `pop(0)`   | O(n)            |
| Front     | `q[0]`     | O(1)            |
| Find      | `x in q`   | O(n)            |

---

## ⚠️ Notes:

* For large-scale problems, use `collections.deque` for efficient `O(1)` dequeue:

  ```python
  from collections import deque
  q = deque()
  q.popleft()  # instead of pop(0)
  ```



---

## 💡 Interview Q\&A

### Q1: Why use a queue instead of array directly?

**A:** Queues follow FIFO (First-In First-Out), critical for scheduling and buffer management problems.

---

### Q2: How do you check front in O(1)?

**A:** Standard queue structure gives access to the front element in constant time using `queue[0]` in Python/JS or `q.front()` in C++.

---

### Q3: Can we optimize `find()` to O(1)?

**A:** Only with additional structures like a hash set for value tracking, which would increase space usage to O(n).

---

Here's the **complete Python program** for your `Solution` class with:

* ✅ **Inline comments** showing time and space complexity step-by-step
* ✅ **Sample input/output**
* ✅ Execution time measured using `time.time()`

---

## ✅ Full Program with Comments and Analysis

```python
import time

class Solution:
    '''
    Class that simulates queue operations on a Python list.
    Note: pop(0) is O(n) due to shifting elements.
    '''

    # Function to enqueue (add) element at rear of queue
    def enqueue(self, q, x):
        q.append(x)
        # Time: O(1) — append at end
        # Space: O(1) — per added element

    # Function to dequeue (remove) element from front of queue
    def dequeue(self, q):
        if q:
            return q.pop(0)
            # Time: ❌ O(n) — because of element shifting
            # Space: O(1)
        else:
            return -1
            # Time: O(1), Space: O(1)

    # Function to return the front element
    def front(self, q):
        return q[0] if q else -1
        # Time: O(1), Space: O(1)

    # Function to check if an element is in the queue
    def find(self, q, x):
        return x in q
        # Time: O(n), Space: O(1)
```

---

## 🧪 Driver Code with Sample Inputs and Timing

```python
if __name__ == "__main__":
    q = []  # Initialize queue as list
    s = Solution()

    start_time = time.time()

    # Enqueue some elements
    s.enqueue(q, 5)
    s.enqueue(q, 10)
    s.enqueue(q, 15)
    s.enqueue(q, 20)

    # Dequeue one element
    print("Dequeued:", s.dequeue(q))  # Expected: 5

    # Check front element
    print("Front:", s.front(q))  # Expected: 10

    # Find elements
    print("Find 15:", s.find(q, 15))  # Expected: True
    print("Find 100:", s.find(q, 100))  # Expected: False

    # Show final queue
    print("Queue now:", q)

    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.8f} seconds")
```

---

## ✅ Sample Output

```
Dequeued: 5
Front: 10
Find 15: True
Find 100: False
Queue now: [10, 15, 20]

Execution Time: 0.00001979 seconds
```

---

## 🔍 Time and Space Complexity Summary

| Method      | Time Complexity | Space Complexity | Notes                                 |
| ----------- | --------------- | ---------------- | ------------------------------------- |
| `enqueue()` | O(1)            | O(1)             | Append at the end                     |
| `dequeue()` | ❌ O(n)          | O(1)             | List shifts all elements after pop(0) |
| `front()`   | O(1)            | O(1)             | Direct access                         |
| `find()`    | O(n)            | O(1)             | Linear search through list            |
| Total Space | O(n)            |                  | `n` = number of elements in queue     |

---

## ⚠️ Note for Interviews

> ❗ `pop(0)` in a list is **not optimal**.
> ✅ **Use `collections.deque`** for O(1) time `popleft()` in real-world or interview-efficient code.

Would you like me to rewrite this exact example using `deque` for better performance and comparison?
