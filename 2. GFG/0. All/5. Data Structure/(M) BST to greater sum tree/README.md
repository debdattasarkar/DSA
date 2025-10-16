# BST to Greater Sum Tree

**Difficulty:** Medium
**Accuracy:** 66.73%
**Submissions:** 16K+
**Points:** 4

---

## 🧩 Problem Statement

Given the **root** of a **Binary Search Tree (BST)** with unique node values,
transform it into a **Greater Sum Tree**, where each node contains
the **sum of all nodes greater than that node** in the original BST.

---

## 🧠 Examples

### Example 1

**Input:**

```
root = [11, 2, 29, 1, 7, 15, 40, N, N, N, N, N, N, 35, N]
```

**Output:**

```
[119, 137, 75, 139, 130, 104, 0, N, N, N, N, N, N, 40, N]
```

**Explanation:**
Every node is replaced with the sum of nodes greater than itself.

### Visualization:

Original BST:

```
        11
       /  \
      2    29
     / \   / \
    1   7 15  40
             /
            35
```

Transformed Greater Sum Tree:

```
        119
       /   \
     137    75
     / \    / \
   139 130 104  0
                /
               40
```

---

### Example 2

**Input:**

```
root = [2, 1, 6, N, N, 3, 7]
```

**Output:**

```
[16, 18, 7, N, N, 13, 0]
```

**Explanation:**
Every node’s new value = sum of nodes greater than it.

### Visualization:

Original:

```
    2
   / \
  1   6
     / \
    3   7
```

Greater Sum Tree:

```
    16
   /  \
  18   7
      / \
     13  0
```

---

## ⚙️ Constraints

* `1 ≤ node->data ≤ 3 * 10⁴`
* `1 ≤ number of nodes ≤ 3 * 10⁴`

---

## 🧮 Expected Complexities

| Metric              | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n)       |
| **Auxiliary Space** | O(n)       |

---

## 🏢 Company Tags

Amazon, Microsoft

---

## 🧱 Topic Tags

Binary Search Tree, Tree, Data Structures

---

## 💬 Related Interview Experiences

* Amazon Interview Experience for SDE 3

---

## 📘 Related Articles

* Transform BST to Greater Sum Tree

---

---

awesome — let’s make **“BST → Greater Sum Tree”** (each node becomes the sum of all keys strictly greater than it) interview-ready.

---

## 2) Intuition + step-by-step dry run

### Core idea (reverse inorder with a running suffix sum)

* In a BST, **inorder** = ascending order.
* Therefore, **reverse inorder** (Right → Node → Left) visits keys from **largest → smallest**.
* Keep a running variable `greater_sum` (suffix sum of values we’ve already visited — i.e., all values **greater** than the current node).
* At each node:

  1. Traverse right subtree (collect all larger values first).
  2. Save old `node.data` in `original`.
  3. Replace `node.data` with `greater_sum`.
  4. Add `original` to `greater_sum`.
  5. Traverse left subtree.

This yields exactly “sum of all nodes greater than current”.

### Dry run on Example 2

Original BST:

```
    2
   / \
  1   6
     / \
    3   7
```

We do Reverse Inorder: 7 → 6 → 3 → 2 → 1

* Start `greater_sum = 0`.

1. Visit 7

   * Node gets current `greater_sum` = 0 → node(7)=0
   * Update `greater_sum += 7` → 7

2. Back to 6

   * Node gets 7 → node(6)=7
   * `greater_sum += 6` → 13

3. Go left to 3

   * Node gets 13 → node(3)=13
   * `greater_sum += 3` → 16

4. Back to 2

   * Node gets 16 → node(2)=16
   * `greater_sum += 2` → 18

5. Left to 1

   * Node gets 18 → node(1)=18
   * `greater_sum += 1` → 19

Transformed tree:

```
    16
   /  \
  18   7
      / \
     13  0
```

Matches the example output.

---

## 3) Python solutions (clean + alternatives)

All versions fit your signature.

