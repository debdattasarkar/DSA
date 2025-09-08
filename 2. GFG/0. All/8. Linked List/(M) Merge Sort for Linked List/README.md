# Merge Sort for Linked List

**Difficulty:** Medium
**Accuracy:** 74.76%
**Submissions:** 80K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

You are given the **head** of a linked list. You have to **sort the given linked list using Merge Sort**.

---

## Examples

### Example 1

**Input:**
`head -> 40 -> 20 -> 60 -> 10 -> 50 -> 30 -> NULL`

**Output:**
`10 -> 20 -> 30 -> 40 -> 50 -> 60`

**Explanation:**
After sorting the given linked list, the resultant list will be:
`head -> 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> NULL`

---

### Example 2

**Input:**
`head -> 9 -> 5 -> 2 -> 8 -> NULL`

**Output:**
`2 -> 5 -> 8 -> 9`

**Explanation:**
After sorting the given linked list, the resultant list will be:
`head -> 2 -> 5 -> 8 -> 9 -> NULL`

---

## Constraints

* `1 ≤ number of nodes ≤ 10^5`
* `0 ≤ node->data ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Paytm • Accolite • Amazon • Microsoft • MAQ Software • Adobe • Veritas

---

## Topic Tags

Linked List • Sorting • Merge Sort • Data Structures • Algorithms

---

## Related Interview Experiences

* Adobe Interview Experience Set 40 On Campus
* Maq Software Interview Experience Set 5
* Paytm Interview Experience Set 14 For Senior Android Developer
* Veritas Interview Experience Set 2 Campus
* Microsoft IDC Interview Experience Set 150 Full Time

---

## Related Articles

* [Merge Sort For Linked List](https://www.geeksforgeeks.org/merge-sort-for-linked-list/)

---

---


Here’s a crisp, interview-ready pack for **“Merge Sort for Linked List.”**

---

## 2) Intuition + step-by-step dry run

### Why merge sort for linked lists?

* **Split + merge** fits pointers naturally (no random access needed).
* **Stable**, **O(n log n)** time, and you can do it with **O(1) extra memory** (besides recursion stack).

### Key building blocks

1. **Find middle** with slow/fast pointers → split into two halves.
2. **Recursively** sort the halves.
3. **Merge** two sorted lists by pointer weaving.

### Dry run (top-down merge sort)

Input: `40 -> 20 -> 60 -> 10 -> 50 -> 30`

1. **Split 1** (slow/fast):

* slow stops at `60`, split into:

  * L: `40 -> 20 -> 60`
  * R: `10 -> 50 -> 30`

2. **Split L: 40->20->60** → mid=`20`:

* L1: `40 -> 20`
* L2: `60`
* L1 split again: `40` | `20` → merge → `20 -> 40`
* Merge `20->40` with `60` → `20 -> 40 -> 60`

3. **Split R: 10->50->30** → mid=`50`:

* R1: `10 -> 50`
* R2: `30`
* R1 split again: `10` | `50` → merge → `10 -> 50`
* Merge `10->50` with `30` → `10 -> 30 -> 50`

4. **Final merge**:

* Merge `20 -> 40 -> 60` and `10 -> 30 -> 50`
  → `10 -> 20 -> 30 -> 40 -> 50 -> 60` ✅

---

## 3) Python solutions (optimized + alternatives)

### A) Top-down merge sort (most expected)

```python
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        """
        Top-down merge sort on a singly linked list.
        Time:  O(n log n)
        Space: O(log n) recursion stack (pointer work is O(1))
        """
        if not head or not head.next:             # base case 0/1 node
            return head

        # 1) split by middle
        mid = self._get_mid(head)                 # left end's middle
        right = mid.next
        mid.next = None                           # break into [head..mid], [right..]

        # 2) sort halves
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(right)

        # 3) merge sorted halves
        return self._merge(left_sorted, right_sorted)

    def _get_mid(self, head):
        """Return node at end of left half (slow/fast)."""
        slow, fast = head, head.next
        # fast starts at head.next so mid becomes the left-middle for even length
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a, b):
        """Merge two sorted lists a & b, return head. O(len(a)+len(b)) time, O(1) extra."""
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:                 # stability: take from 'a' when equal
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a else b                # append remainder
        return dummy.next
