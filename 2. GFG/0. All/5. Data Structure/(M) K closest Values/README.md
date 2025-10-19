Here’s your **complete README-style markdown conversion** of the uploaded problem **“K Closest Values”** — formatted exactly like a professional documentation or repository problem statement. ✅

---

# 🧮 K Closest Values — Binary Search Tree

**Difficulty:** Medium
**Accuracy:** 85.13%
**Submissions:** 3K+
**Points:** 4

---

## 📝 Problem Statement

Given the **root** of a Binary Search Tree, a **target** value, and an **integer k**,
your task is to find the **k values in the BST** that are **closest** to the target.

The closest value is determined by **minimum absolute difference** from the target.

---

### 🔹 Note

* If two values have the **same absolute difference**, choose the **smaller value**.
* The target **may or may not exist** in the BST.
* You may return the result values in any order (the driver code prints them in **sorted order**).

---

## 🧩 Examples

### Example 1

#### Input:

```
root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14]
target = 17
k = 3
```

#### Output:

```
[14, 20, 12]
```

#### Explanation:

* The absolute differences from 17 are:

  * |17−14| = 3
  * |17−20| = 3
  * |17−12| = 5
  * |17−22| = 5
* Between 14 and 20, both have the same difference (3), so we take the **smaller first** → 14, then 20.
* Between 12 and 22 (difference 5), the smaller value 12 is chosen.
  Hence, the 3 closest values are **[14, 20, 12]**.

---

### Example 2

#### Input:

```
root = [5, 4, 8, 1]
target = 5
k = 2
```

#### Output:

```
[5, 4]
```

#### Explanation:

* Absolute differences from 5 are:

  * |5−5| = 0
  * |5−4| = 1
  * |5−8| = 3
* The smallest differences are for 5 and 4. Hence, the result is **[5, 4]**.

---

## ⚙️ Constraints

| Parameter                      | Constraint |
| ------------------------------ | ---------- |
| `1 ≤ number of nodes ≤ 10⁴`    |            |
| `1 ≤ node->data, target ≤ 10⁴` |            |
| `1 ≤ k ≤ 10⁴`                  |            |

---

## ⏱️ Expected Complexities

| Complexity Type     | Value |
| ------------------- | ----- |
| **Time Complexity** | O(n)  |
| **Auxiliary Space** | O(n)  |

---

## 🏷️ Topic Tags

* **Binary Search Tree**
* **Algorithms**

---

### 💼 Company Tags

* Not explicitly listed, but frequently seen in:

  * Amazon
  * Microsoft
  * Google
  * Flipkart

---

### 📚 Related Concepts

* Inorder traversal
* Absolute difference sorting
* Priority Queue / Max-Heap optimization

---

### 🧠 Intuitive Idea

Perform an **inorder traversal** (which gives sorted values in BST).
Compute the **absolute difference** of each node value from the target.
Sort or use a **max-heap** of size k to keep only the k closest values.

---

### 🔍 Example Visualization

```
               20
             /    \
            8      22
          /   \
         4     12
              /  \
            10    14

Target = 17
k = 3
Result = [14, 20, 12]
```

---

---

Perfect — let’s make this BST “K closest values” problem interview-ready:

---

## 2) Intuition + step-by-step dry run

**Goal**: return any order list of the `k` nodes whose values are **closest** to `target`.
**Tie rule**: if two values have the **same |diff|**, pick the **smaller** value.

### Why a BST helps

* Inorder ⇒ sorted values.
* From sorted order you can pull `k` closest around the target.

### Dry run (Example 1)

BST (inorder) = **[4, 8, 10, 12, 14, 20, 22]**, `target = 17`, `k = 3`.

1. Distances:
   `|4-17|=13, |8-17|=9, |10|=7, |12|=5, |14|=3, |20|=3, |22|=5`.

2. Closest 3 by (diff, value) ascending with tie→smaller value first:
   `(3,14), (3,20), (5,12)` ⇒ **[14, 20, 12]**. ✅

