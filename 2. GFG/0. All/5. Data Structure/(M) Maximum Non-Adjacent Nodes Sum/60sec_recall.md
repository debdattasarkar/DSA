# **“60-second recall”** for **Maximum Non-Adjacent Nodes Sum** (House Robber on Tree).
This includes a **5-line universal pseudo-code template** + a **mnemonic** so you can reconstruct the code instantly in any language (Python, C++, Java…).

---

## 🧠 60-Second Recall — How to Rebuild in an Interview

### 🪜 Step 1 — Know what you’re solving

> “Pick a subset of tree nodes (no parent–child together) that maximizes total sum.”

Immediately think:
➡ This is *House Robber on Trees.*

So: **for each node → two states:**

* **take:** include this node, skip children
* **skip:** exclude this node, freely choose for children

---

### ⚙️ Step 2 — The 5-Line Pseudo-Code Template

```
moves = function dfs(node):
    if node == null: return (0, 0)             # base case

    left_take, left_skip   = dfs(node.left)    # postorder
    right_take, right_skip = dfs(node.right)

    take = node.val + left_skip + right_skip   # if take node, skip children
    skip = max(left_take, left_skip) + max(right_take, right_skip)

    return (take, skip)

return max(dfs(root))                          # answer at root
```

✅ Works in any language — just rename variables & tuple to struct/pair/list.

---

### 🧩 Step 3 — Easy Mnemonic: **“Take–Skip–Max–Skip–Max”**

Remember this rhythm:

> **Take = Node + Skip(L) + Skip(R)**
> **Skip = Max(L) + Max(R)**

That’s it.

If you blank out:

1. Write “take” on one line, “skip” on the next.
2. Fill in:

   * “take” uses `skip`s (because we can’t take children)
   * “skip” uses `max`s (because we can choose best from each child).

Boom—you’re back in business.

---

### ⏱️ Step 4 — Quick Complexity Recall

| Metric | Value    | Mnemonic                         |
| ------ | -------- | -------------------------------- |
| Time   | **O(n)** | each node visited once           |
| Space  | **O(h)** | recursion stack (height of tree) |

> “One DFS, two states per node, done.”

---

### 🧮 Step 5 — 10-Second Dry Run (mentally)

```
        1
       / \
      2   3
     /   / \
    4   5   6
```

At leaves (4,5,6): `(take,skip)=(val,0)`
At 2: `take=2+skip(4)=2`, `skip=max(4,0)=4`
At 3: `take=3+skip(5)+skip(6)=3`, `skip=max(5,0)+max(6,0)=11`
At 1: `take=1+skip(2)+skip(3)=1+4+11=16`, `skip=max(2,4)+max(3,11)=15`
✅ Answer = `max(16,15)=16`.

---

## ⚡ “Visual Flashcard” Summary

| Concept    | One-Line Recall                                      |
| ---------- | ---------------------------------------------------- |
| Problem    | Tree version of House Robber                         |
| Recursion  | Postorder DFS                                        |
| Formula    | take = val + skip(L)+skip(R)<br>skip = max(L)+max(R) |
| Return     | max(take, skip)                                      |
| Time/Space | O(n) / O(h)                                          |
| Mnemonic   | **“Take uses skip; skip uses max.”**                 |

---

If you rehearse saying that last mnemonic —

> “Take uses skip, skip uses max”
> you’ll *always* be able to derive the recurrence and code on the spot.
