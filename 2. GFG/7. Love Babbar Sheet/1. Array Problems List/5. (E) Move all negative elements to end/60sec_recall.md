Here’s your **“60-second recall kit”** and **5-line pseudo-code** for
**Move all negative elements to the end (stable order).**

---

## 🧠 5-Line Pseudo-code (language-agnostic)

```
function moveNegativesToEndStable(A):
    write = 0; neg = []                # buffer negatives
    for x in A:                        # one linear scan
        if x >= 0: A[write] = x; write += 1
        else: neg.append(x)
    for x in neg: A[write] = x; write += 1
```

**Complexity:** Time O(n); Extra space O(k) (k = #negatives), worst-case O(n).
**Why it’s correct:** We copy non-negatives in arrival order, then append negatives in their arrival order → **stable partition**.

---

## 🎯 Mnemonic (say before coding)

> **“Write, Buffer, Append.”**
>
> * **Write** non-negatives forward,
> * **Buffer** negatives,
> * **Append** negatives at the end.

---

## ⏱️ 60-Second Interview Recall

1. **Goal:** Stable partition → preserve order within positives and within negatives.
2. **Constraint:** In-place result; returning a new array is optional, but we’ll modify `A`.
3. **Plan:** One pass `for x in A` — write `x>=0` to next slot; push negatives to `neg`.
4. **Finish:** Second pass over `neg` to append at the end.
5. **Talk track:** “O(n) time, O(k) extra; stable. In-place + stable with O(1) space generally needs rotations → O(n²), so this is the practical optimum.”

That’s it—repeat **“Write, Buffer, Append”** and you can rebuild this in any language in ~30 seconds.
