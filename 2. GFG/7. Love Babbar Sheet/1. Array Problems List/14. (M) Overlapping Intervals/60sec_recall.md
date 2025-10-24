Excellent — let’s build your **“5-line pseudo-code template”** for **Overlapping Intervals** so you can instantly recall it in an interview.

---

## 🧩 5-Line Pseudo-Code Template (works in any language)

```
sort intervals by start                        # Step 1: ensure order
merged = []                                    # Step 2: output list
cur = first interval                           # Step 3: track current
for next in intervals[1:]:                     # Step 4: iterate remaining
    if next.start <= cur.end: cur.end = max(cur.end, next.end)
    else: merged.append(cur); cur = next       # Step 5: flush + reset
merged.append(cur)                             # final push
```

---

## 🧠 Mnemonic to Remember — **“S M C I F”**

> **S**ort → **M**erge current → **C**heck overlap → **I**f not, flush → **F**inal push

Or just repeat mentally:
**“Sort, Scan, Merge, Flush, Push.”**

That one phrase is your 60-second trigger to rebuild it from scratch.

---

## ⚡ 60-Second Recall Routine Before Interview

| Time        | Step                | What to Recall / Say                                   |
| ----------- | ------------------- | ------------------------------------------------------ |
| **0–10 s**  | **Problem Type**    | “We’re merging overlapping intervals.”                 |
| **10–20 s** | **Sort Step**       | “Sort by start time so overlaps appear consecutively.” |
| **20–30 s** | **Core Logic**      | “Keep current interval; if next overlaps, extend end.” |
| **30–40 s** | **Flush Condition** | “Else push current to output and start new one.”       |
| **40–50 s** | **Edge Finish**     | “After loop, push last current interval.”              |
| **50–60 s** | **Complexities**    | “O(n log n) for sort, O(n) sweep, O(1) extra space.”   |

---

## 💬 10-Second Interview Line

> “I’ll **sort** intervals by start and then **scan once**, extending whenever two overlap;
> if they don’t, I **flush** the previous one to output. That’s O(n log n) time and O(1) space.”

---

## 🧠 Bonus Quick Example (mental dry-run)

Input → `[[1,3],[2,4],[6,8],[9,10]]`
After sort → same.
Scan: merge (1,3)+(2,4)→(1,4); flush (6,8); flush (9,10).
Output = `[[1,4],[6,8],[9,10]]`.

---

✅ Memorize the phrase **“Sort, Scan, Merge, Flush, Push.”**
That’s your **universal skeleton** for interval-merging questions — you can rebuild full working code in **under 30 seconds** in any language.
