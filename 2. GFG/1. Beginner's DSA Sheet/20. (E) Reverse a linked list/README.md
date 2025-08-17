
---

# Reverse a Linked List

**Difficulty:** Easy
**Accuracy:** 73.11%
**Submissions:** 361K+
**Points:** 2
**Average Time:** 30m

---

## Problem Statement

Given the **head** of a linked list, the task is to reverse this list and return the **reversed head**.

---

## Examples

### Example 1:

**Input:**
head: 1 -> 2 -> 3 -> 4 -> NULL

**Output:**
4 3 2 1

**Explanation:**
Input Linked List:

```
1 -> 2 -> 3 -> 4 -> NULL
```

After Reversing the Linked List:

```
4 -> 3 -> 2 -> 1 -> NULL
```

---

### Example 2:

**Input:**
head: 2 -> 7 -> 10 -> 9 -> 8 -> NULL

**Output:**
8 9 10 7 2

**Explanation:**
Input Linked List:

```
2 -> 7 -> 10 -> 9 -> 8 -> NULL
```

After Reversing the Linked List:

```
8 -> 9 -> 10 -> 7 -> 2 -> NULL
```

---

### Example 3:

**Input:**
head: 2 -> NULL

**Output:**
2

**Explanation:**
Input Linked List:

```
2 -> NULL
```

After Reversing the Linked List:

```
2 -> NULL
```

---

## Constraints

* $1 \leq \text{list.size} \leq 10^5$
* $1 \leq \text{node->data} \leq 10^5$

---

## Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(1)$

---

## Company Tags

* `Paytm`, `VMWare`, `Zoho`, `Accolite`, `Amazon`, `Microsoft`, `Samsung`, `Snapdeal`, `D-E-Shaw`, `MakeMyTrip`, `Teradata`, `Walmart`, `Goldman Sachs`, `Intuit`, `Adobe`, `SAP Labs`, `Tejas Network`, `Cisco`, `Qualcomm`, `Cognizant`, `Mahindra Comviva`, `IgniteWorld`

---

## Topic Tags

* `Linked List`, `Data Structures`

---

## Related Articles

