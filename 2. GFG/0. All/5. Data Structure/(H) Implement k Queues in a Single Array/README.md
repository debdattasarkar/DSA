# Implement k Queues in a Single Array

**Difficulty:** Hard  
**Accuracy:** 46.06%  
**Submissions:** 844+  
**Points:** 8  

---

## Problem Statement

You are given two integers **n** and **k**. Your task is to implement a class **kQueues** that uses a **single array of size n** to simulate **k independent queues**.

The class should support the following operations:

- **enqueue(x, i)** → Adds the element **x** into the **i-th** queue.  
- **dequeue(i)** → Removes the **front** element from the **i-th** queue and returns it. Returns **-1** if the queue is empty.  
- **isEmpty(i)** → Returns **true** if **i-th** queue is empty, else return **false**.  
- **isFull()** → Returns **true** if the array is completely full and no more elements can be inserted, otherwise **false**.

There will be a sequence of **q queries** represented as:

- **1 x i** : Call `enqueue(x, i)`
- **2 i** : Call `dequeue(i)`
- **3 i** : Call `isEmpty(i)`
- **4** : Call `isFull()`

The driver code will process the queries, call the corresponding functions, and print the results of **dequeue**, **isEmpty**, and **isFull** operations.

You only need to implement the above four functions.

---

## Examples

### Example 1
**Input:**  
`n = 4, k = 2, q = 8,`  
`queries = [[1, 5, 0], [1, 3, 0], [1, 1, 1], [2, 0], [1, 4, 1], [1, 1, 0], [3, 1], [4]]`

**Output:**  
`[5, false, true]`

**Explanation:** Queries on the queue are as follows:  
- `enqueue(5, 0)` → `queue0 = [5]`  
- `enqueue(3, 0)` → `queue0 = [5, 3]`  
- `enqueue(1, 1)` → `queue1 = [1]`  
- `dequeue(0)` → returns `5`, `queue0 = [3]`  
- `enqueue(4, 1)` → `queue1 = [1, 4]`  
- `enqueue(1, 0)` → `queue0 = [3, 1]`  
- `isEmpty(1)` → `false`  
- `isFull()` → `true`  

---

### Example 2
**Input:**  
`n = 6, k = 3, q = 4,`  
`queries = [[1, 3, 2], [2, 0], [1, 2, 1], [3, 2]]`

**Output:**  
`[-1, false]`

**Explanation:** Queries on the queue are as follows:  
- `enqueue(3, 2)` → `queue2 = [3]`  
- `dequeue(0)` → `queue0` is empty, returns `-1`  
- `enqueue(2, 1)` → `queue1 = [2]`  
- `isEmpty(2)` → `false`  

---

## Expected Complexities

- **Time Complexity:** `O(1)`
- **Auxiliary Space:** `O(n + k)`

---

## Topic Tags

- Data Structures  
- Queue  

---

## Related Articles

- **Efficiently Implement K Queues Single Array**

---

---

## 2) Text explanation (core idea)

We must implement **k independent queues** inside **one array of size n**, supporting:

* `enqueue(x, i)`
* `dequeue(i)`
* `isEmpty(i)`
* `isFull()`

If we simply divide the array into `k` fixed parts, one queue can overflow even if other partitions are empty → **wastes space**.

### Interview-standard solution: “Free list” + linked-list inside array

We simulate linked lists using array indices.

Maintain these arrays:

1. `data[n]`
   Stores actual values.

2. `next_index[n]`
   Works like “next pointer” for each slot (like a linked list node).

3. `front[k]`, `rear[k]`
   For each queue `i`, store indices of front and rear node in `data[]`.

4. `free_head`
   Head index of a linked list of free slots.

#### Initialization

* All slots are free initially.
* Link them: `0 -> 1 -> 2 -> ... -> n-1 -> -1`
* `free_head = 0`
* `front[i] = rear[i] = -1` for all queues

#### Enqueue(x, i)

1. If `free_head == -1` → array full → cannot insert.
2. Take a free slot: `new_idx = free_head`
3. Move `free_head = next_index[new_idx]`
4. Store value: `data[new_idx] = x`
5. Set `next_index[new_idx] = -1` (it becomes tail node)
6. If queue `i` empty: `front[i] = rear[i] = new_idx`
   else link old rear: `next_index[rear[i]] = new_idx`, update `rear[i] = new_idx`

#### Dequeue(i)

1. If `front[i] == -1` → empty → return `-1`
2. Remove front: `idx = front[i]`
3. Update `front[i] = next_index[idx]`
4. If front becomes `-1`, set `rear[i] = -1` as well
5. Add removed slot back to free list:

   * `next_index[idx] = free_head`
   * `free_head = idx`
6. Return `data[idx]`

✅ All operations are **O(1)**.

---

## Step-by-step dry run (Example 1)

`n=4, k=2`
Queries:
`enqueue(5,0), enqueue(3,0), enqueue(1,1), dequeue(0), enqueue(4,1), enqueue(1,0), isEmpty(1), isFull()`

### Init

* `free_head = 0`
* `next = [1,2,3,-1]`
* `front = [-1,-1]`, `rear = [-1,-1]`

