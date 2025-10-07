# Construct Tree from Preorder & Postorder

**Difficulty:** Medium
**Accuracy:** 100.0%
**Submissions:** 1+
**Points:** 4

---

## Problem Statement

Given two arrays `pre[]` and `post[]` that represent the preorder and postorder traversals of a **full binary tree**, your task is to construct the binary tree and return its **root**.

---

### Note:

A **Full Binary Tree** is a binary tree where every node has **either 0 or 2 children**.

The preorder and postorder traversals contain **unique values**, and every value present in the preorder traversal is also found in the postorder traversal.

---

## Examples

### Example 1:

**Input:**

```
pre[]  = [1, 2, 4, 8, 9, 5, 3, 6, 7]  
post[] = [8, 9, 4, 5, 2, 6, 7, 3, 1]
```

**Output:**

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Explanation:**
The constructed tree will look like:

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
   / \
  8   9
```

---

### Example 2:

**Input:**

```
pre[]  = [1, 2, 4, 5, 3, 6, 7]
post[] = [4, 5, 2, 6, 7, 3, 1]
```

**Output:**

```
[1, 2, 3, 4, 5, 6, 7]
```

**Explanation:**
The constructed tree will look like:

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

---

## Constraints

```
1 ≤ number of nodes ≤ 10^3
1 ≤ pre[i], post[i] ≤ 10^4
```

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## Topic Tags

* Tree
* Data Structures

---

## Related Articles

* [Full And Complete Binary Tree From Given Preorder And Postorder Traversals](https://www.geeksforgeeks.org/full-and-complete-binary-tree-from-given-preorder-and-postorder-traversals/)

---

---

Here’s a crisp, interview-ready walkthrough for **Construct Tree from Preorder & Postorder (Full Binary Tree)** — with intuition, a hand-worked dry run, and two Python solutions in the requested format (clean optimal recursion + a simple baseline).

---

## 2) Intuition + Step-by-Step Dry Run

### Key facts

* It’s a **full** binary tree → every internal node has **exactly 2 children** (or 0).
* `pre[]` (root, left, right) and `post[]` (left, right, root) have **unique** values.
* For any subtree:

  * `pre[pre_i]` is the **root**.
  * If the root is a leaf, we’re done.
  * Otherwise, the **left child** of the root is `pre[pre_i + 1]`.
    Find this value in `post[]` to know how big the **left subtree** is.
    (Because `post` lists the whole left subtree first, then right, then root.)

This yields an O(n) solution if we prebuild a hashmap `pos_in_post[val] -> index`.

### Dry run (Example 1)

```
pre  = [1, 2, 4, 8, 9, 5, 3, 6, 7]
post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
```

We maintain a global pointer `pre_i` over `pre`.

1. `pre_i=0` → root = 1. Not a leaf → left child = `pre[1]=2`.

   * In `post`, index(2) = 4 ⇒ left subtree size = 4+1 = 5 elements in post.
   * Build left subtree from `pre[1..]` consuming exactly those nodes.

2. Build subtree rooted at 2 (`pre_i=1`):

   * left child = `pre[2]=4`. In post, idx(4)=2 ⇒ left size = 3.
   * Build left of 2: subtree rooted at 4 (`pre_i=2`):

     * left child = `pre[3]=8`. In post, idx(8)=0 ⇒ left size = 1.
     * Build left of 4: root=8 (`pre_i=3`) is leaf ⇒ done.
     * Build right of 4: root=9 (`pre_i=4`) is leaf ⇒ done.
     * Subtree 4 done; back to node 2.
   * Build right of 2: next root=5 (`pre_i=5`) is leaf ⇒ done.
   * Subtree 2 done; back to node 1.

3. Build right of 1: next root=3 (`pre_i=6`)

   * left child = `pre[7]=6`. In post, idx(6)=5 ⇒ left size = 6 elements up to 6.
   * But within the remaining segment, that corresponds to subtree size 1 → 6 is leaf.
   * Right child becomes 7 (`pre_i=8`) leaf.

Done → Tree:

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
   / \
  8   9
```

---

## 3) Python solutions (expected in interviews)

### A) Optimal Recursion (O(n) time, O(n) space)

* Build a hashmap for fast postorder index lookup.
* Use a **single moving pointer** over `pre` to build nodes top-down.
* At each step, if the current root is not a leaf, compute **left subtree size** from the left child’s position in `post`. Recurse for left, then right.

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructTree(self, pre, post):
        """
        Build a full binary tree from preorder and postorder.
        Assumptions:
          - Full tree (each node has 0 or 2 children)
          - All values are unique; appear in both traversals
        Time  : O(n)  (thanks to O(1) post-index lookups)
        Space : O(n)  (hashmap + recursion stack)
        """
        n = len(pre)
        if n == 0:
            return None

        # Map each value -> its index in post[] for O(1) splits
        idx_in_post = {val: i for i, val in enumerate(post)}

        # 'i' is a moving pointer in preorder (closed over by build())
        self.i = 0

        def build(l, r):
            """
            Rebuilds subtree whose nodes appear somewhere within post[l..r].
            Uses global 'self.i' to pull next root from preorder.
            """
            if l > r:
                return None

            # Create root from preorder
            root_val = pre[self.i]
            self.i += 1
            root = Node(root_val)

            # Leaf node: post[l]..post[r] only contains this root
            if l == r:
                return root

            # Next preorder value must be the left child (since it's full tree)
            left_child_val = pre[self.i]
            # Find how big the left subtree is by where that left child's
            # subtree ends in post (its root appears at idx_in_post[left_child_val])
            mid = idx_in_post[left_child_val]

            # Build left subtree spanning post[l..mid]
            root.left = build(l, mid)
            # Build right subtree spanning post[mid+1..r-1] (r is the current root)
            root.right = build(mid + 1, r - 1)

            return root

        # Entire tree spans post[0..n-1]
        return build(0, n - 1)
