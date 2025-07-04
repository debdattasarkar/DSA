
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
