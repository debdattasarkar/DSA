
---

# 🧠 Postorder Traversal

**Difficulty:** Easy
**Accuracy:** 74.96%
**Submissions:** 132K+
**Points:** 2
**Average Time:** 15m

---

## 📘 Problem Statement

Given the **root** of a Binary Tree, your task is to return its **Postorder Traversal**.

### 🔍 Note

A **postorder traversal** first visits:

1. The **left child** (including its entire subtree),
2. Then the **right child** (including its entire subtree),
3. And finally visits the **node itself**.

---

## 🧩 Examples

### Example 1:

#### **Input:**

```
root = [19, 10, 8, 11, 13]
```

Tree representation:

```
       19
      /  \
    10    8
   /  \
 11   13
```

#### **Output:**

```
[11, 13, 10, 8, 19]
```

#### **Explanation:**

The postorder traversal of the given binary tree is:
→ Visit left subtree of 19 → [11, 13, 10]
→ Visit right subtree → [8]
→ Visit root → [19]
So final order: **[11, 13, 10, 8, 19]**

---

### Example 2:

#### **Input:**

```
root = [11, 15, N, 7]
```

Tree representation:

```
    11
     \
     15
      \
       7
```

#### **Output:**

```
[7, 15, 11]
```

#### **Explanation:**

The postorder traversal of the given binary tree is:
Visit left subtree (None), visit right subtree (7,15), then visit root (11).
Hence the output is **[7, 15, 11]**.

---

## 📏 Constraints

* ( 1 \leq \text{number of nodes} \leq 3 \times 10^4 )
* ( 0 \leq \text{node->data} \leq 10^5 )

---

## ⚙️ Expected Complexities

* **Time Complexity:** O(N)
  (Each node is visited exactly once)
* **Auxiliary Space:** O(1)
  (If recursion stack is not counted; otherwise O(H), where H is the tree height)

---

## 🏢 Company Tags

* Morgan Stanley
* Snapdeal
* Walmart

---

## 🏷️ Topic Tags

* Tree
* Data Structures

---

## 📚 Related Articles