```

**Why it’s O(n):** Each node is created once, and the `idx_in_post` lookup is O(1), so the total is linear.

---

### B) Simple Baseline (search in post without hashmap) — **O(n²)** worst-case

This is the same idea, but each time we find the left child’s index with a linear scan in `post`. (Acceptable for small `n`, illustrates the idea when you forget to pre-hash.)

```python
class Solution:
    def constructTree(self, pre, post):
        """
        Baseline version: O(n^2) due to linear search in post[] at each split.
        Space: O(n)
        """
        n = len(pre)
        if n == 0:
            return None

        self.i = 0  # preorder index

        def find_in_post(val, l, r):
            for k in range(l, r + 1):
                if post[k] == val:
                    return k
            return -1  # should not happen with valid inputs

        def build(l, r):
            if l > r:
                return None
            root = Node(pre[self.i])
            self.i += 1

            if l == r:
                return root

            left_val = pre[self.i]
            mid = find_in_post(left_val, l, r)

            root.left = build(l, mid)
            root.right = build(mid + 1, r - 1)
            return root

        return build(0, n - 1)
```

---

## 4) Interview Q & A (short & useful)

**Q1. Why is the problem solvable from just preorder and postorder?**
In general it isn’t (multiple trees fit the same traversals), but the **full-binary** constraint makes the decomposition unique.

**Q2. How do you split left and right subtrees without an inorder array?**
For a non-leaf root `pre[i]`, its left child must be `pre[i+1]`. Find that value in `post`. Everything up to that index in `post` is the **entire left subtree**.

**Q3. What’s the time/space complexity of the optimal approach?**

* **Time:** O(n) (each node handled once; splits via O(1) hash lookup).
* **Space:** O(n) (hash map + recursion depth up to tree height; worst-case O(n)).

**Q4. What if the tree were not full?**
Pre+Post alone is **not sufficient** to reconstruct a unique tree. You’d need `inorder` or additional structure info.

**Q5. How do you verify your reconstruction?**
Traverse the resulting tree to reproduce preorder & postorder and compare to inputs.

---

### Tiny helper (optional, for local testing)

```python
def preorder(root):
    return [] if not root else [root.data] + preorder(root.left) + preorder(root.right)

def postorder(root):
    return [] if not root else postorder(root.left) + postorder(root.right) + [root.data]
```

Use these to confirm `preorder(root) == pre` and `postorder(root) == post` on your samples.

---

---


Absolutely — here’s a **single, runnable Python script** that:

* Reconstructs a **full** binary tree from **preorder** and **postorder** (optimal **O(n)**).
* Includes **inline comments** calling out **time/space complexity** exactly where they apply.
* Prints **preorder**, **postorder**, and **level-order** of the rebuilt tree for the provided inputs.
* Uses **timeit** to report average runtime per build.
* Ends with a short list of **high-impact real-world use cases**.

---

### 5) Full program (with input, output, and timing)

```python
"""
Construct a Full Binary Tree from Preorder and Postorder
=======================================================

Given traversals `pre` (preorder) and `post` (postorder) of a *full* binary tree,
reconstruct the tree and return its root.

Optimal approach:
- Use a moving pointer in preorder to pick roots in O(1).
- Use a hashmap of "value -> index in postorder" to split subtrees in O(1).
- Because the tree is FULL, if a node is not a leaf, its next preorder value
  must be its LEFT child — which uniquely determines the split.

Global Asymptotics:
  Time  : O(n)   — each node is created once and each split is O(1).
  Space : O(n)   — hashmap + recursion stack (worst-case height n).
"""

from collections import deque
from typing import Optional, List
import timeit
import sys


# ----------------------------- Tree Node ----------------------------- #
class Node:
    def __init__(self, val: int):
        self.data = val
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


# ----------------------- Helpful Traversals -------------------------- #
def preorder_trav(root: Optional[Node]) -> List[int]:
    """O(n) time, O(h) recursion space."""
    if not root:
        return []
    return [root.data] + preorder_trav(root.left) + preorder_trav(root.right)

def postorder_trav(root: Optional[Node]) -> List[int]:
    """O(n) time, O(h) recursion space."""
    if not root:
        return []
    return postorder_trav(root.left) + postorder_trav(root.right) + [root.data]

