
---

# Stack using Two Queues

**Difficulty**: Easy
**Accuracy**: 51.4%
**Submissions**: 152K+
**Points**: 2
**Average Time**: 20m

---

## Problem Statement

Implement a **Stack** using **two queues** `q1` and `q2`.

---

## Examples

### Example 1:

**Input**:

```
push(2)
push(3)
pop()
push(4)
pop()
```

**Output**:

```
3 4
```

**Explanation**:

```
push(2) -> stack will be [2]
push(3) -> stack will be [2, 3]
pop()   -> popped element = 3, stack = [2]
push(4) -> stack = [2, 4]
pop()   -> popped element = 4
```

---

### Example 2:

**Input**:

```
push(2)
pop()
pop()
push(3)
```

**Output**:

```
2 -1
```

**Explanation**:

```
push(2) -> stack = [2]
pop()   -> popped element = 2
pop()   -> stack is empty, popped = -1
push(3) -> stack = [3]
```

---

## Constraints

* `1 <= Number of queries <= 100`
* `1 <= size of stack <= 100`

---

## Expected Complexities

* **Time Complexity**:

  * `O(n)` for `push()`
  * `O(1)` for `pop()`
  * *(or vice versa depending on the implementation)*

* **Auxiliary Space**:

  * `O(1)` for both `push()` and `pop()`.

---

## Company Tags

```
Accolite, Amazon, Microsoft, OYO Rooms, Snapdeal,
D-E-Shaw, Oracle, Adobe, Cisco, Grofers,
CouponDunia, Kritikal Solutions
```

---

## Topic Tags

```
Stack, Queue, Design-Pattern, Data Structures
```

---

## Related Articles

