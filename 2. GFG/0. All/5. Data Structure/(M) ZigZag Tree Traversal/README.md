# ZigZag Tree Traversal

**Difficulty:** Medium
**Accuracy:** 54.05%
**Submissions:** 182K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given the **root** of a binary tree, you have to find the **zig-zag level order traversal** of the binary tree.

**Note:** In zig-zag traversal we traverse the nodes **from left to right for odd-numbered levels**, and **from right to left for even-numbered levels**.

---

## Examples

### Example 1

**Input:** `root = [1, 2, 3, 4, 5, 6, 7]`

```
        1
      /   \
     2     3
    / \   / \
   4  5  6   7
```

**Output:** `[1, 3, 2, 4, 5, 6, 7]`

**Explanation:**

* Level 1 (**left to right**): `[1]`
* Level 2 (**right to left**): `[3, 2]`
* Level 3 (**left to right**): `[4, 5, 6, 7]`
  **Final result:** `[1, 3, 2, 4, 5, 6, 7]`

---

### Example 2

**Input:** `root = [7, 9, 7, 8, 8, 6, N, 10, 9]`

```
          7
        /   \
       9     7
      / \     \
     8   8     6
    / \
   10  9
```

**Output:** `[7, 7, 9, 8, 8, 6, 9, 10]`

**Explanation:**

* Level 1 (**left to right**): `[7]`
* Level 2 (**right to left**): `[7, 9]`
* Level 3 (**left to right**): `[8, 8, 6]`
* Level 4 (**right to left**): `[9, 10]`
  **Final result:** `[7, 7, 9, 8, 8, 6, 9, 10]`

---

## Constraints

* `1 ≤ number of nodes ≤ 10^5`
* `1 ≤ node->data ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Flipkart, Amazon, Microsoft, Snapdeal, FactSet, Hike, Walmart, Cisco

---

## Topic Tags

Traversal, Tree, Data Structures, Algorithms

---

## Related Interview Experiences

* Flipkart Interview Experience Set 24

---

---

got it — here’s a tight, interview-ready pack for ZigZag / Spiral Level Order.

---

# 2) Explanation + step-by-step dry run

## What is ZigZag traversal?

Level-order (BFS) but the direction alternates per level:
odd levels: **left → right**; even levels: **right → left**.

### Core ideas you can use

1. **BFS queue + direction flag**

   * Do a normal level-order.
   * For each level, either:

     * collect values into a list and reverse it when needed (simple), or
     * push values to the front or back of a deque (no per-level reverse).

2. **Two stacks (“spiral order”)**

   * `s1` holds nodes of the current left→right level; `s2` holds the next right→left level.
   * While popping from one stack, push children to the other in opposite order to flip direction.

All approaches are **O(n)** time and **O(n)** space (for the queue/stacks and output).

---

## Dry run (BFS + deque) on:

```
        1
      /   \
     2     3
    / \   / \
   4  5  6   7
```

Expected: `[1, 3, 2, 4, 5, 6, 7]`

State: `q = [1]`, `left_to_right = True`, `ans=[]`

* **Level 1:** size=1
  pop 1 → append **right** (3) and **left** (2) to queue? (No, for BFS we always enqueue left then right; direction only affects *output order*.)
  Collect values: since `left_to_right=True`, append at right → level = `[1]`.
  Enqueue children: 2, 3.
  Toggle → `left_to_right=False`. `ans=[1]`.

* **Level 2:** size=2 (nodes: 2, 3)
  Process 2 → push 4,5; output handling: since `left_to_right=False`, insert 2 at **left** of level deque → `[2]`.
  Process 3 → push 6,7; insert 3 at **left** → `[3, 2]`.
  Toggle → `left_to_right=True`. `ans=[1, 3, 2]`.

* **Level 3:** size=4 (nodes: 4,5,6,7), `left_to_right=True`
  Visit 4,5,6,7 in BFS order; append to right → `[4,5,6,7]`.
  Toggle → `False`. `ans=[1, 3, 2, 4, 5, 6, 7]`. Done.

---

# 3) Python solutions (with interview-style inline comments)

All variants match your class signature and return a **list of ints** in zigzag order.

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
```

## A) BFS + per-level deque (clean & optimal; no `reverse`)

```python
class Solution:
    def zigZagTraversal(self, root):
        # Edge case
        if not root:
            return []
        
        q = deque([root])          # queue for BFS; O(n) worst-case space
        left_to_right = True
        ans = []                   # final output; O(n) space
        
        # Each node is enqueued and dequeued exactly once -> O(n) time
        while q:
            level_size = len(q)    # number of nodes at this level
            level = deque()        # collect values for this level with O(1) appendleft/append
            
            for _ in range(level_size):
                node = q.popleft()               # O(1)
                
                # Direction-aware placement (avoid per-level reverse)
                if left_to_right:
                    level.append(node.data)      # O(1)
                else:
                    level.appendleft(node.data)  # O(1)
                
                # Standard BFS enqueues: always left then right (direction does not affect enqueuing)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Append this level to answer
            ans.extend(level)       # O(width) per level; total O(n)
            left_to_right = not left_to_right
        
        # Total: Time O(n), Space O(n) (queue + output)
        return ans
```

