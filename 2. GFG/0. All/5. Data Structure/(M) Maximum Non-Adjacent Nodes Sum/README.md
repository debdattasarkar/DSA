
# Maximum Non-Adjacent Nodes Sum

**Difficulty:** Medium
**Accuracy:** 55.35%
**Submissions:** 96K+
**Points:** 4
**Average Time:** 45m

---

## 🧩 Problem Statement

Given the **root** of a binary tree with integer values, your task is to select a **subset of nodes** such that the sum of their values is **maximized**,
with the condition that **no two selected nodes are directly connected**.

That is, if a node is included in the subset, neither its **parent** nor its **children** can be included.

---

## 🧠 Examples

### Example 1

**Input:**

```
root = [11, 1, 2]
```

**Output:**

```
11
```

**Explanation:**
The maximum sum is obtained by selecting only node `11`.

Tree:

```
     11
    /  \
   1    2
```

Choosing only 11 gives us the maximum sum (11).

---

### Example 2

**Input:**

```
root = [1, 2, 3, 4, N, 5, 6]
```

**Output:**

```
16
```

**Explanation:**
The maximum sum is obtained by selecting nodes 1, 4, 5, and 6 which are not directly connected.

Their total sum = 1 + 4 + 5 + 6 = **16**

Tree:

```
        1
       / \
      2   3
     /   / \
    4   5   6
```

---

## 📋 Constraints

* `1 ≤ number of nodes ≤ 10⁴`
* `1 ≤ node.data ≤ 10⁵`

---

## ⏱️ Expected Complexities

| Metric              | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n)       |
| **Auxiliary Space** | O(n)       |

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Google

---

## 🧱 Topic Tags

* Tree
* Data Structures

---

## 📚 Related Interview Experiences

* Flipkart Interview Experience for SDE 1 On Campus 2019 Set 2

---

## 📘 Related Articles

* Maximum Sum Nodes in Binary Tree with No Two Adjacent

---

---

awesome — let’s make **Maximum Non-Adjacent Nodes Sum (aka “House Robber on Trees”)** interview-ready.

---

## 2) Intuition + step-by-step dry run

### Core idea (tree DP)

For every node, compute **two values**:

* `take[node]` = best sum **if we include** this node
  ⇒ we **cannot** include its children
  ⇒ `take = node.val + skip[left] + skip[right]`

* `skip[node]` = best sum **if we exclude** this node
  ⇒ children are free to be taken or skipped independently
  ⇒ `skip = max(take[left], skip[left]) + max(take[right], skip[right])`

Answer at the root: `max(take[root], skip[root])`.
We compute these in **postorder** (children first), so each node is processed once: **O(n)** time, **O(h)** recursion stack.

---

### Dry run on Example 2

Tree (level-order: `[1, 2, 3, 4, N, 5, 6]`):

```
        1
       / \
      2   3
     /   / \
    4   5   6
```

Postorder calculations:

* Leaf 4:
  `take=4`, `skip=0`
* Node 2 (left=4, right=None):
  `take=2 + skip[4] + 0 = 2`
  `skip=max(4,0) + 0 = 4`
* Leaf 5:
  `take=5`, `skip=0`
* Leaf 6:
  `take=6`, `skip=0`
* Node 3 (left=5, right=6):
  `take=3 + 0 + 0 = 3`
  `skip=max(5,0) + max(6,0) = 11`
* Root 1 (left=2, right=3):
  `take=1 + skip[2] + skip[3] = 1 + 4 + 11 = 16`
  `skip=max(2,4) + max(3,11) = 4 + 11 = 15`

Answer = `max(16, 15) = 16` ✅ (nodes 1,4,5,6).

---

## 3) Python solutions (brute + optimized styles)

All versions use the given signature.

