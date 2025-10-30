Perfect — this one is a **pattern you’ll see a dozen times** (like “Capture Regions,” “Number of Islands,” “Enclosed Areas,” etc.).
Here’s your short **5-line pseudo-code skeleton** plus a **60-second mental recall cheat** that will keep you safe in any interview.

---

## 🧠 5-Line Pseudo-code Template (Replace O’s with X’s)

```
for each border cell:
    if it's 'O': flood_fill(mark='S')           # DFS/BFS from border 'O's
for each cell:
    if it's 'O': flip to 'X'                    # Surrounded
    if it's 'S': restore to 'O'                 # Safe
```

That’s it.
Everything (DFS recursion or BFS queue) hides inside `flood_fill()`.

---

## ⚙️ Expanded (to show the full mental shape)

```
function fill(grid):
    # 1️⃣ Flood from borders
    for each border cell:
        if grid[r][c] == 'O': mark_safe(r, c)

    # 2️⃣ Sweep entire grid
    for each cell:
        if grid[r][c] == 'O': grid[r][c] = 'X'   # trapped
        if grid[r][c] == 'S': grid[r][c] = 'O'   # restore safe

function mark_safe(r, c):
    grid[r][c] = 'S'
    for each neighbor (up, down, left, right):
        if inside grid and grid[nr][nc] == 'O':
            mark_safe(nr, nc)
```

---

## 🎯 Mnemonic: **“B–M–F–R”**

Say this like a rhythm before coding — it maps to your thought process.

| Step  | Mnemonic    | Meaning                          |
| ----- | ----------- | -------------------------------- |
| **B** | Border      | Start only from border `'O'`s    |
| **M** | Mark Safe   | Flood-fill them as `'S'`         |
| **F** | Flip Others | Flip any remaining `'O'` → `'X'` |
| **R** | Restore     | Convert `'S'` → `'O'`            |

So just recall:

> **“B–M–F–R → Border → Mark → Flip → Restore.”**

---

## ⏱️ 60-Second Interview Recall Routine

🕐 **0–10 sec:**
Recognize problem: “Ah — surrounded regions. It’s a boundary flood-fill.”

🕐 **10–25 sec:**
Say logic out loud:

> “Any ‘O’ connected to border stays ‘O’; others flip to ‘X’.”
> Write down: “BFS/DFS from border → mark safe.”

🕐 **25–45 sec:**
Sketch mini pseudocode:

```
for border:
  if 'O': flood('S')
for all:
  if 'O': 'X'
  if 'S': 'O'
```

🕐 **45–60 sec:**
Mention complexity confidently:

> Time = O(n·m), Space = O(n·m), because we visit each cell once.

---

### 🔑 Quick analogies to remember it

Think of **filling water** from the edges:

* Water leaks in through the borders → mark them safe (S).
* Dry up everything else (flip O → X).
* Then replace safe areas back (S → O).

💧 **Edges leak → seal center.**

---

✅ **If you can recall:**

> **“Flood-fill from border O’s → Mark safe → Flip rest → Restore,”**
> you can rebuild this algorithm in under a minute in **any language**.