### 1) enqueue(5,0)

* new=0, free_head=1
* data[0]=5, next[0]=-1
* queue0: front[0]=rear[0]=0

### 2) enqueue(3,0)

* new=1, free_head=2
* data[1]=3, next[1]=-1
* link: next[rear0=0]=1, rear0=1
* queue0: 0 -> 1

### 3) enqueue(1,1)

* new=2, free_head=3
* data[2]=1
* queue1: front1=rear1=2

### 4) dequeue(0)

* idx=front0=0, front0=next[0]=1
* return data[0]=5
* add idx=0 to free list: next[0]=free_head(3), free_head=0

Now:

* queue0: 1
* free list: 0 -> 3 -> -1

### 5) enqueue(4,1)

* new=0, free_head=3
* data[0]=4
* queue1: 2 -> 0

### 6) enqueue(1,0)

* new=3, free_head=-1
* data[3]=1
* queue0: 1 -> 3

### 7) isEmpty(1) → false (front1=2)

### 8) isFull() → true (free_head=-1)

Outputs: `[5, false, true]` ✅

---

## 3) Python codes (brute/easy + optimized interview expected)

### A) Brute / easy (NOT memory-efficient, but simplest)

Use `k` separate deques. This **does not** meet “single array” requirement, but good baseline.

```python
from collections import deque

class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.queues = [deque() for _ in range(k)]
        self.total_size = 0

    def enqueue(self, x, i):
        if self.isFull():
            return
        self.queues[i].append(x)
        self.total_size += 1

    def dequeue(self, i):
        if self.isEmpty(i):
            return -1
        self.total_size -= 1
        return self.queues[i].popleft()

    def isEmpty(self, i):
        return len(self.queues[i]) == 0

    def isFull(self):
        return self.total_size == self.n
```

---

### B) Interview-expected optimized (Single array + free list) ✅

This is the correct intended solution.

```python
class kQueues:
    def __init__(self, n, k):
        # n = total slots in the single array
        # k = number of queues
        self.n = n
        self.k = k

        # data stores actual values
        self.data = [0] * n

        # next_index acts like "next pointer" for each slot
        self.next_index = list(range(1, n)) + [-1]  # 0->1->2->...->n-1->-1

        # front and rear pointers for each of k queues
        self.front = [-1] * k
        self.rear = [-1] * k

        # head of free list (first free slot index)
        self.free_head = 0

    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        # Time: O(1)
        if self.free_head == -1:
            # No free space available (array full)
            return

        # Take a free index from free list
        new_index = self.free_head
        self.free_head = self.next_index[new_index]

        # Store value
        self.data[new_index] = x
        self.next_index[new_index] = -1  # new node will be the tail

        # If queue i is empty, new node becomes front and rear
        if self.front[i] == -1:
            self.front[i] = self.rear[i] = new_index
        else:
            # Link it after current rear
            self.next_index[self.rear[i]] = new_index
            self.rear[i] = new_index

    def dequeue(self, i):
        # Dequeue element from queue number i
        # Time: O(1)
        if self.front[i] == -1:
            return -1  # queue empty

        # Get front index of queue i
        removed_index = self.front[i]
        result = self.data[removed_index]

        # Move front to next node
        self.front[i] = self.next_index[removed_index]

        # If queue becomes empty, update rear too
        if self.front[i] == -1:
            self.rear[i] = -1

        # Add removed index back to free list
        self.next_index[removed_index] = self.free_head
        self.free_head = removed_index

        return result

    def isEmpty(self, i):
        # Check if queue i is empty
        # Time: O(1)
        return self.front[i] == -1

    def isFull(self):
        # Check if array is full
        # Time: O(1)
        return self.free_head == -1
```

---

## 4) Interview quick recall + expected Q&A

### How to remember quickly (30-second mental model)

**“Array as nodes + next[] as pointers + one free list + front/rear per queue.”**

Mnemonic:
**“F R + NEXT + FREE”**

* `front[k]`, `rear[k]`
* `next[n]` pointer array
* `free_head` = head of free slots

### 5-line pseudo skeleton

```text
init: next[i]=i+1, next[n-1]=-1, free=0, front/rear=-1
enqueue: idx=free; free=next[idx]; data[idx]=x; next[idx]=-1; attach to queue i
dequeue: idx=front[i]; front[i]=next[idx]; if front==-1 rear=-1; add idx to free list; return data[idx]
isEmpty: front[i]==-1
isFull: free==-1
```

---

## Expected interviewer questions & answers

### Q1) Why not split array into k fixed parts?

**A:** It wastes space—one queue can overflow even if other partitions are empty.

### Q2) What data structures do you maintain?

**A:** `data[n]`, `next[n]`, `front[k]`, `rear[k]`, and `free_head`.

### Q3) How do you get O(1) enqueue/dequeue?

**A:** Free list gives O(1) slot allocation; `next[]` links nodes in each queue in O(1) using `rear` and `front`.

### Q4) What happens on dequeue when queue becomes empty?

**A:** Set both `front[i]` and `rear[i]` to `-1`.

### Q5) Space complexity?

