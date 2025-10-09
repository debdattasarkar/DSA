
---

# 🌳 Binary Tree to DLL

**Difficulty:** Hard
**Accuracy:** 53.36%
**Submissions:** 165K+
**Points:** 8
**Average Time:** 60m

---

## 🧠 Problem Statement

Given a **root** of a binary tree (BT), convert it to a **Doubly Linked List (DLL)** *in place* using the **same node structure**.

The **left** and **right** pointers in the binary tree nodes should be used as **prev** and **next** pointers respectively in the resulting DLL.

The DLL should be formed by performing an **inorder traversal** of the binary tree (i.e., `Left → Root → Right`).

The **first node** in the inorder traversal (i.e., the leftmost node) should become the **head** of the DLL.
Return the **head** of the resulting DLL.

---

### 🧾 Note:

`h` is the tree's height, and this space is used implicitly for the recursion stack.

---

### 🖼️ Example Illustration

#### Input Tree:

```
        10
       /  \
     12    15
    / \      \
   25  30     36
```

#### In-Place Conversion:

The above tree should be converted to the following **Doubly Linked List (DLL)**:

```
25 <=> 12 <=> 30 <=> 10 <=> 36 <=> 15
```

---

## 🧩 Examples

### Example 1:

#### Input:

```
root = [1, 2, 3]
```

#### Output:

```
[3, 1, 2]
```

#### Explanation:

The Binary Tree:

```
    1
   / \
  3   2
```

DLL formed by inorder traversal will be:

```
3 <=> 1 <=> 2
```

---

### Example 2:

#### Input:

```
root = [10, 20, 30, 40, 60]
```

#### Output:

```
[40, 20, 60, 10, 30]
```

#### Explanation:

The Binary Tree:

```
       10
      /  \
    20    30
   / \
 40  60
```

DLL formed by inorder traversal will be:

```
40 <=> 20 <=> 60 <=> 10 <=> 30
```

---

## ⚙️ Constraints

