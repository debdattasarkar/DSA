
---

## 🧠 5-Line Pseudo-Code Template (Universal Skeleton)

```
function findDuplicates(arr):
    count = empty hash_map                    # Step 1: count frequency
    for each num in arr:                      # Step 2: update count
        count[num] = count.get(num, 0) + 1
    result = [num for num in count if count[num] > 1]  # Step 3: filter duplicates
    return sorted(result)                     # Step 4: return in order
```

✅ **Time:** O(n)
✅ **Space:** O(n)

---

## ⚡ Easy Mnemonic (Memory Hook)

> **C-F-R-S → Count → Filter → Return → Sort**

Say it mentally:

> “Count first, Filter duplicates, Return sorted — C-F-R-S.”

If you can recall “CFRS,” you can rebuild the entire function in any language (Python, C++, Java, JS) within 30 seconds.

---

## ⏱️ 60-Second Interview Recall Plan

| Time       | Step           | What to Recall / Say                                                                 |
| ---------- | -------------- | ------------------------------------------------------------------------------------ |
| **0–10s**  | Identify       | “We’re finding all elements that appear more than once.”                             |
| **10–20s** | Data structure | “Use a hash map to count each number.”                                               |
| **20–30s** | Logic          | “Loop once to count, then collect keys with count > 1.”                              |
| **30–40s** | Complexity     | “O(n) time, O(n) space.”                                                             |
| **40–50s** | Alternatives   | “Could sort + scan (O(n log n)) if no hash allowed.”                                 |
| **50–60s** | Wrap up        | “If values are 1..n and mutation allowed, I can do it in-place using index marking.” |

---

## 💬 One-Line Interview Answer

> “I’ll use a hash map to count frequencies in O(n) and filter numbers with count > 1.
> It’s clean, linear time, and works for any integer range. If the interviewer restricts space, I can fall back to sorting + scanning in O(n log n).”

---

## ⚙️ Optional Pattern Association

| Pattern               | Similar Problems                                              |
| --------------------- | ------------------------------------------------------------- |
| **Counting hash map** | Top-K Frequent Elements, Majority Element, Unique Occurrences |
| **Sort + scan**       | Remove Duplicates, Merge Intervals                            |
| **In-place marking**  | Find Missing Number, Find All Duplicates in 1..n Array        |

---

### 🎯 TL;DR (30-second recall mantra)

> **“C-F-R-S → Count, Filter, Return, Sort → O(n), O(n)”**

Say it once before an interview, and you’ll never blank on this question again.
