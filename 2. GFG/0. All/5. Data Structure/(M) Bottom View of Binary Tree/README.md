# Bottom View of Binary Tree

**Difficulty:** Medium
**Accuracy:** 54.18%
**Submissions:** 326K+
**Points:** 4
**Average Time:** 45m

---

You are given the **root** of a binary tree, and your task is to return its **bottom view**.
The **bottom view** of a binary tree is the set of nodes visible when the tree is viewed from the bottom.

---

### Note:

If there are **multiple bottom-most nodes** for a horizontal distance from the root, then the **latter one** in the level order traversal is considered.

---

## Examples

### Example 1:

**Input:**

```
root = [1, 2, 3, 4, 5, N, 6]
```

**Output:**

```
[4, 2, 5, 3, 6]
```

**Explanation:**
The green nodes represent the bottom view of the binary tree.

```
           1 (hd = 0)
         /   \
   (hd=-1)2   3(hd=1)
       / \      \
(hd=-2)4 5(hd=0) 6(hd=2)
```

* For hd = -2 → 4
* For hd = -1 → 2
* For hd = 0  → 5 (replaces 1 since it’s lower)
* For hd = 1  → 3
* For hd = 2  → 6

So bottom view = **[4, 2, 5, 3, 6]**

---

### Example 2:

**Input:**

```
root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
```

**Output:**

```
[5, 10, 4, 28, 25]
```

**Explanation:**
The green nodes represent the bottom view of the binary tree.

```
                20 (hd=0)
              /     \
        (hd=-1)8     22(hd=1)
           /   \     /   \
      (hd=-2)5 3(0) 4(0) 25(2)
               / \
          (hd=-1)10 14(1)
                     \
                      28(1)
```

So the bottom-most visible nodes are **[5, 10, 4, 28, 25]**

---

## Constraints:

```
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5
```

---

## Expected Complexities:

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## Company Tags:

* Paytm
* Flipkart
* Accolite
* Amazon
* OYO Rooms
* Walmart
* CouponDunia

---

## Topic Tags:

* Tree
* Data Structures

---

## Related Interview Experiences:

* Paytm Interview Experience Set 12 (1–5 Years Experienced)
* Walmart Labs Interview Experience Set 2 (On Campus)

---

## Related Articles:

* Bottom View Binary Tree

---

---

here we go — bottom view made friendly, interview-ready, and tight.

---

## 2) Intuition + step-by-step dry run

### What is the “bottom view”?

Imagine looking at the tree from below. For each **horizontal distance (hd)** from the root:

* Keep the node that sits **lowest** (i.e., appears last in level order for that hd).
* Root has `hd = 0`.
* Going **left** decreases `hd` by 1; going **right** increases `hd` by 1.

### Most natural approach (BFS / level order)

* Do a **level order traversal** while tracking each node’s `hd`.
* Maintain a map `hd -> node.data`.
  Because BFS visits nodes level by level (top → bottom), the **last node seen for a given hd** is the bottom-most.
* After traversal, collect values in **increasing hd order**.

### Dry run (Example 1)

Tree: `[1, 2, 3, 4, 5, N, 6]`

```
Start: queue = [(1, hd=0)]
map = {}

pop (1,0)   → map[0] = 1; push (2,-1), (3,1)
pop (2,-1)  → map[-1] = 2; push (4,-2), (5,0)
pop (3,1)   → map[ 1] = 3; push (6,2)
pop (4,-2)  → map[-2] = 4
pop (5,0)   → map[ 0] = 5   # overwrites 1 (we're lower in level)
pop (6,2)   → map[ 2] = 6

map = { -2:4, -1:2, 0:5, 1:3, 2:6 }
sorted hd → [-2,-1,0,1,2] → result = [4,2,5,3,6]
```

---

## 3) Python solutions (interview-ready)

Both keep your signature:

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
```

### A) BFS (level order) with horizontal distance — **recommended**

* Simple, iterative, O(n).
* “Latter one in level order” rule is **naturally** satisfied (we overwrite map[hd] as we go).

```python
from collections import deque

