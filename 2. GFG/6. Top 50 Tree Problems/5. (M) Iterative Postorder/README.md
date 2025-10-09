# Iterative Postorder

**Difficulty:** Medium
**Accuracy:** 80.67%
**Submissions:** 48K+
**Points:** 4

---

## Problem Statement

Given a binary tree, **find the postorder traversal of the tree *without using recursion***.
Return a list containing the postorder traversal of the tree, calculated **without using recursion**.

---

## Examples

### Example 1

**Input:**

```
    1
   / \
  2   3
 / \
4   5
```

**Output:** `4 5 2 3 1`

**Explanation:** Postorder traversal (Left -> Right -> Root) of the tree is `4 5 2 3 1`.

---

### Example 2

**Input:**

```
        8
       / \
      1   5
       \  / \
        7 10 6
           /
          10 6
```

**Output:** `10 7 1 6 10 6 5 8`

**Explanation:** Postorder traversal (Left -> Right -> Root) of the tree is `10 7 1 6 10 6 5 8`.

> *Note:* The ASCII layout above mirrors the structure from the prompt; values appear in postorder as shown.

---

## Expected Complexities

* **Expected time complexity:** `O(n)`
* **Expected auxiliary space:** `O(n)`

---

## Constraints

* `1 ≤ Number of nodes ≤ 10^5`
* `1 ≤ Data of a node ≤ 10^5`

---

## Company Tags

* Microsoft

---

## Topic Tags

* Stack
* Tree
* Data Structures

---

## Related Articles

* [Iterative Postorder Traversal Using Stack](https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/)

---

---

gotcha—let’s make this interview-ready.

# 2) Explanation + step-by-step dry run

## What is postorder?

Traversal order is **Left → Right → Root**.

Because recursion naturally gives us a call stack, the challenge is to simulate that **iteratively**.

### Common iterative strategies

1. **Two stacks (easy to remember)**

   * `s1` does a modified preorder (Root → Left → Right).
   * Pop from `s1`, push to `s2`.
   * Finally pop everything from `s2` to get Left → Right → Root.

2. **One stack + “last visited” pointer (space-optimal with stack)**

   * Walk down left children, pushing nodes.
   * Peek the top:

     * If it has an unvisited right child, move to that right child.
     * Otherwise, visit (append) the node and set it as `last_visited`.
   * This perfectly simulates the recursion without extra structures.

3. **Reverse-preorder trick (single stack + reverse)**

   * Do Root → Right → Left (by pushing left last).
   * Reverse the collected list to get Left → Right → Root.

4. **Morris Postorder (advanced, O(1) extra space)**

   * Uses threaded binary tree idea and edge reversals along the way.
   * Interviewers rarely require this, but it’s a great “bonus”.

---

## Dry run (two stacks, clear and quick)

Tree:

```
    1
   / \
  2   3
 / \
4   5
```

**Goal:** postorder = `4 5 2 3 1`

**Initialize:**
`s1 = [1]`, `s2 = []`

**Process:**

* Pop `1` from `s1`, push to `s2` → `s2=[1]`.
  Push children of `1` to `s1`: push `2`, push `3`. → `s1=[2,3]` (top is rightmost)
* Pop `3` → `s2=[1,3]`. Children? none → `s1=[2]`.
* Pop `2` → `s2=[1,3,2]`. Push its children: push `4`, push `5` → `s1=[4,5]`.
* Pop `5` → `s2=[1,3,2,5]`.
* Pop `4` → `s2=[1,3,2,5,4]`.

**Final readout:** pop everything from `s2` (or just reverse it) → `4 5 2 3 1`.

---

## Dry run (single stack + last_visited)

State vars: `stack`, `curr`, `last = None`, `ans=[]`

Start: `curr=1`

1. Go left down pushing: push 1,2,4.
   `stack=[1,2,4]`, `curr=None`.
