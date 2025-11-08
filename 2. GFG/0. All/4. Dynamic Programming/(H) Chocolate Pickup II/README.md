
---

# 🍫 Chocolate Pickup II

### Difficulty: Hard

**Accuracy:** 69.84%
**Submissions:** 372+
**Points:** 8

---

## 🧠 Problem Statement

You are given a square matrix **mat[][]** of size **n × n**, where each cell represents either a **blocked cell** or a cell **containing some chocolates**.

* If `mat[i][j] = -1`, then the cell is **blocked** and **cannot** be visited.
* Otherwise, `mat[i][j]` represents the **number of chocolates** present in that cell.

Your task is to determine the **maximum number of chocolates** a robot can collect by starting from the **top-left cell (0,0)**, moving to the **bottom-right cell (n-1, n-1)**, and then returning back to **(0,0)**.

---

### Rules:

* While moving **from (0,0) to (n-1,n-1)**, the robot can move **only right (i, j+1)** or **down (i+1, j)**.
* On the return journey **from (n-1,n-1) to (0,0)**, the robot can move **only left (i, j-1)** or **up (i-1, j)**.

After collecting chocolates from a cell `(i, j)`, that cell becomes **empty** (`mat[i][j] = 0`) for the next visit.

If **either** the forward path `(0,0) → (n-1,n-1)` or the return path `(n-1,n-1) → (0,0)` is **impossible** (blocked or unreachable), the answer must be **0**.

---

### Note:

* After visiting a cell `(i, j)`, it becomes empty for the second trip.
* If there is **no valid path** for either the forward or the return journey, return **0**.

---

## 🧩 Examples

### Example 1

**Input:**

```
mat = [
  [0, 1, -1],
  [1, 1, -1],
  [1, 1,  2]
]
```

**Output:**

```
7
```

**Explanation:**
One optimal route is:

* Forward: `(0,0) → (1,0) → (2,0) → (2,1) → (2,2)`
* Return: `(2,2) → (2,1) → (1,1) → (0,1) → (0,0)`

Total chocolates collected = **7**.

---

### Example 2

**Input:**

```
mat = [
  [1, 1, 0],
  [1, 1, 1],
  [0, 1, 1]
]
```

**Output:**

```
7
```

**Explanation:**
Optimal route:

* Forward: `(0,0) → (1,0) → (2,0) → (2,1) → (2,2)`
* Return: `(2,2) → (1,2) → (1,1) → (0,1) → (0,0)`

Total chocolates = **7**.

---

### Example 3

**Input:**

```
mat = [
  [1,  0, -1],
  [2, -1, -1],
  [1, -1,  3]
]
```

**Output:**

```
0
```

**Explanation:**
It is **impossible** to reach `(2,2)` from `(0,0)` since all paths are blocked.
Hence, result = **0**.

---

## ⚙️ Constraints