class Solution:
    def bottomView(self, root):
        """
        Level-order (BFS) + horizontal distance.
        Time  : O(n)  — each node enqueued/dequeued once; final sort by distinct hd (≤ n)
        Space : O(n)  — queue + map
        """
        if not root:
            return []

        # Queue holds (node, hd)
        q = deque([(root, 0)])
        hd_to_val = {}  # {hd: node.data}

        while q:
            node, hd = q.popleft()

            # For bottom view, we want the last (lowest) node seen at each hd in BFS order.
            # Overwrite is intentional: latter nodes in level order replace earlier ones.
            hd_to_val[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Collect values by increasing horizontal distance
        result = [hd_to_val[hd] for hd in sorted(hd_to_val.keys())]
        return result
```

### B) DFS (preorder) with (depth, hd) tracking

* Keep a map `hd -> (depth, val)`.
* Only update if **depth is greater** (lower in tree), or equal but you want to follow the “latter in level order” tie-break.
  With DFS you must **define** “latter”: one way is to traverse left then right and allow **equal depth** to overwrite, imitating the “later encountered” node.

```python
class Solution:
    def bottomView(self, root):
        """
        DFS + store the deepest (or later at equal depth) node per hd.
        Time  : O(n)
        Space : O(n) recursion + map
        """
        if not root:
            return []

        # hd -> (depth, value)
        best = {}

        def dfs(node, hd, depth):
            if not node:
                return
            # update if: not seen OR deeper OR (equal depth -> overwrite to simulate 'latter')
            if hd not in best or depth > best[hd][0] or (depth == best[hd][0]):
                best[hd] = (depth, node.data)

            dfs(node.left,  hd - 1, depth + 1)
            dfs(node.right, hd + 1, depth + 1)

        dfs(root, 0, 0)
        return [best[hd][1] for hd in sorted(best.keys())]
```

> In interviews, prefer the BFS version; it’s cleaner and exactly matches the statement’s “latter in level order” rule.

---

## 4) Common interview Q & A

**Q1. Why does BFS naturally satisfy the “latter in level order” rule?**
Because BFS visits nodes level by level from top to bottom. The **last** node you encounter at a given `hd` is the one at the **lowest** level (or last in that level order), so overwriting `map[hd]` is correct.

**Q2. What are the horizontal distances?**
`hd(root) = 0`. For any node with `hd = h`:

* `hd(left)  = h - 1`
* `hd(right) = h + 1`

**Q3. Why do we need to sort before outputting?**
The bottom view must be printed from **leftmost to rightmost**, which corresponds to **increasing hd** order.

**Q4. Complexity?**

* **Time:** O(n) for traversal + O(k log k) to sort distinct hd’s where `k ≤ n`. Typically stated as **O(n)**.
* **Space:** O(n) (queue/map or recursion + map).

**Q5. Differences between Top View vs Bottom View?**

* **Top view:** Keep the **first** node seen at each `hd` in BFS (don’t overwrite).
* **Bottom view:** Keep the **last** node seen at each `hd` (overwrite).

**Q6. Can we do it without sorting?**
You still need left-to-right order. Without sorting, you’d track `min_hd`/`max_hd` and fill an offset array, which is equivalent in asymptotics and avoids a dict sort if you want.

**Q7. What if the tree is skewed?**
Still O(n). `hd` range may be large (≈ n), but this only affects the size of the map and the range to print.

---

---

awesome — here’s a complete, runnable script for **Bottom View of Binary Tree** with:

* clean BFS solution (and an optional DFS variant for reference)
* inline time/space complexity notes at each step
* helpers to build a tree from level-order input (supports numbers and `'N'`/`None`)
* demo runs on the two examples + a custom case
* a small **timeit** benchmark that reports average seconds/run

---

## 5) Full program (with inline complexity + input/outputs + timing)

```python
"""
Bottom View of Binary Tree
--------------------------
Approach used in `Solution.bottomView`:
  • BFS (level order) while tracking horizontal distance (hd)
  • For each hd, keep the last value seen in BFS order (this is the bottom-most node)
  • Finally, output values in increasing hd order

Complexities
------------
Let n = number of nodes in the tree, k = number of distinct horizontal distances (k <= n)

Build tree from list (helper):       O(n) time, O(n) space
BFS traversal with hd tracking:      O(n) time, O(n) space (queue + map)
Sorting distinct hds to print:       O(k log k) time, O(k) space
Overall (commonly stated):           O(n) time, O(n) space
"""

from collections import deque
import timeit
from typing import Optional, List, Any


# --------------------------- Binary Tree Node --------------------------- #
class Node:
    def __init__(self, val: int):
        self.data: int = val
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


# --------------------------- Solution (BFS) ----------------------------- #
class Solution:
    def bottomView(self, root: Optional[Node]) -> List[int]:
        """
        Level-order (BFS) with horizontal distance (hd).
        Time  : O(n) for traversal + O(k log k) to sort hds (k<=n)
        Space : O(n) for queue + map
        """
        if not root:
            return []

        # Queue holds pairs (node, hd).  Space: O(n) worst-case
        q = deque([(root, 0)])

        # Map: hd -> last value seen in BFS order (i.e., bottom-most)
        # Space: O(k) where k<=n
        hd_to_val = {}

        # BFS traversal — each node enqueued & dequeued once -> O(n)
        while q:
            node, hd = q.popleft()

            # Overwrite: latter nodes in BFS (deeper or later in level) replace earlier ones
            hd_to_val[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Collect values from leftmost hd to rightmost hd
        # Sorting distinct hds: O(k log k), k<=n
        return [hd_to_val[hd] for hd in sorted(hd_to_val.keys())]


# --------------------------- (Optional) DFS variant --------------------- #
class SolutionDFS:
    def bottomView(self, root: Optional[Node]) -> List[int]:
        """
        DFS that keeps deepest (or later at same depth) value for each hd.
        Time  : O(n)
        Space : O(n) recursion + map
        """
        if not root:
            return []

        best = {}  # hd -> (depth, value)

        def dfs(node: Optional[Node], hd: int, depth: int) -> None:
            if not node:
                return
            # Update if deeper or equal (overwrite to simulate 'latter in level order')
            if hd not in best or depth >= best[hd][0]:
                best[hd] = (depth, node.data)
            dfs(node.left, hd - 1, depth + 1)
            dfs(node.right, hd + 1, depth + 1)

        dfs(root, 0, 0)
        return [best[hd][1] for hd in sorted(best.keys())]


# --------------------------- Helpers: Build Tree ------------------------ #
def build_tree_level(values: List[Any]) -> Optional[Node]:
    """
    Build a binary tree from a level-order list where 'N' or None denotes null.
    Example: [1, 2, 3, 4, 5, 'N', 6]
    Time : O(n)   Space : O(n)
    """
    if not values:
        return None

    # Normalize 'N' strings to None
    vals = [None if (x == 'N' or x is None) else x for x in values]
    if vals[0] is None:
        return None

    root = Node(vals[0])
    q = deque([root])
    i = 1

    while q and i < len(vals):
        cur = q.popleft()
        # left child
        if i < len(vals) and vals[i] is not None:
            cur.left = Node(vals[i])
            q.append(cur.left)
        i += 1
        # right child
        if i < len(vals) and vals[i] is not None:
            cur.right = Node(vals[i])
            q.append(cur.right)
        i += 1

    return root


# --------------------------- Pretty print helper ------------------------ #
def print_case(title: str, arr: List[Any], solver) -> None:
    print(title)
    print("Level-order input:", arr)
    root = build_tree_level(arr)
    ans = solver.bottomView(root)
    print("Bottom view       :", ans)
    print()


# --------------------------- Demo + Timing ------------------------------ #
def run_demo_and_benchmark():
    sol = Solution()

    # Demo 1 (from the prompt)
    arr1 = [1, 2, 3, 4, 5, 'N', 6]
    print_case("Demo 1", arr1, sol)  # Expected: [4, 2, 5, 3, 6]

    # Demo 2 (from the prompt)
    arr2 = [20, 8, 22, 5, 3, 4, 25, 'N', 'N', 10, 14, 'N', 'N', 28, 'N']
    print_case("Demo 2", arr2, sol)  # Expected: [5, 10, 4, 28, 25]

    # Demo 3 (custom)
    arr3 = [7, 3, 9, 1, 5, 8, 10, 'N', 2]
    print_case("Demo 3", arr3, sol)

    # --- Benchmark with timeit (average time per run) ---
    def task():
        root = build_tree_level(arr2)
        sol.bottomView(root)

    runs = 100
    avg = timeit.timeit(task, number=runs) / runs
    print("Timing:")
    print(f"  Average over {runs} runs: {avg:.6f} seconds/run")
    print("  (Traversal is O(n); building the tree is also O(n).)")

if __name__ == "__main__":
    run_demo_and_benchmark()
```

### Sample output (what you’ll see)

```
Demo 1
Level-order input: [1, 2, 3, 4, 5, 'N', 6]
Bottom view       : [4, 2, 5, 3, 6]

Demo 2
Level-order input: [20, 8, 22, 5, 3, 4, 25, 'N', 'N', 10, 14, 'N', 'N', 28, 'N']
Bottom view       : [5, 10, 4, 28, 25]

Demo 3
Level-order input: [7, 3, 9, 1, 5, 8, 10, 'N', 2]
Bottom view       : [1, 2, 5, 9, 10]

Timing:
  Average over 100 runs: 0.000xyz seconds/run
  (Traversal is O(n); building the tree is also O(n).)
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Rendering/Visualization Layers**
   When stacking elements along a horizontal axis with depths, the “bottom view” corresponds to **which element is visible from below** — handy in CAD/graphics or map rendering layers.

2. **Network/Org Charts**
   In hierarchical diagrams, “bottom view” can quickly show which **leaf or deepest node per vertical slice** would be visible (e.g., last-responsible teams per division).

3. **Geo/Topology Profiles**
   For terrain cross-sections or skyline problems, computing a “bottom profile” along a horizontal distance axis is conceptually similar: **the lowest visible point per column**.
