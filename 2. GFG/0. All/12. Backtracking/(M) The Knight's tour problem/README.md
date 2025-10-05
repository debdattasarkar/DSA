
---

# 🏇 The Knight’s Tour Problem

### Difficulty: Medium

**Accuracy:** 66.34%
**Submissions:** 639k+
**Points:** 4

---

## 🧩 Problem Statement

You are given an **n × n chessboard** with a **Knight** starting at the top-left corner **(0, 0)**.
Your task is to determine a **valid Knight's Tour**, where the Knight visits **every square exactly once**, following the standard movement rules of a chess Knight.

You have to return the **order in which each cell is visited**.
If a solution exists, print the sequence of numbers representing the order of visited squares.
If no solution is possible, **return -1**.

> **Note:**
> You can return any valid ordering. If it is correct, the driver code will print `true`, else it will print `false`.

---

## 🧠 Examples

### Example 1

**Input:**

```
n = 5
```

**Output:**

```
true
```

**Explanation:**
A possible Knight's Tour in a 5×5 chessboard is given below where each number represents the step at which the Knight visits that cell, starting from (0, 0) as step 0.

```
[[0, 11,  2, 17, 20],
 [3, 16, 19, 12,  7],
 [10,  1,  6, 21, 18],
 [15,  4, 23,  8, 13],
 [24,  9, 14,  5, 22]]
```

---

### Example 2

**Input:**

```
n = 4
```

**Output:**

```
true
```

**Explanation:**
For n = 4, it is **not possible** for a valid Knight's Tour,
so you have to **return -1**.

---

## ⚙️ Constraints

```
1 ≤ n ≤ 6
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(8^(n * n))
* **Auxiliary Space:** O(n²)

---

## 🏷️ Topic Tags

* Recursion
* Backtracking
* Puzzles

---

## 📚 Related Articles

* [The Knight’s Tour Problem](https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/)

---

---

awesome — here’s everything based on the **latest working solution** (that returns `[[-1]]` when impossible, to satisfy the driver).

---

## 2) Intuition + Step-by-Step Dry Run

### Goal

* On an `n × n` chessboard, start at `(0,0)`.
* Visit **every square exactly once** using knight moves.
* Return the **visit-order matrix** (`0 … n²−1`) if a tour exists; otherwise return **`[[-1]]`** (because the driver checks exactly for a 1×1 `[-1]` matrix).

### Facts to remember (used for fast exits)

* Tour **exists** for `n = 1` and **all `n ≥ 5`**.
* **No tour** for `n ∈ {2,3,4}`.
* We’ll still keep a backtracking search for safety and to produce an actual tour.

### Core idea

* This is a Hamiltonian path problem on the “knight-move graph”.
* Use **backtracking**: place step `k` on a square, try legal next moves for step `k+1`, backtrack on dead ends.
* Speed it up with **Warnsdorff’s heuristic**: from the current square, try next squares in the order of **fewest onward legal moves** first (i.e., least-constraining).

### Dry run (first moves, `n = 5`)

We’ll sketch the **Warnsdorff** ordering from `(0,0)`.

1. **Step 0** at `(0,0)` → mark board[0][0] = 0.
   Legal moves: `(2,1)` and `(1,2)`.
   Compute **onward degree** for both (how many unvisited legal moves from there). Suppose they tie; we pick lexicographically `(1,2)` first.

2. **Step 1** at `(1,2)`.
   Generate its legal unvisited neighbors and sort them by onward degree: e.g., candidates might be `(3,3)`, `(3,1)`, `(2,4)`, `(0,4)`, `(2,0)`, `(0,0-visited)`.
   Choose the one with the **fewest onward options**, say `(3,3)`.

3. **Step 2** at `(3,3)`.
   Again, generate & sort next moves by onward degree, take the smallest.

… Continue.

* If at some point **no candidates** and we’ve **not** filled all `25` cells → **backtrack** to previous step and try the next candidate.
* For `n = 5` this typically fills all cells quickly.
* For `n = 2/3/4`, we never even search — we immediately return `[[-1]]`.

---

## 3) Python Solutions (interview-ready)

Both use your required signature:

```python
class Solution:
    def knightTour(self, n):
        # code here
