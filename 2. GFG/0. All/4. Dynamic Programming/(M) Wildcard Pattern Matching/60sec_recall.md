**“5-line pseudo-code template”** and a **mnemonic recall system** that helps you rebuild the entire Wildcard Pattern Matching algorithm in **under 60 seconds** before an interview.

---

## 🧩 5-Line Pseudo-code Template

*(This is the exact skeleton for the DP version — can be rewritten in Python, C++, or Java instantly.)*

```
dp[0][0] = True
for i in 1..m: if pat[i-1]=='*': dp[i][0] = dp[i-1][0]

for i in 1..m:
  for j in 1..n:
    if pat[i-1]=='*': dp[i][j] = dp[i-1][j] or dp[i][j-1]
    elif pat[i-1]=='?' or pat[i-1]==txt[j-1]: dp[i][j] = dp[i-1][j-1]
    else: dp[i][j] = False

return dp[m][n]
```

✅ **Time Complexity:** O(n × m)
✅ **Space Complexity:** O(n × m)
✅ **Answer:** `dp[m][n]` → True if pattern matches full text

---

## 🧠 Mnemonic — **“Star is Flexible, Question is Diagonal”**

Memorize this one line:

> **“Star = Up or Left, Question = Diagonal, Letter = Diagonal if Equal.”**

| Pattern     | DP Move                    | Meaning                     |
| ----------- | -------------------------- | --------------------------- |
| `*`         | `dp[i-1][j] OR dp[i][j-1]` | *Empty* or *match one more* |
| `?`         | `dp[i-1][j-1]`             | Matches *exactly one*       |
| Normal char | `dp[i-1][j-1] if equal`    | Must match directly         |

---

## 🧱 60-Second Recall Routine (Mental Rehearsal Before Interview)

| Seconds    | What to Recall       | Key Phrase                                       |
| ---------- | -------------------- | ------------------------------------------------ |
| **0–10s**  | Define states        | `dp[i][j] = pattern[:i] matches text[:j]`        |
| **10–20s** | Base cases           | `dp[0][0]=True`; `dp[i][0]=True if all '*'`      |
| **20–35s** | Star rule            | “`*` → (Up or Left): `dp[i-1][j] or dp[i][j-1]`” |
| **35–50s** | Question/Letter rule | “`?` → Diagonal, letter → Equal & Diagonal”      |
| **50–60s** | Return               | `dp[m][n]` is the final answer                   |

---

## 🔁 Mental Sticky-Note (quick sketch memory)

```
      j →
    +---+---+---+---+
  i |   | t | e | x |
    +---+---+---+---+
p | * | ↑or← | ← | ← |   # * extends in both directions
a | ? | ↖     |   |   |   # ? or letter moves diagonal
t | a | ↖     |   |   |
```

📌 **Visual mnemonic:**

* `↑` (up)  → skip `*` (empty)
* `←` (left) → consume one char with `*`
* `↖` (diagonal) → move one-to-one for `?` or same char

---

## 🗣️ Quick Verbal Template (for interview explanation)

> “I use DP where `dp[i][j]` means pattern prefix `pat[:i]` matches text prefix `txt[:j]`.
> `*` can be empty or consume one char → `dp[i][j] = dp[i-1][j] or dp[i][j-1]`.
> `?` or equal characters → move diagonally from `dp[i-1][j-1]`.
> Finally, `dp[m][n]` gives full match.
> Runs in O(n×m) time and O(n×m) space.”

---

### 🧩 Shortcut Recap in 10 Words:

> **“Star Up/Left, Question Diagonal, Equal Diagonal, Base Empty.”**

That’s your 30-second rebuild and 60-second explanation mastery formula 🚀
