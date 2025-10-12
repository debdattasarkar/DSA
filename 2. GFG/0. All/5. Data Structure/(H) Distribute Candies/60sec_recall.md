Perfect 👏 — here’s the **5-line pseudo-code memory template** for the **Distribute Candies in a Binary Tree** problem.

You can literally recall or rebuild this in **<30 seconds** during an interview — it captures the *entire* logic pattern.

---

## 🧠 5-Line “DFS-Balance” Pseudo-Code Template

```
moves = 0                          # Global tracker for total moves

function dfs(node):
    if node is None: return 0      # Base case — no candies, no flow

    left = dfs(node.left)          # Process left subtree
    right = dfs(node.right)        # Process right subtree

    moves += abs(left) + abs(right) # Add flows from both subtrees
    return node.val - 1 + left + right  # Net candies to pass up

dfs(root)
return moves
```

---

### 🔑 Memory Hooks

| Concept                 | Mnemonic                                    |
| ----------------------- | ------------------------------------------- |
| **Postorder traversal** | “Left → Right → Node” (bottom-up balancing) |
| **Formula for balance** | “Have - Need + Child flows”                 |
| **Counting moves**      | “Add absolute imbalance of children”        |
| **Return from DFS**     | “Net candies left after balancing subtree”  |
| **Total result**        | “Sum of all absolute child flows”           |

---

### 🧩 Example Walkthrough Reminder

For this tree:

```
        5
       / \
      0   0
         / \
        0   0
```

* Bottom nodes (0s) each return `-1`
* Parent of (0,0) returns `0 - 1 + (-1) + (-1) = -3`
* Root: `5 - 1 + (-1) + (-3) = 0` (balanced)
* Total moves = `abs(-1)+abs(-1)+abs(-3)+abs(-1)+abs(-1)=6`

✅ Matches expected answer.

---

### ⚙️ Complexity

* **Time:** O(n) → each node visited once
* **Space:** O(h) → recursion depth (height of tree)

---

### 💡 Real-World Analogy

If each node is a **server**, and candies are **load units**,
→ this algorithm minimizes **data transfer** needed to equalize load across the hierarchy.

---

