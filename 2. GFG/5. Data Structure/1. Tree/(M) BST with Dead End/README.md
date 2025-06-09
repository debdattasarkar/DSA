# 🌲 BST with Dead End

---

## 🧾 Problem Statement

You are given a **Binary Search Tree (BST)** containing **unique positive integers greater than 0**.

Your task is to determine whether the BST contains a **dead end**.

---

### 🔍 What is a Dead End?

A **dead end** is a **leaf node** in the BST such that **no new node can be inserted** at or below this node while maintaining:

* The **BST property**, and
* The constraint that all nodes must be **strictly greater than 0**

---

## 🧪 Examples

### Example 1:

```text
Input: root[] = [8, 5, 9, 2, 7, N, N, 1]

Tree:
        8
       / \
      5   9
     / \
    2   7
   /
  1

Output: true

Explanation:
Node 1 is a dead end because:
- No number < 1 (due to > 0 constraint)
- 1 is a leaf node and cannot have further insertions
```

---

### Example 2:

```text
Input: root[] = [8, 7, 10, 2, N, 9, 13]

Tree:
        8
       / \
      7   10
     /    / \
    2    9  13

Output: true

Explanation:
Node 9 is a dead end — cannot insert any more nodes in its valid BST range (8 < x < 10).
```

---

## 📌 Constraints

* 1 ≤ number of nodes ≤ 3000
* 1 ≤ node->data ≤ 10⁵

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(h)

---

## 🏷️ Topic Tags

`Binary Search Tree` `Tree` `Data Structures`

---

## 📚 Related Articles

