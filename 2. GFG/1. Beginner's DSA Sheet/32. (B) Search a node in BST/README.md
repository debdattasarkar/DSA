
---

# Search a Node in BST

**Difficulty:** Basic
**Accuracy:** 68.46%
**Submissions:** 105K+
**Points:** 1
**Average Time:** 15m

---

## Problem Statement

Given a **Binary Search Tree (BST)** and a node value **X**, find if the node with value **X** is present in the BST or not.

---

## Example 1:

**Input:**

```
       2
        \
        81
       /  \
      42   87
       \     \
       45     90
      /
     66
```

X = 87

**Output:**

```
1
```

**Explanation:**
As 87 is present in the given nodes, the output will be **1**.

---

## Example 2:

**Input:**

```
       6
        \
         8
        / \
       7   9
```

X = 11

**Output:**

```
0
```

**Explanation:**
As 11 is not present in the given nodes, the output will be **0**.

---

## Your Task

You don't need to read input or print anything.
Complete the function **`search()`** which returns **true** if the node with value **X** is present in the BST, else returns **false**.

---

## Expected Time Complexity

* **O(Height of the BST)**

## Expected Auxiliary Space

* **O(1)**

---

## Constraints

* **1 ≤ Number of nodes ≤ 10⁵**

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## Company Tags

* Linkedin

---

## Topic Tags

* Binary Search Tree
* Data Structures

---

## Related Articles

* [Binary Search Tree Set 1 Search And Insertion](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)

---

---

Here’s a tight, interview-ready package for **“Search a node in a BST”**.

---

# 2) Problem intuition + step-by-step dry run

**BST property**
For every node `N`, all values in `N.left` are `< N.data`, and all values in `N.right` are `> N.data`.
So to find `x`, at each node:

* if `x == node.data` → found
* if `x < node.data` → go left
* else → go right

This gives a directed, at-most-one-child path: time is proportional to the tree **height** `h` (best O(log n) for balanced, worst O(n) for skewed).

**Dry run** (Example 1)

```
         2
          \
          81
         /  \
       42    87
         \     \
         45     90
        /
       66
x = 87
```

1. Start at `2`: `87 > 2` → go right.
2. At `81`: `87 > 81` → go right.
3. At `87`: `87 == 87` → **found** → return `True`.

**Dry run** (Example 2)

```
      6
       \
        8
       / \
      7   9
x = 11
```

1. Start at `6`: `11 > 6` → right to `8`.
2. At `8`: `11 > 8` → right to `9`.
3. At `9`: `11 > 9` → right is `None` → **not found** → return `False`.

---

# 3) Codes (brute + optimized)

### A) Brute force (works on any binary tree, ignores BST property)

* Do an inorder / preorder traversal and check if you ever see `x`.
* Time: **O(n)**, Space: **O(h)** recursion stack (worst O(n)).

```python
'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class BST:
    def search(self, node, x):
        # Brute force: DFS (inorder)
        def dfs(cur):
            if not cur:
                return False
            # check left, current, right
            if dfs(cur.left):
                return True
            if cur.data == x:
                return True
            return dfs(cur.right)

        return dfs(node)
```

### B) Optimized #1 — Iterative BST search (most common in interviews)

* Follow the BST rule to choose one side each step.
* Time: **O(h)**, Space: **O(1)**.

```python
class BST:
    def search(self, node, x):
        # Optimized iterative: O(h) time, O(1) space
        cur = node
        while cur:
            if x == cur.data:
                return True
            elif x < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False
```

### C) Optimized #2 — Recursive BST search (same complexity, cleaner)

* Often used if recursion is allowed.
* Time: **O(h)**, Space: **O(h)** recursion stack.

```python
class BST:
    def search(self, node, x):
        # Optimized recursive: O(h) time, O(h) stack
        if not node:
            return False
        if node.data == x:
            return True
        if x < node.data:
            return self.search(node.left, x)
        else:
            return self.search(node.right, x)
```

**Which to pick in interviews?**
If they stress **O(1) extra space**, go **iterative**. If they emphasize clarity and the input sizes are small, recursion is fine.

---

# 4) Interviewer-style Q\&A

**Q1. What are the time and space complexities?**

* Optimized search: **O(h)** time, where `h` is height.

  * Balanced BST: `h ≈ log₂n` → **O(log n)**
  * Skewed BST: `h ≈ n` → **O(n)**
* Space: Iterative **O(1)**; Recursive **O(h)** call stack.

**Q2. Why is the brute force approach suboptimal for BSTs?**
It ignores the ordering property and explores many nodes unnecessarily, costing **O(n)** instead of **O(h)**.

**Q3. What cases cause worst-case O(n) even with the optimized approach?**
A highly **skewed** BST (like a linked list) where all nodes are on one side.

**Q4. How could we guarantee O(log n) search?**
Use a **balanced BST** (AVL, Red-Black, Treap) or a **B-Tree** style structure. In interviews, you can mention self-balancing trees.

**Q5. How would you handle duplicates?**
Define a policy:

* Either **disallow** duplicates,
* Or store duplicates consistently (e.g., **left** subtree or **right** subtree), and search accordingly.
  Return `True` on the first match.

**Q6. How to make search iterative without while?**
You can simulate recursion with your own stack, but it gives no benefit over the simple loop.

**Q7. Can we short-circuit on ranges?**
Yes; the BST property implicitly prunes half the search space each step (in a balanced tree), which is why it’s efficient.

**Q8. How do you test quickly?**

* Positive cases (value exists as root/leaf/internal).
* Negative cases (smaller than min, greater than max, between nodes).
* Edge: empty tree, tree with one node, skewed trees.

---

### Tiny sanity check

