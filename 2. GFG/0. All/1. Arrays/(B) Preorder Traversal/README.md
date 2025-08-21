
---

# Preorder Traversal

**Difficulty:** Basic
**Accuracy:** 62.73%
**Submissions:** 185K+
**Points:** 1
**Average Time:** 15m

---

## Problem Statement

Given a binary tree, find its preorder traversal.

---

## Examples

**Example 1:**

```
Input: 
    1
   /
  4
 / \
4   2

Output: [1, 4, 4, 2]
```

**Example 2:**

```
Input:
      6
     / \
    3   2
     \
      1
       \
        2

Output: [6, 3, 1, 2, 2]
```

**Example 3:**

```
Input:
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

Output: [8, 3, 1, 6, 4, 7, 10, 14, 13]
```

---

## Constraints

* $1 \leq \text{number of nodes} \leq 10^5$
* $0 \leq \text{node->data} \leq 10^6$

---

## Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(n)$

---

## Company Tags

* Flipkart
* Amazon
* Microsoft
* Walmart

---

## Topic Tags

* `Stack`, `Tree`, `Data Structures`

---

## Related Articles

* [Preorder Traversal Of Binary Tree](https://www.geeksforgeeks.org/preorder-traversal-of-binary-tree/)

---

---

Here’s a crisp, interview‑style walkthrough and three Python solutions (simple recursive, iterative with a stack, and Morris preorder with O(1) extra space). I’ve matched your required class/method signature.

---

## 2) Text explanation (what and why)

**Preorder traversal** visits nodes in the order: **Root → Left subtree → Right subtree**.

Two common ways to implement it:

1. **Recursive DFS** (the “textbook” way): call the function on the left, then on the right.
2. **Iterative DFS with a stack** (production‑safe in Python because recursion depth can overflow for n≈1e5).
3. **Morris Preorder** (advanced): uses threaded binary tree idea to do preorder in O(1) extra space by temporarily linking predecessors.

---

## Step‑by‑step dry run (small example)

Take the tree:

```
       6
     /   \
    3     2
     \
      1
       \
        2
```

**Preorder (Root, Left, Right)**:

* Start at 6 → output `[6]`.
* Go left to 3 → output `[6, 3]`.
* 3’s left is None; go right to 1 → output `[6, 3, 1]`.
* 1’s left is None; go right to 2 → output `[6, 3, 1, 2]`.
* Done left subtree of 6; go right to 2 → output `[6, 3, 1, 2, 2]`.
* End.

The same order is achieved by all three approaches below.

---

## 3) Optimized codes in different ways

### A) **Brute/Easy (Recursive DFS)** – clearest for interviews

```python
'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def preorder(self, root):
        """
        Returns list of nodes in preorder (Root -> Left -> Right)
        Time:  O(n) — each node visited once
        Space: O(h) recursion stack, h = tree height (O(n) worst-case, O(log n) avg for balanced)
        """
        ans = []

        def dfs(node):
            if not node:          # Base case
                return
            ans.append(node.data) # Root
            dfs(node.left)        # Left
            dfs(node.right)       # Right

        dfs(root)
        return ans
```

**Why interviewers like it:** shortest, most readable, shows you know the order.
**Caveat in Python:** for very deep trees (n \~ 10^5), recursion may hit recursion limit; mention iterative as safer.

---

### B) **Iterative with Stack** – production‑safe in Python

```python
'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def preorder(self, root):
        """
        Iterative preorder using an explicit stack
        Time:  O(n)
        Space: O(h) for stack (O(n) worst-case skewed, O(log n) avg balanced)
        """
        if not root:
            return []

        ans, st = [], [root]
        while st:
            node = st.pop()            # pop current
            ans.append(node.data)      # visit Root
            # push Right first so Left is processed first
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return ans
```

**Why interviewers like it:** avoids recursion limit; demonstrates control over traversal order via stack push sequence.

---

### C) **Morris Preorder (O(1) extra space)** – advanced/bonus

```python
'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def preorder(self, root):
        """
        Morris Preorder traversal (threaded tree), no extra stack/recursion.
        Time:  O(n)
        Space: O(1) auxiliary (modifies pointers temporarily, restores them)
        """
        ans = []
        cur = root
        while cur:
            if not cur.left:
                # No left child: visit current and move to right
                ans.append(cur.data)
                cur = cur.right
            else:
                # Find inorder predecessor (rightmost node in left subtree)
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right

                if pre.right is None:
                    # Make a temporary thread to current, visit current (preorder visit),
                    # then go to left subtree
                    ans.append(cur.data)
                    pre.right = cur
                    cur = cur.left
                else:
                    # Thread exists -> remove it and go right
                    pre.right = None
                    cur = cur.right
        return ans
```

**Why interviewers like it:** shows depth; you understand threaded traversal and can reason about O(1) space traversals.

---

## 4) Interview Q\&A (high‑yield)

1. **What is preorder traversal order?**
   Root → Left → Right.

2. **Time and space complexity?**
   Time O(n) for all approaches.
   Space: Recursive/Iterative use O(h) auxiliary; Morris uses O(1) auxiliary (but temporarily modifies pointers).

3. **Why push right before left on the stack?**
   Stack is LIFO; pushing right first ensures the left child is processed next (preorder demands left before right).

4. **When can recursion fail in Python?**
   With very deep/skewed trees (depth > \~1000 by default). Use the iterative version.

5. **How does Morris Preorder work in one line?**
   It temporarily sets the right pointer of the inorder predecessor to the current node to avoid a stack/recursion, visiting each node in preorder and restoring pointers afterward.

6. **Preorder vs Inorder vs Postorder?**

   * Preorder: Root, Left, Right (useful for copying/serializing trees).
   * Inorder: Left, Root, Right (BST inorder yields sorted keys).
   * Postorder: Left, Right, Root (useful for deletions/freeing).

7. **How do you handle an empty tree?**
   Return an empty list.

8. **What if the tree is skewed (like a linked list)?**
   Time stays O(n); recursion stack becomes O(n). Iterative avoids recursion stack growth.

9. **Where is preorder used in practice?**
   Serialization (prefix forms), generating prefix expressions from expression trees, exporting/printing hierarchical structures in “parent then children” order.

10. **Can you do preorder without extra space and without altering the tree?**
    Not in general; you need recursion stack or an explicit stack. Morris achieves O(1) auxiliary but temporarily changes pointers (restored later).

---

---

Awesome—here’s a complete, runnable program that:

* Implements **three** preorder traversals (recursive, iterative, Morris O(1) space).
* Includes **inline time & space comments** right where they matter.
* Builds sample inputs, prints **input and output**, and uses `timeit`‑style timing (`perf_counter`) for the overall run.

> You can paste this into a single Python file and run it as‑is.

```python
"""
Preorder Traversal – Full Program with timing and I/O

Preorder order: Root -> Left -> Right
We include three approaches:
  A) Recursive DFS
  B) Iterative with an explicit stack
  C) Morris Preorder (O(1) auxiliary space)

We also print inputs/outputs and measure end-to-end runtime using perf_counter.
"""

from time import perf_counter
from collections import deque

# -----------------------------
# Node definition for a binary tree
# -----------------------------
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# -----------------------------
# Solution implementing 3 variants
# -----------------------------
class Solution:
    # ---- A) Recursive DFS ----
    def preorder_recursive(self, root):
        """
        Time:  O(n) – each node visited once
        Space: O(h) – recursion depth (h = height; worst-case O(n) for skewed tree)
        """
        ans = []

        def dfs(node):
            if not node:                 # O(1) check
                return
            ans.append(node.data)        # O(1) append
            dfs(node.left)               # O(h) stack depth
            dfs(node.right)              # O(h) stack depth

        dfs(root)
        return ans

    # ---- B) Iterative with stack ----
    def preorder_iterative(self, root):
        """
        Time:  O(n) – each node pushed/popped once
        Space: O(h) – stack (height of tree; worst-case O(n))
        """
        if not root:
            return []
        ans = []
        st = [root]                      # O(1) init
        while st:                        # loop runs n times overall
            node = st.pop()              # O(1)
            ans.append(node.data)        # O(1)
            # Push right first so left is processed next
            if node.right:
                st.append(node.right)    # O(1)
            if node.left:
                st.append(node.left)     # O(1)
        return ans

    # ---- C) Morris Preorder (O(1) extra space) ----
    def preorder_morris(self, root):
        """
        Time:  O(n)
        Space: O(1) auxiliary – temporarily rewires pointers, restores later
        """
        ans = []
        cur = root
        while cur:
            if not cur.left:
                ans.append(cur.data)     # visit when no left child
                cur = cur.right
            else:
                # Find inorder predecessor of cur (rightmost in left subtree)
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right
                if pre.right is None:
                    # Thread to cur and visit cur (preorder visit)
                    ans.append(cur.data)
                    pre.right = cur
                    cur = cur.left
                else:
                    # Remove thread and go right
                    pre.right = None
                    cur = cur.right
        return ans


# -----------------------------
# Utilities to build/pretty-print test trees
# -----------------------------
def build_tree_from_level_order(vals):
    """
    Build a binary tree from a level-order list containing ints or None.
    Example: [6, 3, 2, None, 1, None, None, None, 2]
    Time:  O(n)
    Space: O(n)
    """
    if not vals:
        return None
    it = iter(vals)
    root = Node(next(it))
    q = deque([root])
    for v in it:
        node = q.popleft()
        # left
        if v is not None:
            node.left = Node(v)
            q.append(node.left)
        # right (pull next if exists)
        try:
            w = next(it)
        except StopIteration:
            break
        if w is not None:
            node.right = Node(w)
            q.append(node.right)
    return root


def tree_to_level_order(root):
    """
    Level-order listing for display only.
    Time:  O(n), Space: O(n)
    """
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        out.append(node.data if node else None)
        if node:
            q.append(node.left)
            q.append(node.right)
    # trim trailing None for cleaner print
    while out and out[-1] is None:
        out.pop()
    return out


# -----------------------------
# Main demo with timing
# -----------------------------
if __name__ == "__main__":
    # Build a couple of example trees
    # Example 1 (matches the second example style in prompt):
    #        6
    #      /   \
    #     3     2
    #      \
    #       1
    #        \
    #         2
    vals1 = [6, 3, 2, None, 1, None, None, None, 2]
    root1 = build_tree_from_level_order(vals1)

    # Example 2 (bigger, for timing):
    #            8
    #          /   \
    #         3     10
    #        / \      \
    #       1   6      14
    #          / \     /
    #         4   7   13
    vals2 = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    root2 = build_tree_from_level_order(vals2)

    sol = Solution()

    print("=== INPUT (tree 1 level-order) ===")
    print(tree_to_level_order(root1))
    print("=== INPUT (tree 2 level-order) ===")
    print(tree_to_level_order(root2))
    print()

    # Time the overall program run (all methods, both trees)
    t0 = perf_counter()

    # Recursive
    out1_rec = sol.preorder_recursive(root1)
    out2_rec = sol.preorder_recursive(root2)

    # Iterative
    out1_it = sol.preorder_iterative(root1)
    out2_it = sol.preorder_iterative(root2)

    # Morris
    out1_mo = sol.preorder_morris(root1)
    out2_mo = sol.preorder_morris(root2)

    t1 = perf_counter()

    print("=== OUTPUTS ===")
    print("Recursive  (tree1):", out1_rec)
    print("Iterative  (tree1):", out1_it)
    print("Morris     (tree1):", out1_mo)
    print()
    print("Recursive  (tree2):", out2_rec)
    print("Iterative  (tree2):", out2_it)
    print("Morris     (tree2):", out2_mo)
    print()

    print(f"Total program runtime (s): {t1 - t0:.6f}")
```

### Sample Output (will be similar)

```
=== INPUT (tree 1 level-order) ===
[6, 3, 2, None, 1, None, None, None, 2]
=== INPUT (tree 2 level-order) ===
[8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]

=== OUTPUTS ===
Recursive  (tree1): [6, 3, 1, 2, 2]
Iterative  (tree1): [6, 3, 1, 2, 2]
Morris     (tree1): [6, 3, 1, 2, 2]

Recursive  (tree2): [8, 3, 1, 6, 4, 7, 10, 14, 13]
Iterative  (tree2): [8, 3, 1, 6, 4, 7, 10, 14, 13]
Morris     (tree2): [8, 3, 1, 6, 4, 7, 10, 14, 13]

Total program runtime (s): 0.000xyz
```

> The three variants must match; if they differ, check your tree building or pointer restoring in Morris.

---

## 6) Real‑World Use Cases (only the key ones)

1. **Serialization / Export of Hierarchies**
   Output parent before children (e.g., exporting UI trees, org charts, directory trees) for top‑down rebuilds.

2. **Expression Trees (Compilers/Interpreters)**
   Generating **prefix notation** (Polish notation) from an expression tree is a preorder traversal.

3. **Code Generators & AST Walkers**
   Visiting the node (parent construct) before its parts (children) matches many compilation and transformation passes.

4. **Configuration / Policy Trees**
   Apply a parent policy first, then refine with children—preorder is a natural fit.
