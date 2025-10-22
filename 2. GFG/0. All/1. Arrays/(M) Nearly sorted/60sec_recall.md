**“5-line pseudo-code + mnemonic + 60-second recall”** for the **Nearly Sorted (k-sorted) Array** problem 👇

---

## 🧠 5-Line Pseudo-Code Template (universal skeleton)

```
function nearlySorted(arr, k):
    heap = first (k+1) elements                # Step 1: build initial window
    heapify(heap)                              # Step 2: min-heap O(k)
    for i from k+1 to end:                     # Step 3: push next, pop smallest
        output.append(heappop_push(heap, arr[i]))
    while heap not empty:                      # Step 4: drain remaining elements
        output.append(heappop(heap))
    return output                              # Step 5: done
```

✅ **Time:** O(n log k)
✅ **Space:** O(k)

---

## ⚡ Mnemonic (to recall instantly)

> **“Heap — Push — Pop — Drain.”**

That’s the whole mental model:
1️⃣ Build heap of first `k+1` items,
2️⃣ For each next item, **push new → pop min**,
3️⃣ Drain the heap at end.

Easy 4-word recall you can say to yourself before coding.

---

## ⏱️ 60-Second Interview Recall Plan

| Time        | Step                 | What to say / think                                                     |
| ----------- | -------------------- | ----------------------------------------------------------------------- |
| **0–10 s**  | Restate problem      | “Each element ≤ k away from sorted position ⇒ use a heap of size k+1.”  |
| **10–20 s** | Outline              | “Min-heap keeps smallest available among next k+1 candidates.”          |
| **20–40 s** | Pseudo-code mentally | “Build heap; for each next element: pop→output, push→heap; drain heap.” |
| **40–50 s** | Complexity           | “O(n log k) time, O(k) space; much better than O(n log n).”             |
| **50–60 s** | Edge / sanity        | “If k = 0 → already sorted; if k ≥ n → normal heap sort behavior.”      |

---

## 🎯 Extra mental shortcut (pattern)

This belongs to the family of **“k-window heap problems”**, same as:

* Merge K sorted arrays → heap of size k
* Top-K elements → heap of size k
* K-sorted array → heap of size k+1

💡 So if you remember:

> **“When order deviation = k → heap size = k+1 → O(n log k).”**

…you can instantly rebuild this in any language (Python, C++, Java) under pressure.

---

**Summary (30-second rebuild mantra):**

> 🪄 “Heap (k+1), Push–Pop–Drain, O(n log k), O(k).”