```

### A) Backtracking + **Warnsdorff’s heuristic** (recommended / fast)

```python
class Solution:
    def knightTour(self, n):
        """
        Returns:
          - n x n matrix with visit order (0..n^2-1) if a tour exists,
          - [[-1]] if no tour exists (this is what the driver expects on failure).

        Notes:
          • Classic results: tour exists for n=1 and all n>=5; none for n in {2,3,4}.
          • We still run a backtracking search (with Warnsdorff) to construct a concrete tour.
          • Time (worst-case): exponential; typically very fast for n in this problem.
          • Space: O(n^2) for the board and recursion depth.
        """
        # Early outs to match the judge’s driver (return a 1x1 [-1] matrix, not int -1)
        if n in (2, 3, 4):
            return [[-1]]
        if n == 1:
            return [[0]]

        # 8 possible knight moves
        MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2), (1, -2), (2, -1)]

        # Board initialization: -1 means unvisited
        board = [[-1] * n for _ in range(n)]
        board[0][0] = 0  # start at (0,0) with step 0

        def inside(x, y):
            return 0 <= x < n and 0 <= y < n

        def onward_degree(x, y):
            """Count how many unvisited legal moves exist from (x,y). O(1) * 8."""
            cnt = 0
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    cnt += 1
            return cnt

        def next_moves(x, y):
            """
            Warnsdorff ordering:
              generate candidate (nx,ny) and sort by their onward degree ascending
            Deterministic tiebreak with (deg, nx, ny) so results are stable.
            """
            cand = []
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    cand.append((onward_degree(nx, ny), nx, ny))
            cand.sort()
            for _, nx, ny in cand:
                yield nx, ny

        def dfs(step, x, y):
            # Base: all cells placed
            if step == n * n - 1:
                return True
            # Try next squares in least-constraining order
            for nx, ny in next_moves(x, y):
                board[nx][ny] = step + 1
                if dfs(step + 1, nx, ny):
                    return True
                board[nx][ny] = -1  # backtrack
            return False

        # If (unexpectedly) search fails, return [[-1]] to satisfy driver
        return board if dfs(0, 0, 0) else [[-1]]
```

### B) **Plain backtracking** (no heuristic) — simple but slower

> Useful to show you know the baseline; fine for very small `n`. Still returns `[[-1]]` on failure.

```python
class Solution:
    def knightTour(self, n):
        """
        Pure backtracking (try all legal moves in fixed order).
        Time  : Exponential in worst-case (upper bound ~ 8^(n^2))
        Space : O(n^2)
        """
        if n in (2, 3, 4):
            return [[-1]]
        if n == 1:
            return [[0]]

        MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2), (1, -2), (2, -1)]

        board = [[-1] * n for _ in range(n)]
        board[0][0] = 0

        def inside(x, y):
            return 0 <= x < n and 0 <= y < n

        def dfs(step, x, y):
            if step == n * n - 1:
                return True
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    board[nx][ny] = step + 1
                    if dfs(step + 1, nx, ny):
                        return True
                    board[nx][ny] = -1  # backtrack
            return False

        return board if dfs(0, 0, 0) else [[-1]]
