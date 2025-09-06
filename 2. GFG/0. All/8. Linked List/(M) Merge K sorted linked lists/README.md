# Merge K sorted linked lists

**Difficulty:** Medium
**Accuracy:** 57.01%
**Submissions:** 113K+
**Points:** 4
**Average Time:** 60m

---

## Problem Statement

Given an array `arr[]` of **n sorted linked lists** of different sizes. Your task is to **merge** all these lists into a single **sorted** linked list and **return the head** of the merged list.

---

## Examples

### Example 1

**Input:**

```
arr[] =
  head1: 1 → 3 → 7 → NULL
  head2: 2 → 4 → 8 → NULL
  head3: 9 → NULL
```

**Output:**
`1 → 2 → 3 → 4 → 7 → 8 → 9`

**Explanation:**
The `arr[]` has 3 sorted linked lists of size 3, 3, 1.
The merged list will be `1 → 2 → 3 → 4 → 7 → 8 → 9`.

---

### Example 2

**Input:**

```
arr[] =
  head1: 1 → 3 → NULL
  head2: 8 → NULL
  head3: 4 → 5 → 6 → NULL
```

**Output:**
`1 → 3 → 4 → 5 → 6 → 8`

**Explanation:**
The `arr[]` has 3 sorted linked lists of size 2, 1, 3.
The merged list will be `1 → 3 → 4 → 5 → 6 → 8`.

---

## Constraints

* `1 ≤ total no. of nodes ≤ 10^5`
* `1 ≤ node->data ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

VMWare • Amazon • Microsoft • Oracle

---

## Topic Tags

* Linked List
* Heap
* Data Structures
* Merge Sort
* two-pointer-algorithm

---

## Related Interview Experiences

* Vmware Interview Set 1 For Mts 2 Position

---

## Related Articles

* [Merge K Sorted Linked Lists](https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/)

---

---

Here’s an interview-ready guide for **Merge K Sorted Linked Lists**.

---

## 2) Intuition + step-by-step dry run

### What we want

Input: an array `arr` of `k` heads of **sorted** singly linked lists.
Goal: produce a single **sorted** list by **reusing the existing nodes** (no new nodes).

### Two mainstream ways (both are expected in interviews)

1. **Min-Heap (priority queue):**
   Put the *current* head of each list in a min-heap keyed by node value.
   Repeatedly pop the smallest node and append it to the answer; if that node had a `next`, push it.

   * Time: **O(N log k)** (N = total nodes)
   * Space: **O(k)** for the heap

2. **Divide & Conquer (pairwise merging):**
   Repeatedly merge lists in pairs like merge sort: merge #0 with #1, #2 with #3, … then repeat on the merged set.

   * Each merge is linear; depth is `⌈log2 k⌉`
   * Time: **O(N log k)**
   * Space: **O(1)** extra (iterative merge uses pointers)

> Brute ideas for completeness:
>
> * **Flatten & sort values, rebuild nodes** → **O(N log N)** and **allocates new nodes** (usually not preferred).
> * **Sequentially merge left-to-right** → **O(kN)** (OK but slower when k is big).

---

### Dry run (Min-Heap) on Example 1

```
arr:
  L1: 1 → 3 → 7
  L2: 2 → 4 → 8
  L3: 9
```

* Push heads: heap = \[(1,L1), (2,L2), (9,L3)]
* Pop 1 → output: 1; push 3 → heap = \[(2,L2), (9,L3), (3,L1)]
* Pop 2 → output: 1→2; push 4 → heap = \[(3,L1), (9,L3), (4,L2)]
* Pop 3 → output: 1→2→3; push 7 → heap = \[(4,L2), (9,L3), (7,L1)]
* Pop 4 → output: 1→2→3→4; push 8 → heap = \[(7,L1), (9,L3), (8,L2)]
* Pop 7 → output: …→7; L1 empty
* Pop 8 → output: …→8; L2 empty
* Pop 9 → output: …→9; L3 empty; heap empty → done

Result: `1 → 2 → 3 → 4 → 7 → 8 → 9`.

---

## 3) Python solutions (brute & optimized), with inline interview-style comments

The platform usually provides a `Node` with fields `.data` and `.next`.
We **do not** allocate new nodes—just rewire pointers.

### A) Min-Heap (Priority Queue) — most common answer

```python
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

import heapq

