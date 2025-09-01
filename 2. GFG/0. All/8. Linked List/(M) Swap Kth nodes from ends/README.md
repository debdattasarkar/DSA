# Swap Kth nodes from ends

**Difficulty:** Medium
**Accuracy:** 35.5%
**Submissions:** 63K+
**Points:** 4
**Average Time:** 45m

---

## Problem Statement

Given the **head** of a singly linked list and an integer **k**. **Swap the k<sup>th</sup> node (1-based index) from the beginning and the k<sup>th</sup> node from the end** of the linked list.
Return the head of the final formed list and **if it's not possible** to swap the nodes **return the original list**.

---

## Examples

### Example 1

**Input:** `k = 1`,
`head`: `1 → 2 → 3 → 4 → 5 → NULL`

**Output:**
`5 → 2 → 3 → 4 → 1 → NULL`

**Explanation:**
Here `k = 1`, hence after swapping the 1st node from the beginning and end the new list will be `5 → 2 → 3 → 4 → 1`.

---

### Example 2

**Input:** `k = 2`,
`head`: `5 → 10 → 8 → 5 → 9 → 3 → NULL`

**Output:**
`5 → 9 → 8 → 5 → 10 → 3 → NULL`

**Explanation:**
Here `k = 2`, hence after swapping the 2nd node from the beginning and end the new list will be `5 → 9 → 8 → 5 → 10 → 3`.

---

## Constraints

* `1 ≤ list size ≤ 10^4`
* `1 ≤ node->data ≤ 10^6`
* `1 ≤ k ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Morgan Stanley
* Amazon

---

## Topic Tags

* Linked List
* Data Structures

---

## Related Articles

* *[Swap Kth Node From Beginning With Kth Node From End In A Linked List](https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/)*

---

---

Here’s a crisp, interview-ready pack for **“Swap k-th nodes from beginning and end (1-based)”**.

---

## 2) Idea + step-by-step dry run

We need to swap the **k-th node from the start** with the **k-th node from the end** (i.e., the `(n-k+1)`-th from the start) in a **singly** linked list. Return the (possibly new) head.
If `k > n` → impossible → return original.
If both nodes are the same (`k == n-k+1`) → no change.

### Why we need “prev” pointers

In a singly list we can’t go backwards. To splice nodes we must also know their **previous** nodes (`prev1`, `prev2`) so we can redirect `next` links.

### Adjacency corner cases

If the two nodes are **adjacent** (e.g., `node1.next is node2` or vice-versa), a generic “swap next pointers” can create a self-loop. We handle these two tiny cases explicitly.

### Dry run (matches picture #2)

List: `5 → 10 → 8 → 5 → 9 → 3 → ∅`, `k = 2`
Length `n = 6`, so the second from end is index `(6-2+1)=5` → node `10` ↔ node `9`.

* `node1 = 10`, `prev1 = 5`
* `node2 = 9`,  `prev2 = 5 (the second 5)`
* Not adjacent? (Here, nodes are separated by `8`, `5`) → generic swap

  * `prev1.next -> node2`
  * `prev2.next -> node1`
  * swap `node1.next` and `node2.next`
    Result: `5 → 9 → 8 → 5 → 10 → 3 → ∅` ✅

---

## 3) Python solutions (interview-style)

### A) Swap the **nodes (pointers)** — O(n) time, O(1) space (preferred when problem says “swap nodes”)

```python
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        """
        Swaps the k-th node from start with k-th from end (1-based).
        Time:  O(n)  (single pass to get length + two short scans)
        Space: O(1)
        """
        if head is None:
            return head

        # 1) Compute length n
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 2) If k out of range or same node -> no change
        if k < 1 or k > n:
            return head
        if k == n - k + 1:  # same node
            return head

        # Helper to fetch (prev, node) for the p-th node from start (1-based)
        def get_prev_and_node(head, p):
            prev = None
            cur = head
            for _ in range(p - 1):
                prev = cur
                cur = cur.next
            return prev, cur

        # 3) Identify both nodes (and their prevs)
        prev1, node1 = get_prev_and_node(head, k)
        prev2, node2 = get_prev_and_node(head, n - k + 1)

        # 4) Handle adjacency explicitly (two cases)
        if node1.next is node2:  # node1 immediately before node2
            if prev1: prev1.next = node2
            else:     head = node2
            node1.next = node2.next
            node2.next = node1
            return head

        if node2.next is node1:  # node2 immediately before node1
            if prev2: prev2.next = node1
            else:     head = node1
            node2.next = node1.next
            node1.next = node2
            return head

        # 5) Non-adjacent: swap links via prev1/prev2 and swap next pointers
        if prev1: prev1.next = node2
        else:     head = node2
        if prev2: prev2.next = node1
        else:     head = node1

        node1.next, node2.next = node2.next, node1.next
        return head
