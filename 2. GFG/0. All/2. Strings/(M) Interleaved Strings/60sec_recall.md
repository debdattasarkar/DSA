**5-line pseudo-code template** and **memory recall system** for the **Interleaved Strings problem** that you can rebuild in **30 seconds** before an interview.

---

## 🧩 5-Line Pseudo-code Template

This is the **exact DP skeleton** that works in any language (Python, C++, Java, etc.):

```
if len(s1)+len(s2) != len(s3): return False
dp[0][0] = True
for i in range(n1+1):
  for j in range(n2+1):
    if i>0: dp[i][j] |= dp[i-1][j] and s1[i-1]==s3[i+j-1]
    if j>0: dp[i][j] |= dp[i][j-1] and s2[j-1]==s3[i+j-1]
return dp[n1][n2]
```

✅ **Time Complexity:** O(n1 × n2)
✅ **Space Complexity:** O(n2) (can be reduced with row compression)

---

## 🧠 Mnemonic — **“Pick from S1 (↑) or S2 (←) if they match S3 (↖)”**

Memorize this one sentence:

> “At each step, you can take the next character from S1 or S2 — if it matches the current position of S3.”

Or visualize it as:

| Move  | Meaning                                          |
| ----- | ------------------------------------------------ |
| **↑** | Took a char from `s1` → check `dp[i-1][j]`       |
| **←** | Took a char from `s2` → check `dp[i][j-1]`       |
| **↖** | Both possible → if either path works, it’s valid |

So `dp[i][j] = (top match) or (left match)`

---

## 🧱 60-Second Recall Routine (Mental Rehearsal)

| Seconds | What to Recall                                           | Mnemonic                                    |
| ------- | -------------------------------------------------------- | ------------------------------------------- |
| 0–10    | **State**: `dp[i][j]` means s1[:i], s2[:j] form s3[:i+j] | “Prefix match up to i+j”                    |
| 10–25   | **Transition**: From top (s1) or left (s2)               | “Pick ↑ or ← if matches current char of s3” |
| 25–40   | **Base**: `dp[0][0]=True`                                | “Empty + empty = empty”                     |
| 40–50   | **Precheck**: total length must match                    | `if len(s1)+len(s2)!=len(s3): return False` |
| 50–60   | **Answer**: `return dp[n1][n2]`                          | “Full prefixes must match full s3”          |

---

## 📌 Quick Visual Sticky Note (for paper/whiteboard memory)

```
        s2 →
     +---+---+---+---+
 s1  | T |   |   |   |
 ↓   +---+---+---+---+
     |   | ↑ | ← | ↖ |
     +---+---+---+---+

↑ = from s1 (check dp[i-1][j])
← = from s2 (check dp[i][j-1])
↖ = both valid
```

---

## 🗣️ Quick Interview Explanation Template (say this out loud)

> “I use DP where `dp[i][j]` means whether the first `i` characters of `s1` and the first `j` of `s2` form the first `i+j` of `s3`.
> For each position, I check if the current character of `s3` matches either from `s1` (top) or `s2` (left).
> If yes, I mark it True.
> Finally, `dp[n1][n2]` gives the result.
> Runs in O(n1×n2) time and O(n2) space.”

---

### 🔁 10-Word Memory Hook:

> **“Match from Top or Left if Char Equals in S3.”**

That’s it — your 30-second rebuild + 60-second full recall recipe for **Interleaved Strings** ✅
