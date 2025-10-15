**“60-second recall kit”** and **5-line pseudo-code skeleton** for the **k-th Smallest Element in a BST** problem — the version interviewers love because it tests your understanding of **BST + inorder traversal**.

---

## 🧠 5-Line Pseudo-Code Template (Universal)

This is the exact minimal skeleton that works in **any language** (Python, C++, Java, etc.).
Just recall this and fill in the syntax.

```
function kthSmallest(root, k):
    stack = []
    node = root
    count = 0

    while node or stack:
        while node:
            push node to stack
            node = node.left

        node = pop from stack
        count += 1
        if count == k: return node.value
        node = node.right

    return -1
```

✅ That’s literally all you need for iterative inorder.

---

## 🧩 Memory Hook (to recall the logic fast)

### 1️⃣ The core idea

> **“Inorder of BST gives sorted order.”**
> So if you count during inorder traversal, the **k-th** visit = **k-th smallest**.

### 2️⃣ Mnemonic phrase to memorize

> **“Go left, visit, go right — count the k-th visit.”**

Say it out loud once:

> “Go left till none, pop, count, go right.”

This phrase **maps exactly** to your code logic:

| Step | Mnemonic | Code                                             |
| ---- | -------- | ------------------------------------------------ |
| 1    | Go left  | `while node: stack.push(node); node = node.left` |
| 2    | Pop      | `node = stack.pop()`                             |
| 3    | Count    | `count += 1; if count == k: return node.value`   |
| 4    | Go right | `node = node.right`                              |

---

## ⚙️ Key Concepts to Recall in <30s

| Concept              | Recall                             |
| -------------------- | ---------------------------------- |
| **Traversal Type**   | Inorder (Left → Node → Right)      |
| **Why Inorder?**     | Because BST inorder = sorted order |
| **When to Return**   | When `count == k`                  |
| **Space Complexity** | O(h) stack (height of tree)        |
| **Time Complexity**  | O(h + k), worst O(n)               |
| **Edge Case**        | If `k` > #nodes → return -1        |
| **Alternative**      | Morris traversal for O(1) space    |

---

## ⏱️ 60-Second Pre-Interview Recall Routine

When interviewer says:

> “Find k-th smallest in a BST”

You quickly recall this pattern mentally:

> 🧩 “BST + inorder = sorted → k-th visit = answer.”
> 🪜 “Iterative inorder using stack:
> 1️⃣ Go left till None
> 2️⃣ Pop node
> 3️⃣ Count
> 4️⃣ If count == k → return value
> 5️⃣ Go right”

Then say:

> “Time O(h + k), Space O(h).
> Morris traversal gives O(1) space version if needed.”

Boom 💥 — you can now confidently start coding.

---

## 🧭 Bonus — “If you forget the code logic”

If your brain freezes in the interview, visualize this:

```
        5
       / \
      3   7
     / \   \
    2   4   8
```

Inorder = 2, 3, 4, 5, 7, 8
Counting left → right, k-th = simple counting.

So just say to yourself:

> “Keep pushing left → pop → count → move right.”

Even if you blank out, this 4-step mental image rebuilds the logic instantly.

---

### ✅ TL;DR (Fast Recall Sheet)

| Category             | One-liner                            |
| -------------------- | ------------------------------------ |
| **Core Rule**        | Inorder traversal gives sorted order |
| **Algorithm**        | Iterative inorder using stack        |
| **Key Mnemonic**     | “Go left, pop, count, go right”      |
| **Return Condition** | count == k                           |
| **Time / Space**     | O(h + k) / O(h)                      |
| **Upgrade**          | Morris traversal for O(1) space      |
| **Fallback**         | Recursive inorder counter            |

---

💡 **Final 10-second Self-Talk Before Interview**

> “BST + inorder = sorted.
> Stack + while loop = iterative inorder.
> Count visits → return on k-th.
> O(h + k) time, O(h) space.”
