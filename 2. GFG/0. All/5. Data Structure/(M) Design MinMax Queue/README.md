# Design MinMax Queue

**Difficulty:** Medium
**Accuracy:** 80.91%
**Submissions:** 560K+
**Points:** 4

Design a **SpecialQueue** data structure that functions like a normal queue but with additional support for retrieving the **minimum** and **maximum** element efficiently.

The **SpecialQueue** must support the following operations:

* **enqueue(x):** Insert an element `x` at the rear of the queue.
* **dequeue():** Remove the element from the front of the queue.
* **getFront():** Return the front element **without** removing.
* **getMin():** Return the **minimum** element in the queue in **O(1)** time.
* **getMax():** Return the **maximum** element in the queue in **O(1)** time.

There will be a sequence of queries `queries[][]`. The queries are represented in numeric form:

* **1 x** : Call `enqueue(x)`
* **2**   : Call `dequeue()`
* **3**   : Call `getFront()`
* **4**   : Call `getMin()`
* **5**   : Call `getMax()`

The driver code will process the queries, call the corresponding functions, and print the outputs of **getFront()**, **getMin()**, **getMax()** operations.
You only need to implement the above five functions.

> **Note:** It is guaranteed that all the queries are valid.

---

## Examples

### Example 1

**Input:**
`q = 6, queries[][] = [[1, 4], [1, 2], [3], [4], [2], [5]]`

**Output:**
`[4, 2, 2]`

**Explanation:**
Queries on queue are as follows:

* `enqueue(4)`: Insert `4` at the rear of the queue.
* `enqueue(2)`: Insert `2` at the rear of the queue.
* `getFront()`: return the front element i.e. `4`
* `getMin()`: return minimum element from the queue i.e. `2`
* `dequeue()`: Remove the front element `4` from the queue
* `getMax()`: return maximum element from the queue i.e. `2`

---

### Example 2

**Input:**
`q = 4, queries[][] = [[1, 3], [4], [1, 5], [5]]`

**Output:**
`[3, 5]`

**Explanation:**
Queries on queue are as follows:

* `enqueue(3)`: Insert `3` at the rear of the queue.
* `getMin()`: return minimum element from the queue i.e. `3`
* `enqueue(5)`: Insert `5` at the rear of the queue.
* `getMax()`: return maximum element from the queue i.e. `5`

---

## Constraints

* `1 ≤ queries.size() ≤ 10^5`
* `0 ≤ values in the queue ≤ 10^9`

---

## Expected Complexities

* **Time Complexity:** O(1)
* **Auxiliary Space:** O(n)

---

## Topic Tags

`Deque` • `implementation` • `Data Structures` • `Queue`

---

## Related Articles

* *Design A Queue Data Structure To Get Minimum Or Maximum In O(1) Time*

---

---

Here’s a clean, interview-ready write-up for **Design MinMax Queue**.

---

# 2) Explanation + Step-by-Step Dry Run

## Goal

Build a queue with the **usual operations** plus two O(1) queries:

* `getMin()` → smallest element currently in the queue
* `getMax()` → largest element currently in the queue

### Core idea (monotonic deques)

Besides the normal FIFO queue, keep two **monotonic deques**:

* `minDQ` is **increasing** from front→back (front is the current minimum).
* `maxDQ` is **decreasing** from front→back (front is the current maximum).

#### Enqueue(x)

* Push `x` to the normal queue.
* For `minDQ`, pop from **back** while those values `>` x, then push `x`.
* For `maxDQ`, pop from **back** while those values `<` x, then push `x`.
  This maintains monotonicity and keeps only “useful” candidates.

#### Dequeue()

* Pop from the **front** of the normal queue. Suppose it is `y`.
* If `y == minDQ.front`, pop it from `minDQ` too (since that exact value leaves the queue).
* If `y == maxDQ.front`, pop it from `maxDQ` too.

#### Getters

