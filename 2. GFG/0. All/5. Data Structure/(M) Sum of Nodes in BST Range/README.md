# Sum of Nodes in BST Range

**Difficulty:** Medium
**Accuracy:** 88.11%
**Submissions:** 4K+
**Points:** 4

---

## Problem Statement

Given the **root** of a **Binary Search Tree** and two integers **l** and **r**, find the **sum of all nodes** that lie between **l** and **r**, **inclusive**.

---

## Examples

### Example 1

**Input:**
`root = [22, 12, 30, 8, 20]`, `l = 10`, `r = 22`

```
        22
       /  \
     12    30
    /  \
   8   20
```

**Output:**
`54`

**Explanation:**
Nodes in range `[10, 22]` are `{12, 20, 22}`.
Sum = `12 + 20 + 22 = 54`.

---

### Example 2

**Input:**
`root = [8, 5, 11, 3, 6, N, 20]`, `l = 11`, `r = 15`

```
        8
       / \
      5   11
     / \    \
    3   6    20
```

**Output:**
`11`

**Explanation:**
Nodes in range `[11, 15]` are `{11}`.
Sum = `11`.

---

## Constraints

* `0 ≤ number of nodes ≤ 10^4`
* `0 ≤ node->data ≤ 10^4`
* `0 ≤ l ≤ r ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(h)` (height of the BST)

---

## Topic Tags

* Binary Search Tree
* Data Structures
* Algorithms

---

## Related Articles

