Absolutely — here is your **5-line pseudo-code**, **mnemonic**, and **60-second interview recall routine** for the *Row With Maximum 1s* problem.

---

# ✅ 5-Line Pseudo-Code Template (Optimal O(n + m))

```
row = 0; col = m - 1; best = -1
while row < n and col >= 0:
    if arr[row][col] == 1:
        best = row; col -= 1     # move LEFT on 1
    else:
        row += 1                 # move DOWN on 0
return best
```

This is all you need to reconstruct the full solution.

---

# 🎯 Mnemonic (Extremely Easy)

## **“Top-Right → 1 Left, 0 Down.”**

Visualize a chant:

👉 **Start at top-right**
👉 **If 1 → go left** (more 1s in this row)
👉 **If 0 → go down** (row can’t beat previous rows)

It’s that simple.

---

# 🧠 Why it Works (Interview 10-second line)

> “Because rows are sorted (0s then 1s), moving left only happens when a row proves it has more 1s than previous rows. Moving down skips rows that can't beat the current best. Since we only move left or down, we take at most n+m steps.”

---

# ⏱️ 60-Second Interview Recall Routine

### **0–10 seconds — Problem Recognition**

“Each row is 0…01…1. Find row with most 1s. Sorted rows → monotonic grid traversal trick.”

### **10–20 seconds — Starting Point**

“Top-right cell (0, m-1).”

### **20–35 seconds — Movement Rule**

* If `1` → move **left**, row becomes candidate
* If `0` → move **down**, row useless

### **35–45 seconds — Why Best Updates on 1**

“Every left move indicates more 1s in current row → update best row.”

### **45–55 seconds — Time Complexity**

“At most (n+m) moves → O(n+m). Space O(1).”

### **55–60 seconds — Summary to interviewer**

> “I start top-right, move left when I see 1, down when I see 0. Maintain best row. Finish in O(n+m).”

---

# 🪄 Edge-Case Quick Checks

* All zeros → best = -1
* First row has most 1s → discovered immediately
* Large n,m → safe because complexity is linear in dimensions

