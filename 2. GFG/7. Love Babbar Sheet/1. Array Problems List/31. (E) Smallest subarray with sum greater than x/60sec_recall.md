👌**5-line pseudo-code + mnemonic memory system** for
🧩 **Smallest Subarray with Sum > X** (the sliding window classic).

---

## ⚙️ 5-Line Pseudo-Code Template (universal skeleton)

```
sum = 0; left = 0; best = ∞
for right in 0..n-1:
    sum += arr[right]
    while sum > x:
        best = min(best, right - left + 1)
        sum -= arr[left]; left += 1
return 0 if best == ∞ else best
```

✅ **O(n)** time — each index enters/leaves window once
✅ **O(1)** space
✅ Works only because all numbers are **non-negative**

---

## 🧠 Easy Mnemonic — “**E-S-S-M**” → *Expand, Shrink, Save, Move*

| Step  | Meaning                                | Visual cue                |
| ----- | -------------------------------------- | ------------------------- |
| **E** | **Expand** right → include new element | ➕ arrow forward           |
| **S** | **Shrink** left while sum > x          | ✂️ trimming window        |
| **S** | **Save** best (min length)             | 📝 record answer          |
| **M** | **Move** left pointer                  | 👣 sliding window forward |

> 💬 **Catchphrase:**
> “Expand till overflow, then shrink to fit.”

---

## 🕒 60-Second Interview Recall Routine

1. **State the problem:**
   “Find the smallest contiguous subarray with sum > X.”

2. **Think logic quickly:**

   * Array is non-negative → sliding window works.
   * Expand right until `sum > x`.
   * Then shrink from left to minimize window size.

3. **Rebuild code mentally (5 lines):**

   * `sum=0, left=0, best=inf`
   * For right in range(n):

     * Add arr[right]
     * While sum>x → update best, subtract arr[left], left++
   * Return 0 if best==inf else best

4. **Edge checks (10s):**

   * No subarray → return 0
   * Single element > x → answer = 1

5. **Complexity mantra:**
   “Time O(n), Space O(1). Each index enters & exits once.”

---

### 🎯 One-line sticky recall

> **“Expand till sum>target → shrink till valid → keep smallest window.”**
