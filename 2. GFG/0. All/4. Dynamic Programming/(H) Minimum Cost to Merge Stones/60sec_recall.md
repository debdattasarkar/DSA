**“5-line pseudo-code template”** and a **super easy mnemonic system** so you can rebuild the entire **Minimum Cost to Merge Stones** solution from memory in *under a minute* before an interview.

---

## 🧩 5-Line Pseudo-Code Template

*(This is the exact skeleton you can retype instantly in any language — Python, C++, Java, etc.)*

```
if (n - 1) % (k - 1) != 0: return -1
pref[i] = prefix sum of stones
dp[i][i] = 0
for len = 2..n:
  for i..:
    j = i + len - 1
    dp[i][j] = min_{m = i, i+(k-1), ... < j}(dp[i][m] + dp[m+1][j])
    if (len - 1) % (k - 1) == 0: dp[i][j] += sum(i..j)
return dp[0][n-1]
```

✅ **Time Complexity:** O(n³)
✅ **Space Complexity:** O(n²)

---

## 🧠 Mnemonic — “**Merge by (k−1) → Add Sum when One Left**”

Use this short memory phrase:

> **“Check feasible, range-sum ready, merge by gap (k−1), add sum if single.”**

Breakdown:

| Step                      | Meaning                                   |
| ------------------------- | ----------------------------------------- |
| ✅ **Check feasible**      | `(n−1)%(k−1)==0`, else return `-1`        |
| 🧮 **Range-sum ready**    | Use prefix sums for O(1) interval totals  |
| 🔁 **Merge by gap (k−1)** | Split intervals at steps of `(k−1)` only  |
| ➕ **Add sum if single**   | Add total pile sum when interval → 1 pile |
| 🎯 **Return dp[0][n−1]**  | Final minimum merge cost                  |

---

## ⏱️ 60-Second Recall Routine (Brain Warm-up Before Interview)

| Seconds    | What to Recall | Memory Hook                                      |
| ---------- | -------------- | ------------------------------------------------ |
| **0–10s**  | Feasibility    | “(n−1) % (k−1) == 0 → else impossible.”          |
| **10–20s** | Prefix sums    | “Need `sum(i,j)` fast → build once.”             |
| **20–35s** | DP State       | “`dp[i][j]` = min cost to merge stones[i..j].”   |
| **35–50s** | Split rule     | “Only split at steps of `(k−1)`.”                |
| **50–60s** | Add sum rule   | “If interval can shrink to 1 pile, add its sum.” |

> ⏳ By the time you hit 60s, you can rebuild both top-down and bottom-up DP from this skeleton.

---

## 🧱 Quick Visual Sticky-Note (mental diagram)

```
     Merge cost only when interval length
     can become ONE pile
      ↓
 i ───────────────────── j
 |  split every (k-1)   |
 |  dp[i][j] = dp[i][m] + dp[m+1][j]  |
 |  + sum(i..j) if (len-1)%(k-1)==0   |
```

**“(k−1) gap split + conditional add”** — that’s the heart of it.

---

## 🗣️ Quick Interview Explanation Template (say this out loud)

> “We first check if merging to one pile is even possible using `(n−1)%(k−1)`.
> Then, we define `dp[i][j]` as the minimum cost to merge stones between i and j.
> We try all split points stepping by `(k−1)` since merging removes `(k−1)` piles each time.
> When the interval length allows it to form one pile, we add the sum of that segment.
> Finally, `dp[0][n−1]` gives the minimum cost.
> Time is O(n³), space O(n²).”

---

### ⚡ 10-word summary:

> **“Check feasible → merge by (k−1) → add sum if single.”**

That’s your 30-second rebuild + 60-second full recall for **Minimum Cost to Merge Stones** — completely interview-proof 🚀
