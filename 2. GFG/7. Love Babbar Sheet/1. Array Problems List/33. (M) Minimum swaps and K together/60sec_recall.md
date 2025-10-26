**“5-line pseudo-code + 60-second recall system”** for
🧩 **Minimum Swaps and K Together**

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
good = count(arr[i] <= k)
bad = count(arr[i] > k for i in 0..good-1)
min_swaps = bad
for i in range(good, n):
    if arr[i] > k: bad += 1
    if arr[i-good] > k: bad -= 1
    min_swaps = min(min_swaps, bad)
return min_swaps
```

✅ **Time:** O(n) — each index enters/exits window once
✅ **Space:** O(1) — constant extra variables
✅ Works for any language and integer array

---

## 🧠 Easy Mnemonic — “**G-B-W**” → *Good–Bad–Window*

| Step  | Action                                 | Symbol | Quick Meaning           |
| ----- | -------------------------------------- | ------ | ----------------------- |
| **G** | Count how many are “Good” (≤ k)        | 🍏     | That’s your window size |
| **B** | Count “Bad” (> k) in that first window | 🍎     | How many misplaced      |
| **W** | Slide the Window                       | 🔁     | Track min bad → answer  |

> 💬 **Catchphrase:**
> “Count Good, Slide Bad, Keep Min.”

---

## 🕒 60-Second Recall Routine

1. **Say the goal out loud:**
   “Group all ≤ k together — minimize swaps → minimize bads (> k) inside the good-sized window.”

2. **Visualize:**

   * Imagine a window of size = number of ≤ k elements.
   * Move it across the array → find where the fewest > k occur.

3. **Think step-by-step:**

   * Count good = how many ≤ k.
   * Count bad = > k in first window.
   * Slide right: add arr[i], remove arr[i–good].
   * Keep the smallest bad.
   * Return bad.

4. **Edge checks:**

   * `good <= 1` → return 0.
   * All ≤ k → return 0.
   * Empty array → 0.

5. **Complexity mantra:**

   > “Linear time, constant space, one sliding window.”

---

### 🎯 10-Second Sticky Recall Line

> **“Window size = count ≤ k → min bads inside = min swaps.”**
