**“5-line pseudo-code template”** plus a **mnemonic recall system** you can rebuild in **under 30 seconds** before any interview.

---

## 🧩 5-Line Pseudo-Code Template

*(for “Number of Paths in Matrix with Exactly K Coins”)*

```
1. if out of bounds or k < 0: return 0
2. if at destination: return 1 if k == mat[i][j] else 0
3. rem = k - mat[i][j]
4. return ways(i+1, j, rem) + ways(i, j+1, rem)
5. use memo[i][j][k] to avoid recomputation
```

✅ **Time:** O(n × m × k)
✅ **Space:** O(n × m × k) (or O(m × k) with rolling DP)

---

## 🧠 Easy Mnemonic — **“CUT → BASE → SUB → ADD → CACHE”**

| Step  | Word      | What to Remember                                | Example                            |
| ----- | --------- | ----------------------------------------------- | ---------------------------------- |
| **C** | **CUT**   | Cut recursion if out of bounds or overshoot sum | `if i>=n or j>=m or k<0:`          |
| **B** | **BASE**  | Handle destination cell                         | `if (n-1,m-1): return 1 if k==val` |
| **S** | **SUB**   | Subtract cell value from remaining target       | `rem = k - mat[i][j]`              |
| **A** | **ADD**   | Add ways from right & down                      | `down + right`                     |
| **C** | **CACHE** | Memoize the state `(i,j,k)`                     | `dp[i][j][k]`                      |

👉 So just remember: **“CUT, BASE, SUB, ADD, CACHE.”**

---

## ⚙️ 60-Second Recall Routine (mental checklist before interview)

| Seconds | Recall Step          | Key Thought                                                        |
| ------- | -------------------- | ------------------------------------------------------------------ |
| 0-10 s  | **State definition** | “`f(i,j,k)` = # paths from (i,j) to end with exactly k coins.”     |
| 10-20 s | **Recurrence**       | “`f(i,j,k) = f(i+1,j,k-val) + f(i,j+1,k-val)`.”                    |
| 20-30 s | **Base cases**       | “Stop when out-of-bounds or target < 0; destination must equal k.” |
| 30-45 s | **Memoization**      | “Use 3D memo [i][j][k] to cut duplicates.”                         |
| 45-60 s | **Complexity/flow**  | “O(n m k) time/space; prune early if k < mat[i][j].”               |

---

## 🪄 Quick verbal template (say this to interviewer)

> “I’ll define a recursive DP `f(i,j,k)` that counts paths from (i,j) collecting exactly k coins.
> From each cell, subtract its value from k and go Right or Down.
> Base case: if I reach the end and remaining k equals that cell’s value, count 1.
> I’ll memoize `(i,j,k)` for O(n m k) time and space.”

---

## 🧱 Sticky-note version (you can write on paper in 5 sec)

```
# f(i,j,k)
if out OR k<0: return 0
if end: return (k==val)
rem = k - val
return f(i+1,j,rem) + f(i,j+1,rem)
memo[i][j][k]
# Mnemonic: CUT → BASE → SUB → ADD → CACHE
```

Memorize that — you can rebuild the full DP solution in **any language within 30 seconds.**
