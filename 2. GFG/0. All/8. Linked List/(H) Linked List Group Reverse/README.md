# Linked List Group Reverse

**Difficulty:** Hard
**Accuracy:** 57.08%
**Submissions:** 259K+
**Points:** 8
**Average Time:** 30m

---

## Problem Statement

You are given the **head** of a Singly linked list. You have to **reverse every `k` node** in the linked list and return the head of the modified list.

**Note:** If the number of nodes is **not a multiple of `k`** then the left-out nodes at the end should be **considered as a group and must be reversed**.

---

## Examples

### Example 1

**Input:** `k = 2`,
`head`: `1 → 2 → 3 → 4 → 5 → 6 → NULL`

**Output:** `2 → 1 → 4 → 3 → 6 → 5`

**Explanation:** Linked List is reversed in groups of size `k = 2`.

---

### Example 2

**Input:** `k = 4`,
`head`: `1 → 2 → 3 → 4 → 5 → 6 → NULL`

**Output:** `4 → 3 → 2 → 1 → 6 → 5`

**Explanation:** Linked List is reversed in groups of size `k = 4`.

---

## Constraints

* `1 ≤ size of linked list ≤ 10^5`
* `0 ≤ node->data ≤ 10^6`
* `1 ≤ k ≤ size of linked list`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Paytm • VMWare • Accolite • Amazon • Microsoft • Snapdeal • Hike • MakeMyTrip • Walmart • Goldman Sachs • Adobe • SAP Labs

---

## Topic Tags

* Linked List
* Data Structures
* two-pointer-algorithm

---

## Related Interview Experiences

* Accolite Interview Experience Set 13 On Campus For Internship And FTE
* Vmware Interview Experience Set 3
* Paytm Interview Experience Set 4 Walk In Drive
* Paytm Interview Experience Set 9
* Makemytrip Interview Experience Set 4
* Makemytrip Interview Experience Set 14 Senior Android Developer
* Amazon Interview Experience For SDE 1 2 Years Experienced

---

## Related Articles

