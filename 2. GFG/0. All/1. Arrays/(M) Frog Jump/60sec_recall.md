**5-line pseudo-code template** + **mnemonic recall method** you can use for **Frog Jump** or any **1–2 step DP** problem.

---

## 🧩 5-Line Pseudo-code Template

```
1. dp0 = 0
2. dp1 = |h1 - h0|
3. for i = 2 → n-1:
       dpi = min(dp1 + |hi - h(i-1)|, dp0 + |hi - h(i-2)|)
       dp0, dp1 = dp1, dpi
4. return dp1
```

That’s it — 5 lines, portable to **Python / C++ / Java / JS** instantly.

---

## 🧠 Easy Mnemonic — **“1-2 DP → Slide & Min”**

Say this 5-word chant in your head right before the coding round:

> **“One-Two DP — Slide and Min!”**

It reminds you that:

* You can jump **1 or 2** steps.
* You’re doing **DP**.
* You only **slide** two variables (rolling window).
* And you always take the **minimum** cost.

---

## ⚙️ 60-Second Recall Routine (Pre-interview brain warm-up)

Spend **under 1 minute** recalling these checkpoints mentally:

| Step | What to Recall                      | Why it matters     |               |                            |
| ---- | ----------------------------------- | ------------------ | ------------- | -------------------------- |
| 1️⃣  | “`dp[i] = min(from i-1, from i-2)`” | Core recurrence    |               |                            |
| 2️⃣  | “`                                  | height diff        | ` gives cost” | Transition cost            |
| 3️⃣  | “Base cases: dp0=0, dp1=            | h1-h0              | ”             | Always initialize properly |
| 4️⃣  | “Keep two vars: prev2, prev1”       | Space optimization |               |                            |
| 5️⃣  | “Answer = last dp”                  | Final result       |               |                            |

Bonus: visualize a frog hopping up stairs with numbers — each jump’s cost is the **height gap**, and you choose the cheaper of 1-step vs 2-step.

---

### ⚡ Quick Verbal Rebuild Example (how to say it out loud in interview)

> “I’ll use dynamic programming with O(1) space.
> Base: dp0 = 0, dp1 = |h1-h0|.
> Then for each i ≥ 2,
> dp = min(dp1 + |hi-h(i-1)|, dp0 + |hi-h(i-2)|).
> Finally return dp1, updating dp0, dp1 as we go.”

That’s **under 20 seconds** to explain **and** code the skeleton.

---

✅ **Summary mnemonic you can write on scratchpad in 5 seconds:**

```
1-2 DP → Slide & Min
dp0=0, dp1=|h1-h0|
for i: dp=min(dp1+|i-1|, dp0+|i-2|)
slide dp0,dp1
```

You can reconstruct the full code from just that pattern in any language.
