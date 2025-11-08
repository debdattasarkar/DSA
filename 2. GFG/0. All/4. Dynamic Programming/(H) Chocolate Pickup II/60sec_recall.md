**“5-line pseudo-code template”** and **mnemonic recall strategy** for **Chocolate Pickup II (a.k.a. Cherry Pickup / Two-Robot DP)**.
This is what top candidates use to instantly rebuild the logic in any language under 30 seconds.

---

## 🧩 5-Line Pseudo-code Template

*(Universal — Python, C++, Java, JS… same skeleton)*

```
1. dp(r1, c1, c2):
2.     r2 = r1 + c1 - c2                          # same total steps
3.     if any out_of_bounds / blocked: return -∞
4.     if all at end: return mat[n-1][n-1]
5.     gain = mat[r1][c1] + (mat[r2][c2] if (r1,c1)!=(r2,c2) else 0)
       return gain + max( dp(r1+1,c1,c2), dp(r1,c1+1,c2),
                          dp(r1+1,c1,c2+1), dp(r1,c1+1,c2+1) )
```

✅ **Time Complexity:** O(n³)
✅ **Space Complexity:** O(n³) (or O(n²) if bottom-up compressed)

---

## 🧠 Mnemonic — **“TWO WALKERS → SAME STEP → FOUR MOVES → AVOID DOUBLE COUNT.”**

Say this in your head:

> “Two walkers, same step, check bounds, collect once, explore four moves.”

Break it down:

| Step                       | Idea                                            | What to Code                            |
| -------------------------- | ----------------------------------------------- | --------------------------------------- |
| 🧍‍♂️🧍‍♀️ **Two walkers** | Simulate both forward and return trips together | `dp(r1,c1,c2)` with `r2 = r1 + c1 - c2` |
| 🧮 **Same step**           | Total moves are equal (r+c)                     | Derive r2 this way                      |
| 🚫 **Check bounds**        | Skip invalid / blocked states                   | Return `-inf`                           |
| 🍫 **Collect once**        | Add chocolates; if same cell, count once        | Use `if (r1,c1)!=(r2,c2)`               |
| 🔁 **Four moves**          | Down/Right combos for both walkers              | Try 4 recursive branches                |

---

## ⚙️ 60-Second Recall Routine Before Interview

| Seconds | Step                   | What to Recall                                         |
| ------- | ---------------------- | ------------------------------------------------------ |
| 0–10    | **State meaning**      | “dp(r1,c1,c2): walker1 at (r1,c1), walker2 at (r2,c2)” |
| 10–20   | **r2 relation**        | “r2 = r1 + c1 - c2 (same step)”                        |
| 20–30   | **Base case**          | “If both at (n-1,n-1): return mat[n-1][n-1]”           |
| 30–40   | **Transitions**        | “Four moves: (D,D), (D,R), (R,D), (R,R)”               |
| 40–50   | **Avoid double-count** | “Count once if both same cell”                         |
| 50–60   | **Answer**             | “Return max(0, dp(0,0,0)) — if impossible, 0.”         |

---

## 🪄 Quick Verbal Template (for explaining to interviewer)

> “I treat the two trips as two robots walking together from (0,0) to (n-1,n-1).
> At any step, both have taken the same number of moves, so r2 = r1 + c1 - c2.
> I collect chocolates once per unique cell, skip blocked states, and take the max over four move combinations.
> DP has O(n³) states and O(1) transition per state.”

---

## 🧱 Sticky-note Recall (write this mentally on your scratchpad)

```
dp(r1,c1,c2):
 r2 = r1+c1-c2
 if invalid: return -∞
 if end: return mat[n-1][n-1]
 gain = mat[r1][c1] + (mat[r2][c2] if diff)
 return gain + max(4 moves)
# Mnemonic: "Two Walkers — Same Step — 4 Moves — Count Once"
```

That’s all you need — you can now **rebuild the full solution in under 30 seconds** and explain it confidently in an interview.
