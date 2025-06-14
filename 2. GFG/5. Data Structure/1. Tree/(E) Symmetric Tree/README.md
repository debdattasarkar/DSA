
---

# 🌳 Symmetric Tree

**Difficulty:** Easy
**Topics:** Tree, Data Structures
**Tags:** Amazon, Microsoft

---

## 🧩 Problem Statement

Given the `root` of a binary tree, check whether it is **symmetric**. A binary tree is said to be symmetric if the left subtree is a **mirror reflection** of the right subtree.

---

## 🧪 Examples

### Example 1:

```
Input:
  root[] = [1, 2, 2, 3, 4, 4, 3]

Output:
  True

Explanation:
  Left subtree = [2, 3, 4]
  Right subtree = [2, 4, 3]
  They are mirror images.
```

### Example 2:

```
Input:
  root[] = [1, 2, 2, null, 3, null, 3]

Output:
  False

Explanation:
  Asymmetric due to nulls and 3s being placed asymmetrically.
```

---

## 🧠 Approach

We recursively check if the **left subtree of one node** is a **mirror** of the **right subtree** of the other node and vice versa.

---

## 🔄 Recursive Mirror Check

```python
def isMirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (t1.val == t2.val) and \
           isMirror(t1.left, t2.right) and \
           isMirror(t1.right, t2.left)
```

Then call:

```python
return isMirror(root.left, root.right)
```

---

## 📊 Time and Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space (Recursion Stack):** O(h) — h is tree height

---

## 💻 Python Code

```python
class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))
        
        return isMirror(root, root)
```

---

## 💻 C++ Code

```cpp
class Solution {
public:
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        return (t1->val == t2->val) &&
               isMirror(t1->left, t2->right) &&
               isMirror(t1->right, t2->left);
    }

    bool isSymmetric(TreeNode* root) {
        return isMirror(root, root);
    }
};
```

---

## 💻 JavaScript Code

```javascript
class Solution {
    isSymmetric(root) {
        function isMirror(t1, t2) {
            if (!t1 && !t2) return true;
            if (!t1 || !t2) return false;
            return (t1.val === t2.val &&
                    isMirror(t1.left, t2.right) &&
                    isMirror(t1.right, t2.left));
        }
        return isMirror(root, root);
    }
}
```

---

## 🧠 Key Insight

A tree is symmetric if `left` and `right` subtree are **mirror** of each other at every level.

---

Here’s a detailed explanation and dry run for the **Symmetric Tree** problem followed by code for **Python**, **C++**, and **JavaScript** with inline comments:

---

## ✅ Problem Explanation

Given the `root` of a binary tree, check whether it is **symmetric**, i.e., a **mirror image of itself**.

### ➕ A tree is symmetric if:

* Left subtree is a mirror reflection of the right subtree.
* For every node:
  `left.left == right.right` and `left.right == right.left`

---

## 🔍 Step-by-Step Dry Run

Let's take an example:

```
        1
      /   \
     2     2
    / \   / \
   3   4 4   3
```

**Step-by-step check:**

* Compare `1` with `1` → ✅ Same
* Check mirror:

  * `2 (left)` vs `2 (right)` → ✅

    * `3 (left.left)` vs `3 (right.right)` → ✅
    * `4 (left.right)` vs `4 (right.left)` → ✅

Hence the tree is **symmetric** ✅

---

## 🧠 Recursive Idea

Write a helper function `isMirror(t1, t2)`:

* If both nodes are null → True
* If one is null and other is not → False
* Check values and recurse:

  * Left of `t1` vs Right of `t2`
  * Right of `t1` vs Left of `t2`

---

## 🐍 Python Code

```python
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.data == t2.data and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        
        return isMirror(root, root)
```

---

## 💠 C++ Code

```cpp
/*
class Node {
public:
    int data;
    Node *left, *right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};
*/

class Solution {
  public:
    bool isMirror(Node* t1, Node* t2) {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        return (t1->data == t2->data &&
                isMirror(t1->left, t2->right) &&
                isMirror(t1->right, t2->left));
    }

    bool isSymmetric(Node* root) {
        return isMirror(root, root);
    }
};
```

---

## 🟨 JavaScript Code

```javascript
/*
class Node
{
    constructor(x){
        this.key = x;
        this.left = null;
        this.right = null;
    }
}
*/

class Solution {
    isSymmetric(root) {
        function isMirror(t1, t2) {
            if (!t1 && !t2) return true;
            if (!t1 || !t2) return false;
            return (
                t1.key === t2.key &&
                isMirror(t1.left, t2.right) &&
                isMirror(t1.right, t2.left)
            );
        }

        return isMirror(root, root);
    }
}
```

---

## ⏱ Time & Space Complexity

| Aspect            | Value                 |
| ----------------- | --------------------- |
| Time Complexity   | O(n)                  |
| Space (recursive) | O(h) — height of tree |

Let me know if you want the **iterative version** using queue!