2. Peek `4`:

   * `4.right` is None **or** equals `last` → visit 4.
     `ans=[4]`, `last=4`, pop 4.
3. Peek `2`:

   * `2.right` exists (=5) and `last != 5` → go right: `curr=5`.
4. Go left down from 5 (none) ⇒ peek `5`:

   * visit 5 → `ans=[4,5]`, `last=5`, pop 5.
5. Peek `2` again:

   * right(5) == last → visit 2 → `ans=[4,5,2]`, `last=2`, pop 2.
6. Peek `1`:

   * right(3) exists and not visited → `curr=3`, push 3, then left down (none).
   * visit 3 → `ans=[4,5,2,3]`, `last=3`, pop 3.
7. Peek `1`:

   * right(3) == last → visit 1 → `ans=[4,5,2,3,1]`.

Done.

---

# 3) Python solutions (brute/easy + optimized), with interview-style inline comments

All versions return a list of node values in postorder.
Template matches the provided GFG-style signature.

```python
# User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self, node):
        # ---- Version 1: Two Stacks (very common, easy to explain) ----
        if not node:
            return []
        
        s1 = [node]   # acts like a preorder driver
        s2 = []       # will store nodes in reverse postorder
        ans = []
        
        while s1:
            cur = s1.pop()
            s2.append(cur)  # root gets pushed; we'll reverse by s2 later
            
            # For modified preorder, push left and right children
            if cur.left:
                s1.append(cur.left)
            if cur.right:
                s1.append(cur.right)
        
        # s2 holds nodes in Root->Right->Left order; reverse gives postorder
        while s2:
            ans.append(s2.pop().data)
        return ans
```

### Alternative implementations (pick the one you prefer in interviews)

#### A) Single stack + last visited (optimized stack usage)

* One stack only; visits a node when:

  1. It has no right child, or
  2. Its right child was the `last_visited`.

```python
class SolutionOneStack:
    def postOrder(self, node):
        if not node:
            return []
        
        stack = []
        ans = []
        last = None   # last visited node
        curr = node
        
        while curr or stack:
            # push left spine
            while curr:
                stack.append(curr)
                curr = curr.left
            
            peek = stack[-1]
            # if right child exists and not processed yet, go right
            if peek.right and last is not peek.right:
                curr = peek.right
            else:
                # visit the node
                ans.append(peek.data)
                last = stack.pop()
                # loop continues with curr=None to consider parent
        return ans
```

#### B) Reverse-preorder trick (single stack + reverse result)

```python
class SolutionReversePreorder:
    def postOrder(self, node):
        if not node:
            return []
        stack = [node]
        out = []  # collects Root->Right->Left
        while stack:
            cur = stack.pop()
            out.append(cur.data)
            # push left last so it is processed after right
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        # reverse to get Left->Right->Root
        return out[::-1]
```

#### C) Morris Postorder (advanced: O(1) extra space)

This is a bonus you can mention if pressed for optimal space.
Key idea: create a dummy root, build temporary threads, and when returning from a left subtree, **reverse the right edge** of that subtree to output nodes in reverse, then restore edges.

```python
class SolutionMorris:
    def postOrder(self, node):
        # Morris traversal variant, O(1) extra space (excluding output list)
        def reverse_path(start, end):
            # reverse right pointers from start to end (inclusive)
            if start is end:
                return
            prev, cur = None, start
            while prev is not end:
                nxt = cur.right
                cur.right = prev
                prev, cur = cur, nxt
        
        def collect_reverse(start, end, ans):
            # output nodes from end to start after reversing, then restore
            reverse_path(start, end)
            cur = end
            while True:
                ans.append(cur.data)
                if cur is start:
                    break
                cur = cur.right
            reverse_path(end, start)  # restore
        
        if not node:
            return []
        dummy = Node(0)
        dummy.left = node
        cur = dummy
        ans = []
        
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                # find predecessor in left subtree (rightmost of left)
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur  # thread created
                    cur = cur.left
                else:
                    # left subtree finished; collect left boundary in reverse
                    collect_reverse(cur.left, pre, ans)
                    pre.right = None  # remove thread
                    cur = cur.right
        return ans
```

