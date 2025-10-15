# k-th Smallest in BST

**Difficulty:** Medium
**Accuracy:** 43.53%
**Submissions:** 152K+
**Points:** 4
**Average Time:** 40m

---

## Problem Statement

Given the **root** of a **BST** and an integer **k**, find the **k-th smallest** element in the BST.
If there is no k-th smallest element present, return **-1**.

---

## Examples

### Example 1

**Input:**
`root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 3`

**Output:**
`10`

**Explanation:**
10 is the 3rd smallest element in the BST.

BST sketch:

```
        20
       /  \
      8    22
     / \
    4   12
       /  \
      10  14
```

---

### Example 2

**Input:**
`root = [2, 1, 3], k = 5`

**Output:**
`-1`

**Explanation:**
There is no 5th smallest element in the BST as the size of BST is 3.

BST sketch:

```
   2
  / \
 1   3
```

---

## Constraints

* `1 ≤ number of nodes, k ≤ 10^4`
* `1 ≤ node->data ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(h)` where `h` is the height of the BST

---

## Company Tags

Accolite, Amazon, Google

---

## Topic Tags

Binary Search Tree, Data Structures

---

## Related Articles

* Find K-th Smallest Element in BST (Order Statistics in BST)
* K-th Smallest Element in BST Using O(1) Extra Space

---

---

awesome — let’s make **k-th Smallest in a BST** interview-ready.

---

## 2) Intuition + step-by-step dry run

### Key fact

In a **Binary Search Tree (BST)**, **inorder traversal** (Left → Node → Right) visits keys in **sorted ascending order**.
So the **k-th visit** during inorder is the **k-th smallest**.

### Dry run (Example 1)

BST:

```
        20
       /  \
      8    22
     / \
    4   12
       /  \
      10  14
```

Find k = 3.

Do inorder with a counter:

1. Go left from 20 → 8 → 4 (leftmost).
2. Visit **4** → count=1.
3. Back to **8** → visit → count=2.
4. Go right to 12 → go left to **10** → visit → count=3 ⇒ **answer = 10** (stop).
   (We would not need to traverse the rest.)

---

## 3) Python solutions (brute + optimal variants)

All solutions return **-1** if k is out of bounds.

### A) Iterative Inorder with Stack (most expected in interviews)

* Time `O(h + k)` (worst `O(n)`)
* Space `O(h)` for stack

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k):
        """
        Iterative inorder: walk to leftmost, then unwind with a stack.
        Each pop is the next-smallest value; when we pop the k-th time, return it.
        Time  : O(h + k)  (worst O(n))
        Space : O(h)      (stack)
        """
        stack = []
        current = root
        visited_count = 0

        # Standard inorder traversal
        while current or stack:
            # go as left as possible
            while current:
                stack.append(current)
                current = current.left

            # visit node
            current = stack.pop()
            visited_count += 1
            if visited_count == k:
                return current.data

            # then go right
            current = current.right

        return -1  # k larger than number of nodes
```

---

### B) Recursive Inorder (clean & concise; uses call stack)

* Time `O(h + k)` (worst `O(n)`)
* Space `O(h)` recursion

```python
class SolutionRecursive:
    def kthSmallest(self, root, k):
        """
        Recursive inorder with a shared counter.
        Time  : O(h + k)  (worst O(n))
        Space : O(h)      recursion
        """
        self.count = 0
        self.answer = -1

        def inorder(node):
            if not node or self.answer != -1:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.data
                return
            inorder(node.right)

        inorder(root)
        return self.answer
```

---

### C) Morris Inorder Traversal (O(1) extra space)

* Modifies tree temporarily (threading), restores it
* Time `O(n)`, Space **O(1)**

```python
class SolutionMorris:
    def kthSmallest(self, root, k):
        """
        Morris inorder (threaded) => O(1) space.
        Time  : O(n)
        Space : O(1)
        """
        current = root
        visited_count = 0

        while current:
            if not current.left:
                visited_count += 1
                if visited_count == k:
                    return current.data
                current = current.right
            else:
                # Find inorder predecessor (rightmost in left subtree)
                pred = current.left
                while pred.right and pred.right is not current:
                    pred = pred.right

                if not pred.right:
                    # thread it
                    pred.right = current
                    current = current.left
                else:
                    # remove thread, visit current
                    pred.right = None
                    visited_count += 1
                    if visited_count == k:
                        return current.data
                    current = current.right

        return -1
```

---

### D) Brute (collect-all + index) — simple but uses O(n) space

* Do a full inorder into a list, then pick `k-1` index if valid.
* Time `O(n)`, Space `O(n)`

```python
class SolutionBrute:
    def kthSmallest(self, root, k):
        """
        Collect all inorder values, then index.
        Time  : O(n)
        Space : O(n)
        """
        sorted_vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.data)
            inorder(node.right)

        inorder(root)
        return sorted_vals[k-1] if 1 <= k <= len(sorted_vals) else -1