### A) Optimized Postorder DP (most expected)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        """
        For each node, return (take, skip):
          take = node.data + skip_left + skip_right
          skip = max(take_left, skip_left) + max(take_right, skip_right)

        Time  : O(n)   each node processed once
        Space : O(h)   recursion stack (h = tree height)
        """
        def dfs(node):
            if not node:
                # (take, skip) for empty subtree
                return (0, 0)

            take_l, skip_l = dfs(node.left)   # postorder
            take_r, skip_r = dfs(node.right)

            take_here = node.data + skip_l + skip_r
            skip_here = max(take_l, skip_l) + max(take_r, skip_r)
            return (take_here, skip_here)

        take_root, skip_root = dfs(root)
        return max(take_root, skip_root)
```

### B) Brute force (exponential / overlapping work) — good to mention, not to use

Choose node or not; if you choose it, you can only go to **grandchildren**.

```python
class SolutionBrute:
    def getMaxSum(self, root):
        """
        Exponential due to recomputation (worst O(2^n)).
        Shows the idea behind include vs exclude, but inefficient.
        """
        if not root:
            return 0

        # Include root: sum of grandchildren + root.data
        include_sum = root.data
        if root.left:
            include_sum += self.getMaxSum(root.left.left)
            include_sum += self.getMaxSum(root.left.right)
        if root.right:
            include_sum += self.getMaxSum(root.right.left)
            include_sum += self.getMaxSum(root.right.right)

        # Exclude root: free to choose best from children
        exclude_sum = self.getMaxSum(root.left) + self.getMaxSum(root.right)

        return max(include_sum, exclude_sum)
```

### C) Memoized include/exclude (top-down with caching) — easy upgrade of brute to O(n)

```python
class SolutionMemo:
    def getMaxSum(self, root):
        """
        Memoize the brute logic on nodes to avoid recomputation.
        Time  : O(n)
        Space : O(h) recursion + O(n) memo
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def best(node):
            if node is None:
                return 0

            # Python can't hash custom objects by default in lru_cache unless
            # we pass an id; we’ll wrap by using the object id.
            return best_by_id(id(node))

        # Map id(node) -> node reference
        node_map = {}
        def index_nodes(node):
            if not node: return
            node_map[id(node)] = node
            index_nodes(node.left)
            index_nodes(node.right)
        index_nodes(root)

        from functools import lru_cache
        @lru_cache(maxsize=None)
        def best_by_id(node_id):
            if node_id == 0:
                return 0
            node = node_map[node_id]

            include_sum = node.data
            if node.left:
                include_sum += best_by_id(id(node.left.left) if node.left.left else 0)
                include_sum += best_by_id(id(node.left.right) if node.left.right else 0)
            if node.right:
                include_sum += best_by_id(id(node.right.left) if node.right.left else 0)
                include_sum += best_by_id(id(node.right.right) if node.right.right else 0)

            exclude_sum = best_by_id(id(node.left) if node.left else 0) + \
                          best_by_id(id(node.right) if node.right else 0)
            return max(include_sum, exclude_sum)

        return best(root)
```

### D) Iterative Postorder (stack) returning (take, skip) table

```python
class SolutionIterative:
    def getMaxSum(self, root):
        """
        Iterative postorder using one stack and a visited flag.
        Time  : O(n)
        Space : O(n) for stack + table
        """
        if not root:
            return 0

        stack = [(root, False)]
        dp = {}  # node -> (take, skip)

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                # Postorder: push node again marked visited, then children
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                take_l, skip_l = dp.get(node.left, (0, 0))
                take_r, skip_r = dp.get(node.right, (0, 0))
                take_here = node.data + skip_l + skip_r
                skip_here = max(take_l, skip_l) + max(take_r, skip_r)
                dp[node] = (take_here, skip_here)

        take_root, skip_root = dp[root]
        return max(take_root, skip_root)