* ( 1 \leq n \leq 50 )
* ( -1 \leq mat[i][j] \leq 100 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** ( O(n^3) )
* **Auxiliary Space:** ( O(n^3) )

---

## 🏷️ Topic Tags

* Dynamic Programming
* Recursion

---

## 📚 Related Articles

* [**Maximizing Chocolates in Grid with Restricted Moves**](https://www.geeksforgeeks.org/maximizing-chocolates-in-grid-with-restricted-moves/)

---

---

awesome—let’s crack **Chocolate Pickup II** (aka “Cherry Pickup”) the interview-way.

# 2) Explanation + step-by-step dry run

## Problem recap

* Grid `mat[n][n]` (blocked cells are `-1`, others are chocolates ≥0).
* Go **(0,0) → (n-1,n-1)** using only **Right/Down**, then come back to **(0,0)** using only **Left/Up**.
* A cell gives chocolates once; on second visit it is `0`. If either leg is impossible, answer is `0`.

## Key trick (classic reduction)

Doing two trips sequentially is the same as letting **two walkers** start at `(0,0)` and move **simultaneously** to `(n-1,n-1)`, each step moving Right or Down.
At “time” (step) `t`, both walkers have taken `t` moves, so:

```
r1 + c1 = t
r2 + c2 = t  ⇒ r2 = t - c2
```

If both stand on the **same cell**, count its chocolates **once**.

We want to **maximize** collected chocolates subject to:

* No one steps on a blocked cell `-1`.
* Both stay inside the grid.

### DP state (top-down view)

Let `dp(r1, c1, c2)` = max chocolates when:

* Walker1 at `(r1, c1)`
* Walker2 at `(r2, c2)` with `r2 = r1 + c1 - c2` (same step)

Transitions (4 combinations for next move):

```
(r1+1,c1) with (r2+1,c2)   # down, down
(r1+1,c1) with (r2,  c2+1) # down, right
(r1,  c1+1) with (r2+1,c2) # right, down
(r1,  c1+1) with (r2,  c2+1)# right, right
```

Cell gain at current step:

```
gain = mat[r1][c1] + (mat[r2][c2] if (r1,c1)!=(r2,c2) else 0)
```

Base: when both reach `(n-1,n-1)`, return `mat[n-1][n-1]`.

If any index goes out or a cell is `-1`, return `-∞` (invalid), so maximization ignores it.
Final answer is `max(0, dp(0,0,0))` (if impossible, dp is `-∞` → 0).

### Tiny dry run (from prompt’s first example)

```
mat =
[ [0, 1, -1],
  [1, 1, -1],
  [1, 1,  2] ]
n=3

Start t=0: (0,0) & (0,0) → gain 0 (count once).
A best route is:
  W1: (0,0)->(1,0)->(2,0)->(2,1)->(2,2)
  W2: (0,0)->(0,1)->(1,1)->(2,1)->(2,2)
Cells collected once overall: 0 + 1 + 1 + 1 + 1 + 2 = 7
dp computes exactly this maximum.
```

---

# 3) Python solutions (brute → memo → tabulation)

All match:

```python
class Solution: 
    def chocolatePickup(self, mat): 
        # code here
```

### A) Brute recursion (two walkers, **no memo**) — exponential (teaching aid)

```python
class Solution:
    def chocolatePickup(self, mat):
        n = len(mat)

        def go(r1, c1, c2):
            r2 = r1 + c1 - c2
            # bounds or blocked
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n: return float('-inf')
            if mat[r1][c1] == -1 or mat[r2][c2] == -1:   return float('-inf')

            # destination
            if r1 == c1 == r2 == c2 == n-1:
                return mat[n-1][n-1]

            gain = mat[r1][c1]
            if (r1, c1) != (r2, c2):
                gain += mat[r2][c2]

            # 4 move pairs
            best_next = max(
                go(r1+1, c1,   c2  ),  # down,down
                go(r1+1, c1,   c2+1),  # down,right
                go(r1,   c1+1, c2  ),  # right,down
                go(r1,   c1+1, c2+1)   # right,right
            )
            return gain + best_next

        ans = go(0, 0, 0)
        return max(0, ans)  # if impossible -> 0
```

> Use this only to explain the recurrence; it’s exponential.

---

### B) Top-down DP (memoized) — **O(n³)** time & space (most common in interviews)

```python
class Solution:
    def chocolatePickup(self, mat):
        """
        Two-walker DP (cherry-pick style)
        Time:  O(n^3) states  (r1 in [0..n-1], c1 in [0..n-1], c2 in [0..n-1])
        Space: O(n^3) memo + O(n) recursion stack
        """
        from functools import lru_cache
        n = len(mat)

        @lru_cache(maxsize=None)
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2  # ensure same step for walker2

            # invalid states
            if r1 < 0 or c1 < 0 or c2 < 0 or r2 < 0: return float('-inf')
            if r1 >= n or c1 >= n or c2 >= n or r2 >= n: return float('-inf')
            if mat[r1][c1] == -1 or mat[r2][c2] == -1:   return float('-inf')

            # destination
            if r1 == c1 == r2 == c2 == n - 1:
                return mat[n - 1][n - 1]

            gain = mat[r1][c1]
            if (r1, c1) != (r2, c2):
                gain += mat[r2][c2]

            # explore 4 combinations (R/D for each walker)
            best_next = max(
                dp(r1 + 1, c1,     c2    ),  # D, D
                dp(r1 + 1, c1,     c2 + 1),  # D, R
                dp(r1,     c1 + 1, c2    ),  # R, D
                dp(r1,     c1 + 1, c2 + 1)   # R, R
            )
            return gain + best_next

        ans = dp(0, 0, 0)
        return 0 if ans == float('-inf') else ans
```

---

### C) Bottom-up tabulation (by “step t”) — **O(n³)** time, **O(n²)** space

We compress by iterating `t = 0..2n-2` and keeping a 2D DP over `(c1, c2)`; rows are derived as `r1=t-c1`, `r2=t-c2`.

```python
class Solution:
    def chocolatePickup(self, mat):
        """
        Bottom-up by steps t = r+c.
        dp[c1][c2] = best when walker1 at (r1=t-c1,c1) and walker2 at (r2=t-c2,c2).
        Time:  O(n^3)   Space: O(n^2)
        """
        n = len(mat)
        NEG = float('-inf')

        # initialize for t=0 at (0,0),(0,0)
        dp = [[NEG]*n for _ in range(n)]
        dp[0][0] = mat[0][0] if mat[0][0] != -1 else NEG

        for t in range(1, 2*n - 1):           # total steps to reach (n-1,n-1) is 2n-2
            new = [[NEG]*n for _ in range(n)]
            for c1 in range(max(0, t-(n-1)), min(n-1, t)+1):
                r1 = t - c1
                if r1 < 0 or r1 >= n: continue
                for c2 in range(max(0, t-(n-1)), min(n-1, t)+1):
                    r2 = t - c2
                    if r2 < 0 or r2 >= n: continue

                    if mat[r1][c1] == -1 or mat[r2][c2] == -1:
                        continue

                    gain = mat[r1][c1]
                    if (r1, c1) != (r2, c2):
                        gain += mat[r2][c2]

                    # transitions from previous step (t-1)
                    best_prev = max(
                        dp[c1][c2],                  # (r1-1,c1) & (r2-1,c2)  => D,D
                        dp[c1][c2-1] if c2-1 >= 0 else NEG,  # D,R
                        dp[c1-1][c2] if c1-1 >= 0 else NEG,  # R,D
                        dp[c1-1][c2-1] if c1-1 >= 0 and c2-1 >= 0 else NEG  # R,R
                    )
                    if best_prev != NEG:
                        new[c1][c2] = best_prev + gain
            dp = new

        ans = dp[n-1][n-1]
        return 0 if ans == NEG else ans
```

> Either B (memo) or C (tab) is “the” expected solution. B is usually quicker to code; C shows strong DP chops.

---

# 4) Interview quick-recall + Q&A

## 5-line pseudo (memorize this)

```
dp(r1,c1,c2):
  r2 = r1 + c1 - c2
  if out/blocked: -∞
  if all at end: return cell(n-1,n-1)
  gain = a[r1][c1] + (a[r2][c2] if (r1,c1)!=(r2,c2) else 0)
  return gain + max( 4 recursive moves )
answer = max(0, dp(0,0,0))
```

**Mnemonic:** **“Two Walkers, Same Step.”**
Say out loud: *“I’ll run two walkers from (0,0) to (n-1,n-1) at the same time; step t fixes r+c, avoid double count when they meet.”*

## Likely interviewer questions (with crisp answers)

**Q1. Why two walkers instead of forward+backward?**
Because cells get emptied after first visit; two synchronized walkers model both trips at once and avoid re-counting. It’s the standard reduction for “cherry pickup” style problems.

**Q2. What’s the DP state and why `O(n³)`?**
State `(r1,c1,c2)` uniquely determines both positions (`r2=t-c2`). Each index is `O(n)`, so states are `O(n³)`; each does `O(1)` work over 4 transitions → `O(n³)` time.

**Q3. How do you handle blocked cells and impossible paths?**
Return `-∞` from invalid states; final `max(0, ans)` converts “no valid route” to `0`.

**Q4. Why count a cell once when both walkers are on it?**
Because the cell is emptied after collection; visiting simultaneously represents that it would be collected once across the two trips.

**Q5. Can you cut space?**
Yes. Bottom-up by “step `t`” keeps only a 2D `n×n` table for `(c1,c2)` → **`O(n²)` space**.

**Q6. Edge cases?**
Start or end blocked ⇒ immediate `0`. Rows/cols with walls might isolate zones—`-∞` propagation ensures we return `0`.

---

### Quick pick in an interview

* **Short on time:** write **Top-Down memo** (Solution B).
* **Want to impress:** mention the **step-compressed tabulation** (Solution C) and its `O(n²)` space.

You’re set: present the “two walkers, same step” story, code the memo in ~25 lines, and you look sharp.

---

---

awesome — here are the last two pieces for **Chocolate Pickup II** (a.k.a. Cherry Pickup).

# 5) Real-World Use Cases (quick, relatable)

* **Two-way delivery/return with perishables:** A courier must go from warehouse → client and then return to base, passing through a city grid with road closures (`-1`). Each block has items/credits to collect once; maximize total value across the pair of trips.
* **Autonomous cleaning robot (out-and-back):** Robot travels to a far corner and back; each dust patch can be vacuumed once. Obstacles are blocked cells. Plan both legs to maximize cleaned dust.
* **Data collection drone (download + upload run):** Drone flies to a station to drop data and comes back; each waypoint yields data only once (after first pass it’s empty). No-fly zones are blocked.

All map to the **two-walkers, same-step DP**: simulate going and returning simultaneously, avoid double counting when both visit the same cell.

---

# 6) Full Program (with inline time/space notes + timing)

* Implementation: **Top-Down DP with memoization** (clear, interview-standard).
* Complexity: **O(n³)** time / **O(n³)** memo (or **O(n²)** if you switch to step-tabulation).
* Includes two sample inputs from the prompt and end-to-end timing using `timeit`.

```python
"""
Chocolate Pickup II (a.k.a. Cherry Pickup) — Full Program
---------------------------------------------------------
We must go from (0,0) -> (n-1,n-1) and back, maximizing total chocolates.
Blocked cells have -1. A cell's chocolates are collected at most once.

Key reduction:
Run TWO walkers from (0,0) to (n-1,n-1) *simultaneously*, each moving R/D.
At "step" t, both have taken t moves, so r1+c1 = r2+c2 = t.
If both are on the same cell, count that cell once.

DP state (top-down memo):
    dp(r1, c1, c2)  -> max chocolates when walker1 is at (r1,c1),
                        walker2 at (r2, c2) where r2 = r1 + c1 - c2.
Transitions (4 combos): (D,D), (D,R), (R,D), (R,R).
Invalid states (out of bounds / blocked): return -inf so they are never chosen.

Complexities:
- Number of states: r1 in [0..n-1], c1 in [0..n-1], c2 in [0..n-1] => O(n^3)
- Each state computes max over 4 transitions => O(1) per state
- Time:  O(n^3)
- Space: O(n^3) memo + O(n) recursion stack

We also include an optional bottom-up (step-compressed) version you can flip to.
"""

from functools import lru_cache
import timeit

class Solution:
    # ---------- Version A: Top-Down Memoized (recommended) ----------
    def chocolatePickup(self, mat):
        """
        Args:
            mat: List[List[int]] — n x n grid; -1 => blocked, else chocolates >= 0
        Returns:
            int — maximum chocolates collectable over forward+return, or 0 if impossible.

        Step-by-step complexity notes:
            - Index math & bounds checks: O(1)
            - Memo lookup/storing per state: O(1) average
            - 4 recursive transitions: O(1) each, total O(1) per state
            - Total states: O(n^3)  -> Time O(n^3), Space O(n^3)
        """
        n = len(mat)
        NEG_INF = float('-inf')

        # Memoize by (r1, c1, c2); r2 is derived to keep states to O(n^3)
        @lru_cache(maxsize=None)
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2  # same step t => r2 computed from r1,c1,c2

            # --- Invalid state checks (O(1)) ---
            if r1 < 0 or c1 < 0 or c2 < 0 or r2 < 0: 
                return NEG_INF
            if r1 >= n or c1 >= n or c2 >= n or r2 >= n:
                return NEG_INF
            if mat[r1][c1] == -1 or mat[r2][c2] == -1:
                return NEG_INF

            # --- Destination: both at (n-1, n-1) (O(1)) ---
            if r1 == c1 == r2 == c2 == n - 1:
                return mat[n - 1][n - 1]

            # --- Collect chocolates from current cells (count once if same) (O(1)) ---
            gain = mat[r1][c1]
            if (r1, c1) != (r2, c2):
                gain += mat[r2][c2]

            # --- Explore 4 move combinations (O(1)) ---
            best_next = max(
                dp(r1 + 1, c1,     c2    ),  # Down, Down
                dp(r1 + 1, c1,     c2 + 1),  # Down, Right
                dp(r1,     c1 + 1, c2    ),  # Right, Down
                dp(r1,     c1 + 1, c2 + 1)   # Right, Right
            )
            return gain + best_next

        res = dp(0, 0, 0)
        return 0 if res == NEG_INF else res

    # ---------- Version B: Bottom-Up Step-Compressed (optional) ----------
    def chocolatePickup_bottomup(self, mat):
        """
        Compress by step t = r+c; keep a 2D dp over (c1, c2).
        Time:  O(n^3), Space: O(n^2)
        """
        n = len(mat)
        NEG = float('-inf')

        # t=0 base: both at (0,0)
        dp = [[NEG] * n for _ in range(n)]
        dp[0][0] = -NEG if mat[0][0] == -1 else mat[0][0]
        if mat[0][0] == -1:
            return 0  # start blocked → impossible

        for t in range(1, 2 * n - 1):  # steps to reach bottom-right = 2n-2
            new = [[NEG] * n for _ in range(n)]
            # c1 and c2 loops restricted so r1=t-c1 and r2=t-c2 are in [0,n-1]
            cmin = max(0, t - (n - 1))
            cmax = min(n - 1, t)
            for c1 in range(cmin, cmax + 1):
                r1 = t - c1
                if mat[r1][c1] == -1:
                    continue
                for c2 in range(cmin, cmax + 1):
                    r2 = t - c2
                    if mat[r2][c2] == -1:
                        continue
                    gain = mat[r1][c1] + (mat[r2][c2] if (r1, c1) != (r2, c2) else 0)

                    # Transitions from previous step (t-1):
                    best_prev = max(
                        dp[c1][c2],                           # D,D
                        dp[c1][c2 - 1] if c2 - 1 >= 0 else NEG,  # D,R
                        dp[c1 - 1][c2] if c1 - 1 >= 0 else NEG,  # R,D
                        dp[c1 - 1][c2 - 1] if (c1 - 1 >= 0 and c2 - 1 >= 0) else NEG
                    )
                    if best_prev != NEG:
                        new[c1][c2] = best_prev + gain
            dp = new

        ans = dp[n - 1][n - 1]
        return 0 if ans == NEG else ans


# ------------------------------ Demo + Timing ------------------------------
if __name__ == "__main__":
    # Example matrices from the prompt
    mat1 = [
        [0, 1, -1],
        [1, 1, -1],
        [1, 1,  2],
    ]
    mat2 = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1],
    ]
    mat3 = [
        [1,  0, -1],
        [2, -1, -1],
        [1, -1,  3],
    ]

    sol = Solution()

    # Time each call exactly once with timeit (includes all DP work)
    t1 = timeit.timeit(lambda: sol.chocolatePickup(mat1), number=1)
    r1 = sol.chocolatePickup(mat1)

    t2 = timeit.timeit(lambda: sol.chocolatePickup(mat2), number=1)
    r2 = sol.chocolatePickup(mat2)

    t3 = timeit.timeit(lambda: sol.chocolatePickup(mat3), number=1)
    r3 = sol.chocolatePickup(mat3)

    print("Top-Down Memoized DP (O(n^3) time, O(n^3) space)")
    print(f"Input 1: {mat1}\nOutput 1: {r1}\nRun Time 1: {t1:.8f} s\n")
    print(f"Input 2: {mat2}\nOutput 2: {r2}\nRun Time 2: {t2:.8f} s\n")
    print(f"Input 3: {mat3}\nOutput 3: {r3}\nRun Time 3: {t3:.8f} s\n")

    # Optional: also show the bottom-up version timing for comparison
    tb1 = timeit.timeit(lambda: sol.chocolatePickup_bottomup(mat1), number=1)
    ab1 = sol.chocolatePickup_bottomup(mat1)
    print("Bottom-Up Step-Compressed DP (O(n^3) time, O(n^2) space)")
    print(f"Input 1: {mat1}\nOutput 1 (BU): {ab1}\nRun Time 1 (BU): {tb1:.8f} s")
```

### Sample output (what you should see)

```
Top-Down Memoized DP (O(n^3) time, O(n^3) space)
Input 1: [[0, 1, -1], [1, 1, -1], [1, 1, 2]]
Output 1: 7
Run Time 1: 0.0000xx s

Input 2: [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
Output 2: 7
Run Time 2: 0.0000xx s

Input 3: [[1, 0, -1], [2, -1, -1], [1, -1, 3]]
Output 3: 0
Run Time 3: 0.0000xx s

Bottom-Up Step-Compressed DP (O(n^3) time, O(n^2) space)
Input 1: [[0, 1, -1], [1, 1, -1], [1, 1, 2]]
Output 1 (BU): 7
Run Time 1 (BU): 0.0000xx s
```

**Why this is interview-ready**

* You explain the **two-walker reduction**, define the **state**, and show the **4 transitions**.
* You deliver both a concise **memoized** solution and a memory-lean **tabulation** variant.
* You annotate **time/space** right where it matters and show **timed runs** end-to-end.