```

### B) Same pointer-swap but **one pass** to find the k-th from end (two-pointer trick)

```python
class Solution:
    def swapKth(self, head, k):
        """
        Find k-th from start, then use a runner to find k-th from end in one sweep.
        Time:  O(n)
        Space: O(1)
        """
        if not head:
            return head

        # Find k-th from start (node1) and its prev
        prev1 = None
        node1 = head
        for _ in range(k - 1):
            if not node1:  # k > n
                return head
            prev1 = node1
            node1 = node1.next
        if not node1:      # k > n
            return head

        # Use runner from node1 to the end to locate k-th from end
        fast = node1
        prev2 = None
        node2 = head
        while fast and fast.next:
            fast = fast.next
            prev2 = node2
            node2 = node2.next

        if node1 is node2:
            return head

        # Adjacency cases
        if node1.next is node2:
            if prev1: prev1.next = node2
            else:     head = node2
            node1.next = node2.next
            node2.next = node1
            return head
        if node2.next is node1:
            if prev2: prev2.next = node1
            else:     head = node1
            node2.next = node1.next
            node1.next = node2
            return head

        # Generic swap
        if prev1: prev1.next = node2
        else:     head = node2
        if prev2: prev2.next = node1
        else:     head = node1
        node1.next, node2.next = node2.next, node1.next
        return head
```

### C) (Sometimes accepted) **Swap only the data** — simplest, still O(n)/O(1)

> Use this only if the interviewer allows value swap; some problems insist on swapping the **nodes**.

```python
class Solution:
    def swapKth(self, head, k):
        """
        Swap node 'data' fields, not pointers.
        Time:  O(n) ; Space: O(1)
        """
        if not head:
            return head

        # Find length
        n, cur = 0, head
        while cur:
            n += 1; cur = cur.next
        if k < 1 or k > n or k == n - k + 1:
            return head

        # Find k-th from start and k-th from end
        def kth_from_start(h, p):
            cur = h
            for _ in range(p - 1):
                cur = cur.next
            return cur
        a = kth_from_start(head, k)
        b = kth_from_start(head, n - k + 1)

        a.data, b.data = b.data, a.data
        return head
```

---

## 4) Common interviewer Q\&A

**Q1. What if `k > n`?**
Return the original list; swap is impossible.

**Q2. What if both nodes are the same (`k == n-k+1`)?**
No change; return head as-is.

**Q3. Why do we need the previous pointers?**
With a singly list, to redirect `prev.next` when re-linking each swapped node.

**Q4. How do you handle adjacent nodes?**
Do a tiny special case:

* If `node1.next is node2` (or vice-versa), re-wire as a “local rotate” so you don’t create a self-loop (`node1.next = node1`).

**Q5. Complexity?**
All pointer-swap versions here are **O(n)** time and **O(1)** space.

**Q6. Is swapping data acceptable?**
Only if explicitly allowed. If the node contains extra fields (e.g., child pointers) or the problem says “swap nodes,” you must swap the **links**, not the values.

**Q7. Can we do it in one pass?**
Yes after locating the k-th from start, use the fast runner to reach the tail and slide a `node2` pointer from the head—when `fast` hits tail, `node2` is k-th from end. You still need `prev1` and `prev2`.

---

---

Awesome — here’s a complete, interview-ready **Python program** for *Swap k-th nodes from beginning and end* with:

* clear inline **time/space complexity comments**,
* multiple implementations (pointer swap = canonical, one-pass variant, and data-swap),
* sample **inputs & outputs** printed,
* and a **total runtime** using `timeit`.

```python
# =========================
# Swap Kth nodes from ends
# =========================