```python
# Build:
#        8
#       / \
#      3  10
#     / \   \
#    1  6    14
#      / \     \
#     4  7      16

root = Node(8)
root.left = Node(3); root.right = Node(10)
root.left.left = Node(1); root.left.right = Node(6)
root.left.right.left = Node(4); root.left.right.right = Node(7)
root.right.right = Node(14); root.right.right.right = Node(16)

bst = BST()
print(bst.search(root, 7))   # True
print(bst.search(root, 2))   # False
```

That’s it—clear logic, two optimized variants, and the brute fallback.

---

---

Here you go—an end-to-end, copy-pasteable program you can run as a script.
It includes: clean BST implementation, iterative search (O(h), O(1) extra space), a tiny builder to create a BST from a list, example inputs, printed outputs, and a quick timing using `timeit`.

---

```python
#!/usr/bin/env python3
"""
Search a node in a BST — full runnable program with timing.

Complexities summary:
- Building BST by inserting n keys (average case balanced-ish):  O(n log n) time
  (Worst case skewed: O(n^2)). Space: O(1) auxiliary (nodes themselves are O(n)).
- Iterative BST search for a value x:                           O(h) time, O(1) space
  where h is the tree height: h ≈ log2(n) for balanced, h ≈ n for skewed.
"""

from dataclasses import dataclass
from typing import Optional, Iterable, List
import timeit


# ------------------------------
# Data structure definitions
# ------------------------------

@dataclass
class Node:
    """BST node."""
    data: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST:
    """Binary Search Tree with iterative search."""

    # Insertion helper to build test trees quickly.
    # Time:  O(h) per insert; Space: O(1) extra.
    def insert(self, root: Optional[Node], key: int) -> Node:
        if root is None:
            return Node(key)
        cur = root
        while True:  # walk down the tree and attach a new leaf
            if key < cur.data:
                if cur.left is None:
                    cur.left = Node(key)
                    break
                cur = cur.left
            else:  # duplicates go to the right by convention
                if cur.right is None:
                    cur.right = Node(key)
                    break
                cur = cur.right
        return root

    # Optimized iterative search using BST property.
    # Time:  O(h)     (best O(log n) if balanced, worst O(n) if skewed)
    # Space: O(1) extra (no recursion).
    def search(self, node: Optional[Node], x: int) -> bool:
        cur = node
        while cur is not None:
            if x == cur.data:
                return True
            elif x < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False


# ------------------------------
# Utility to build BST from an iterable
# ------------------------------

def build_bst(values: Iterable[int]) -> Optional[Node]:
    """Builds a BST by iterative inserts. Returns the root."""
    bst = BST()
    root: Optional[Node] = None
    for v in values:
        root = bst.insert(root, v)
    return root


# ------------------------------
# Demo / main
# ------------------------------

def demo_one_case(values: List[int], queries: List[int]) -> None:
    """
    Build a BST from `values`, run search for each x in `queries`,
    and print 1 if found else 0 (matches the typical GFG style).
    """
    bst = BST()
    root = None
    for v in values:
        root = bst.insert(root, v)

    print("Input values (level-order in example, inserted as given):", values)
    print("Queries:", queries)
    print("Outputs (1 = present, 0 = absent):")
    for x in queries:
        print(1 if bst.search(root, x) else 0, end=" ")
    print("\n")


def main():
    # Example 1 from the prompt image:
    # Tree (values inserted in this order) and query x = 87 → present
    values1 = [2, 81, 42, 87, 45, 90, 66]
    queries1 = [87, 3]
    demo_one_case(values1, queries1)

    # Example 2 from the prompt image:
    # Tree (values inserted in this order) and query x = 11 → absent
    values2 = [6, 8, 7, 9]
    queries2 = [11, 7, 6, 9]
    demo_one_case(values2, queries2)

    # Quick timing: measure the total time to build and query a random-ish tree
    setup_code = """
from __main__ import build_bst, BST
import random
vals = list(range(1, 2000, 3))     # about ~667 nodes
random.shuffle(vals)               # avoid worst-case skew
root = build_bst(vals)
bst = BST()
qs = [1, 500, 1999, 7777, -5, 1234, 1500]
"""
    stmt_code = """
for x in qs:
    bst.search(root, x)
"""
    elapsed = timeit.timeit(stmt=stmt_code, setup=setup_code, number=1000)
    print(f"Time to perform 7 searches × 1000 runs on a ~667-node BST: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
```

### Example run (what you’ll see)

```
Input values (level-order in example, inserted as given): [2, 81, 42, 87, 45, 90, 66]
Queries: [87, 3]
Outputs (1 = present, 0 = absent):
1 0 

Input values (level-order in example, inserted as given): [6, 8, 7, 9]
Queries: [11, 7, 6, 9]
Outputs (1 = present, 0 = absent):
0 1 1 1 

Time to perform 7 searches × 1000 runs on a ~667-node BST: 0.0XXX seconds
```

*(Your timing will vary by machine; it’s just a sanity check that the iterative search is fast.)*

---

## 6) Real-World Use Cases (a few critical ones)

1. **Symbol tables / indices**
   BSTs (especially self-balancing variants like AVL/Red-Black trees) underpin maps/sets in many libraries—fast membership checks (`search`) are fundamental.

2. **Routing / decision trees**
   When keys are ordered (e.g., IP ranges, thresholds), BST-style search is a natural way to route queries or decisions by repeatedly narrowing intervals.

3. **Compilers & interpreters**
   Identifier lookups (scopes), constant folding tables, or any “is this thing defined?” checks can be efficiently handled with ordered maps (BSTs).

4. **Gaming/AI**
   Searching sorted event times, score thresholds, or tuning parameters—BSTs give logarithmic lookups while maintaining dynamic insert/delete.
