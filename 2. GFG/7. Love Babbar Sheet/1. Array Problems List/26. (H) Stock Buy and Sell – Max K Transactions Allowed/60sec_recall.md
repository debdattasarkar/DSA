 **5-line pseudo-code template + 60-second recall kit** for
🧩 **Stock Buy & Sell — Max K Transactions Allowed** (classic DP + state-machine form).

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
if k >= n/2: return sum(max(0, p[i]-p[i-1]))   # unlimited case
buy  = [-inf]*(k+1)
sell = [0]*(k+1)
for price in prices:
    for t in 1..k:
        buy[t]  = max(buy[t],  sell[t-1] - price)
        sell[t] = max(sell[t], buy[t] + price)
return sell[k]
```

✅ **O(n·k)** time, **O(k)** space
✅ Handles unlimited-transactions optimization
✅ Language-agnostic (works in Python, C++, Java)

---

## 🧠 Easy Mnemonic — “**B–S Loop**” → *Buy, Sell, Loop through days & k*

| Step     | Meaning                                    | Visual cue             |
| -------- | ------------------------------------------ | ---------------------- |
| **B**    | Maintain best cash after a **Buy**         | 📉 “money down”        |
| **S**    | Maintain best cash after a **Sell**        | 💰 “profit up”         |
| **Loop** | Update both for each price and transaction | 🔁 arrows through days |
| **End**  | Return last `sell[k]`                      | 🏁 final balance       |

> 💬 **Catchphrase:**
> “Track best Buy/Sell at each transaction level — Buy low, Sell high, Repeat!”

---

## 🕒 60-Second Interview Recall Routine

1. **State the goal:**
   “Max profit in at most `k` buy/sell pairs; no overlapping transactions.”

2. **Identify base cases:**

   * `k == 0 or n <= 1 → 0`
   * `k >= n/2 → unlimited trades → sum of positive rises.`

3. **Core recurrence (think state machine):**

   * `buy[t]  = max(buy[t],  sell[t-1] - price)`
   * `sell[t] = max(sell[t], buy[t] + price)`

4. **Explain flow:**

   * Iterate prices once.
   * For each `t=1..k`, update both states.

5. **Say complexity:**

   * Time: O(n·k)
   * Space: O(k)
   * Early exit for `k >= n/2` → O(n).

---

### 🧩 Sticky-line summary (to recall in 10s)

> “**Buy-Sell per k → max(B, S–P) / max(S, B+P)** — end with S[k].**”
