Here is the **README** file generated for the **Burning Tree** problem as described in the provided image:

---

# 🔥 Burning Tree

## 📝 Problem Statement

Given a binary tree and a **target node**, determine the **minimum time required** to burn the entire tree if the target node is initially set on fire.

At each second, the fire spreads from a burning node to its:

* Left child
* Right child
* Parent

> 🔹 The tree contains **unique values**.

---

## 📌 Examples

### Example 1

**Input:**
`root[] = [1, 2, 3, 4, 5, 6, 7], target = 2`

**Tree Representation:**

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

**Output:** `3`
**Explanation:**

* At 0 sec: Node 2 is burning
* At 1 sec: Nodes 1, 4, 5 catch fire
* At 2 sec: Node 3 catches fire
* At 3 sec: Nodes 6, 7 catch fire
  ✅ It takes **3 seconds** to burn the whole tree.

---

### Example 2

**Input:**
`root[] = [1, 2, 3, 4, 5, N, 7, 8, N, 10], target = 10`

**Tree Representation:**

```
           1
         /   \
        2     3
       / \     \
      4   5     7
     /         /
    8         10
```

**Output:** `5`
**Explanation:**

* At 0 sec: Node 10
* At 1 sec: Node 5
* At 2 sec: Node 2
* At 3 sec: Nodes 1 and 4
* At 4 sec: Nodes 3 and 8
* At 5 sec: Node 7
  ✅ It takes **5 seconds** to burn the whole tree.

---

## 🔒 Constraints

* `1 ≤ number of nodes ≤ 10^5`
* `1 ≤ node->data ≤ 10^5`

---

## ⏱️ Expected Time & Space Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(h) where h = height of the tree

---

## 🧠 Topic Tags

* Tree
* BFS
* Data Structures
* Algorithms

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft
* Adobe

---

## 💼 Related Interview Experiences

* Adobe Interview Experience – Adobe For Women

---

## 📚 Related Articles

* [Minimum Time to Burn a Tree Starting From a Leaf Node](#)

---

Here's a complete solution for the **"Burning Tree"** problem, including:

* ✅ Clear explanation
* ✅ Step-by-step dry run
* ✅ Implementations in **Python**, **C++**, and **JavaScript**, with inline comments

---

## 🔥 Problem Summary

You are given a binary tree and a **target node**. If the target catches fire, it spreads each second to its:

* Left child
* Right child
* Parent

Determine the **minimum time** to burn the entire tree.

---

## 🔍 Strategy & Key Concepts

1. **Build a parent mapping**: So we can move upward from any node.
2. **Locate the target node**.
3. **BFS traversal** from target using a queue and a `visited` set.
4. At each level of BFS = 1 second of fire spread.

---

## 🧪 Dry Run

### Input:

Tree =

```
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
```

**Target = 2**

### Step-by-Step Fire Spread

| Time | Burning Nodes |
| ---- | ------------- |
| 0s   | 2             |
| 1s   | 1, 4, 5       |
| 2s   | 3             |
| 3s   | 6, 7          |

✅ Output: `3 seconds`

---

## ✅ Python Code

```python
from collections import deque

class Solution:
    def minTime(self, root, target):
        def map_parents(node, parent_map):
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                if curr.left:
                    parent_map[curr.left] = curr
                    queue.append(curr.left)
                if curr.right:
                    parent_map[curr.right] = curr
                    queue.append(curr.right)

        def find_target(node, target):
            if not node:
                return None
            if node.data == target:
                return node
            return find_target(node.left, target) or find_target(node.right, target)

        parent_map = {}
        map_parents(root, parent_map)
        target_node = find_target(root, target)

        queue = deque([target_node])
        visited = set([target_node])
        time = 0

        while queue:
            size = len(queue)
            new_fire = False
            for _ in range(size):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent_map.get(node)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        new_fire = True
            if new_fire:
                time += 1

        return time
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int minTime(Node* root, int target) {
        unordered_map<Node*, Node*> parent;
        queue<Node*> q;
        q.push(root);

        // Step 1: Map parent references
        while (!q.empty()) {
            Node* curr = q.front(); q.pop();
            if (curr->left) {
                parent[curr->left] = curr;
                q.push(curr->left);
            }
            if (curr->right) {
                parent[curr->right] = curr;
                q.push(curr->right);
            }
        }

        // Step 2: Find the target node
        function<Node*(Node*)> findTarget = [&](Node* node) -> Node* {
            if (!node) return nullptr;
            if (node->data == target) return node;
            Node* left = findTarget(node->left);
            return left ? left : findTarget(node->right);
        };
        
        Node* targetNode = findTarget(root);

        // Step 3: BFS
        unordered_set<Node*> visited;
        q.push(targetNode);
        visited.insert(targetNode);
        int time = 0;

        while (!q.empty()) {
            int size = q.size();
            bool spread = false;
            while (size--) {
                Node* node = q.front(); q.pop();
                for (Node* neighbor : {node->left, node->right, parent[node]}) {
                    if (neighbor && visited.find(neighbor) == visited.end()) {
                        visited.insert(neighbor);
                        q.push(neighbor);
                        spread = true;
                    }
                }
            }
            if (spread) time++;
        }

        return time;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    minTime(root, target) {
        const mapParents = (node, parentMap) => {
            let q = [node];
            while (q.length) {
                let curr = q.shift();
                if (curr.left) {
                    parentMap.set(curr.left, curr);
                    q.push(curr.left);
                }
                if (curr.right) {
                    parentMap.set(curr.right, curr);
                    q.push(curr.right);
                }
            }
        };

        const findTarget = (node, target) => {
            if (!node) return null;
            if (node.key === target) return node;
            return findTarget(node.left, target) || findTarget(node.right, target);
        };

        let parentMap = new Map();
        mapParents(root, parentMap);
        let targetNode = findTarget(root, target);

        let q = [targetNode];
        let visited = new Set([targetNode]);
        let time = 0;

        while (q.length) {
            let size = q.length;
            let fireSpread = false;
            while (size--) {
                let node = q.shift();
                for (let neighbor of [node.left, node.right, parentMap.get(node)]) {
                    if (neighbor && !visited.has(neighbor)) {
                        visited.add(neighbor);
                        q.push(neighbor);
                        fireSpread = true;
                    }
                }
            }
            if (fireSpread) time++;
        }

        return time;
    }
}
```

---

## ⏱️ Time and Space Complexity

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

---



