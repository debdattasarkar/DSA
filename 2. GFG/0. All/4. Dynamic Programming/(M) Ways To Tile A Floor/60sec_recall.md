Perfect — here’s your **5-line pseudo-code template** and a **memory hook** you can recall and rebuild instantly before an interview.
This is tailored for **“Ways to Tile a 2×n Floor”**, but it’s also a general pattern for any Fibonacci-like DP.

---

## 🧩 5-Line Pseudo-Code Template

```
1. dp0 = 1, dp1 = 1             # base cases
2. for i = 2 → n:               # iterate from 2 to n
3.     dp = dp1 + dp0           # recurrence relation (ways[n] = ways[n-1] + ways[n-2])
4.     dp0, dp1 = dp1, dp       # slide window forward
5. return dp1                   # final answer
```

✅ **Time:** O(n)
✅ **Space:** O(1)
✅ **Universal:** Works in Python, C++, Java, JS — same pattern.

---

## 🧠 Easy Mnemonic – **“1-2 SLIDE & SUM”**

Say it mentally before you start coding — it covers everything!

| Step      | Meaning                     | What to do           |
| --------- | --------------------------- | -------------------- |
| **1**     | “1-2”                       | Base cases for n=0,1 |
| **SLIDE** | Use two rolling variables   | `dp0`, `dp1`         |
| **& SUM** | Add the two previous values | `dp = dp1 + dp0`     |

👉 **“1-2 SLIDE & SUM”** =
Start with 1, 1 → loop → sum previous two → slide → done.

---

## ⚙️ 60-Second Recall Checklist Before Interview

When interviewer says “Ways to Tile a Floor” or any Fibonacci-style DP:

| Time      | What to Recall                 | What to Say / Think                           |
| --------- | ------------------------------ | --------------------------------------------- |
| 0–10 sec  | 🎯 **State**                   | “ways[i] = number of ways to tile 2×i board.” |
| 10–20 sec | 🧮 **Transition**              | “ways[i] = ways[i-1] + ways[i-2].”            |
| 20–30 sec | ⚙️ **Base cases**              | “ways[0]=1, ways[1]=1.”                       |
| 30–45 sec | 💡 **Space optimization**      | “Only depends on last two → rolling vars.”    |
| 45–60 sec | 🧱 **Code skeleton (5 lines)** | mentally repeat “1-2 SLIDE & SUM.”            |

---

### 🪄 Quick Verbal Explanation (when interviewer asks for logic)

> “For a 2×n board, either the last column is one vertical tile (reduces to n−1)
> or two horizontals stacked (reduces to n−2).
> So the recurrence is `ways[n] = ways[n-1] + ways[n-2]`.
> I’ll implement it in O(n) time and O(1) space with two rolling variables.”

---

### ✅ TL;DR Summary Sticky Note

```
# Ways to Tile 2×n
dp0, dp1 = 1, 1
for i in 2..n:
    dp = dp1 + dp0
    dp0, dp1 = dp1, dp
return dp1
# Mnemonic: "1-2 SLIDE & SUM"
```
