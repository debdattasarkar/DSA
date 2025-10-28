Perfect — this problem (Distance of Nearest Cell Having 1) is a **must-memorize BFS pattern** for interviews.
Here’s the exact **“5-line pseudo-code template”** + **mnemonic recall flow** that will make it stick permanently.

---

## 🧠 5-Line Pseudo-code Template (Multi-source BFS)

```
Initialize queue with all 1-cells (dist = 0)
While queue not empty:
    Pop cell (r, c)
    For each of 4 directions (up/down/left/right):
        If neighbor is valid and dist > dist[r][c] + 1:
            Update dist and push neighbor
Return dist
```

---

## 🔑 Mnemonic: **"Seed → Pop → Check → Push → Repeat"**

Or think of it as:

> **“SPCPR — The BFS heartbeat”**

| Step           | Meaning                        | Explanation                          |
| -------------- | ------------------------------ | ------------------------------------ |
| **S (Seed)**   | Initialize queue with all 1s   | All `1` cells start with distance 0  |
| **P (Pop)**    | Pop from queue                 | Take the current frontier cell       |
| **C (Check)**  | Check 4 neighbors              | Up, down, left, right                |
| **P (Push)**   | Push valid unvisited neighbors | Only if you found a smaller distance |
| **R (Repeat)** | Repeat until queue empty       | BFS wave expands until all covered   |

---

## ⏱️ 60-Second Recall Flow Before an Interview

### 0–10s → Recognize the pattern

> "This is a **multi-source shortest distance on grid** — BFS problem."

### 10–20s → Write the core structure

> Queue seeded with all 1s at distance 0.

### 20–40s → Write the BFS loop

```
while q:
    r, c = q.popleft()
    for dr, dc in DIRS:
        nr, nc = r+dr, c+dc
        if valid and dist[nr][nc] > dist[r][c] + 1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
```

### 40–50s → Mention complexity

> Each cell is visited once → **O(n*m)** time, **O(n*m)** space.

### 50–60s → Say the intuition out loud

> “All 1s act as sources; BFS spreads in waves; the first visit gives the nearest 1.”

---

## ⚡ Quick Visualization (Mental Picture)

Think of **dropping pebbles (1s)** into a **pond (0s)** —
each wave (BFS layer) expands one step per time unit,
and every 0 gets hit by the *nearest* pebble first. 💧🌊

---

## 🧩 Universal Skeleton (language-agnostic)

```
function nearestOneDistance(grid):
    q = all cells with value 1
    dist = same-size matrix, INF everywhere, 0 for 1s
    while q not empty:
        (r, c) = q.pop()
        for each (dr, dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
            if inBounds(r+dr,c+dc) and dist[r+dr][c+dc] > dist[r][c]+1:
                dist[r+dr][c+dc] = dist[r][c]+1
                q.push((r+dr,c+dc))
    return dist
```

---

✅ **Quick mental trigger:**

> “All 1s in queue → BFS in 4 dirs → Fill distances → O(n*m) done.”

Memorize **SPCPR** (Seed → Pop → Check → Push → Repeat).
It’s the same structure you’ll reuse for:

* Rotten Oranges 🍊
* Walls and Gates 🏰
* Nearest Exit in Maze 🚪
* Flood Fill 🌊
* Word Ladder (on grid variants) 🔠

---

