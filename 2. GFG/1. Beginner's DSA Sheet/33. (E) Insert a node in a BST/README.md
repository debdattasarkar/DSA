
---

# Insert a Node in a BST

**Difficulty:** Easy
**Accuracy:** 47.15%
**Submissions:** 175K+
**Points:** 2
**Average Time:** 15m

---

## Problem Statement

Given a **root** binary search tree and a **key**.

* If the key is not present in the tree, **insert** a new node with a value equal to the key into the tree.
* If the key is already present in the tree, **don't modify** the tree.

Return the root of the modified tree after inserting the key.

**Note:** The generated output contains the in-order traversal of the modified tree.

---

## Examples

### Example 1:

**Input:**

```
root = [2, 1, 3], key = 4
```

**Output:**

```
[1, 2, 3, 4]
```

**Explanation:**
After inserting the node 4, inorder traversal will be `1 2 3 4`.

---

### Example 2:

**Input:**

```
root = [2, 1, 3, N, N, N, 6], key = 4
```

**Output:**

```
[1, 2, 3, 4, 6]
```

**Explanation:**
After inserting the node 4, inorder traversal of the above tree will be `1 2 3 4 6`.

---

### Example 3:

**Input:**

```
root = [2, 1, 3], key = 2
```

**Output:**

```
[1, 2, 3]
```

**Explanation:**
Node with key = 2 already present in BST, so inorder traversal remains `1 2 3`.

---

## Constraints

* $1 \leq \text{number of nodes} \leq 10^5$
* $1 \leq \text{node->data} \leq 10^9$
* $1 \leq \text{key} \leq 10^9$

---

## Expected Complexities

* **Time Complexity:** $O(h)$, where *h* is the height of the BST.
* **Auxiliary Space:** $O(h)$, due to recursion stack (iterative version can achieve $O(1)$).

---

## Company Tags

* Paytm
* Accolite
* Amazon
* Microsoft
* Samsung

---

## Topic Tags

* Binary Search Tree
* Design-Pattern
* Data Structures

---

## Related Articles

* [Binary Search Tree Set 1 Search and Insertion](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)

---

---

Here you go — everything you need for interviews on “Insert a node in a BST” ✨

---

# 2) Text explanation + step-by-step dry run

## What we’re doing

Given the root of a Binary Search Tree (BST) and an integer `key`, insert `key` into the BST while preserving the BST property:

* Left subtree values < node value
* Right subtree values > node value
* If `key` already exists, do **nothing** and return the (unchanged) root.

## How insertion works (conceptually)

1. If the tree is empty → create a new node and return it as root.
2. Otherwise, walk down the tree:

   * If `key < node.data`, go left.
   * If `key > node.data`, go right.
   * If `key == node.data`, stop (duplicates not allowed by problem), return root.
3. When you fall off a `None` child in the correct direction, attach a new node there.

The height of the tree is `h`; we touch at most one node per level → `O(h)` time.

## Dry run

**Input:**
Tree (level order): `[2, 1, 3]`
`key = 4`

**Process (iterative view):**

* Start at `2`. `4 > 2` → go right to `3`.
* At `3`. `4 > 3` → go right. Right child is `None` → insert new node `4` here.

**Resulting tree (inorder):** `1, 2, 3, 4`

Another quick one:

**Input:**
Tree: `[2, 1, 3]`, `key = 2`

**Process:**

* At `2`. `key == 2` → already present. Do nothing.

**Inorder remains:** `1, 2, 3`.

---

# 3) Optimized codes in Python (both common interview styles)

You can use either recursive (short & clean) or iterative (no recursion stack). Both are optimal with `O(h)` time. Iterative uses `O(1)` extra space; recursive uses `O(h)` call stack.

