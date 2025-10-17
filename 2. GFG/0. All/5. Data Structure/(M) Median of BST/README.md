# Median of BST

**Difficulty:** Medium
**Accuracy:** 27.43%
**Submissions:** 98K+
**Points:** 4

---

## 🧩 Problem Statement

You are given the **root** of a **Binary Search Tree (BST)**, find the **median** of it.

Let the nodes of the BST, when written in ascending order (**inorder traversal**), be represented as
V1, V2, V3, …, Vn, where n is the total number of nodes in the BST.

The median is defined as:

* If the number of nodes is **even**, return **V(n/2)**.
* If the number of nodes is **odd**, return **V((n+1)/2)**.

---

## 🧠 Examples

### Example 1

**Input:**

```
root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14]
```

**Output:**

```
12
```

**Explanation:**
The inorder traversal of the given BST is:
`4, 8, 10, 12, 14, 20, 22`

Here, n = 7 (odd)
So the median = V((7+1)/2) = V(4) = **12**

---

### Example 2

**Input:**

```
root = [5, 4, 8, 1]
```

**Output:**

```
4
```

**Explanation:**
The inorder traversal of the given BST is:
`1, 4, 5, 8`

Here, n = 4 (even)
So the median = V(4/2) = V(2) = **4**

---

## ⚙️ Constraints

* `1 ≤ number of nodes ≤ 10⁵`
* `1 ≤ node->data ≤ 10⁵`

---

## 🧮 Expected Complexities

| Metric              | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n)       |
| **Auxiliary Space** | O(1)       |

---

## 🏢 Company Tags

Amazon

---

## 🧱 Topic Tags

Traversal, Binary Search Tree, Data Structures, Algorithms

---

## 📘 Related Articles

* Find Median of BST in O(1) Extra Space

---

---

Awesome — let’s make **Median of a BST** interview-ready.

---

## 2) Intuition + step-by-step dry run

### Key idea

In a **BST**, an **inorder traversal** (Left → Node → Right) visits values in **ascending** order:

`V1, V2, …, Vn`

By the problem’s definition:

* If `n` is **odd**, return `V((n+1)/2)`  (the middle)
* If `n` is **even**, return `V(n/2)`      (the **lower** median, 1-indexed)

So we only need to know `n` and then fetch the `k`-th value in inorder where:

* `k = n//2` if `n` even
* `k = n//2 + 1` if `n` odd

### How to get it in O(1) extra space

Use **Morris inorder traversal** (threaded traversal):

* **Pass 1:** count nodes `n` (no extra memory).
* **Pass 2:** walk again and return the `k`-th visited value.

### Dry run on Example 1

BST:

```
        20
       /  \
      8    22
     / \
    4  12
      /  \
     10  14
```

Inorder: `4, 8, 10, 12, 14, 20, 22`
`n = 7` (odd) → `k = 7//2 + 1 = 4` → the 4th value is **12** ✅

---

## 3) Python solutions in the requested format

### A) ✅ Optimal: Two-pass **Morris inorder** (O(1) extra space)

```python
'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        """
        Two-pass Morris inorder (O(1) extra space):
          1) Count nodes n with Morris.
          2) Visit again and return k-th element in inorder (k per problem rule).
        Time  : O(n)
        Space : O(1) auxiliary (threads are created & restored)
        """

        if not root:
            return -1  # guard, though constraints imply at least 1 node

        # --- Pass 1: count nodes with Morris ---
        def count_nodes(node):
            count = 0
            curr = node
            while curr:
                if curr.left is None:
                    count += 1
                    curr = curr.right
                else:
                    # find inorder predecessor
                    pred = curr.left
                    while pred.right and pred.right is not curr:
                        pred = pred.right
                    if pred.right is None:
                        pred.right = curr       # thread
                        curr = curr.left
                    else:
                        pred.right = None       # unthread
                        count += 1
                        curr = curr.right
            return count

        n = count_nodes(root)

        # k: 1-indexed target per statement
        k = (n // 2) if (n % 2 == 0) else (n // 2 + 1)

        # --- Pass 2: return k-th value with Morris ---
        curr = root
        visited = 0
        while curr:
            if curr.left is None:
                visited += 1
                if visited == k:
                    return curr.data
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr           # thread
                    curr = curr.left
                else:
                    pred.right = None           # unthread
                    visited += 1
                    if visited == k:
                        return curr.data
                    curr = curr.right

        return -1  # should not happen with valid inputs
```