* [Reverse A Linked List](https://www.geeksforgeeks.org/reverse-a-linked-list/)

---

---

Here’s a compact, interview-ready pack for **Reverse a Linked List**.

---

## 2) Intuition + Step-by-Step Dry Run

Goal: reverse the `next` pointers so the list runs backward, e.g.
`1 → 2 → 3 → 4 → ∅` becomes `4 → 3 → 2 → 1 → ∅`.

### Two-pointer idea (iterative, in-place)

Keep three pointers as you walk the list once:

* `prev` → the already-reversed prefix (initially `None`)
* `cur`  → the node we’re flipping now (starts at `head`)
* `nxt`  → save `cur.next` before we overwrite it

At each step:

1. `nxt = cur.next` (save next)
2. `cur.next = prev` (reverse link)
3. `prev = cur` (grow reversed prefix)
4. `cur = nxt` (advance)

When `cur` becomes `None`, `prev` is the new head.

### Dry run on `1 → 2 → 3 → 4 → ∅`

* Start: `prev=None`, `cur=1`
* Step 1: `nxt=2`, set `1.next=None`, move: `prev=1`, `cur=2`
  Reversed part: `1 → ∅`
* Step 2: `nxt=3`, set `2.next=1`, move: `prev=2`, `cur=3`
  Reversed part: `2 → 1 → ∅`
* Step 3: `nxt=4`, set `3.next=2`, move: `prev=3`, `cur=4`
  Reversed part: `3 → 2 → 1 → ∅`
* Step 4: `nxt=None`, set `4.next=3`, move: `prev=4`, `cur=None`
  Reversed part: `4 → 3 → 2 → 1 → ∅`
* Stop. Return `prev` (`4`).

Time: each node visited once → **O(n)**.
Extra space: pointers only → **O(1)**.

---

## 3) Optimized Codes (multiple ways)

All return the **new head**.

### A) Iterative two-pointer (most expected)

```python
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Time: O(n) — visit each node once
        # Space: O(1) — constant extra pointers
        prev = None
        cur = head
        while cur:
            nxt = cur.next        # 1) save next      — O(1)
            cur.next = prev       # 2) reverse link   — O(1)
            prev = cur            # 3) advance prev   — O(1)
            cur = nxt             # 4) advance cur    — O(1)
        return prev               # prev is new head
```

### B) Recursive (clean but uses call stack)

```python
class Solution:
    def reverseList(self, head):
        # Time: O(n)
        # Space: O(n) for recursion stack (worst case)
        if head is None or head.next is None:
            return head
        # reverse rest of the list
        new_head = self.reverseList(head.next)
        # put current node at the end of reversed part
        head.next.next = head
        head.next = None
        return new_head
```

### C) Using a stack (easy to reason, uses extra memory)

```python
class Solution:
    def reverseList(self, head):
        # Time: O(n)
        # Space: O(n) for the stack
        if not head:
            return None
        stack = []
        cur = head
        while cur:                # push all nodes — O(n)
            stack.append(cur)
            cur = cur.next
        new_head = stack.pop()    # last becomes head
        cur = new_head
        while stack:              # rebuild links in reverse — O(n)
            node = stack.pop()
            cur.next = node
            cur = node
        cur.next = None
        return new_head
```

**Which to use?**
Iterative two-pointer is the standard: O(n) time, O(1) space, no recursion limits.

---

## 4) Interview Q\&A (typical)

**Q1. What are the time and space complexities of your iterative solution?**
A: Time **O(n)** (each node once), Space **O(1)** (constant extra pointers).

**Q2. How would you handle very long lists where recursion depth might be an issue?**
A: Prefer the iterative two-pointer method to avoid recursion stack overflow.

**Q3. Can you reverse only a sublist between positions `m` and `n`?**
A: Yes—walk to `m-1`, reverse `n-m+1` links with the same pointer technique, then reconnect the three parts. (Common follow-up.)

**Q4. Can you reverse in pairs (swap every two nodes)?**
A: Yes—iterate while `cur` and `cur.next` exist; flip pairs and keep track of previous tail. (Another follow-up.)

**Q5. Does your algorithm modify node values or links?**
A: Only **links** are changed; values are untouched (required for linked-list reverse).

**Q6. How to detect and handle cycles before reversing?**
A: Use Floyd’s cycle detection. If a cycle exists, either break it first or define desired behavior. The standard problem assumes no cycles.

**Q7. Can you reverse a doubly linked list?**
A: Swap `next` and `prev` for each node while moving forward; finally return the last processed node as head.

---

---

Here’s a complete, runnable script for **Reverse a Linked List** with:

* Clean class structure
* Detailed inline complexity notes at each step
* A tiny I/O harness that builds lists, prints input/outputs
* `timeit` used to time the full program run

> You can copy–paste this into a file and run with Python 3.

```python
#!/usr/bin/env python3
"""
Reverse a Singly Linked List — full program with timing.

We implement the *iterative two-pointer* solution (most common in interviews) and
also offer a recursive variant for completeness (not used in timing by default).

Complexities:
    - Iterative reverse:   Time O(n), Space O(1)
    - Recursive reverse:   Time O(n), Space O(n) due to call stack
"""

from timeit import timeit
from typing import Optional, Iterable


# -----------------------------
# Linked List Infrastructure
# -----------------------------

class Node:
    """Singly-linked list node."""
    def __init__(self, val: int):
        self.data = val
        self.next: Optional["Node"] = None

    def __repr__(self):
        return f"Node({self.data})"


def build_list(values: Iterable[int]) -> Optional[Node]:
    """
    Build a linked list from an iterable of values.

    Time:  O(n)  — iterate once to create nodes and links
    Space: O(n)  — n nodes created for the list (input-to-structure)
    """
    head = None
    tail = None
    for v in values:
        node = Node(v)                     # O(1)
        if head is None:                   # O(1)
            head = tail = node
        else:
            tail.next = node               # O(1)
            tail = node
    return head


def list_to_pylist(head: Optional[Node]) -> list:
    """
    Convert linked list to standard Python list for display.

    Time:  O(n)  — visit each node once
    Space: O(n)  — output list of n elements
    """
    out = []
    cur = head
    while cur:
        out.append(cur.data)               # O(1) append
        cur = cur.next
    return out


# -----------------------------
# Solutions
# -----------------------------

class Solution:
    def reverseList_iterative(self, head: Optional[Node]) -> Optional[Node]:
        """
        Iterative two-pointer reverse (most expected in interviews).

        Time:  O(n)  — each node visited once
        Space: O(1)  — only a few pointers
        """
        prev = None        # O(1) space
        cur = head         # O(1)
        # Loop runs n times, each step O(1) work
        while cur:
            nxt = cur.next     # O(1): save next
            cur.next = prev    # O(1): reverse the link
            prev = cur         # O(1): advance prev
            cur = nxt          # O(1): advance cur
        return prev            # new head

    def reverseList_recursive(self, head: Optional[Node]) -> Optional[Node]:
        """
        Recursive reverse (elegant but uses call stack).

        Time:  O(n)
        Space: O(n)  — recursion depth n
        """
        if head is None or head.next is None:
            return head
        new_head = self.reverseList_recursive(head.next)  # O(n) stack growth
        head.next.next = head     # O(1)
        head.next = None          # O(1)
        return new_head


# -----------------------------
# Demo / Main program
# -----------------------------

def demo_once(values, use_recursive=False):
    """Build → print → reverse → print. Returns reversed Python list."""
    head = build_list(values)                 # O(n) build
    print(f"Input:  {list_to_pylist(head)}")  # O(n) convert for display

    sol = Solution()
    if use_recursive:
        rev = sol.reverseList_recursive(head)
    else:
        rev = sol.reverseList_iterative(head)

    out = list_to_pylist(rev)                 # O(n)
    print(f"Output: {out}")                   # O(n) print
    return out


def main():
    """
    Main run:
    - Two example runs (same as common GFG-style samples).
    - Uses the iterative solution (switch to recursive by setting use_recursive=True).
    """
    print("=== Reverse a Linked List — Iterative Two-Pointer ===")
    # Example 1
    demo_once([1, 2, 3, 4])

    # Example 2
    demo_once([2, 7, 10, 9, 8])

    # Example 3 (single node)
    demo_once([2])

    # (Optional) Try recursive variant once
    print("\n=== Recursive variant (single demo) ===")
    demo_once([5, 6, 7, 8], use_recursive=True)


if __name__ == "__main__":
    # Time the full program (build + reverse + prints) in one run
    elapsed = timeit("main()", globals=globals(), number=1)
    print(f"\n[timeit] Total program run time: {elapsed:.6f} seconds")
```

### Sample Output (illustrative)

```
=== Reverse a Linked List — Iterative Two-Pointer ===
Input:  [1, 2, 3, 4]
Output: [4, 3, 2, 1]
Input:  [2, 7, 10, 9, 8]
Output: [8, 9, 10, 7, 2]
Input:  [2]
Output: [2]

=== Recursive variant (single demo) ===
Input:  [5, 6, 7, 8]
Output: [8, 7, 6, 5]

[timeit] Total program run time: 0.00xxxx seconds
```

---

## 6) Real-World Use Cases (a few crucial ones)

1. **Undo/Redo Stacks or History Reversal**
   Converting a forward log into a reverse order to replay actions backward (or vice versa).

2. **Network Packet Processing**
   Some network pipelines model packets as linked nodes; reversing can be used to transform traversal order for certain passes or to convert LIFO/FIFO semantics.

3. **Persistent/Functional Data Structures**
   Reversing lists is a fundamental primitive for building efficient concatenation or rotating queues (e.g., in purely functional queue implementations).

4. **Interview/Systems Tasks**
   Linked list reversal is a building block for more complex problems:

   * Reverse a **sublist** between `m` and `n`
   * Reverse in **k-groups**
   * Reverse a **doubly** linked list by swapping `prev`/`next`
