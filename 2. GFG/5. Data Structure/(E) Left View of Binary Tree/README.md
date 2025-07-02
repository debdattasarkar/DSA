
---

# 🌳 Left View of Binary Tree

### 🟢 Difficulty: Easy

**Accuracy:** 33.74%
**Submissions:** 565K+
**Points:** 2
**Average Time:** 20 min

---

## 🧩 Problem Statement

You are given the **root of a binary tree**. Your task is to **return the left view** of the binary tree.

* The **left view** of a binary tree is the set of **nodes visible when the tree is viewed from the left side**.
* If the tree is empty, return an **empty list**.

---

## 🔍 Examples

### Example 1:

**Input:**
`root[] = [1, 2, 3, 4, 5, N, N]`

```
        1
       / \
      2   3
     / \
    4   5
```

**Output:**
`[1, 2, 4]`
**Explanation:**
From the left side of the tree, only nodes `1`, `2`, and `4` are visible.

---

### Example 2:

**Input:**
`root[] = [1, 2, 3, N, N, 4, N, 5, N, N]`

```
        1
       / \
      2   3
           \
            4
           /
          5
```

**Output:**
`[1, 2, 4, 5]`
**Explanation:**
From the left side of the tree, the nodes `1`, `2`, `4`, and `5` are visible.

---

### Example 3:

**Input:**
`root[] = [N]`
**Output:**
`[]`

---

## 🔒 Constraints

* `0 ≤ number of nodes ≤ 10⁶`
* `0 ≤ node.data ≤ 10⁵`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)` (for level order traversal)

---

## 💼 Company Tags

`Paytm`, `Flipkart`, `Accolite`, `Amazon`, `OYO Rooms`, `Samsung`,
`Snapdeal`, `MakeMyTrip`, `Ola Cabs`, `Adobe`, `Qualcomm`, `Twitter`, `Knowlarity`, `Open Solutions`

---

## 🧠 Topic Tags

* Tree
* Data Structures

---

## 📚 Related Articles

* [Print Left View Binary Tree](https://www.geeksforgeeks.org/print-left-view-binary-tree/)

---

## 📘 Explanation with Step-by-Step Dry Run

We perform a **level order traversal** using a queue. For each level, we **add the first node (leftmost)** encountered to the result.

---

### 🧪 Dry Run

#### Tree:

```
        1
       / \
      2   3
     / \
    4   5
```

* **Level 0:** `[1]` → Add `1`
* **Level 1:** `[2, 3]` → Add `2`
* **Level 2:** `[4, 5]` → Add `4`

✅ Output: `[1, 2, 4]`

---

## ✅ Optimized Solutions

---

### 🐍 Python

```python
'''
# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

# Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
```

---

### 💠 C++

```cpp
/* A binary tree node
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};
*/

class Solution {
  public:
    vector<int> leftView(Node *root) {
        vector<int> result;
        if (!root) return result;

        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; ++i) {
                Node* node = q.front();
                q.pop();
                if (i == 0)
                    result.push_back(node->data);
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
        }

        return result;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {Node} root
 * @returns {number[]}
 */

/*
class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
*/

class Solution {
    leftView(root) {
        if (!root) return [];

        let result = [];
        let queue = [root];

        while (queue.length > 0) {
            let levelSize = queue.length;
            for (let i = 0; i < levelSize; i++) {
                let node = queue.shift();
                if (i === 0) {
                    result.push(node.data);
                }
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
        }

        return result;
    }
}
```

---

# With Class Node

---

## ✅ Optimized Code

---

### 🐍 Python

```python
# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
```

---

### 💠 C++

```cpp
/* A binary tree node */

struct Node {
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};

class Solution {
  public:
    vector<int> leftView(Node *root) {
        vector<int> result;
        if (!root) return result;

        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; ++i) {
                Node* node = q.front();
                q.pop();
                if (i == 0)
                    result.push_back(node->data);
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }
        }
        return result;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {Node} root
 * @returns {number[]}
 */

class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    leftView(root) {
        if (!root) return [];

        const result = [];
        const queue = [root];

        while (queue.length > 0) {
            const levelSize = queue.length;
            for (let i = 0; i < levelSize; i++) {
                const node = queue.shift();
                if (i === 0) result.push(node.data);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
        }

        return result;
    }
}
```

---

## 💬 Interview Questions & Answers

---

### ❓Q1. What is the left view of a binary tree?

**A:** It is the set of nodes visible when the tree is viewed from the **left side** — one node per level (leftmost).
 The left view contains the **leftmost node at each level** of the binary tree when viewed from the left side.

---

### ❓Q2. Why is BFS (level order traversal) used here?

**A:** Because we want to detect the **first node at every level**, and BFS processes nodes level by level.

---

### ❓Q3: What traversal strategy is used to get the left view?

**A:** **Level-order traversal (BFS)** using a queue, and picking the **first node of every level**.

---

### ❓Q4. Can DFS be used instead?

**A:** Yes, by using **preorder traversal (root-left-right)** and keeping track of the maximum level reached, you can implement it using DFS too.

---

### ❓Q5. What is the space complexity of this approach?

**A:** O(n) for queue (in worst case for a complete binary tree).

---

### ❓Q6. Can the solution handle 10⁶ nodes?

**A:** Yes, both time and space complexities are linear, which makes the solution efficient for the given constraints.

---





---

### ❓Q3: Can we solve this using DFS?

**A:** Yes, using **preorder traversal** and keeping track of the maximum level visited.

---

### ❓Q4: What is the time and space complexity?

* **Time Complexity:** `O(n)` (each node is visited once)
* **Space Complexity:** `O(n)` (queue can hold up to n nodes in worst case)

---

### ❓Q5: Can this handle large trees (10⁶ nodes)?

**A:** Yes, it uses linear space and time — scalable for large inputs.

---
