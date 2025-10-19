Excellent 👏 — here’s your **“K Closest Values in BST” 5-line pseudo-code + 60-second recall plan**, designed exactly for interview mental recall.

---

## 🧠 **5-Line Pseudo-Code Template (Language-Agnostic)**

```
function getKClosest(root, target, k):
    inorder = []                           # Step 1: collect sorted BST values
    DFS_inorder(root, inorder)

    sort inorder by (abs(x - target), x)   # Step 2: smaller diff first, tie → smaller value
    return first k elements                # Step 3: return k closest
```

✅ **Time:** O(n log n)
✅ **Space:** O(n)

---

Now, to recall the **optimized Two-Stack version (O(h + k))**, here’s your **mental skeleton** 👇

```
function getKClosest(root, target, k):
    build preds, succs stacks near target     # Step 1: split BST around target
    result = []                               # Step 2: gather k values
    repeat k times:
        pick closer top(pred, succ)           # Step 3: abs diff check, tie → smaller
        advance that side (predecessor/successor)
    return result
```

✅ **Time:** O(h + k)
✅ **Space:** O(h)

---

## ⚡ **Easy Mnemonic to Remember Both**

> 🧩 **“Traverse → Split → Compare → Advance → Collect.”**

| Step         | Meaning                                     | Code Part                        |
| ------------ | ------------------------------------------- | -------------------------------- |
| **Traverse** | Do inorder / partial traversal              | `_init_stacks()` or DFS          |
| **Split**    | Separate ≤ target (preds), > target (succs) | build stacks                     |
| **Compare**  | Choose smaller diff (tie → smaller value)   | abs() logic                      |
| **Advance**  | Pop chosen side & move to next              | `_next_pred()` or `_next_succ()` |
| **Collect**  | Append to result                            | `result.append()`                |

---

## ⏱️ **60-Second Recall Flow Before Interview**

**0–10 sec →** “BST → closest k → by abs difference.”
**10–20 sec →** “Inorder = sorted; can do brute O(n log n) or stack O(h+k).”
**20–40 sec →** “Two stacks → predecessors (≤ target), successors (> target).”
**40–50 sec →** “Pick closer of top two; tie → smaller value → predecessor.”
**50–60 sec →** “Repeat k times; complexity O(h + k). Done ✅.”

---

## 💬 **What to Say in Interview**

> “I can solve it by doing an inorder and sorting differences — O(n log n).
> For an optimized version, I’ll maintain **two stacks** — predecessors and successors — around the target.
> Each step, I pick the side with the smaller difference (tie → smaller value).
> This gives me O(h + k) time and O(h) space.”

---

## 🧩 **Ultra-Compact “Mental Template”**

```
preds, succs = splitBST(root, target)
for i in 1..k:
    choose closer(preds[-1], succs[-1])
    advance that stack
```

Mnemonic to keep in mind → **“Split, Compare, Advance.”**
That’s the entire two-stack algorithm’s brain in 3 words.