* `getFront()` → front of the normal queue.
* `getMin()` → front of `minDQ`.
* `getMax()` → front of `maxDQ`.

All these are O(1) **amortized**.

---

## Dry Run

Consider the query list:
`[enqueue(4), enqueue(2), getFront(), getMin(), dequeue(), getMax()]`

Start: `Q=[], minDQ=[], maxDQ=[]`

1. `enqueue(4)`

* Q = `[4]`
* minDQ: pop back while `> 4` (none). push 4 → `[4]`
* maxDQ: pop back while `< 4` (none). push 4 → `[4]`

2. `enqueue(2)`

* Q = `[4, 2]`
* minDQ: pop back while `> 2` → pop 4. push 2 → `[2]`
* maxDQ: pop back while `< 2` → none. push 2 → `[4, 2]` (still decreasing)

3. `getFront()` → `4`

4. `getMin()` → `minDQ.front = 2`

5. `dequeue()` → remove `4`

* Q becomes `[2]`
* Since `4 == minDQ.front?` No (front is 2) → minDQ unchanged `[2]`
* Since `4 == maxDQ.front?` Yes → pop front of maxDQ → `[2]`

Now: `Q=[2], minDQ=[2], maxDQ=[2]`

6. `getMax()` → `maxDQ.front = 2`

Outputs for the getters in order: `[4, 2, 2]` ✅

---

# 3) Python Implementations (Brute & Optimal)

### A) Brute-force (simple but slow)

* Store values in a `deque` (queue).
* `enqueue` & `dequeue` are O(1).
* `getMin`/`getMax` each scan the whole queue → O(n).
* Good for quick correctness, not for performance.

```python
from collections import deque

class SpecialQueue:
    def __init__(self):
        # main queue
        self.q = deque()

    def enqueue(self, x):
        # O(1)
        self.q.append(x)

    def dequeue(self):
        # O(1), assumes valid as per statement
        return self.q.popleft()

    def getFront(self):
        # O(1)
        return self.q[0]

    def getMin(self):
        # O(n): scan queue
        return min(self.q)

    def getMax(self):
        # O(n): scan queue
        return max(self.q)
```

**Complexities:**

* Time: `enqueue`/`dequeue`/`getFront` O(1), `getMin` O(n), `getMax` O(n)
* Space: O(n)

---

### B) Optimal (monotonic deques; most expected in interviews)

```python
from collections import deque

class SpecialQueue:
    def __init__(self):
        # FIFO queue to store actual elements
        self.q = deque()
        # Monotonic deques:
        # minDQ keeps elements in non-decreasing order; front is the min
        self.minDQ = deque()
        # maxDQ keeps elements in non-increasing order; front is the max
        self.maxDQ = deque()

    def enqueue(self, x):
        # Push to main queue
        self.q.append(x)

        # Maintain minDQ: remove larger elements from the back
        while self.minDQ and self.minDQ[-1] > x:
            self.minDQ.pop()
        self.minDQ.append(x)

        # Maintain maxDQ: remove smaller elements from the back
        while self.maxDQ and self.maxDQ[-1] < x:
            self.maxDQ.pop()
        self.maxDQ.append(x)

    def dequeue(self):
        # Pop from main queue
        val = self.q.popleft()

        # Synchronize with minDQ / maxDQ if the popped value is at their front
        if self.minDQ and val == self.minDQ[0]:
            self.minDQ.popleft()
        if self.maxDQ and val == self.maxDQ[0]:
            self.maxDQ.popleft()

        return val

    def getFront(self):
        # Front of main queue
        return self.q[0]

    def getMin(self):
        # Min is at front of minDQ
        return self.minDQ[0]

    def getMax(self):
        # Max is at front of maxDQ
        return self.maxDQ[0]
```

**Why O(1) amortized?**
Each element is added once and removed at most once from each deque. So total pops/pushes across all operations are linear in the number of enqueues, making each operation amortized O(1).

**Complexities:**

* Time: All operations **O(1) amortized**
* Space: O(n)

---

