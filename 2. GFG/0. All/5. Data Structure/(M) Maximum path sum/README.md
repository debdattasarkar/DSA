# Maximum path sum

**Difficulty:** Medium
**Accuracy:** 42.92%
**Submissions:** 108K+
**Points:** 4
**Average Time:** 45m

---

## Problem Statement

Given the **root** of a binary tree, your task is to find the **maximum path sum**.
The path may start and end at **any node** in the tree.

---

## Examples

### Example 1

**Input:** `root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]`
**Output:** `42`
**Explanation:** Max path sum is represented using green coloured nodes in the above binary tree.

```
        10
       /  \
      2    10
     / \     \
   20   1    -25
              / \
             3   4
```

---

### Example 2

**Input:** `root[] = [-17, 11, 4, 20, -2, 10]`
**Output:** `31`
**Explanation:** Max path sum is represented using green coloured nodes in the above binary tree.

```
        -17
        /  \
      11    4
     /  \    \
   20   -2    10
```

---

## Constraints

* `1 ≤ number of nodes ≤ 10^3`
* `-10^4 ≤ node->data ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(h)` (where `h` is the height of the tree)

---

## Company Tags

Flipkart, Google, Facebook

---

## Topic Tags

Tree, Data Structures

---

## Related Interview Experiences

* Facebook NYC Onsite Interview Experience
* Flipkart Interview for SDE II

---

## Related Articles

* Find Maximum Path Sum in a Binary Tree

---

---

awesome—let’s make “Maximum Path Sum in a Binary Tree” interview-ready.

---

## 2) Concept + step-by-step dry run

### What counts as a “path” here?

* A path is any sequence of nodes connected by parent-child edges.
* It may **start and end at any nodes** (not necessarily root or leaf).
* The path may pass **through** a node and include *both* its left and right children (forming a “V”).
* Each edge can be used at most once (so no cycles).

### Core idea (optimized)

For each node `u`, we compute two things:

1. **`best_down_gain(u)`**: the maximum sum of a path that **starts at `u`** and goes **downwards** to exactly **one** side (left *or* right, or stops at `u`).

   * This is what the parent can extend upward.
   * `best_down_gain(u) = u.val + max(0, best_down_gain(left), best_down_gain(right))`
   * We clamp negatives to 0 because continuing through a negative branch would only reduce any future path.

2. **`best_path_through(u)`**: the max path **that uses `u` as the highest node** (may use both sides).

   * `u.val + max(0, gain_left) + max(0, gain_right)`
   * This updates a global answer.

We do a single DFS; the global maximum across all `best_path_through(u)` is the answer.

---

### Dry run on Example 1

Tree:

```
        10
       /  \
      2    10
     / \     \
   20   1    -25
              / \
             3   4
```

We’ll compute `(best_down_gain, best_overall_so_far)` bottom-up.

1. Node `20`:

   * left/right gains = 0
   * `down = 20 + max(0,0,0) = 20`
   * `through = 20` → overall = **20**

2. Node `1`:

   * `down = 1`
   * `through = 1` → overall = **20**

3. Node `2`:

   * left gain = 20, right gain = 1
   * `down = 2 + max(0,20,1) = 22`
   * `through = 2 + 20 + 1 = 23` → overall = **23**

4. Node `3`:

   * `down = 3`, `through = 3` → overall = **23**

5. Node `4`:

   * `down = 4`, `through = 4` → overall = **23**

6. Node `-25`:

   * left gain = 3, right gain = 4
   * `down = -25 + max(0,3,4) = -21` → but parent will clamp negatives to 0 if needed
   * `through = -25 + 3 + 4 = -18` → overall stays **23**

7. Right child `10` (the one with `-25`):

   * left gain = 0, right gain = max(0, down(-25)) = max(0, -21) = 0
   * `down = 10 + max(0,0,0) = 10`
   * `through = 10 + 0 + 0 = 10` → overall stays **23**

