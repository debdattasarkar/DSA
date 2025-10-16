**BST → Greater Sum Tree** (each node becomes sum of all greater nodes).

---

## 🧠 5-Line Pseudo-code Template (universal, rebuild in 30s)

```
function transformBST(node):
    if node is None: return
    transformBST(node.right)       # visit larger nodes first
    original = node.val
    node.val = totalSum            # replace with sum of greater keys
    totalSum += original           # add this node to running sum
    transformBST(node.left)        # then visit smaller nodes
```

✅ That’s the **entire logic** in 5 lines.

---

## 🔑 Mnemonic to Instantly Recall

> **“Right → Write → Add → Left.”**

Or in words:

1. **Right** → Go right (bigger numbers first).
2. **Write** → Replace node with running sum.
3. **Add** → Add this node’s original value to total sum.
4. **Left** → Go left (smaller values next).

This phrase ensures you remember the order and update sequence!

---

## ⚙️ Mental Model (Intuitive Visualization)

Picture BST in **descending order traversal**:
Largest → ... → Smallest

Keep a “bucket” (suffix sum).
Each time you visit a node:

* its **new value = what’s currently in the bucket**
* then **you pour its old value into the bucket**.

By the time you finish, every node has “how much is greater than me.”

---

## ⏱️ 60-Second Pre-Interview Recap

When interviewer says:

> “Convert BST to Greater Sum Tree.”

Think aloud:

1. **“BST inorder = ascending, so reverse inorder = descending.”**
2. **“I’ll keep a running suffix sum.”**
3. **“For each node: replace it with sum_so_far, then add its own value.”**
4. **“That’s Right → Write → Add → Left traversal.”**
5. **“O(n) time, O(h) recursion.”**

Then start coding confidently.

---

## ✅ Summary Table for Quick Memory

| Step | Action                       | Purpose                     | Mnemonic                     |
| ---- | ---------------------------- | --------------------------- | ---------------------------- |
| 1    | Go **Right**                 | Visit larger elements first | “R”                          |
| 2    | **Write** node = totalSum    | Replace current node value  | “W”                          |
| 3    | **Add** original to totalSum | Accumulate                  | “A”                          |
| 4    | Go **Left**                  | Move to smaller             | “L”                          |
| 5    | Repeat                       | Until tree complete         | “Right → Write → Add → Left” |

---

### Example mental snapshot:

For `[2, 1, 6, N, N, 3, 7]`
reverse inorder = 7 → 6 → 3 → 2 → 1
keep adding → new tree values = [16, 18, 7, N, N, 13, 0].

---

### 💬 Bonus “10-second answer” if interviewer asks for summary:

> “I’ll do a **reverse inorder traversal** (Right→Node→Left),
> maintain a running sum of visited nodes,
> and update each node to that running sum before adding its own value —
> effectively replacing it with the sum of all greater nodes.” ✅

---