### (A) Recursive insertion (clean & idiomatic)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def insert(self, root, key):
        """
        Time:  O(h) where h is the height of the BST
        Space: O(h) recursion stack
        """
        # Base: empty spot -> place new node here
        if root is None:
            return Node(key)

        if key < root.data:
            # Insert into left subtree and reattach (important for persistence)
            root.left = self.insert(root.left, key)
        elif key > root.data:
            # Insert into right subtree and reattach
            root.right = self.insert(root.right, key)
        else:
            # key == root.data: duplicate; do nothing
            return root

        return root
```

### (B) Iterative insertion (no recursion; constant extra space)

```python
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def insert(self, root, key):
        """
        Time:  O(h)
        Space: O(1)
        """
        # Empty tree -> new root
        if root is None:
            return Node(key)

        cur = root
        parent = None

        # Walk down to find insertion point or detect duplicate
        while cur:
            parent = cur
            if key < cur.data:
                cur = cur.left
            elif key > cur.data:
                cur = cur.right
            else:
                # key already exists: no change
                return root

        # Attach new node under parent on the correct side
        if key < parent.data:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

        return root
```

### (C) Tail-recursive (same complexity, sometimes discussed)

This is the same idea as (A) but explicitly tail-oriented; Python doesn’t optimize tail recursion, so prefer (A) or (B) in practice.

---

## Edge cases to be aware of

* **Empty tree** (`root = None`) → new node becomes the root.
* **Duplicate key** → return `root` unchanged.
* **Highly skewed tree** (essentially a linked list) → `h = n`, so `O(n)` in worst case.
* **Very large keys / values** → handled by Python ints; no special handling needed.

---

# 4) Interviewer-style Q\&A

**Q1. What’s the time and space complexity?**
**A.** Time `O(h)` where `h` is the height of the BST (best `O(log n)` if balanced, worst `O(n)` if skewed).
Space is `O(h)` for the recursive version (call stack) or `O(1)` for the iterative version.

**Q2. How do you handle duplicates?**
**A.** The problem states *don’t modify the tree* if the key exists. We detect `key == node.data` and return the unchanged root.

**Q3. Why reassign `root.left = insert(root.left, key)` in recursion?**
**A.** Because the recursive call may return a new subtree root (e.g., when inserting into an empty subtree). Reattaching preserves the parent’s pointer.

**Q4. How would you keep the tree balanced after many insertions?**
**A.** Use a self-balancing BST (AVL, Red-Black Tree, Treap, etc.). Standard BST insertion doesn’t rebalance, so performance may degrade to `O(n)`.

**Q5. Can this be done iteratively? Pros/Cons vs recursion?**
**A.** Yes (see solution B). Iterative is `O(1)` extra space and avoids recursion-depth limits. Recursive is shorter and often clearer.

**Q6. How do you confirm your insertion worked?**
**A.** Run an inorder traversal → it should remain sorted, and it should contain the inserted key if it wasn’t a duplicate.

---

---

Awesome — here’s a complete, ready-to-run program for **Insert a node in a BST** with clear inline complexity notes, sample input/outputs, and a tiny timing harness.

---

# 5) Full program (with time & space complexity comments, inputs, outputs, and timing)

```python
"""
Insert a node into a Binary Search Tree (BST).

Complexities (high level)
-------------------------
Let h be the height of the BST, n be the number of nodes.
- Insertion: Time  O(h)     (best O(log n) if balanced, worst O(n) if skewed)
              Space O(1)    (iterative) or O(h) for recursion

Below we implement the ITERATIVE insert -> O(1) extra space.
We also include an inorder traversal for verification.
"""

from time import perf_counter

# ---------- Data structures ----------

