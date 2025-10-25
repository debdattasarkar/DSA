**5-line pseudo-code template + 60-second recall kit** for
🧩 **More than n/k Occurrences** (a.k.a. *generalized majority voting / Misra–Gries algorithm*).

---

## ⚙️ 5-Line Pseudo-Code Template (universal, rebuildable in any language)

```
cand = {}
for x in arr:
    if x in cand: cand[x]+=1
    elif len(cand)<k-1: cand[x]=1
    else: decrease all counts, remove zeros
verify actual freq for cand; count those > n//k
```

✅ **O(n)** time, **O(k)** space
✅ Works for any `k ≥ 2`
✅ Outputs all elements appearing more than ⌊n/k⌋ times

---

## 🧠 Easy Mnemonic — “**K-C-V**” → *Keep, Cancel, Verify*

| Step  | Meaning                                      | Mental Cue                    |
| ----- | -------------------------------------------- | ----------------------------- |
| **K** | **Keep** top `k−1` candidates while counting | 🧺 holding only a few marbles |
| **C** | **Cancel** all when “full”                   | ⚖️ balance out counts equally |
| **V** | **Verify** actual frequencies in second pass | 🧾 check the real winners     |

> 💬 **Catchphrase:**
> “Keep few, Cancel many, Verify truly.”

---

## 🕒 60-Second Recall Routine (before interview)

1. **Say the core idea aloud:**
   “At most (k−1) numbers can occur more than n/k times. Keep ≤ (k−1) candidates, decrement when full, verify later.”

2. **Visualize loop logic:**

   * ✅ If number already in map → increment
   * ➕ Else if map has room → add it
   * ❌ Else → decrement all counts, remove zeros

3. **Second pass mental step:**

   * Recount these few candidates in original array
   * Check which `> n//k`

4. **Edge case recall:**

   * If `k == 1` → impossible (threshold > n)
   * If `k > n` → threshold = 0 → all distinct counted

5. **Complexities (say it confidently):**

   * Time = **O(n)** (two passes)
   * Space = **O(k)**

---

### 🧩 One-line Sticky Summary:

> “**Keep k−1 survivors, cancel the rest, verify after.**”