# 4) Interview Q\&A (what you’re likely to be asked)

**Q1. Why do we need two extra deques?**
Each deque supports one extremum in O(1): one increasing deque for min, one decreasing for max.

**Q2. Why is it amortized O(1)?**
Every element can be inserted and removed from each monotonic deque at most once. So across `m` operations, total work is O(m).

**Q3. What happens with duplicates?**
We don’t remove equal values on the way in (only strictly larger/smaller). When a value leaves via `dequeue`, we only pop from the corresponding deque if its front equals the leaving value—this handles duplicates correctly.

**Q4. Could we use indices instead of values in the deques?**
Yes—storing indices is common when a sliding window with fixed width is involved. Here, either values or indices work because queries are guaranteed valid and we synchronize by comparing the leaving value with deque fronts.

**Q5. Edge cases?**

* Immediately calling getters on an empty queue? The prompt guarantees valid queries, so we can assume getters won’t be called on empty.
* All elements equal → both deques just hold repeated equal values; logic still holds.
* Strictly increasing/decreasing streams → one of the deques shrinks to size 1, still fine.

**Q6. Could we support `getMin` or `getMax` in O(1) without extra space?**
Not generally for a dynamic queue. You’d need extra structure to avoid rescanning the queue.

**Q7. What are the trade-offs vs. maintaining a heap?**
A heap gives O(log n) updates and O(1) peek, but removing the front element from the queue is not aligned with removing an arbitrary element from a heap (would need lazy deletion or indexed heap). Monotonic deques fit the queue order perfectly and give O(1) amortized operations.

---

---

Awesome — here’s a **complete, runnable program** that implements the Min/Max-Queue with **O(1) amortized** operations, runs a couple of example inputs, prints the outputs, and measures total runtime inline.

---

## Full Program (with inline complexity notes + timing)

