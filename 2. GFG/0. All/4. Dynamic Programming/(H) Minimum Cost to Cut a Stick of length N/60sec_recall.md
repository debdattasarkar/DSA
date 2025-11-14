**“5-line pseudo-code template”** for the **Minimum Cost to Cut a Stick** problem, plus a quick **mnemonic memory system** that helps you recall and rebuild the full logic in *30 seconds flat* before any interview.

---

## 🧩 5-Line Pseudo-code Template

This is the minimal skeleton you can instantly rebuild in any language (Python, C++, Java, etc.):

```
cuts = [0] + sort(cuts) + [n]
for len = 2..m:
  for i = 0..m-len:
    j = i + len
    dp[i][j] = min( (cuts[j]-cuts[i]) + dp[i][k] + dp[k][j] for k in i+1..j-1 )
return dp[0][m-1]
```

✅ **Time Complexity:** O(m³)
✅ **Space Complexity:** O(m²)

Where `m = len(cuts) + 2` (we add the boundaries 0 and n).

---

## 🧠 Mnemonic — “Add Ends → Cut Inside → Pay Length → Merge Min”

**Sentence mnemonic (easy to speak before coding):**

> “Add boundaries, choose each cut as the first, pay its length, merge left and right for min cost.”

**Breakdown:**

| Step                  | Meaning                                                       |
| --------------------- | ------------------------------------------------------------- |
| 🧱 **Add boundaries** | `[0] + sorted(cuts) + [n]` ensures we know the stick edges.   |
| ✂️ **Cut inside**     | For each interval `(i, j)`, try every possible inner cut `k`. |
| 💰 **Pay length**     | Each chosen first cut costs `cuts[j] - cuts[i]`.              |
| 🔁 **Merge min**      | Combine left and right sub-costs with the smallest total.     |
| 🎯 **Return**         | `dp[0][m-1]` is the answer.                                   |

---

## 🧱 60-Second Recall Routine (Before Interview)

| Seconds    | What to Recall                                                   | Mental Hook                      |
| ---------- | ---------------------------------------------------------------- | -------------------------------- |
| **0–10s**  | State: `dp[i][j] = min cost to cut between cuts[i] and cuts[j]`. | “DP on stick intervals.”         |
| **10–20s** | Base case: `dp[i][i+1] = 0`.                                     | “No cuts inside → no cost.”      |
| **20–35s** | Transition: try each inner cut `k`.                              | “Cut at k → pay segment length.” |
| **35–50s** | Add prefix boundaries 0, n.                                      | “Add ends → avoid edge chaos.”   |
| **50–60s** | Return `dp[0][m-1]`.                                             | “Final min cost from 0 to n.”    |

> 🧩 **Mental summary phrase:**
> **“Interval DP → Try every cut → Pay segment length → Pick min.”**

---

## 🔍 Sticky-note Visualization

```
Stick: 0-----x----y------n
cuts = [0, x, y, n]

dp[i][j] = min(
   (cuts[j]-cuts[i])   # cost of cutting this piece
 + dp[i][k]            # cost of left part
 + dp[k][j]            # cost of right part
)
```

* You always **pay** the full segment length when you make a cut.
* The recursion ensures you **minimize total sequence cost**.

---

## 🗣️ Interview Quick Explanation (say this out loud)

> “We sort cuts and add boundaries 0 and n.
> Then, we use interval DP where `dp[i][j]` is the minimum cost to cut between `cuts[i]` and `cuts[j]`.
> For each possible first cut `k`, we pay the current segment length `cuts[j]-cuts[i]` plus left and right sub-costs.
> Finally, we take the minimum across all possible `k`.
> Time is O(m³), space O(m²).”

---

### ⚡ 10-word Memory Hook:

> **“Add 0,n → Cut k → Pay length → Min left+right.”**

That’s your **30-second rebuild** and **60-second interview recall plan** for *Minimum Cost to Cut a Stick* ✅