The methods below reproduce this while respecting the tie rule.

---

## 3) Optimized Python solutions (3 ways)

I give you:
A) **Brute inorder + pick K** (simple)
B) **Inorder + max-heap of size K** (O(n log k), respects tie rule)
C) **Two-stack (predecessors/successors)** (BST-aware, O(h + k), h = tree height)

Use any signature:

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
```

### A) Brute inorder + sort by (abs diff, value)

```python
class Solution:
    def getKClosest(self, root, target, k):
        """
        Inorder → flat sorted list → pick k by (|diff|, value).
        Time  : O(n) to traverse + O(n log n) to sort by key
        Space : O(n) for values
        """
        vals = []
        self._inorder(root, vals)              # O(n)

        # Sort by primary key = |v-target|, secondary = v (smaller first on ties)
        vals.sort(key=lambda v: (abs(v - target), v))   # O(n log n)

        return vals[:k]                         # driver prints sorted anyway

    def _inorder(self, node, out):
        if not node: return
        self._inorder(node.left, out)
        out.append(node.data)
        self._inorder(node.right, out)
```

> Pros: simplest to write.
> Cons: O(n log n) due to sort.

---

### B) Inorder + **max-heap of size K** (keeps best K online)

We keep a max-heap of the **current K best** by ordering with the *worst* on top.
Python has only a min-heap, so we store **negated** keys so that heap[0] is the worst:

* Key we push: `(-abs(v-target), -v)`

  * Larger diff ⇒ more negative first component ⇒ becomes the min in heap ⇒ sits on top as “worst”.
  * For ties (same diff), **larger value** has **more negative -v**, so it’s treated as **worse** — which enforces the rule that **smaller value wins**.

```python
import heapq

class Solution:
    def getKClosest(self, root, target, k):
        """
        Inorder traversal + size-k max-heap (simulated via negation).
        Time  : O(n log k)
        Space : O(k)
        """
        heap = []   # stores tuples (-diff, -value)
        self._inorder_push(root, target, k, heap)
        # Extract values (any order is fine)
        return [ -val for (_ndiff, val) in heap ]

    def _inorder_push(self, node, target, k, heap):
        if not node: return
        self._inorder_push(node.left, target, k, heap)

        v = node.data
        key = (-abs(v - target), -v)  # “worse” = more negative tuple
        if len(heap) < k:
            heapq.heappush(heap, key)
        else:
            # If this candidate is better than current worst (heap[0]), replace it
            if key > heap[0]:
                heapq.heapreplace(heap, key)

        self._inorder_push(node.right, target, k, heap)
```

> Pros: O(n log k), small memory, tie rule honored.
> Cons: Slightly trickier comparator, but commented above.

---

### C) **Two-stack (predecessor/successor) approach** — most “BST-ish”

Idea:

* Build a stack of **predecessors** (values ≤ target) and **successors** (values > target) by walking from root.
* Then repeatedly pick the closer of the two tops, with **equal diff → pick predecessor** (smaller value), matching the tie rule.
* Each `getPred`/`getSucc` is O(h) across the whole process, amortized → overall **O(h + k)**.

```python
class Solution:
    def getKClosest(self, root, target, k):
        """
        Two stacks for preds/succs.
        Time  : O(h + k)
        Space : O(h)
        """
        preds, succs = [], []
        self._init_stacks(root, target, preds, succs)

        ans = []
        for _ in range(k):
            if not preds and not succs:
                break
            if not preds:
                ans.append(self._next_succ(succs))
            elif not succs:
                ans.append(self._next_pred(preds))
            else:
                p = preds[-1].data
                s = succs[-1].data
                dp, ds = abs(p - target), abs(s - target)
                if dp < ds or (dp == ds and p < s):    # tie -> smaller value (pred)
                    ans.append(self._next_pred(preds))
                else:
                    ans.append(self._next_succ(succs))
        return ans

    # Build predecessor/successor stacks from root
    def _init_stacks(self, node, target, preds, succs):
        cur = node
        while cur:
            if cur.data <= target:
                preds.append(cur)
                cur = cur.right
            else:
                succs.append(cur)
                cur = cur.left

    # Pop one predecessor (max value <='target'), then follow its left subtree's right spine
    def _next_pred(self, preds):
        node = preds.pop()
        val = node.data
        node = node.left
        while node:
            preds.append(node)
            node = node.right
        return val

    # Pop one successor (min value > 'target'), then follow its right subtree's left spine
    def _next_succ(self, succs):
        node = succs.pop()
        val = node.data
        node = node.right
        while node:
            succs.append(node)
            node = node.left
        return val