## B) BFS + collect-and-reverse per level (simple to explain)

```python
class SolutionReversePerLevel:
    def zigZagTraversal(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        left_to_right = True
        
        while q:
            level_size = len(q)
            tmp = []                        # temporary level list
            
            for _ in range(level_size):
                node = q.popleft()
                tmp.append(node.data)       # O(1)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            
            # Reverse this level if needed (O(level_size))
            if not left_to_right:
                tmp.reverse()
            
            ans.extend(tmp)                 # O(level_size)
            left_to_right = not left_to_right
        
        # Time: O(n) (each node once + total reversing still O(n)), Space: O(n)
        return ans
```

## C) Two stacks (a classic “spiral order” solution)

```python
class SolutionTwoStacks:
    def zigZagTraversal(self, root):
        if not root:
            return []
        s1 = [root]     # current level (left->right)
        s2 = []         # next level (right->left)
        ans = []
        
        # Each node is pushed/popped a constant number of times -> O(n)
        while s1 or s2:
            # Process s1 left->right; push children into s2 in order: left then right
            while s1:
                node = s1.pop()
                ans.append(node.data)
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
            
            # Process s2 right->left; push children into s1 in order: right then left
            while s2:
                node = s2.pop()
                ans.append(node.data)
                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)
        
        # Time: O(n), Space: O(n) (stacks + output)
        return ans
```

> Pick A) in interviews for clarity and optimality without extra reversals, or C) if the interviewer specifically mentions “two stacks / spiral order”.

---

# 4) Interviewer-style Q&A

**Q1. What’s the time and space complexity?**
**A.** Time **O(n)** because every node is visited once. Space **O(n)** due to the queue or stacks holding up to a level’s width (plus output).

**Q2. Why not reverse the queueing order instead of values?**
**A.** BFS queueing order should stay consistent (left then right). The *output* direction is what alternates. If you mix queue orders, you can still solve it (two stacks approach), but standard BFS stays simpler and less error-prone.

**Q3. How does the deque solution avoid per-level `reverse()`?**
**A.** At each level, we add values to a `deque`: `append` when left→right, `appendleft` when right→left. This keeps per-level cost linear without a separate reverse pass.

**Q4. What are the corner cases?**
**A.** Empty tree, single node, skewed trees (all left or all right), and trees with missing children on various nodes. The algorithm still processes levels correctly.

**Q5. Can we achieve O(1) auxiliary space?**
**A.** Not generally for level-order traversal because you must hold at least the current level’s nodes (Θ(width)). Morris-style tricks help for inorder/postorder, not for zigzag level order.

**Q6. When would you prefer the two-stacks solution?**
**A.** When a “spiral order” approach is requested explicitly, or in languages/platforms where pushing to opposite stacks is more natural than maintaining a deque per level.

**Q7. How do you verify correctness quickly in an interview?**
**A.** Walk a small tree by hand (like the example), listing levels and alternating directions, and ensure the produced sequence matches.

---

---

awesome — here’s a **complete, runnable Python program** that:

* builds a binary tree from **level-order input** (use `'N'` for nulls — GfG style),
* runs **two** zigzag implementations (BFS+deque and Two Stacks),
* prints the traversal and **benchmarks** each using `perf_counter` and `timeit`,
* and includes **inline comments** explaining **time/space complexity** at each step.

---

## Full Program (copy–paste and run)