* [*Sum Of Nodes In A Binary Search Tree With Values From A Given Range*](https://www.geeksforgeeks.org/sum-of-nodes-in-a-binary-search-tree-with-values-from-a-given-range/)

---

---

awesome — let’s make **“Sum of Nodes in a BST within range [l, r]”** interview-ready.

---

## 2) Concept + step-by-step dry run

### What’s the trick?

Use the **BST property**:

* Left subtree values `< node.data`
* Right subtree values `> node.data`

So at any node `x`:

* If `x.data < l`: everything on the **left** is `< l` → **skip left**, go **right** only.
* If `x.data > r`: everything on the **right** is `> r` → **skip right**, go **left** only.
* Else (`l ≤ x.data ≤ r`): **include x.data** and explore **both** sides.

This **prunes** whole subtrees and gives near-optimal work.

### Dry run (Example 1)

BST:

```
        22
       /  \
     12    30
    /  \
   8   20
```

Range `[l, r] = [10, 22]`.

Walk (recursive with pruning):

1. Node 22: in range → sum += 22; explore left (≤22) and right (≥22)
2. Left (12): in range → sum += 12; explore both
3. Left of 12 (8): 8 < l → prune left, go right (None) → contributes 0
4. Right of 12 (20): in range → sum += 20; leaf → done
5. Right of 22 (30): 30 > r → prune right, go left (None) → contributes 0

Total = **22 + 12 + 20 = 54** ✅

---

## 3) Python solutions (brute + optimized), with interview-style comments

You can use any of these inside the provided signature.

### A) Optimized recursive DFS with pruning (most expected)

```python
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        """
        BST-aware recursion with pruning.
        If node.val < l  -> skip left
        If node.val > r  -> skip right
        Else include node and visit both sides.

        Time  : O(m)  where m is number of visited nodes (≤ n; often much less due to pruning)
        Space : O(h)  recursion stack, h = tree height (worst O(n), avg O(log n) if balanced)
        """
        def dfs(node):
            if not node:
                return 0

            if node.data < l:
                # Entire left subtree < l -> ignore
                return dfs(node.right)
            if node.data > r:
                # Entire right subtree > r -> ignore
                return dfs(node.left)

            # In range: include node and search both sides
            return node.data + dfs(node.left) + dfs(node.right)

        return dfs(root)
```

### B) Iterative using a stack (same pruning, avoids recursion)

```python
class SolutionIterative:
    def nodeSum(self, root, l, r):
        """
        Iterative DFS with explicit stack and BST pruning.
        Time  : O(m)
        Space : O(h) for stack
        """
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            if node.data < l:
                # skip left, go right
                stack.append(node.right)
            elif node.data > r:
                # skip right, go left
                stack.append(node.left)
            else:
                # in range
                total += node.data
                # both children may contain in-range values
                stack.append(node.left)
                stack.append(node.right)
        return total
```

### C) Brute force (traverse all nodes; ignore BST property)

```python
class SolutionBrute:
    def nodeSum(self, root, l, r):
        """
        Full traversal without pruning.
        Time  : O(n)
        Space : O(h)
        """
        if not root:
            return 0
        here = root.data if l <= root.data <= r else 0
        return here + self.nodeSum(root.left, l, r) + self.nodeSum(root.right, l, r)
```

### D) Inorder traversal with pruning (yields sorted order; easy to reason about)

```python
class SolutionInorder:
    def nodeSum(self, root, l, r):
        """
        Inorder (sorted) with pruning:
          - Stop going left if node.data < l and skip the whole left subtree
          - Stop going right if node.data > r and skip the whole right subtree

        Time  : O(m)
        Space : O(h)
        """
        total, stack, node = 0, [], root
        while stack or node:
            # Go left while values could still be ≥ l
            while node:
                # If node.data < l, its left is also < l; jump right directly
                if node.data < l:
                    node = node.right
                else:
                    stack.append(node)
                    node = node.left

            node = stack.pop()
            if l <= node.data <= r:
                total += node.data
            # If node.data > r, all nodes to its right are even larger; prune
            if node.data > r:
                node = None  # force unwind more
            else:
                node = node.right
        return total
```

> In interviews, implement **A (recursive pruning)** first; mention **B** if asked to avoid recursion, and cite **C** as the naive baseline.

---

### Why pruning is correct

Because of BST ordering:

* If `node.data < l`, every value in `node.left` is **even smaller** → can’t be in `[l, r]`.
* If `node.data > r`, every value in `node.right` is **even larger** → can’t be in `[l, r]`.

Thus entire subtrees can be skipped safely.

---

### Edge cases to call out (interview tips)

* Empty tree → `0`
* `l == r` (single value)
* All nodes < l or > r → result `0`
* Highly skewed BST → recursion depth may hit O(n); consider iterative version.

---

---

awesome — here’s a crisp “interview pack” for **Sum of Nodes in a BST in range [l, r]**.

---

## 4) How to remember it quickly (60-second recall)

### Visual mnemonic: **“Gatekeeper BST”**

* Picture the current node as a **gatekeeper** standing between two doors:

  * **Left door:** all values **smaller** than the gatekeeper.
  * **Right door:** all values **greater** than the gatekeeper.
* Range check:

  * **Too small** (`node < l`) → everything on the **left** is even smaller → **ignore left**, go **right**.
  * **Too large** (`node > r`) → everything on the **right** is even larger → **ignore right**, go **left**.
  * **In range** (`l ≤ node ≤ r`) → **add node**, visit **both doors**.

### 3-line pseudo (what you say while writing code)

```
if node is None: return 0
if node.val < l: return dfs(node.right)
if node.val > r: return dfs(node.left)
return node.val + dfs(node.left) + dfs(node.right)
```

### One-liner mantra

> “**Compare, prune one side, or add and take both.**”

### Complexity cue

> Time = **O(m)** (only the visited/pruned nodes), Space = **O(h)** (recursion stack).

---

## Expected Interview Q&A

### Understanding & Correctness

**Q1. Why can we prune entire subtrees?**
Because it’s a **BST**: if `node.val < l`, then **every** value in `node.left` is `< node.val < l` → can never be in `[l, r]`. Similarly for `node.val > r` and `node.right`.

**Q2. What’s the difference between this and a normal DFS sum?**
Normal DFS is **O(n)**. Using BST pruning, we visit only relevant parts → **O(m)** where `m ≤ n`, often much smaller.

**Q3. Is the sum inclusive?**
Yes, the problem states **inclusive**: add when `l ≤ node.val ≤ r`.

**Q4. What if the tree is not a BST?**
Pruning is invalid. You must traverse all nodes → **O(n)**. (State this explicitly if interviewer tries to “trap” you.)

**Q5. What if `l > r`?**
Swap them or return 0 by convention. Easiest: `if l > r: l, r = r, l`.

**Q6. Duplicates in BST?**
If duplicates are allowed, the logic still works; just be consistent about where equal keys live (typically left or right). Since range is inclusive, equal values are counted.

### Complexity & Variants

**Q7. Time/Space complexity?**

* **Time:** `O(m)` where `m` = number of visited nodes (worst `O(n)`, best ~`O(h + k)` if only k matches).
* **Space:** `O(h)` recursion stack (worst `O(n)` skewed, average `O(log n)` balanced).

**Q8. Can you do it iteratively?**
Yes — use a stack for DFS (same pruning), or do **inorder** with pruning. Both keep **O(h)** space.

**Q9. Can you do it with O(1) extra space?**
Use **Morris inorder traversal with pruning**. It’s trickier to implement but reduces auxiliary space to `O(1)` (modifies pointers temporarily).

**Q10. What about very large sums / overflow?**
In Python you’re fine (big ints). In fixed-width languages use 64-bit integers (`long long` in C++/Java) and discuss overflow risk.

### Edge Cases & Testing

**Q11. Edge cases you’d test?**

* Empty tree → 0
* All nodes `< l` or `> r` → 0
* `l == r` (single key)
* Skewed tree (stack depth)
* l/r beyond the min/max keys
* Tree with duplicates at the boundaries (e.g., many `l` or `r` values)

**Q12. How do you quickly justify the pruning to an interviewer?**
One sentence: *“Because it’s a BST: if the gatekeeper is below `l`, the entire left side is below `l`; if above `r`, entire right side is above `r` — so we skip them entirely.”*

### Follow-ups (common)

**Q13. Return also the count of nodes in the range?**
Track a second accumulator: when in range, `count += 1`; return both or store externally.

**Q14. Find **k** smallest values and sum them?**
Inorder traversal with an early stop after collecting k nodes; or maintain a max-heap of size k while traversing.

**Q15. If it were a general binary tree, how would you optimize?**
You can’t prune by order; you may prune by **value bounds** only if the tree stores min/max subtree bounds (augmented tree), otherwise it’s full traversal.

---

### Final “write-it-now” template (what you code under pressure)

```python
def nodeSum(self, root, l, r):
    def dfs(node):
        if not node: return 0
        if node.data < l:  # too small: skip left
            return dfs(node.right)
        if node.data > r:  # too large: skip right
            return dfs(node.left)
        # in range
        return node.data + dfs(node.left) + dfs(node.right)
    if l > r: l, r = r, l  # optional safety
    return dfs(root)
```

Say out loud as you code: **“compare → prune one side → else add + both.”** That’s the whole pattern.

---

---

Absolutely—let’s wrap this up with concise, interview-friendly **real-world use cases** and a **complete runnable program** (with timing + inline complexity notes).

---

## 5) Real-World Use Cases (memorable + relatable)

* **Org-chart incentives (No Manager–Direct Report together)**
  Pick employees to reward so total impact (value) is maximized, but you can’t award both a manager and their direct report.

* **Network hardening (No Adjacent Servers)**
  Enable expensive security agents only on a subset of machines in a datacenter tree such that no parent–child pair both run it (to avoid resource contention), maximizing total risk reduction.

* **Sensor placement with interference**
  Choose sensors to activate in a tree-shaped field network where adjacent sensors interfere; maximize total coverage score.

* **API throttling tokens in service trees**
  Allocate “burst tokens” to a subset of services where adjacent (parent/child) services cannot both receive tokens, maximizing total throughput.

> Memory hook you can say aloud: **“This is ‘House Robber’ on a tree—pick nodes so no parent–child both picked.”**

---

## 6) Full Program (read input, solve, print result, and time it)

* **Input format (level order, `N` for nulls)**
  Example:
  `1 2 3 4 N 5 6`

* **Output**
  Maximum non-adjacent sum and timing stats.

```python
#!/usr/bin/env python3
"""
Maximum Non-Adjacent Nodes Sum in a Binary Tree
-----------------------------------------------
Pick a subset of nodes (no parent-child both chosen) to maximize the sum.

Approach (Interview-standard Tree DP, Postorder):
  For each node, compute a pair (take, skip):
    take = node.value + skip(left) + skip(right)
    skip = max(take, skip)(left) + max(take, skip)(right)

Answer: max(take(root), skip(root))

Complexities:
  Time  : O(n)  -- each node processed exactly once
  Space : O(h)  -- recursion stack; h = tree height (worst O(n) if skewed)
"""

from collections import deque
from time import perf_counter
import timeit
import sys

# ----------------------------- Node definition -----------------------------
class Node:
    def __init__(self, val: int):
        # O(1) time / O(1) space
        self.data = val
        self.left = None
        self.right = None

# ------------------------- Build tree from level-order ----------------------
def build_tree(tokens):
    """
    Build a binary tree from space-separated level-order tokens.
    'N' denotes a null/missing child.

    Complexity:
      Time  : O(n)  -- each token consumed once
      Space : O(n)  -- queue + created nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root = Node(int(next(it)))    # O(1)
    q = deque([root])             # O(1)

    # Level-order expansion -> overall O(n)
    for left_tok in it:
        parent = q.popleft()      # amortized O(1)

        if left_tok != 'N':       # left child
            lc = Node(int(left_tok))
            parent.left = lc
            q.append(lc)

        try:
            right_tok = next(it)  # right child (guard StopIteration)
        except StopIteration:
            break
        if right_tok != 'N':
            rc = Node(int(right_tok))
            parent.right = rc
            q.append(rc)

    return root

# ---------------------------- Optimized DP solution -------------------------
class Solution:
    def getMaxSum(self, root):
        """
        Returns the maximum sum with no adjacent (parent-child) nodes both chosen.

        For each node, postorder returns a tuple (take, skip):
          take = node.data + skip_left + skip_right
          skip = max(take_left, skip_left) + max(take_right, skip_right)

        Complexity:
          Time  : O(n)
          Space : O(h) recursion stack
        """
        def dfs(node):
            if not node:                 # O(1)
                return (0, 0)
            take_l, skip_l = dfs(node.left)   # O(size(left))
            take_r, skip_r = dfs(node.right)  # O(size(right))

            take_here = node.data + skip_l + skip_r
            skip_here = max(take_l, skip_l) + max(take_r, skip_r)
            return (take_here, skip_here)

        take_root, skip_root = dfs(root)      # O(n)
        return max(take_root, skip_root)

# ------------------------------- Timing utils ------------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter. O(1) overhead."""
    t0 = perf_counter()
    out = func(*args, **kwargs)
    t1 = perf_counter()
    return out, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit. O(number * T(func))."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number

# ------------------------------------ Main ---------------------------------
def main():
    # Read a single level-order line, e.g.:
    #   1 2 3 4 N 5 6
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("No input provided.\nExample:\n  1 2 3 4 N 5 6")
        return

    # Build tree: O(n)
    root = build_tree(tokens)

    solver = Solution()

    # Single run timing (wall clock): O(n)
    ans, t_single = time_single_run(solver.getMaxSum, root)

    # Average over 5 runs (fresh call each run)
    avg = time_with_timeit(lambda: Solution().getMaxSum(root), number=5)

    print("Maximum Non-Adjacent Nodes Sum:", ans)
    print(f"Single-run time : {t_single:.6f} s")
    print(f"Avg over 5 runs : {avg:.6f} s")

    # Quick complexity recap
    print("\nComplexity:")
    print("  Time  : O(n)")
    print("  Space : O(h) recursion (worst O(n) if skewed)")

if __name__ == "__main__":
    """
    Example:
      echo "1 2 3 4 N 5 6" | python3 max_non_adjacent_sum.py
    Expected:
      Maximum Non-Adjacent Nodes Sum: 16
    """
    main()
```

### Example run

Input

```
1 2 3 4 N 5 6
```

Output (timings vary by machine)

```
Maximum Non-Adjacent Nodes Sum: 16
Single-run time : 0.0000xx s
Avg over 5 runs : 0.0000xx s

Complexity:
  Time  : O(n)
  Space : O(h) recursion (worst O(n) if skewed)
```

> Interview one-liner you can say before you code:
> **“I’ll do a postorder DP that returns two values per node: take and skip.
> take = val + skip(L) + skip(R); skip = max(take,skip)(L) + max(take,skip)(R).
> Answer is max at root, O(n) time, O(h) space.”**

---