* [Reverse A Linked List In Groups Of Given Size Iterative Approach](https://www.geeksforgeeks.org/reverse-a-linked-list-in-groups-of-given-size-iterative-approach/)

---

---

Here’s an interview-ready pack for **Reverse Linked List in Groups of k (including the last short group)**.

---

## 2) Intuition + step-by-step dry run

We’re given the head of a **singly** linked list and an integer `k`. We must **reverse every k nodes** in order.
Unlike some variants, here **the remaining nodes at the end (size < k) must also be reversed**.

### Core idea (iterative, in-place, O(1) space)

Process the list chunk by chunk:

1. For the current chunk starting at `curr`, reverse **up to** `k` nodes by the normal 3-pointer technique (`prev`, `curr`, `nxt`).
2. Connect the **previous chunk’s tail** to the **new head** of this chunk.
3. Connect the **new tail** (which is the old chunk head) to the next chunk’s start.
4. Move on until `curr` becomes `None`.

We keep a `prev_tail` pointer to splice chunks together. For each chunk, record:

* `new_head` (the reversed chunk’s first node, i.e., `prev` after reversing),
* `new_tail` (the chunk’s original first node),
* `next_start` (the node after the chunk when we began reversing).

### Dry run (Example 1)

List: `1 → 2 → 3 → 4 → 5 → 6`, `k = 2`

* **Chunk 1:** reverse `1,2` → `2 → 1`, link into list → `2 → 1 → ...`
* **Chunk 2:** reverse `3,4` → `4 → 3`, link → `2 → 1 → 4 → 3 → ...`
* **Chunk 3:** reverse `5,6` → `6 → 5`, link → `2 → 1 → 4 → 3 → 6 → 5` ✅

### Dry run (Example 2)

List: `1 → 2 → 3 → 4 → 5 → 6`, `k = 4`

* **Chunk 1:** reverse `1,2,3,4` → `4 → 3 → 2 → 1`, link…
* **Chunk 2 (last, size 2 < k but must reverse):** reverse `5,6` → `6 → 5`
  Final: `4 → 3 → 2 → 1 → 6 → 5` ✅

Edge cases:

* `k = 1` → list unchanged.
* Single node / empty list → unchanged.
* `k` equal to list length → whole list reversed once.

---

## 3) Python solutions (brute → optimized), interview-style

### A) Optimized iterative, in-place (recommended)

```python
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        """
        Reverse the list in groups of size k; the last (short) group is also reversed.
        Time:  O(n)   — each node is visited and rewired once
        Space: O(1)   — in-place pointer rewiring
        """
        if head is None or k <= 1:
            return head

        def reverse_chunk(start, k):
            """
            Reverse up to k nodes starting at 'start'.
            Returns (new_head, new_tail, next_start)
              - new_head: head of the reversed chunk
              - new_tail: tail of the reversed chunk (original 'start')
              - next_start: node after the chunk before reversal
            """
            prev, curr = None, start
            cnt = 0
            while curr is not None and cnt < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt += 1
            # prev is new_head of chunk; start is new_tail; curr is next_start
            return prev, start, curr

        dummy = Node(0)
        dummy.next = head
        prev_tail = dummy       # tail of the previous processed chunk
        curr = head

        while curr:
            new_head, new_tail, next_start = reverse_chunk(curr, k)

            # splice the reversed chunk into the main list
            prev_tail.next = new_head
            new_tail.next = next_start

            # advance
            prev_tail = new_tail
            curr = next_start

        return dummy.next
```

### B) Recursive in-place (clean & short)

> Since the last group must be reversed even if its size < k, we reverse “up to k” nodes and recurse on the rest.

```python
class Solution:
    def reverseKGroup(self, head, k):
        """
        Time:  O(n)
        Space: O(n) recursion stack in the worst case
        """
        if head is None or k <= 1:
            return head

        # reverse up to k nodes
        prev, curr = None, head
        cnt = 0
        while curr is not None and cnt < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt += 1
        # 'prev' is new head of this reversed block, 'head' is new tail
        head.next = self.reverseKGroup(curr, k)
        return prev
```

### C) Brute / easy to explain: collect chunk nodes in an array and relink

> Clear to reason about, but uses extra memory.

```python
class Solution:
    def reverseKGroup(self, head, k):
        """
        Collect nodes in groups, reverse the references per group, relink.
        Time:  O(n)
        Space: O(k) per group (or O(n) worst case if you store all)
        """
        if head is None or k <= 1:
            return head

        dummy = Node(0); dummy.next = head
        prev_tail = dummy
        curr = head

        while curr:
            # collect up to k nodes
            group = []
            gcur = curr
            for _ in range(k):
                if gcur is None: break
                group.append(gcur)
                gcur = gcur.next

            # reverse the collected nodes (even if len < k)
            for i in range(len(group)-1, 0, -1):
                group[i].next = group[i-1]
            # connect previous tail to group's new head
            prev_tail.next = group[-1]
            # connect group's new tail to next_start
            group[0].next = gcur

            # move prev_tail & curr for next group
            prev_tail = group[0]
            curr = gcur

        return dummy.next
```

> If an interviewer insists on **O(1)** extra space, use (A) or (B). If they want clarity first, start with (C) and then optimize.

---

## 4) Typical interviewer Q\&A

**Q1. What’s the time/space complexity of your in-place solution?**
**A.** Time `O(n)` (every node visited once); Space `O(1)` iterative, or `O(n)` recursion stack in the recursive version.

**Q2. What happens when the remaining nodes are fewer than `k`?**
**A.** In this problem, they **must still be reversed** as a group. (This differs from some other versions like LeetCode 25, which leave them as-is.)

**Q3. Why use a dummy node?**
**A.** It simplifies edge cases when the **first chunk** becomes the new head after reversal; splicing is uniform for all chunks.

**Q4. What edge cases should we consider?**

* `k = 1` or empty list → return original head.
* `k` equals list length → reverse the entire list once.
* Repeated values — swap nodes, not data (the algorithm rewires pointers, so values are irrelevant).

**Q5. Can you do it in one pass without counting group length?**
**A.** Yes. Since we must reverse the last short group as well, we can **always reverse up to k** nodes and continue; no need to pre-check size (unlike the “leave last short group as-is” variant).

**Q6. How would you verify correctness quickly?**
**A.** Trace small lists (`k=2,3,4`) with both exact multiples and leftovers; ensure each chunk is locally reversed and that chunk boundaries are connected correctly (`prev_tail.next` and `new_tail.next`).

---

---

All set! I’ve executed a **full inline Python program** that:

* Implements `reverseKGroup` (iterative, in-place, `O(n)` time / `O(1)` space) which **also reverses the last short group**.
* Includes helpers to build/print linked lists.
* Prints **inputs and outputs** for multiple cases (including edge cases).
* Benchmarks on a `n=20000` list and shows the **TOTAL MAIN RUNTIME** using `timeit`.

```python

# Re-run to display outputs
from typing import Optional, List, Tuple
import timeit

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None

def build_ll(values: List[int]) -> Optional[Node]:
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

def ll_to_list(head: Optional[Node]) -> List[int]:
    out: List[int] = []
    cur = head
    while cur is not None:
        out.append(cur.data)
        cur = cur.next
    return out

class Solution:
    def reverseKGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        if head is None or k <= 1:
            return head

        def reverse_chunk(start: Node, k: int):
            prev = None
            curr = start
            cnt = 0
            while curr is not None and cnt < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                cnt += 1
            return prev, start, curr

        dummy = Node(0)
        dummy.next = head
        prev_tail = dummy
        curr = head
        while curr is not None:
            new_head, new_tail, next_start = reverse_chunk(curr, k)
            prev_tail.next = new_head
            new_tail.next = next_start
            prev_tail = new_tail
            curr = next_start
        return dummy.next

def main():
    sol = Solution()
    print("=== Reverse Linked List in Groups of k (last group also reversed) ===\n")
    arr1, k1 = [1,2,3,4,5,6], 2
    head1 = build_ll(arr1)
    print("Input 1:", arr1, "k =", k1)
    res1 = ll_to_list(sol.reverseKGroup(head1, k1))
    print("Output 1:", res1)
    arr2, k2 = [1,2,3,4,5,6], 4
    head2 = build_ll(arr2)
    print("\nInput 2:", arr2, "k =", k2)
    res2 = ll_to_list(sol.reverseKGroup(head2, k2))
    print("Output 2:", res2)
    arr3, k3 = [1,2,3,4,5], 3
    head3 = build_ll(arr3)
    print("\nInput 3:", arr3, "k =", k3)
    res3 = ll_to_list(sol.reverseKGroup(head3, k3))
    print("Output 3:", res3)
    arr4, k4 = [42], 5
    print("\nEdge 1:", arr4, "k =", k4)
    print("Output  :", ll_to_list(sol.reverseKGroup(build_ll(arr4), k4)))
    arr5, k5 = [], 3
    print("\nEdge 2:", arr5, "k =", k5)
    print("Output  :", ll_to_list(sol.reverseKGroup(build_ll(arr5), k5)))
    arr6, k6 = [1,2,3,4], 1
    print("\nEdge 3:", arr6, "k =", k6)
    print("Output  :", ll_to_list(sol.reverseKGroup(build_ll(arr6), k6)))
    n, kk = 20000, 3
    big = list(range(1, n+1))
    big_head = build_ll(big)
    t0 = timeit.default_timer()
    _ = sol.reverseKGroup(big_head, kk)
    t1 = timeit.default_timer()
    print(f"\nTiming on n={n}, k={kk}: {(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **Batch processing of streams:** Reverse chunks (windows) of items for time-based or count-based operations (e.g., log processing, telemetry).
* **Data structure operations:** Reversing sublists in **rope lists**, **text buffers**, or **editor history** where batch inversions are needed.
* **Scheduling & batching:** When tasks are grouped (e.g., by arrival) and then need to be processed in LIFO order within each group.
* **Networking & packets:** Reordering packets within bounded-size frames (window-based transforms).
* **Interview spin-offs:** Same technique underpins reversing **sublist ranges**, **k-alt reversal** (reverse k, skip k), or **pairwise swaps**—showing mastery of in-place pointer rewiring.