**Complexities:**

* Two stacks / One stack / Reverse-preorder: **Time O(n)**, **Space O(n)** worst case (stack or output).
* Morris: **Time O(n)**, **Space O(1)** (excluding output), but more complex and error-prone.

---

# 4) Interviewer-style Q&A

**Q1. Why can’t we just use recursion?**
**A.** You can, but the prompt forbids it and recursion can overflow the call stack for very deep trees (height ≈ number of nodes). Iterative methods avoid that risk and give explicit control over memory.

**Q2. Compare the common iterative methods.**
**A.**

* **Two stacks:** simplest to reason about; mechanically converts preorder to postorder.
* **One stack + last_visited:** uses less auxiliary space than two stacks and is idiomatic; closely simulates the recursive flow.
* **Reverse-preorder:** easy code; one stack and a final reverse.
* **Morris:** O(1) extra space; hardest to implement; usually “bonus”.

**Q3. What’s the time and space complexity?**
**A.** All are **O(n)** time because each node is pushed/popped a constant number of times.
Space: `O(h)` for the single-stack method (`h` = tree height; `O(n)` worst-case for skewed trees). Two stacks is also `O(n)` worst-case. Morris is `O(1)` extra space.

**Q4. How does the one-stack method know when to visit a node?**
**A.** Maintain `last_visited`. After pushing the left spine, peek the top.

* If it has an unvisited right child, move to the right.
* Else (no right OR right == last_visited), we know both subtrees are done → visit it.

**Q5. What are edge cases to test?**
**A.**

* Empty tree.
* Single node.
* Only left chain; only right chain.
* Perfectly balanced tree.
* Tree with missing one child at many places (ragged).

**Q6. When would you prefer Morris postorder?**
**A.** When recursion is disallowed, memory is tight, and you’re comfortable with threaded trees / edge reversal. For most interviews, mention it as an option; implement the one-stack or two-stack version.

**Q7. Can you derive postorder from preorder or inorder easily?**
**A.** Without additional structure (like knowing it’s a BST and having both traversals), not in a single pass. The reverse-preorder trick specifically builds Root→Right→Left and then reverses to get postorder in linear time.

**Q8. How do these approaches behave on a skewed tree?**
**A.** All keep **O(n)** time. Stack depth becomes **O(n)** for one/two-stack methods; Morris stays **O(1)** extra space.

---

---

awesome—here’s a complete, **runnable** program that:

* builds a binary tree from **level-order input** (space-separated, `N` for nulls — GfG style),
* runs **three** iterative postorder variants (two stacks, one stack, reverse-preorder),
* prints the **output traversal** for each,
* and benchmarks each method using **`timeit`** (and a single-run wall clock).

I’ve added **inline comments** describing the **time/space complexity** of each step.

---

## Full Python Program (with timing + sample I/O)