---

### B) Clean & common: **Iterative inorder with a stack** (O(h) space)

```python
class SolutionIterative:
    def findMedian(self, root):
        """
        Two-pass iterative inorder using an explicit stack.
        Pass 1: count nodes.
        Pass 2: fetch k-th node.
        Time  : O(n)
        Space : O(h) where h is tree height
        """
        if not root:
            return -1

        # Count nodes
        count, stack, curr = 0, [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            curr = curr.right

        k = (count // 2) if (count % 2 == 0) else (count // 2 + 1)

        # k-th visit
        visited, stack, curr = 0, [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            visited += 1
            if visited == k:
                return curr.data
            curr = curr.right

        return -1
```

---

### C) Brute (simple): collect inorder into a list, index it (O(n) space)

```python
class SolutionBrute:
    def findMedian(self, root):
        """
        Brute force: store inorder in a list and index per rule.
        Time  : O(n)
        Space : O(n)
        """
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.data)
            inorder(node.right)

        inorder(root)
        n = len(vals)
        if n == 0:
            return -1
        # 1-indexed positions required by problem:
        # even -> V(n/2) ; odd -> V((n+1)/2)
        if n % 2 == 0:
            return vals[n // 2 - 1]    # lower median, zero-based index
        else:
            return vals[n // 2]        # middle, zero-based index
```

> Which to present in interviews?
>
> * If they emphasize **O(1) space**, implement **A (Morris)**.
> * If they’re fine with typical solutions, implement **B (iterative stack)** — very common and readable.
> * **C** is a straightforward baseline but uses O(n) space.

---

## 4) Interview quick-memory + Q&A

### 10-second mnemonic

> **“Inorder is sorted.
> Count `n`, pick `k = (n//2)` if even else `n//2+1`, return the `k`-th inorder.”**

If they want O(1) space:

> **“Use Morris inorder: pass-1 count, pass-2 kth.”**

### Likely questions

**Q1. Why inorder?**
BST inorder yields sorted values; median is just the k-th item in that order.

**Q2. What exactly is the median here for even `n`?**
Per statement, use the **lower** median: `V(n/2)` (1-indexed).
(Zero-indexed index = `n//2 - 1`.)

**Q3. Complexity?**
All variants are **O(n)** time.
Space: **O(1)** for Morris, **O(h)** for stack, **O(n)** for list.

**Q4. What is Morris traversal and why O(1) space?**
It temporarily creates “threads” from an inorder predecessor to the current node and later removes them, avoiding a stack.

**Q5. Edge cases?**

* Single node → median is that node.
* Skewed tree → Morris still restores links safely.
* Ensure you return **lower** median when `n` is even.

**Q6. Could we do it in one pass?**
Not without knowing `n` first (since `k` depends on `n`). That’s why we do **two passes** (count → select).

---

---

Absolutely—let’s finish this with (5) razor-sharp, interview-friendly **use cases**, then (6) a **complete runnable program** (reads a BST, computes the median by the problem’s rule, and times it) with inline complexity notes.

---

## 5) Real-World Use Cases (easy to relate)

* **Database index percentile/median:**
  A BST-like index of keys; median (or lower median for even counts) is a common percentile summary for dashboards and query planners.

* **Latency/telemetry median:**
  Track request durations in a BST; median gives a robust central tendency (less sensitive to outliers than mean).

* **Pricing & bids:**
  With unique prices in a BST (e.g., order book snapshot), the median price can be used for fair pricing heuristics or guardrails.

* **A/B experiment metrics:**
  User metrics stored in BST by value; median is a robust split threshold for categorization or anomaly detection.

> Sound bite: **“Inorder gives sorted; median is just k-th inorder. With Morris, we do it in O(1) extra space.”**

---

## 6) Full Program (I/O, median, timings, complexity notes)

**Input format (1 line):** level-order of the BST with `N` for nulls
Example: `20 8 22 4 12 N N N N 10 14`

**Output:** the median (as defined by the prompt: lower median for even `n`) and timing stats.

