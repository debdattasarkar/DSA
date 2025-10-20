**“5-line pseudo-code + 60-second recall” kit** for the **Number of BST from Array** problem (easy to rebuild in any language in <30 seconds).

---

## 🧠 **5-Line Pseudo-Code Template**

```
function countBSTs(arr):
    sort(arr); rank[v] = index in sorted arr
    precompute Catalan[0..n]           # C[0]=1, C[k]=Σ C[i]*C[k-1-i]
    for each x in arr:
        L = rank[x]                    # smaller count
        R = n - 1 - L                  # greater count
        ans[i] = Catalan[L] * Catalan[R]
    return ans
```

✅ **Time:** O(n²) (Catalan DP) + O(n log n) (sort)
✅ **Space:** O(n)

---

## ⚡ **Mnemonic to Instantly Recall**

> **“Sort → Rank → Catalan → Multiply → Return.”**

| Step         | Meaning                             | Example     |
| ------------ | ----------------------------------- | ----------- |
| **Sort**     | Get ordered array                   | `[1,2,3]`   |
| **Rank**     | Count smaller/greater for each root | `L, R`      |
| **Catalan**  | Precompute unique BST counts        | `C[0..n]`   |
| **Multiply** | Independent subtrees ⇒ multiply     | `C[L]*C[R]` |
| **Return**   | Output per root                     | `[1,2,2]`   |

Mnemonic phrase to say aloud before you code:

> **“Sort it, Rank it, Catalan it, Multiply, Return.”**

---

## ⏱️ **60-Second Recall Plan**

| Time        | Step                                                             | What to think/say |
| ----------- | ---------------------------------------------------------------- | ----------------- |
| **0–10 s**  | “We need #BSTs per root = left × right Catalans.”                |                   |
| **10–20 s** | “Sort the array to get ranks; rank[i] ⇒ #smaller, #greater.”     |                   |
| **20–40 s** | “Precompute Catalan numbers via DP or formula.”                  |                   |
| **40–50 s** | “For each x: L = rank[x]; R = n−1−L; ans[i] = C[L]*C[R].”        |                   |
| **50–60 s** | “Return ans — done. O(n²) DP or O(n) formula + O(n log n) sort.” |                   |

---

## 💬 **What to Say in Interview**

> “The number of unique BSTs for `n` distinct keys is the `n`-th Catalan number.
> For each root, left subtree size = #smaller elements, right = #greater.
> So total = `Catalan(L) × Catalan(R)`.
> I’ll sort to find ranks, precompute Catalans, then multiply for each root.”

---

### 🧩 **Quick Recap Mnemonic**

> 🪄 **“Sort → Rank → Catalan → Multiply → Return.”**

That’s the entire algorithm in five mental checkpoints you can recall in 30 seconds anywhere.