```python
#!/usr/bin/env python3
"""
Iterative Postorder Traversal - Full Program with Timing

Input format (single test):
- A single line with the level-order traversal of the binary tree.
- Use 'N' for a missing (null) child, e.g.:
    1 2 3 4 5 N N N N N N

Example tree used in the prompt:
    1
   / \
  2   3
 / \
4   5
Level-order input: 1 2 3 4 5 N N

This script prints postorder results from:
  1) Two-stacks method
  2) One-stack + last_visited pointer
  3) Reverse-preorder + reverse the list

It also times each method using both:
  - A single run wall-clock (perf_counter)
  - timeit.timeit(number=3) average over 3 runs
"""

from collections import deque
from time import perf_counter
import timeit
import sys

# ---------- Node Definition ----------
class Node:
    def __init__(self, val):
        # O(1) time, O(1) space
        self.data = val
        self.left = None
        self.right = None

# ---------- Build Tree from Level-Order (GfG style) ----------
def build_tree(level_order_tokens):
    """
    Build a binary tree from a list of tokens (strings) where:
      - tokens[i] is either an integer string or 'N' for None
    Returns root: Node | None

    Complexity:
      - Time: O(n) where n = number of tokens (each token processed once)
      - Space: O(n) for the queue plus nodes created
    """
    if not level_order_tokens or level_order_tokens[0] == 'N':
        return None

    it = iter(level_order_tokens)
    root_val = next(it)
    root = Node(int(root_val))  # O(1)
    q = deque([root])           # O(1)

    for left_val in it:
        # Pop parent whose children we are about to attach
        parent = q.popleft()    # Amortized O(1)

        # Attach left child if present
        if left_val != 'N':
            left = Node(int(left_val))  # O(1)
            parent.left = left
            q.append(left)              # O(1)

        # Next token is right child (if any)
        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val != 'N':
            right = Node(int(right_val))  # O(1)
            parent.right = right
            q.append(right)               # O(1)

    return root

# ---------- Solution 1: Two Stacks (easy & popular) ----------
class SolutionTwoStacks:
    def postOrder(self, node):
        """
        Idea:
          - Push root to s1.
          - Pop from s1, push to s2, push its left and right to s1.
          - Finally pop everything from s2 => postorder.

        Complexity:
          - Time: O(n) (each node pushed/popped a constant number of times)
          - Space: O(n) for s1+s2 in the worst case (skewed tree)
        """
        if not node: return []
        s1 = [node]  # O(1)
        s2 = []      # O(1)
        while s1:    # Each node enters/leaves s1 once -> O(n)
            cur = s1.pop()       # O(1)
            s2.append(cur)       # O(1)
            if cur.left:         # O(1)
                s1.append(cur.left)
            if cur.right:        # O(1)
                s1.append(cur.right)
        # s2 contains nodes in Root->Right->Left; reverse pop gives postorder
        out = []
        while s2:                # Each node leaves s2 once -> O(n)
            out.append(s2.pop().data)
        return out

# ---------- Solution 2: One Stack + last_visited pointer ----------
class SolutionOneStack:
    def postOrder(self, node):
        """
        Idea:
          - Push left spine.
          - Peek: if right child exists and not visited, go right.
            else visit/append.
        Complexity:
          - Time: O(n)
          - Space: O(h) for stack (h = tree height), O(n) worst case if skewed
        """
        if not node: return []
        stack = []
        out = []
        last = None
        curr = node
        # Outer loop visits every node a constant number of times -> O(n)
        while curr or stack:
            # Push the left spine -> at most n pushes over whole run -> O(n)
            while curr:
                stack.append(curr)  # O(1)
                curr = curr.left
            peek = stack[-1]        # O(1)
            # If unvisited right child exists, traverse it next
            if peek.right and last is not peek.right:
                curr = peek.right
            else:
                # Visit current node
                out.append(peek.data)   # O(1)
                last = stack.pop()      # O(1)
        return out

# ---------- Solution 3: Reverse-Preorder Trick ----------
class SolutionReversePreorder:
    def postOrder(self, node):
        """
        Idea:
          - Do "Root -> Right -> Left" using a single stack, append data,
            then reverse the result to get postorder.
        Complexity:
          - Time: O(n) (each node pushed/popped once, then O(n) reverse)
          - Space: O(n) for stack and output list
        """
        if not node: return []
        stack = [node]  # O(1)
        out = []        # O(1)
        while stack:    # O(n)
            cur = stack.pop()     # O(1)
            out.append(cur.data)  # O(1)
            # Push left last so it's processed after right
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        # Reverse to achieve Left->Right->Root
        out.reverse()             # O(n)
        return out

# ---------- Helpers for timing ----------
def time_single_run(func, *args, **kwargs):
    """
    Single wall-clock timing using perf_counter
    """
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)

def time_with_timeit(stmt_callable, number=3):
    """
    Uses timeit.timeit to measure average time over `number` runs.
    `stmt_callable` is a zero-argument lambda capturing the environment.
    """
    # timeit.timeit returns total time over 'number' runs
    total = timeit.timeit(stmt_callable, number=number)
    return total / number  # average per run

# ---------- Main ----------
def main():
    # Read one line of level-order input from stdin
    # Example inputs you can paste:
    # 1) 1 2 3 4 5 N N
    # 2) 8 1 5 N 7 10 6 N N N N 10 6
    data = sys.stdin.read().strip().split()
    if not data:
        print("No input provided. Example: 1 2 3 4 5 N N")
        return

    # Build tree (O(n) time, O(n) space)
    root = build_tree(data)

    # Prepare solvers
    sol_two = SolutionTwoStacks()
    sol_one = SolutionOneStack()
    sol_rev = SolutionReversePreorder()

    # ---- Two Stacks ----
    res_two, t_two_single = time_single_run(sol_two.postOrder, root)
    t_two_avg = time_with_timeit(lambda: sol_two.postOrder(root), number=3)

    # ---- One Stack ----
    res_one, t_one_single = time_single_run(sol_one.postOrder, root)
    t_one_avg = time_with_timeit(lambda: sol_one.postOrder(root), number=3)

    # ---- Reverse-Preorder ----
    res_rev, t_rev_single = time_single_run(sol_rev.postOrder, root)
    t_rev_avg = time_with_timeit(lambda: sol_rev.postOrder(root), number=3)

    # Print results
    print("Postorder Traversal (Two Stacks):", *res_two)
    print("  Single-run time (s):", f"{t_two_single:.6f}")
    print("  timeit avg over 3 runs (s):", f"{t_two_avg:.6f}")
    print()

    print("Postorder Traversal (One Stack):", *res_one)
    print("  Single-run time (s):", f"{t_one_single:.6f}")
    print("  timeit avg over 3 runs (s):", f"{t_one_avg:.6f}")
    print()

    print("Postorder Traversal (Reverse-Preorder):", *res_rev)
    print("  Single-run time (s):", f"{t_rev_single:.6f}")
    print("  timeit avg over 3 runs (s):", f"{t_rev_avg:.6f}")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 iterative_postorder.py << EOF
1 2 3 4 5 N N
EOF
```