```

> What to pick in interviews?
>
> * Choose **A (iterative stack)** first — predictable and robust.
> * Mention **C (Morris)** if they ask for **O(1) space**.
> * You can sketch **B (recursive)** if they’re fine with recursion.

---

## 4) 60-second interview recall + Q&A

### 10-second mnemonic

> **“BST + inorder = sorted.
> k-th pop during inorder is the answer.”**

### Micro-plan to speak out loud

1. “Since it’s a BST, inorder traversal yields sorted order.”
2. “I’ll do iterative inorder with a stack and count visits.”
3. “When count == k, return node’s value; else -1.”
4. “Time O(h + k), Space O(h); Morris gives O(1) space.”

### Likely interviewer questions

**Q1. Why inorder finds k-th smallest?**
Because BST property ensures `Left < Node < Right`, so inorder yields ascending order.

**Q2. Complexity?**
Iterative/recursive: **O(h + k)** time (worst O(n)), **O(h)** space.
Morris: **O(n)** time, **O(1)** space.

**Q3. What if k is invalid?**
Return **-1** if traversal finishes before visiting k nodes (k > size) or if k < 1.

**Q4. Why might you prefer Morris? Why not?**
Prefer if you **must** use **O(1)** extra memory.
Downside: more complex; temporarily threads pointers (must be careful to restore).

**Q5. Can we stop early?**
Yes. In all approaches, once we’ve visited k nodes, we **return immediately**.

**Q6. Could we augment the BST to do better?**
Yes — store **subtree sizes** at each node. Then:

* Compare `k` with `size(left) + 1` to decide to go left / return / go right.
* Achieves **O(h)** time, **O(1)** space per query (but needs augmented tree maintenance).

**Q7. Edge cases you’d test?**

* Single node, k=1 and k>1
* Skewed tree (all left / all right)
* k = size (largest element)
* Duplicates? (Usually BSTs avoid duplicates; if allowed, define visit order.)

---

---

## 5) Real-World Use Cases (memorable + relatable)

* **Ranked search results / leaderboards:**
  Results stored in a BST by score; fetch the **k-th best** (or **k-th smallest** if ascending).
  In practice you might augment nodes with subtree sizes for O(h) queries.

* **Stock order book (price levels):**
  Buy/sell limit orders keyed by price in a BST; find the **k-th price level** (e.g., top-k bids/asks).

* **Telemetry thresholds:**
  Metrics (latencies, sizes) kept in a BST; quickly locate **k-th percentile** candidates (e.g., p50/p95).

* **Scheduling / prioritization:**
  Jobs keyed by priority or deadline; pick the **k-th** job in sorted order to balance fairness vs priority.

* **Database indexing (conceptual):**
  Secondary indexes as search trees; “k-th smallest key” corresponds to **order statistics** queries.

> Tip to say aloud: “BST + inorder is sorted, so the k-th visit is the k-th smallest. If we need repeated queries, we can **augment each node with subtree size** to answer in O(h).”

---

## 6) Full Program (reads tree + k, solves, prints, and times)

* **Input format** (2 lines):

  * Line 1: level-order of BST, space-separated, `'N'` for nulls
    e.g. `20 8 22 4 12 N N N N 10 14`
  * Line 2: integer `k`
* **Output**: k-th smallest and timing stats (iterative inorder, plus Morris optional).

```python
#!/usr/bin/env python3
"""
k-th Smallest in BST
--------------------
Given root of a BST and integer k, return the k-th smallest element else -1.

Main approach (interview-standard):
  Iterative inorder traversal with an explicit stack.
  Inorder on a BST yields ascending order; the k-th visit is the k-th smallest.

Complexities:
  Iterative inorder:
    Time  : O(h + k)   (worst O(n)) -- each node pushed/popped at most once
    Space : O(h)       -- stack (h = tree height; worst O(n) if skewed)

Also included for reference:
  Morris inorder (O(1) extra space), Time O(n).
"""

from collections import deque
from time import perf_counter
import timeit
import sys

# ----------------------------- Node definition -----------------------------
class Node:
    def __init__(self, val: int):
        # O(1) time/space
        self.data = val
        self.left = None
        self.right = None

