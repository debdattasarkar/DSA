**“5-line pseudo-code + 60-second recall”** system for
🧩 **Median of an Array**

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
sort(arr)
n = length(arr)
mid = n // 2
if n is odd:
    return arr[mid]
else:
    return (arr[mid - 1] + arr[mid]) / 2
```

✅ **Time Complexity:** O(n log n)
✅ **Space Complexity:** O(1) (if sorted in-place)
✅ Works for **any language** — Python, C++, Java, Go, etc.

---

## 🧠 Easy Mnemonic — “**S-M-A**” → *Sort → Middle → Average (if even)*

| Step  | Action            | Symbol | Quick Meaning           |
| ----- | ----------------- | ------ | ----------------------- |
| **S** | Sort array        | 🔀     | Arrange ascending       |
| **M** | Find middle index | 🎯     | `n // 2`                |
| **A** | Average if even   | ➗      | `(a[mid-1] + a[mid])/2` |

> 💬 **Catchphrase:**
> “Sort. Middle. Average. — the three words to median.”

---

## 🕒 60-Second Recall Routine (before interview)

1. **Say the goal aloud:**
   “Find the middle value of a sorted array.”

2. **Visualize:**

   * Odd → one center.
   * Even → two centers → take their average.

3. **Think the plan quickly:**

   * Step 1: Sort → O(n log n).
   * Step 2: If odd → return middle.
   * Step 3: If even → average two middles.
   * Done. Easy and deterministic.

4. **Edge checks:**

   * Single element → it’s the median.
   * Empty array → undefined (depends on spec).
   * Return float for even case.

5. **Complexity mantra:**

   > “O(n log n) time, O(1) space, one pass after sort.”

---

### 🎯 10-Second Sticky Recall Line

> **“Sort → Middle → Average if even.”**