### Sample Output (for input `1 2 3 4 5 N N`)

```
Postorder Traversal (Two Stacks): 4 5 2 3 1
  Single-run time (s): 0.0000xx
  timeit avg over 3 runs (s): 0.0000yy

Postorder Traversal (One Stack): 4 5 2 3 1
  Single-run time (s): 0.0000xx
  timeit avg over 3 runs (s): 0.0000yy

Postorder Traversal (Reverse-Preorder): 4 5 2 3 1
  Single-run time (s): 0.0000xx
  timeit avg over 3 runs (s): 0.0000yy
```

> Exact times depend on your machine and Python version.

---

## Real-World Use Cases (high-impact)

* **Garbage Collection / Resource Release:** Many systems perform **postorder**-like processing to free child resources before their parent (e.g., deleting files in a directory tree, destroying scene graphs, releasing dependency graphs).

* **Expression Trees (Compilers/DB engines):** Evaluating an expression tree (AST) in postfix (Reverse Polish) order is naturally a postorder traversal: compute left and right operands before applying the parent operator.

* **Filesystem and Build Tools:** When removing directories or when computing **build orders** in DAG-like structures for tasks that require children built before parents (postorder on a tree; topological order on a DAG).

* **Rendering / Game Engines:** Updating transforms or physics where a parent’s final state depends on children having been updated or aggregated first (e.g., computing bounding boxes bottom-up).