* [Check Whether BST Contains Dead End – GeeksforGeeks](#)

---

Here’s a **step-by-step explanation and dry run** for the **BST with Dead End** problem, followed by implementations in **Python**, **C++**, and **JavaScript** with inline comments.

---

## 🧠 Problem Understanding

You are given a **BST** with **positive unique integers**. You need to check if it contains a **dead end**.

---

### ✅ Definition of Dead End

A **dead end** is a **leaf node** such that **no further insertion is possible**:

* You **cannot insert** any value **less than or greater than** the leaf.
* It happens when **min == max** and there's no space left to insert.

---

## 🔁 Approach (Using Min-Max Ranges)

* For each node, maintain the **range of allowed values** (`min`, `max`).
* If at any node, the allowed range becomes a single value (`min == max`), it's a **dead end**.
* Traverse recursively and check all paths.

---

## 🪜 Dry Run Example

Tree:

```
        8
       / \
      5   9
     / \
    2   7
   /
  1
```

Check leaf node `1`:

* Range to insert new value: (0,1)
* Left of 1 < 1 → invalid due to > 0
* Right of 1 > 1 → only 2 is allowed, but it exists up the tree
* ✅ Dead end

---

## ✅ Python Code

```python
class Solution:
    def isDeadEnd(self, root):
        # Helper function with min and max range
        def dfs(node, min_val, max_val):
            if not node:
                return False
            if min_val == max_val:
                return True
            # Recurse on left and right with updated bounds
            return (dfs(node.left, min_val, node.data - 1) or
                    dfs(node.right, node.data + 1, max_val))

        return dfs(root, 1, float('inf'))
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    bool dfs(Node* node, int min_val, int max_val) {
        if (!node) return false;
        if (min_val == max_val) return true;

        return dfs(node->left, min_val, node->data - 1) ||
               dfs(node->right, node->data + 1, max_val);
    }

    bool isDeadEnd(Node *root) {
        return dfs(root, 1, INT_MAX);
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    isDeadEnd(root) {
        const dfs = (node, min, max) => {
            if (!node) return false;
            if (min === max) return true;

            return dfs(node.left, min, node.data - 1) ||
                   dfs(node.right, node.data + 1, max);
        };

        return dfs(root, 1, Infinity);
    }
}
```

---

## ⏱ Time & Space Complexity

| Metric          | Value                                  |
| --------------- | -------------------------------------- |
| Time Complexity | O(n)                                   |
| Auxiliary Space | O(h) — recursive stack (height of BST) |

---

Would you like the **set-based approach** or version that lists all dead ends?

Great! Let's explore an alternative **Set-Based Approach** that not only checks if a **dead end exists**, but also lays the foundation to **list all dead-end nodes** if needed.

---

## 🧠 Set-Based Approach Explanation

We use:

* A **set of all nodes** (`all_nodes`)
* A **set of leaf nodes** (`leaf_nodes`)

### 🔍 Observation:

A **dead end** occurs if:

> `leaf in all_nodes` and both `(leaf - 1)` and `(leaf + 1)` are also in `all_nodes`.

* Since all values are **> 0**, we add a **sentinel `0`** to `all_nodes` to cover edge cases for node `1`.

---

## 🧪 Dry Run

### Input:

```
Tree:
        8
       / \
      5   9
     / \
    2   7
   /
  1
```

* `leaf_nodes = {1, 7, 9}`
* `all_nodes = {0, 1, 2, 5, 7, 8, 9}`

For `leaf = 1`:

* `0 in all_nodes`, `2 in all_nodes` ⇒ ❌ DEAD END

---

## ✅ Python Code (Set-Based)

```python
class Solution:
    def isDeadEnd(self, root):
        all_nodes = set()
        leaf_nodes = set()

        def traverse(node):
            if not node:
                return
            all_nodes.add(node.data)
            if not node.left and not node.right:
                leaf_nodes.add(node.data)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        all_nodes.add(0)  # Handle edge case for node 1

        for leaf in leaf_nodes:
            if (leaf - 1) in all_nodes and (leaf + 1) in all_nodes:
                return True
        return False
```

---

## 💠 C++ Code (Set-Based)

```cpp
class Solution {
  public:
    void collect(Node* node, unordered_set<int>& all_nodes, unordered_set<int>& leaf_nodes) {
        if (!node) return;

        all_nodes.insert(node->data);
        if (!node->left && !node->right)
            leaf_nodes.insert(node->data);

        collect(node->left, all_nodes, leaf_nodes);
        collect(node->right, all_nodes, leaf_nodes);
    }

    bool isDeadEnd(Node *root) {
        unordered_set<int> all_nodes, leaf_nodes;
        collect(root, all_nodes, leaf_nodes);
        all_nodes.insert(0); // to handle node 1 edge case

        for (int leaf : leaf_nodes) {
            if (all_nodes.count(leaf - 1) && all_nodes.count(leaf + 1))
                return true;
        }
        return false;
    }
};
```

---

## 🌐 JavaScript Code (Set-Based)

```javascript
class Solution {
    isDeadEnd(root) {
        const allNodes = new Set();
        const leafNodes = new Set();

        const traverse = (node) => {
            if (!node) return;
            allNodes.add(node.data);
            if (!node.left && !node.right) {
                leafNodes.add(node.data);
            }
            traverse(node.left);
            traverse(node.right);
        };

        traverse(root);
        allNodes.add(0); // handle node 1 case

        for (const leaf of leafNodes) {
            if (allNodes.has(leaf - 1) && allNodes.has(leaf + 1)) {
                return true;
            }
        }

        return false;
    }
}
```

---

## ⏱ Complexity

| Metric           | Value           |
| ---------------- | --------------- |
| Time Complexity  | O(n)            |
| Space Complexity | O(n) (for sets) |

---

## 🧩 Listing All Dead Ends (Optional Extension)

You can easily collect and return all such dead-end leaves:

In Python:

```python
return [leaf for leaf in leaf_nodes if (leaf - 1) in all_nodes and (leaf + 1) in all_nodes]
```

Let me know if you want a version that **prints or returns all dead-end nodes**.

Here’s the **extended version** of the solution that not only detects dead ends but also **returns a list of all dead-end nodes** in a **Binary Search Tree (BST)**.

---

## 🔍 What is a Dead End?

A **dead end** is a **leaf node** such that:

* Its valid range of insertion is **completely blocked**, i.e. `(leaf - 1)` and `(leaf + 1)` are already present in the tree (with all node values > 0).

---

## ✅ Python Code (Return All Dead Ends)

```python
class Solution:
    def getAllDeadEnds(self, root):
        all_nodes = set()
        leaf_nodes = set()

        def traverse(node):
            if not node:
                return
            all_nodes.add(node.data)
            if not node.left and not node.right:
                leaf_nodes.add(node.data)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        all_nodes.add(0)  # Add 0 to handle leaf node == 1

        # Collect all dead-end leaves
        dead_ends = []
        for leaf in leaf_nodes:
            if (leaf - 1) in all_nodes and (leaf + 1) in all_nodes:
                dead_ends.append(leaf)

        return dead_ends
```

---

## 💠 C++ Code (Return All Dead Ends)

```cpp
class Solution {
  public:
    void traverse(Node* node, unordered_set<int>& all, unordered_set<int>& leaf) {
        if (!node) return;
        all.insert(node->data);
        if (!node->left && !node->right)
            leaf.insert(node->data);
        traverse(node->left, all, leaf);
        traverse(node->right, all, leaf);
    }

    vector<int> getAllDeadEnds(Node* root) {
        unordered_set<int> all_nodes, leaf_nodes;
        traverse(root, all_nodes, leaf_nodes);
        all_nodes.insert(0);

        vector<int> result;
        for (int leaf : leaf_nodes) {
            if (all_nodes.count(leaf - 1) && all_nodes.count(leaf + 1))
                result.push_back(leaf);
        }
        return result;
    }
};
```

---

## 🌐 JavaScript Code (Return All Dead Ends)

```javascript
class Solution {
    getAllDeadEnds(root) {
        const allNodes = new Set();
        const leafNodes = new Set();

        const traverse = (node) => {
            if (!node) return;
            allNodes.add(node.data);
            if (!node.left && !node.right) {
                leafNodes.add(node.data);
            }
            traverse(node.left);
            traverse(node.right);
        };

        traverse(root);
        allNodes.add(0); // for handling node 1

        const deadEnds = [];
        for (const leaf of leafNodes) {
            if (allNodes.has(leaf - 1) && allNodes.has(leaf + 1)) {
                deadEnds.push(leaf);
            }
        }

        return deadEnds;
    }
}
```

---

## 🧪 Example

BST:

```
        8
       / \
      5   9
     / \
    2   7
   /
  1
```

Output:

```python
[1]
```

---