```

### B) Iterative **bottom-up** merge sort (no recursion)

```python
class Solution:
    def mergeSort(self, head):
        """
        Bottom-up (iterative) merge sort to avoid recursion.
        Time:  O(n log n)
        Space: O(1) extra
        """
        if not head or not head.next:
            return head

        # compute length
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        dummy = Node(0)
        dummy.next = head
        size = 1

        # sublist size doubles each pass
        while size < n:
            prev, curr = dummy, dummy.next
            while curr:
                # split first block of size 'size'
                left = curr
                right = self._split(left, size)
                curr = self._split(right, size)   # next starting point

                # merge left & right, attach after 'prev'
                merged_head, merged_tail = self._merge_iter(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1
        return dummy.next

    def _split(self, head, size):
        """Cut list after 'size' nodes; return head of the remainder."""
        if not head:
            return None
        for _ in range(size - 1):
            if head.next:
                head = head.next
            else:
                break
        nxt = head.next
        head.next = None
        return nxt

    def _merge_iter(self, a, b):
        """Merge two sorted lists; return (head, tail)."""
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a else b

        # advance tail to the end
        while tail.next:
            tail = tail.next
        return dummy.next, tail
```

### C) Brute (array helper) — simplest but uses extra memory

> Collect values, sort, and **rewrite node data** (no pointer reweaving).
> Time `O(n log n)`, Space `O(n)`. Sometimes accepted, but less “linked-list-idiomatic.”

```python
class Solution:
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        vals = []
        p = head
        while p:
            vals.append(p.data)
            p = p.next
        vals.sort()
        p = head
        for v in vals:
            p.data = v
            p = p.next
        return head
```

---

## 4) Likely interviewer Q\&A

**Q1. Why prefer merge sort over quicksort for linked lists?**
Quicksort needs random access for good partitioning; linked lists don’t have it. Merge sort only needs sequential access and pointer weaving → **naturally efficient** and **stable**.

**Q2. What’s the complexity?**

* Time: **O(n log n)** (each level merges `n` nodes; there are `log n` levels).
* Space: **Top-down** uses **O(log n)** recursion stack; **bottom-up** is **O(1)** extra.

**Q3. How do you find the middle correctly?**
Use **slow/fast pointers**. Starting `fast = head.next` yields the **left middle** for even lengths, which prevents infinite loops when splitting.

**Q4. Is the algorithm stable?**
Yes—if you pick from the left list when values tie (`<=`), original relative order of equals is preserved.

**Q5. Edge cases to handle?**
Empty list, single node, all equal keys, already sorted, reverse sorted.

**Q6. Can you sort in descending order?**
Yes—just flip the comparison in the merge (`>=` vs `<=`).

**Q7. How to avoid recursion limits?**
Use the **bottom-up** iterative variant.

---

---

All set! I ran a **full inline Python program** that:

* Implements **merge sort for linked lists** in two ways:

  * **Top-down (recursive)** — classic, stable, O(n log n) time, O(log n) recursion stack, O(1) extra memory for pointers.
  * **Bottom-up (iterative)** — avoids recursion, still O(n log n) time, O(1) extra memory.
* Includes helpers to build/inspect linked lists.
* Prints inputs and outputs for the sample cases and a **large benchmark**, and uses **timeit** to report timings, plus the **TOTAL MAIN RUNTIME**.

```python

# Re-run to display outputs after the reset
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple, List
import random, timeit

@dataclass
class Node:
    data: int
    next: Optional['Node'] = None

def build_list(values: List[int]) -> Optional[Node]:
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def to_list(head: Optional[Node]) -> List[int]:
    out = []
    while head:
        out.append(head.data)
        head = head.next
    return out

class SolutionTopDown:
    def mergeSort(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        mid = self._get_mid(head)
        right = mid.next
        mid.next = None
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(right)
        return self._merge(left_sorted, right_sorted)

    def _get_mid(self, head: Node) -> Node:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next

class SolutionBottomUp:
    def mergeSort(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        dummy = Node(0)
        dummy.next = head
        size = 1
        while size < n:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = self._split(left, size)
                curr = self._split(right, size)
                merged_head, merged_tail = self._merge_runs(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1
        return dummy.next

    def _split(self, head: Optional[Node], size: int) -> Optional[Node]:
        if head is None:
            return None
        for _ in range(size - 1):
            if head.next is None:
                break
            head = head.next
        nxt = head.next
        head.next = None
        return nxt

    def _merge_runs(self, a: Optional[Node], b: Optional[Node]) -> Tuple[Optional[Node], Optional[Node]]:
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a else b
        while tail.next:
            tail = tail.next
        return dummy.next, tail

def main():
    print("=== Merge Sort for Linked List — Demo & Timing ===")

    vals1 = [40, 20, 60, 10, 50, 30]
    head1 = build_list(vals1)
    t0 = timeit.default_timer()
    out1_top = to_list(SolutionTopDown().mergeSort(head1))
    t1 = timeit.default_timer()

    vals2 = [9, 5, 2, 8]
    head2 = build_list(vals2)
    t2 = timeit.default_timer()
    out2_top = to_list(SolutionTopDown().mergeSort(head2))
    t3 = timeit.default_timer()

    print("\nExample 1 input :", vals1)
    print("Sorted (TopDown):", out1_top, f"   time={(t1 - t0):.6f}s")
    print("Expected        :", sorted(vals1))

    print("\nExample 2 input :", vals2)
    print("Sorted (TopDown):", out2_top, f"   time={(t3 - t2):.6f}s")
    print("Expected        :", sorted(vals2))

    head1_bu = build_list(vals1)
    head2_bu = build_list(vals2)
    t4 = timeit.default_timer()
    out1_bu = to_list(SolutionBottomUp().mergeSort(head1_bu))
    t5 = timeit.default_timer()
    t6 = timeit.default_timer()
    out2_bu = to_list(SolutionBottomUp().mergeSort(head2_bu))
    t7 = timeit.default_timer()
    print("\nSorted (BottomUp) ex1:", out1_bu, f"   time={(t5 - t4):.6f}s")
    print("Sorted (BottomUp) ex2:", out2_bu, f"   time={(t7 - t6):.6f}s")

    n = 120_000
    rand_vals = [random.randint(0, 10**6) for _ in range(n)]
    head_big_td = build_list(rand_vals)
    head_big_bu = build_list(rand_vals)

    t0 = timeit.default_timer()
    sorted_td = SolutionTopDown().mergeSort(head_big_td)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    sorted_bu = SolutionBottomUp().mergeSort(head_big_bu)
    t3 = timeit.default_timer()

    print(f"\nLarge n={n}:")
    print("Top-Down time  :", f"{(t1 - t0):.6f}s")
    print("Bottom-Up time :", f"{(t3 - t2):.6f}s")
    print("First 10 TD    :", to_list(sorted_td)[:10])
    print("First 10 BU    :", to_list(sorted_bu)[:10])

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (where LL merge sort shines)

* **Streaming/linked data pipelines:** When data arrives as linked chunks (e.g., log nodes) and you need a stable sort without converting to arrays.
* **External/blocked storage structures:** Sorting lists built from disk or network streams where **sequential access** is cheap and random access is expensive.
* **Stable sort in in-memory LLs:** Maintaining relative order of equal keys (e.g., sort by amount but keep original timestamp order for equal amounts).

