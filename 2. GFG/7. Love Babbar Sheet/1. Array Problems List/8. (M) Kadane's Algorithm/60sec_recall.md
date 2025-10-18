**Interview muscle-memory version** of **Kadane’s Algorithm** — the 5-line pseudo-code, a 60-second recall flow, and a mnemonic that sticks 🔥

---

## 🧠 **5-Line Pseudo-Code Template (Language Agnostic)**

```
function maxSubarraySum(arr):
    curr = best = arr[0]                # init
    for x in arr[1:]:
        curr = max(x, curr + x)         # extend or restart
        best = max(best, curr)          # track global best
    return best
```

✅ **Time:** O(n)
✅ **Space:** O(1)

---

## ⚡ **Mnemonic to Recall Quickly**

> 🧩 **“Extend — Compare — Keep — Return.”**

Or simpler:

> **ECKR → Extend, Compare, Keep, Return**

| Step  | Meaning                  | Variable                  |
| ----- | ------------------------ | ------------------------- |
| **E** | Extend or restart        | `curr = max(x, curr + x)` |
| **C** | Compare with global best | `best = max(best, curr)`  |
| **K** | Keep track across array  | inside the loop           |
| **R** | Return final answer      | `return best`             |

You can literally say to yourself before coding:

> “Extend or restart → Compare → Return best.”

---

## ⏱️ **60-Second Recall (Quick Rebuild Flow)**

**0–10 sec** → “Kadane’s = max subarray sum, contiguous, linear scan.”
**10–20 sec** → Initialize `curr` & `best` with `arr[0]`.
**20–40 sec** → Loop each element:

```text
curr = max(x, curr + x)
best = max(best, curr)
```

**40–50 sec** → Handles all-negatives automatically.
**50–60 sec** → Mention O(n), O(1), dynamic programming → done ✅

---

## 💬 **How to Explain in Interview**

> “At each step, I decide whether to extend the current subarray or start a new one, based on which gives a higher sum.
> I keep track of the global best while iterating once through the array — that’s O(n) time, O(1) space.”

---

### 🧩 One-Line Summary to Say Aloud Before You Code:

> “Kadane’s scans once, keeps a running sum, resets if it goes negative, and records the best sum — extend or restart, compare, return.”

---

That’s your **mental 5-line skeleton + ECKR mnemonic** —
you can rebuild it **in 30 seconds** in Python, C++, or Java every single time.