```

> In most interviews, implement **A (postorder DP)**. If they push for variants, mention **D (iterative)**; if they ask about naive/optimization path, mention **B → C**.

---

## 4) How to remember quickly + likely interviewer Q&A

### 10-second memory hook

> **“House Robber on trees: for each node compute (take, skip).
> take = val + skip(L) + skip(R); skip = max(take,skip)(L) + max(take,skip)(R).
> Answer = max at root.”**

If you blank out, say out loud:

* “If I take a node, I can’t take its children.”
* “If I skip a node, I pick the best from each child.”
  Then write those two equations — you’re back on track.

### Common interviewer questions (and crisp answers)

**Q1. Why postorder?**
We need children’s `(take, skip)` to compute parent’s — that’s postorder.

**Q2. Time/space complexity?**
`O(n)` time (each node once), `O(h)` space (recursion stack).

**Q3. What if values could be zero or negative?**
Formulas still work. If a subtree is bad, `skip` will dominate. (If negatives exist widely, you might clamp with `max(0, …)` variants depending on specification; here values are positive per constraints.)

**Q4. Relation to known problems?**
Exactly **House Robber III** on LeetCode; classic tree DP with two states per node.

**Q5. Can you write it iteratively?**
Yes — simulate postorder with a stack and compute `(take, skip)` bottom-up (see Solution D).

**Q6. Prove correctness briefly.**
Induction on subtree size: optimal solution at a node is either (1) take node, force skip on children, or (2) skip node, independently choose best on each child — which is precisely what the recurrence encodes.

**Q7. Memory optimization?**
We already use O(1) per frame; no extra hash maps needed in solution A.

**Q8. How to test quickly?**

* Single node
* Chain/Skewed tree
* Perfect binary tree
* Mixed values to ensure skip/take swap dominance

---

---

awesome — let’s wrap “**Maximum Non-Adjacent Nodes Sum (House Robber on Trees)**” with practical context + a complete runnable program that includes timing.

---

## 5) Real-World Use Cases (interviewer-friendly, easy to relate)

* **Endpoint hardening in org charts**
  Choose which managers or ICs to receive a limited “security training budget” so that **no manager and direct report both receive it** (avoid redundancy/overlap) while maximizing overall risk reduction score (node value).

* **IoT / sensor maintenance**
  Schedule battery replacement for sensors arranged in a tree (hub → sub-hubs → leaves) such that **no parent and child are serviced in the same window** (operational constraints), maximizing total “health gain”.

* **Ad / notification throttling in hierarchies**
  In a content tree (category → subcategory → item), pick nodes to display a promo where **direct parent–child duplicates are disallowed**, maximizing engagement value.

* **Data aggregation / cache pinning**
  Pin either a directory or its files in a storage tree (but not both) to maximize total “hotness” score while respecting **no parent–child pin** policy.

Use these as analogies: *“We’re selecting a set of nodes with no immediate adjacency to maximize value.”*

---

## 6) Full Python Program (with inline time/space notes + timing)

```python
#!/usr/bin/env python3
"""
Maximum Non-Adjacent Nodes Sum (House Robber on Trees)

Goal:
  Pick a subset of tree nodes (no parent-child pairs together) that maximizes
  the sum of values.

Approach (interview standard):
  For each node, compute two DP states in postorder:
    take = node.val + skip(left) + skip(right)
    skip = max(take,skip)(left) + max(take,skip)(right)
  Answer = max(take(root), skip(root))

Complexities:
  Time  : O(n)  -- each node processed exactly once
  Space : O(h)  -- recursion stack height (worst O(n) if skewed)
"""

from collections import deque
from time import perf_counter
import timeit
import sys


# ----------------------------- Node definition -----------------------------
class Node:
    def __init__(self, val):
        # O(1) construct
        self.data = val
        self.left = None
        self.right = None