```python
#!/usr/bin/env python3
"""
ZigZag (Spiral) Level-Order Traversal of a Binary Tree
- Input: one line, level-order with 'N' for nulls   e.g. 1 2 3 4 5 6 7
- Output: zigzag traversal list
This file prints results for two implementations and times them.
"""

from collections import deque
from time import perf_counter
import timeit
import sys

# -------------------- Node definition --------------------
class Node:
    def __init__(self, val):
        # O(1) time, O(1) space
        self.data = val
        self.left = None
        self.right = None


# -------------------- Build tree from level order --------------------
def build_tree(tokens):
    """
    Build a binary tree from level-order tokens (strings).
    Complexity:
      - Time:  O(n) — each token processed once
      - Space: O(n) — queue + nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root = Node(int(next(it)))     # O(1)
    q = deque([root])              # O(1)

    # Each node is enqueued/dequeued once -> O(n)
    for left_val in it:
        parent = q.popleft()       # amortized O(1)

        # attach left child
        if left_val != 'N':
            left = Node(int(left_val))  # O(1)
            parent.left = left
            q.append(left)              # O(1)

        # attach right child if exists
        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val != 'N':
            right = Node(int(right_val))  # O(1)
            parent.right = right
            q.append(right)               # O(1)

    return root


# -------------------- Solution A: BFS + per-level deque --------------------
class SolutionDeque:
    def zigZagTraversal(self, root):
        """
        Direction-aware per-level deque (no reverse step).
        Complexity:
          - Time:  O(n) — each node visited once; O(1) append/appendleft
          - Space: O(n) — queue + output
        """
        if not root:
            return []

        q = deque([root])     # BFS queue, O(n) worst-case space (width)
        left_to_right = True
        ans = []              # O(n) space for output

        while q:                                  # loops levels -> O(n) total work
            level_size = len(q)
            level = deque()                       # O(1)
            for _ in range(level_size):           # processes each node once
                node = q.popleft()                # O(1)
                # O(1) placement depending on direction
                if left_to_right:
                    level.append(node.data)       # O(1)
                else:
                    level.appendleft(node.data)   # O(1)

                # Enqueue children (standard BFS)
                if node.left:  q.append(node.left)   # O(1)
                if node.right: q.append(node.right)  # O(1)

            ans.extend(level)                     # O(level_size) -> O(n) total
            left_to_right = not left_to_right

        return ans


# -------------------- Solution B: Two Stacks (classic spiral) --------------------
class SolutionTwoStacks:
    def zigZagTraversal(self, root):
        """
        Two-stack spiral order.
        Complexity:
          - Time:  O(n) — each node pushed/popped constant times
          - Space: O(n) — stacks + output
        """
        if not root:
            return []

        s1 = [root]   # current level, left->right
        s2 = []       # next level,   right->left
        ans = []

        # Process until both stacks empty
        while s1 or s2:
            # Pop all from s1 (left->right), push children into s2 (left then right)
            while s1:
                node = s1.pop()        # O(1)
                ans.append(node.data)  # O(1)
                if node.left:  s2.append(node.left)   # O(1)
                if node.right: s2.append(node.right)  # O(1)

            # Pop all from s2 (right->left), push children into s1 (right then left)
            while s2:
                node = s2.pop()        # O(1)
                ans.append(node.data)  # O(1)
                if node.right: s1.append(node.right)  # O(1)
                if node.left:  s1.append(node.left)   # O(1)

        return ans


# -------------------- Timing helpers --------------------
def time_single_run(func, *args, **kwargs):
    """
    Single wall-clock timing using perf_counter.
    """
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)


def time_with_timeit(callable_stmt, number=5):
    """
    Average runtime over `number` runs using timeit.
    """
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# -------------------- Main driver --------------------
def main():
    # Read one line of tokens for the tree (level-order)
    # Examples:
    #   1 2 3 4 5 6 7
    #   7 9 7 8 8 6 N 10 9
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("No input provided. Example: 1 2 3 4 5 6 7")
        return

    # Build the tree (O(n) time/space)
    root = build_tree(tokens)

    # Prepare solvers
    sol_deque = SolutionDeque()
    sol_stacks = SolutionTwoStacks()

    # ---- Run A: BFS + deque ----
    res_a, t_a = time_single_run(sol_deque.zigZagTraversal, root)
    avg_a = time_with_timeit(lambda: sol_deque.zigZagTraversal(root), number=5)

    # ---- Run B: Two Stacks ----
    res_b, t_b = time_single_run(sol_stacks.zigZagTraversal, root)
    avg_b = time_with_timeit(lambda: sol_stacks.zigZagTraversal(root), number=5)

    # Print results
    print("ZigZag (BFS + deque):", res_a)
    print(f"  Single-run time : {t_a:.6f} s")
    print(f"  Avg over 5 runs : {avg_a:.6f} s\n")

    print("ZigZag (Two Stacks):", res_b)
    print(f"  Single-run time : {t_b:.6f} s")
    print(f"  Avg over 5 runs : {avg_b:.6f} s\n")

    # Complexity summary (for quick reference)
    print("Complexity Summary (both methods):")
    print("  Time  : O(n)")
    print("  Space : O(n)   (queue/stacks + output)")


# Entry point
if __name__ == "__main__":
    """
    Example:
      echo "1 2 3 4 5 6 7" | python3 zigzag.py
      -> ZigZag: [1, 3, 2, 4, 5, 6, 7]
    """
    main()
```

### Example run

Input:

```
1 2 3 4 5 6 7
```

Output (times will vary by machine):

```
ZigZag (BFS + deque): [1, 3, 2, 4, 5, 6, 7]
  Single-run time : 0.000012 s
  Avg over 5 runs : 0.000011 s

ZigZag (Two Stacks): [1, 3, 2, 4, 5, 6, 7]
  Single-run time : 0.000013 s
  Avg over 5 runs : 0.000012 s

Complexity Summary (both methods):
  Time  : O(n)
  Space : O(n)   (queue/stacks + output)
```

---

## Real-World Use Cases (high-impact)

* **UI rendering / scene graphs:** Alternate pass directions across levels for layout/animation sweeps that reduce cache misses or match designer-specified “snake” ordering.
* **Matrix snake/zigzag serialization:** JPEG uses zigzag order to serialize DCT coefficients; tree zigzag is a conceptual cousin when emitting hierarchical states in alternating orders.
* **Breadth-phase processing with alternating policies:** In search/exploration (game trees, dependency trees), zigzag can simulate alternating priorities between sibling groups while preserving level boundaries.
