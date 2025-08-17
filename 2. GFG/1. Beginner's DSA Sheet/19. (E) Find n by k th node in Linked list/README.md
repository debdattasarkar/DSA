

---

# Find n/k th node in Linked List

**Difficulty:** Easy
**Accuracy:** 39.46%
**Submissions:** 56K+
**Points:** 2

---

## Problem Statement

Given a singly linked list and a number **k**, find the **(n/k)th** element, where **n** is the number of elements in the linked list.
We need to consider **ceil value** in case of decimals.

---

## Examples

### Example 1:

**Input:**
LinkedList: 1->2->3->4->5->6 , k = 2

**Output:**
3

**Explanation:**
6/2 = 3rd element is the 3rd (1-based indexing) element which is 3.

---

### Example 2:

**Input:**
LinkedList: 2->7->9->3->5 , k = 3

**Output:**
7

**Explanation:**
The 5/3rd element is the 2nd element as mentioned in the question that we need to consider ceil value in the case of decimals. So 2nd element is 7.

---

## Constraints

* 1 ≤ number of nodes ≤ 10⁴
* 1 ≤ k ≤ number of nodes
* 1 ≤ node->data ≤ 10³

---

## Company Tags

* Hike
* SAP Labs

---

## Topic Tags

* Linked List
* Data Structures

---

## Related Articles

