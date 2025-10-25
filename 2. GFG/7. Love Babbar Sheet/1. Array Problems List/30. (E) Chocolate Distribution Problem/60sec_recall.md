👌 **5-line pseudo-code template + 60-second recall mnemonic** for
🍫 **Chocolate Distribution Problem** (one of the most common “fairness” array questions).

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
sort(arr)
min_diff = ∞
for i in 0..n-M:
    diff = arr[i+M-1] - arr[i]
    min_diff = min(min_diff, diff)
return min_diff
```

✅ **Time:** O(n log n)
✅ **Space:** O(1) (in-place sort)
✅ Works for duplicates & large numbers

---

## 🧠 Easy Mnemonic — “**S-W-M**” → *Sort, Window, Minimize*

| Step  | Meaning                      | Visual cue             |
| ----- | ---------------------------- | ---------------------- |
| **S** | **Sort** the array           | 📊 packets in order    |
| **W** | Slide a **Window** of size M | 📦 scanning groups     |
| **M** | Track **Minimum difference** | 📉 keep smallest range |

> 💬 **Catchphrase:**
> “Sort → Window → Minimize.”

---

## 🕒 60-Second Interview Recall Routine

1. **Say the goal clearly:**
   “We need to give M students one packet each such that the **max–min difference** among their packets is **minimum**.”

2. **Think it through visually:**

   * After sorting, best M must be **contiguous**.
   * Range = last − first in that window.
   * Slide window → pick minimum range.

3. **Code skeleton recall:**
   `sort → loop → window difference → keep min → return.`

4. **Edge checks:**

   * `M == 1 → 0`
   * `M > n → invalid (-1)`
   * Empty or zero chocolates handled implicitly.

5. **Complexity mantra:**
   “Sort drives cost: O(n log n). Scan linear: O(n). Space constant.”

---

### 🧩 10-second sticky line:

> **“Sort packets → Slide window → Track smallest gap.”**
