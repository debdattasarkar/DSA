
---

# Node at a Given Index in Linked List

**Difficulty:** Easy
**Accuracy:** 65.11%
**Submissions:** 101K+
**Points:** 2

---

## Problem Statement

Given the head of a **Singly Linked List** and an **index**, the task is to find the node at the given `index` (1-based index) of the linked list.
If no such index exists, then return **-1**.

---

## Examples

### Example 1

**Input:**
LinkedList: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`
index = `3`

**Output:**

```
3
```

**Explanation:**
The Node value at index 3 is 3.

---

### Example 2

**Input:**
LinkedList: `19 -> 28 -> 37 -> 46 -> 55`
index = `6`

**Output:**

```
-1
```

**Explanation:**
As the number of nodes is less than k (6 in this case), there is no node at index 6, therefore the answer is -1.

---

## Expected Time Complexity

```
O(n)
```

---

## Expected Auxiliary Space

```
O(1)
```

---

## Constraints

* `1 <= number of nodes <= 10^5`
* `1 <= node->data , k <= 10^5`

---

## Topic Tags

* Linked List
* Data Structures

---

## Related Articles

* [Insert A Node At A Specific Position In A Linked List](https://www.geeksforgeeks.org/insert-a-node-at-a-specific-position-in-a-linked-list/)
* [Write A Function To Get Nth Node In A Linked List](https://www.geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/)

---

---

Alright—let’s nail this one cleanly and interview‑ready.

# What the problem wants (in plain English)

You’re given the head of a singly linked list and a 1‑based index `index`. Return the **data** stored at the node in the `index`th position. If the index doesn’t exist (too big or non‑positive), return **-1**.

---

# Step‑by‑step reasoning (dry run)

Consider the list: `1 → 2 → 3 → 4 → 5`, and `index = 3`.

1. Start at `head` (value `1`), `pos = 1`. Is `pos == index`? No.
2. Move to `2`, `pos = 2`. Still not equal.
3. Move to `3`, `pos = 3`. Now `pos == index` → return `3`.

Edge cases:

* `index = 1` → immediately return `head.data` if `head` exists.
* `index = 7` with list length `5` → traversal ends at `None` before reaching `pos = 7` → return `-1`.
* `index <= 0` → invalid by problem statement → return `-1`.

---

# Approaches & Code (method‑only, as requested)

### 1) Iterative traversal (the standard, optimal solution)

* Time: **O(n)** — we may traverse the list once.
* Space: **O(1)** — just a few variables.

```python
"""
index is 1-based position whose node's data we must return.
Return -1 if index is invalid or beyond list length.
"""
class Solution:
    def GetNth(self, head, index):
        # Guard for invalid index (<= 0)
        if index <= 0:
            return -1  # O(1) time/space
        
        curr = head    # O(1) space
        pos  = 1       # current 1-based position
        
        # Traverse until we either hit the index or run out of nodes
        while curr is not None and pos < index:  # Each loop is O(1); total O(n)
            curr = curr.next
            pos += 1
        
        # If we stopped because we reached the desired position, return data
        if curr is not None and pos == index:
            return curr.data  # Found; O(1)
        
        # Otherwise, index is out of bounds
        return -1  # O(1)
```

---

### 2) Recursive traversal (elegant, but uses stack space)

* Time: **O(n)**
* Space: **O(n)** recursion stack (so this is *not* preferred for very long lists).

```python
class SolutionRecursive:
    def GetNth(self, head, index):
        # invalid index
        if index <= 0:
            return -1
        
        def helper(node, k):
            # Base: ran out of list before k hits 1
            if node is None:
                return -1  # O(1)
            # If k == 1, current node is the target
            if k == 1:
                return node.data  # O(1)
            # Else, move to next node and decrease k
            return helper(node.next, k - 1)  # Depth up to n (O(n) space)
        
        return helper(head, index)
```

---

### 3) “Brute” conversion to array (simple but extra memory)

* Time: **O(n)**
* Space: **O(n)** to store values in a list. Useful for clarity/tests, not for large inputs.

```python
class SolutionBrute:
    def GetNth(self, head, index):
        if index <= 0:
            return -1
        
        vals = []               # O(n) space
        curr = head
        while curr:
            vals.append(curr.data)  # O(1) amortized per push; total O(n)
            curr = curr.next
        
        # index is 1-based, Python list is 0-based
        if 1 <= index <= len(vals):
            return vals[index - 1]  # O(1)
        return -1