```

> In interviews, mention you’d **prefer Warnsdorff** because it prunes dramatically by visiting tight squares early.

---

## 4) Interview Q&A (high-yield)

**Q1. Why do we return `[[-1]]` instead of `-1`?**
Because some drivers (like the one you’re using) **check specifically** for a **1×1 matrix `[-1]`** to mark “no solution”. Returning int `-1` would cause their post-processing to crash (`len(-1)`).

**Q2. When is a Knight’s Tour possible?**
Classic result: **possible** for `n = 1` and **all `n ≥ 5`**; **not possible** for `n ∈ {2,3,4}`. (We still keep search for safety and to construct the actual tour.)

**Q3. What is Warnsdorff’s heuristic and why does it help?**
At each step, choose the next square with the **fewest onward legal moves**. This **reduces branching** and leads to a solution quickly in practice.

**Q4. Complexity?**

* **Backtracking** worst-case is exponential (`~ 8^(n²)` upper bound).
* With **Warnsdorff**, it’s still exponential in theory, but **very fast in practice** for small `n`.
* **Space** is `O(n²)` for the board (and recursion depth up to `n²`).

**Q5. How do you verify a returned tour?**

* Matrix contains exactly the integers **0 to n²−1** once each.
* For each `k` from 0 to n²−2, the cell of `k` is a **legal knight move** away from the cell of `k+1`.

**Q6. Can we start from a different square?**
Yes. The search works from any start, just set the initial `(x0,y0)` and `board[x0][y0] = 0`.

**Q7. Any further optimizations?**

* Precompute legal moves per cell to avoid recomputation.
* Tie-break Warnsdorff by preferring moves toward the board center (empirical).
* In systems languages, bitboards can speed things up drastically.

---

---

perfect — here’s a **runnable, interview-style full program** that:

* implements the exact signature `class Solution: def knightTour(self, n): ...`
  (returns an `n×n` visit-order matrix or **`[[-1]]`** when impossible — driver-safe)
* also includes a plain backtracking variant for comparison
* prints **inputs & outputs** for a few values of `n`
* measures runtime with **`timeit`** and reports **average seconds/run**
* has **inline comments** calling out **time & space complexity** at each step

---

## 5) Full Python program (with inline complexity notes + timings)

```python
"""
Knight's Tour — Backtracking with Warnsdorff (driver-safe)
---------------------------------------------------------
We provide:
  • class Solution.knightTour(n)  -> main solution (Warnsdorff + backtracking)
      - returns n×n visit-order matrix if a tour exists
      - returns [[-1]] if impossible (this shape avoids driver crashes)
  • class SolutionPlain.knightTour(n) -> plain backtracking (no heuristic), for timing contrast

Complexities
------------
Let N = n*n (cells).
• Backtracking (theoretical upper bound): exponential (≈ 8^N worst case).
• Warnsdorff heuristic: still exponential worst-case, but typically very fast for n ≤ 6.
• Space: O(N) for the board + O(N) recursion depth (each step places one number).

Notes
-----
• Classic results: Knight's tour exists for n = 1 and all n ≥ 5; no tour for n ∈ {2,3,4}.
• We still keep search to actually construct a tour matrix for valid sizes.
"""

from typing import List
import timeit


# =============================== Main (Warnsdorff) solution =============================== #
class Solution:
    def knightTour(self, n: int):
        """
        Returns:
          - n x n matrix of visit order [0..n^2-1] if a tour exists,
          - [[-1]] if no tour exists (driver-safe: some drivers check for a 1x1 [-1]).

        Time  : Exponential worst-case; in practice fast for small n with Warnsdorff.
        Space : O(n^2) for the board and recursion stack.
        """
        # ---- Early exits (O(1)) ----
        # The driver expects [[-1]] on impossibility; do NOT return int -1.
        if n in (2, 3, 4):
            return [[-1]]
        if n == 1:
            return [[0]]

        # ---- Preliminaries ----
        # Knight move deltas — constant size, O(1)
        MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2), (1, -2), (2, -1)]

        # Board O(n^2) space; -1 means unvisited
        board = [[-1] * n for _ in range(n)]
        board[0][0] = 0  # step 0 at (0,0) — O(1)

        def inside(x: int, y: int) -> bool:
            # O(1)
            return 0 <= x < n and 0 <= y < n

        def onward_degree(x: int, y: int) -> int:
            """
            Count how many unvisited legal moves exist from (x, y).
            Each check is O(1); we do up to 8 checks -> O(1) overall.
            """
            cnt = 0
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    cnt += 1
            return cnt

        def next_moves(x: int, y: int):
            """
            Warnsdorff ordering: generate candidate next squares sorted by their
            onward degree (fewest first). Sorting at most 8 items -> O(1).
            """
            cand = []
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    cand.append((onward_degree(nx, ny), nx, ny))
            cand.sort()  # O(1) since len<=8
            for _, nx, ny in cand:
                yield nx, ny

        def dfs(step: int, x: int, y: int) -> bool:
            """
            Backtracking with Warnsdorff ordering.
            Depth is at most n^2; branching greatly reduced by heuristic.
            """
            # Base: placed all steps 0..n^2-1  -> O(1)
            if step == n * n - 1:
                return True

            # Try the least-constraining candidates first  -> typical fast convergence
            for nx, ny in next_moves(x, y):
                board[nx][ny] = step + 1        # place next step  -> O(1)
                if dfs(step + 1, nx, ny):       # recurse
                    return True
                board[nx][ny] = -1              # backtrack       -> O(1)
            return False

        # Search — exponential worst-case (see header), typically fast here
        return board if dfs(0, 0, 0) else [[-1]]


