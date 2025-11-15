**5-line pseudo-code template**, plus a **super-simple mnemonic** and **60-second recall system** you can rely on right before any interview.

---

## 🧩 5-Line Pseudo-Code Template (for “Median in a Row-wise Sorted Matrix”)

```
low  = min(first element of each row)
high = max(last element of each row)
K = (n * m + 1) // 2
while low < high:
    mid = (low + high) // 2
    cnt = sum(upper_bound(row, mid) for row in mat)
    if cnt < K: low = mid + 1
    else: high = mid
return low
```

✅ **Time Complexity:** O(n × log m × log(value_range))
✅ **Space Complexity:** O(1)

---

## 🧠 Mnemonic — “**Value Range → Count ≤ mid → Adjust Bounds → Return low**”

Say this short mantra before coding:

> **“Find min & max, count ≤ mid, move bound, return low.”**

| Step                 | Meaning                                                  | Visual/Intuitive Hook                           |
| -------------------- | -------------------------------------------------------- | ----------------------------------------------- |
| 🔽 **Value Range**   | Start with global `low` and `high` from matrix edges     | “Search in value space, not index space.”       |
| 🔢 **Count ≤ mid**   | For a given `mid`, count how many elements ≤ mid         | “Each row gives you a count via binary search.” |
| 🔁 **Adjust Bounds** | If not enough numbers ≤ mid → move right; else move left | “Classic binary search narrowing.”              |
| 🏁 **Return low**    | When low == high, you’ve landed on the median            | “Both ends meet at the K-th number.”            |

---

## 🔑 60-Second Recall Routine (Before Interview)

| Time       | Focus                   | What to Remember                                       |
| ---------- | ----------------------- | ------------------------------------------------------ |
| **0–10s**  | Problem nature          | “Each row sorted. Global matrix not sorted.”           |
| **10–20s** | Trick                   | “Binary search the **value range** (not flatten).”     |
| **20–35s** | Core condition          | “Count elements ≤ mid in each row (with upper_bound).” |
| **35–50s** | Binary search direction | “If count < K → low = mid+1 else high = mid.”          |
| **50–60s** | Complexity & closure    | “O(n·log m·log Δ), Δ = max - min; space O(1).”         |

> ⚡️ Say aloud:
> **“Binary search on value range. Count ≤ mid per row. Adjust bounds. Return low.”**

---

## 🧱 Quick Sticky-Note Visualization (Mental Image)

```
min(matrix) ------------------ max(matrix)
        ↑ mid
  count of <= mid = ?
     | < K → move right
     | ≥ K → move left
When range collapses ⇒ median
```

---

## 🗣️ Interview-ready One-Liner

> “We binary search over possible values between global min and max.
> For each mid, we count how many elements are ≤ mid using `bisect_right` on each sorted row.
> If the count is less than half of total elements, move right; otherwise left.
> When the range collapses, that’s our median.”

---

### ⚡ 10-Word Memory Hook:

> **“Min–Max → Count ≤ mid → Adjust Bounds → Return low.”**

That’s your **30-second rebuild** + **60-second recall** plan — bulletproof for interviews 🚀
