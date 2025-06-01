Here’s a comprehensive README in Markdown format for the **“AVL Tree Deletion”** problem, based on your uploaded image:

---

# AVL Tree Deletion

## Introduction

The **AVL Tree Deletion** problem involves implementing a deletion operation on an **AVL tree**, a self-balancing Binary Search Tree (BST). The goal is to ensure that after each deletion, the tree remains balanced by performing necessary rotations.

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

Given:

* An AVL tree.
* An integer `N`, the number of values to be deleted.
* `N` values to be deleted from the tree, one by one.

Write a function `deleteNode()` that takes:

* The **root** of the AVL tree.
* A **value to be deleted**.

After each deletion, you must return the **new root** of the tree, ensuring the AVL balance property is preserved.

> **Note**: AVL trees must maintain the balance condition where for any node, the height difference between left and right subtrees is at most 1.

---

## Examples

### Example 1

```
Initial Tree:
       4
     /   \
    2     6
   / \   / \
  1   3 5   7

Deletions: [4, 1, 3, 6]

After deleting 4:
       5
     /   \
    2     6
   / \     \
  1   3     7

After deleting 1:
       5
     /   \
    2     6
     \     \
      3     7

After deleting 3:
       5
     /   \
    2     6
             \
              7

After deleting 6:
       5
     /   \
    2     7
```

---

## Constraints

* `1 ≤ N ≤ 500`

---

## Expected Complexity

* **Time Complexity**: O(height of tree) ≈ O(log n) on average
* **Auxiliary Space**: O(height of tree)

---

## Tags

### Company Tags

`Morgan Stanley`, `Amazon`, `Snapdeal`, `MakeMyTrip`, `Oracle`, `Oxigen Wallet`

### Topic Tags

`Tree`, `AVL-Tree`, `Data Structures`, `Advanced Data Structure`

---

## Related Content