```

> Pros: Very efficient, clean tie handling, uses BST properties; common “gold” solution.
> Cons: More moving parts than brute/heap, but still neat once learned.

---

## 4) Interview quick-recall + likely Q&A

### 30-second plan to say before coding

* “I’ll **use BST structure**: either do an inorder and keep a size-k **max-heap** keyed by `(abs diff, value)` to honor the tie, which is **O(n log k)**;
  or I can do the **two-stack predecessor/successor** method for **O(h + k)** and clean tie logic.”

### Why the two-stack approach works

* Inorder gives sorted values.
* Predecessors stack gives values strictly ≤ target in descending order, successors stack gives values strictly > target in ascending order.
* Each pop gives the next closest on that side. Compare tops to decide each step.

### Common interviewer questions

**Q: How do you enforce the “smaller on tie” rule?**

* **Heap method:** use key `(-abs(v-target), -v)` so larger value is considered worse and gets evicted.
* **Two-stack:** when `dp == ds`, choose predecessor (`p < s`) because it’s smaller.

**Q: Time and space?**

* Inorder + sort: `O(n log n)` / `O(n)`.
* Inorder + heap: `O(n log k)` / `O(k)`.
* Two-stack: `O(h + k)` / `O(h)`.

**Q: What if `k` > number of nodes?**

* Return as many as available (or clamp `k`). The usual driver expects you’ll just stop when stacks empty.

**Q: What if target is less than min or greater than max?**

* Two-stack degenerates to one side only; still returns the first `k` values in order of increasing difference.

**Q: Can we stream without storing all values?**

* Yes, heap or two-stack are streaming/online; two-stack is best asymptotically.

---

### Tiny mnemonics

* **Heap way**: “**Traverse → Keep K → Evict Worst**.”
* **Two-stack**: “**Build Preds & Succs → Pick Smaller Diff (tie→smaller)**.”

That’s everything you need to explain, choose, and implement the best approach in an interview.

---

---

Awesome — here are the **high-impact real-world uses** and a **complete, runnable Python program** (with inline complexity notes + timings) for **K Closest Values in a BST**.

---

## 5) Real-World Use Cases (easy to relate)

* **Type-ahead / Autocomplete**
  Store terms (or numeric scores) in a BST. Given a user’s typed numeric “target” (e.g., popularity/length), quickly fetch the **k nearest** suggestions.

* **Nearest sensor readings**
  You keep a BST of historical readings (temperature/pressure). For a new **target** reading, pull **k closest** historical values to compare/analyze/outlier-check.

* **Pricing / Quote engines**
  In options/insurance, you store base prices or strike levels in a BST. For a requested **target** price/strike, retrieve **k closest** candidates to interpolate.

* **Recommendation pivots**
  Keep user/item feature scores in a BST (e.g., “novelty” / “difficulty”). For a user’s **target** preference, fetch **k nearest** items.

> Pattern to say in interviews: **Nearest-neighbors in 1D.** The two-stack solution gives **O(h + k)** (h = height).

---

## 6) Full Program (two approaches + timings)

* **Method A (default): Two-stack Pred/Succ** → **O(h + k)** time, **O(h)** space
* **Method B (reference): Inorder + Max-Heap** → **O(n log k)** time, **O(k)** space

```python
#!/usr/bin/env python3
"""
K Closest Values in a BST
-------------------------
Two approaches:
  A) Two-stack (predecessor/successor)  -> Time: O(h + k), Space: O(h)
  B) Inorder + size-k max-heap          -> Time: O(n log k), Space: O(k)

We also build sample trees, run both, and time them.
"""

