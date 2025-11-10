Perfect — here’s your **5-line pseudo-code template** and **recall mnemonic** for the **Stock Buy and Sell with Cooldown** problem.
You can rebuild this in **30 seconds** in any language (Python, C++, Java, etc.) before an interview.

---

## 🧩 5-Line Pseudo-code Template

*(core logic — the heart of every optimal DP solution for this problem)*

```
hold = -price[0]; sold = -∞; rest = 0
for price in prices[1:]:
    new_hold = max(hold, rest - price)
    new_sold = hold + price
    new_rest = max(rest, sold)
    hold, sold, rest = new_hold, new_sold, new_rest
return max(sold, rest)
```

✅ **Time Complexity:** O(n)
✅ **Space Complexity:** O(1)
✅ **Answer:** max(sold, rest) (since we don’t want to end holding a stock)

---

## 🧠 Mnemonic — **“HSR → Hold, Sold, Rest”**

Memorize this single line:

> **“Hold from Rest, Sold from Hold, Rest from Rest/Sold.”**

That’s the full logic encoded in one sentence:

| State    | Formula                   | Meaning                                                |
| -------- | ------------------------- | ------------------------------------------------------ |
| **Hold** | `max(hold, rest - price)` | Either continue holding or buy today (only if resting) |
| **Sold** | `hold + price`            | You must sell a stock you were holding                 |
| **Rest** | `max(rest, sold)`         | You’re either cooling down or doing nothing            |

---

## 🧩 60-Second Recall Routine (Pre-Interview Drill)

| Seconds    | What to Recall                        | Mental Shortcut                                                       |
| ---------- | ------------------------------------- | --------------------------------------------------------------------- |
| **0–10s**  | **Define 3 states:** hold, sold, rest | “Hold = have stock; Sold = just sold; Rest = empty hand”              |
| **10–20s** | **Write transitions**                 | “Hold from Rest - price; Sold from Hold + price; Rest from Rest/Sold” |
| **20–30s** | **Base cases**                        | `hold=-price[0], sold=-∞, rest=0`                                     |
| **30–45s** | **Loop and update**                   | Use temp variables or tuple swap                                      |
| **45–60s** | **Answer & complexity**               | “Return max(sold, rest); O(n) time, O(1) space.”                      |

---

## 🧱 Sticky-Note Visual (mental cheat code)

```
H → S → R
↑     ↓
←-----←
Buy → Hold → Sell → Rest → (buy again)
```

🔁 After every **Sell**, there’s **Rest** (cooldown).
Then only from **Rest** can you **Buy** again.

---

## 🪄 Quick Verbal Template (say this in your interview)

> “I track 3 states per day — hold, sold, and rest.
> Hold means I own a stock, sold means I sold today, and rest means I’m free to buy.
> I update them daily with:
>
> * hold = max(hold, rest - price)
> * sold = hold + price
> * rest = max(rest, sold)
>   Finally, I return max(sold, rest).
>   It runs in O(n) time and O(1) space.”

---

🎯 **Memory Hook Summary:**

> 🧠 **HSR Pattern:**
> “Hold from Rest, Sold from Hold, Rest from Rest or Sold.”

You’ll rebuild and explain this in **under 60 seconds** — guaranteed.
