**“60-second recall kit”** and **5-line pseudo-code skeleton** for the **Sorted Matrix** problem (a super common warm-up question at Amazon / FactSet / TCS interviews).

---

## 🧠 5-Line Pseudo-Code Template (Universal Skeleton)

```
function sortedMatrix(N, Mat):
    flat = all elements of Mat                 # flatten
    sort(flat)                                 # global ascending order
    fill Mat row by row from flat              # rewrite back
    return Mat
```

✅ That’s all you need — works in **Python / C++ / Java / C# / Go**.
The logic never changes.

---

## 🧩 Mnemonic to Instantly Recall

> **“Flat → Sort → Fill → Return.”**

1️⃣ **Flat** → collect all `N×N` values into one array.
2️⃣ **Sort** → global sort (ascending).
3️⃣ **Fill** → refill the matrix row-wise.
4️⃣ **Return** → sorted 2-D matrix.

Just say this to yourself once before coding:

> “Flatten → Sort → Refill → Done.”

---

## ⏱️ 60-Second Pre-Interview Recall

When interviewer says:

> “Sort all elements of an N×N matrix.”

You think/say out loud:

1️⃣ “I’ll flatten all N² elements into a single list.”
2️⃣ “Then sort that list (O(N² log N)).”
3️⃣ “Finally, fill the matrix row by row from that list.”
4️⃣ “This ensures global ordering, not just per row or column.”
5️⃣ “Space O(N²) for the flattened list; can do in-place variant if needed.”

---

## ⚙️ Quick Example Mental Check

Matrix =

```
[[1,5,3],
 [2,8,7],
 [4,6,9]]
```

Flatten → `[1,5,3,2,8,7,4,6,9]`
Sort → `[1,2,3,4,5,6,7,8,9]`
Fill →

```
1 2 3
4 5 6
7 8 9
```

✅ Done — 3 lines of actual code in Python!

---

## 💬 10-Second “Why” Answer (if interviewer asks)

> “Because a full sort of all N² values guarantees true global order.
> Sorting row-wise or column-wise doesn’t.
> Complexity is O(N² log N) and space O(N²).”

---

## 🔁 Quick Mnemonic Recap Table

| Step | Action  | Purpose                | Keyword    |
| ---- | ------- | ---------------------- | ---------- |
| 1️⃣  | Flatten | Get all N² values      | **Flat**   |
| 2️⃣  | Sort    | Global ascending order | **Sort**   |
| 3️⃣  | Fill    | Rebuild row-wise       | **Fill**   |
| 4️⃣  | Return  | Output matrix          | **Return** |

🧩 **One-liner memory trick:**

> “Flat, Sort, Fill, Return — F-S-F-R.”

---
