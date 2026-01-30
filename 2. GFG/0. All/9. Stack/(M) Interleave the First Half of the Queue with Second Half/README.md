# Interleave the First Half of the Queue with Second Half

**Difficulty:** Medium  
**Accuracy:** 62.41%  
**Submissions:** 26K+  
**Points:** 4  
**Average Time:** 20m  

---

## Problem Statement

Given a queue **q[]** of **even size**. Your task is to rearrange the queue by interleaving its **first half** with the **second half**.

### What is Interleaving?
Interleaving is the process of mixing two sequences by alternating their elements while preserving their relative order.  
In other words, Interleaving means place the **first element** from the first half and then **first element** from the 2nd half and again **second element** from the first half and then **second element** from the 2nd half and so on....

---

## Examples

### Example 1
**Input:**  
`q[] = [2, 4, 3, 1]`  

**Output:**  
`[2, 3, 4, 1]`  

**Explanation:**  
We place the first element of the first half `2` and after that place the first element of second half `3` and after that repeat the same process one more time so the resulting queue will be `[2, 3, 4, 1]`.

---

### Example 2
**Input:**  
`q[] = [3, 5]`  

**Output:**  
`[3, 5]`  


---

---

## 2) Text explanation (what to do)

Queue size is **even**: `n`.
Split it into:

* **first half**: first `n/2` elements
* **second half**: last `n/2` elements

Then interleave while preserving order:

`f1, f2, f3...` and `s1, s2, s3...`  →  `f1, s1, f2, s2, f3, s3...`

---

## Step-by-step dry run

### Example: `q = [2, 4, 3, 1]`

* `n = 4`, `half = 2`
* first half = `[2, 4]`
* second half = `[3, 1]`

Interleave:

* take `2` (first half), take `3` (second half) → `[2, 3]`
* take `4`, take `1` → `[2, 3, 4, 1]`

Final queue: `[2, 3, 4, 1]`

---

## 3) Python solutions (brute/easy + interview-expected)

### A) Easiest (use list conversion) — very readable

**Time:** `O(n)`
**Aux Space:** `O(n)`

```python
from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        # Convert queue to list for easy indexing
        elements = list(q)
        n = len(elements)
        half = n // 2

        first_half = elements[:half]
        second_half = elements[half:]

        # Build interleaved order
        interleaved = []
        for i in range(half):
            interleaved.append(first_half[i])
            interleaved.append(second_half[i])

        # Rewrite back into the same deque (in-place update)
        q.clear()
        q.extend(interleaved)
        return q
```

---

### B) Most expected in interviews (Queue + Stack method)

Classic approach using a stack to hold first half.

**Idea:**

1. Push first half into stack (reverses order)
2. Append stack back into queue (first half reversed goes to back)
3. Rotate first half elements to back to restore correct half positioning
4. Again push first half into stack
5. Now interleave by alternating stack element (first half) and queue front (second half)

**Time:** `O(n)`
**Aux Space:** `O(n)` (stack)

```python
from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        stack = []

        # Step 1: push first half into stack
        # Time: O(n/2), Space: O(n/2)
        for _ in range(half):
            stack.append(q.popleft())

        # Step 2: push stack back to queue (reversed first half goes behind)
        # Time: O(n/2)
        while stack:
            q.append(stack.pop())

        # Step 3: rotate first half (now at front) to back to restore order separation
        # Time: O(n/2)
        for _ in range(half):
            q.append(q.popleft())

        # Step 4: again push first half (original order now at front) into stack
        # Time: O(n/2)
        for _ in range(half):
            stack.append(q.popleft())

        # Step 5: interleave stack (first half) + queue (second half)
        # stack top is the correct next element of first half
        # Time: O(n)
        while stack:
            q.append(stack.pop())    # element from first half
            q.append(q.popleft())    # element from second half

        return q
```

---

### C) Clean two-queue approach (simple & clear)

Split into two deques and merge.

**Time:** `O(n)`
**Aux Space:** `O(n)`