class Solution:
    def mergeKLists(self, arr):
        """
        Merge k sorted linked lists using a min-heap of size at most k.
        Time:  O(N log k)  (N total nodes)
        Space: O(k)        (heap holds at most one node per list)
        """
        # Edge case: no lists
        if not arr:
            return None

        # Min-heap entries are tuples: (node_value, unique_id, node)
        # unique_id breaks ties so Python doesn't need to compare Node objects.
        heap = []
        uid = 0
        for head in arr:
            if head:  # skip empty lists
                heapq.heappush(heap, (head.data, uid, head))
                uid += 1

        dummy = Node(0)  # sentinel to build the result easily
        tail = dummy

        while heap:
            _, _, node = heapq.heappop(heap)  # smallest node
            tail.next = node                  # append this node
            tail = tail.next                  # advance tail

            if node.next:                     # push next node from same list
                heapq.heappush(heap, (node.next.data, uid, node.next))
                uid += 1

        tail.next = None  # ensure the merged list terminates
        return dummy.next
```

### B) Divide & Conquer (pairwise merge) — equally acceptable, elegant

```python
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        """
        Pairwise merge lists like merge sort.
        Time:  O(N log k)
        Space: O(1) extra (in-place merges using pointers)
        """
        if not arr:
            return None
        # Remove empties for convenience
        lists = [h for h in arr if h]

        if not lists:
            return None

        # Keep merging pairs until one list remains
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self._merge_two(l1, l2))
            lists = merged
        return lists[0]

    def _merge_two(self, a, b):
        """Standard merge of two sorted linked lists, reusing nodes.
        Time:  O(len(a)+len(b)), Space: O(1) extra."""
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:
                tail.next = a; a = a.next
            else:
                tail.next = b; b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next
```

### C) Brute (flatten values and sort) — simple but not preferred

```python
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        """
        Flatten values, sort, then rebuild nodes.
        Time:  O(N log N)
        Space: O(N) for values
        Not preferred: allocates new nodes and ignores the 'reuse nodes' intent.
        """
        vals = []
        for head in arr:
            cur = head
            while cur:
                vals.append(cur.data)
                cur = cur.next
        if not vals:
            return None
        vals.sort()
        # Rebuild a fresh list
        dummy = Node(0)
        tail = dummy
        for v in vals:
            tail.next = Node(v)
            tail = tail.next
        return dummy.next
```

---

## 4) Likely interviewer Q\&A

**Q1. Which approach do you prefer and why?**

* **Min-heap** is very common: simple to code, predictable **O(N log k)**.
* **Divide & conquer** is also **O(N log k)** and avoids heap overhead; great when you’re comfortable with merging.

**Q2. What if some lists are empty?**
Just skip pushing `None` heads into the heap (or filter empties before divide-and-conquer). The code above handles that.

**Q3. Why do you include a `unique_id` with the heap tuple?**
Python can’t compare `Node` objects when values tie. `(value, uid, node)` ensures ties are broken by `uid`, avoiding `TypeError`.

**Q4. Can you guarantee stability (relative order of equal values)?**
For linked lists the notion of “stability across lists” is irrelevant—nodes with equal values can interleave arbitrarily. Within a single list, order is preserved because we always advance from it in order.

**Q5. Space complexity?**

* Heap: **O(k)** extra; output reuses nodes so no extra list memory.
* Divide & conquer: **O(1)** extra beyond a few pointers (iterative version).

**Q6. Edge cases to test?**

* `k = 0` (empty `arr`) → `None`
* All lists empty → `None`
* One list only → same list returned
* Duplicate values across lists
* Very skewed sizes (one huge list + many tiny lists)

**Q7. Can we do better than `O(N log k)`?**
No, in comparison-based merging you can’t beat `Ω(N log k)` in general. Both heap and pairwise merging meet that bound.

---

---

All set! I ran a **complete inline Python program** that:

* Implements two optimal approaches for merging k sorted linked lists:

  * **Min-Heap** (`mergeKLists_heap`) — `O(N log k)` time, `O(k)` extra space.
  * **Divide & Conquer** (`mergeKLists_divide`) — `O(N log k)` time, \~`O(1)` extra space (pointer-only).
* Includes clean helpers to build and print lists.
* Shows outputs for the two sample inputs, a few edge cases, and a large benchmark (`N=100,000`, `k=50`) with **timeit** measurements.
* Reuses existing nodes (no unnecessary allocations).

```python

# Re-run to display outputs after the reset
from typing import List, Optional, Tuple
import heapq
import timeit

