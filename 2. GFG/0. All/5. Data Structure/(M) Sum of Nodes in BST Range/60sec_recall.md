# **“60-second recall kit”** 🔥
for the **Maximum Non-Adjacent Nodes Sum (Tree DP)** problem — also known as **House Robber III (Tree version)**.

---

## 🧠 5-Line Pseudo-Code Template (Universal Skeleton)

This is the **core** you can rebuild in **C++ / Java / Python / Go** instantly.

```
function dfs(node):
    if node is None: return (0, 0)
    left_take, left_skip   = dfs(node.left)
    right_take, right_skip = dfs(node.right)

    take = node.val + left_skip + right_skip
    skip = max(left_take, left_skip) + max(right_take, right_skip)
    return (take, skip)

ans_take, ans_skip = dfs(root)
return max(ans_take, ans_skip)
```

### ✅ That’s it. Exactly 7 lines of code = full logic.

---

## 🧩 Memory Hook (how to recall instantly)

### 1️⃣ Think of **2 states per node**:

* **take** → I take this node → I cannot take children.
* **skip** → I skip this node → I can take or skip children freely.

### 2️⃣ The two key formulas:

```
take = val + skip(L) + skip(R)
skip = max(take, skip)(L) + max(take, skip)(R)
```

That’s the **heart** of the problem — once you remember this, you can rebuild any language version.

---

## 🧠 Easy Mnemonic to Remember

### Phrase:

> **“Take means skip kids; Skip means take best of kids.”**

You can literally say it out loud in your head when interviewer asks:

> “What’s your recurrence relation?”

### Breakdown:

| State    | Meaning        | Formula                         | Think of it as...                  |
| -------- | -------------- | ------------------------------- | ---------------------------------- |
| **take** | If I take node | node + skip(left) + skip(right) | “I grab this one, kids rest.”      |
| **skip** | If I skip node | best(left) + best(right)        | “I skip myself, let kids compete.” |

---

## ⏱️ 60-Second Recall Routine (Before Interview)

When interviewer says *“Maximum sum with no adjacent nodes”*, mentally run this script:

1️⃣ **Tree DP → Postorder traversal** (children first).
2️⃣ Each node returns **(take, skip)** pair.
3️⃣ Formulas →
`take = val + skip(L) + skip(R)`
`skip = max(take, skip)(L) + max(take, skip)(R)`
4️⃣ Final answer → `max(take(root), skip(root))`.
5️⃣ Complexity → O(n) time, O(h) recursion.

Say it once in your head and you’re interview-ready.

---

## 🎯 Bonus “One-Liner Summary” for Interviews

> “It’s a **Tree Dynamic Programming** problem.
> For every node, I track two states — if I take it or skip it.
> `take = val + skip(left) + skip(right)`
> `skip = max(take, skip)(left) + max(take, skip)(right)`
> Answer = max(take(root), skip(root)) — O(n) time, O(h) space.”

---

## 💡 Extra Tip (for multi-problem recall)

Group similar problems by **DP state logic**:

| Category     | Key DP Idea                        | Example                       |
| ------------ | ---------------------------------- | ----------------------------- |
| **Linear**   | Choose or skip adjacent            | House Robber I                |
| **Circular** | Choose but skip first/last overlap | House Robber II               |
| **Tree**     | Skip parent if child taken         | Maximum Non-Adjacent Node Sum |

> Remember: **Linear → Circular → Tree** are all the same idea in increasing difficulty.

---

✅ **Final 5-second cue**:
When you see “no adjacent nodes” + “maximize sum” → say out loud:

> **“Postorder DP — take = val + skip kids; skip = best of kids.”**

Then start coding your 5-line DFS template confidently.