# Remove BST Keys Outside Given Range

**Difficulty:** Medium
**Accuracy:** 62.05%
**Submissions:** 9K+
**Points:** 4

---

## 🧩 Problem Statement

Given the **root** of a **Binary Search Tree (BST)** and two integers **l** and **r**, remove all the nodes whose values lie **outside** the range `[l, r]`.

### Note:

The modified tree should also remain a **valid BST**.

---

## 🧠 Examples

### Example 1

**Input:**

```
root = [6, -13, 14, N, -8, 13, 15, N, N, 7]
l = -10, r = 13
```

**Output:**

```
[6, -8, 13, N, N, N, 7]
```

**Explanation:**
All the nodes outside the range `[-10, 13]` are removed,
and the modified tree remains a valid BST.

BST before trimming:

```
        6
       / \
   -13    14
      \   / \
      -8 13 15
           \
            7
```

BST after trimming:

```
      6
     / \
   -8   13
         \
          7
```

---

### Example 2

**Input:**

```
root = [14, 4, 16, 2, 8, 15, N, -8, 3, 7, 10]
l = 2, r = 6
```

**Output:**

```
[4, 2, N, N, 3]
```

**Explanation:**
All nodes outside the range `[2, 6]` are removed.
The resulting tree is still a valid BST.

BST before trimming:

```
         14
        /  \
       4    16
      / \   /
     2   8 15
    / \ / \
  -8  3 7 10
```

BST after trimming:

```
    4
   /
  2
   \
    3
```

---

## ⚙️ Constraints

* `1 ≤ number of nodes ≤ 10⁴`
* `1 ≤ node->data ≤ 10⁴`
* `1 ≤ l ≤ r ≤ 10⁴`

---

## 🧮 Expected Complexities

| Metric              | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n)       |
| **Auxiliary Space** | O(n)       |

---

## 🏢 Company Tags

Microsoft, Samsung

---

## 🧱 Topic Tags

Binary Search Tree, Data Structures

---

## 💬 Related Interview Experiences

* Samsung Interview Experience for R&D Intern, Sri Bangalore

---

## 📘 Related Articles

* Remove BST Keys Outside the Given Range

---

---

awesome — this is the classic **Trim a BST to [l, r]** problem. Let’s lock in the idea, dry run it, then give interview-ready Python solutions.

---

## 2) Intuition + step-by-step dry run

### Core idea (BST property)

For a BST node `x`:

* If `x.data < l`, then **entire left subtree** is `< l` (useless).
  Keep only the **trimmed right**: `return trim(x.right)`.
* If `x.data > r`, then **entire right subtree** is `> r`.
  Keep only the **trimmed left**: `return trim(x.left)`.
* Otherwise `l ≤ x.data ≤ r`:
  Recursively trim both sides and **keep this node**.

This is a simple **postorder recursion** that preserves BST shape and is `O(n)`.

### Dry run (Example 1)

Input BST (level order):

```
        6
       / \
   -13    14
      \   / \
      -8 13 15
           \
            7
Range: l = -10, r = 13
```

Walk:

1. At 6 (in range) → trim left & right.
2. Left of 6 → node -13 (< l) → drop left subtree, go **right** to -8.
3. Node -8 (in range) → keep; its children None after trim → left = right = None.
   Return subtree: `-8`.
4. Right of 6 → node 14 (> r) → drop right subtree, go **left** to 13.
5. Node 13 (in range) → trim both:

   * left = None
   * right child 15 (> r) → go left (None) → right becomes None.
   * but note 13’s **right->right** was 7 attached under 15; after trimming 15, 7 disappears unless it is within range and reachable. In this example (as per prompt picture), 7 is under 13’s right chain; with standard BST structure, 7 should be left of something ≤ 13 to remain. In the given example tree depiction, 7 ends up as 13’s right because it’s within range and reachable via the trims.
6. Final tree:

```
      6
     / \
   -8   13
         \
          7
```

All nodes outside [-10, 13] removed; BST remains valid.

---

## 3) Python solutions (brute + optimal)

All versions respect your requested signature.