```

---

# Common interviewer Q\&A

**Q1. Is the index 0‑based or 1‑based?**
A. It’s **1‑based** per the prompt. So `index = 1` returns `head.data`.

**Q2. What if `index <= 0`?**
A. Invalid by problem statement—return **-1**.

**Q3. What are the time and space complexities of your main solution?**
A. Iterative approach: **O(n)** time, **O(1)** extra space.

**Q4. Why not recursion?**
A. Recursion is clean but uses **O(n)** call stack space, which risks stack overflow for large lists. Iteration is safer in production.

**Q5. How would you get the k‑th node from the end?**
A. Use two pointers: move `fast` k steps, then move `slow` and `fast` together until `fast` hits the end—`slow` then points to the k‑th from the end. Still **O(n)** time and **O(1)** space.

**Q6. What if the list can change while you’re traversing?**
A. In single-threaded contexts, it usually doesn’t. In concurrent scenarios, you’d need synchronization or a snapshot.

**Q7. What if you needed to return the node itself, not just its data?**
A. Return the `Node` instead of `node.data`. The traversal logic is identical.

**Q8. Can you do better than O(n)?**
A. Not in general for a singly linked list without extra indexing structures; accessing by position inherently requires traversal.

---

---

Awesome—here’s a clean, runnable script that:

* Builds a singly linked list
* Implements the optimal iterative solution to “get node at a given (1‑based) index”
* Prints inputs and outputs
* Benchmarks total runtime with `timeit`

I’ve sprinkled inline comments that call out time/space complexity of each step.

---

### Full Program (with timing and examples)

```python
from timeit import default_timer as timer

# ----------------------------
# Data structures
# ----------------------------

class Node:
    """Singly Linked List node"""
    def __init__(self, data):
        self.data = data  # O(1) space
        self.next = None  # O(1) space


class LinkedList:
    """Utility list to build and print nodes"""
    def __init__(self):
        self.head = None  # O(1) space

    def append(self, data):
        """
        Append at tail.
        Time:
          - Best O(1) if list empty
          - Worst O(n) to walk to the end (n = current size)
        Space: O(1)
        """
        new_node = Node(data)  # O(1) space
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:       # O(n) worst case
            cur = cur.next
        cur.next = new_node

    def __len__(self):
        """
        Length (for demo only)
        Time: O(n) to traverse entire list
        Space: O(1)
        """
        n, cur = 0, self.head
        while cur:
            n += 1
            cur = cur.next
        return n

    def to_list(self):
        """Helper to print. Time: O(n), Space: O(n) for the produced list (printing only)."""
        out, cur = [], self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out


# ----------------------------
# Core solution
# ----------------------------

class Solution:
    def GetNth(self, head, index):
        """
        Return the data of the 1-based 'index'th node; -1 if index invalid or out of bounds.
        Time:  O(n) — single pass up to index
        Space: O(1) — constant extra variables
        """
        # Guard: invalid index
        if index <= 0:                # O(1)
            return -1

        cur = head                    # O(1)
        pos = 1                       # O(1)

        # Walk until we reach the desired 1-based position (or list ends)
        while cur is not None and pos < index:   # Each loop O(1); total O(n)
            cur = cur.next
            pos += 1

        # If we found it, return node data; else -1
        return cur.data if (cur is not None and pos == index) else -1  # O(1)


# ----------------------------
# Demo / main with timing
# ----------------------------

def main():
    # Build example list
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:   # 5 items → list length is 5
        ll.append(v)

    print("Linked List:", ll.to_list())
    print("Length:", len(ll))

    # Indices to test (1-based): valid and invalid
    tests = [1, 3, 5, 6, 0, -2]

    sol = Solution()

    # Start timer for "full program run" (build + queries + prints)
    t0 = timer()

    for idx in tests:
        ans = sol.GetNth(ll.head, idx)   # O(n) per call worst-case (but < n average)
        print(f"Index = {idx:>2}  ->  Output = {ans}")

    t1 = timer()

    print(f"\nTotal run time (including building, queries, printing): {(t1 - t0) * 1000:.3f} ms")


if __name__ == "__main__":
    main()
```

#### Sample Output (illustrative)

```
Linked List: [1, 2, 3, 4, 5]
Length: 5
Index =  1  ->  Output = 1
Index =  3  ->  Output = 3
Index =  5  ->  Output = 5
Index =  6  ->  Output = -1
Index =  0  ->  Output = -1
Index = -2  ->  Output = -1

Total run time (including building, queries, printing): 0.47 ms
```

> Note: Your exact time will vary per machine.

---

## Real‑World Use Cases (just a few, high‑value)

1. **Streaming / Log Processing Pipelines**
   When you keep data as a linked structure (e.g., a chain of operations or events), you may need to fetch the *kth* event for sampling/monitoring or checkpoint recovery.

2. **Undo/Redo Stacks Implemented as Linked Nodes**
   Editors or CAD tools might implement actions as linked nodes; accessing the `k`th state from the beginning (or after a checkpoint) is a direct application.

3. **Runtime Schedulers / Task Chains**
   In lightweight task graphs linked by “next” pointers, fetching the `k`th task (e.g., for prefetch, visualization, or diagnostics) is the same operation.