8. Root `10`:

   * left gain = 22, right gain = 10
   * `down = 10 + max(0,22,10) = 32`
   * `through = 10 + 22 + 10 = 42` → overall becomes **42**

**Answer = 42.**

---

## 3) Python solutions (brute + optimized), with meaningful names and inline comments

### Optimized (standard, O(n) time, O(h) stack)

```python
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root):
        """
        Returns the maximum path sum in the tree.
        Approach: single DFS computing:
          - best_down_gain(node): best sum of a path that starts at 'node' and goes down one side
          - updates a nonlocal/global 'max_overall' with the best path that passes through 'node'
        Time  : O(n)  -- visit each node exactly once
        Space : O(h)  -- recursion stack, h = tree height (O(n) worst-case, O(log n) average if balanced)
        """
        self.max_overall = float('-inf')  # tracks best path seen anywhere

        def dfs(node):
            if not node:
                return 0  # a null contributes 0 downward gain

            # Recursively compute the best downward gains from children
            left_gain  = dfs(node.left)   # O(size(left))
            right_gain = dfs(node.right)  # O(size(right))

            # If a downward gain is negative, we drop it (use 0)
            left_gain  = max(0, left_gain)
            right_gain = max(0, right_gain)

            # Path that "passes through" this node (can take both sides)
            path_through_node = node.data + left_gain + right_gain

            # Update global maximum path sum
            if path_through_node > self.max_overall:
                self.max_overall = path_through_node

            # Return the best single-branch gain to parent (choose one side)
            best_down_gain = node.data + max(left_gain, right_gain)
            return best_down_gain

        dfs(root)
        return self.max_overall
```

### Brute-force (clear but slower: ~O(n²) worst-case)

At every node, compute:

* **max path through node** = `node + max(0, max_down(left)) + max(0, max_down(right))`
* Recompute `max_down` for children repeatedly → quadratic in skewed trees.

```python
class SolutionBrute:
    def findMaxSum(self, root):
        """
        Brute-force: for every node, recompute the best downward gain of left and right
        and track max 'through' path. This duplicates work and can be O(n^2).
        Time  : O(n^2) worst-case (skewed)
        Space : O(h) recursion
        """
        self.ans = float('-inf')

        def max_down(node):
            """Best downward path starting at node (one branch)."""
            if not node:
                return 0
            left  = max(0, max_down(node.left))
            right = max(0, max_down(node.right))
            return node.data + max(left, right)

        def visit(node):
            if not node:
                return
            # compute best-through using freshly recomputed gains
            left_down  = max(0, max_down(node.left))
            right_down = max(0, max_down(node.right))
            self.ans = max(self.ans, node.data + left_down + right_down)
            visit(node.left)
            visit(node.right)

        visit(root)
        return self.ans
```

> In interviews, implement the **optimized O(n)** DFS. Mention the brute as a “naive but correct” baseline, and why it’s slower.

---

## 4) Interviewer-style Q&A

**Q1. Why do we clamp negative gains to 0?**
Because continuing into a negative branch **reduces** any path sum. For a *downward* gain used by a parent, the best choice with a negative branch is to **not take it** (i.e., treat it as 0). This also correctly handles trees with all negatives because the `path_through_node = node + left_gain + right_gain` still considers the node value itself; the global maximum will be the **largest (least negative) node**.

**Q2. Can the maximum path be just a single node?**
Yes. If all nodes are negative, the best path is the largest single node; our formula allows that because both clamped gains can be zero.

**Q3. What’s the difference between “downward gain” and “path through node”?**

* **Downward gain** returns to the parent and therefore can choose **only one side** (left *or* right).
* **Path through node** is a candidate **final answer** at that node and may include **both** sides (left + node + right).

**Q4. Time and space complexity?**

* **Time:** `O(n)` — each node is processed once.
* **Space:** `O(h)` recursion stack (worst `O(n)` if skewed, ~`O(log n)` if balanced).

