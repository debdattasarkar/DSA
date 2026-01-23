## 5-line pseudo-code skeleton (30-second rebuild)

```
build prevGE: stack; for i=0..n-1: while stack not empty and a[stack.top] < a[i]: pop; prev[i]=stack.top or -1; push i
build nextGE: stack; for i=n-1..0: while stack not empty and a[stack.top] < a[i]: pop; next[i]=stack.top or n; push i
best=1
for i=0..n-1: best=max(best, next[i]-prev[i]-1)
return best
```

That’s the whole solution.

---

## Easy mnemonic (sticky)

### **“Pop smaller, keep blockers (>=). Gap is answer.”**

* **Pop smaller** (`<`) because they **can’t block** anyone taller.
* **Keep bigger/equal** on stack because **they are blockers** (>=).
* For each i, visible count is just **gap between blockers**:
  **`nextGE - prevGE - 1`**

---

## 60-second recall script (before interview)

1. **Restate rule (10s):**
   “Person i can see in a direction until the first person with height **>= arr[i]**. That person blocks and is not visible.”

2. **Reduce problem (10s):**
   “So I need nearest **greater-or-equal** on left and right for every i.”

3. **Formula (10s):**
   “Visible including self = people between blockers = `R - L - 1`.”

4. **How to compute blockers fast (20s):**
   “Use monotonic **decreasing** stack of indices.
   While top height < current, pop. The remaining top is previous GE.
   Repeat from right to get next GE.”

5. **Finish (10s):**
   “Scan i, compute `next[i]-prev[i]-1`, take max. O(n) time, O(n) space.”