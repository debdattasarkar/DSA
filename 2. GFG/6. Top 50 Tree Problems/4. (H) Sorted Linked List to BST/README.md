
---

# 🌳 Sorted Linked List to BST

**Difficulty:** Hard
**Accuracy:** 53.24%
**Submissions:** 29K+
**Points:** 8

---

## 🧠 Problem Statement

Given a **Singly Linked List** whose data members are **sorted in ascending order**,
construct a **Balanced Binary Search Tree (BST)** that contains the **same data members** as the given Linked List.

> **Note:**
> There might be nodes with the same value.

---

## 🧩 Examples

### Example 1:

**Input:**
Linked List:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
```

**Output:**

```
4 2 1 3 6 5 7
```

**Explanation:**
The BST formed using elements of the linked list is:

```
        4
      /   \
     2     6
    / \   / \
   1   3 5   7
```

Hence, the **preorder traversal** of this tree is:

```
4 2 1 3 6 5 7
```

---

### Example 2:

**Input:**
Linked List:

```
1 -> 2 -> 3 -> 4
```

**Output:**

```
3 2 1 4
```

**Explanation:**
The BST formed using elements of the linked list is:

```
      3
     / \
    2   4
   /
  1
```

Hence, the **preorder traversal** of this tree is:

```
3 2 1 4
```

---

## ⚙️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🔢 Constraints

* ( 1 \leq \text{Number of Nodes} \leq 10^6 )
* ( 1 \leq \text{Value of each node} \leq 10^6 )

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Google

---

## 🏷️ Topic Tags

* Linked List
* Binary Search Tree
* Tree
* Data Structures

---

## 🧩 Related Interview Experiences

* Amazon Interview Experience WOW 2020 (6-Months Internship)

---

## 📚 Related Articles

* [Sorted Linked List To Balanced BST](https://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/)

---

---
Here’s everything you’ll want for interviews: a crisp explanation, a step-by-step dry run, then multiple Python solutions (from easiest to optimal) written in the exact signature you gave, plus common interviewer Q&A.

---

# 2) Problem explanation

You’re given a **sorted singly linked list** and must build a **height-balanced BST** containing the same multiset of values.

Why a BST?
Because an **inorder traversal of a BST is sorted**. So if we split the list at its middle, that middle value becomes the BST root; the left half builds the left subtree; the right half builds the right subtree. Recursing this way keeps the tree **balanced**.

Key constraints & goals:

* Input is a *singly* linked list (no random access).
* Output must be a **balanced** BST.
* Aim for **O(n)** time and **O(log n)** recursion depth (height of the tree), i.e., **O(n)** extra space overall (due to recursion), or O(1) auxiliary besides the recursion stack.

---

# Step-by-step dry run (on `1 → 2 → 3 → 4 → 5 → 6 → 7`)

We’ll dry run the **optimal O(n)** approach (inorder simulation) because it’s the most “interview-favorite”.

Idea:

1. First count the length `n = 7`.
2. Build the BST by simulating an **inorder traversal**:

   * Recursively build the left subtree of size `n_left = (n-1)//2`.
   * Create a node using the **current list head** (this head always points to the inorder “next” value).
   * Advance the list head to the next node.
   * Recursively build the right subtree of size `n_right = n - n_left - 1`.

**Call:** build(7)

* build(3)        ← left part for root

  * build(1)      ← left part for node 2

    * build(0) → None
    * Create TNode(1), head moves to 2
    * build(0) → None
  * Create TNode(2), head moves to 3
  * build(1)

    * build(0) → None
    * Create TNode(3), head moves to 4
    * build(0) → None
* Create TNode(4), head moves to 5
* build(3)

  * build(1)

    * build(0) → None
    * Create TNode(5), head moves to 6
    * build(0) → None
  * Create TNode(6), head moves to 7
  * build(1)

    * build(0) → None
    * Create TNode(7), head moves to None
    * build(0) → None

Resulting tree:

```
        4
      /   \
     2     6
    / \   / \
   1  3  5  7
```

Preorder: 4 2 1 3 6 5 7 (as in the sample).

---

# 3) Python solutions (from “brute/easy” to “optimal”)

All snippets follow your types and function signature:

```python
#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''
```

## A) Brute-force / easiest to reason (List -> Array -> BST)

* Convert the linked list to an array in O(n).
* Build a height-balanced BST from sorted array in O(n).
* **Time:** O(n)
* **Extra space:** O(n) for the array + O(log n) recursion.

