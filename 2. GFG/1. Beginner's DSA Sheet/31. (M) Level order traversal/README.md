
---

# Level Order Traversal

**Difficulty:** Medium
**Accuracy:** 70.31%
**Submissions:** 243K+
**Points:** 4

---

### Problem Statement

Given a **root** of a binary tree with `n` nodes, the task is to find its **level order traversal**.

Level order traversal of a tree is **breadth-first traversal** for the tree.

---

### Examples

#### Example 1:

**Input:**

```
root[] = [1, 2, 3]
```

**Output:**

```
[[1], [2, 3]]
```

**Explanation:**
We start with the root node `1`, so the first level of the traversal is `[1]`.
Then we move to its children `2` and `3`, which form the next level, giving the final output `[[1], [2, 3]]`.

---

#### Example 2:

**Input:**

```
root[] = [10, 20, 30, 40, 50]
```

**Output:**

```
[[10], [20, 30], [40, 50]]
```

**Explanation:**
We begin with the root node `10`, which forms the first level as `[10]`.
Its children `20` and `30` make up the second level, and their children `40` and `50` form the third level, resulting in `[[10], [20, 30], [40, 50]]`.

---

#### Example 3:

**Input:**

```
root[] = [1, 3, 2, N, N, 4, 6, 5]
```

**Output:**

```
[[1], [3, 2], [4], [6, 5]]
```

**Explanation:**
The traversal starts with root node `1`, giving the first level `[1]`.
At the second level, we visit its children `3` and `2` from left to right.
Then we move to the third level with node `4`, and finally reach the fourth level with its children `6` and `5`, resulting in `[[1], [3, 2], [4], [6, 5]]`.

---

### Constraints:

* $1 \leq \text{number of nodes} \leq 10^5$
* $0 \leq \text{node->data} \leq 10^9$

---

### Expected Complexities:

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(n)$

---

### Company Tags

* Flipkart
* Morgan Stanley
* Accolite
* Amazon
* Microsoft
* Samsung
* Adobe
* Cisco
* Qualcomm

---

### Topic Tags

* Tree
* Data Structures

---

### Related Interview Experiences

* Ola Cabs Interview Experience Set 2 Android 1.5 Years
* Amazon Interview Experience Set 413 Sdet 1 Campus Internship

---

### Related Articles

* [Level Order Tree Traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/)

---

---

Here’s a crisp interview-style guide to **Level Order Traversal (Breadth-First Search) of a Binary Tree**.

---

## 2) Concept + Step-by-Step Dry Run

### What we need

Return a list of levels, left→right, top→down.
Example tree: `[1, 2, 3, N, N, 4, 6, 5]` (from the prompt)

```
        1
      /   \
     3     2
          /
         4
        / \
       6   5
```

### Core idea (BFS)

Use a **queue**:

1. Push root
2. While queue not empty:

   * Let `cnt = len(queue)` be the number of nodes in this level
   * Pop `cnt` nodes, record their values, push their non-null children
   * Append the level list to `ans`

### Dry run on the above tree

* Start: queue = \[1]
* Level 0:

  * cnt=1 → pop 1 → level = \[1]
  * push children: 3, 2 → queue=\[3,2]
  * ans = \[\[1]]
* Level 1:

  * cnt=2 → pop 3 (no children), pop 2 (left=4) → level=\[3,2]
  * push 4 → queue=\[4]
  * ans = \[\[1],\[3,2]]
* Level 2:

  * cnt=1 → pop 4 → level=\[4]
  * push 6, 5 → queue=\[6,5]
  * ans = \[\[1],\[3,2],\[4]]
* Level 3:

  * cnt=2 → pop 6, pop 5 → level=\[6,5]
  * ans = \[\[1],\[3,2],\[4],\[6,5]] ✅

Time: `O(n)` (each node enqueued/dequeued once)
Space: `O(w)` (w = max width of tree; worst case `O(n)`)

---

## 3) Optimized Python Solutions (multiple ways)

### A) BFS with size-loop (most common in interviews)

```python
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
from collections import deque

class Solution:
    def levelOrder(self, root):
        # Edge case: empty tree => return empty list
        if root is None:
            return []

        ans = []
        q = deque([root])  # queue for BFS; O(n) worst-case memory

        while q:
            level_size = len(q)       # number of nodes on current level
            level_vals = []           # collects values for this level

            for _ in range(level_size):
                node = q.popleft()    # O(1)
                level_vals.append(node.data)

                # push children if present
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level_vals)    # store this level

        return ans
```

**Why interviewers like it:** clean, obvious `level_size` loop isolates per-level work; easy to reason about.

---

### B) BFS using a sentinel/None separator (alternative)

```python
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        ans, level = [], []
        q = deque([root, None])  # None marks the end of a level

        while q:
            node = q.popleft()
            if node is None:
                ans.append(level)
                level = []
                if q:            # there are more nodes; add level marker
                    q.append(None)
                continue

            level.append(node.data)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)

        return ans
```

**Note:** Slightly trickier around trailing `None`, but equally `O(n)`.

---

### C) DFS with depth mapping (no queue; sometimes a follow-up)

```python
class Solution:
    def levelOrder(self, root):
        ans = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append([])          # create list for this depth
            ans[depth].append(node.data)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ans
```

**Why it works:** we visit nodes in pre-order but group values by `depth`.
**Complexity:** `O(n)` time; recursion stack up to `O(h)` (height), worst `O(n)`.

---

## 4) Interviewer Q\&A (high-signal)

**Q1. What’s the time/space complexity of BFS level order?**
A: Time `O(n)`; space `O(w)` where `w` = max breadth (worst `O(n)`).

**Q2. How would you print each level on a new line without extra data structures?**
A: Track `level_size = len(queue)` before the inner loop; process exactly that many nodes, then newline / append the collected list.

