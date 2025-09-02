# Reverse a Doubly Linked List

**Difficulty:** Easy
**Accuracy:** 70.38%
**Submissions:** 192K+
**Points:** 2
**Average Time:** 15m

---

## Problem Statement

You are given the **head** of a **doubly linked list**. You have to **reverse** the doubly linked list and **return its head**.

---

## Examples

### Example 1

**Input:**
List: `NULL ←→ 3 ←→ 4 ←→ 5 ←→ NULL`

**Output:**
`5 ←→ 4 ←→ 3`

**Explanation:**
After reversing the given doubly linked list the new list will be `5 ←→ 4 ←→ 3`.

---

### Example 2

**Input:**
List: `NULL ←→ 75 ←→ 122 ←→ 59 ←→ 196 ←→ NULL`

**Output:**
`196 ←→ 59 ←→ 122 ←→ 75`

**Explanation:**
After reversing the given doubly linked list the new list will be `196 ←→ 59 ←→ 122 ←→ 75`.

---

## Constraints

* `1 ≤ number of nodes ≤ 10^6`
* `0 ≤ node->data ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* D-E-Shaw
* Adobe

---

## Topic Tags

* doubly-linked-list
* Data Structures

---

## Related Articles

* [Reverse A Doubly Linked List](https://www.geeksforgeeks.org/reverse-a-doubly-linked-list/)

---

---

Here’s an interview-ready guide to **Reverse a Doubly Linked List**.

---

## 2) Intuition + step-by-step dry run

A doubly linked list node has two pointers:

* `next` → forward neighbor
* `prev` → backward neighbor

To **reverse** the list **in place**, we can iterate through nodes and **swap** each node’s `next` and `prev`. After swapping, the “forward” direction has flipped, so to continue the traversal we must move using the **new** `next` (which used to be `prev`). An easy way to express that is: after swapping, advance with `curr = curr.prev`.

We also track the **last node we touched** (after swapping) as `new_head`. When the loop finishes, that last node is the head of the reversed list.

### Dry run

List: `NULL ←→ 3 ←→ 4 ←→ 5 ←→ NULL` (head = 3)

Start: `curr = 3`, `new_head = None`

1. `curr = 3`

   * Before: `prev(None), next(4)`
   * Swap: `prev ←→ next` → `prev = 4`, `next = None`
   * Update `new_head = 3`
   * Move: `curr = curr.prev` (which is `4`)

2. `curr = 4`

   * Before: `prev(3), next(5)` (original list)
   * Swap: `prev = 5`, `next = 3`
   * Update `new_head = 4`
   * Move: `curr = curr.prev` → `5`

3. `curr = 5`

   * Before: `prev(4), next(None)`
   * Swap: `prev = None`, `next = 4`
   * Update `new_head = 5`
   * Move: `curr = curr.prev` → `None` → stop

Return `new_head = 5`
Reversed list: `NULL ←→ 5 ←→ 4 ←→ 3 ←→ NULL` ✅

Edge cases:

* Empty list → return `None`.
* Single node → swap makes no change; return that node.

---

## 3) Python solutions (expected in interviews)

### A) Iterative in-place swap (canonical)

```python
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        """
        Reverse a doubly linked list by swapping next/prev at each node.
        - Time:  O(n)  (touch each node once)
        - Space: O(1)  (in-place)

        Steps:
          1) Walk curr from head to tail.
          2) For each curr: swap curr.next and curr.prev.
          3) After swap, move curr = curr.prev  (because links swapped).
          4) Track 'new_head' as the last node processed.
        """
        curr = head
        new_head = None
        while curr:
            # swap pointers
            curr.prev, curr.next = curr.next, curr.prev
            # record potential new head
            new_head = curr
            # move forward in the *reversed* sense
            curr = curr.prev
        return new_head
```

### B) Recursive in-place (elegant, same complexity)

```python
class Solution:
    def reverse(self, head):
        """
        Recursive reversal.
        - Swap next/prev at current node.
        - If after swapping, curr.prev is None, we reached new head.
        - Otherwise recurse on curr.prev (which is the original next).

        Time:  O(n), Space: O(n) due to recursion stack
        """
        if head is None:
            return None

        # swap
        head.prev, head.next = head.next, head.prev

        # if prev is now None, we are at new head
        if head.prev is None:
            return head
        # otherwise continue recursively
        return self.reverse(head.prev)
