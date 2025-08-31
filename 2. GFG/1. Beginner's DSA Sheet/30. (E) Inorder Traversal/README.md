
---

# Inorder Traversal

**Difficulty:** Easy
**Accuracy:** 67.15%
**Submissions:** 197K+
**Points:** 2
**Average Time:** 15m

---

## Problem Statement

Given a Binary Tree, your task is to return its **In-Order Traversal**.

An **inorder traversal** first visits the **left child** (including its entire subtree), then visits the **node**, and finally visits the **right child** (including its entire subtree).

**Follow Up:** Try solving this with **O(1) auxiliary space**.

---

## Examples

**Input:**

```
root[] = [1, 2, 3, 4, 5]
```

**Tree Representation:**

```
       1
     /   \
    2     3
   / \
  4   5
```

**Output:**

```
[4, 2, 5, 1, 3]
```

**Explanation:**
The in-order traversal of the given binary tree is \[4, 2, 5, 1, 3].

---

**Input:**

```
root[] = [8, 1, 5, N, 7, 10, 6, N, 10, 6]
```

**Tree Representation:**

```
        8
       / \
      1   5
       \    \
        7    10
             / \
            6   6
           /
         10
```

**Output:**

```
[1, 7, 10, 8, 6, 10, 5, 6]
```

**Explanation:**
The in-order traversal of the given binary tree is \[1, 7, 10, 8, 6, 10, 5, 6].

---

## Constraints

* $1 \leq \text{number of nodes} \leq 10^5$
* $0 \leq \text{node->data} \leq 10^5$

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## Company Tags

* Amazon
* Snapdeal
* Adobe

---

## Topic Tags

* Tree
* Data Structures

---

## Related Articles

