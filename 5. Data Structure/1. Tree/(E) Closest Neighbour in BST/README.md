# Closest Neighbour in BST

## Problem Statement

Given the **root** of a **Binary Search Tree (BST)** and a number **k**, find the **greatest number** in the BST that is **less than or equal to k**.

---

## Examples

### Example 1

**Input:**
`root = [10, 7, 15, 2, 8, 11, 16]`
`k = 14`

**Output:**
`11`

**Explanation:**
The greatest element in the BST that is ≤ 14 is **11**.

---

### Example 2

**Input:**
`root = [5, 2, 12, 1, 3, 9, 21, N, N, N, N, N, N, 19, 25]`
`k = 24`

**Output:**
`21`

**Explanation:**
The greatest element in the BST that is ≤ 24 is **21**.

---

### Example 3

**Input:**
`root = [5, 2, 12, 1, 3, 9, 21, N, N, N, N, N, N, 19, 25]`
`k = 4`

**Output:**
`3`

**Explanation:**
The greatest element in the BST that is ≤ 4 is **3**.

---

## Constraints

* `1 <= number of nodes <= 10^5`
* `1 <= node->data, k <= 10^5`
* All nodes are unique in the BST

---

## Expected Complexity

* **Time Complexity:** O(h), where h is the height of the BST
* **Auxiliary Space:** O(h)

---

## Approach

* Start from the root of the BST.
* If `root.data <= k`, store it as a potential answer and move to the right subtree to find a potentially larger value ≤ k.
* If `root.data > k`, move to the left subtree.
* Continue this process until the node is `None`.

This uses BST properties efficiently, leading to O(h) time.

---

## Python Code

```python
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxForN(self, root, n):
        res = -1
        while root:
            if root.data <= n:
                res = root.data
                root = root.right
            else:
                root = root.left
        return res
```

---

## C++ Code

```cpp
class Solution {
  public:
    int findMaxForN(Node* root, int n) {
        int res = -1;
        while (root) {
            if (root->data <= n) {
                res = root->data;
                root = root->right;
            } else {
                root = root->left;
            }
        }
        return res;
    }
};
```

---

## JavaScript Code

```javascript
class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    findMaxForN(root, n) {
        let res = -1;
        while (root) {
            if (root.data <= n) {
                res = root.data;
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return res;
    }
}
```

---

## Tags

* Binary Search Tree
* Tree
* Data Structures

---