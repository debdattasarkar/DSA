**“5-line pseudo-code template”** for **Spiral Traversal of a Matrix**, plus a **simple mnemonic** and a **60-second recall strategy** to ace it in interviews. 🚀

---

## 🧩 5-Line Pseudo-Code Template

*(This exact skeleton can be rebuilt in Python, C++, or Java in <30 seconds)*

```
top = 0, bottom = n-1, left = 0, right = m-1
while top <= bottom and left <= right:
    traverse top row (left → right), then top++
    traverse right col (top → bottom), then right--
    if top <= bottom: traverse bottom row (right → left), then bottom--
    if left <= right: traverse left col (bottom → top), then left++
```

✅ **Time Complexity:** O(n × m)
✅ **Space Complexity:** O(1) (ignoring output list)

---

## 🧠 Mnemonic — **“T-R-B-L → Top, Right, Bottom, Left”**

Remember the word **“TRaBLe” (like “trouble”)**, meaning the spiral order:

**T → R → B → L → shrink → repeat**

👉 **Say it aloud:**

> “Top → Right → Bottom → Left — then shrink and repeat.”

This instantly recalls both traversal directions and boundary updates.

---

## ⚙️ Step Mnemonics Breakdown

| Step     | Name       | Action                                 | Boundary Update |
| -------- | ---------- | -------------------------------------- | --------------- |
| 🟢 **T** | Top Row    | Move Left → Right                      | `top += 1`      |
| 🔵 **R** | Right Col  | Move Top → Bottom                      | `right -= 1`    |
| 🟠 **B** | Bottom Row | Move Right → Left (if `top <= bottom`) | `bottom -= 1`   |
| 🔴 **L** | Left Col   | Move Bottom → Top (if `left <= right`) | `left += 1`     |

---

## 🧩 60-Second Recall Routine (Pre-Interview Warm-up)

| Seconds | What to Recall        | Key Thought                                                      |
| ------- | --------------------- | ---------------------------------------------------------------- |
| 0–10 s  | **Define boundaries** | top, bottom, left, right = 0, n-1, 0, m-1                        |
| 10–25 s | **While condition**   | Loop until top <= bottom & left <= right                         |
| 25–40 s | **Four traversals**   | Top→Right→Bottom→Left in that order                              |
| 40–50 s | **Shrink bounds**     | After each edge, adjust respective boundary                      |
| 50–60 s | **Edge cases**        | Use `if` checks for bottom/left layers to avoid double traversal |

---

## 🧱 Sticky-note version (to write on paper/board quickly)

```
T, R, B, L pattern
while t<=b and l<=r:
  → top row
  ↓ right col
  ← bottom row (if t<=b)
  ↑ left col (if l<=r)
```

🧠 **Trigger phrase to recall it:**

> “Peel the onion — T, R, B, L — shrink each side, repeat.”

---

💡 **Pro tip (how to speak it in interview):**

> “I maintain four boundaries — top, bottom, left, right.
> I traverse one layer clockwise (Top → Right → Bottom → Left),
> then shrink the layer inward and repeat until all elements are covered.”

Boom — clear logic, structured explanation, and easy code recall in 30 seconds flat.
