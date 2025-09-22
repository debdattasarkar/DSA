# Queue Reversal

**Difficulty:** Easy
**Accuracy:** 77.98%
**Submissions:** 145K+
**Points:** 2

---

Given a queue `q` containing integer elements, your task is to **reverse the queue**.

---

## Examples

**Input:** `q[] = [5, 10, 15, 20, 25]`
**Output:** `[25, 20, 15, 10, 5]`
**Explanation:** After reversing the given elements of the queue, the resultant queue will be `25 20 15 10 5`.

---

**Input:** `q[] = [1, 2, 3, 4, 5]`
**Output:** `[5, 4, 3, 2, 1]`
**Explanation:** After reversing the given elements of the queue, the resultant queue will be `5 4 3 2 1`.

---

## Constraints

* `1 ≤ q.size() ≤ 10^3`
* `0 ≤ q[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Amazon

---

## Topic Tags

Stack • Queue • Data Structures

---

## Related Articles

* Reversing A Queue

---

---

Awesome—let’s lock it in using the **stack-based** solution you validated.

# 2) Plain-English explanation + step-by-step dry run

### Goal

Reverse a queue `q` (front → back order becomes back → front) **in place**.

### Idea (based on your accepted solution)

1. **Dequeue** each element from the front of `q` and **push** it onto a **stack** (LIFO).
2. **Pop** each element from the stack and **enqueue** it back to `q`.
3. Because stacks reverse order, the queue ends up reversed.

This works whether `q` is a Python **list** being used like a queue (`pop(0)` / `append`) or a **deque** (`popleft()` / `append`).

---

### Dry run

Input: `q = [4, 3, 1, 10, 2, 6]` (front is the left side)

**Phase 1 — move to stack**

* pop front → 4 → stack = \[4], q = \[3, 1, 10, 2, 6]
* pop front → 3 → stack = \[4, 3], q = \[1, 10, 2, 6]
* pop front → 1 → stack = \[4, 3, 1], q = \[10, 2, 6]
* pop front → 10 → stack = \[4, 3, 1, 10], q = \[2, 6]
* pop front → 2 → stack = \[4, 3, 1, 10, 2], q = \[6]
* pop front → 6 → stack = \[4, 3, 1, 10, 2, 6], q = \[]

**Phase 2 — put back from stack**

* pop → 6 → enqueue → q = \[6]
* pop → 2 → enqueue → q = \[6, 2]
* pop → 10 → enqueue → q = \[6, 2, 10]
* pop → 1 → enqueue → q = \[6, 2, 10, 1]
* pop → 3 → enqueue → q = \[6, 2, 10, 1, 3]
* pop → 4 → enqueue → q = \[6, 2, 10, 1, 3, 4]

**Result:** `q = [6, 2, 10, 1, 3, 4]` ✅

---

# 3) Optimized Python solutions (interview-ready)

All variants below follow your required signature.

## A) Iterative with a stack (most expected)

```python
from collections import deque

class Solution:
    def reverseQueue(self, q):
        """
        Reverse the queue in-place using a stack.
        Works for both list (used as a queue) and collections.deque.
        Time  : O(n)
        Space : O(n)
        """
        is_deque = hasattr(q, "popleft")  # True for deque

        stack = []

        # Dequeue everything to a stack
        while q:
            x = q.popleft() if is_deque else q.pop(0)  # remove from front
            stack.append(x)

        # Pop stack back into the queue (reverses order)
        while stack:
            q.append(stack.pop())

        return q  # some judges want return, some rely on in-place
```

## B) Recursive (no explicit stack; uses call stack)

Uses only queue operations; elegant and commonly discussed.

```python
from collections import deque

class Solution:
    def reverseQueue(self, q):
        """
        Recursively reverse the queue using only queue ops.
        Time  : O(n)
        Space : O(n) recursion depth (implicit stack)
        """
        is_deque = hasattr(q, "popleft")

        # Base case: empty queue
        if not q:
            return q

        # Remove front
        x = q.popleft() if is_deque else q.pop(0)

        # Reverse the remaining queue
        self.reverseQueue(q)

        # Put this element at the rear
        q.append(x)
        return q
```

## C) One-liner “built-in reverse” (use only if allowed)

Some platforms allow it; others don’t. It’s O(n) and in-place.

```python
from collections import deque

class Solution:
    def reverseQueue(self, q):
        """
        Use built-in reverse (allowed on some platforms).
        Time  : O(n)
        Space : O(1)
        """
        # Both list and deque support reverse()
        q.reverse()  # in-place
        return q
```

> If the judge forbids built-ins, stick to **A** (stack) or **B** (recursive).

---

# 4) Interview Q\&A (quick hitters)

**Q1. What’s the time and space complexity of your stack solution?**
**A.** Time **O(n)** (each element moved twice). Space **O(n)** for the stack.

**Q2. Can you do it without extra space?**
**A.** If using Python’s `reverse()` (for list/deque) is allowed, it’s **O(1)** extra space. Otherwise, pure queue operations require either an auxiliary stack or recursion (implicit stack).

**Q3. Why not use `list.pop(0)`? Isn’t it O(n)?**
**A.** Yes, `pop(0)` is O(n). For constraints up to \~1e3 it’s fine; for larger inputs we should pass a `deque` and use `popleft()` which is **O(1)**.

**Q4. Does your function mutate the original queue?**
**A.** Yes, it reverses **in place** and also returns the same object for convenience.

**Q5. What are edge cases?**
**A.** Empty queue → remains empty. Single element → unchanged. Duplicates → preserved; only order changes.

**Q6. Why is recursion acceptable here?**
**A.** It’s a common interview variant demonstrating call-stack usage; complexity is still O(n) time, O(n) space (implicit).

**Q7. Which approach would you choose in production?**
**A.** If the container is a `deque`, I’d call `q.reverse()` for clarity and speed. If that’s disallowed, the **stack** approach is the most straightforward and robust.

---

---

Here you go — a **complete, runnable program** that implements the stack-based queue reversal (the same approach you validated), prints the input/output, and measures the runtime using `timeit`. I’ve annotated each step with **time/space complexity** comments right where the work is done.

```python
# -*- coding: utf-8 -*-
"""
Reverse a queue using a stack (interview-standard solution)

Key idea:
1) Dequeue all items to a stack (LIFO)  -> O(n) time, O(n) extra space.
2) Pop from the stack and enqueue back  -> O(n) time, O(1) extra space besides the stack.
Total: O(n) time, O(n) extra space.

This file:
- Implements the stack solution (and a recursive variant for reference).
- Shows one sample run with input + output.
- Uses timeit to measure performance inline.
"""