**A:** `O(n + k)` for arrays `data`, `next`, `front`, `rear`.

### Q6) How is this similar to a linked list?

**A:** Each occupied slot is like a node, and `next[]` stores the “next pointer”.

---

---

## 5) Real-world use cases (few, very relatable)

1. **Multi-tenant request queues in a shared buffer (OS / networking)**

   * Different clients/flows each need their own FIFO queue, but memory is a shared fixed-size buffer (e.g., packet buffering, socket send queues).
   * k-queues-in-1-array avoids wasting space when some flows are idle.

2. **Embedded systems with tight RAM**

   * You may need multiple command/event queues (sensor events, UI events, comm events) but can only afford one fixed array.
   * Free-list allocation gives predictable O(1) ops and efficient memory reuse.

3. **Task scheduling across multiple priorities**

   * Each priority level is a queue, but you store tasks in one pool (array).
   * Prevents the “priority-0 queue full while priority-3 empty” waste.

---

## 6) Full program (timed) + inline complexity notes + sample I/O

### Input format (simple and clear)

* Line 1: `n k q`
* Next `q` lines: query

  * `1 x i`  → enqueue(x, i)
  * `2 i`    → dequeue(i)      (print returned value)
  * `3 i`    → isEmpty(i)      (print true/false)
  * `4`      → isFull()        (print true/false)

This matches the statement’s query format.

> Execution time printed to **stderr** so normal outputs remain clean.

```python
import sys
import time

class kQueues:
    def __init__(self, n, k):
        """
        Initialize k queues in one array of size n.

        Space:
          data[n] + next_index[n] => O(n)
          front[k] + rear[k]      => O(k)
        Total Auxiliary Space: O(n + k)
        """
        self.n = n
        self.k = k

        # Stores actual values
        # Space: O(n)
        self.data = [0] * n

        # "Next pointer" array to link nodes AND maintain free list
        # Space: O(n)
        self.next_index = list(range(1, n)) + [-1]

        # Front and rear indices for each queue
        # Space: O(k)
        self.front = [-1] * k
        self.rear = [-1] * k

        # Head of free list
        self.free_head = 0

    def enqueue(self, x, i):
        """
        Enqueue x into i-th queue.
        Time: O(1)
        """
        if self.free_head == -1:
            # No free slot available => array full
            return

        # Take one free slot
        new_index = self.free_head
        self.free_head = self.next_index[new_index]

        # Store data in that slot
        self.data[new_index] = x
        self.next_index[new_index] = -1  # new node becomes tail

        # If queue is empty, front and rear both become new_index
        if self.front[i] == -1:
            self.front[i] = self.rear[i] = new_index
        else:
            # Link at the end of queue i
            self.next_index[self.rear[i]] = new_index
            self.rear[i] = new_index

    def dequeue(self, i):
        """
        Dequeue front element from i-th queue.
        Time: O(1)
        Returns -1 if empty.
        """
        if self.front[i] == -1:
            return -1

        removed_index = self.front[i]
        value = self.data[removed_index]

        # Move front pointer ahead
        self.front[i] = self.next_index[removed_index]

        # If queue becomes empty, rear should also become -1
        if self.front[i] == -1:
            self.rear[i] = -1

        # Put removed slot back to free list
        self.next_index[removed_index] = self.free_head
        self.free_head = removed_index

        return value

    def isEmpty(self, i):
        """
        Time: O(1)
        """
        return self.front[i] == -1

    def isFull(self):
        """
        Time: O(1)
        """
        return self.free_head == -1


def main():
    """
    Reads input, processes queries, prints outputs for:
    - dequeue
    - isEmpty
    - isFull
    Also prints total runtime to stderr.
    """
    start_time = time.perf_counter()  # full program timer

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Step A: Parse n, k, q
    # Time: O(1)
    n = int(data[0])
    k = int(data[1])
    q = int(data[2])

    queues = kQueues(n, k)

    output_lines = []
    idx = 3

    # Step B: Process queries
    # Each operation is O(1); total time O(q)
    for _ in range(q):
        query_type = int(data[idx])
        idx += 1

        if query_type == 1:
            # 1 x i : enqueue(x, i)
            x = int(data[idx]); i = int(data[idx + 1])
            idx += 2
            queues.enqueue(x, i)

        elif query_type == 2:
            # 2 i : dequeue(i)
            i = int(data[idx]); idx += 1
            output_lines.append(str(queues.dequeue(i)))

        elif query_type == 3:
            # 3 i : isEmpty(i)
            i = int(data[idx]); idx += 1
            output_lines.append("true" if queues.isEmpty(i) else "false")

        elif query_type == 4:
            # 4 : isFull()
            output_lines.append("true" if queues.isFull() else "false")

    # Step C: Print all outputs
    sys.stdout.write("\n".join(output_lines))

    end_time = time.perf_counter()
    print(f"\n[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
4 2 8
1 5 0
1 3 0
1 1 1
2 0
1 4 1
1 1 0
3 1
4

Expected Output:
5
false
true

Explanation:
dequeue(0) -> 5
isEmpty(1) -> false
isFull() -> true
"""
```