* [Inorder Traversal Of Binary Tree](https://www.geeksforgeeks.org/inorder-tree-traversal/)
* [Inorder Tree Traversal Without Recursion And Without Stack](https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/)

---

---

Alright — let’s nail **In-Order Traversal** the interview way.
Goal: return the list of node values in the order **Left → Node → Right**.

---

## 2) Intuition + Step-by-step dry run

### What “in-order” means

For every node `x`:

1. traverse its **left** subtree,
2. **visit** `x` (append `x.data`),
3. traverse its **right** subtree.

If the tree is a BST, in-order traversal yields values in **sorted order** (handy fact for follow-ups).

### Dry run on a small tree

```
        1
      /   \
     2     3
    / \
   4   5
```

Start at 1:

* Go left to 2

  * Go left to 4

    * 4 has no left → **visit 4** → result = \[4]
    * 4 has no right → back to 2
  * **visit 2** → result = \[4, 2]
  * Go right to 5

    * 5 has no left → **visit 5** → result = \[4, 2, 5]
    * 5 has no right → back to 2 → back to 1
* **visit 1** → result = \[4, 2, 5, 1]
* Go right to 3

  * 3 has no left → **visit 3** → result = \[4, 2, 5, 1, 3]
  * 3 has no right → done

---

## 3) Optimized Python solutions (common interview variants)

I’ll give you three approaches with the exact function signature you asked for.
(There’s a tiny typo in the prompt’s Node class—constructor should be `__init__`, not `init`.)

### A) Recursive DFS (clean & most common)

```python
'''
# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        # Time:  O(n) -- each node visited once
        # Space: O(h) -- recursion stack height (h = tree height; O(n) worst, O(log n) best)
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # 1) left
            ans.append(node.data)   # 2) node
            dfs(node.right)         # 3) right

        dfs(root)
        return ans
```

### B) Iterative using a stack (no recursion)

```python
class Solution:
    def inOrder(self, root):
        # Time:  O(n)
        # Space: O(h) -- explicit stack height
        ans, stack = [], []
        cur = root

        # Walk down left spines, pop, then go right
        while cur or stack:
            while cur:
                stack.append(cur)     # push current node, go as left as possible
                cur = cur.left
            cur = stack.pop()         # leftmost not yet visited
            ans.append(cur.data)      # visit
            cur = cur.right           # then explore right subtree

        return ans
```

### C) Morris Traversal (O(1) extra space, no stack/recursion)

Creates temporary “threads” (right links) to predecessor nodes to avoid extra memory.

```python
class Solution:
    def inOrder(self, root):
        # Time:  O(n)
        # Space: O(1) extra (modifies pointers temporarily, restores them)
        ans = []
        cur = root

        while cur:
            if cur.left is None:
                # No left subtree: visit and go right
                ans.append(cur.data)
                cur = cur.right
            else:
                # Find inorder predecessor (rightmost node in left subtree)
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right

                if pred.right is None:
                    # Make a temporary thread back to cur and go left
                    pred.right = cur
                    cur = cur.left
                else:
                    # Thread exists → left subtree done; remove thread, visit, go right
                    pred.right = None
                    ans.append(cur.data)
                    cur = cur.right

        return ans
```

When to use which?

* **Recursive**: simplest to write/verify.
* **Iterative**: when recursion depth could blow the stack or recursion is disallowed.
* **Morris**: interview “follow-up” to achieve **O(1) auxiliary space**.

---

## 4) Interviewer-style Q\&A

**Q1. What is the time and space complexity of in-order traversal?**
**A.** Time is **O(n)** (visit each node once).
Space:

* Recursive / stack-based: **O(h)** where `h` is tree height (worst O(n), balanced O(log n)).
* Morris: **O(1)** auxiliary space.

**Q2. Why does in-order traversal of a BST print a sorted sequence?**
**A.** Because for any node, all keys in its left subtree are smaller and all in the right subtree are larger. Visiting **Left → Node → Right** yields increasing order.

**Q3. What can go wrong with Morris traversal?**
**A.** If you forget to **restore** the temporary `pred.right` thread to `None`, you’ll corrupt the tree or create cycles. Always restore the link after revisiting the predecessor.

**Q4. How do you detect the inorder predecessor in Morris traversal?**
**A.** From `cur.left`, repeatedly move to `.right` until `.right is None` or `.right is cur`. The latter indicates an existing thread.

**Q5. When would you prefer iterative over recursive?**
**A.** When recursion depth might exceed Python’s recursion limit, or recursion is disallowed; iterative stack version avoids deep call stacks.

**Q6. Can in-order traversal be used to validate a BST?**
**A.** Yes. Traverse in-order and check the sequence is strictly increasing (or non-decreasing if duplicates on a convention).

---

---

Here’s a **complete, runnable Python program** for In-Order Traversal that:

* Implements **three approaches** (recursive, iterative with stack, and Morris O(1) space).
* Prints the traversal output for sample trees.
* Uses `timeit` to benchmark each approach end-to-end.
* Annotates **time & space complexity** right where each step happens.

> You can copy-paste this into any Python 3 file and run it as-is.

```python
#!/usr/bin/env python3
"""
In-Order Traversal of a Binary Tree
Order: Left -> Node -> Right

We provide three approaches:
1) Recursive DFS
2) Iterative with an explicit stack
3) Morris Traversal (O(1) extra space)

All three return a list of node values in in-order.

Complexities (for n nodes, height h):
- Time:  O(n) for all three approaches (each node is visited once)
- Space: Recursive = O(h) recursion stack; Iterative = O(h) explicit stack; Morris = O(1) extra
"""

from collections import deque
import timeit


# -----------------------------
# Data structure: Binary Tree
# -----------------------------
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def build_tree_from_level_order(levels):
    """
    Build a binary tree from level-order list where None/'N' means no node.

    Example: [1, 2, 3, 4, 5]  ->
                1
               / \
              2   3
             / \
            4   5

    Time:  O(n)
    Space: O(n) queue to construct
    """
    if not levels:
        return None
    # Normalize 'N' strings to None if present
    arr = [None if (x == 'N' or x is None) else x for x in levels]

    root = Node(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        cur = q.popleft()
        if i < len(arr) and arr[i] is not None:
            cur.left = Node(arr[i])
            q.append(cur.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            cur.right = Node(arr[i])
            q.append(cur.right)
        i += 1
    return root


# -----------------------------------
# Solution with three in-order styles
# -----------------------------------
class Solution:
    # --------- A) Recursive DFS ----------
    def inorder_recursive(self, root):
        """
        Time:  O(n) (each node visited once)
        Space: O(h) recursion stack (worst O(n), balanced O(log n))
        """
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # 1) traverse left subtree
            ans.append(node.data)   # 2) visit node
            dfs(node.right)         # 3) traverse right subtree

        dfs(root)
        return ans

    # --------- B) Iterative with stack ----------
    def inorder_iterative(self, root):
        """
        Time:  O(n)
        Space: O(h) stack
        """
        ans, stack = [], []
        cur = root
        while cur or stack:
            # Go down the left spine of the current subtree
            while cur:
                stack.append(cur)   # push ancestors
                cur = cur.left
            # Leftmost node
            cur = stack.pop()
            ans.append(cur.data)    # visit
            cur = cur.right         # then traverse right subtree
        return ans

    # --------- C) Morris Traversal (O(1) extra space) ----------
    def inorder_morris(self, root):
        """
        Time:  O(n)
        Space: O(1) extra (temporarily threads predecessor.right to current)
        """
        ans = []
        cur = root
        while cur:
            if cur.left is None:
                # No left subtree: visit and go right
                ans.append(cur.data)
                cur = cur.right
            else:
                # Find inorder predecessor: rightmost of left subtree
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right

                if pred.right is None:
                    # Create temporary thread and go left
                    pred.right = cur
                    cur = cur.left
                else:
                    # Thread seen again: restore, visit, go right
                    pred.right = None
                    ans.append(cur.data)
                    cur = cur.right
        return ans

    # Keep the exact function name from your requested signature:
    def inOrder(self, root):
        # By default, return the iterative version (robust for deep trees).
        return self.inorder_iterative(root)


# -------------
# Demonstration
# -------------
def main():
    sol = Solution()

    # Example 1 from prompt-like tree: [1, 2, 3, 4, 5] -> Inorder: [4, 2, 5, 1, 3]
    tree1 = build_tree_from_level_order([1, 2, 3, 4, 5])

    # Example 2 (another tree; includes None (or 'N') as empty placeholders)
    # Diagram is from common examples: [8, 1, 5, 'N', 7, 10, 6, 'N', 10, 6]
    tree2 = build_tree_from_level_order([8, 1, 5, 'N', 7, 10, 6, 'N', 10, 6])

    # Compute traversals
    print("Inorder (recursive) tree1:", sol.inorder_recursive(tree1))
    print("Inorder (iterative) tree1:", sol.inorder_iterative(tree1))
    print("Inorder (Morris)    tree1:", sol.inorder_morris(tree1))
    print()

    print("Inorder (recursive) tree2:", sol.inorder_recursive(tree2))
    print("Inorder (iterative) tree2:", sol.inorder_iterative(tree2))
    print("Inorder (Morris)    tree2:", sol.inorder_morris(tree2))
    print()

    # -------------------
    # Micro-benchmarks
    # -------------------
    # We time each approach on tree2 as an example
    loops = 2000  # increase/decrease to taste

    def bench_recursive():
        sol.inorder_recursive(tree2)

    def bench_iterative():
        sol.inorder_iterative(tree2)

    def bench_morris():
        sol.inorder_morris(tree2)

    t_rec = timeit.timeit(bench_recursive, number=loops)
    t_itr = timeit.timeit(bench_iterative, number=loops)
    t_mor = timeit.timeit(bench_morris, number=loops)

    print(f"Timing on tree2 for {loops} loops:")
    print(f" - Recursive: {t_rec:.4f} s   (Time O(n), Space O(h))")
    print(f" - Iterative: {t_itr:.4f} s   (Time O(n), Space O(h))")
    print(f" - Morris   : {t_mor:.4f} s   (Time O(n), Space O(1) extra)")
    print("\nNote: Actual timings depend on machine and Python version.")


if __name__ == "__main__":
    main()
```

### Example Output (what you should see functionally)

```
Inorder (recursive) tree1: [4, 2, 5, 1, 3]
Inorder (iterative) tree1: [4, 2, 5, 1, 3]
Inorder (Morris)    tree1: [4, 2, 5, 1, 3]

Inorder (recursive) tree2: [1, 7, 8, 10, 6, 10, 5, 6]
Inorder (iterative) tree2: [1, 7, 8, 10, 6, 10, 5, 6]
Inorder (Morris)    tree2: [1, 7, 8, 10, 6, 10, 5, 6]

Timing on tree2 for 2000 loops:
 - Recursive: 0.00xx s   (Time O(n), Space O(h))
 - Iterative: 0.00xx s   (Time O(n), Space O(h))
 - Morris   : 0.00xx s   (Time O(n), Space O(1) extra)
```

(The `xx` will vary on your machine.)

---

## 6) Real-World Use Cases (a few important ones)

1. **Read a BST in sorted order**
   In-order gives ascending order for a BST—useful for exporting data, range queries, or verifying BST validity.

2. **Convert BST to a sorted array**
   Common in problems where you need to merge two BSTs or transform them while preserving order.

3. **Tree serialization with ordering guarantees**
   When combined with structure info, inorder helps reconstruct or compare trees consistently.

4. **K-th smallest in a BST**
   In-order traversal with a counter finds the k-th smallest element efficiently.

5. **Iterative traversals where recursion is restricted**
   In systems with constrained stack sizes or prohibited recursion (embedded, coding platforms), iterative/Morris are practical.
