**“5-line pseudo-code + 60-second recall system”** for
🧩 **Median of Two Sorted Arrays (Different Sizes)**

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
if len(a) > len(b): swap(a, b)
n, m = len(a), len(b)
L = (n + m + 1) // 2
lo, hi = 0, n
while lo <= hi:
    i = (lo + hi)//2; j = L - i
    aL = -inf if i==0 else a[i-1]; aR = inf if i==n else a[i]
    bL = -inf if j==0 else b[j-1]; bR = inf if j==m else b[j]
    if aL <= bR and bL <= aR: 
        return odd? max(aL,bL) : (max(aL,bL)+min(aR,bR))/2
    elif aL > bR: hi = i - 1
    else: lo = i + 1
```

✅ **Time:** O(log(min(n, m)))
✅ **Space:** O(1)
✅ Works in any language — Python, C++, Java, Go, etc.

---

## 🧠 Easy Mnemonic — **"S-P-C" → Swap → Partition → Compare**

| Step  | Meaning                      | Icon | Quick Memory Hook                      |
| ----- | ---------------------------- | ---- | -------------------------------------- |
| **S** | **Swap** to make `a` smaller | 🔄   | Always binary-search smaller array     |
| **P** | **Partition** both arrays    | ✂️   | Choose cut `i` in `a`, auto `j` in `b` |
| **C** | **Compare** border elements  | ⚖️   | `aL <= bR` and `bL <= aR` valid        |

> 💬 **Catchphrase:**
> “Swap, Partition, Compare — find perfect balance!”

---

## 🕒 60-Second Recall Routine (Before Interview)

1. **Say the goal aloud:**
   “Find a partition of the two arrays where all left ≤ all right.”

2. **Visualize:**

   ```
   [a_left] | [a_right]
   [b_left] | [b_right]
   ```

   Total left size = (n+m+1)//2
   Adjust partition in `a` until left_max ≤ right_min.

3. **Think flow quickly:**

   * Binary search index `i` in `a`.
   * Compute `j = L - i`.
   * Use `-inf/+inf` guards for boundaries.
   * When condition holds → compute median.
   * Move `hi` / `lo` depending on `aL` vs `bR`.

4. **Complexity mantra:**
   “O(log(min(n,m))) time, O(1) space — binary search for equilibrium.”

5. **Edge check:**

   * One array empty → median of other.
   * Duplicates & overlaps are fine.

---

### 🎯 10-Second Sticky Recall Line

> **“Swap smaller, Partition both, Compare borders → Median = balance point.”**