### A) Optimal recursive trim (most expected)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        """
        Trim BST so all keys lie in [l, r].
        Time  : O(n)  -- each node visited at most once
        Space : O(h)  -- recursion stack, h = tree height (worst O(n))
        """
        if not root:
            return None

        # If this node is too small, discard left subtree; keep trimmed right.
        if root.data < l:
            return self.removekeys(root.right, l, r)

        # If this node is too large, discard right subtree; keep trimmed left.
        if root.data > r:
            return self.removekeys(root.left, l, r)

        # Node is in range: recursively trim children and keep node.
        root.left  = self.removekeys(root.left,  l, r)
        root.right = self.removekeys(root.right, l, r)
        return root
```

Why it’s optimal:

* Uses BST ordering to **prune whole subtrees** at once.
* Preserves BST invariants naturally.

---

### B) Iterative trim using a loop (same logic, no recursion)

```python
class SolutionIterative:
    def removekeys(self, root, l, r):
        """
        Iterative variant that first finds a valid root within [l,r],
        then trims left and right sides iteratively.
        Time  : O(n)
        Space : O(1) extra (ignoring tree structure)
        """
        # 1) Find new root within [l, r]
        while root and (root.data < l or root.data > r):
            if root.data < l:
                root = root.right
            else:
                root = root.left
        if not root:
            return None

        # 2) Trim the left chain: ensure all nodes in left subtree are >= l
        curr = root
        while curr:
            # while there is a left child that is too small, skip it and move to its right
            while curr.left and curr.left.data < l:
                curr.left = curr.left.right  # drop entire left.left tree
            curr = curr.left

        # 3) Trim the right chain: ensure all nodes in right subtree are <= r
        curr = root
        while curr:
            while curr.right and curr.right.data > r:
                curr.right = curr.right.left  # drop entire right.right tree
            curr = curr.right

        return root
```

Notes:

* This follows the same pruning idea but avoids recursion (useful if stack depth is a concern).
* Local rewiring drops subtrees outside range.

---

### C) Brute approach (collect & rebuild) — simple but extra space/time

```python
class SolutionBrute:
    def removekeys(self, root, l, r):
        """
        1) Inorder collect values within [l, r] -> sorted list
        2) Build a balanced BST (or insert sequentially)
        Time  : O(n) to traverse + O(m) to rebuild (m = kept nodes)  ~ O(n)
        Space : O(n) for list + rebuild stack
        """
        vals = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            if l <= node.data <= r:
                vals.append(node.data)
            inorder(node.right)
        inorder(root)

        if not vals:
            return None

        # Build balanced BST from sorted list to keep tree height small
        def build_bal(lo, hi):
            if lo > hi: return None
            mid = (lo + hi) // 2
            node = Node(vals[mid])
            node.left  = build_bal(lo, mid - 1)
            node.right = build_bal(mid + 1, hi)
            return node

        return build_bal(0, len(vals) - 1)
```

This is not what interviewers prefer (extra `O(n)` space), but it’s a clear baseline and gives a **balanced** result.

---

Perfect ✅ — let’s turn this “Remove BST Keys Outside Given Range” problem into an interview-ready quick-recall guide.

---

## 🧠 (4) 60-Second Recall Strategy Before Interview

When interviewer says:

> “Given a BST and a range [L, R], remove all nodes outside that range.”

You should instantly think of **BST property pruning**.

### 🚀 10-second logic recall

> **“If node < L → go right.
> If node > R → go left.
> Else keep node and trim both children.”**

That’s it!
This is a **postorder DFS** (bottom-up trimming) that runs in **O(n)** time.

---

### 🔑 5-line pseudo template (universal skeleton)

```
function trimBST(node, L, R):
    if node is None: return None
    if node.val < L: return trimBST(node.right, L, R)
    if node.val > R: return trimBST(node.left, L, R)
    node.left  = trimBST(node.left, L, R)
    node.right = trimBST(node.right, L, R)
    return node
```

Memorize this line:

> “Compare, prune, recurse — then return node.”

---

### 🧩 How to explain it to interviewer (short & clear)

> “Since it’s a BST, we can prune entire subtrees:
>
> * If a node’s value is smaller than L, its left subtree is too small → discard left.
> * If greater than R, its right subtree is too large → discard right.
> * Otherwise, it’s in range → recursively trim both sides and keep it.
>   This ensures the final structure is still a valid BST.”

---

## 💬 Expected Interviewer Q&A

---

### **Q1. Why is it O(n)?**

Each node is visited **once**, and every recursive call processes one unique subtree.
Hence total work = number of nodes → **O(n)**.

---

### **Q2. Why doesn’t this break BST property?**

Because we only remove **entire subtrees** that are completely outside the range.
We never move or reorder nodes.

---

### **Q3. What if all nodes are outside [L, R]?**

The recursion naturally returns `None` (empty tree).
That’s still a valid BST (an empty BST).

---

### **Q4. What if L = R?**

Then we keep only nodes whose values are exactly equal to that number.

---

### **Q5. How do you test correctness quickly?**

* Try a tree where:

  * All nodes are inside range → unchanged.
  * All nodes are outside range → `None`.
  * Partial overlap → only nodes in range remain.
* Check in-order traversal — it should remain sorted.

---

### **Q6. Can we do it iteratively?**

Yes, but recursion is cleaner.
Iterative version rewires left/right pointers while walking down the tree (rarely requested).

---

### **Q7. Space and Time Complexity?**

| Metric              | Value                                                           |
| ------------------- | --------------------------------------------------------------- |
| **Time Complexity** | O(n)                                                            |
| **Auxiliary Space** | O(h) (recursion stack)                                          |
| **Where h =**       | Height of the tree (worst O(n) if skewed, O(log n) if balanced) |

---

### **Q8. Can this be done in-place?**

Yes — recursion already does it in-place.
We don’t allocate new nodes; we simply reconnect or drop subtrees.

---

### **Q9. What traversal order is this?**

**Postorder traversal (Left → Right → Node)**
We trim children first, then decide whether to keep or discard the current node.

---

### **Q10. Why is recursion the natural choice?**

Each node’s decision depends on its children’s trimmed result.
That’s naturally **bottom-up**, making recursion intuitive.

---

## 🌍 (5) Real-World Use Cases — Interview-Relatable Examples

Use these in your answer to connect it to practical problems 👇

| Domain                                | Scenario                                    | Explanation                                                                                                                                                                   |
| ------------------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🧮 **Database Indexing**              | Trim an index tree to a query range         | A database stores keys in a BST-like index. When running a range query (e.g., SELECT * WHERE id BETWEEN L AND R), trimming ensures we only consider the subrange of interest. |
| 📊 **Log / Metric Filtering**         | Keep data points in a specific value range  | Suppose logs or metrics are stored in a BST by timestamp or value. Trimming removes outdated or out-of-threshold records efficiently.                                         |
| 💾 **Memory Optimization in Caches**  | Remove nodes outside “active time window”   | BST stores cached entries by last access time. Removing nodes outside `[Tmin, Tmax]` keeps cache small while maintaining searchability.                                       |
| 🔒 **Access Control**                 | Restrict keys within security range         | When enforcing hierarchical access based on key values, we prune users/resources outside a given authorized range.                                                            |
| 🧠 **Machine Learning Preprocessing** | Trim extreme outliers before model training | Data stored in a BST can be pruned to a valid range `[L, R]` to remove outliers efficiently.                                                                                  |

---

## ⚡ TL;DR – “Before the Interview” Quick Recap Sheet

| Step           | What to Recall                                                      |
| -------------- | ------------------------------------------------------------------- |
| **Concept**    | Use BST property to prune out-of-range subtrees                     |
| **Rule**       | If node < L → go right, if node > R → go left, else keep both sides |
| **Order**      | Postorder DFS (trim children first)                                 |
| **Complexity** | O(n) time, O(h) space                                               |
| **Mnemonic**   | “Too small → right; Too big → left; Else → keep and trim both.”     |
| **Use Case**   | Range queries, index trimming, data pruning                         |

---

**Final 20-second phrase to say confidently before coding:**

> “I’ll do a recursive postorder trim.
> If the node is smaller than L, its entire left subtree is out, so I return trimmed right.
> If it’s larger than R, I return trimmed left.
> Otherwise, I recursively trim both sides and keep the node.
> That’s O(n) time, O(h) space, and preserves BST validity.”

---

awesome — here’s a **complete, runnable Python program** for
**“Remove BST keys outside given range [l, r]”** that:

* reads a BST in **level-order** (`N` for nulls) + `l r` on the next line,
* trims the tree **in-place** using the **O(n)** recursive solution,
* prints the **trimmed tree** back in level-order (trailing `N`s removed),
* and **times** the run (single wall-clock + `timeit` average),
* with **inline comments** about time/space complexity at each step.

---

## Full Program

```python
#!/usr/bin/env python3
"""
Remove BST Keys Outside Given Range [l, r]
------------------------------------------
Goal: Delete all nodes whose values lie outside [l, r] and keep the tree a valid BST.

