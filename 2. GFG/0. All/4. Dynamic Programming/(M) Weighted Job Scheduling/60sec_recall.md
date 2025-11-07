Perfect — here’s your **5-line pseudo-code template** (the version you can recall + rebuild instantly in any language) and an easy **mnemonic** to lock it in your memory before interviews.

---

## 🧩 5-Line Pseudo-Code Template (Weighted Job Scheduling)

```
1. sort jobs by end
2. for each job i:
       j = last job with end <= start[i]      # via binary search
       dp[i] = max(dp[i-1], profit[i] + dp[j])
3. return dp[n-1]
```

✅ **Time:** O(n log n) (because of sort + binary search)
✅ **Space:** O(n)

---

## 🧠 Mnemonic — **“SORT → SEARCH → MAX”**

Say this in your head before you start coding:

> **“SORT by END, SEARCH prev, take MAX(skip, take).”**

That one line encodes everything:

* **SORT** = jobs by end time
* **SEARCH** = binary search to find compatible previous job
* **MAX** = choose between skipping or taking current job

---

## ⚙️ 60-Second Recall Routine Before Interview

| Time      | What to Recall                    | What to Say/Think                                                       |
| --------- | --------------------------------- | ----------------------------------------------------------------------- |
| 0–10 sec  | **State definition**              | “`dp[i]` = max profit from first i jobs (sorted by end).”               |
| 10–20 sec | **Transition**                    | “`dp[i] = max(dp[i-1], profit[i] + dp[prev[i]])`.”                      |
| 20–30 sec | **Prev job**                      | “Use binary search on `end[]` to find last job ending ≤ start[i]`.”     |
| 30–45 sec | **Base case**                     | “`dp[0] = profit[0]`, no overlaps before first job.”                    |
| 45–60 sec | **Code skeleton in any language** | Just type the 5-line pseudo: “sort → for loop → bisect → max → return.” |

---

## 🪄 Quick Verbal Template (for interviewer explanation)

> “I’ll sort jobs by end time, then for each job I’ll use binary search to find the previous job that ends before it starts.
> My DP relation is `dp[i] = max(dp[i-1], profit[i] + dp[prev[i]])`.
> This gives O(n log n) time and O(n) space.”

---

## ✏️ Sticky-note memory version

```
Weighted Job Scheduling
------------------------
1️⃣ Sort by end
2️⃣ prev = binsearch(end <= start)
3️⃣ dp[i] = max(skip, take)
    skip = dp[i-1]
    take = profit[i] + dp[prev]
4️⃣ return dp[-1]
🧠 Mnemonic: SORT → SEARCH → MAX
```

Stick that mentally (or literally on your notebook margin).
You’ll rebuild this entire solution in **under 30 seconds** during any interview.