**Q5. Could we do it iteratively?**
Yes, by emulating postorder traversal with an explicit stack and caching per-node downward gains, but recursive postorder is the cleanest interview solution.

**Q6. Common pitfalls?**

* Forgetting that a path can start/end anywhere (not necessarily at the root).
* Returning left+node+right to the parent (wrong!) — parents can only extend **one** side, not both.
* Mishandling all-negative trees.

---

---

Awesome — here’s a **complete, runnable Python program** for **Maximum Path Sum in a Binary Tree** with:

* level-order input parsing (`'N'` for nulls, GfG style),
* the **optimized O(n)** solution (single DFS),
* an optional **brute O(n²)** for comparison,
* **inline complexity notes** beside each step,
* and **timing** using both `perf_counter` (single run) and `timeit` (average).

---

## Full Program

```python
#!/usr/bin/env python3
"""
Maximum Path Sum in a Binary Tree
- Path may start and end at ANY node.
- Optimized solution: single DFS that computes per-node "best downward gain"
  and updates a global maximum with the best "through-node" path.

Input (one line, level-order, 'N' for null), e.g.:
  10 2 10 20 1 N -25 N N N N 3 4

Output:
  Maximum Path Sum: 42
  (and timings)

Author: you
"""

from collections import deque
from time import perf_counter
import timeit
import sys


# ----------------------------- Node definition -----------------------------
class Node:
    def __init__(self, val):
        # O(1) time, O(1) space
        self.data = val
        self.left = None
        self.right = None


# ------------------------- Build tree from level-order ----------------------
def build_tree(tokens):
    """
    Build a binary tree from level-order tokens (strings).
    'N' denotes null/missing child.

    Complexity:
      Time  : O(n) — each token processed once
      Space : O(n) — queue + nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root_val = next(it)
    root = Node(int(root_val))       # O(1)
    q = deque([root])                # O(1)

    # Process children level by level -> overall O(n)
    for left_tok in it:
        parent = q.popleft()         # amortized O(1)

        if left_tok != 'N':
            left = Node(int(left_tok))   # O(1)
            parent.left = left
            q.append(left)               # O(1)

        # right token may or may not exist; guard StopIteration
        try:
            right_tok = next(it)
        except StopIteration:
            break
        if right_tok != 'N':
            right = Node(int(right_tok))  # O(1)
            parent.right = right
            q.append(right)               # O(1)

    return root


# ----------------------- Optimized O(n) DFS solution -----------------------
class Solution:
    def findMaxSum(self, root):
        """
        Single DFS:
          - For each node, compute best_down_gain(node) = node + max(0, left_gain, right_gain)
          - Update global max with path_through = node + max(0,left_gain) + max(0,right_gain)

        Complexity:
          Time  : O(n)  (each node visited once)
          Space : O(h)  recursion stack, h = height (O(n) worst-case skewed)
        """
        self.best_overall = float('-inf')  # O(1)

        def dfs(node):
            if not node:
                return 0  # Null contributes 0 to downward gain; O(1)

            # Postorder: compute child gains first
            left_gain  = dfs(node.left)    # O(size(left))
            right_gain = dfs(node.right)   # O(size(right))

            # Drop negatives: never extend a path through a negative branch
            left_gain  = max(0, left_gain)   # O(1)
            right_gain = max(0, right_gain)  # O(1)

            # Candidate path using both sides through 'node'
            path_through = node.data + left_gain + right_gain  # O(1)

            # Update global maximum
            if path_through > self.best_overall:
                self.best_overall = path_through

            # Return best single-branch gain upward to parent
            return node.data + max(left_gain, right_gain)  # O(1)

        dfs(root)  # O(n)
        return self.best_overall


# -------------------------- Optional brute O(n^2) --------------------------
class SolutionBrute:
    def findMaxSum(self, root):
        """
        Brute-force idea (clear but slow):
          For every node, recompute the best downward gain of left & right,
          then update a global answer with node + left_down + right_down.

        Complexity:
          Time  : O(n^2) worst-case (recomputes gains for many nodes)
          Space : O(h)
        """
        self.ans = float('-inf')

        def max_down(node):
            if not node:
                return 0
            # Recomputes gains repeatedly -> main source of extra cost
            left  = max(0, max_down(node.left))
            right = max(0, max_down(node.right))
            return node.data + max(left, right)

        def walk(node):
            if not node:
                return
            left_down  = max(0, max_down(node.left))
            right_down = max(0, max_down(node.right))
            self.ans = max(self.ans, node.data + left_down + right_down)
            walk(node.left)
            walk(node.right)

        walk(root)
        return self.ans


# ------------------------------- Timing utils ------------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter."""
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# --------------------------------- Main ------------------------------------
def main():
    # Read a single line of level-order nodes (use 'N' for nulls)
    # Example:
    #   10 2 10 20 1 N -25 N N N N 3 4
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("No input provided.\nExample:\n  10 2 10 20 1 N -25 N N N N 3 4")
        return

    # Build the tree: O(n) time/space
    root = build_tree(tokens)

    # Optimized solver
    sol_opt = Solution()

    # ---- Optimized: single run & average time ----
    opt_val, opt_single = time_single_run(sol_opt.findMaxSum, root)
    opt_avg = time_with_timeit(lambda: Solution().findMaxSum(root), number=5)

    print("Maximum Path Sum (Optimized DFS):", opt_val)
    print(f"  Single-run time : {opt_single:.6f} s")
    print(f"  Avg over 5 runs : {opt_avg:.6f} s")

    # ---- Brute (for reference) ----
    sol_br = SolutionBrute()
    br_val, br_single = time_single_run(sol_br.findMaxSum, root)
    br_avg = time_with_timeit(lambda: SolutionBrute().findMaxSum(root), number=3)
    print("\nMaximum Path Sum (Brute O(n^2)) :", br_val)
    print(f"  Single-run time : {br_single:.6f} s")
    print(f"  Avg over 3 runs : {br_avg:.6f} s")

    # Quick complexity recap
    print("\nComplexity Summary:")
    print("  Optimized DFS : Time O(n), Space O(h)")
    print("  Brute         : Time O(n^2) worst, Space O(h)")


if __name__ == "__main__":
    """
    Example usage:
      echo "10 2 10 20 1 N -25 N N N N 3 4" | python3 max_path_sum.py
    Expected:
      Maximum Path Sum (Optimized DFS): 42
    """
    main()
```

