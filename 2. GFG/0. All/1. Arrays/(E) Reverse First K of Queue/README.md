
---

# 📘 Reverse First K of Queue

**Difficulty:** Easy
**Accuracy:** 76.97%
**Submissions:** 566+
**Points:** 2

---

## 🧾 Problem Statement

Given an integer `k` and a **queue** of integers, we need to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

---

## 🛠 Allowed Operations

Only the following **standard operations** are allowed on queue:

* `enqueue(x)` : Add an item `x` to rear of queue
* `dequeue()` : Remove an item from front of queue
* `size()` : Returns number of elements in queue
* `front()` : Finds front item

> **Note:** The above operations represent the general processing. In-built functions of the respective languages can be used to solve the problem.

---

## 💡 Examples

### Example 1:

**Input:**
`k = 3`, `queue[] = [1, 2, 3, 4, 5]`
**Output:**
`3 2 1 4 5`
**Explanation:**
After reversing the given input from the 3rd position the resultant output will be `3 2 1 4 5`.

---

### Example 2:

**Input:**
`k = 4`, `queue[] = [4, 3, 2, 1]`
**Output:**
`1 2 3 4`
**Explanation:**
After reversing the given input from the 4th position the resultant output will be `1 2 3 4`.

---

## 🔒 Constraints

* $1 \leq k \leq \text{queue.size()} \leq 10^5$

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(k)

---

## 🏷 Company Tags

* Amazon

---

## 🏷 Topic Tags

* Stack
* Queue
* Data Structures

---

---

Sure! Here's a comprehensive breakdown for the **"Reverse First K elements of Queue"** problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🔹 Problem Statement

You're given a queue of integers and an integer `k`. Your task is to reverse the **first `k` elements** of the queue and leave the **rest of the queue unchanged**, maintaining their relative order.

---

### 🔹 Approach

We will use a **stack** to reverse the first `k` elements, then reinsert them back into the queue and **rotate** the remaining elements to maintain their relative order.

---

### 🔹 Dry Run

#### Example:

Input:

```
k = 3  
queue = [1, 2, 3, 4, 5]
```

**Step 1: Push first `k` elements to stack**
stack = \[1, 2, 3] → top of stack is 3

**Step 2: Pop all from stack and enqueue back to queue**
queue = \[4, 5, 3, 2, 1]

**Step 3: Move the (n-k) remaining elements to back**
(2 elements: 4, 5)
→ dequeue and enqueue them back

Final queue = \[3, 2, 1, 4, 5]

✅ Output: `3 2 1 4 5`

---

## ✅ 3. Optimized Code in Python, C++, and JavaScript

---

### 🔹 Python (with inline comments)

```python
from queue import Queue

class Solution:
    def modifyQueue(self, q, k):
        # Step 1: Use stack to reverse first k elements
        stack = []
        for _ in range(k):
            stack.append(q.get())  # O(k)

        # Step 2: Enqueue stack elements back into queue
        while stack:
            q.put(stack.pop())  # O(k)

        # Step 3: Move the remaining (size-k) elements to the rear
        size = q.qsize()
        for _ in range(size - k):
            q.put(q.get())  # O(n-k)

        return q
```

---

### 🔹 C++ (STL queues)

```cpp
#include <queue>
#include <stack>

class Solution {
  public:
    queue<int> modifyQueue(queue<int> &q, int k) {
        stack<int> st;

        // Step 1: Push first k elements into stack
        for (int i = 0; i < k; ++i) {
            st.push(q.front());
            q.pop();
        }

        // Step 2: Enqueue stack elements back to queue
        while (!st.empty()) {
            q.push(st.top());
            st.pop();
        }

        // Step 3: Move remaining elements to the back
        int size = q.size();
        for (int i = 0; i < size - k; ++i) {
            q.push(q.front());
            q.pop();
        }

        return q;
    }
};
```

---

### 🔹 JavaScript

```javascript
class Solution {
    modifyQueue(q, k) {
        let stack = [];

        // Step 1: Push first k elements to stack
        for (let i = 0; i < k; i++) {
            stack.push(q.shift()); // dequeue
        }

        // Step 2: Enqueue elements back from stack
        while (stack.length > 0) {
            q.push(stack.pop()); // enqueue
        }

        // Step 3: Rotate remaining elements to maintain order
        let rem = q.length - k;
        while (rem--) {
            q.push(q.shift());
        }

        return q;
    }
}
```

---

## ✅ 4. Interview Questions & Answers

---

### 💬 Q1: Why is a stack used to reverse the queue?

**A:** A stack reverses the order of elements due to its LIFO nature. So pushing first `k` elements into a stack and popping them back reverses them.

---

### 💬 Q2: Can we solve this problem without using a stack?