```python
from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2

        first_half = deque()
        for _ in range(half):
            first_half.append(q.popleft())

        # Now q contains the second half
        second_half = q

        interleaved = deque()
        while first_half:
            interleaved.append(first_half.popleft())
            interleaved.append(second_half.popleft())

        # Put back into original queue
        q.clear()
        q.extend(interleaved)
        return q
```

---

## 4) Interview quick recall + expected Q&A

### Quick memory trick

**“Split in half, then alternate.”**

Mnemonic:
**“F-S-F-S…”** (First half element, Second half element, repeat)

### 5-line pseudo template (most memorable)

```text
half = n/2
move first half into temp
while temp not empty:
  q.push(temp.pop_front())   # or temp[i]
  q.push(q.pop_front())      # from second half
```

---

## Expected interviewer questions & answers

### Q1) Why must queue size be even?

**A:** Because we must split into equal halves; otherwise one half would have extra elements and interleaving definition changes.

### Q2) Complexity?

**A:** `O(n)` time. Space depends on method: list/extra queue/stack typically `O(n)`.

### Q3) Can it be done in-place with O(1) extra space?

**A:** With a queue ADT (only push/pop front/back), pure O(1) is tricky; most standard solutions use `O(n)` auxiliary structure (stack or extra queue). If we allow array indexing, we can do in-place rearrangement with index math, but not with strict queue operations.

### Q4) Does interleaving preserve relative order inside each half?

**A:** Yes. We always take elements from each half in their original order.

### Q5) Which solution is best for interviews?

**A:** The “split into two halves using a temp queue and merge” is simplest. The “stack + queue” method is a classic DS interview pattern.

---

---

## 5) Real-world use cases (few, high-signal)

1. **Round-robin / fairness scheduling**

   * Interleaving two groups ensures fairness: take one from Group A, then one from Group B (e.g., customer support queues: priority vs normal).

2. **Merging two ordered streams**

   * Combining events from two sources while preserving order within each source (e.g., logs from two services, A/B experiment streams).

3. **Load balancing / batching**

   * Alternating items from two partitions (hot vs cold tasks) to avoid bursts and smooth processing.

---

## 6) Full program (timed) + inline complexity notes + sample I/O

### Assumptions

* Input queue size is even (as per problem).
* We use the **most interview-friendly** method: split into two halves (extra queue) and interleave.

### Input format (simple CP style)

* Line 1: `n`
* Line 2: `n` integers

### Output

* Interleaved queue as space-separated integers

> Execution time printed to **stderr** so stdout stays clean.

```python
import sys
import time
from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        """
        Interleave first half with second half of an even-sized queue.

        Time Complexity: O(n)
        Auxiliary Space: O(n)  (temporary queue for first half)
        """
        n = len(q)
        half = n // 2

        # Step 1: Extract first half into a temp queue
        # Time: O(n/2), Space: O(n/2)
        first_half = deque()
        for _ in range(half):
            first_half.append(q.popleft())

        # Now q contains the second half (size = half)

        # Step 2: Interleave into a result queue
        # Time: O(n), Space: O(n)
        interleaved = deque()
        while first_half:
            interleaved.append(first_half.popleft())  # from first half
            interleaved.append(q.popleft())           # from second half

        # Step 3: Put back into original queue
        # Time: O(n), Space: O(1) extra
        q.extend(interleaved)
        return q


def main():
    """
    Input:
      n
      q elements...

    Output:
      interleaved queue
    """
    start_time = time.perf_counter()  # measure full program runtime

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Step A: Read inputs
    # Time: O(n), Space: O(n)
    n = int(data[0])
    elements = list(map(int, data[1:1 + n]))

    # Build queue
    # Time: O(n), Space: O(n)
    q = deque(elements)

    # Step B: Solve
    # Time: O(n), Aux Space: O(n)
    solver = Solution()
    solver.rearrangeQueue(q)

    # Step C: Print result (stdout)
    # Time: O(n)
    print(" ".join(map(str, q)))

    end_time = time.perf_counter()
    # Print timing to stderr so it does not affect judge output
    print(f"[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
4
2 4 3 1

Expected Output:
2 3 4 1
"""
```