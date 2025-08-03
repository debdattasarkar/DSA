Here's the complete README conversion for the problem **Queue Using Array**:

---

# Queue Using Array

**Difficulty:** Basic
**Accuracy:** 47.24%
**Submissions:** 237K+
**Points:** 1
**Average Time:** 15m

---

## Problem Statement

Implement a Queue using an Array. Queries in the Queue are of the following type:

* **(i)** `1 x` → A query of this type means **pushing `x` into the queue**
* **(ii)** `2` → A query of this type means to **pop** an element from the queue and **print** the popped element. If the queue is empty then return **-1**

> You only need to implement the functions `push()` and `pop()`. The driver code will handle input/output.

---

## Examples

### Example 1:

**Input:**
Queries = `1 2 1 3 2 1 4 2`
**Output:**
`2 3`

**Explanation:**

```
For query 1 2 → Queue = {2}  
For query 1 3 → Queue = {2, 3}  
For query 2   → Popped = 2, Queue = {3}  
For query 1 4 → Queue = {3, 4}  
For query 2   → Popped = 3  
```

---

### Example 2:

**Input:**
Queries = `1 3 2 2 1 4`
**Output:**
`3 -1`

**Explanation:**

```
1 3 → Queue = {3}  
2   → Popped = 3, Queue = {}  
2   → Queue is empty → return -1  
1 4 → Queue = {4}  
```

---

### Example 3:

**Input:**
Queries = `1 3 2 2 1 3`
**Output:**
`3 -1`

**Explanation:**

```
1 3 → Queue = {3}  
2   → Popped = 3  
2   → Queue is empty → return -1  
1 3 → Queue = {3}  
```

---

## Constraints

* $1 \leq \text{{number of queries}} \leq 10^5$
* $0 \leq x \leq 10^5$

---

## Expected Complexities

* **Time Complexity:** O(1)
* **Auxiliary Space:** O(1)

---

## Company Tags

Amazon, Goldman Sachs

---

## Topic Tags

Arrays, Queue, Data Structures

---

## Related Articles