```python
class Solution:
    def sortedListToBST(self, head):
        # 1) Copy list to array (O(n))
        arr = []
        cur = head
        while cur:
            arr.append(cur.data)
            cur = cur.next

        # 2) Build BST from sorted array (classic)
        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TNode(arr[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(arr) - 1)
```

**When to use:** if you want a very quick, bulletproof solution in an interview warmup.

---

## B) Two-pointer split (slow/fast middle) – direct list recursion

* Find middle node with slow/fast pointers.
* Middle becomes root; left list forms left subtree, right list forms right subtree.
* Requires breaking the list at mid (keep track of prev).
* **Time:** O(n log n) on average (because each `findMid` is O(k) per level)
* **Extra space:** O(log n) recursion.

```python
class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        # Helper: return (mid_prev, mid) where mid is middle node of list starting at head
        def find_mid(start):
            prev = None
            slow = fast = start
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev, slow  # prev can be None if only 1 node

        # Base cases handled inside recursion
        def build(start):
            if not start:
                return None
            mid_prev, mid = find_mid(start)

            # mid is root
            root = TNode(mid.data)

            # left list is start .. mid_prev
            if mid_prev:
                mid_prev.next = None       # cut
                root.left = build(start)   # left from start to mid_prev
                mid_prev.next = mid        # (optional) restore if needed
            else:
                root.left = None

            # right list is mid.next .. end
            root.right = build(mid.next)
            return root

        return build(head)
```

**When to use:** if the interviewer asks you to “do it without extra array space” but isn’t strict about linear time.

---

## C) Optimal O(n) — Inorder simulation with a moving head

* Count length `n`.
* Recursively build the BST “inorder style”; create nodes using the current `head` and advance it as you return from left recursion.
* **Time:** O(n)
* **Extra space:** O(log n) recursion; **no extra list/array**.

```python
class Solution:
    def sortedListToBST(self, head):
        # Count length of list (O(n))
        def length(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        n = length(head)
        self.curr = head  # moving pointer used during inorder construction

        # Build a BST of 'size' nodes using the next 'size' elements from the list in order.
        def build(size):
            if size <= 0:
                return None

            # 1) build left subtree with size//2 nodes
            left = build(size // 2)

            # 2) root from current list node
            root = TNode(self.curr.data)
            root.left = left

            # advance the global list pointer
            self.curr = self.curr.next

            # 3) build right subtree with remaining nodes
            right_size = size - size // 2 - 1
            root.right = build(right_size)
            return root

        return build(n)
```

**Why it’s optimal:** You never “search for mid” repeatedly; you walk the list exactly once in order.

---

# 4) Interview-style Q&A

**Q1. Why does picking the middle element as root ensure the BST is balanced?**
Because the left and right sublists are as equal in size as possible (difference at most 1). Recursively applying this ensures tree height is O(log n).

**Q2. What are the time/space complexities of each approach?**

* Array → BST: **O(n)** time, **O(n)** extra space (array) + **O(log n)** recursion.
* Slow/Fast middle split: **O(n log n)** time (each level scans), **O(log n)** space.
* Inorder simulation (optimal): **O(n)** time, **O(log n)** space (recursion only).

**Q3. Why does the inorder simulation work?**
An inorder traversal of a BST produces values in sorted order. If you *construct* the tree by doing a virtual inorder traversal and, at the “visit root” step, consume the current list node, you’re assigning the i-th smallest value to the i-th visited node—exactly what a BST needs.

**Q4. How do you handle duplicates?**
All approaches naturally handle duplicates. Inorder simulation and array-to-BST both insert equal values; the resulting BST remains valid (BST definition here allows equal values to be on either consistent side—most implementations place duplicates either left or right consistently).

**Q5. Can we do it iteratively?**
Not cleanly for the optimal O(n) approach; recursion neatly preserves subtree sizes and order. You *could* simulate recursion with a stack, but it complicates the “moving head” mechanism.

**Q6. What’s the auxiliary space of the optimal approach?**
O(log n) for recursion depth (balanced tree height). No extra data structures are required.

**Q7. What if the list is extremely long (e.g., 10^6 nodes)?**
The optimal approach is linear time and uses only recursion stack. In Python you might hit recursion depth for degenerate cases only if the list weren’t balanced, but this construction is balanced, so depth is ~log2(n), which is fine.

---

---

Awesome — here’s a **complete, runnable program** that:

* Implements the **optimal O(n)** “inorder-simulation” solution for **Sorted Linked List → Balanced BST** using your required signature.
* Includes **inline time/space complexity notes** right where they matter.
* Builds a couple of **sample inputs**, prints the **preorder traversal** of the BST (as in the problem examples), and uses `timeit` to show how long the full run took.
* Ends with a few **real-world use cases**.