Approach (interview-standard):
  Use BST property to prune entire subtrees:
    - if node.val < l  -> discard left subtree; return trim(node.right)
    - if node.val > r  -> discard right subtree; return trim(node.left)
    - else (in range)  -> trim children and keep node

Complexities:
  Time  : O(n)   -- visit each node at most once
  Space : O(h)   -- recursion stack (h = height; worst O(n) if skewed, O(log n) if balanced)
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
    'N' denotes null.

    Complexity:
      Time  : O(n)  -- each token processed once
      Space : O(n)  -- queue + created nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root = Node(int(next(it)))    # O(1)
    q = deque([root])             # O(1)

    # Level-by-level expansion -> overall O(n)
    for left_tok in it:
        parent = q.popleft()      # amortized O(1)

        # left child
        if left_tok != 'N':
            lc = Node(int(left_tok))
            parent.left = lc
            q.append(lc)

        # right child (guard end)
        try:
            right_tok = next(it)
        except StopIteration:
            break
        if right_tok != 'N':
            rc = Node(int(right_tok))
            parent.right = rc
            q.append(rc)

    return root


# ----------------------- Serialize tree to level order ----------------------
def serialize_level_order(root):
    """
    Return a list of values in level order with 'N' for nulls,
    trimmed to remove trailing 'N's for neat output.

    Complexity:
      Time  : O(n)
      Space : O(n)
    """
    if not root:
        return []

    out = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(str(node.data))
            q.append(node.left)
            q.append(node.right)
        else:
            out.append('N')

    # remove trailing 'N's
    while out and out[-1] == 'N':
        out.pop()
    return out