from typing import Optional, List
import timeit

class Node:
    def __init__(self, x: int):
        self.data = x
        self.next: Optional["Node"] = None

# ---------- helpers (I/O & utilities) ----------
def build_ll(values: List[int]) -> Optional[Node]:
    """Build linked list from Python list.  Time: O(n)  Space: O(1) extra."""
    head = prev = None
    for v in values:
        node = Node(v)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head

def ll_to_list(head: Optional[Node]) -> List[int]:
    """Convert linked list back to Python list.  Time: O(n)  Space: O(1) extra."""
    out = []
    cur = head
    while cur:
        out.append(cur.data)
        cur = cur.next
    return out

# ============= Core solutions =============
class Solution:
    # ---- Canonical solution: swap the NODES (not just data) ----
    def swapKth(self, head: Optional[Node], k: int) -> Optional[Node]:
        """
        Swap the k-th node from start with the k-th node from end (1-based).
        * Computes n in O(n). If k>n or both nodes are same -> return head.
        * Finds both nodes and their previous pointers in O(n).
        * Carefully handles adjacency and head updates, then rewires pointers.

        Time  : O(n)            (one pass for n + two short scans)
        Space : O(1) auxiliary   (in-place link rewiring)
        """
        if not head:
            return head

        # 1) Compute length n.  O(n)
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next

        # 2) Validate k and "same node" case.  O(1)
        if k < 1 or k > n:
            return head
        if k == n - k + 1:
            return head  # same node, nothing to do

        # --- small helper to fetch (prev, node) for p-th from start (1-based) ---
        def get_prev_and_node(h: Node, p: int):
            prev, cur = None, h
            for _ in range(p - 1):      # advances p-1 steps; O(p)
                prev, cur = cur, cur.next
            return prev, cur

        # 3) Locate nodes and their prevs.  O(k) + O(n-k+1) = O(n)
        prev1, node1 = get_prev_and_node(head, k)
        prev2, node2 = get_prev_and_node(head, n - k + 1)

        # 4) If nodes are adjacent, handle explicitly to avoid self-loops.  O(1)
        if node1.next is node2:
            # node1 before node2
            if prev1: prev1.next = node2
            else:     head = node2
            node1.next = node2.next
            node2.next = node1
            return head
        if node2.next is node1:
            # node2 before node1
            if prev2: prev2.next = node1
            else:     head = node1
            node2.next = node1.next
            node1.next = node2
            return head

        # 5) Non-adjacent: splice both sides, then swap next pointers.  O(1)
        if prev1: prev1.next = node2
        else:     head = node2
        if prev2: prev2.next = node1
        else:     head = node1

        node1.next, node2.next = node2.next, node1.next
        return head

    # ---- One-sweep variant (find k-th from end using runner) ----
    def swapKth_one_pass(self, head: Optional[Node], k: int) -> Optional[Node]:
        """
        Find k-th from start, then slide a runner from that node to tail while
        moving a second pointer from head -> you land on k-th from end.
        Still O(n) time, O(1) space.
        """
        if not head: return head

        # find k-th from start
        prev1, node1 = None, head
        for _ in range(k - 1):
            if not node1: return head     # k > n
            prev1, node1 = node1, node1.next
        if not node1: return head         # k > n

        # find k-th from end by running from node1 to tail
        fast, prev2, node2 = node1, None, head
        while fast and fast.next:
            fast = fast.next
            prev2, node2 = node2, node2.next

        if node1 is node2: return head    # same node

        # adjacency and generic swap (same logic as above)
        if node1.next is node2:
            if prev1: prev1.next = node2
            else:     head = node2
            node1.next = node2.next
            node2.next = node1
            return head
        if node2.next is node1:
            if prev2: prev2.next = node1
            else:     head = node1
            node2.next = node1.next
            node1.next = node2
            return head

        if prev1: prev1.next = node2
        else:     head = node2
        if prev2: prev2.next = node1
        else:     head = node1
        node1.next, node2.next = node2.next, node1.next
        return head

    # ---- Simplest (if allowed): swap only data fields ----
    def swapKth_data(self, head: Optional[Node], k: int) -> Optional[Node]:
        """
        Swaps node values instead of links.  O(n) time, O(1) space.
        Use only if the interviewer/problem permits swapping data.
        """
        if not head: return head

        # compute n
        n, cur = 0, head
        while cur:
            n += 1; cur = cur.next
        if k < 1 or k > n or k == n - k + 1:
            return head

        # fetch k-th and (n-k+1)-th
        def kth(h: Node, p: int) -> Node:
            cur = h
            for _ in range(p - 1):
                cur = cur.next
            return cur
        a = kth(head, k)
        b = kth(head, n - k + 1)
        a.data, b.data = b.data, a.data
        return head


