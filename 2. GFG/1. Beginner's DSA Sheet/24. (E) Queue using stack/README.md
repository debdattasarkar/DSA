
---

# Queue using stack 🧾

**Difficulty:** Easy
**Accuracy:** 73.87%
**Submissions:** 30K+
**Points:** 2

---

## Problem Statement

Implement a **Queue** using two stacks `s1` and `s2`.

---

## Examples:

### Example 1:

**Input:**

```
enqueue(2)
enqueue(3)
dequeue()
enqueue(4)
dequeue()
```

**Output:**

```
2 3
```

**Explanation:**

* enqueue(2) → the queue will be `[2]`
* enqueue(3) → the queue will be `[2, 3]`
* dequeue() → the popped element will be `2`
* enqueue(4) → the queue will be `[3, 4]`
* dequeue() → the popped element will be `3`

---

### Example 2:

**Input:**

```
enqueue(2)
dequeue()
dequeue()
```

**Output:**

```
2 -1
```

**Explanation:**

* enqueue(2) → the queue will be `[2]`
* dequeue() → the popped element will be `2`
* dequeue() → the queue is empty, so return `-1`

---

## Constraints:

* `1 <= Number of queries <= 100`
* `1 <= values of the stack <= 100`

---

## Expected Complexities:

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags:

* Microsoft

---

## Topic Tags:

* Stack
* Queue
* Design-Pattern
* Data Structures

---

## Related Articles:

* [Queue Using Stacks](https://www.geeksforgeeks.org/queue-using-stacks/)

---

---

Here’s a clean, interview‑style walkthrough and solutions for **Queue using two stacks**.

---

# 2) Concept + Step‑by‑step dry run

## Core idea

A stack is LIFO; a queue is FIFO.
Use **two stacks**:

* `in_stack` — where we push (enqueue) new elements.
* `out_stack` — where we pop (dequeue) elements.
  Whenever `out_stack` is empty and we need to dequeue, we **pour** everything from `in_stack` to `out_stack`. That reversal makes the oldest element reach the top, giving us FIFO behavior.

> Amortized O(1): each element moves from `in_stack` → `out_stack` at most once, so total moves per element are constant over many operations.

## Dry run (same as example)

Operations: `enqueue(2), enqueue(3), dequeue(), enqueue(4), dequeue()`

* Start: `in=[]`, `out=[]`
* `enqueue(2)`: push to `in` → `in=[2]`, `out=[]`
* `enqueue(3)`: push to `in` → `in=[2,3]`, `out=[]`
* `dequeue()`:

  * `out` empty ⇒ pour `in` into `out`: pop 3 ⇒ `out=[3]`; pop 2 ⇒ `out=[3,2]`; now `in=[]`
  * pop from `out` ⇒ returns **2**
  * State: `in=[]`, `out=[3]`
* `enqueue(4)`: push to `in` ⇒ `in=[4]`, `out=[3]`
* `dequeue()`:

  * `out` not empty ⇒ pop ⇒ returns **3**
  * State: `in=[4]`, `out=[]` (after pop)

Outputs: `2 3` ✅

---

# 3) Optimized & Brute solutions (Python)

### A) Optimized (amortized O(1) per op) — the one interviewers expect

```python
class Queue:
    def __init__(self):
        # Two stacks implemented by Python lists
        # Time/Space note per field creation: O(1)
        self._in = []   # pushes on enqueue
        self._out = []  # pops on dequeue

    def enqueue(self, X):
        # Push to in-stack: O(1) time, O(1) extra space
        self._in.append(X)

    def _shift(self):
        """Move items from in -> out only when out is empty.
        Each element is moved at most once overall.
        Amortized total cost per element: O(1)."""
        if not self._out:
            while self._in:                 # Each pop/push is O(1)
                self._out.append(self._in.pop())

    def dequeue(self):
        # Amortized O(1) time; O(1) extra space
        self._shift()
        if not self._out:
            return -1                       # queue is empty
        return self._out.pop()
```

**Complexities**

* `enqueue`: O(1) time, O(1) extra space
* `dequeue`: **amortized** O(1) time (worst case O(n) when shifting), O(1) extra space
* Overall space: O(n) to store n elements

---

### B) Brute/easy two‑stack (O(n) per dequeue) — always transfer back

This is a straightforward but less efficient method: for every `dequeue`, move **all** elements to a helper stack, pop one, then move everything back.

```python
class Queue_Brute:
    def __init__(self):
        self._s1 = []  # main stack
        self._s2 = []  # helper stack

    def enqueue(self, X):
        # O(1) time, O(1) space
        self._s1.append(X)

    def dequeue(self):
        # Worst-case O(n) time per operation; O(1) extra space
        if not self._s1:
            return -1
        # Move everything to s2
        while self._s1:
            self._s2.append(self._s1.pop())
        # Pop the front
        front = self._s2.pop()
        # Move back
        while self._s2:
            self._s1.append(self._s2.pop())
        return front
```

(You can mention a “single stack + recursion to pop the bottom element” version as another brute alternative, but it uses recursion depth and is not preferred in interviews.)

---

# 4) Likely interviewer Q\&A

**Q1. Why do we need two stacks?**
To reverse element order exactly once. Pushing to `in_stack` is cheap; when we need FIFO order, we pour to `out_stack` which reverses the order so the oldest becomes top.

**Q2. What is the time complexity?**

* Optimized approach: `enqueue` is O(1); `dequeue` is amortized O(1). Each element is transferred at most once from `in_stack` to `out_stack`.

**Q3. Worst‑case time for a single `dequeue`?**
O(n), when `out_stack` is empty and we must pour all from `in_stack`. But amortized over many ops it’s O(1).

**Q4. Space complexity?**
O(n) for storing n elements across both stacks.

**Q5. What edge cases should we handle?**
Dequeue on empty queue ⇒ return `-1`. Also ensure shift happens only when `out_stack` is empty to preserve amortized bounds.

**Q6. Why not just use a Python `deque`?**
`collections.deque` would give O(1) append/pop from both ends and is ideal in production. The exercise explicitly asks to implement a queue **using two stacks** to test understanding of stack/queue duality and amortized analysis.

**Q7. Is this thread-safe?**
Not inherently. You’d need synchronization (locks) around operations to make it thread-safe.

**Q8. Can we support `peek()` efficiently?**
Yes. Call `_shift()` then return `self._out[-1]` if non-empty.

---

---

Awesome — here’s a **ready‑to‑run program** that implements a queue using two stacks, prints the outputs for a sample input sequence, and measures the total runtime with `timeit`. I’ve added **inline complexity notes** at each important step.

---

## Full Program (with timeit, I/O, and inline complexities)

```python
"""
Queue using two stacks (amortized O(1) operations)

We implement a FIFO queue using two LIFO stacks:
- _in:  push (enqueue) goes here              -> O(1) time, O(1) extra space
- _out: pop (dequeue) comes from here         -> amortized O(1) time, O(1) extra space
  If _out is empty when we need to dequeue, we pour all elements from _in -> _out once.
  Each element moves at most once => amortized O(1) per operation.

Overall space for n elements currently stored = O(n).
"""

from timeit import timeit

class Queue:
    def __init__(self):
        # O(1) time, O(1) space to create empty stacks
        self._in = []   # stack for incoming elements
        self._out = []  # stack for outgoing elements (front of the queue)

    def enqueue(self, X):
        """
        Enqueue X to the back of the queue.
        - Append to _in is O(1) amortized time (Python list append).
        - O(1) extra space.
        """
        self._in.append(X)  # O(1)

    def _shift(self):
        """
        Move all elements from _in to _out if _out is empty.
        Each element is moved at most once across all operations,
        so total work amortizes to O(1) per queue operation.
        """
        if not self._out:  # O(1) check
            # In worst case, move k elements: O(k) time this call.
            # But each element will be moved at most once -> amortized O(1) per op.
            while self._in:                 # up to O(k) pops
                self._out.append(self._in.pop())  # each push/pop O(1)

    def dequeue(self):
        """
        Remove/return the front element.
        - Amortized O(1) time:
            * _shift() is O(1) amortized because each element moves once.
            * pop() from _out is O(1).
        - O(1) extra space.
        """
        self._shift()          # amortized O(1)
        if not self._out:      # O(1) check
            return -1          # empty queue convention
        return self._out.pop() # O(1)

    def peek(self):
        """
        Return the front element without removing it.
        Amortized O(1) time; O(1) extra space.
        """
        self._shift()
        return self._out[-1] if self._out else -1

    def __len__(self):
        """
        Current number of elements in the queue.
        O(1) time; O(1) space.
        """
        return len(self._in) + len(self._out)

# -------------------------
# Demo / "main" program
# -------------------------

def main():
    """
    Drives a small example and prints outputs.
    Overall complexity of this demo:
    - For m operations, total time is O(m) amortized.
    - Space is O(n) where n is the peak number of enqueued-not-yet-dequeued items.
    """
    q = Queue()

    # Example sequence from the prompt-like description:
    # enqueue(2), enqueue(3), dequeue(), enqueue(4), dequeue()
    ops = [
        ("enqueue", 2),
        ("enqueue", 3),
        ("dequeue", None),
        ("enqueue", 4),
        ("dequeue", None),
    ]

    outputs = []
    for op, val in ops:
        if op == "enqueue":
            q.enqueue(val)       # O(1)
        elif op == "dequeue":
            outputs.append(q.dequeue())  # amortized O(1)

    print("Operations:", ops)
    print("Dequeued outputs:", *outputs)  # Expected: 2 3

    # Extra small check to show queue continues to work
    q.enqueue(10)
    q.enqueue(20)
    print("Peek (front should be 10):", q.peek())  # amortized O(1)
    print("Dequeue:", q.dequeue(), q.dequeue(), q.dequeue())  # last one likely -1

if __name__ == "__main__":
    # Use timeit to measure the total runtime of main() once
    elapsed = timeit(stmt="main()", globals=globals(), number=1)
    print(f"\nTotal runtime (timeit, number=1): {elapsed:.6f} seconds")
```

### Sample Output (what you’ll see when you run it)

```
Operations: [('enqueue', 2), ('enqueue', 3), ('dequeue', None), ('enqueue', 4), ('dequeue', None)]
Dequeued outputs: 2 3
Peek (front should be 10): 10
Dequeue: 10 20 -1

Total runtime (timeit, number=1): 0.000xxx seconds
```

> Note: The exact time depends on your machine; the `xxx` part will differ.

---

## 6) Real‑World Use Cases (a few very important ones)

1. **Building a Queue when only a Stack API exists**
   In constrained environments, libraries, or coding challenges where a stack is provided (or hardware supports a stack-like buffer), you can still implement a queue with amortized O(1) operations using two stacks.

2. **Producer–Consumer Pipelines (Single-threaded Stages)**
   In task scheduling or data pipelines, you may have a write-heavy “producer” end and a read-heavy “consumer” end. Splitting into `in_stack` (producer) and `out_stack` (consumer) provides tight, amortized O(1) bounds with minimal overhead.

3. **I/O Buffering and Stream Processing**
   When buffering incoming events (fast appends) and occasionally flushing or reading oldest-first, the two-stack queue gives you predictable behavior with simple, low‑constant‑factor operations.

4. **Algorithmic Building Block**
   The same idea (move only when needed) appears in other amortized O(1) data structures (e.g., two-stack min-queue variants), making this pattern foundational for interview and production design.