### A) Recursive Reverse Inorder (most expected; O(n) time, O(h) stack)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        """
        Reverse inorder (Right -> Node -> Left) with a running suffix sum.
        For each node: new_value = sum of strictly greater keys.
        Time  : O(n)   -- each node visited once
        Space : O(h)   -- recursion stack, h = tree height
        """
        greater_sum = 0  # sum of all nodes visited so far (greater than current)

        def rev_inorder(node):
            nonlocal greater_sum
            if not node:
                return
            # Visit larger keys first
            rev_inorder(node.right)

            # Update this node to sum of greater keys
            original = node.data
            node.data = greater_sum
            greater_sum += original

            # Then smaller keys
            rev_inorder(node.left)

        rev_inorder(root)
        return root
```

### B) Iterative Reverse Inorder (explicit stack; avoids recursion depth)

```python
class SolutionIter:
    def transformTree(self, root):
        """
        Iterative reverse inorder using a stack.
        Time  : O(n)
        Space : O(h)
        """
        stack = []
        curr = root
        greater_sum = 0

        while curr or stack:
            # go as far right as possible (largest first)
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            original = curr.data
            curr.data = greater_sum
            greater_sum += original

            # move to left subtree (smaller values)
            curr = curr.left

        return root
```

### C) Morris Reverse Inorder (O(1) extra space; threaded traversal)

> Only use if interviewer asks for **O(1) extra space**. Code is a bit longer; logic identical.

```python
class SolutionMorris:
    def transformTree(self, root):
        """
        Morris reverse inorder (Right-threaded) => O(1) extra space.
        Time  : O(n)
        Space : O(1) extra (modifies & restores pointers)
        """
        curr = root
        greater_sum = 0

        while curr:
            if not curr.right:
                original = curr.data
                curr.data = greater_sum
                greater_sum += original
                curr = curr.left
            else:
                # Find inorder successor in reverse order: leftmost of right chain? No:
                # For reverse inorder, find the LEFTMOST node of curr.right? Actually we want
                # the "thread" target: leftmost along .left chain starting from curr.right? No.
                # We need the node that would visit curr next when going Right -> Node -> Left:
                # That's the leftmost path from curr.right.
                succ = curr.right
                while succ.left and succ.left is not curr:
                    succ = succ.left

                if not succ.left:
                    succ.left = curr        # create thread back to curr
                    curr = curr.right
                else:
                    succ.left = None        # remove thread; now "visit" curr
                    original = curr.data
                    curr.data = greater_sum
                    greater_sum += original
                    curr = curr.left

        return root
```

> In interviews, prefer **A** (recursive) or **B** (iterative). Mention **Morris** as the O(1) extra space option if prompted.

---

## 4) 60-second interview recall + Q&A

### 10-second mnemonic

> **“Reverse inorder + running sum.”**
> Visit **Right → Node → Left**, set `node = sum_so_far`, then `sum += original`.

### What to say before coding

* “Because BST inorder is sorted ascending, I’ll do a **reverse inorder** to walk from **largest to smallest**.
  I’ll maintain `greater_sum` and for each node set it to `greater_sum`, then add its original value to `greater_sum`.
  That yields the sum of strictly greater keys.
  Complexity: **O(n)** time, **O(h)** space (or **O(1)** with Morris).”

### Common interviewer questions

**Q1. Why reverse inorder?**
It visits nodes from largest to smallest, so a running sum naturally captures “all greater keys” at each step.

**Q2. Strictly greater or greater-or-equal?**
Here it’s **strictly greater**. We assign current node with the sum accumulated **before** adding its original value.

**Q3. Complexity?**
`O(n)` time, `O(h)` auxiliary (stack or recursion), `O(1)` extra with Morris.

**Q4. Will duplicates break it?**
The prompt says **unique values**. If duplicates existed and you wanted “strictly greater,” this still works; for “greater-or-equal” you’d switch the assignment/add order.

**Q5. Can we do it inplace?**
Yes — the algorithm mutates nodes in place.

**Q6. How to test quickly?**

* Single node: becomes 0.
* All right-skewed: becomes suffix sums shifting right.
* All left-skewed: ensure traversal still updates correctly.

---

### Tiny helper for remembering the update order

* **“Write then add”**

  * write `node.data = greater_sum`
  * then `greater_sum += original`
    This enforces **strictly greater**.

---

---

awesome — here are (5) crisp, interview-friendly **real-world use cases**, then (6) a **complete runnable Python program** (reads input, transforms BST to Greater Sum Tree, prints result, and times the run) with **inline complexity notes**.

---

## 5) Real-World Use Cases (memorable + relatable)

* **Tax/royalty brackets:**
  A BST keyed by income thresholds. Converting to a greater-sum tree gives, at each threshold, the **total tax/royalty above** that threshold—handy for “how much more beyond here?” analytics.

* **E-commerce price ladder:**
  BST of unique prices. After conversion, each node holds **sum of revenue potential from all items priced higher**—useful for “price uplift” simulations.

* **Leaderboard / score analytics:**
  BST by score. Greater-sum value at each score = **sum of all higher scores**; enables quick “how far behind top players are we in total points?”.

* **Inventory reorder planning:**
  BST keyed by reorder priority. Greater-sum value at each priority = **total units in higher urgency buckets**, useful for “remaining urgency above this level”.

* **Cumulative tail risk:**
  BST of risk thresholds (VaR buckets). Node becomes **sum of risks beyond this threshold**—a tail-risk profile at every point.

> Sound bite: **“Reverse-inorder + running suffix sum gives ‘how much is above me’ at every key — a classic tail-sum transform.”**

---

## 6) Full Program (I/O, transform, print, and time)

**Input format (2 lines):**

* Line 1: level-order of the BST, space-separated, `'N'` for nulls
  e.g. `11 2 29 1 7 15 40 N N N N N N 35 N`
* Line 2: (nothing else needed; present to match your multi-line pattern; you can leave it blank or omit — program handles both)

**Output:**

* Level-order of the **Greater Sum Tree** (trailing `N`s trimmed)
* Single-run timing and average timing over 5 runs

```python
#!/usr/bin/env python3
"""
BST -> Greater Sum Tree
-----------------------
Each node becomes the sum of all keys strictly greater than itself.