* [Implement Stack Using Queue](https://www.geeksforgeeks.org/implement-stack-using-queue/)

---

---

## ✅ 2. Optimized Code Implementations with Inline Comments

---

### ✅ Python (using two queues, push costly)

```python
'''
    :param x: value to be inserted
    :return: None
'''

from queue import Queue

queue_1 = Queue() # first queue
queue_2 = Queue() # second queue

def push(x):

    global queue_1
    global queue_2
    # code here
    
    # Step 1: Push new element into queue_2
    queue_2.put(x)  # Time: O(1), Space: O(1)

    # Step 2: Move all elements from queue_1 to queue_2
    while not queue_1.empty():
        queue_2.put(queue_1.get())  # Time: O(n), Space: O(1)

    # Step 3: Swap the queues
    queue_1, queue_2 = queue_2, queue_1  # Time: O(1), Space: O(1)

def pop():

    global queue_1
    global queue_2

    # code here
        # If queue_1 is empty, the stack is empty
    if queue_1.empty():
        return -1

    # The front of queue_1 is the top of the stack
    return queue_1.get()  # Time: O(1), Space: O(1)
```

---

### ✅ C++ (same logic, push costly)

```cpp
class QueueStack {
private:
    queue<int> q1, q2;
public:
    void push(int x) {
        // Time: O(n)
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    int pop() {
        // Time: O(1)
        if (q1.empty()) return -1;
        int top = q1.front();
        q1.pop();
        return top;
    }
};
```

---

### ✅ JavaScript

```javascript
class Queue {
    constructor() {
        this.arr = [];
        this.front = 0;
    }

    push(a) {
        this.arr.push(a);
    }

    pop() {
        if (this.arr.length != this.front)
            return this.arr[this.front++];
        return -1;
    }

    front_ele() {
        return this.arr[this.front];
    }

    empty() {
        return this.arr.length === this.front;
    }
}

class QueueStack {
    constructor() {
        this.q1 = new Queue();
        this.q2 = new Queue();
    }

    push(x) {
        // O(n)
        this.q2.push(x);
        while (!this.q1.empty()) {
            this.q2.push(this.q1.pop());
        }
        [this.q1, this.q2] = [this.q2, this.q1];
    }

    pop() {
        // O(1)
        return this.q1.pop();
    }
}
```

---

## ✅ 3. Expected Interview Questions & Answers

### Q1: Why are we using two queues?

**A:** To simulate the LIFO behavior of a stack using FIFO behavior of queues. One queue temporarily holds elements while the other maintains the stack order.

---

### Q2: Which operation is more expensive in your implementation?

**A:** Push operation is O(n) due to reordering, while pop is O(1). We can reverse the approach to make pop expensive if needed.

---

### Q3: What is the auxiliary space used?

**A:** O(1) extra space beyond the queues themselves. Just a few variables and swaps.

---

### Q4: Can this be done using one queue?

**A:** Yes, we can rotate elements within a single queue after each push to maintain stack order, but that’s a different variant.

---

Let's walk through the Python code you've shared, **line by line**, and explain how it implements a **Stack (LIFO)** using **two Queues (FIFO)** — specifically, using the **"Push Costly" strategy**.

---

### ✅ Import & Global Queues

```python
from queue import Queue

queue_1 = Queue()  # This queue will always hold the current stack (in order).
queue_2 = Queue()  # Temporary queue used only during push.
```

* We use two instances of `queue.Queue` from Python's standard library.
* `queue_1` will behave like the stack — top of the stack is at the front of this queue.
* `queue_2` is a helper used during the push operation.

---

### ✅ Push Operation (Costly)

```python
def push(x):
    global queue_1
    global queue_2
```

We declare `queue_1` and `queue_2` as `global` so we can modify them.

#### Step 1: Add the new element to `queue_2`

```python
queue_2.put(x)  # O(1)
```

* You start by placing the new element `x` into `queue_2`.
* This is because `queue_1` will be rebuilt with the new element on top.

#### Step 2: Move all elements from `queue_1` to `queue_2`

```python
while not queue_1.empty():
    queue_2.put(queue_1.get())  # O(n)
```

* This loop transfers all elements currently in `queue_1` (the existing stack) to `queue_2`, preserving the insertion order.
* This makes sure the newly pushed element (`x`) comes out **first** when popped.

#### Step 3: Swap the two queues

```python
queue_1, queue_2 = queue_2, queue_1  # O(1)
```

* After the transfer, `queue_2` now represents the updated stack with the new element on top.
* So we **swap** them: `queue_1` becomes the updated stack, and `queue_2` becomes empty again (ready for the next push).

---

### ✅ Pop Operation (Efficient)

```python
def pop():
    global queue_1
    global queue_2
```

Again, we refer to the global queues.

#### Step 1: Check for empty stack

```python
if queue_1.empty():
    return -1
```

* If `queue_1` is empty, that means the stack has no elements, so return `-1`.

#### Step 2: Return top of the stack

```python
return queue_1.get()  # O(1)
```

* The front of `queue_1` is always the **top of the stack** due to the rearrangement during push.
* So we simply `.get()` (dequeue) the front element — which simulates a stack pop.

---

### 🧠 Summary: Why It Works

#### What we're trying to simulate:

* **Stack:** LIFO (Last In First Out)
* **Queue:** FIFO (First In First Out)

To simulate LIFO using FIFO queues:

* During `push(x)`, we rearrange the queue so that the most recently pushed element (`x`) is **always at the front**.
* So that a simple `.get()` during `pop()` returns the correct element.

---

### 🕒 Time and Space Complexity

| Operation | Time | Space |
| --------- | ---- | ----- |
| `push(x)` | O(n) | O(1)  |
| `pop()`   | O(1) | O(1)  |

> `n` is the number of elements in the stack before push.

---

### ✅ Example Dry Run

#### Input:

```python
push(2)
push(3)
pop()
push(4)
pop()
```

#### Execution:

1. `push(2)`:

   * queue\_2: \[2]
   * move queue\_1 (empty) → queue\_2: \[2]
   * swap: queue\_1 = \[2]
2. `push(3)`:

   * queue\_2: \[3]
   * move queue\_1 (\[2]) → queue\_2: \[3, 2]
   * swap: queue\_1 = \[3, 2]
3. `pop()` → return `3`, now queue\_1 = \[2]
4. `push(4)`:

   * queue\_2: \[4]
   * move queue\_1 (\[2]) → queue\_2 = \[4, 2]
   * swap: queue\_1 = \[4, 2]
5. `pop()` → return `4`

✅ Output:

```
3
4
```

🧑🏻‍🤝‍👨🧑🏻‍🤝‍👨 The code is indeed using the `queue` module — specifically:

---

## ✅ How is the `queue` module used?

```python
from queue import Queue
```

This line imports Python’s **thread-safe FIFO queue** implementation from the `queue` module. Then you're using it to create two queue objects:

```python
queue_1 = Queue()  # first queue
queue_2 = Queue()  # second queue
```

These are instances of `queue.Queue`, **not** lists or `collections.deque`.

---

## ✅ What `Queue` is being used?

You're using:

```python
class queue.Queue(maxsize=0)
```

Which is:

* A **multi-producer, multi-consumer FIFO queue**
* **Thread-safe** (uses internal locking)
* **Blocking by default** (e.g., `.get()` will wait if the queue is empty unless specified otherwise)
* Not the most efficient for purely algorithmic/DSA uses

---

## 🛠 Functions used from `Queue`:

| Method          | Description                        |
| --------------- | ---------------------------------- |
| `queue.put(x)`  | Adds an item to the queue          |
| `queue.get()`   | Removes and returns the front item |
| `queue.empty()` | Returns `True` if queue is empty   |

---

## ❗ Important Note for DSA:

While `queue.Queue` works and is correct:

* It is **meant for multithreading**, not DSA/interview use.
* For **DSA and coding interviews**, it is better to use:

  * `collections.deque` for queues
  * `list` for stacks

---

## 🔁 In summary:

✅ **Yes**, the code uses the `queue` module by instantiating `Queue()` objects, and calling `.put()`, `.get()`, and `.empty()`.

---
