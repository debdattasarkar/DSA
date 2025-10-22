
---

## 🧠 5-Line Pseudo-Code Template

```
function topKFreq(arr, k):
    freq = count_occurrences(arr)                     # Step 1: Hashmap of value→frequency
    rank = sort(freq.items(), by=(-frequency, -value)) # Step 2: Sort descending by freq, value
    return first k values from rank                    # Step 3: Output top k
```

That’s literally all you need to rebuild the main logic.

✅ **Time:** O(n log n) (sorting step)
✅ **Space:** O(n)

---

## ⚙️ Optimized Mental Variant (Heap / Bucket)

If interviewer says “optimize for large n” or “k ≪ n,” expand to:

```
count freq
heap = []                          # min-heap of (freq, value)
for each (value, freq):
    if heap size < k → push
    else if (freq, value) > heap[0] → replace top
return heap sorted by (-freq, -value)
```

Mnemonic: **“Count → Heap → Replace → Return.”**

Or, if asked for O(n): **Bucket** idea —

```
bucket[freq] = list of values
for freq from max→1:
    add sorted(bucket[freq]) values until len==k
```

Mnemonic: **“Count → Bucket → Reverse → Pick K.”**

---

## 🧩 Easy Mnemonic

> **C → R → P** = **Count → Rank → Pick.**

That’s the 3-step pattern you’ll use for any frequency ranking or top-k problem:

* **Count:** hashmap / Counter
* **Rank:** sort or heap or bucket
* **Pick:** take first k

If you remember *CRP*, you can reconstruct any top-k solution instantly.

---

## ⏱️ 60-Second Recall Flow Before an Interview

| Time    | Step                     | What You Recall / Say Out Loud             |
| ------- | ------------------------ | ------------------------------------------ |
| 0–10 s  | **Problem pattern**      | “Top-K → frequency count + ranking.”       |
| 10–20 s | **Data structure**       | “Use hashmap for counting → O(n).”         |
| 20–30 s | **Basic solution**       | “Sort by (−freq, −value) → O(n log n).”    |
| 30–40 s | **Optimized variant**    | “If k ≪ n, keep a size-k min-heap.”        |
| 40–50 s | **Edge/tie logic**       | “When freq ties, pick larger value first.” |
| 50–60 s | **Complexities summary** | “O(n log n) or O(n log k); O(n) space.”    |

---

### 🧩 Mini mental picture (for visualization)

```
arr → [counting] → {5:3, 11:2, 7:2, 10:1}
→ sort by (-freq, -val)
→ [(3,5), (2,11), (2,7), (1,10)]
→ take first k
```

---

### 💬 What to say if asked “Walk me through your thought process”

> “I’ll first count all elements using a hashmap, then rank them by frequency descending and value descending to handle ties.
> For small k, I can keep a size-k min-heap keyed on (frequency, value).
> The top k items are then the highest frequencies, breaking ties by larger numbers.”

---

✅ **60-second recall checklist:**

> **C-R-P → Count, Rank, Pick.**
> (Say it in your head before coding.)