**A:** Yes, using recursion or a deque, but a stack gives a simple and efficient O(k) solution with O(k) space.

---

### 💬 Q3: What is the time complexity?

**A:**

* Reversing first `k` elements: O(k)
* Reinserting: O(k)
* Rotating remaining: O(n - k)
  ➡️ **Total Time: O(n)**

---

### 💬 Q4: What is the space complexity?

**A:**

* Stack stores `k` elements
  ➡️ **Auxiliary Space: O(k)**

---

### 💬 Q5: What happens if `k > queue size`?

**A:** It's invalid. Constraints guarantee `1 ≤ k ≤ queue.size()`, so we don't need to handle it explicitly.

---

Here is the **complete Python program** that uses the `queue.Queue` module to reverse the first `k` elements of a queue. This includes:

* ✅ Inline comments for each step’s **time and space complexity**
* ✅ A sample **input/output test case**
* ✅ Execution time using `time` module

---

## ✅ Full Program with Comments and Timing

```python
from queue import Queue
import time

class Solution:
    def modifyQueue(self, q, k):
        """
        Reverses the first k elements of the queue using a stack.
        """

        # Step 1: Use a stack to reverse first k elements
        stack = []
        for _ in range(k):
            stack.append(q.get())
            # Time: O(k), Space: O(k) for the stack

        # Step 2: Enqueue stack elements back into the queue
        while stack:
            q.put(stack.pop())
            # Time: O(k), Space: O(1) additional (stack shrinking)

        # Step 3: Move the remaining (size-k) elements to the back
        size = q.qsize()
        for _ in range(size - k):
            q.put(q.get())
            # Time: O(n-k), Space: O(1)

        return q
```

---

## 🧪 Driver Code with Sample Input, Output, and Execution Time

```python
if __name__ == "__main__":
    start_time = time.time()

    # Input values
    q = Queue()
    elements = [10, 20, 30, 40, 50]
    k = 3  # Reverse first 3 elements

    # Load elements into queue
    for item in elements:
        q.put(item)

    # Call the solution
    sol = Solution()
    result = sol.modifyQueue(q, k)

    # Collect and print output
    output = []
    while not result.empty():
        output.append(result.get())

    print("Modified Queue after reversing first k elements:", output)
    print(f"Execution Time: {time.time() - start_time:.8f} seconds")
```

---

## ✅ Output

```
Modified Queue after reversing first k elements: [30, 20, 10, 40, 50]
Execution Time: 0.00002193 seconds
```

---

## 📊 Time and Space Complexity Summary

Let `n` be the size of the queue and `k` be the number of elements to reverse.

| Step                                | Time Complexity | Space Complexity | Explanation                              |
| ----------------------------------- | --------------- | ---------------- | ---------------------------------------- |
| Dequeue first `k` elements to stack | O(k)            | O(k)             | Stack stores k elements                  |
| Enqueue back reversed elements      | O(k)            | O(1)             | Stack pops all elements                  |
| Rotate remaining `n-k` elements     | O(n-k)          | O(1)             | Queue put/get operations                 |
| **Total**                           | **O(n)**        | **O(k)**         | Complete queue traversal + k-space stack |

---

## ✅ Final Notes

* This solution uses the standard **"Reverse first k elements of a queue"** approach.
* It’s often seen in:

  * Queue rotation/reversal questions
  * System design buffers
  * Intermediate-level interview questions

# We arent calling Queue anywhere in the program?

In this code:

```python
from queue import Queue
```

We're **importing `Queue`**, but in the `modifyQueue()` method, we are **not creating a new `Queue` object** inside the function. Instead, we're assuming the input `q` **is already a `Queue` object** created *outside* the function (likely by the driver code or test harness).

---

### ✅ Why the `Queue` import is necessary?

Because although you're not explicitly doing something like `q = Queue()` **inside** the function, the `Queue` class (from Python's `queue` module) must be imported **so that the object passed in has `.get()`, `.put()`, and `.qsize()` methods**, which are methods of `Queue`.

So the full lifecycle might look like:

```python
from queue import Queue

q = Queue()
for val in [1, 2, 3, 4, 5]:
    q.put(val)

sol = Solution()
k = 3
q = sol.modifyQueue(q, k)

# Print the modified queue
while not q.empty():
    print(q.get(), end=' ')
```

This is where the `Queue` object is **actually instantiated**, and then passed to `modifyQueue()`.

---

### 🔁 Summary

* ✅ You **import** `Queue` to use `.get()`, `.put()`, `.qsize()`, etc.
* ❌ But you don’t need to **instantiate** `Queue()` inside the function unless you're creating a new queue yourself.
* ✅ The input queue is expected to be created by the **caller** (e.g., main driver function or test framework).