**Q3. How to do level order without a queue?**
A: DFS with a `depth` parameter (solution C), grouping values by depth. Another way is recursion with “height” and printing each level separately—inefficient (`O(n*h)`), so not recommended.

**Q4. How do you handle a very skewed tree?**
A: BFS still `O(n)` time; memory at most `O(1)` extra per level (so small). DFS recursion depth could be `O(n)` → risk of recursion depth limits in Python; BFS preferred.

**Q5. How would you modify to return a flat list instead of levels?**
A: Run the same BFS but append values directly into one list instead of nested lists.

**Q6. How to compute the average of nodes at each level?**
A: During the `level_size` loop, accumulate the sum and divide by `level_size` at the end of each level.

---

### Quick Edge Cases to mention in interviews

* `root` is `None` → `[]`
* Single node → `[[root.data]]`
* Unbalanced (linked-list) tree → BFS still fine
* Very wide level → memory dominated by that level

---

---

Below is a **complete, runnable Python program** for Level Order Traversal (BFS) of a binary tree.
It includes: the `Node` class, the `Solution.levelOrder` method (BFS), helpers to build a tree from level-order arrays (with `None` as missing), **inline complexity notes**, example inputs, outputs, and **timing** using `time.perf_counter()`.

```python
from collections import deque
from time import perf_counter

# ----------------------------
# Binary Tree Node definition
# ----------------------------
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# -----------------------------------
# Helper: build tree from level array
# input: list like [1, 2, 3, None, 5]
# -----------------------------------
def build_tree_from_level(arr):
    """
    Time:  O(n)  — each list element is processed once
    Space: O(n)  — queue + nodes
    """
    if not arr:
        return None
    it = iter(arr)
    root_val = next(it)
    if root_val is None:
        return None

    root = Node(root_val)
    q = deque([root])

    for val in it:
        parent = q[0]  # peek parent
        # Fill left if empty
        if parent.left is None:
            if val is not None:
                parent.left = Node(val)
                q.append(parent.left)
        else:
            # Fill right, then pop this parent
            if val is not None:
                parent.right = Node(val)
                q.append(parent.right)
            q.popleft()
    return root


# -------------------------------------------------------
# Solution: BFS level order traversal (list of level lists)
# -------------------------------------------------------
class Solution:
    def levelOrder(self, root):
        """
        Returns: List[List[int]] — values level by level.
        Time:  O(n)  — each node enqueued & dequeued once
        Space: O(w)  — queue holds at most width of a level (<= n)
        """
        if root is None:
            return []

        ans = []
        q = deque([root])

        while q:
            level_size = len(q)       # nodes on current level
            level_vals = []           # collect values here

            # Process exactly this level
            for _ in range(level_size):
                node = q.popleft()    # O(1)
                level_vals.append(node.data)

                # enqueue children (if any)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level_vals)

        return ans


# ----------------------------
# Demo / "Main" (with timing)
# ----------------------------
if __name__ == "__main__":
    # Example 1 (from prompt-like): [1, 2, 3] -> [[1], [2, 3]]
    arr1 = [1, 2, 3]
    root1 = build_tree_from_level(arr1)

    # Example 2: [1, None, 2, 3] means 1 -> right=2, and 2 -> left=3
    # Level order should be [[1], [2], [3]]
    arr2 = [1, None, 2, 3]
    root2 = build_tree_from_level(arr2)

    # Example 3: deeper tree
    #        1
    #      /   \
    #     3     2
    #          /
    #         4
    #        / \
    #       6   5
    arr3 = [1, 3, 2, None, None, 4, None, 6, 5]
    root3 = build_tree_from_level(arr3)

    sol = Solution()

    # Time each run (very small trees; timing mostly illustrative)
    for idx, root in enumerate([root1, root2, root3], start=1):
        t0 = perf_counter()
        levels = sol.levelOrder(root)
        t1 = perf_counter()

        print(f"Input Tree {idx}:")
        if idx == 1:
            print("  Level array:", arr1)
        elif idx == 2:
            print("  Level array:", arr2)
        else:
            print("  Level array:", arr3)
        print("Output (levels):", levels)
        print(f"Time taken: {(t1 - t0)*1e6:.2f} μs\n")
```

### Sample Output (illustrative)

```
Input Tree 1:
  Level array: [1, 2, 3]
Output (levels): [[1], [2, 3]]
Time taken: 80.21 μs

Input Tree 2:
  Level array: [1, None, 2, 3]
Output (levels): [[1], [2], [3]]
Time taken: 77.34 μs

Input Tree 3:
  Level array: [1, 3, 2, None, None, 4, None, 6, 5]
Output (levels): [[1], [3, 2], [4], [6, 5]]
Time taken: 109.47 μs
```

> Notes on timing
>
> * For very small inputs, timings are dominated by interpreter overhead; on large trees you’ll still see linear scaling `O(n)`.

---

## 6) Real-World Use Cases (a few high-impact ones)

1. **Systems & Networking (BFS over topologies):**
   Level-by-level exploration of a computer network, social graph, or service dependency graph (e.g., find nodes at “distance k” from a failure).

2. **Compiler/Interpreter Pipelines:**
   Walking abstract syntax trees by levels (e.g., staged analyses, constraints resolution order).

3. **UI & Game Engines:**
   Performing operations by scene-graph layers—layout, culling, or effects applied breadth-first for consistent level ordering.

4. **Scheduling & Batch Processing:**
   Processing tasks in waves by dependency level (topological layers sometimes derived via BFS on DAGs or tree-like job hierarchies).

5. **Distributed Systems (Tree-based aggregations):**
   Collecting metrics or broadcasting configuration updates per “layer” to bound fan-out per round.