# ------------------------- Build tree from level-order ----------------------
def build_tree(tokens):
    """
    Build a BST tree from level-order tokens. 'N' means null.

    Complexity:
      Time  : O(n) -- each token consumed once
      Space : O(n) -- queue + nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root = Node(int(next(it)))
    q = deque([root])

    for left_tok in it:
        parent = q.popleft()  # amortized O(1)

        if left_tok != 'N':
            lc = Node(int(left_tok))
            parent.left = lc
            q.append(lc)

        try:
            right_tok = next(it)
        except StopIteration:
            break
        if right_tok != 'N':
            rc = Node(int(right_tok))
            parent.right = rc
            q.append(rc)

    return root

# ----------------------- Approach A: Iterative Inorder ----------------------
def kth_smallest_iterative(root, k: int) -> int:
    """
    Iterative inorder traversal.
    Time  : O(h + k)  (worst O(n))
    Space : O(h)      stack
    """
    stack = []          # O(h)
    curr = root
    visited_count = 0   # O(1)

    # Standard inorder loop: go left, visit, go right
    while curr or stack:
        while curr:
            stack.append(curr)     # push left chain; each node at most once
            curr = curr.left

        curr = stack.pop()         # visit node
        visited_count += 1
        if visited_count == k:
            return curr.data

        curr = curr.right          # then traverse right subtree

    return -1  # k > number of nodes

# ----------------------- Approach B: Morris Inorder (O(1) space) -----------
def kth_smallest_morris(root, k: int) -> int:
    """
    Morris inorder traversal (threaded tree).
    Time  : O(n)
    Space : O(1) extra
    Note  : Temporarily modifies right pointers; restores them.
    """
    curr = root
    visited_count = 0

    while curr:
        if not curr.left:
            visited_count += 1
            if visited_count == k:
                return curr.data
            curr = curr.right
        else:
            # find inorder predecessor of curr
            pred = curr.left
            while pred.right and pred.right is not curr:
                pred = pred.right

            if not pred.right:
                pred.right = curr     # create thread
                curr = curr.left
            else:
                pred.right = None     # remove thread, visit curr
                visited_count += 1
                if visited_count == k:
                    return curr.data
                curr = curr.right

    return -1

# ------------------------------- Timing helpers ----------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter. O(1) overhead."""
    t0 = perf_counter()
    res = func(*args, **kwargs)
    t1 = perf_counter()
    return res, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number

# ------------------------------------ Main ---------------------------------
def main():
    # Input: level-order tokens on line 1, k on line 2
    # Example:
    #   20 8 22 4 12 N N N N 10 14
    #   3
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        print("No input provided.\nExample:\n  20 8 22 4 12 N N N N 10 14\n  3")
        return
    if len(lines) < 2:
        print("Provide two lines: level-order, then k.\nExample:\n  20 8 22 4 12 N N N N 10 14\n  3")
        return

    tokens = lines[0].split()
    k = int(lines[1])

    root = build_tree(tokens)  # O(n)

    # --- Iterative inorder (primary) ---
    ans_iter, t_iter = time_single_run(kth_smallest_iterative, root, k)
    avg_iter = time_with_timeit(lambda: kth_smallest_iterative(root, k), number=5)

    print("k-th Smallest (Iterative inorder):", ans_iter)
    print(f"  Single-run time : {t_iter:.6f} s")
    print(f"  Avg over 5 runs : {avg_iter:.6f} s")

    # --- Morris inorder (O(1) space) ---
    # Rebuild the tree if you suspect Morris might alter threading mid-run;
    # here we call it once after iterative (iterative doesn't modify the tree).
    ans_morris, t_morris = time_single_run(kth_smallest_morris, root, k)
    avg_morris = time_with_timeit(lambda: kth_smallest_morris(root, k), number=5)

    print("\nk-th Smallest (Morris inorder):   ", ans_morris)
    print(f"  Single-run time : {t_morris:.6f} s")
    print(f"  Avg over 5 runs : {avg_morris:.6f} s")

    # Complexity recap
    print("\nComplexity Summary:")
    print("  Iterative inorder : Time O(h + k) (worst O(n)), Space O(h)")
    print("  Morris inorder    : Time O(n), Space O(1) extra")

if __name__ == "__main__":
    """
    Example:
      echo -e "20 8 22 4 12 N N N N 10 14\n3" | python3 kth_smallest_bst.py
    Expected:
      k-th Smallest (Iterative inorder): 10
      ...
    """
    main()
```

### Example Run

**Input**

```
20 8 22 4 12 N N N N 10 14
3
```

**Output** (times vary)

```
k-th Smallest (Iterative inorder): 10
  Single-run time : 0.0000xx s
  Avg over 5 runs : 0.0000xx s

k-th Smallest (Morris inorder):    10
  Single-run time : 0.0000xx s
  Avg over 5 runs : 0.0000xx s

Complexity Summary:
  Iterative inorder : Time O(h + k) (worst O(n)), Space O(h)
  Morris inorder    : Time O(n), Space O(1) extra
```

> Interview one-liner to say before coding:
> **“BST + inorder = sorted. I’ll do an iterative inorder with a stack and count to k (O(h+k) time, O(h) space). If asked for O(1) space, I’ll switch to Morris traversal.”**

---

---