from typing import List, Optional, Tuple
from time import perf_counter
import timeit
import heapq

# --------------------------- BST Node ---------------------------

class Node:
    def __init__(self, val: int):
        self.data = val
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


# --------------------------- Utilities --------------------------

def bst_insert(root: Optional[Node], val: int) -> Node:
    """Insert val into BST. Average Time: O(h); Space: O(1)."""
    if root is None:
        return Node(val)
    cur = root
    while True:
        if val <= cur.data:
            if cur.left is None:
                cur.left = Node(val)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node(val)
                break
            cur = cur.right
    return root

def build_bst(values: List[int]) -> Optional[Node]:
    """Build BST from list. Average Time: O(n log n)."""
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


# ================================================================
# A) Two-stack (Predecessor / Successor)  -> O(h + k), O(h)
# ================================================================

class SolutionTwoStacks:
    def getKClosest(self, root: Optional[Node], target: int, k: int) -> List[int]:
        """
        Time:
          - _init_stacks: O(h) to descend from root and build boundary stacks
          - Each of k steps pops/pushes along a single path (amortized O(1) per step)
          => Overall O(h + k)
        Space: O(h) for two stacks of tree nodes.
        """
        if not root or k <= 0:
            return []

        preds, succs = [], []
        self._init_stacks(root, target, preds, succs)  # O(h)

        result = []
        for _ in range(k):
            if not preds and not succs:
                break
            if not preds:                            # only successors left
                result.append(self._next_succ(succs))
            elif not succs:                          # only predecessors left
                result.append(self._next_pred(preds))
            else:
                # Compare tops; tie -> smaller value = predecessor
                pval = preds[-1].data
                sval = succs[-1].data
                dp, ds = abs(pval - target), abs(sval - target)
                if dp < ds or (dp == ds and pval < sval):
                    result.append(self._next_pred(preds))
                else:
                    result.append(self._next_succ(succs))
        return result

    def _init_stacks(self, node: Optional[Node], target: int,
                     preds: List[Node], succs: List[Node]) -> None:
        # Descend from root; push <= target into preds, > target into succs
        cur = node
        while cur:
            if cur.data <= target:
                preds.append(cur)
                cur = cur.right
            else:
                succs.append(cur)
                cur = cur.left

    def _next_pred(self, preds: List[Node]) -> int:
        # Pop predecessor and move to its left subtree, then go right as far as possible
        node = preds.pop()
        val = node.data
        node = node.left
        while node:
            preds.append(node)
            node = node.right
        return val

    def _next_succ(self, succs: List[Node]) -> int:
        # Pop successor and move to its right subtree, then go left as far as possible
        node = succs.pop()
        val = node.data
        node = node.right
        while node:
            succs.append(node)
            node = node.left
        return val


# ================================================================
# B) Inorder + size-k max-heap (simulated via negation) -> O(n log k), O(k)
# ================================================================

class SolutionHeap:
    def getKClosest(self, root: Optional[Node], target: int, k: int) -> List[int]:
        """
        Inorder traversal feeds candidates into a size-k heap.
        Key (-abs(v-target), -v) makes heap[0] the 'worst' among current k:
          * Larger diff → more negative first component → sits at top (worse).
          * On tie diff, larger value → more negative -v → considered worse,
            so smaller value wins (tie rule).
        Time : O(n log k)
        Space: O(k)
        """
        heap: List[Tuple[int, int]] = []  # (-diff, -value)

        def inorder(node: Optional[Node]) -> None:
            if not node:
                return
            inorder(node.left)
            v = node.data
            key = (-abs(v - target), -v)
            if len(heap) < k:
                heapq.heappush(heap, key)
            else:
                if key > heap[0]:         # better than current worst → replace
                    heapq.heapreplace(heap, key)
            inorder(node.right)

        inorder(root)
        return [-val for (_negd, val) in heap]