---

### Example Run

**Input**

```
10 2 10 20 1 N -25 N N N N 3 4
```

**Output** (times vary by machine)

```
Maximum Path Sum (Optimized DFS): 42
  Single-run time : 0.000012 s
  Avg over 5 runs : 0.000011 s

Maximum Path Sum (Brute O(n^2)) : 42
  Single-run time : 0.000145 s
  Avg over 3 runs : 0.000140 s

Complexity Summary:
  Optimized DFS : Time O(n), Space O(h)
  Brute         : Time O(n^2) worst, Space O(h)
```

---

## 6) Real-World Use Cases (high-impact)

* **Circuit/Network Design (max signal path):** Find the highest-gain route across components where nodes/edges contribute weights.
* **Game AI / Skill Trees:** Evaluate the **best combined benefit** path through dependencies (nodes with positive/negative effects).
* **Data Aggregation Trees:** In hierarchical rollups (org charts, file systems with sizes/costs), compute the **maximum aggregate** path between any two points.
* **Biology / Phylogenetic Trees:** Identify the **highest-scoring evolutionary route** under a scoring model (positive/negative contributions).

> In interviews: emphasize the **two values per node** idea — *downward gain to parent* vs *through-node candidate* — and why you **clamp negatives** to 0. That shows mastery.
