**“60-second recall kit”** and **5-line pseudo-code template** for the **Median of a BST** problem — the exact structure you can rebuild confidently in *any* language (Python, C++, Java, etc.) before or during an interview.

---

## 🧠 5-Line Pseudo-code Template (Universal Skeleton)

```
function findMedian(root):
    n = countNodes(root)                      # pass 1: count total nodes
    k = (n // 2) if n even else (n // 2 + 1)  # decide which inorder index
    count = 0
    for node in inorder(root):                # pass 2: traverse inorder
        count += 1
        if count == k: return node.value
```

✅ That’s all you need — **just two passes of inorder traversal.**
The only trick is remembering to use **Morris traversal** if interviewer asks for **O(1) space**.

---

## 🧩 Mnemonic to Remember It Instantly

> **“Count, Compute k, Come back for k.”**

1️⃣ **Count** → Count total nodes `n` (using inorder).
2️⃣ **Compute k** → `k = n//2` if even else `n//2 + 1`.
3️⃣ **Come back** → Do inorder again and stop at the k-th node.

---

## ⚙️ Optional O(1) Space Upgrade

If interviewer pushes for **O(1) auxiliary space**, replace both inorder traversals with **Morris Traversal**:

> **“Right thread → visit → remove thread → move right.”**

That lets you do the traversal without recursion or stack.

---

## ⏱️ 60-Second Pre-Interview Recall Routine

When the interviewer says:

> “Find the median of a BST.”

You think and speak this:

1️⃣ **“Inorder traversal gives sorted order.”**
2️⃣ **“We first count total nodes `n`.”**
3️⃣ **“Then find k = n//2 (even) or n//2+1 (odd).”**
4️⃣ **“Do another inorder and return the k-th visited node.”**
5️⃣ **“If asked for O(1) space, I’ll use Morris traversal for both passes.”**

💡 Optional bonus phrase:

> “If it’s even and they want the lower median, I’ll pick V(n/2); otherwise (odd) V((n+1)/2).”

---

## 🧭 Quick Example Recall

BST:

```
        20
       /  \
      8    22
     / \
    4  12
      /  \
     10  14
```

Inorder: `[4, 8, 10, 12, 14, 20, 22]`
`n = 7`, `k = 4` → **12** ✅

---

## 💬 10-Second “Why” Answer (when interviewer asks)

> “Inorder traversal of a BST gives values in sorted order, so the median is just the k-th visited node.
> Two passes — one for count, one for selection — make it O(n) time, O(1) space with Morris traversal.”

---

### ✅ Quick Cheat Sheet

| Step | What to Recall                  | Mnemonic                    |
| ---- | ------------------------------- | --------------------------- |
| 1️⃣  | Inorder = sorted                | “Inorder means order”       |
| 2️⃣  | Count total nodes               | “Count all”                 |
| 3️⃣  | Compute k (n//2 or n//2+1)      | “Middle index”              |
| 4️⃣  | Traverse again to kth           | “Come back for k”           |
| 5️⃣  | Use Morris if O(1) space needed | “Thread → Visit → Unthread” |

---

💡 **Final mantra (to say silently before coding):**

> “Count → Compute k → Come back for k.
> Inorder gives sorted, Morris gives O(1) space.” ✅