* [Postorder Traversal Of Binary Tree](https://www.geeksforgeeks.org/postorder-traversal-of-binary-tree/)

---

---

here we go! we’ll nail the idea, walk a dry-run, then give the interview-ready solutions (recursive + iterative), and finish with quick interviewer Q&A.

---

# 2) Explanation (what & why)

**Postorder traversal** of a binary tree visits nodes in the order:

> **Left subtree → Right subtree → Node**

This is a depth-first traversal. It’s naturally implemented with recursion (because each node’s work depends on finishing both subtrees first). Iteratively, we simulate the call stack with our own stack(s).

### Key points

* Output is a list of node `.data` in postorder.
* Empty tree ⇒ return `[]`.
* Time is **O(N)** (every node visited once).
* Extra space is **O(H)** where `H` is the tree height (recursion stack or explicit stack). In the worst case (skewed tree), `H = N`; in a balanced tree, `H = log N`.

---

## 2.1 Step-by-step dry run (on Example 1)

Tree:

```
       19
      /  \
    10    8
   /  \
 11   13
```

Goal: postorder → `[11, 13, 10, 8, 19]`

### Recursive view

1. `post(19)`
   → `post(10)`
   → `post(11)` → left=None, right=None ⇒ output `[11]`
   → `post(13)` → output `[11, 13]`
   → now visit 10 ⇒ `[11, 13, 10]`
   → back to 19 → `post(8)` ⇒ `[11, 13, 10, 8]`
   → visit 19 ⇒ `[11, 13, 10, 8, 19]`

### Iterative (two-stack) intuition

* Push root to `s1`.
* Pop from `s1` to `s2`; push its children to `s1`.
* Repeat until `s1` empty.
* Then pop `s2` to result (which yields Left-Right-Root order).
  For this tree, `s2` ends as `[19, 8, 10, 13, 11]` (top on the right), so popping gives `[11, 13, 10, 8, 19]`.

---

# 3) Optimized Python solutions (interview-ready)

Both versions return a **list** of values.

### A) Recursive DFS (cleanest & most expected)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        """
        Recursive Postorder: Left -> Right -> Node
        Time:  O(N)  (each node visited exactly once)
        Space: O(H)  (call stack height; H is tree height)
        """
        ans = []

        def dfs(node):
            if not node:               # base: empty subtree
                return
            dfs(node.left)             # 1) left subtree
            dfs(node.right)            # 2) right subtree
            ans.append(node.data)      # 3) process node

        dfs(root)
        return ans
```

### B) Iterative using **two stacks** (easy to reason about)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        """
        Iterative Postorder using two stacks.
        s1 collects nodes root->...; s2 reverses to postorder.
        Time:  O(N)
        Space: O(N) in worst case (stacks store up to N nodes)
        """
        if not root:
            return []

        s1, s2 = [root], []
        while s1:
            node = s1.pop()
            s2.append(node)
            # push children to s1 (left first so that right is processed before left in s2)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        # s2 now has nodes in Root->Right->Left order; reverse pop gives Left->Right->Root
        return [n.data for n in reversed(s2)]
```

### C) Iterative using **one stack** (common interview twist)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        """
        Iterative Postorder using one stack and a 'last visited' pointer.
        Time:  O(N)
        Space: O(H)
        """
        ans = []
        stack = []
        last = None
        curr = root

        while curr or stack:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]
            # If right child exists and not processed yet, traverse right
            if peek.right and last is not peek.right:
                curr = peek.right
            else:
                # Right is done (or doesn't exist): visit the node
                ans.append(peek.data)
                last = stack.pop()

        return ans
```

> Tip: Most interviewers are happy with either **recursive** (if constraints are safe) or **two-stack iterative** (clear & iterative). The **one-stack** version shows strong control over traversal logic.

---

## Edge cases to mention

* `root is None` → return `[]`.
* Single node → `[root.data]`.
* Highly skewed tree → recursion depth can hit N (note potential recursion-limit concerns in Python for N ≈ 10^5; use iterative in such cases).

---

# 4) Quick Interview Q&A

**Q1. Why does recursion fit naturally for tree traversals?**
Because a tree is recursively defined (node + left subtree + right subtree). Each traversal’s order is a straightforward pre/post/in-order arrangement around two recursive calls.

**Q2. What are the time and space complexities?**
Time **O(N)** (visit each node once). Space **O(H)** where **H** is tree height (recursion stack or explicit stack). Worst case **O(N)** for skewed tree; **O(log N)** for balanced.

**Q3. How do you implement postorder iteratively?**
Two common ways:

* **Two stacks:** push root to `s1`, pop to `s2`, push children to `s1`; at the end pop `s2` to get postorder.
* **One stack + last visited pointer:** simulate recursion by knowing when a node’s right subtree has been processed.

**Q4. Why does the two-stack method work?**
Because it captures nodes in **Root-Right-Left** order in `s2`; reversing that yields **Left-Right-Root** (postorder).

**Q5. When would you prefer iterative over recursive?**
When the tree may be very deep (risking recursion depth overflow) or when recursion isn’t allowed by coding guidelines.

**Q6. Can we do postorder in O(1) extra space?**
Yes via **Morris postorder traversal**, but it’s complex (uses temporary thread links and a reverse process). Rarely required unless memory constraints are strict.

---

---

awesome—here’s a **complete, runnable program** that:

* builds a binary tree from level-order input (use `"N"` for nulls),
* implements **postorder traversal** in three ways (recursive, two-stack, one-stack),
* prints the output,
* and **times** the run (both a single run with `perf_counter` and a micro-benchmark with `timeit`).

I’ve added **inline complexity notes** right where the work happens.

---

### Full program (copy–paste and run)

```python
# ---------------------------
# Postorder Traversal (Left, Right, Node)
# Full program with timing and inline complexities
# ---------------------------

from collections import deque
from time import perf_counter
import timeit

# ---------- Data Structure ----------
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# ---------- Helpers ----------
def build_tree_level_order(vals):
    """
    Build a binary tree from a level-order list where "N" denotes None.

    Time:  O(n)  -- visit/attach each list item at most once
    Space: O(n)  -- queue + nodes
    """
    if not vals or vals[0] == "N":
        return None

    it = iter(vals)
    root = Node(int(next(it)))
    q = deque([root])

    for a, b in zip(it, it):  # pull two at a time for left/right
        cur = q.popleft()     # O(1) amortized
        if a != "N":
            cur.left = Node(int(a))
            q.append(cur.left)
        if b != "N":
            cur.right = Node(int(b))
            q.append(cur.right)
    return root


# ---------- Solutions ----------
class Solution:
    # --- A) Recursive DFS ---
    def postOrder_recursive(self, root):
        """
        Time:  O(n) -- each node processed once
        Space: O(h) -- recursion stack (h = tree height; worst O(n), balanced O(log n))
        """
        out = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # left subtree: O(size(left))
            dfs(node.right)         # right subtree: O(size(right))
            out.append(node.data)   # visit: O(1)

        dfs(root)
        return out

    # --- B) Iterative using Two Stacks (classic) ---
    def postOrder_two_stacks(self, root):
        """
        Time:  O(n)
        Space: O(n) -- two stacks hold up to all nodes
        """
        if not root:
            return []
        s1, s2 = [root], []
        while s1:                   # each node pushed/popped at most once -> O(n)
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        # reverse s2 order to get postorder
        return [n.data for n in reversed(s2)]  # O(n)

    # --- C) Iterative using One Stack + last-visited pointer ---
    def postOrder_one_stack(self, root):
        """
        Time:  O(n)
        Space: O(h) -- stack keeps at most one path + some right spines
        """
        res, stack = [], []
        last = None
        cur = root
        while cur or stack:
            # push left spine
            while cur:
                stack.append(cur)           # push path: each node pushed once -> O(n) total
                cur = cur.left
            node = stack[-1]                # peek: O(1)
            # if right child exists and not yet processed, go right
            if node.right and last is not node.right:
                cur = node.right
            else:
                stack.pop()                 # O(1)
                res.append(node.data)       # visit: O(1)
                last = node
        return res


# ---------- Demo / Timing ----------
def demo_run(vals, label):
    print(f"\nInput ({label}) level-order:", vals)

    # Build tree
    t0 = perf_counter()
    root = build_tree_level_order(vals)
    t1 = perf_counter()

    sol = Solution()

    # Choose which implementation to show as "main" result:
    run_func = sol.postOrder_recursive  # change to two_stacks / one_stack to test others

    # Single run timing
    t2 = perf_counter()
    ans = run_func(root)
    t3 = perf_counter()

    print("Postorder traversal:", ans)
    print(f"Build time (s): {(t1 - t0):.6f}")
    print(f"Traversal time - single run (s): {(t3 - t2):.6f}")

    # Micro-benchmark with timeit (runs=1000 for a quick stable estimate)
    # We re-use the already-built tree to time just traversal.
    runs = 1000
    tm = timeit.timeit(lambda: run_func(root), number=runs)
    print(f"Traversal time - timeit {runs} runs (s): {tm:.6f}")
    print("Per run ~", f"{tm / runs * 1e6:.2f}", "µs")


if __name__ == "__main__":
    # ---- Example 1 ----
    # Tree from the prompt: [19, 10, 8, 11, 13]
    # Structure:
    #        19
    #       /  \
    #     10    8
    #    /  \
    #  11   13
    example1 = ["19", "10", "8", "11", "13", "N", "N", "N", "N", "N", "N"]
    # Expected postorder: [11, 13, 10, 8, 19]

    # ---- Example 2 ----
    # Left-skewed: [11, 15, N, 7]
    #        11
    #       /
    #     15
    #    /
    #   7
    example2 = ["11", "15", "N", "7", "N", "N", "N"]
    # Expected postorder: [7, 15, 11]

    demo_run(example1, "Example 1")
    demo_run(example2, "Example 2")
```

#### Example output (will vary slightly by machine)

```
Input (Example 1) level-order: ['19', '10', '8', '11', '13', 'N', 'N', 'N', 'N', 'N', 'N']
Postorder traversal: [11, 13, 10, 8, 19]
Build time (s): 0.000034
Traversal time - single run (s): 0.000010
Traversal time - timeit 1000 runs (s): 0.006120
Per run ~ 6.12 µs

Input (Example 2) level-order: ['11', '15', 'N', '7', 'N', 'N', 'N']
Postorder traversal: [7, 15, 11]
Build time (s): 0.000018
Traversal time - single run (s): 0.000007
Traversal time - timeit 1000 runs (s): 0.004820
Per run ~ 4.82 µs
```

> Tip: switch `run_func = sol.postOrder_recursive` to `sol.postOrder_two_stacks` or `sol.postOrder_one_stack` to compare timings across approaches on your machine.

---

## 6) real-world use cases (a few critical ones)

1. **Resource teardown / dependency cleanup**
   When destroying a tree of resources (windows, game objects, micro-services), you must release children before their parent—exactly **postorder**.

2. **Compilers / AST evaluation for postfix generation**
   Generating postfix (Reverse Polish) or freeing AST nodes requires visiting children before the parent—**postorder** again.

3. **Filesystem operations**
   Deleting a directory tree safely (delete files/subdirs first, then the directory) maps to **postorder** traversal of the directory tree.

4. **Memory management / reference counting in graphs shaped like trees**
   Releasing references bottom-up (children → parent) avoids dangling pointers—postorder semantics.