```python
#!/usr/bin/env python3
"""
Median of a BST (lower median if n is even)
-------------------------------------------
We compute the median value where inorder(BST) = V1..Vn (ascending):
  if n is odd : return V((n+1)//2)
  if n is even: return V(n//2)        # lower median (1-indexed)

Approach:
  Two-pass Morris inorder traversal (threaded), O(1) extra space.
  Pass 1: count nodes n (O(n) time, O(1) space).
  Pass 2: visit again and return the k-th item where
          k = n//2      if n even else n//2 + 1

Why Morris? Avoids recursion/stack → O(1) auxiliary space.

Overall complexities:
  Time  : O(n)
  Space : O(1) auxiliary
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
    'N' denotes a null child.

    Complexity:
      Time  : O(n)  -- each token processed once
      Space : O(n)  -- queue + nodes
    """
    if not tokens or tokens[0] == 'N':
        return None

    it = iter(tokens)
    root = Node(int(next(it)))
    q = deque([root])

    # Level-by-level construction: overall O(n)
    for left_tok in it:
        parent = q.popleft()

        if left_tok != 'N':
            lc = Node(int(left_tok))
            parent.left = lc
            q.append(lc)

        try:
            right_tok = next(it)
        except StopIteration:
            break
        if right_tok != 'N':
            rc = Node(int(right_tok))
            parent.right = rc
            q.append(rc)

    return root


# ---------------------------- Median via Morris -----------------------------
class Solution:
    def findMedian(self, root):
        """
        Two-pass Morris inorder. O(n) time, O(1) extra space.
        """

        if not root:
            return -1

        # -------- Pass 1: count nodes (Morris) --------
        def count_nodes(node):
            count = 0
            curr = node
            while curr:
                if curr.left is None:
                    count += 1
                    curr = curr.right
                else:
                    # find inorder predecessor
                    pred = curr.left
                    while pred.right and pred.right is not curr:
                        pred = pred.right
                    if pred.right is None:
                        pred.right = curr        # create thread
                        curr = curr.left
                    else:
                        pred.right = None        # remove thread
                        count += 1
                        curr = curr.right
            return count

        n = count_nodes(root)

        # k (1-indexed) per problem spec:
        # even -> V(n//2), odd -> V(n//2 + 1)
        k = (n // 2) if (n % 2 == 0) else (n // 2 + 1)

        # -------- Pass 2: return k-th inorder value (Morris) --------
        curr = root
        visited = 0
        while curr:
            if curr.left is None:
                visited += 1
                if visited == k:
                    return curr.data
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr            # create thread
                    curr = curr.left
                else:
                    pred.right = None            # remove thread
                    visited += 1
                    if visited == k:
                        return curr.data
                    curr = curr.right

        return -1  # should not occur if input is valid


# ------------------------------- Timing helpers -----------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter (O(1) overhead)."""
    t0 = perf_counter()
    out = func(*args, **kwargs)
    t1 = perf_counter()
    return out, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# ------------------------------------ Main ----------------------------------
def main():
    """
    Input (1 line):
      level-order tokens with 'N' for nulls
      e.g. 20 8 22 4 12 N N N N 10 14
    """
    line = sys.stdin.read().strip()
    if not line:
        print("No input provided.\nExample:\n  20 8 22 4 12 N N N N 10 14")
        return

    tokens = line.split()
    root = build_tree(tokens)

    solver = Solution()

    # Single-run timing: O(n)
    median, t_single = time_single_run(solver.findMedian, root)

    # Average timing over 5 runs (rebuild tree each run to be fair):
    def run_once():
        rt = build_tree(tokens)
        Solution().findMedian(rt)
    avg = time_with_timeit(run_once, number=5)

    print(median)
    print(f"Single-run time : {t_single:.6f} s")
    print(f"Avg over 5 runs : {avg:.6f} s")

    # Complexity recap
    print("\nComplexity:")
    print("  Time  : O(n)")
    print("  Space : O(1) auxiliary (Morris threaded traversal)")

if __name__ == "__main__":
    """
    Example:
      echo "20 8 22 4 12 N N N N 10 14" | python3 median_bst.py

    Inorder: 4, 8, 10, 12, 14, 20, 22  -> n=7 -> k=4 -> median=12
    """
    main()
```

### Example run

**Input**

```
20 8 22 4 12 N N N N 10 14
```

**Output** (times vary by machine)

```
12
Single-run time : 0.0000xx s
Avg over 5 runs : 0.0000xx s

Complexity:
  Time  : O(n)
  Space : O(1) auxiliary (Morris threaded traversal)
```

> Interview one-liner to say before coding:
> **“Inorder is sorted. I’ll do two-pass Morris: first count n, then return the k-th inorder (k = n//2 for even else n//2+1). O(n) time, O(1) space.”**