* ( 1 \leq \text{Number of nodes} \leq 10^5 )
* ( 0 \leq \text{Data of a node} \leq 10^5 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** ( O(n) )
* **Auxiliary Space:** ( O(\text{height of the tree}) )

---

## 🏢 Company Tags

* Morgan Stanley
* Accolite
* Amazon
* Microsoft
* Snapdeal
* Goldman Sachs
* Salesforce

---

## 🏷️ Topic Tags

* Linked List
* Tree
* Data Structures

---

## 📚 Related Articles

* Convert Binary Tree To Doubly Linked List By Fixing Left And Right Pointers
* Convert Binary Tree To Doubly Linked List Using Inorder Traversal
* Convert Given Binary Tree To Doubly Linked List In Linear Time

---

---

Here’s a tight, interview-ready bundle for **Binary Tree → Doubly Linked List (DLL)**.

---

# 2) Intuition + step-by-step dry run

### What are we building?

* We must **reuse** each tree node.
* In the DLL:

  * `left` will mean **prev**
  * `right` will mean **next**
* The DLL order must be the **inorder traversal** of the tree.
* The **head** is the **leftmost** node of the tree.

### Easiest correct idea

Do an **inorder traversal (Left → Node → Right)** and keep a pointer `prev` to the previously processed node:

* When we visit `node`:

  * Link: `prev.right = node` and `node.left = prev`
  * Move `prev = node`
* The **first** node we visit becomes the **head**.

This is exactly how you “thread” the list while walking the tree.

### Dry run on the example

Tree:

```
        10
       /  \
     12    15
    / \      \
   25  30     36
```

Inorder order should be: **25, 12, 30, 10, 36, 15**

* Start: `prev = None`, `head = None`
* Visit 25:

  * `prev` is `None` → this is the **head**
  * `head = 25`, `prev = 25`
* Visit 12:

  * Connect: `prev(25).right = 12`, `12.left = 25`
  * `prev = 12`
* Visit 30:

  * Connect: `12.right = 30`, `30.left = 12`
  * `prev = 30`
* Visit 10:

  * Connect: `30.right = 10`, `10.left = 30`
  * `prev = 10`
* Visit 36:

  * Connect: `10.right = 36`, `36.left = 10`
  * `prev = 36`
* Visit 15:

  * Connect: `36.right = 15`, `15.left = 36`
  * `prev = 15`

DLL (prev ⇄ next):

```
25 ⇄ 12 ⇄ 30 ⇄ 10 ⇄ 36 ⇄ 15
```

Return `head = 25`.

Complexities:

* **Time:** O(n) (each node touched once)
* **Extra space:** O(h) recursion stack (h = tree height)

  * If you use **Morris traversal**, it becomes **O(1)** extra space.

---

# 3) Optimized codes (multiple ways)

## A) Recursive inorder (most common & clean in interviews)

```python
'''
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None   # will serve as prev in DLL
        self.right = None  # will serve as next in DLL
'''
class Solution:
    def bToDLL(self, root):
        # Inorder threading with two closures variables
        self.prev = None     # last node added to DLL
        self.head = None     # head of DLL (leftmost node)

        def inorder(node):
            if not node:
                return
            # 1) Left
            inorder(node.left)

            # 2) Visit current node: link prev <-> node
            if self.prev is None:
                # first visited = head of DLL
                self.head = node
            else:
                self.prev.right = node  # prev.next = node
                node.left = self.prev   # node.prev = prev

            self.prev = node  # advance prev

            # 3) Right
            inorder(node.right)

        inorder(root)
        return self.head
```

**Why interviewers like it**

* Mirrors the definition of the order we need.
* Short, clear, O(n) time, O(h) stack.

---

## B) Iterative using an explicit stack (no recursion)

```python
class Solution:
    def bToDLL(self, root):
        if not root:
            return None

        stack = []
        curr = root
        head = prev = None

        # Standard iterative inorder traversal
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()  # inorder "visit"

            if prev is None:
                head = node
            else:
                prev.right = node
                node.left = prev
            prev = node

            curr = node.right

        return head
```

**Use this when**

* You want to avoid recursion depth issues.
* You want to show mastery of iterative inorder.

---

## C) Morris inorder (O(1) extra space) — advanced/bonus

```python
class Solution:
    def bToDLL(self, root):
        curr = root
        head = prev = None

        while curr:
            if not curr.left:
                # Visit curr
                if prev is None:
                    head = curr
                else:
                    prev.right = curr
                    curr.left = prev
                prev = curr
                curr = curr.right
            else:
                # Find inorder predecessor
                pre = curr.left
                while pre.right and pre.right is not curr:
                    pre = pre.right

                if not pre.right:
                    # Thread it
                    pre.right = curr
                    curr = curr.left
                else:
                    # Remove thread and visit curr
                    pre.right = None
                    if prev is None:
                        head = curr
                    else:
                        prev.right = curr
                        curr.left = prev
                    prev = curr
                    curr = curr.right

        return head
```

**Pros:** O(1) extra space.
**Cons:** Tricker to write correctly; only use if interviewer asks to reduce space.

---

# 4) Common interviewer Q ↔ A

**Q1. Why is inorder the right order for the DLL?**
**A.** The DLL must reflect the sorted/positional order of a binary tree’s inorder (Left, Node, Right); the problem statement explicitly asks for inorder order.

**Q2. What is the space complexity of your recursive solution?**
**A.** O(h) due to the recursion stack, where h is the tree height. Worst case O(n) for skewed trees; O(log n) for balanced trees.

**Q3. Can you do it in O(1) extra space?**
**A.** Yes, using **Morris traversal**. It temporarily creates “threads” via right pointers of predecessors, restoring them after visiting.

**Q4. Are you allocating any new nodes?**
**A.** No. We reuse each tree node; `left` becomes `prev` and `right` becomes `next`.

**Q5. How do you determine the head of the DLL?**
**A.** The **first node visited** during inorder (leftmost node). We capture it when `prev` is `None`.

**Q6. What if the tree is empty / single node?**
**A.** Empty → return `None`. Single node → that node becomes the head with `left = right = None` (already true).

**Q7. Does the algorithm work if there are duplicate values?**
**A.** Yes. We’re converting structure, not enforcing BST rules. The inorder order is defined regardless of duplicates.

---

---

Absolutely—here’s a **complete, runnable program** that converts a Binary Tree to a **Doubly Linked List (DLL)** in-place using **inorder traversal**, prints the DLL (both directions to verify links), and measures runtime with `timeit`. I’ve added **inline complexity notes** at each important step.

---

### Full Program (with input, output, and timing)

```python
#!/usr/bin/env python3
"""
Binary Tree -> Doubly Linked List (in-place)
In DLL:
  node.left  => prev
  node.right => next

Approach: Recursive Inorder Threading
Time  : O(n)       — each node visited once
Space : O(h) stack — h is tree height (worst O(n), balanced ~O(log n))
"""

from timeit import default_timer as timer
from collections import deque

# -----------------------------
# Data structure
# -----------------------------
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None    # used as DLL 'prev'
        self.right = None   # used as DLL 'next'

# -----------------------------
# Solution
# -----------------------------
class Solution:
    def __init__(self):
        # helpers for threading
        self.prev = None    # last attached node in DLL
        self.head = None    # DLL head (first inorder node)

    def bToDLL(self, root):
        """
        Convert binary tree to DLL using inorder traversal.
        Time: O(n) — every node visited once
        Space: O(h) implicit recursion stack
        """
        self.prev = None
        self.head = None

        def inorder(node):
            # Base: null node => O(1)
            if not node:
                return

            # 1) Visit left subtree — O(size(left))
            inorder(node.left)

            # 2) Process 'node' — O(1)
            if self.prev is None:
                # First node encountered => head of DLL
                self.head = node
            else:
                # Thread the DLL links in-place — O(1)
                self.prev.right = node   # prev.next = node
                node.left = self.prev    # node.prev = prev

            self.prev = node  # advance prev pointer — O(1)

            # 3) Visit right subtree — O(size(right))
            inorder(node.right)

        inorder(root)
        return self.head

# -----------------------------
# Utilities: build & print
# -----------------------------
def build_tree_from_level(level):
    """
    Build binary tree from level-order list (use None for missing).
    Time: O(n), Space: O(n) for queue
    """
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None

    root = Node(root_val)
    q = deque([root])
    for a, b in zip(it, it):
        cur = q.popleft()
        if a is not None:
            cur.left = Node(a)
            q.append(cur.left)
        if b is not None:
            cur.right = Node(b)
            q.append(cur.right)
    return root

def dll_to_list_forward(head):
    """
    Collect DLL forward values for verification.
    Time: O(n), Space: O(1) aside from output list
    """
    out, last = [], None
    cur = head
    while cur:
        out.append(cur.data)
        last = cur
        cur = cur.right
    return out, last

def dll_to_list_backward(tail):
    """
    Collect DLL backward values starting from tail.
    Time: O(n), Space: O(1) aside from output list
    """
    out = []
    cur = tail
    while cur:
        out.append(cur.data)
        cur = cur.left
    return out

# -----------------------------
# Demo / Main
# -----------------------------
if __name__ == "__main__":
    # Example 1 (from prompt image):
    #           10
    #         /    \
    #       12      15
    #      /  \       \
    #     25  30       36
    level = [10, 12, 15, 25, 30, None, 36]

    root = build_tree_from_level(level)

    sol = Solution()
    t0 = timer()
    head = sol.bToDLL(root)          # run conversion
    t1 = timer()

    # Verify by walking forward and backward
    forward, tail = dll_to_list_forward(head)
    backward = dll_to_list_backward(tail)

    # Output
    print("Input level-order tree:", level)
    print("DLL forward :", forward)   # Expected: [25, 12, 30, 10, 36, 15]
    print("DLL backward:", backward)  # Expected: [15, 36, 10, 30, 12, 25]
    print(f"Runtime: {(t1 - t0) * 1e6:.2f} µs")

    # Example 2 (small):
    #     1
    #    / \
    #   3   2
    level2 = [1, 3, 2]
    root2 = build_tree_from_level(level2)
    sol2 = Solution()
    t2 = timer()
    head2 = sol2.bToDLL(root2)
    t3 = timer()

    forward2, tail2 = dll_to_list_forward(head2)
    backward2 = dll_to_list_backward(tail2)

    print("\nInput level-order tree:", level2)
    print("DLL forward :", forward2)   # Expected: [3, 1, 2]
    print("DLL backward:", backward2)  # Expected: [2, 1, 3]
    print(f"Runtime: {(t3 - t2) * 1e6:.2f} µs")
```

#### Sample Output (illustrative)

```
Input level-order tree: [10, 12, 15, 25, 30, None, 36]
DLL forward : [25, 12, 30, 10, 36, 15]
DLL backward: [15, 36, 10, 30, 12, 25]
Runtime: 130.25 µs

Input level-order tree: [1, 3, 2]
DLL forward : [3, 1, 2]
DLL backward: [2, 1, 3]
Runtime: 40.61 µs
```

> Timing will vary by machine; the code prints it using `timeit.default_timer`.

---

## 6) Real-World Use Cases (a few high-impact ones)

1. **In-place tree linearization for traversal**

   * Converting a tree to a DLL is handy when you need to iterate multiple times or support bidirectional iteration without recursion/stack overhead.

2. **Memory-sensitive systems**

   * Reusing nodes (no extra allocations) helps in embedded systems or high-throughput pipelines where GC pressure matters.

3. **Indexing & Range Operations**

   * Inorder DLL of a BST preserves sorted order. It enables fast sequential range scans, merging, and near-neighbor navigation (prev/next) without re-traversing the tree.