from collections import deque
import timeit
from typing import Iterable


class Solution:
    def reverseQueue(self, q):
        """
        Reverse the queue in-place using an auxiliary stack.

        Works for:
          - collections.deque (recommended: O(1) popleft/append)
          - list used as a queue (pop(0) is O(n), OK only for small sizes)

        Time Complexity:
            - Moving all elements from queue to stack: O(n)
            - Moving all elements back from stack to queue: O(n)
            => Total: O(n)

        Space Complexity:
            - Stack holds up to n items => O(n)
        """
        # Detect deque vs list to choose correct "pop-front" operation.
        is_deque = hasattr(q, "popleft")

        stack = []  # O(n) extra space in worst case

        # Phase 1: Dequeue all elements and push to stack (reverses order)
        # O(n) time; each element is moved once
        while q:
            x = q.popleft() if is_deque else q.pop(0)  # remove from front
            stack.append(x)

        # Phase 2: Pop stack back to queue
        # O(n) time; each element is moved once
        while stack:
            q.append(stack.pop())

        return q  # return is convenient; reversal is in-place


    def reverseQueueRecursive(self, q):
        """
        Recursive reversal using only queue operations (no explicit stack).
        For interviews that ask to avoid auxiliary data structures.

        Time Complexity  : O(n)
        Space Complexity : O(n) implicit due to recursion depth
        """
        is_deque = hasattr(q, "popleft")

        # Base case: empty queue
        if not q:
            return q

        # Remove front (O(1) for deque, O(n) for list)
        x = q.popleft() if is_deque else q.pop(0)

        # Recurse on the smaller queue (depth grows to n) -> O(n) calls
        self.reverseQueueRecursive(q)

        # On unwind, append current element to back -> builds reversed order
        q.append(x)
        return q


# -----------------------------
# Demo / Timing
# -----------------------------
def as_deque(iterable: Iterable[int]) -> deque:
    """Helper to ensure we're using deque for O(1) queue ops."""
    return deque(iterable)


def main():
    sol = Solution()

    # ---- Input (front is left-most) ----
    sample = [4, 3, 1, 10, 2, 6]  # change this to try other inputs
    q = as_deque(sample)

    print("Input queue (front -> back):", list(q))

    # ---- Reverse (stack-based) ----
    sol.reverseQueue(q)

    print("Reversed queue (front -> back):", list(q))  # Expected: [6, 2, 10, 1, 3, 4]

    # -----------------------------
    # Timing with timeit
    # -----------------------------
    # Build a small benchmark that recreates the queue each run (so each run starts fresh).
    def bench_once():
        q_local = as_deque(sample)            # O(n) to build small input
        sol.reverseQueue(q_local)             # O(n) to reverse
        return q_local[0] if q_local else -1  # Use the result to avoid being optimized away

    # Run the benchmark multiple times to get a stable average
    runs = 10000  # adjust to 1000 if your machine is slow
    total_sec = timeit.timeit(bench_once, number=runs)
    print(f"\nTimeit: {runs} runs total = {total_sec:.6f}s  |  avg = {total_sec / runs * 1e6:.2f} µs/run")

    # For completeness: quick timing of the recursive variant (smaller runs to avoid recursion limits)
    def bench_recursive_once():
        q_local = as_deque(sample)
        sol.reverseQueueRecursive(q_local)
        return q_local[0] if q_local else -1

    rec_runs = 1000
    rec_total = timeit.timeit(bench_recursive_once, number=rec_runs)
    print(f"Timeit (recursive): {rec_runs} runs total = {rec_total:.6f}s  |  avg = {rec_total / rec_runs * 1e6:.2f} µs/run")


if __name__ == "__main__":
    main()
```

### Sample Output (what you’ll see)

```
Input queue (front -> back): [4, 3, 1, 10, 2, 6]
Reversed queue (front -> back): [6, 2, 10, 1, 3, 4]

Timeit: 10000 runs total = 0.420000s  |  avg = 42.00 µs/run
Timeit (recursive): 1000 runs total = 0.060000s  |  avg = 60.00 µs/run
```

*(Numbers above will vary by machine.)*

---

## 6) Real-World Use Cases (just the big ones)

1. **Job/Task Queues (replay in reverse):** Replaying events from newest to oldest (e.g., compensating actions, sagas, rollback or unwind operations).
2. **Customer Support / Ticketing:** Temporarily reversing a FIFO queue to prioritize the latest items (e.g., “most recent first” triage).
3. **Message Brokers & Log Pipelines (controlled re-ordering):** Controlled reverse processing during re-drives or backfills where newer messages must be handled first.
4. **UI/UX feed rendering:** Switching between chronological and reverse-chronological order without re-fetching (local reordering of a queue-like structure).
