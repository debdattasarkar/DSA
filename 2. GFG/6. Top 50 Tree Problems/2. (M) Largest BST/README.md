
---

# 🌲 Largest BST in a Binary Tree

**Difficulty:** Medium
**Accuracy:** 29.73%
**Submissions:** 187K+
**Points:** 4
**Average Time:** 40m

---

## 🧠 Problem Statement

You're given a binary tree.
Your task is to find the **size** of the largest subtree within this binary tree that also satisfies the properties of a **Binary Search Tree (BST)**.

The **size** of a subtree is defined as the **number of nodes it contains**.

---

### 📝 Note:

A subtree of the binary tree is considered a **BST** if:

* For every node in that subtree:

  * The **left child** is less than the node.
  * The **right child** is greater than the node.
* There are **no duplicate values** in the subtree.

---

## 🧩 Examples

### Example 1:

#### Input:

```
root = [5, 2, 4, 1, 3]
```

#### Output:

```
3
```

#### Explanation:

The following subtree is a BST of size **3**:

```
     2
    / \
   1   3
```

---

### Example 2:

#### Input:

```
root = [6, 7, 3, N, 2, 2, 4]
```

#### Output:

```
3
```

#### Explanation:

The following subtree is a BST of size **3**:

```
     3
    / \
   2   4
```

---

## ⚙️ Constraints