class Node:
    def __init__(self, x: int):
        self.data = x
        self.next: Optional["Node"] = None

def build_ll(values: List[int]) -> Optional[Node]:
    head = tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def to_pylist(head: Optional[Node]) -> List[int]:
    out = []
    cur = head
    while cur:
        out.append(cur.data)
        cur = cur.next
    return out

def arr_heads_to_lists(arr: List[Optional[Node]]) -> List[List[int]]:
    return [to_pylist(h) for h in arr]

class Solution:
    def mergeKLists_heap(self, arr: List[Optional[Node]]) -> Optional[Node]:
        if not arr:
            return None
        heap: List[Tuple[int, int, Node]] = []
        uid = 0
        for head in arr:
            if head:
                heapq.heappush(heap, (head.data, uid, head))
                uid += 1
        dummy = Node(0)
        tail = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.data, uid, node.next))
                uid += 1
        tail.next = None
        return dummy.next

    def mergeKLists_divide(self, arr: List[Optional[Node]]) -> Optional[Node]:
        if not arr:
            return None
        lists = [h for h in arr if h]
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i + 1 < len(lists) else None
                merged.append(self._merge_two(a, b))
            lists = merged
        return lists[0]

    def _merge_two(self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        if a is None: return b
        if b is None: return a
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.data <= b.data:
                tail.next = a; a = a.next
            else:
                tail.next = b; b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next

def main():
    sol = Solution()
    print("=== Merge K Sorted Linked Lists — Demo & Timing ===")
    arr1 = [build_ll([1,3,7]), build_ll([2,4,8]), build_ll([9])]
    print("\nInput 1 (array of lists):", arr_heads_to_lists(arr1))
    t0 = timeit.default_timer()
    merged1 = sol.mergeKLists_heap(arr1)
    t1 = timeit.default_timer()
    print("Output 1 (heap):", to_pylist(merged1))
    print(f"Time (heap): {(t1 - t0):.6f}s")
    arr2 = [build_ll([1,3]), build_ll([8]), build_ll([4,5,6])]
    print("\nInput 2 (array of lists):", arr_heads_to_lists(arr2))
    t0 = timeit.default_timer()
    merged2 = sol.mergeKLists_divide(arr2)
    t1 = timeit.default_timer()
    print("Output 2 (divide&conquer):", to_pylist(merged2))
    print(f"Time (divide): {(t1 - t0):.6f}s")
    empty_arr = []
    one_list = [build_ll([1,2,3])]
    with_empty = [None, build_ll([2,2,2]), None]
    print("\nEdge: empty arr ->", to_pylist(sol.mergeKLists_heap(empty_arr)))
    print("Edge: one list ->", to_pylist(sol.mergeKLists_divide(one_list)))
    print("Edge: mixed empties ->", to_pylist(sol.mergeKLists_heap(with_empty)))
    k = 50
    N = 100_000
    buckets = [[] for _ in range(k)]
    for v in range(1, N+1):
        buckets[(v-1) % k].append(v)
    lists = [build_ll(b) for b in buckets]
    t0 = timeit.default_timer()
    merged_big_heap = sol.mergeKLists_heap(lists)
    t1 = timeit.default_timer()
    print(f"\nLarge test: N={N}, k={k}, heap time={(t1 - t0):.6f}s, first 10 -> {to_pylist(merged_big_heap)[:10]}")
    lists2 = [build_ll(b) for b in buckets]
    t2 = timeit.default_timer()
    merged_big_div = sol.mergeKLists_divide(lists2)
    t3 = timeit.default_timer()
    print(f"Large test: N={N}, k={k}, divide time={(t3 - t2):.6f}s, last 10  -> {to_pylist(merged_big_div)[-10:]}")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")

```

---

## 6) Real-World Use Cases (high-impact)

* **External/Big-data merge**: Merging many already-sorted runs (from map tasks or spill files) into one global sorted stream—exactly like a k-way merge in external sort.
* **Log aggregation**: Joining multiple time-sorted log streams (microservices, shards) into a single chronological feed.
* **Search indexing**: Merging sorted posting lists (per term or shard) during index construction/compaction.
* **Streaming ETL**: Consolidating multiple sorted sources (e.g., Kafka partitions ordered by key/timestamp) into one ordered output.
* **Database internals**: LSM-tree compaction and multi-way merge of sorted SSTables/pages.