* [Find Fractional Nk Th Node Linked List](https://www.geeksforgeeks.org/find-fractional-nk-th-node-linked-list/)

---

---

Interview-ready package for the **Fractional Node (ceil(n/k)-th node)** problem, based on the working solution.

---

# 2) Problem intuition + step-by-step dry run

**Goal**
Given a singly linked list and an integer `k`, return the value at the node positioned at `ceil(n/k)` (1-based), where `n` is the number of nodes.

**Key idea**

* If you know `n`, the answer is simply the `(n+k-1)//k`-th node (1-based).
* There’s also a neat **one-pass** trick that moves a pointer (`frac`) forward once every time we’ve advanced `k` nodes with another pointer (`cur`). With a tiny boundary tweak, this lands exactly on `ceil(n/k)`.

### Dry run (one-pass trick)

List: `2 -> 7 -> 9 -> 3 -> 5`, `k = 3`
We keep:

* `cur` — walks every node
* `frac` — starts at head and advances by one **every time** we have just seen a multiple of `k` nodes **and** we’re not at the end

Steps (`i` counts visited nodes by `cur`):

| i | cur.val | i % k == 0? | cur.next exists? | move frac? | frac.val |
| - | ------- | ----------- | ---------------- | ---------- | -------- |
| 1 | 2       | no          | yes              | no         | 2        |
| 2 | 7       | no          | yes              | no         | 2        |
| 3 | 9       | yes         | yes              | **yes**    | 7        |
| 4 | 3       | no          | yes              | no         | 7        |
| 5 | 5       | no          | **no**           | no         | 7        |

* Visited 5 nodes → `ceil(5/3) = 2` → 2nd node value is **7**, which matches `frac`.

Why the `cur.next` check?
When the last batch ends exactly at the tail, we don’t want to step `frac` past the correct ceil position.

---

# 3) Optimized codes (interview-ready)

### A) One-pass (preferred) — O(n) time, O(1) space

```python
'''class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
        
class Solution:
    def fractional_node(self, head, k):
        """
        Returns value at ceil(n/k)-th node (1-based) using one pass.
        Time  : O(n)  — visit each node once
        Space : O(1)  — constant extra pointers
        """
        if head is None or k <= 0:
            return -1  # or None per platform

        frac = head          # will end at ceil(n/k)-th node
        cur = head
        i = 0

        # Walk with 'cur', bump 'frac' once after every k nodes
        # but only if we aren't at the final node (cur.next != None)
        while cur:
            i += 1
            if i % k == 0 and cur.next is not None:
                frac = frac.next
            cur = cur.next

        return frac.data
```

**Why it works**
After visiting `i` nodes, we will have advanced `frac` `floor((i-1)/k)` times. When `i` reaches `n`, `frac` sits at index `1 + floor((n-1)/k) = ceil(n/k)`.

---

### B) Two-pass (simple & explicit) — O(n) time, O(1) space

```python
class Solution:
    def fractional_node(self, head, k):
        """
        Two-pass: compute n, then jump to index ceil(n/k).
        Time  : O(n)
        Space : O(1)
        """
        if head is None or k <= 0:
            return -1  # or None

        # 1) length
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next

        # 2) target index (1-based)
        target = (n + k - 1) // k

        # 3) move target-1 steps from head
        cur = head
        for _ in range(target - 1):
            cur = cur.next

        return cur.data
```

**When interviews ask for clarity**, the two-pass version is often easier to reason about; the one-pass version shows optimization and pointer skill.

---

## Edge cases to mention

* `k = 1` → node at `ceil(n/1) = n` → last node.
* `k >= n` → node at `ceil(n/k) = 1` → head.
* Single node list.
* Very large `n` (ensure O(n), O(1) solution, no recursion).

---

# 4) Interview Q\&A

**Q1. Why `ceil(n/k)` and not `floor(n/k)`?**
A: By definition of the “fractional node” in this problem, we want the first node that crosses the `n/k` fraction, i.e., `ceil(n/k)`.

**Q2. Prove the one-pass correctness.**
A: After visiting `i` nodes (`cur`), we have completed `floor(i/k)` full groups of size `k`. We advance `frac` **after** finishing each group, except if we’re at the very end (`cur.next` is `None`), to avoid overshooting. At termination (`i = n`), `frac` points to `1 + floor((n-1)/k) = ceil(n/k)`.

**Q3. What’s the time/space complexity?**
A: Both solutions are **O(n)** time. Space is **O(1)** (only pointers).

**Q4. Can this be done with fast/slow pointers?**
A: Classic fast/slow aims for midpoints. Here the ratio is `1:k`. The presented one-pass approach is the most direct and clear.

**Q5. What happens for invalid `k` (e.g., `k <= 0`)?**
A: Return a sentinel (e.g., `-1` or `None`) as per platform constraints. In GFG, `k` is valid per constraints, but it’s good to guard.

**Q6. If the judge expects the **value** but you return the **node**?**
A: You’ll print something like `<__main__.Node object at ...>`. Always return `node.data` for the expected output.

---

---

Here’s a **complete, runnable program** that:

* Implements both approaches (one-pass and two-pass)
* Adds **inline time/space complexity comments** right where they matter
* Builds a linked list, prints the input and result
* Uses `timeit` to measure the total runtime of the program’s main logic

---

### Full Program (copy–paste and run)

```python
from timeit import timeit

# ---------- Linked List Basics ----------
class Node:
    """Singly linked list node."""
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(values):
    """
    Build a linked list from an iterable of values.
    Time:  O(n) — iterate once to chain nodes
    Space: O(n) — n nodes are created
    """
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


def list_to_string(head):
    """
    Convert linked list to a clean string for display.
    Time:  O(n) — visit each node once
    Space: O(n) — build a list of strings for printing
    """
    vals = []
    cur = head
    while cur:
        vals.append(str(cur.data))
        cur = cur.next
    return " -> ".join(vals) if vals else "<empty>"


# ---------- Solutions ----------
class Solution:
    def fractional_node(self, head, k):
        """
        One-pass (preferred) solution that returns value at ceil(n/k)-th node.

        Pointers:
          - cur: walks every node
          - frac: advances one step after each full group of k nodes
                  (but only if not at the end) so it lands at ceil(n/k).

        Time:  O(n)  — one pass through the list
        Space: O(1)  — constant extra pointers
        """
        if head is None or k <= 0:
            return -1  # guard: invalid input

        frac = head
        cur = head
        i = 0

        while cur:
            i += 1
            # Advance 'frac' after finishing every k nodes,
            # but only if we still have more nodes ahead.
            if i % k == 0 and cur.next is not None:
                frac = frac.next
            cur = cur.next

        return frac.data

    def fractional_node_two_pass(self, head, k):
        """
        Two-pass solution:
          1) Compute length n
          2) Target index = ceil(n/k) = (n + k - 1) // k
          3) Walk target-1 steps from head and return that node's value

        Time:  O(n)  — two linear passes still O(n)
        Space: O(1)  — constant extra variables
        """
        if head is None or k <= 0:
            return -1

        # Pass 1: compute n
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next

        # 1-based target index
        target = (n + k - 1) // k

        # Pass 2: move target - 1 steps from head
        cur = head
        for _ in range(target - 1):
            cur = cur.next

        return cur.data


# ---------- Main with timing ----------
def main():
    # ----- Input values (change these to test quickly) -----
    values = [2, 7, 9, 3, 5]  # linked list contents
    k = 3

    # Build list
    head = build_linked_list(values)

    # Show input
    print("Input linked list:", list_to_string(head))
    print("k =", k)

    sol = Solution()

    # Compute results using both methods
    # One-pass
    ans_one_pass = sol.fractional_node(head, k)
    print("\nOne-pass (O(n), O(1)) answer:", ans_one_pass)

    # Two-pass
    ans_two_pass = sol.fractional_node_two_pass(head, k)
    print("Two-pass (O(n), O(1)) answer:", ans_two_pass)

    # Sanity check: both should match
    print("Match?", ans_one_pass == ans_two_pass)


def timed_main():
    """
    Wrap main() so timeit measures the whole "program run".
    Time of this function itself is O(1); main does O(n) work.
    """
    main()


if __name__ == "__main__":
    # Run once to show outputs
    main()

    # Measure "full program run" time (including building list & solving)
    # Increase number= to average across more runs if you want
    total_time = timeit(stmt="timed_main()", setup="from __main__ import timed_main", number=5)
    print(f"\n[timeit] Average time over 5 runs: {total_time/5:.6f} seconds")
```

**Sample Output (for the default input)**

```
Input linked list: 2 -> 7 -> 9 -> 3 -> 5
k = 3

One-pass (O(n), O(1)) answer: 7
Two-pass (O(n), O(1)) answer: 7
Match? True

[timeit] Average time over 5 runs: 0.0000xx seconds
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Pagination / Chunk Navigation**

   * When iterating large streams in chunks of size `k`, you may need the boundary element representing the *ceil(n/k)-th* chunk start (e.g., pick the “first item of the next page” marker).

2. **Sampling / Thinning Logs**

   * From `n` sequential records, the *ceil(n/k)-th* record can serve as a deterministic sample point when down-sampling streams or logs by a factor of `k`.

3. **Checkpointing in Pipelines**

   * In data processing pipelines, you may want a checkpoint at the *ceil(n/k)-th* item to resume safely after each block, especially when `n` isn’t known ahead of time.

4. **Rendezvous Nodes in Distributed Systems**

   * When nodes are placed logically in a ring/list, selecting the *ceil(n/k)-th* node helps in distributing responsibility (leaders/checkpoints) roughly every `k` positions with a simple one-pass scan.
