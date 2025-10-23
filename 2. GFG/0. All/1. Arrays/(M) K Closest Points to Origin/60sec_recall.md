A **classic heap-based k-selection problem** (like Top K Frequent, K Largest, K Closest, etc.), so you can remember it once and apply the same logic everywhere.

**5-line pseudo-code**, **mnemonic**, and **60-second recall** that will make you interview-proof for this question 💪

---

## 🧠 5-Line Pseudo-Code Template (universal & language-agnostic)

```
function kClosest(points, k):
    heap = empty max-heap                         # Step 1: keep k closest so far
    for each (x, y) in points:                    # Step 2: iterate all points
        dist2 = x*x + y*y                         # Step 3: use squared distance
        if heap.size < k: push(-dist2, (x, y))    # Step 4: fill heap first
        else if dist2 < -heap.top().dist2: replace top with (-dist2, (x, y))
    return all points in heap                     # Step 5: extract results
```

✅ **Time:** O(n log k)
✅ **Space:** O(k)

---

## ⚡ Mnemonic to Remember

> **"Square – Keep – Replace – Return"**

That’s the 4-step mental model:

1. **Square** the distance (no sqrt).
2. **Keep** the first `k` points in a heap.
3. **Replace** the farthest whenever you find a closer one.
4. **Return** the heap contents.

It applies to all similar “Top K by metric” problems (distance, frequency, score, etc).

---

## ⏱️ 60-Second Recall Plan Before Interview

| Time       | Step           | What to Recall / Say                                                                                    |
| ---------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| **0–10s**  | Problem type   | “We need the k smallest distances — use a heap.”                                                        |
| **10–20s** | Data structure | “Use a **max-heap** (store negative distances) so we can easily drop the farthest.”                     |
| **20–30s** | Core logic     | “Push first k points → for each new point, compare to heap top → replace if closer.”                    |
| **30–40s** | Complexity     | “Each operation is O(log k), total O(n log k), space O(k).”                                             |
| **40–50s** | Optimization   | “We can use quickselect for average O(n) but heap is simpler and expected.”                             |
| **50–60s** | Final answer   | “Return points from heap (any order). √ step not needed because ordering is same for squared distance.” |

---

## 🧩 Apply This Template To Variants

| Problem Type                    | Change                                        |
| ------------------------------- | --------------------------------------------- |
| **K Closest to Origin**         | Use squared Euclidean distance (x² + y²).     |
| **K Largest Numbers**           | Compare numbers directly (max-heap/min-heap). |
| **Top K Frequent Elements**     | Compare frequency counts.                     |
| **K Closest Elements in Array** | Compare `abs(x - target)`.                    |

🧠 **Same pattern every time:**
→ *“Maintain heap of size k with metric; push, replace, return.”*

---

## 🎯 TL;DR (your 30-second rebuild mantra)

> **"Square – Keep – Replace – Return"**
> (or say “Push first k → replace farthest if closer → return heap → O(n log k)”)

That’s it — with this one mental skeleton, you can rebuild **K Closest Points** (and all Top-K problems) in under a minute in **Python, C++, Java, or Go** during interviews.