# ------------------------- Build tree from level-order ----------------------
def build_tree(tokens):
    """
    Build a binary tree from level-order tokens (space-separated).
    'N' denotes a null child.

    Complexity:
      Time  : O(n)  -- process each token once
      Space : O(n)  -- queue + allocated nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root_val = next(it)
    root = Node(int(root_val))              # O(1)
    q = deque([root])                       # O(1)

    # Level-order expansion -> O(n)
    for left_tok in it:
        parent = q.popleft()                # amortized O(1)

        if left_tok != 'N':                 # left child
            left = Node(int(left_tok))      # O(1)
            parent.left = left
            q.append(left)                  # O(1)

        try:
            right_tok = next(it)            # may raise StopIteration
        except StopIteration:
            break

        if right_tok != 'N':                # right child
            right = Node(int(right_tok))    # O(1)
            parent.right = right
            q.append(right)                 # O(1)

    return root


# --------------------------- DP solution (O(n)) ----------------------------
class Solution:
    def getMaxSum(self, root):
        """
        Postorder DP returning (take, skip) for each subtree.

        Time  : O(n)   (each node visited exactly once)
        Space : O(h)   recursion stack (h = tree height)
        """
        def dfs(node):
            if not node:
                # Empty subtree contributes 0 to both states. O(1)
                return (0, 0)

            # Postorder: compute children's states first
            take_l, skip_l = dfs(node.left)     # O(size(left))
            take_r, skip_r = dfs(node.right)    # O(size(right))

            # If we take this node, we must skip both children
            take_here = node.data + skip_l + skip_r     # O(1)

            # If we skip this node, each child independently chooses best
            skip_here = max(take_l, skip_l) + max(take_r, skip_r)  # O(1)

            return (take_here, skip_here)

        take_root, skip_root = dfs(root)        # O(n)
        return max(take_root, skip_root)        # O(1)


# ------------------------------- Timing utils ------------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter. Overhead ~O(1)."""
    t0 = perf_counter()
    out = func(*args, **kwargs)
    t1 = perf_counter()
    return out, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime across `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# ------------------------------------ Main ---------------------------------
def main():
    # INPUT: one line, level-order, 'N' for nulls
    # Example: 1 2 3 4 N 5 6
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("No input provided.\nExample:\n  1 2 3 4 N 5 6")
        return

    # Build tree: O(n)
    root = build_tree(tokens)

    solver = Solution()

    # Single-run time: O(n)
    ans, t_single = time_single_run(solver.getMaxSum, root)

    # timeit average: run fresh solver each time
    avg = time_with_timeit(lambda: Solution().getMaxSum(root), number=5)

    print("Maximum Non-Adjacent Nodes Sum:", ans)
    print(f"Single-run time : {t_single:.6f} s")
    print(f"Avg over 5 runs : {avg:.6f} s")

    print("\nComplexity:")
    print("  Time  : O(n)")
    print("  Space : O(h) recursion (worst O(n) if skewed)")


if __name__ == "__main__":
    """
    Example:
      echo "1 2 3 4 N 5 6" | python3 max_non_adjacent_tree.py

    Tree:
            1
           / \
          2   3
         /   / \
        4   5   6

    Expected Output:
      Maximum Non-Adjacent Nodes Sum: 16
      Single-run time : 0.000xxx s
      Avg over 5 runs : 0.000xxx s
    """
    main()
```

### How to run (example)

```bash
echo "1 2 3 4 N 5 6" | python3 max_non_adjacent_tree.py
```

**Output (timings vary):**

```
Maximum Non-Adjacent Nodes Sum: 16
Single-run time : 0.000012 s
Avg over 5 runs : 0.000011 s

Complexity:
  Time  : O(n)
  Space : O(h) recursion (worst O(n) if skewed)
```

---

**Interview tip recap (10s):**
“**House Robber on Trees**: at each node compute `(take, skip)`.
`take = val + skip(L)+skip(R)`, `skip = max(take,skip)(L) + max(take,skip)(R)`.
Answer is `max` at root. Postorder, O(n).”