---

## Full Program (ready to paste & run)

```python
# ----------------------------
#  Sorted Linked List -> BST
#  Optimal O(n) construction
# ----------------------------

from timeit import default_timer as timer

# ----------------------------
# Node definitions (as in prompt)
# ----------------------------
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class TNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# ----------------------------
# Utilities for building/testing
# ----------------------------

def build_linked_list(values):
    """Builds singly linked list from Python list.
    Time:  O(n), Space: O(1) extra (excluding the list of values)"""
    head = tail = None
    for v in values:
        node = LNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def preorder(root):
    """Returns the preorder traversal of a BST as a Python list.
    Time:  O(n) visits each node once
    Space: O(h) recursion (h = height, ~log n for balanced tree)"""
    out = []
    def dfs(node):
        if not node:
            return
        out.append(node.data)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return out


# ----------------------------
# Required Solution class/signature
# ----------------------------
class Solution:
    def sortedListToBST(self, head):
        """
        Build a height-balanced BST from a sorted singly linked list.
        Strategy: Inorder simulation with a moving head pointer.

        High-level complexities:
        - Time:  O(n)  (each list node is consumed exactly once)
        - Space: O(log n) recursion stack (balanced tree height)
        """

        # ---- helper: compute length of list ----
        # Time: O(n), Space: O(1)
        def length(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        n = length(head)             # O(n)
        self.curr = head             # moving pointer during "inorder" build

        # ---- core builder: simulate inorder ----
        # build(size) constructs a BST from the next `size` list nodes.
        # Time:  O(size) overall across all calls
        # Space: O(log n) recursion (balanced)
        def build(size):
            if size <= 0:
                return None

            # 1) build left subtree with size//2 nodes
            #    Time (amortized): contributes to overall O(n)
            #    Space: recursion grows by +1 per level => O(log n)
            left = build(size // 2)

            # 2) root node from current list head
            root = TNode(self.curr.data)  # O(1)
            root.left = left

            # advance the global list pointer (O(1))
            self.curr = self.curr.next

            # 3) build right subtree with remaining nodes
            right_size = size - size // 2 - 1
            root.right = build(right_size)

            return root

        # Build and return the balanced BST
        return build(n)


# ----------------------------
# Demo + timing
# ----------------------------
if __name__ == "__main__":
    # Two sample inputs (feel free to add your own):
    cases = [
        [1, 2, 3, 4, 5, 6, 7],            # perfectly balanced outcome
        [1, 2, 3, 4]                       # even count
    ]

    start = timer()

    for i, arr in enumerate(cases, 1):
        print(f"\nCase {i}: input list = {arr}")
        head = build_linked_list(arr)          # O(n)
        root = Solution().sortedListToBST(head)  # O(n) time, O(log n) stack
        pre = preorder(root)                    # O(n)
        print("Preorder of constructed BST:", pre)

    end = timer()
    print(f"\nTotal time for full program run: {end - start:.6f} seconds")
```

### What you’ll see when you run it

Example output (will vary slightly by machine):

```
Case 1: input list = [1, 2, 3, 4, 5, 6, 7]
Preorder of constructed BST: [4, 2, 1, 3, 6, 5, 7]

Case 2: input list = [1, 2, 3, 4]
Preorder of constructed BST: [3, 2, 1, 4]

Total time for full program run: 0.0008 seconds
```

---

## Complexity recap (line-by-line where it matters)

* `length(head)`: **O(n)** time, **O(1)** space.
* Inorder-simulation `build(size)` across all recursive calls: **O(n)** time total, visits each list node once; **O(log n)** recursion depth (the produced tree is balanced).
* `preorder(root)` printing (only for the demo): **O(n)** time, **O(log n)** space.

**Overall program run (per case): O(n)** time + **O(log n)** space.

---

## 6) Real-World Use Cases (a few highly relevant ones)

1. **Indexing & Search Trees from Streams**
   When data arrives **sorted** (e.g., from a sorted file or network stream with order guarantees), you can build a **balanced BST** on the fly to support fast in-memory **binary search / range queries**.

2. **Memory-tight conversions**
   If your input is a **singly linked list** (low random-access locality), building a BST in **O(n)** without extra arrays avoids doubling memory footprint (important in embedded/low-memory services).

3. **Balanced Partitioning for Scheduling/Load-balancing**
   Turning a sorted list of tasks or keys into a balanced BST yields balanced **left/right partitions** recursively — useful in **divide-and-conquer** task scheduling or **shard** assignment.

---
