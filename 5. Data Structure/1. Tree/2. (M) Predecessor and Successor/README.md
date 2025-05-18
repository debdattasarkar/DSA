Here's a full README in Markdown format based on the problem **“Predecessor and Successor in BST”** from the provided image:

---

# Predecessor and Successor

## Introduction

The **Predecessor and Successor** problem in a **Binary Search Tree (BST)** involves finding:

* The **in-order predecessor**: the largest value smaller than a given key.
* The **in-order successor**: the smallest value greater than a given key.

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given the **root node of a BST** and an **integer key**, return the **in-order predecessor** and **in-order successor** of the key.

* If the predecessor or successor does not exist, return `NULL` (i.e., `-1` in output).

> **Note:** In an in-order traversal, the number just **smaller** than the target is the **predecessor**, and the number just **greater** than the target is the **successor**.

---

## Examples

### Example 1

```
Input: root = [8, 1, 9, N, 4, N, 10, 3], key = 8
Output: 4 9

Explanation:
In-order traversal = [1, 3, 4, 8, 9, 10]
Predecessor of 8 is 4
Successor of 8 is 9
```

---

### Example 2

```
Input: root = [10, 2, 11, 1, 5, N, N, 3, 6, 4], key = 11
Output: 10 -1

Explanation:
In-order traversal = [1, 2, 3, 4, 5, 6, 10, 11]
Predecessor of 11 is 10
Successor doesn't exist → -1
```

---

### Example 3

```
Input: root = [2, 1, 3], key = 3
Output: 2 -1

Explanation:
Predecessor is 2
No successor exists
```

---

## Constraints

* `1 ≤ Number of nodes ≤ 10^5`
* `1 ≤ Node->data ≤ 10^6`
* `1 ≤ key ≤ 10^6`

---

## Expected Complexities

* **Time Complexity**: O(Height of the BST)
* **Auxiliary Space**: O(1)

---

## Tags

### Company Tags

`Ola Cabs`

### Topic Tags

`Binary Search Tree`, `Tree`, `Data Structures`

---

## Related Content

* **Interview Experiences**:

  * Ola Interview Experience Set 6 For SDE 1

* **Article**: [Inorder Predecessor Successor Given Key BST](#)

---

Here's a **complete breakdown** of the **"Predecessor and Successor in BST"** problem with:

* ✅ Text explanation
* ✅ Step-by-step dry run
* ✅ Code in Python, C++, and JavaScript (with inline comments)

---

## 🧠 Problem Summary

Given a **Binary Search Tree** and a **key**, find:

* The **inorder predecessor**: Largest value smaller than the key.
* The **inorder successor**: Smallest value greater than the key.

### Inorder Traversal Property in BST:

* In BST, the inorder traversal results in a **sorted array**.

---

## 🔍 Algorithm Explanation

### Step 1: Traverse the BST

* If `key == root.data`:

  * For predecessor: Go **left**, then as far **right** as possible.
  * For successor: Go **right**, then as far **left** as possible.
* If `key < root.data`:

  * Current node **might be successor**, go **left**.
* If `key > root.data`:

  * Current node **might be predecessor**, go **right**.

This ensures **O(h)** time complexity.

---

## 🧪 Dry Run

### Tree:

```
       10
      /  \
     2    11
    / \
   1   5
      / \
     3   6
        /
       4
```

### Key = 11

* Predecessor = 10 (largest smaller)
* Successor = None → -1

---

## ✅ Python Code

```python
class Solution:
    def findPreSuc(self, root, key):
        pre = suc = None
        node = root

        # Find predecessor
        while node:
            if node.data < key:
                pre = node
                node = node.right
            else:
                node = node.left

        node = root
        # Find successor
        while node:
            if node.data > key:
                suc = node
                node = node.left
            else:
                node = node.right

        return (pre, suc)
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    vector<Node*> findPreSuc(Node* root, int key) {
        Node* pre = nullptr;
        Node* suc = nullptr;
        Node* node = root;

        // Find predecessor
        while (node) {
            if (node->data < key) {
                pre = node;
                node = node->right;
            } else {
                node = node->left;
            }
        }

        node = root;

        // Find successor
        while (node) {
            if (node->data > key) {
                suc = node;
                node = node->left;
            } else {
                node = node->right;
            }
        }

        return {pre, suc};
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    findPreSuc(root, key) {
        let pre = null;
        let suc = null;
        let node = root;

        // Find predecessor
        while (node) {
            if (node.data < key) {
                pre = node;
                node = node.right;
            } else {
                node = node.left;
            }
        }

        node = root;

        // Find successor
        while (node) {
            if (node.data > key) {
                suc = node;
                node = node.left;
            } else {
                node = node.right;
            }
        }

        return [pre, suc];
    }
}
```

---

## 🧩 Summary

| Term        | Meaning                             |
| ----------- | ----------------------------------- |
| Predecessor | Max value smaller than key          |
| Successor   | Min value greater than key          |
| Time        | O(height of BST) = O(log n) average |
| Space       | O(1) auxiliary                      |

Let me know if you'd like a recursive or traversal-based version too!