class Node:
    def __init__(self, val):
        # Time: O(1), Space: O(1)
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def insert(self, root, key):
        """
        Insert `key` into BST rooted at `root`. If key already exists, return root unchanged.

        Iterative approach:
        - Walk down from root to find the correct null child to attach new node
        - If we see a duplicate, we stop (problem asks to not modify)

        Time:  O(h) — one pass from root down to a leaf-level position
        Space: O(1) — constant extra pointers
        """
        # Case 1: Empty tree -> new root
        if root is None:
            # Time: O(1), Space: O(1)
            return Node(key)

        cur = root
        parent = None

        # Walk: at most h iterations (one per level)
        # Time total: O(h)
        while cur:
            parent = cur
            if key < cur.data:
                cur = cur.left      # Time per step O(1), Space O(1)
            elif key > cur.data:
                cur = cur.right     # Time per step O(1), Space O(1)
            else:
                # key == cur.data -> duplicate; do not modify the tree
                # Time: O(1), Space: O(1)
                return root

        # We fell off the tree at 'parent'; attach the new node to correct side.
        # Time: O(1), Space: O(1)
        if key < parent.data:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

        return root


# ---------- Utility functions (for demo & validation) ----------

def build_bst_from_list(values):
    """
    Build a BST by inserting values in order.

    Time:  O(m * h_avg) where m=len(values), h_avg avg height during building
    Space: O(1) extra (iterative insert)
    """
    sol = Solution()
    root = None
    for v in values:
        root = sol.insert(root, v)
    return root

def inorder(root):
    """
    Inorder traversal -> sorted sequence for a valid BST.

    Time:  O(n) — visits each node once
    Space: O(h) recursion stack (worst O(n) if skewed)
    """
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


# ---------- Main demo with timing ----------

if __name__ == "__main__":
    # Example input 1
    initial_values = [2, 1, 3]      # BST built by these insertions (one by one)
    key_to_insert = 4               # Insert 4 (not present)
    # Example input 2 (duplicate)
    key_duplicate = 2               # Already present

    # Build initial BST
    t0 = perf_counter()
    root = build_bst_from_list(initial_values)

    print("Initial BST (inorder):", inorder(root))  # Expect [1, 2, 3]

    # Insert a new key
    sol = Solution()
    root = sol.insert(root, key_to_insert)
    print("After inserting", key_to_insert, "(inorder):", inorder(root))  # Expect [1, 2, 3, 4]

    # Insert duplicate key (no change)
    root = sol.insert(root, key_duplicate)
    print("After inserting duplicate", key_duplicate, "(inorder):", inorder(root))  # Expect [1, 2, 3, 4]

    t1 = perf_counter()
    print(f"\nTotal program time (incl. building, 2 inserts, traversals): {(t1 - t0)*1000:.3f} ms")

    # Another quick test: larger set
    more_values = [5, 2, 8, 1, 3, 7, 9]
    root2 = build_bst_from_list(more_values)
    print("\nSecond BST (inorder):", inorder(root2))  # Expect [1, 2, 3, 5, 7, 8, 9]
    root2 = sol.insert(root2, 6)  # Insert 6
    print("Second BST after inserting 6 (inorder):", inorder(root2))  # Expect [1,2,3,5,6,7,8,9]
```

### Example run (typical output)

```
Initial BST (inorder): [1, 2, 3]
After inserting 4 (inorder): [1, 2, 3, 4]
After inserting duplicate 2 (inorder): [1, 2, 3, 4]

Total program time (incl. building, 2 inserts, traversals): 0.230 ms

Second BST (inorder): [1, 2, 3, 5, 7, 8, 9]
Second BST after inserting 6 (inorder): [1, 2, 3, 5, 6, 7, 8, 9]
```

---

# 6) Real-World Use Cases (important ones only)

1. **Ordered sets / indexes in in-memory systems**
   BSTs are the backbone of ordered containers (e.g., TreeSet/TreeMap in other languages), and of in-memory indexes where you need **fast insert** and **ordered iteration**.

2. **Autocomplete / range queries**
   Storing dictionary words, user IDs, or timestamps in a BST lets you **insert as events arrive** and then **iterate in sorted order** or **query ranges** quickly.

3. **Event schedulers / calendars**
   A BST keyed by time lets you **insert new events** while keeping everything sorted for upcoming reminders and conflict checks.

4. **Compilers & interpreters (symbol tables)**
   When balanced (AVL/RB trees), BSTs provide predictable performance for **inserting** and **looking up** identifiers while preserving order for diagnostics and optimization passes.