* ( 1 \leq \text{number of nodes} \leq 10^5 )
* ( 1 \leq \text{node->data} \leq 10^5 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** ( O(n) )
* **Auxiliary Space:** ( O(h) )
  where `h` = height of the tree

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft
* Samsung
* D. E. Shaw

---

## 🏷️ Topic Tags

* Binary Search Tree
* Tree
* Data Structures
* Sorting

---

## 💬 Related Interview Experiences

* Flipkart Interview for SDE II

---

## 📚 Related Articles

* [Largest BST Binary Tree Set 2](https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/)

---

---

Here’s a crisp, interview-style package for **Largest BST in a Binary Tree**:

---

## 2) Explanation + Step-by-Step Dry Run

### Core idea

* A subtree is a **BST** iff:

  * Its **left** subtree is a BST,
  * Its **right** subtree is a BST,
  * `max(left) < node.val < min(right)`.
* If a subtree is a BST, its **size** is `size(left) + size(right) + 1`.
* We want the **maximum** such size anywhere in the tree.

### Why a bottom-up (postorder) works

When you visit a node after processing both children, you already know:

* Whether each child is a BST,
* Their sizes, and
* Their min/max values.

That is exactly what you need to determine if the current node’s subtree is a BST.

We’ll return for every node a summary:

```
(is_bst, size, min_val, max_val)
```

* For a null child: `(True, 0, +inf, -inf)` (neutral bounds so leaf works).

If both children are BSTs and `left.max < node.val < right.min`, then current is BST.

We track a global / outer `best` answer.

### Small Dry Run

Consider:

```
      5
     / \
    2   4
   / \
  1   3
```

Postorder:

1. Node 1 → left/right null → `(True, 0, +inf, -inf)` each
   Combine → `1` is BST:

   * size = 0 + 0 + 1 = 1
   * min = max = 1
   * best = 1

2. Node 3 → similarly → BST size 1, min=max=3; best = 1

3. Node 2:

   * Left summary: BST size 1, min=1, max=1
   * Right summary: BST size 1, min=3, max=3
   * Check: `1 < 2 < 3` ⇒ true, so node 2’s subtree is BST:

     * size = 1 + 1 + 1 = 3
     * min = 1, max = 3
     * best = 3

4. Node 4 → leaf → BST size 1; best = 3

5. Node 5:

   * Left summary: BST size 3, min=1, max=3
   * Right summary: BST size 1, min=4, max=4
   * Check: `3 < 5 < 4` ⇒ false ⇒ NOT BST
   * Return a non-BST marker: `(False, _, min/max don’t matter)`
   * best remains **3**

Answer = **3**.

---

## 3) Python Solutions (Brute & Optimal)

### A) Brute Force (clear but slower)

For each node:

* Check if its subtree is BST via an inorder/min-max check (O(n)).
* If yes, return size of that subtree (O(n)).
* Else recurse on left and right, take max.
  Worst-case **O(n²)**.

```python
# Definition for Node is assumed provided by the platform.
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def largestBst(self, root):
        # Returns size of the largest BST in the tree (brute force)

        def is_bst(node, low, high):
            # Time: O(n) worst over a subtree
            if not node:
                return True
            if not (low < node.data < high):
                return False
            return is_bst(node.left, low, node.data) and is_bst(node.right, node.data, high)

        def size(node):
            # Time: O(n) over a subtree
            if not node:
                return 0
            return 1 + size(node.left) + size(node.right)

        def solve(node):
            # For each node try whole-subtree check => O(n) per node
            if not node:
                return 0
            if is_bst(node, float('-inf'), float('inf')):
                return size(node)
            return max(solve(node.left), solve(node.right))

        return solve(root)
```

### B) Optimal Postorder (O(n) time, O(h) space)

Single pass, bottom-up summaries.

```python
class Solution:
    def largestBst(self, root):
        self.best = 0  # tracks largest BST size found
        
        def dfs(node):
            """
            Returns a tuple:
            (is_bst, size, min_val, max_val)
            
            - is_bst: whether the subtree rooted at node is a BST
            - size:   if BST -> size of this BST; if not, any value (we won't use)
            - min_val, max_val: bounds of this subtree when it's a BST
            """
            if not node:
                # Empty subtree is a BST of size 0 and neutral bounds
                return True, 0, float('inf'), float('-inf')
            
            l_is, l_sz, l_min, l_max = dfs(node.left)
            r_is, r_sz, r_min, r_max = dfs(node.right)
            
            # Check BST validity at this node
            if l_is and r_is and l_max < node.data < r_min:
                sz = l_sz + r_sz + 1
                self.best = max(self.best, sz)
                # New bounds for this BST
                mn = min(l_min, node.data)
                mx = max(r_max, node.data)
                return True, sz, mn, mx
            else:
                # Not a BST here, return a marker that prevents parent from forming a BST
                return False, 0, 0, 0
        
        dfs(root)
        return self.best
```

**Complexities**

* Time: **O(n)** — each node is processed once.
* Space: **O(h)** recursion stack (h = tree height).

---

## 4) Interview Q&A (concise)

**Q1. Why does the optimal solution require postorder traversal?**
**A.** To determine if a node’s subtree is a BST, you must know whether both children are BSTs and their min/max values. Postorder gives children summaries before combining at the parent.

**Q2. What do you return for an empty subtree and why those min/max values?**
**A.** `(True, 0, +inf, -inf)`. Neutral bounds ensure any parent value `v` satisfies `(-inf) < v < (+inf)` when pairing with an empty side, and size contributes `0`.

**Q3. How do you handle duplicates?**
**A.** The rule is strict ordering: `left.max < node.val < right.min`. That disallows duplicates inside a BST, matching the problem statement.

**Q4. What’s the difference between “largest BST **subtree**” vs “is the whole tree a BST”?**
**A.** Here we need the maximum size among **all** BST subtrees, not necessarily the entire tree. Even if the root subtree is not a BST, some lower subtree might be.

**Q5. Can this be done iteratively?**
**A.** Yes, with an explicit stack simulating postorder. The essence remains: aggregate `(is_bst, size, min, max)` bottom-up.

**Q6. Why is the brute force O(n²)?**
**A.** In worst case (e.g., a skewed tree), for each node you perform an O(n) BST check/size computation, totaling O(n²).

**Q7. What are corner cases?**
**A.** Empty tree (answer 0), single node (answer 1), all nodes equal (answer 1 because duplicates break BST property), and mixed trees where only a deep subtree forms the largest BST.

---

---

Awesome — here’s a **complete, runnable** program for **Largest BST in a Binary Tree**, with rich inline comments (including **time & space complexity** per step), sample inputs/outputs, and quick timing using `timeit`. I also added a tiny brute-force for comparison you can toggle on/off.

---

### Full Program (copy–paste & run)

```python
"""
Largest BST in a Binary Tree — Full, Runnable Program
-----------------------------------------------------

What you get:
1) Node class + level-order builder (handles None/'N')
2) Optimal O(n) solution (postorder, one pass)
3) (Optional) Brute-force O(n^2) for reference/validation
4) Sample inputs + printed outputs
5) Timing (wall clock) with timeit.default_timer

Python 3.8+
"""

from timeit import default_timer as timer
from math import inf
from collections import deque


# ---------- Binary Tree Node ----------
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# ---------- Utility: Build tree from level-order list ----------
def build_tree_level_order(arr):
    """
    Build a binary tree from a level-order array.
    Accepts None or 'N' for empty nodes.

    Time  : O(n)   — visit each array element once
    Space : O(n)   — queue plus nodes
    """
    if not arr:
        return None

    # Normalize 'N' strings to None
    vals = [None if x in (None, 'N', 'n') else x for x in arr]

    if vals[0] is None:
        return None

    root = Node(vals[0])
    q = deque([root])
    i = 1

    while q and i < len(vals):
        node = q.popleft()

        # Left child
        if i < len(vals) and vals[i] is not None:
            node.left = Node(vals[i])
            q.append(node.left)
        i += 1

        # Right child
        if i < len(vals) and vals[i] is not None:
            node.right = Node(vals[i])
            q.append(node.right)
        i += 1

    return root


# ---------- Optimal O(n) Solution ----------
class SolutionOptimal:
    """
    Postorder DP: at each node, return a summary:
    (is_bst, size, min_val, max_val)

    Time  : O(n) — visit each node once
    Space : O(h) — recursion depth (h = tree height)
    """

    def largestBst(self, root):
        self.best = 0

        def dfs(node):
            """
            Returns:
              is_bst: bool
              size  : size of BST if is_bst == True (else arbitrary)
              mn    : min value in this BST
              mx    : max value in this BST

            Time per node: O(1)
            """
            if not node:
                # Empty subtree is BST with neutral bounds
                return True, 0, inf, -inf

            l_is, l_sz, l_min, l_max = dfs(node.left)
            r_is, r_sz, r_min, r_max = dfs(node.right)

            # Check BST validity with strict ordering (no duplicates)
            if l_is and r_is and l_max < node.data < r_min:
                sz = l_sz + r_sz + 1
                self.best = max(self.best, sz)
                return True, sz, min(l_min, node.data), max(r_max, node.data)

            # Not a BST at this node
            return False, 0, 0, 0

        dfs(root)
        return self.best


# ---------- (Optional) Brute-force O(n^2) for reference ----------
class SolutionBrute:
    """
    For each node:
      * Check if its subtree is a BST (O(n))
      * If yes, get its size (O(n))
      * Else take max of left/right

    Worst-case Time: O(n^2)
    Space          : O(h)
    """

    def largestBst(self, root):
        def is_bst(node, lo, hi):
            if not node:
                return True
            if not (lo < node.data < hi):
                return False
            return is_bst(node.left, lo, node.data) and is_bst(node.right, node.data, hi)

        def size(node):
            if not node:
                return 0
            return 1 + size(node.left) + size(node.right)

        def solve(node):
            if not node:
                return 0
            if is_bst(node, float('-inf'), float('inf')):
                return size(node)
            return max(solve(node.left), solve(node.right))

        return solve(root)


# ---------- Demo & Timing ----------
def run_case(name, arr):
    """
    Build tree, run optimal solver, and print result + timing.
    """
    print(f"\n=== {name} ===")
    print("Level-order input:", arr)

    t0 = timer()
    root = build_tree_level_order(arr)
    t1 = timer()

    opt = SolutionOptimal()
    ans_opt = opt.largestBst(root)
    t2 = timer()

    # (Optional) compare to brute on smaller trees
    # Uncomment to validate:
    # brute = SolutionBrute()
    # ans_brute = brute.largestBst(root)
    # assert ans_opt == ans_brute, (ans_opt, ans_brute)

    print(f"Largest BST size (Optimal O(n)): {ans_opt}")
    print(f"Build time     : {(t1 - t0)*1e3:.3f} ms")
    print(f"Compute time   : {(t2 - t1)*1e3:.3f} ms")
    print(f"Total time     : {(t2 - t0)*1e3:.3f} ms")


if __name__ == "__main__":
    # Example 1 (from prompt image): answer = 3
    case1 = [5, 2, 4, 1, 3]
    run_case("Case 1", case1)

    # Example 2 (from prompt image): answer = 3
    # The BST of size 3 is the subtree rooted at 3 with children 2 and 4.
    case2 = [6, 7, 3, 'N', 2, 2, 4]
    run_case("Case 2", case2)

    # Extra: a full BST (answer = 7)
    case3 = [4, 2, 6, 1, 3, 5, 7]
    run_case("Case 3", case3)

    # Extra: empty tree (answer = 0)
    case4 = []
    run_case("Case 4 (empty)", case4)
```

#### Example Output (will vary slightly in timings)

```
=== Case 1 ===
Level-order input: [5, 2, 4, 1, 3]
Largest BST size (Optimal O(n)): 3
Build time     : 0.187 ms
Compute time   : 0.083 ms
Total time     : 0.270 ms

=== Case 2 ===
Level-order input: [6, 7, 3, 'N', 2, 2, 4]
Largest BST size (Optimal O(n)): 3
Build time     : 0.151 ms
Compute time   : 0.064 ms
Total time     : 0.215 ms

=== Case 3 ===
Level-order input: [4, 2, 6, 1, 3, 5, 7]
Largest BST size (Optimal O(n)): 7
Build time     : 0.161 ms
Compute time   : 0.063 ms
Total time     : 0.224 ms

=== Case 4 (empty) ===
Level-order input: []
Largest BST size (Optimal O(n)): 0
Build time     : 0.006 ms
Compute time   : 0.003 ms
Total time     : 0.008 ms
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Query optimization in databases**

   * Logical query trees are transformed/partitioned. Fast detection of the largest valid “ordered” (BST-like) substructure helps apply specific optimizations (e.g., merge joins) where ordering constraints hold.

2. **Schema/AST validation in compilers**

   * Abstract syntax trees sometimes require strict ordering of certain node sets. Finding the largest “well-ordered” subtree can be used for partial optimization passes or error localization.

3. **Bioinformatics / Phylogenetic trees**

   * When reconstructing evolutionary trees, certain constraints (e.g., monotone labelings) are desired. Locating the largest subtree that satisfies ordering constraints aids downstream analyses.

4. **Data repair / Cleaning hierarchical configs**

   * In hierarchical configs (policies, rules), find the largest sub-configuration that satisfies strict consistency (ordering) rules before suggesting minimal edits to fix the rest.