```

### C) “Brute” using an auxiliary stack / array (not preferred)

* Traverse list, push nodes (or values) into a stack, then rebuild or rewire.
* **Time:** `O(n)`; **Space:** `O(n)` extra.
  Interviewers generally **prefer A** (in-place, `O(1)` space) unless they ask for a different approach.

---

## 4) Likely interviewer Q\&A

**Q1. Why set `curr = curr.prev` after swapping?**
Because after swapping `next` and `prev`, the node that was originally to the **right** of `curr` is now referenced by `curr.prev`. Moving to `curr.next` would go back.

**Q2. What is the time and space complexity?**
Iterative in-place: **Time `O(n)`**, **Aux space `O(1)`**.
Recursive: **Time `O(n)`**, **Aux space `O(n)`** (call stack).

**Q3. How do you update the head?**
Keep a `new_head` updated to the last processed node in the loop (or in the recursive version, return when `prev` becomes `None`).

**Q4. What about empty or single-node lists?**
Both are handled naturally: loop runs zero or one iteration; return the same node (or `None`).

**Q5. Any pitfalls?**

* Forgetting to move `curr = curr.prev` after swap (you’ll loop incorrectly).
* Not updating `head`/`new_head` → you’ll return the original head.
* Accidentally breaking links by only updating one of the two pointers.

**Q6. How would this differ for a singly linked list?**
You’d need a classic reversal with three pointers (`prev`, `curr`, `nxt`) since there’s no `prev` pointer to swap; complexity remains `O(n)` time, `O(1)` space.

---

---

All set! I executed a **full inline Python program** that:

* Builds doubly linked lists from arrays,
* Reverses them **in place** (iterative `O(n)` / `O(1)`), with an optional recursive variant,
* Prints **inputs and outputs**, plus a backward traversal check to confirm `prev` links,
* And prints the **TOTAL MAIN RUNTIME** using `timeit.default_timer()`.

```python

# Re-run to display outputs
from typing import Optional, List
import timeit

class Node:
    def __init__(self, val: int):
        self.data = val
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None

def build_dll(values: List[int]) -> Optional[Node]:
    head = None
    prev = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
            node.prev = prev
        prev = node
    return head

def dll_to_list(head: Optional[Node]) -> List[int]:
    out = []
    cur = head
    while cur:
        out.append(cur.data)
        cur = cur.next
    return out

def dll_to_list_reverse(tail: Optional[Node]) -> List[int]:
    out = []
    cur = tail
    while cur:
        out.append(cur.data)
        cur = cur.prev
    return out

def tail_of(head: Optional[Node]) -> Optional[Node]:
    cur = head
    last = None
    while cur:
        last = cur
        cur = cur.next
    return last

class Solution:
    def reverse(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        new_head = None
        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            new_head = curr
            curr = curr.prev
        return new_head

    def reverse_recursive(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        head.prev, head.next = head.next, head.prev
        if head.prev is None:
            return head
        return self.reverse_recursive(head.prev)

def main():
    sol = Solution()
    print("=== Reverse a Doubly Linked List — Demo ===")
    vals1 = [3, 4, 5]
    head1 = build_dll(vals1)
    print("\nInput 1:", dll_to_list(head1))
    new_head1 = sol.reverse(head1)
    print("Output 1:", dll_to_list(new_head1))
    print("Backwards check:", dll_to_list_reverse(tail_of(new_head1)))
    vals2 = [75, 122, 59, 196]
    head2 = build_dll(vals2)
    print("\nInput 2:", dll_to_list(head2))
    new_head2 = sol.reverse(head2)
    print("Output 2:", dll_to_list(new_head2))
    print("Backwards check:", dll_to_list_reverse(tail_of(new_head2)))
    head3 = build_dll([42])
    print("\nEdge (single):", dll_to_list(head3))
    print("Reversed:", dll_to_list(sol.reverse(head3)))
    head4 = build_dll([])
    print("\nEdge (empty):", dll_to_list(head4))
    print("Reversed:", dll_to_list(sol.reverse(head4)))

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **Text editors / browser history:** Doubly linked lists are used to move back and forth; reversing can support “undo stack” transformations or reordering.
* **Media playlists & queues:** Flip playback order efficiently without rebuilding the list.
* **Bidirectional caches / LRU lists:** Some maintenance operations involve reversing or rotating segments while keeping `prev`/`next` integrity.
* **Path reconstruction / UI navigation:** When a breadcrumb or navigation trail needs to be inverted for display or processing.

