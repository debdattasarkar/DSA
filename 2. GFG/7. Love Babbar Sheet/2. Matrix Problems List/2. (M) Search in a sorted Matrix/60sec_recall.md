**5-line pseudo-code template** + **super-easy mnemonic** that helps you rebuild the *Search in a Sorted Matrix* logic in **30 seconds flat** before any interview 🚀

---

## 🧩 5-Line Pseudo-Code Template

```
n, m = len(mat), len(mat[0])
l, r = 0, n*m - 1
while l <= r:
    mid = (l + r) // 2
    val = mat[mid // m][mid % m]
    if val == x: return True
    elif val < x: l = mid + 1
    else: r = mid - 1
return False
```

✅ **Time Complexity:** O(log(n × m))
✅ **Space Complexity:** O(1)

---

## 🧠 Mnemonic — “**Think 1D → Map → Compare → Narrow → Done**”

| Step             | What It Means                              | Mnemonic Hint                          |
| ---------------- | ------------------------------------------ | -------------------------------------- |
| **1️⃣ Think 1D** | Treat the matrix as one long sorted list.  | *“Imagine it stretched out flat.”*     |
| **2️⃣ Map**      | Map mid → `(row, col)` using `//` and `%`. | *“Row = mid // m, Col = mid % m.”*     |
| **3️⃣ Compare**  | Check if mid-value matches the target `x`. | *“Compare like normal binary search.”* |
| **4️⃣ Narrow**   | Adjust `l` or `r` based on comparison.     | *“Move left or right halves.”*         |
| **5️⃣ Done**     | Return `True` if found, else `False`.      | *“End when l > r.”*                    |

### 🔑 Quick sentence mnemonic:

> **“Flatten the matrix, Map with divmod, Compare, Cut half, Done!”**

---

## 🧱 60-Second Recall Routine (Before Interview)

| Time       | What to Recall          | How to Say It                                                                              |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------ |
| **0–10s**  | Matrix property         | “Each row sorted and next row starts after previous ends — behaves like one sorted array.” |
| **10–20s** | Flattening logic        | “Imagine the matrix as length `n*m`; mid → (mid//m, mid%m).”                               |
| **20–35s** | Binary search structure | “Standard binary search pattern: l, r, mid, compare.”                                      |
| **35–50s** | Update rule             | “If val < x → go right; if val > x → go left.”                                             |
| **50–60s** | Complexity recall       | “O(log(n*m)) time, O(1) space.”                                                            |

> ⚡ In 60 seconds, you can reconstruct the logic and confidently start coding.

---

## 🧭 Alternate Recall for Staircase Search (When matrix not globally sorted)

**Mnemonic:**

> **“Start Top-Right → Greater → Left, Smaller → Down.”**

**5-line Template:**

```
r, c = 0, m - 1
while r < n and c >= 0:
    if mat[r][c] == x: return True
    elif mat[r][c] > x: c -= 1
    else: r += 1
return False
```

✅ **Time:** O(n + m)
✅ **Space:** O(1)

---

## 🎯 10-Word Memory Hook

> **“Flatten, Map, Compare, Cut — or Top-Right Walk Down.”**

---

### 🔁 Quick Visualization to Remember

```
Matrix → Flattened Sorted List
mid → (mid // m, mid % m)
< x → move right   > x → move left
== x → found ✅
```

---

### 🧩 Interview Tip:

If you forget the index math, say:

> “We can map 1D → 2D using: row = index // columns, col = index % columns.”

That one sentence shows deep understanding — interviewers love it.
