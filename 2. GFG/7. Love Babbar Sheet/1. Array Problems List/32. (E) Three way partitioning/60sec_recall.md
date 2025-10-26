**“5-line pseudo-code + 60-second recall system”** for
🧩 **Three-Way Partitioning (around range [a, b])**

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
low, mid, high = 0, 0, n-1
while mid <= high:
    if arr[mid] < a:  swap(arr[low], arr[mid]); low++; mid++
    elif arr[mid] > b: swap(arr[mid], arr[high]); high--
    else: mid++
```

✅ **Time:** O(n) — each element moves at most once
✅ **Space:** O(1) — only three pointers
✅ Works in **any language** (C++, Java, Python, Go, etc.)

---

## 🧠 Easy Mnemonic — “L-M-H Flow” → *Left, Middle, High*

| Step  | Meaning                                | Visual Cue |
| ----- | -------------------------------------- | ---------- |
| **L** | `< a` → swap with `low`, push left     | ⬅️         |
| **M** | `[a, b]` → already in middle → move on | ➡️         |
| **H** | `> b` → swap with `high`, push right   | ➡️⬅️       |

> 💬 **Catchphrase:**
> “**Left → smalls, Mid → stay, High → bigs away.**”

---

## 🕒 60-Second Recall Routine Before Interview

1. **Say the goal aloud:**
   “Partition array into three zones — less than `a`, between `[a,b]`, greater than `b`.”

2. **Visualize three walls:**
   `[ low | mid | high ]` sweeping from left to right.

3. **Recall the rules:**

   * `arr[mid] < a` → swap with low → both ++
   * `arr[mid] in [a,b]` → just mid++
   * `arr[mid] > b` → swap with high → high--

4. **Code mentally in 5 lines (above skeleton).**

5. **Complexity mantra:**
   “One pass, three zones. O(n) time, O(1) space.”

---

### 🎯 10-Second Sticky Recall Line:

> **“low-mid-high: small → left, mid → pass, large → right.”**