# ============= Demo / main program (with total runtime) =============
def main():
    sol = Solution()
    print("=== Swap K-th nodes from ends — Demo ===")

    # Example 1
    head1 = build_ll([1, 2, 3, 4, 5])
    k1 = 1
    print("\nInput 1:", ll_to_list(head1), "k =", k1)
    out1 = sol.swapKth(build_ll([1, 2, 3, 4, 5]), k1)     # pointer swap
    print("Output 1 (node swap):", ll_to_list(out1))       # expected [5,2,3,4,1]
    out1b = sol.swapKth_data(build_ll([1, 2, 3, 4, 5]), k1)
    print("Output 1 (data swap):", ll_to_list(out1b))

    # Example 2
    head2 = build_ll([5, 10, 8, 5, 9, 3])
    k2 = 2
    print("\nInput 2:", ll_to_list(head2), "k =", k2)
    out2 = sol.swapKth(build_ll([5, 10, 8, 5, 9, 3]), k2)
    print("Output 2 (node swap):", ll_to_list(out2))       # expected [5,9,8,5,10,3]
    out2b = sol.swapKth_one_pass(build_ll([5, 10, 8, 5, 9, 3]), k2)
    print("Output 2 (one-pass): ", ll_to_list(out2b))

    # Edge cases
    # Adjacent nodes: [1,2,3,4], k=2 -> swap 2 and 3
    head3 = build_ll([1, 2, 3, 4])
    k3 = 2
    print("\nEdge (adjacent):", ll_to_list(head3), "k =", k3)
    out3 = sol.swapKth(build_ll([1, 2, 3, 4]), k3)
    print("Output (adjacent):", ll_to_list(out3))          # [1,3,2,4]

    # Same node: [1,2,3,4,5], k=3 -> unchanged
    head4 = build_ll([1, 2, 3, 4, 5])
    k4 = 3
    print("\nEdge (same node):", ll_to_list(head4), "k =", k4)
    out4 = sol.swapKth(build_ll([1, 2, 3, 4, 5]), k4)
    print("Output (same node):", ll_to_list(out4))         # unchanged

    # k > n: [1,2,3], k=5 -> unchanged
    head5 = build_ll([1, 2, 3])
    k5 = 5
    print("\nEdge (k > n):", ll_to_list(head5), "k =", k5)
    out5 = sol.swapKth(build_ll([1, 2, 3]), k5)
    print("Output (k > n):", ll_to_list(out5))             # unchanged


if __name__ == "__main__":
    # Time the *entire* program run (build + calls + prints).
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
```

---

## 6) Real-World Use Cases (high-impact)

* **Editors & UI lists:** Swapping two items far apart in a singly linked list (e.g., moving the k-th item from the top with the k-th from the bottom) without rebuilding the structure.
* **LRU/Cache structures & queues:** Repositioning nodes (e.g., promoting/demoting items) where you must update links safely, including adjacency and head changes.
* **Streaming logs / playlists:** Efficiently rewiring items in long, singly linked sequences when users perform “swap” operations between symmetric positions.
