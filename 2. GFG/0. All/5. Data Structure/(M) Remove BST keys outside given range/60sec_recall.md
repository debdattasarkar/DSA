**60-second recall kit** for **“Remove BST keys outside given range [L, R]”**.

---

## 🧠 5-Line Pseudo-code (universal skeleton)

```
function trimBST(node, L, R):
    if node is None: return None
    if node.val < L: return trimBST(node.right, L, R)   # too small → go right
    if node.val > R: return trimBST(node.left,  L, R)   # too big   → go left
    node.left  = trimBST(node.left,  L, R)              # in range → trim kids
    node.right = trimBST(node.right, L, R); return node
```

That’s the whole algorithm you can recreate in any language.

---

## 🔑 One-line mnemonic

> **“Too small → right, too big → left, else keep & trim both.”**

Say it once before coding and your hands will remember the rest.

---

## ⏱️ 60-second pre-interview script (what to say + think)

1. **BST property** lets me prune whole subtrees.
2. If `node < L`, its entire left subtree `< L` → discard; **recurse right**.
3. If `node > R`, entire right subtree `> R` → discard; **recurse left**.
4. Otherwise keep node, **trim both children**, return node.
5. **Complexity**: Time **O(n)** (visit each node once), Space **O(h)** (recursion stack).

---

## ✅ Quick edge-case checklist

* All nodes out of range → returns **None** (empty tree).
* `L == R` → keep only nodes equal to that value.
* Skewed tree → recursion depth may be O(n); iterative version is possible but not needed unless asked.

---

## ⚙️ If they ask for iterative hint (one sentence)

> “Find a new root within [L, R], then walk down left and right chains, cutting left children `< L` and right children `> R` by rewiring to their in-range subtrees.”