def level_order(root: Optional[Node]) -> List[int]:
    """O(n) time, O(w) space (w = max width)."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        cur = q.popleft()
        out.append(cur.data)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return out


# ----------------------------- Solution ------------------------------ #
class Solution:
    def constructTree(self, pre: List[int], post: List[int]) -> Optional[Node]:
        """
        Build a full binary tree from preorder and postorder.

        Steps & Local Costs:
        - Build a hashmap from post values to indices  -> O(n) time, O(n) space
        - Recursively rebuild with a single preorder pointer:
            * Node creation                                -> O(1)
            * Split left/right using hashmap               -> O(1) per node
          Total over all nodes                             -> O(n)
        """
        n = len(pre)
        if n == 0:
            return None

        # Map each value to its index in post for O(1) subtree split. O(n) time, O(n) space.
        post_idx = {val: i for i, val in enumerate(post)}

        self.pi = 0                  # O(1) space for moving pointer
        sys.setrecursionlimit(1_000_000)

        def build(l: int, r: int) -> Optional[Node]:
            """
            Rebuild subtree represented by post[l..r].
            - Base/leaf detection: O(1)
            - Create node from pre[self.pi]: O(1)
            - If internal node, split using post_idx: O(1)
            - Two recursive calls → total across tree O(n)
            """
            if l > r:
                return None

            # root from preorder (O(1))
            root_val = pre[self.pi]
            self.pi += 1
            root = Node(root_val)

            # Leaf subtree when post interval has single element (O(1))
            if l == r:
                return root

            # Because it's FULL, next preorder value is left child if not leaf
            left_val = pre[self.pi]
            mid = post_idx[left_val]   # O(1) lookup

            # Build left: occupies post[l..mid]
            root.left = build(l, mid)
            # Build right: occupies post[mid+1..r-1] (r is this root)
            root.right = build(mid + 1, r - 1)
            return root

        return build(0, n - 1)


# --------------------------- Demo + Timing --------------------------- #
def run_one_case(pre: List[int], post: List[int], title: str) -> None:
    print(f"\n{title}")
    print("Input preorder :", pre)
    print("Input postorder:", post)

    sol = Solution()
    root = sol.constructTree(pre, post)

    # Output traversals to verify (O(n) each)
    print("Rebuilt Preorder   :", preorder_trav(root))
    print("Rebuilt Postorder  :", postorder_trav(root))
    print("Level-Order (shape):", level_order(root))


def benchmark(pre: List[int], post: List[int], rounds: int = 50) -> None:
    sol = Solution()
    def once():
        sol.constructTree(pre, post)   # O(n) per build

    avg = timeit.timeit(once, number=rounds) / rounds
    print(f"\n[timeit] Average over {rounds} runs: {avg:.6f} seconds per build (O(n)).")


if __name__ == "__main__":
    # Example 1
    pre1  = [1, 2, 4, 8, 9, 5, 3, 6, 7]
    post1 = [8, 9, 4, 5, 2, 6, 7, 3, 1]
    run_one_case(pre1, post1, "Example 1")

    # Example 2
    pre2  = [1, 2, 4, 5, 3, 6, 7]
    post2 = [4, 5, 2, 6, 7, 3, 1]
    run_one_case(pre2, post2, "Example 2")

    # Small timing on example 1
    benchmark(pre1, post1, rounds=100)
```

**What you’ll see (typical):**

```
Example 1
Input preorder :  [1, 2, 4, 8, 9, 5, 3, 6, 7]
Input postorder:  [8, 9, 4, 5, 2, 6, 7, 3, 1]
Rebuilt Preorder   : [1, 2, 4, 8, 9, 5, 3, 6, 7]
Rebuilt Postorder  : [8, 9, 4, 5, 2, 6, 7, 3, 1]
Level-Order (shape): [1, 2, 3, 4, 5, 6, 7, 8, 9]

Example 2
Input preorder :  [1, 2, 4, 5, 3, 6, 7]
Input postorder:  [4, 5, 2, 6, 7, 3, 1]
Rebuilt Preorder   : [1, 2, 4, 5, 3, 6, 7]
Rebuilt Postorder  : [4, 5, 2, 6, 7, 3, 1]
Level-Order (shape): [1, 2, 3, 4, 5, 6, 7]

[timeit] Average over 100 runs: 0.0000xx seconds per build (O(n)).
```

---

### 6) Real-World Use Cases (most relevant)

1. **Expression Tree Reconstruction (Prefix + Postfix)**
   In full binary expression trees (operators are binary), prefix (preorder) and postfix (postorder) forms can be used to rebuild the exact tree for evaluation, optimization, or display.

2. **Program Trace → Call Tree**
   Systems that log **enter** (pre) and **exit** (post) events for nested calls/tasks can reconstruct the exact full call tree, helping with profiling, debugging, and flame-graph generation.

3. **Serialization/Deserialization**
   When only two traversals are stored (for compactness), this method reconstructs the exact full tree structure for further processing or rendering.