# =============================== Plain backtracking (for contrast) =============================== #
class SolutionPlain:
    def knightTour(self, n: int):
        """
        Plain backtracking without Warnsdorff.
        Time  : Exponential worst-case (~8^(n^2) upper bound).
        Space : O(n^2).

        Returns n×n tour matrix or [[-1]] if impossible.
        """
        if n in (2, 3, 4):
            return [[-1]]
        if n == 1:
            return [[0]]

        MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2), (1, -2), (2, -1)]

        board = [[-1] * n for _ in range(n)]
        board[0][0] = 0

        def inside(x, y):
            return 0 <= x < n and 0 <= y < n

        def dfs(step, x, y):
            if step == n * n - 1:
                return True
            for dx, dy in MOVES:              # try all 8 in fixed order
                nx, ny = x + dx, y + dy
                if inside(nx, ny) and board[nx][ny] == -1:
                    board[nx][ny] = step + 1
                    if dfs(step + 1, nx, ny):
                        return True
                    board[nx][ny] = -1        # backtrack
            return False

        return board if dfs(0, 0, 0) else [[-1]]


# =============================== Small validator (optional) =============================== #
def is_valid_tour(board) -> bool:
    """
    Verify a board is a valid knight tour:
      • Must be a square list of lists with values 0..n^2-1 each exactly once.
      • Consecutive k,k+1 must be a knight move apart.
    O(n^2) time, O(n^2) space for reverse index map.
    """
    if not isinstance(board, list) or not board or not isinstance(board[0], list):
        return False
    n = len(board)
    for row in board:
        if len(row) != n:
            return False

    # Flatten and check range & uniqueness
    flat = [x for r in board for x in r]
    if sorted(flat) != list(range(n * n)):
        return False

    # Build position of each label k
    pos = [None] * (n * n)
    for i in range(n):
        for j in range(n):
            pos[board[i][j]] = (i, j)

    def is_knight(a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        return (dx, dy) in {(1, 2), (2, 1)}

    for k in range(n * n - 1):
        if not is_knight(pos[k], pos[k + 1]):
            return False
    return True


# =============================== Timing helper =============================== #
def bench(func, *args, number=10) -> float:
    """
    Return average seconds/run using timeit.
    For small n, Python overhead dominates; treat as relative measure.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# =============================== Demo / main =============================== #
if __name__ == "__main__":
    print("=== Knight's Tour — Warnsdorff vs Plain Backtracking ===\n")

    tests = [1, 2, 5, 6]   # include impossible & possible cases
    for n in tests:
        print(f">>> n = {n}")
        sol = Solution().knightTour(n)
        if sol == [[-1]]:
            print("Result: [[-1]]  (no tour — expected for n in {2,3,4})")
        else:
            # print the tour matrix (small n only to keep output compact)
            for row in sol:
                print(row)
            # Validate (optional)
            print("Valid tour?", is_valid_tour(sol))
        print()

    # -------- Timings (average seconds per run) --------
    print("=== Timings (average seconds per run) ===")
    for n in [5, 6]:
        runs = 10
        t_warn = bench(Solution().knightTour, n, number=runs)
        t_plain = bench(SolutionPlain().knightTour, n, number=max(1, runs // 5))  # plain is slower
        print(f"n={n}: Warnsdorff {t_warn:.6f}s/run | Plain {t_plain:.6f}s/run (fewer runs if too slow)")

    print("\nNotes:")
    print(" • For n ∈ {2,3,4}, the function instantly returns [[-1]] (driver-safe).")
    print(" • Warnsdorff greatly reduces backtracking vs plain, especially as n grows.")
    print(" • Space is O(n^2); worst-case time is exponential but practical here.")
```

### What you’ll see when you run it

* For `n=1`: prints `[[0]]`, “Valid tour? True”
* For `n=2`: prints `[[−1]]` (as required)
* For `n=5` and `n=6`: prints a full valid tour matrix and “Valid tour? True”
* Timing lines comparing **Warnsdorff** vs **Plain** backtracking

---

## 6) Real-World Use Cases (the very important ones)

1. **Path planning with hard constraints**
   The board can represent waypoints; knight moves encode feasible transitions. The tour models visiting all waypoints **exactly once** (e.g., inspection drones with limited maneuvering patterns).

2. **Hamiltonian path search in sparse geometric graphs**
   Knight’s tour is a canonical constrained Hamiltonian path problem; the techniques (heuristic ordering like Warnsdorff + backtracking) transfer to **PCB routing**, **maze generation**, and **graph puzzle solvers**.

3. **Testing & benchmarking backtracking/heuristics**
   Used widely in research/education to compare **ordering heuristics**, **pruning**, and **search strategies** in NP-complete contexts.
