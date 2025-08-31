
---

# Postorder Traversal 🌳

**Difficulty:** Basic
**Accuracy:** 74.96%
**Submissions:** 131K+
**Points:** 1
**Average Time:** 15m

---

## Problem Statement

Given a binary tree, find the **Postorder Traversal** of it and return a list containing the postorder traversal of the given tree.

---

## Examples

### Example 1:

**Input:**
root = `[19, 10, 8, 11, 13]`

**Tree Representation:**

```
        19
       /  \
     10    8
    /  \
   11   13
```

**Output:**
`[11, 13, 10, 8, 19]`

---

### Example 2:

**Input:**
root = `[11, 15, N, 7]`

**Tree Representation:**

```
       11
      /
    15
   /
  7
```

**Output:**
`[7, 15, 11]`

---

## Constraints:

* `1 <= number of nodes <= 10^5`
* `0 <= node->data <= 10^6`

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## Company Tags

* Morgan Stanley
* Snapdeal
* Walmart

---

## Topic Tags

* Tree
* Data Structures

---

## Related Articles

* [Postorder Traversal Of Binary Tree](https://www.geeksforgeeks.org/postorder-traversal-of-binary-tree/)

---

---

Great choice—postorder is the one where you visit **Left → Right → Root**. Here’s a crisp walk-through, then multiple interview-ready solutions, and finally a compact Q\&A.

---

## 2) Text explanation + step-by-step dry run

### What is postorder?

For every node:

1. Traverse its left subtree (postorder).
2. Traverse its right subtree (postorder).
3. Visit (append) the node itself.

This is perfect for problems where you need children processed before the parent (e.g., freeing memory, evaluating expression trees).

### Dry run on this tree

```
        19
       /  \
     10    8
    /  \
   11   13
```

Call `postOrder(19)`

* Recurse left → `postOrder(10)`

  * Recurse left → `postOrder(11)`

    * 11 has no children ⇒ output 11
  * Recurse right → `postOrder(13)`

    * 13 has no children ⇒ output 13
  * Visit 10 ⇒ output 10
* Recurse right → `postOrder(8)`

  * 8 has no children ⇒ output 8
* Visit 19 ⇒ output 19

Final order: **\[11, 13, 10, 8, 19]** ✅

---

## 3) Optimized Python solutions (interview-friendly)

All variants return a list of node values in postorder.

### A) Recursion (clean & canonical)

* Time: O(n) — each node visited once
* Space: O(h) — recursion stack height (h = tree height; O(n) in worst case, O(log n) for balanced)

```python
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        # Left -> Right -> Root
        out = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # visit left subtree
            dfs(node.right)         # visit right subtree
            out.append(node.data)   # visit node
        dfs(root)
        return out
```

### B) Iterative using **two stacks** (most common iterative pattern)

* Time: O(n)
* Space: O(n) for stacks and output

```python
class Solution:
    def postOrder(self, root):
        if not root:
            return []
        s1, s2 = [root], []   # s1: process stack, s2: results in reverse
        while s1:
            node = s1.pop()
            s2.append(node)
            # Push left and right so that when s2 is popped, order becomes Left, Right, Root
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        # s2 has nodes in Root, Right, Left -> reverse pop gives Left, Right, Root
        return [node.data for node in reversed(s2)]
```

### C) Iterative using **one stack** (trickier but space-friendly)

* Time: O(n)
* Space: O(h) average (stack of path)

Idea: Go left as far as possible, then peek: if right child exists and not processed, go right; otherwise process node.

```python
class Solution:
    def postOrder(self, root):
        out = []
        stack = []
        last_visited = None
        curr = root

        while curr or stack:
            # 1) Go as left as possible
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack[-1]
                # 2) If right child exists and not yet visited, go right
                if node.right and last_visited is not node.right:
                    curr = node.right
                else:
                    # 3) Visit node
                    out.append(node.data)
                    last_visited = node
                    stack.pop()
        return out
```

---

## 4) Likely interviewer Q\&A

**Q1. What’s the time and space complexity of postorder traversal?**
**A.** Time is **O(n)** (each node once). Space is **O(h)** for recursion/stack where **h** is tree height (O(n) worst, O(log n) balanced).

**Q2. When would you prefer iterative over recursive?**
**A.** When recursion depth may exceed call stack (degenerate trees), or when recursion is disallowed. The two-stack method is the easiest iterative approach.

**Q3. Can we do postorder in one stack?**
**A.** Yes—track `last_visited` to know whether you’ve already processed the right subtree of the top node. (See solution C.)

**Q4. Why is postorder useful?**
**A.** Parent depends on results of children: expression evaluation, deleting/freeing tree nodes, bottom-up dynamic programming on trees.

**Q5. How would you modify code to return nodes instead of values?**
**A.** Append `out.append(node)` instead of `node.data`.

**Q6. How to handle empty tree?**
**A.** Return `[]`. All variants do that.

---

---

Here’s a **complete, runnable program** that implements postorder traversal three ways (recursive, iterative with two stacks, iterative with one stack), includes **clear inline complexity notes**, builds sample inputs, **prints outputs**, and measures wall time with `timeit`.

> Postorder = **Left → Right → Root**

```python
#!/usr/bin/env python3
"""
Postorder Traversal (Left -> Right -> Root)

Complexities:
- Time:  O(n)  for all approaches (visit each node once)
- Space: Recursion: O(h) call stack (h = height), Two-stacks: O(n), One-stack: O(h)
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
import timeit


# ---------------------------
# Node definition
# ---------------------------
@dataclass
class Node:
    data: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


# ---------------------------
# Solution with 3 approaches
# ---------------------------
class Solution:
    # A) Recursive DFS
    # Time:  O(n)   -- each node visited once
    # Space: O(h)   -- recursion depth (worst O(n), balanced O(log n))
    def postOrder_recursive(self, root: Optional[Node]) -> List[int]:
        out: List[int] = []

        def dfs(node: Optional[Node]) -> None:
            if not node:                            # O(1)
                return
            dfs(node.left)                          # O(size of left subtree)
            dfs(node.right)                         # O(size of right subtree)
            out.append(node.data)                   # O(1)

        dfs(root)
        return out

    # B) Iterative with TWO stacks
    # Idea: push root to s1, pop -> push to s2, push its children into s1.
    # Finally, s2 (reversed) yields Left,Right,Root.
    # Time:  O(n)
    # Space: O(n)  -- s1 + s2 can together hold all nodes
    def postOrder_two_stacks(self, root: Optional[Node]) -> List[int]:
        if not root:
            return []
        s1: List[Node] = [root]                     # O(1)
        s2: List[Node] = []                         # O(1)
        while s1:                                   # each node pushed/popped once => O(n)
            node = s1.pop()
            s2.append(node)                         # add visit order
            if node.left:                           # O(1) checks
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        # reverse order of s2 to get Left, Right, Root
        return [node.data for node in reversed(s2)] # O(n)

    # C) Iterative with ONE stack (track last visited)
    # Time:  O(n)
    # Space: O(h)  -- at most height of tree on the stack
    def postOrder_one_stack(self, root: Optional[Node]) -> List[int]:
        out: List[int] = []
        stack: List[Node] = []
        curr, last = root, None                     # last = last visited node
        # Standard simulation of recursion:
        while curr or stack:                        # O(n) iterations overall
            if curr:
                stack.append(curr)                  # go left: push nodes
                curr = curr.left
            else:
                node = stack[-1]                    # peek
                # if right child exists and not processed, traverse right
                if node.right and last is not node.right:
                    curr = node.right
                else:
                    out.append(node.data)           # visit
                    last = node
                    stack.pop()
        return out


# ---------------------------
# Helpers to build test trees
# ---------------------------
def build_sample_tree() -> Node:
    # Tree from prompt examples:
    #         19
    #        /  \
    #      10    8
    #     /  \
    #   11   13
    n11 = Node(11)
    n13 = Node(13)
    n10 = Node(10, n11, n13)
    n8  = Node(8)
    n19 = Node(19, n10, n8)
    return n19

def build_skewed_tree(n: int) -> Node:
    # Right-skewed chain to stress recursion depth/stack behavior
    root = Node(0)
    cur = root
    for i in range(1, n):
        cur.right = Node(i)
        cur = cur.right
    return root


# ---------------------------
# Pretty print utility
# ---------------------------
def show(title: str, result: List[int]) -> None:
    print(f"{title}: {result}")


# ---------------------------
# Main (demo + timeit)
# ---------------------------
def main():
    sol = Solution()

    # --- Input 1: sample from statement ---
    root = build_sample_tree()
    # Expected: [11, 13, 10, 8, 19]
    r1 = sol.postOrder_recursive(root)
    r2 = sol.postOrder_two_stacks(root)
    r3 = sol.postOrder_one_stack(root)
    show("Recursive  ", r1)
    show("Two stacks ", r2)
    show("One stack  ", r3)

    # --- Input 2: single node ---
    single = Node(42)
    show("Single node (recursive)", sol.postOrder_recursive(single))  # [42]

    # --- Input 3: skewed (to show stacks vs recursion) ---
    skew = build_skewed_tree(7)  # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    show("Skewed (one stack)", sol.postOrder_one_stack(skew))         # [6,5,4,3,2,1,0]

    # --- Timing with timeit ---
    # Note: each timeit runs the traversal 10,000 times for stable numbers on small trees.
    # For large trees, reduce the repeat count to avoid long runs.
    setup_code = (
        "from __main__ import Solution, build_sample_tree, build_skewed_tree\n"
        "sol = Solution()\n"
        "root = build_sample_tree()\n"
        "skew = build_skewed_tree(1000)\n"
    )
    t_rec_sample = timeit.timeit("sol.postOrder_recursive(root)", setup=setup_code, number=10000)
    t_two_sample = timeit.timeit("sol.postOrder_two_stacks(root)", setup=setup_code, number=10000)
    t_one_sample = timeit.timeit("sol.postOrder_one_stack(root)", setup=setup_code, number=10000)

    print("\n--- timeit on sample tree (10,000 runs) ---")
    print(f"Recursive   : {t_rec_sample:.6f}s")
    print(f"Two-stacks  : {t_two_sample:.6f}s")
    print(f"One-stack   : {t_one_sample:.6f}s")

    # A quick timing on a larger skewed tree (1000 nodes), fewer runs
    t_one_skew = timeit.timeit("sol.postOrder_one_stack(skew)", setup=setup_code, number=200)
    print("\n--- timeit on 1000-node skewed tree (200 runs) ---")
    print(f"One-stack   : {t_one_skew:.6f}s")


if __name__ == "__main__":
    main()
```

### Example Output (for the sample tree)

```
Recursive  : [11, 13, 10, 8, 19]
Two stacks : [11, 13, 10, 8, 19]
One stack  : [11, 13, 10, 8, 19]
Single node (recursive): [42]
Skewed (one stack): [6, 5, 4, 3, 2, 1, 0]

--- timeit on sample tree (10,000 runs) ---
Recursive   : 0.0xxx s
Two-stacks  : 0.0xxx s
One-stack   : 0.0xxx s

--- timeit on 1000-node skewed tree (200 runs) ---
One-stack   : 0.xxxx s
```

*(Exact timings depend on your machine.)*

---

## 6) Real-World Use Cases (most important)

1. **Expression tree evaluation / code generation**
   Postorder naturally computes child values before the operator node (parent), matching evaluation order.

2. **Resource cleanup / dependency teardown**
   When an object depends on its children (files in directories, tasks with prerequisites), postorder frees/destroys children before the parent.

3. **Bottom-up dynamic programming on trees**
   Many DP-on-tree problems (e.g., compute subtree sums, choose best subtree) require children processed first.

4. **Filesystem operations**
   Deleting a directory tree safely uses postorder: delete files/subdirs first, then the directory itself.