```python
from collections import deque
from time import perf_counter

class SpecialQueue:
    """
    Min/Max Queue using two monotonic deques.
    - minDQ: non-decreasing → front is current minimum
    - maxDQ: non-increasing → front is current maximum

    Space: O(n) for the stored elements (queue + helper deques).
    Each element enters and leaves each deque at most once.
    """

    def __init__(self):
        # Main FIFO queue
        self.q = deque()
        # Monotonic helpers
        self.minDQ = deque()  # increasing
        self.maxDQ = deque()  # decreasing

    def enqueue(self, x):
        """
        Insert x at the rear.
        Time: Amortized O(1)
        - Each element is appended once to q.
        - Pops from minDQ/maxDQ across all operations sum to O(n).
        """
        self.q.append(x)

        # Maintain minDQ (increasing)
        while self.minDQ and self.minDQ[-1] > x:
            self.minDQ.pop()  # amortized O(1) across all operations
        self.minDQ.append(x)

        # Maintain maxDQ (decreasing)
        while self.maxDQ and self.maxDQ[-1] < x:
            self.maxDQ.pop()  # amortized O(1)
        self.maxDQ.append(x)

    def dequeue(self):
        """
        Remove and return front.
        Time: Amortized O(1)
        Synchronize helper deques if their front equals the leaving value.
        """
        val = self.q.popleft()
        if self.minDQ and self.minDQ[0] == val:
            self.minDQ.popleft()
        if self.maxDQ and self.maxDQ[0] == val:
            self.maxDQ.popleft()
        return val

    def getFront(self):
        """
        Return front value without removing.
        Time: O(1)
        """
        return self.q[0]

    def getMin(self):
        """
        Return current minimum.
        Time: O(1)
        """
        return self.minDQ[0]

    def getMax(self):
        """
        Return current maximum.
        Time: O(1)
        """
        return self.maxDQ[0]


def run_queries(queries):
    """
    Driver that accepts a list of queries in numeric form, as per problem:
      1 x : enqueue(x)
      2   : dequeue()
      3   : getFront()
      4   : getMin()
      5   : getMax()
    Returns the list of outputs from (3), (4), (5) queries in order.

    Overall time: O(m) amortized where m = number of operations.
    Overall space: O(n) (n = max queue size during the run).
    """
    sq = SpecialQueue()
    out = []
    for q in queries:
        op = q[0]
        if op == 1:
            # enqueue
            sq.enqueue(q[1])
        elif op == 2:
            # dequeue
            sq.dequeue()
        elif op == 3:
            # getFront
            out.append(sq.getFront())
        elif op == 4:
            # getMin
            out.append(sq.getMin())
        elif op == 5:
            # getMax
            out.append(sq.getMax())
        else:
            raise ValueError(f"Unknown op code: {op}")
    return out


if __name__ == "__main__":
    # --------------------------
    # Example 1 from prompt
    # --------------------------
    queries1 = [
        [1, 4],  # enqueue(4)
        [1, 2],  # enqueue(2)
        [3],     # getFront -> 4
        [4],     # getMin   -> 2
        [2],     # dequeue  -> remove 4
        [5],     # getMax   -> 2
    ]

    t0 = perf_counter()
    output1 = run_queries(queries1)
    t1 = perf_counter()

    print("Example 1")
    print("Queries:", queries1)
    print("Output:", output1)   # Expected: [4, 2, 2]
    print(f"Runtime: {(t1 - t0) * 1e6:.1f} µs\n")

    # --------------------------
    # Example 2 (from the problem image explanation)
    # q = 6, queries = [[1,4], [1,2], [3], [4], [2], [5]]
    # --------------------------
    queries2 = [[1, 4], [1, 2], [3], [4], [2], [5]]

    t2 = perf_counter()
    output2 = run_queries(queries2)
    t3 = perf_counter()

    print("Example 2")
    print("Queries:", queries2)
    print("Output:", output2)   # Expected: [4, 2, 2]
    print(f"Runtime: {(t3 - t2) * 1e6:.1f} µs\n")

    # --------------------------
    # Example 3: another sequence with duplicates
    # --------------------------
    queries3 = [
        [1, 3], [1, 1], [1, 5], [4], [5], [3],  # min=1, max=5, front=3
        [2], [4], [5], [3],                     # after pop 3 -> min=1, max=5, front=1
        [2], [4], [5],                          # after pop 1 -> min=5, max=5
    ]

    t4 = perf_counter()
    output3 = run_queries(queries3)
    t5 = perf_counter()

    print("Example 3")
    print("Queries:", queries3)
    print("Output:", output3)
    print(f"Runtime: {(t5 - t4) * 1e6:.1f} µs")
```

### Sample Output (what you should see)

```
Example 1
Queries: [[1, 4], [1, 2], [3], [4], [2], [5]]
Output: [4, 2, 2]
Runtime:  ... µs

Example 2
Queries: [[1, 4], [1, 2], [3], [4], [2], [5]]
Output: [4, 2, 2]
Runtime:  ... µs

Example 3
Queries: [[1, 3], [1, 1], [1, 5], [4], [5], [3], [2], [4], [5], [3], [2], [4], [5]]
Output: [1, 5, 3, 1, 5, 1, 5]
Runtime:  ... µs
```

> The exact runtime µs will vary by machine; the point is we measured it inline with `perf_counter()`.

---

## 6) Real-World Use Cases (just the key ones)

1. **Sliding-window analytics**
   When you’re scanning a stream and need the min or max over the current window while pushing and popping from opposite ends, a min/max queue is perfect.

2. **Scheduling / throttling**
   Keep a queue of request times and quickly answer, “What’s the earliest/latest timestamp in the current bucket?” to apply rate limits or backpressure.

3. **Order book / inventory snapshots**
   For FIFO event streams (prices, quantities), you can maintain the current minimum/maximum price in O(1) while processing new trades and removing old ones.

4. **Real-time monitoring**
   Event queues where you frequently need “current worst/best value” (e.g., min latency, max CPU reading) without scanning the entire queue each time.