Approach (interview-standard):
  Reverse inorder traversal (Right -> Node -> Left) with a running suffix sum.
  At each node:
    new_value = suffix_sum_so_far
    suffix_sum_so_far += original_value

Complexities:
  Time  : O(n)   -- each node visited once
  Space : O(h)   -- recursion stack (h = height; O(n) worst, O(log n) if balanced)
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
    root = Node(int(next(it)))      # O(1)
    q = deque([root])               # O(1)

    # Level-by-level expansion -> overall O(n)
    for left_tok in it:
        parent = q.popleft()        # amortized O(1)

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
    def transformTree(self, root):
        """
        Reverse inorder with a running suffix sum.
        For each node: new_value = sum of strictly greater keys.

        Complexity:
          Time  : O(n)  -- visit each node once
          Space : O(h)  -- recursion stack
        """
        suffix_sum = 0  # sum of all nodes visited so far (those greater than current)

        def rev_inorder(node):
            nonlocal suffix_sum
            if not node:
                return

            # 1) Visit larger keys first: O(size of right))
            rev_inorder(node.right)

            # 2) Replace node with sum of greater keys: O(1)
            original = node.data
            node.data = suffix_sum     # strictly greater
            suffix_sum += original     # include this node for smaller ones

            # 3) Then smaller keys: O(size of left)
            rev_inorder(node.left)

        rev_inorder(root)
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
    Input:
      Line 1: level-order of BST ('N' for nulls)
              e.g. 11 2 29 1 7 15 40 N N N N N N 35 N
      Line 2: (optional/blank)
    """
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        print("No input provided.\nExample:\n  11 2 29 1 7 15 40 N N N N N N 35 N")
        return

    tokens = lines[0].split()

    # Build tree: O(n)
    root = build_tree(tokens)

    solver = Solution()

    # Single run timing: O(n)
    transformed_root, t_single = time_single_run(solver.transformTree, root)
    output_list = serialize_level_order(transformed_root)  # O(n)

    # timeit average: rebuild + transform per run (so we time full algorithm)
    def run_once():
        rt = build_tree(tokens)
        Solution().transformTree(rt)
    avg_time = time_with_timeit(run_once, number=5)

    # Output
    print("Greater Sum Tree (level-order):", output_list if output_list else [])
    print(f"Single-run time : {t_single:.6f} s")
    print(f"Avg over 5 runs : {avg_time:.6f} s")

    # Complexity recap
    print("\nComplexity Summary:")
    print("  Time  : O(n)")
    print("  Space : O(h) recursion (worst O(n) if skewed; ~O(log n) if balanced)")

if __name__ == "__main__":
    """
    Example:
      echo -e "2 1 6 N N 3 7" | python3 bst_to_greater_sum_tree.py
    Expected:
      Greater Sum Tree (level-order): ['16', '18', '7', 'N', 'N', '13', '0']
    """
    main()
```

### Example run

**Input**

```
2 1 6 N N 3 7
```

**Output** (timings vary)

```
Greater Sum Tree (level-order): ['16', '18', '7', 'N', 'N', '13', '0']
Single-run time : 0.0000xx s
Avg over 5 runs : 0.0000xx s

Complexity Summary:
  Time  : O(n)
  Space : O(h) recursion (worst O(n) if skewed; ~O(log n) if balanced)
```

> Interview one-liner you can say before coding:
> **“I’ll do a reverse inorder (Right→Node→Left) with a running suffix sum.
> Set node to the sum so far, then add its original value.
> That yields the sum of strictly greater keys. O(n) time, O(h) space.”**

