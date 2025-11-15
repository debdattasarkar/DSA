**5-line pseudo-code template** for **LCIS (Longest Common Increasing Subsequence)**, plus an **easy mnemonic** that guarantees you can recall and rebuild it in *under 60 seconds* before an interview.

---

## 🧩 5-Line Pseudo-code Template

This is the **minimal skeleton** that captures the entire algorithm — language-agnostic and rebuildable in 30 seconds:

```
dp[0..m-1] = 0
for each x in a:
    best = 0
    for j in 0..m-1:
        if b[j] < x: best = max(best, dp[j])
        elif b[j] == x: dp[j] = max(dp[j], best + 1)
return max(dp)
```

✅ **Time Complexity:** O(n × m)
✅ **Space Complexity:** O(m)

---

## 🧠 Mnemonic — “**SCAN–COMPARE–MATCH–EXTEND**”

Think of the LCIS process as four brain-steps you can say out loud:

| Step           | Meaning                                     | Visual cue                |
| -------------- | ------------------------------------------- | ------------------------- |
| 🧭 **SCAN**    | Go through each element in `a`              | Left-to-right scan over A |
| ⚖️ **COMPARE** | Compare with each element in `b`            | Nested loop               |
| 🔗 **MATCH**   | If values are equal → potential subsequence | Connecting same numbers   |
| ⛓️ **EXTEND**  | Extend from best smaller subsequence        | Chain grows only upward   |

> **Mnemonic sentence:**
> “Scan A, Compare with B — when Match found, Extend chain upward.”

---

## 🔁 60-Second Recall Routine (Before Interview)

| Time        | Recall Focus       | What You Say To Yourself                             |
| ----------- | ------------------ | ---------------------------------------------------- |
| **0–10 s**  | State definition   | "`dp[j]` = LCIS ending exactly at b[j]."             |
| **10–20 s** | Outer loop         | “For every element `x` in A…”                        |
| **20–30 s** | Inner loop idea    | “Track best LCIS length among smaller values in B.”  |
| **30–45 s** | Condition handling | “If b[j] < x → update best; if b[j] == x → extend.”  |
| **45–60 s** | Final step         | “Answer is max(dp). That’s O(n×m) time, O(m) space.” |

✅ After 60 seconds, you can *write or explain* the full LCIS algorithm fluently.

---

## 🧱 Quick Visual (mental sticky-note)

```
     A[i]=x   →   scan B
                ↓
        smaller → update best
        equal   → dp[j] = best + 1
                ↓
             max(dp) → answer
```

---

## 🗣️ Interview-ready one-liner explanation

> “We keep `dp[j]` as LCIS ending at `b[j]`.
> For each `a[i]`, we walk `b` left to right.
> We track `best = max(dp[j])` for all `b[j] < a[i]`.
> When `b[j] == a[i]`, we extend it by `best + 1`.
> Finally, `max(dp)` gives the result in O(n·m) time.”

---

### ⚡ 10-Word Memory Hook:

> **“Scan A → Track smaller in B → Extend on match → Max.”**

That’s your **30-second rebuild + 60-second verbal recall plan** for **LCIS**, guaranteed to impress in interviews 🔥