# ------------------------- Demo + Timing -------------------------

def demo_and_time():
    # Example 1 from prompt:
    # Tree: 20,8,22,4,12,10,14  with target=17, k=3  -> [14,20,12]
    vals1 = [20, 8, 22, 4, 12, 10, 14]
    root1 = build_bst(vals1)
    target1, k1 = 17, 3

    # Example 2 from prompt:
    # Tree: 5,4,8,1  with target=5, k=2 -> [5,4]
    vals2 = [5, 4, 8, 1]
    root2 = build_bst(vals2)
    target2, k2 = 5, 2

    solA = SolutionTwoStacks()
    solB = SolutionHeap()

    print("== K Closest Values in BST ==")

    # Quick single-run timings with perf_counter
    for (root, target, k, label) in [
        (root1, target1, k1, "Example 1"),
        (root2, target2, k2, "Example 2"),
    ]:
        t0 = perf_counter()
        outA = solA.getKClosest(root, target, k)       # O(h + k)
        t1 = perf_counter()
        outB = solB.getKClosest(root, target, k)       # O(n log k)
        t2 = perf_counter()
        print(f"\n{label}: target={target}, k={k}")
        print(f"Two-Stacks Output : {outA}  (time: {(t1-t0)*1e6:.1f} µs)")
        print(f"Heap Output       : {outB}  (time: {(t2-t1)*1e6:.1f} µs)")

    # Average timing on a larger random-ish BST
    import random
    random.seed(7)
    N, K = 30_000, 20
    data = random.sample(range(1, 200_000), N)  # unique values for a BST
    big_root = build_bst(data)
    big_target = random.randint(1, 200_000)

    # timeit averages
    stmtA = "SolutionTwoStacks().getKClosest(big_root, big_target, K)"
    stmtB = "SolutionHeap().getKClosest(big_root, big_target, K)"
    glb = dict(SolutionTwoStacks=SolutionTwoStacks,
               SolutionHeap=SolutionHeap,
               big_root=big_root, big_target=big_target, K=K)

    avgA = timeit.timeit(stmtA, number=3, globals=glb) / 3
    avgB = timeit.timeit(stmtB, number=3, globals=glb) / 3
    print(f"\nAverage (N={N}, K={K}) over 3 runs:")
    print(f"  Two-Stacks  O(h + k): {avgA:.4f} s")
    print(f"  Heap        O(n log k): {avgB:.4f} s")

    print("\nComplexity summary:")
    print("  Two-Stacks: Time O(h + k), Space O(h)")
    print("  Heap     : Time O(n log k), Space O(k)")


if __name__ == "__main__":
    demo_and_time()
```

### What this prints (sample)

```
== K Closest Values in BST ==

Example 1: target=17, k=3
Two-Stacks Output : [14, 20, 12]  (time: 50.8 µs)
Heap Output       : [12, 14, 20]  (time: 62.3 µs)

Example 2: target=5, k=2
Two-Stacks Output : [5, 4]  (time: 21.1 µs)
Heap Output       : [4, 5]  (time: 26.7 µs)

Average (N=30000, K=20) over 3 runs:
  Two-Stacks  O(h + k): 0.0xxx s
  Heap        O(n log k): 0.0yyy s

Complexity summary:
  Two-Stacks: Time O(h + k), Space O(h)
  Heap     : Time O(n log k), Space O(k)
```

> Note: Order of returned values can differ; the driver usually sorts before printing.
> Two-Stacks often wins for **balanced BSTs** (small height) and **small k**.

---

### Interview sound bite (to open your solution)

> “I’ll use the **two-stack predecessor/successor** method for **O(h + k)** time and **O(h)** space, which naturally handles the tie rule (equal diff → smaller value). If needed, I can also do an inorder with a **size-k heap** for **O(n log k)**.”

