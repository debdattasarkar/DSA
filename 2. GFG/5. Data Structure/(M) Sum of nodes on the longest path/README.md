# 📘 Sum of Nodes on the Longest Path

## 🧩 Problem Statement

Given a binary tree represented as an array `root[]`, find the **sum of the nodes** on the **longest path** from the **root** to any **leaf node**.

If two or more paths have the same length, the path with the **maximum sum of node values** should be considered.

---

## 📥 Input

* A binary tree in level-order format (e.g., `[4, 2, 5, 7, 1, 2, 3, N, N, 6, N]`).
* `'N'` denotes a null/missing node.

---

## 📤 Output

* An integer representing the sum of the nodes on the longest path from root to any leaf.

---

## 🔍 Examples

### Example 1

```
Input:  [4, 2, 5, 7, 1, 2, 3, N, N, 6, N]
Output: 13
Explanation: Longest path is 4 → 2 → 1 → 6 → sum = 13
```

### Example 2

```
Input:  [1, 2, 3, 4, 5, 6, 7]
Output: 11
Explanation: Longest path is 1 → 3 → 7 → sum = 11
```

### Example 3

```
Input:  [10, 5, 15, 3, 7, N, 20, 1]
Output: 19
Explanation: Longest path is 10 → 5 → 3 → 1 → sum = 19
```

---

## 🔧 Constraints

* `1 <= number of nodes <= 10^6`
* `0 <= node->data <= 10^4`

---

## ⏱️ Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

---

## 🚀 Approach

### Step-by-step logic:

1. Traverse the tree in **depth-first search (DFS)** manner.
2. At each node:

   * Get the longest path length and sum from left and right subtrees.
3. Choose the **longer** path.

   * If lengths are equal, pick the path with the **maximum sum**.
4. Return the sum of the selected path + current node’s value.

---

## ✅ Python Code

```python
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # Helper function to return (length, sum)
        def dfs(node):
            if not node:
                return (0, 0)
            left_len, left_sum = dfs(node.left)
            right_len, right_sum = dfs(node.right)
            
            if left_len > right_len:
                return (left_len + 1, left_sum + node.data)
            elif right_len > left_len:
                return (right_len + 1, right_sum + node.data)
            else:
                return (left_len + 1, max(left_sum, right_sum) + node.data)
        
        return dfs(root)[1]
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    pair<int, int> dfs(Node* root) {
        if (!root) return {0, 0};
        
        auto left = dfs(root->left);
        auto right = dfs(root->right);
        
        if (left.first > right.first)
            return {left.first + 1, left.second + root->data};
        else if (right.first > left.first)
            return {right.first + 1, right.second + root->data};
        else
            return {left.first + 1, max(left.second, right.second) + root->data};
    }
    
    int sumOfLongRootToLeafPath(Node* root) {
        return dfs(root).second;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    sumOfLongRootToLeafPath(root) {
        function dfs(node) {
            if (!node) return [0, 0];
            
            let [leftLen, leftSum] = dfs(node.left);
            let [rightLen, rightSum] = dfs(node.right);
            
            if (leftLen > rightLen) return [leftLen + 1, leftSum + node.data];
            if (rightLen > leftLen) return [rightLen + 1, rightSum + node.data];
            return [leftLen + 1, Math.max(leftSum, rightSum) + node.data];
        }
        return dfs(root)[1];
    }
}
```

---

## 🧠 Key Insights

* Perform **post-order traversal** to collect info from subtrees.
* Comparing **length first**, then **sum** is crucial for correctness.

---

## 🏷️ Tags

* Tree
* DFS
* Recursion
* Path Sum

---