* [Array Implementation Of Queue Simple](https://www.geeksforgeeks.org/array-implementation-of-queue-simple/)
* [Introduction To Circular Queue](https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/)

---

---

Let's walk through the complete breakdown of the **"Queue Using Array"** problem:

---

## ✅ 2. Step-by-Step Text Explanation and Dry Run

### Problem Recap:

You're asked to implement a **queue** using an **array**. You must support two operations:

1. `1 x` → Push `x` into the queue
2. `2` → Pop an element from the queue. If the queue is empty, return `-1`.

---

### Step-by-Step Dry Run

Let’s walk through this query sequence:
**Queries = \[1 2, 1 3, 2, 1 4, 2]**

1. `1 2`: Push 2 → Queue becomes: `[2]`
2. `1 3`: Push 3 → Queue becomes: `[2, 3]`
3. `2`  : Pop front → Output: `2`, Queue becomes `[3]`
4. `1 4`: Push 4 → Queue becomes `[3, 4]`
5. `2`  : Pop front → Output: `3`, Queue becomes `[4]`

✅ Final Output: `2 3`

---

## ✅ 3. Optimized Interview-Ready Code

### Python (Using simple list with two pointers)

```python
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0

    # Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)  # Append to end of list (rear)

    # Function to pop an element from queue and return that element.
    def pop(self):
        if self.front == len(self.arr):
            return -1  # Queue is empty
        val = self.arr[self.front]  # Fetch the front value
        self.front += 1
        return val
```

---

### C++ (Fixed size array + front/rear pointers)

```cpp
class MyQueue {
private:
    int arr[100005];
    int front, rear;

public:
    MyQueue() {
        front = 0;
        rear = 0;
    }

    // Function to push an element x in a queue.
    void push(int x) {
        arr[rear++] = x;
    }

    // Function to pop an element from queue and return that element.
    int pop() {
        if (front == rear) return -1; // Empty
        return arr[front++];
    }
};
```

---

### JavaScript (with front/rear emulation)

```javascript
class MyQueue {
    constructor() {
        this.front = 0;
        this.rear = 0;
        this.arr = new Array(100005);
    }

    // Function to push an element x in a queue.
    push(x) {
        this.arr[this.rear++] = x;
    }

    // Function to pop an element from queue and return that element.
    pop() {
        if (this.front === this.rear) return -1;
        return this.arr[this.front++];
    }
}
```

---

## ✅ 4. Expected Interview Questions & Answers

### Q1: Why do we track `front` and `rear`?

**A:** `front` indicates where to pop from, and `rear` indicates where to push new elements. This simulates queue behavior with O(1) operations.

---

### Q2: Can we use `collections.deque` or `queue.Queue` in Python?

**A:** In real-world code, yes. But in interviews or low-level implementations, using raw arrays or lists shows understanding of core mechanics.

---

### Q3: What happens if we keep pushing and popping for a long time?

**A:** The array keeps growing even though older indices are unused. To prevent memory issues, we could periodically reset the array or use a circular queue.

---

### Q4: What's the time and space complexity?

**A:**

* Time: O(1) for `push()` and `pop()`
* Space: O(n), where `n` is the number of queries or elements

---

---

## 🎯 **Your Goal**

You need to implement a **queue** using an array where:

### 🔧 Operations:
1. **`1 x`** — Push `x` into the queue.
2. **`2`** — Pop the front element from the queue.
   - If the queue is empty, return `-1`.

You don’t return or print during `push(x)`  
You **return the value** during `pop()`.

---

## 🧪 Let's Walk Through an Example

### ✅ Input:
```plaintext
Queries = [1 2, 1 3, 2, 1 4, 2]
```

We'll simulate each step:

### Initial state:
```
Queue: []
```

---

### 🔹 Step 1: `1 2` → Push 2

```
Queue: [2]
Output: -
```

---

### 🔹 Step 2: `1 3` → Push 3

```
Queue: [2, 3]
Output: -
```

---

### 🔹 Step 3: `2` → Pop
- Front element is `2`, pop it.

```
Queue: [3]
Output: 2 ✅
```

---

### 🔹 Step 4: `1 4` → Push 4

```
Queue: [3, 4]
Output: -
```

---

### 🔹 Step 5: `2` → Pop
- Front element is `3`, pop it.

```
Queue: [4]
Output: 3 ✅
```

---

### Final Output:
```
2 3
```

---

## 🧠 What If Queue Is Empty?

### Input:
```plaintext
1 3, 2, 2
```

Steps:
```
Push 3 → [3]
Pop → 3
Pop → Queue is empty → return -1
```

### Output:
```
3 -1
```

---

## 📌 Visual Simulation (Text-Based)

| Step | Operation | Queue        | Output |
|------|-----------|--------------|--------|
| 1    | 1 2       | [2]          | -      |
| 2    | 1 3       | [2, 3]       | -      |
| 3    | 2         | [3]          | 2      |
| 4    | 1 4       | [3, 4]       | -      |
| 5    | 2         | [4]          | 3      |

---
You're tackling the classic **“Queue Using Array”** problem — one of the best exercises for understanding queue operations!

---

## ✅ **Problem Summary**

You need to implement:
- `push(x)` → Pushes `x` into the queue  
- `pop()` → Removes front element from the queue and returns it. If empty, return `-1`.

You'll receive a list of queries of two types:
1. `1 x` — enqueue `x`
2. `2` — dequeue (pop and return front)

---

## 🧪 Example:

### Input:
```
Queries = [1, 2, 1, 3, 2, 1, 4, 2]
```

### Output:
```
2 3
```

---

## 🧠 Time & Space Complexity

| Operation | Time | Space |
|-----------|------|--------|
| push(x)   | O(1) | O(1)   |
| pop()     | O(1) | O(1)   |

---

## 🐍 Python Code (Queue Using Array)

```python
class MyQueue:
    def __init__(self):
        self.q = []
        self.front = 0  # pointer to the front index (to simulate queue)

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if self.front == len(self.q):
            return -1
        val = self.q[self.front]
        self.front += 1
        return val
```

---

## 🧑‍💻 C++ Version (Efficient with Index Management)

```cpp
class MyQueue {
    int arr[100000];
    int frontIndex = 0;
    int rearIndex = 0;

public:
    void push(int x) {
        arr[rearIndex++] = x;
    }

    int pop() {
        if (frontIndex == rearIndex)
            return -1;
        return arr[frontIndex++];
    }
};
```

---

## 🌐 JavaScript Version

```javascript
class MyQueue {
    constructor() {
        this.q = [];
        this.front = 0;
    }

    push(x) {
        this.q.push(x);
    }

    pop() {
        if (this.front === this.q.length) return -1;
        return this.q[this.front++];
    }
}
```

---

## ✅ Efficient Notes:
- This array-based approach avoids shifting elements on every pop.
- `front` pointer simulates "removing" elements.

Would you like a visual walkthrough or animation showing the queue growing and shrinking in action?