* **Article**: [Deletion In An AVL Tree](#)

---

Here’s a **step-by-step explanation**, a **dry run**, and full code solutions for **AVL Tree Deletion** in **Python, C++, and JavaScript**, all with inline comments.

---

## 🧠 AVL Tree Deletion – Explanation

### Goal:

Delete a node from an AVL tree and rebalance it if needed.

---

## 🔍 Key Concepts:

### Step 1: Perform standard BST deletion

* If node has one or no children → simply remove it.
* If node has two children → replace it with its **inorder successor**, then delete that successor.

### Step 2: Update the height of current node

```python
node.height = 1 + max(height(node.left), height(node.right))
```

### Step 3: Calculate **balance factor**

```python
balance = height(left subtree) - height(right subtree)
```

### Step 4: Apply rotations if unbalanced:

* **Left-Left (LL)**: Right rotate
* **Right-Right (RR)**: Left rotate
* **Left-Right (LR)**: Left rotate → Right rotate
* **Right-Left (RL)**: Right rotate → Left rotate

---

## 🧪 Dry Run (on deletion)

```
Initial Tree:
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Delete 4:
- Inorder successor of 4 is 5.
- Replace 4 with 5.
- Balance the tree (no rotation needed in this case)

Resulting Tree:
        5
       / \
      2   6
     / \   \
    1   3   7
```

---

## ✅ Python Code

```python
def height(node):
    return node.height if node else 0

def getBalance(node):
    return height(node.left) - height(node.right) if node else 0

def rightRotate(z):
    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def leftRotate(z):
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

def deleteNode(root, key):
    if not root:
        return root

    # Perform BST delete
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        # Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children: Get the inorder successor
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Balance the node
    balance = getBalance(root)

    # Case 1 - Left Left
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    # Case 2 - Left Right
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Case 3 - Right Right
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    # Case 4 - Right Left
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root
```

---

## ✅ C++ Code

```cpp
int height(Node* node) {
    return node ? node->height : 0;
}

int getBalance(Node* node) {
    return node ? height(node->left) - height(node->right) : 0;
}

Node* rightRotate(Node* z) {
    Node* y = z->left;
    Node* T3 = y->right;

    y->right = z;
    z->left = T3;

    z->height = 1 + max(height(z->left), height(z->right));
    y->height = 1 + max(height(y->left), height(y->right));

    return y;
}

Node* leftRotate(Node* z) {
    Node* y = z->right;
    Node* T2 = y->left;

    y->left = z;
    z->right = T2;

    z->height = 1 + max(height(z->left), height(z->right));
    y->height = 1 + max(height(y->left), height(y->right));

    return y;
}

Node* minValueNode(Node* node) {
    Node* current = node;
    while (current->left != NULL)
        current = current->left;
    return current;
}

Node* deleteNode(Node* root, int key) {
    if (!root) return root;

    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        if (!root->left || !root->right) {
            Node* temp = root->left ? root->left : root->right;
            delete root;
            return temp;
        }

        Node* temp = minValueNode(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }

    root->height = 1 + max(height(root->left), height(root->right));
    int balance = getBalance(root);

    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}
```

---

## ✅ JavaScript Code

```javascript
function height(node) {
    return node ? node.height : 0;
}

function getBalance(node) {
    return node ? height(node.left) - height(node.right) : 0;
}

function rightRotate(z) {
    let y = z.left;
    let T3 = y.right;

    y.right = z;
    z.left = T3;

    z.height = 1 + Math.max(height(z.left), height(z.right));
    y.height = 1 + Math.max(height(y.left), height(y.right));

    return y;
}

function leftRotate(z) {
    let y = z.right;
    let T2 = y.left;

    y.left = z;
    z.right = T2;

    z.height = 1 + Math.max(height(z.left), height(z.right));
    y.height = 1 + Math.max(height(y.left), height(y.right));

    return y;
}

function minValueNode(node) {
    while (node.left !== null) node = node.left;
    return node;
}

class Solution {
    deleteNode(root, key) {
        if (!root) return root;

        if (key < root.data) {
            root.left = this.deleteNode(root.left, key);
        } else if (key > root.data) {
            root.right = this.deleteNode(root.right, key);
        } else {
            if (!root.left || !root.right) {
                return root.left || root.right;
            }

            let temp = minValueNode(root.right);
            root.data = temp.data;
            root.right = this.deleteNode(root.right, temp.data);
        }

        root.height = 1 + Math.max(height(root.left), height(root.right));
        let balance = getBalance(root);

        if (balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);

        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }

        if (balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);

        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }

        return root;
    }
}
```

---

Let me know if you'd like visual examples of each rotation or unit tests for your implementation!

Absolutely! Here's a **clear and uncropped step-by-step dry run**, followed by **complete AVL deletion code** in **Python**, **C++**, and **JavaScript** — fully explained with inline comments.

---

## 🧠 AVL Tree Deletion – Concept Recap

An **AVL Tree** is a self-balancing Binary Search Tree (BST). After **deleting a node**, it must remain balanced by applying appropriate **rotations**.

### Properties:

* Each node stores a `height` value.
* The **balance factor** (BF) of a node = height(left) - height(right)
* If BF ∉ \[-1, 0, 1], **rotations** are applied.

---

## 🧪 Step-by-Step Dry Run

### Initial Tree:

```
         4
       /   \
      2     6
     / \   / \
    1   3 5   7
```

### Delete: 4

#### 1. Node 4 has **two children**

* Find **inorder successor** → **5**
* Replace 4 → 5, then **delete 5** recursively

#### 2. Delete 5 (has no child) → simply remove it

#### 3. Update heights and check balances

### Resulting Tree:

```
         5
       /   \
      2     6
     / \     \
    1   3     7
```

* Tree remains balanced → ✅

---

## ✅ Python Code (With Full Rotation Logic)

```python
def height(node):
    return node.height if node else 0

def getBalance(node):
    return height(node.left) - height(node.right) if node else 0

def rightRotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

def deleteNode(root, key):
    if not root:
        return None

    # BST delete
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        # Node with one or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Rebalance
    balance = getBalance(root)

    # LL
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    # LR
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # RR
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    # RL
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root
```

---

## ✅ C++ Code

```cpp
int height(Node* node) {
    return node ? node->height : 0;
}

int getBalance(Node* node) {
    return node ? height(node->left) - height(node->right) : 0;
}

Node* rightRotate(Node* y) {
    Node* x = y->left;
    Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = 1 + max(height(y->left), height(y->right));
    x->height = 1 + max(height(x->left), height(x->right));

    return x;
}

Node* leftRotate(Node* x) {
    Node* y = x->right;
    Node* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = 1 + max(height(x->left), height(x->right));
    y->height = 1 + max(height(y->left), height(y->right));

    return y;
}

Node* minValueNode(Node* node) {
    Node* current = node;
    while (current->left)
        current = current->left;
    return current;
}

Node* deleteNode(Node* root, int key) {
    if (!root) return root;

    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        if (!root->left)
            return root->right;
        else if (!root->right)
            return root->left;

        Node* temp = minValueNode(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }

    root->height = 1 + max(height(root->left), height(root->right));
    int balance = getBalance(root);

    // Left Left
    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);

    // Left Right
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    // Right Right
    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);

    // Right Left
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}
```

---

## ✅ JavaScript Code

```javascript
function height(node) {
    return node ? node.height : 0;
}

function getBalance(node) {
    return node ? height(node.left) - height(node.right) : 0;
}

function rightRotate(y) {
    let x = y.left;
    let T2 = x.right;

    x.right = y;
    y.left = T2;

    y.height = 1 + Math.max(height(y.left), height(y.right));
    x.height = 1 + Math.max(height(x.left), height(x.right));

    return x;
}

function leftRotate(x) {
    let y = x.right;
    let T2 = y.left;

    y.left = x;
    x.right = T2;

    x.height = 1 + Math.max(height(x.left), height(x.right));
    y.height = 1 + Math.max(height(y.left), height(y.right));

    return y;
}

function minValueNode(node) {
    while (node.left) node = node.left;
    return node;
}

class Solution {
    deleteNode(root, key) {
        if (!root) return null;

        if (key < root.data) {
            root.left = this.deleteNode(root.left, key);
        } else if (key > root.data) {
            root.right = this.deleteNode(root.right, key);
        } else {
            if (!root.left || !root.right) {
                return root.left || root.right;
            }
            let temp = minValueNode(root.right);
            root.data = temp.data;
            root.right = this.deleteNode(root.right, temp.data);
        }

        root.height = 1 + Math.max(height(root.left), height(root.right));
        let balance = getBalance(root);

        if (balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);

        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }

        if (balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);

        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }

        return root;
    }
}
```

---