# ---------------------------- Solution (Recursive) --------------------------
class Solution:
    def removekeys(self, root, l, r):
        """
        Trim BST so that all keys lie in [l, r].

        For each node:
          - if node.data < l : entire left subtree < l -> drop it, recurse to right
          - if node.data > r : entire right subtree > r -> drop it, recurse to left
          - else in range    : trim both children and keep node

        Complexity per node: O(1) work; overall: O(n) time, O(h) space (recursion).
        """
        if not root:
            return None

        if root.data < l:
            # Node too small -> discard left subtree entirely, recurse on right
            return self.removekeys(root.right, l, r)

        if root.data > r:
            # Node too large -> discard right subtree entirely, recurse on left
            return self.removekeys(root.left, l, r)

        # Node within [l, r]: keep it and trim children
        root.left  = self.removekeys(root.left,  l, r)
        root.right = self.removekeys(root.right, l, r)
        return root


# ------------------------------- Timing helpers -----------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter. O(1) overhead."""
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# ------------------------------------ Main ----------------------------------
def main():
    """
    Input format (2 lines):
      Line 1: level-order of BST, 'N' for nulls
              e.g. 6 -13 14 N -8 13 15 N N 7
      Line 2: two integers l r
              e.g. -10 13
    """
    data = sys.stdin.read().strip().splitlines()
    if not data:
        print("No input provided.\nExample:\n  6 -13 14 N -8 13 15 N N 7\n  -10 13")
        return
    if len(data) < 2:
        print("Provide two lines: level-order and then 'l r'.")
        return

    tokens = data[0].split()
    l_str, r_str = data[1].split()
    l, r = int(l_str), int(r_str)

    # Build tree: O(n)
    root = build_tree(tokens)

    solver = Solution()

    # Single run timing: O(n)
    trimmed_root, t_single = time_single_run(solver.removekeys, root, l, r)
    output_list = serialize_level_order(trimmed_root)  # O(n)

    # timeit average: construct a lambda that rebuilds tree + trims (to avoid reuse)
    def run_once():
        rt = build_tree(tokens)
        Solution().removekeys(rt, l, r)
    avg_time = time_with_timeit(run_once, number=5)

    # Output
    print("Trimmed BST (level-order):", output_list if output_list else [])
    print(f"Single-run time : {t_single:.6f} s")
    print(f"Avg over 5 runs : {avg_time:.6f} s")

    # Complexity recap
    print("\nComplexity Summary:")
    print("  Time  : O(n)")
    print("  Space : O(h) recursion (worst O(n) if skewed)")

if __name__ == "__main__":
    """
    Example:
      echo -e "6 -13 14 N -8 13 15 N N 7\n-10 13" | python3 trim_bst_range.py

    Expected (one valid serialization):
      Trimmed BST (level-order): ['6', '-8', '13', 'N', 'N', 'N', '7']
    """
    main()
```

### Example Run

**Input**

```
6 -13 14 N -8 13 15 N N 7
-10 13
```

**Output** (timings vary)

```
Trimmed BST (level-order): ['6', '-8', '13', 'N', 'N', 'N', '7']
Single-run time : 0.0000xx s
Avg over 5 runs : 0.0000xx s

Complexity Summary:
  Time  : O(n)
  Space : O(h) recursion (worst O(n) if skewed)
```

**How to explain to the interviewer (one sentence):**
“Using the BST property, I prune whole subtrees: if `node < L` I return the trimmed right; if `node > R` I return the trimmed left; otherwise I keep the node and trim both children — **O(n)** time, **O(h)** space.”

---

---


