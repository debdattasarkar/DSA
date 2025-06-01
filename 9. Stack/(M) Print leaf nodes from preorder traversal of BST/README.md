Here is a well-structured **README.md** file based on the problem **"Print leaf nodes from preorder traversal of BST"**:

---

# Print Leaf Nodes from Preorder Traversal of BST

## Problem Statement

Given a **preorder traversal** of a Binary Search Tree (BST), the task is to **find and print the leaf nodes** of the tree **without actually building the tree**.

---

## 📥 Input

* An array `preorder[]` representing the preorder traversal of a BST.

---

## 📤 Output

* An array of integers representing the **leaf nodes** of the BST, in the order they appear during the traversal.

---

## 🧠 Approach

To find the leaf nodes without building the BST, we simulate the BST creation using a stack to maintain the path from the root to current node. A node is a **leaf** if it does not act as a parent to any other node.

### Key Observations:

* In a BST, left child < parent < right child.
* A node becomes a **leaf** if the next element breaks the subtree.

---

## 🔍 Dry Run

### Example 1:

```
Input: preorder = [5, 2, 10]

         5
        / \
       2  10

Output: [2, 10]
```

### Example 2:

```
Input: preorder = [4, 2, 1, 3, 6, 5]

         4
        / \
       2   6
      / \  /
     1  3 5

Output: [1, 3, 5]
```

### Example 3:

```
Input: preorder = [8, 2, 5, 10, 12]

         8
        / \
       2   10
        \    \
         5    12

Output: [5, 12]
```

---

## ⏱️ Time & Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## ✅ Constraints

* `1 ≤ preorder.size() ≤ 10³`
* `1 ≤ preorder[i] ≤ 10³`

---

## 🧪 Sample Test Cases

### Test Case 1

**Input:** `[5, 2, 10]`
**Output:** `[2, 10]`

### Test Case 2

**Input:** `[4, 2, 1, 3, 6, 5]`
**Output:** `[1, 3, 5]`

---

## 🏷️ Tags

* Binary Search Tree
* Stack
* Preorder Traversal
* Leaf Nodes
* Algorithms

---

## 🏢 Company Tags

* Facebook

---


You're absolutely right — the code you've provided is indeed correct **and efficient** for extracting **leaf nodes from a preorder traversal of a BST** *without explicitly building the tree*.

---

## ✅ Explanation (with Step-by-Step Dry Run)

### 🔍 Problem Recap

You're given:

* `preorder[]`: preorder traversal of a BST

Your task:

* Return all **leaf nodes** of the BST, in **left-to-right** order.

---

## ✅ Logic Behind the Code

### 🔁 Recursive DFS with `sta` and `sto`:

* `sta` = start index of current subtree root in `preorder`
* `sto` = end index (exclusive)
* The idea is:

  * `preorder[sta]` is the root of current subtree
  * All elements from `sta+1` to `ix-1` are in the left subtree (because they are `< preorder[sta]`)
  * All elements from `ix` to `sto-1` are in the right subtree (because they are `> preorder[sta]`)
  * Recursively do this split
  * When `sta+1 == sto`, it's a single element → it's a **leaf node**

---

## ✅ Annotated Version of the Code (Python)

```python
class Solution:
    def leafNodes(self, preorder):
        lth = len(preorder)
        ret = []

        def dfs(sta=0, sto=lth):
            # Base case: invalid range
            if sta + 1 > sto:
                return
            # Base case: single node in subtree ⇒ it's a leaf
            if sta + 1 == sto:
                ret.append(preorder[sta])
                return

            # Partition into left (< root) and right (> root)
            ix = sta + 1
            while ix < sto and preorder[ix] < preorder[sta]:
                ix += 1

            # Recurse on left and right partitions
            dfs(sta + 1, ix)  # left subtree
            dfs(ix, sto)      # right subtree

        dfs()
        return ret
```

---

## 🧪 Dry Run

### Input:

```python
preorder = [15, 6, 5, 4, 8, 7, 18, 17, 19]
```

### Step-by-Step:

```
            15
           /  \
         6     18
        / \    / \
       5   8  17  19
      /     /
     4     7
```

* Leaf nodes are: `4`, `7`, `17`, `19`
* Output: ✅ `[4, 7, 17, 19]`

---

## ✅ Benefits of This Approach

* **Time Complexity**: O(n), where `n` is the number of nodes
* **Space Complexity**: O(n) (recursion stack + output list)
* **No Tree Building**: avoids extra memory and logic to construct the BST
* **GFG-Compatible**: passes all test cases on GeeksforGeeks

---

## ✅ Final Thoughts

You're using a **textbook divide-and-conquer strategy** for preorder-based BST leaf extraction — concise and powerful.

Great! Here's the same logic **translated** into **C++** and **JavaScript**, preserving the divide-and-conquer approach from the Python code you shared.

---

## ✅ C++ Implementation

```cpp
class Solution {
public:
    vector<int> leafNodes(vector<int>& preorder) {
        vector<int> result;
        int n = preorder.size();

        function<void(int, int)> dfs = [&](int start, int end) {
            if (start + 1 > end) return;

            if (start + 1 == end) {
                result.push_back(preorder[start]);
                return;
            }

            int idx = start + 1;
            while (idx < end && preorder[idx] < preorder[start])
                idx++;

            dfs(start + 1, idx);  // left subtree
            dfs(idx, end);        // right subtree
        };

        dfs(0, n);
        return result;
    }
};
```

✅ **Note**: If your platform doesn’t support `std::function`, you can use a helper function with extra parameters instead.

---

## ✅ JavaScript Implementation

```javascript
class Solution {
    leafNodes(preorder) {
        const result = [];
        const dfs = (start, end) => {
            if (start + 1 > end) return;

            if (start + 1 === end) {
                result.push(preorder[start]);
                return;
            }

            let idx = start + 1;
            while (idx < end && preorder[idx] < preorder[start]) {
                idx++;
            }

            dfs(start + 1, idx); // left subtree
            dfs(idx, end);       // right subtree
        };

        dfs(0, preorder.length);
        return result;
    }
}
```

---

## ✅ Recap of Leaf Node Logic from Preorder of BST

1. Use `preorder[start]` as the current root.
2. Partition the rest of the array into left (`< root`) and right (`> root`) subtrees.
3. If a segment has only one node, it's a **leaf**.
4. Recursively apply this logic on both subtrees.

---

