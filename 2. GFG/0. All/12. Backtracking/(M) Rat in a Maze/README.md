
---

# 🐀 Rat in a Maze

**Difficulty:** Medium
**Accuracy:** 35.75%
**Submissions:** 377K+
**Points:** 4
**Average Time:** 25 minutes

---

## 🧩 Problem Description

Consider a rat placed at position **(0, 0)** in an **n × n** square matrix `maze[][]`.
The rat's goal is to reach the **destination at position (n−1, n−1)**.

The rat can move in **four possible directions**:

* `'U'` → Up
* `'D'` → Down
* `'L'` → Left
* `'R'` → Right

The matrix contains only **two possible values**:

* `0`: A blocked cell through which the rat **cannot travel**.
* `1`: A free cell through which the rat **can pass**.

---

## 🎯 Task

Find **all possible paths** the rat can take to reach the destination, starting from `(0, 0)` and ending at `(n−1, n−1)`.

* The rat **cannot revisit any cell** in the same path.
* The rat can **only move to adjacent cells** within bounds of the matrix and not blocked (`1` cells only).
* If **no path exists**, return an **empty list**.
* The result must be in **lexicographically smallest order**.

---

## 📘 Note

Return the final result vector in **lexicographically smallest order**.

---

## 🧠 Examples

### Example 1:

**Input:**

```python
maze = [
 [1, 0, 0, 0],
 [1, 1, 0, 1],
 [1, 1, 0, 0],
 [0, 1, 1, 1]
]
```

**Output:**

```
["DDRDRR", "DRDDRR"]
```

**Explanation:**
The rat can reach the destination `(3,3)` from `(0,0)` by two paths:

1️⃣ **DRDDRR**
2️⃣ **DDRDRR**

When printed in **sorted order**, we get:
→ `DDRDRR DRDDRR`

---

### Example 2:

**Input:**

```python
maze = [
 [1, 0],
 [1, 0]
]
```

**Output:**

```
[]
```

**Explanation:**
No path exists because the destination cell `(1,1)` is blocked.

---

### Example 3:

**Input:**

```python
maze = [
 [1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]
]
```

**Output:**

```
["DDRR", "RRDD"]
```

**Explanation:**
The rat has two possible paths to reach the destination:

* **DDRR**
* **RRDD**

---

## ⚙️ Constraints

```
2 ≤ n ≤ 5
0 ≤ maze[i][j] ≤ 1
```

---

## ⏱️ Expected Time and Space Complexity

* **Time Complexity:** O(4^(n × n))
  (Each cell can branch into 4 directions in the worst case)

* **Auxiliary Space:** O(n × n)
  (For recursion stack + visited matrix)

---

## 🏢 Company Tags

* Amazon
* Microsoft

---

## 🧩 Topic Tags

* Backtracking
* Algorithms

---

## 💼 Related Interview Experiences

* Makemytrip Interview Experience
* Paytm Interview Experience Set 16
* Makemytrip Interview Experience Set 13 On Campus For Full Time

---

## 📚 Related Articles

* [Compute The Minimum Or Maximum Of Two Integers Without Branching](https://www.geeksforgeeks.org/compute-the-minimum-or-maximum-max-of-two-integers-without-branching/)
* [Rat In A Maze Problem When Movement In All Possible Directions Is Allowed](https://www.geeksforgeeks.org/rat-in-a-maze-problem-when-movement-in-all-possible-directions-is-allowed/)

---

---

awesome — let’s lock this down for interviews: a crisp intuition + a hand-walked dry run, then two Python solutions in your requested signature (a **brute/clear DFS** and an **optimized backtracking** that emits results already in lexicographic order). I’ll end with sharp interviewer Q&A.

---

## 2) Intuition + Step-by-Step Dry Run

### Problem recap

* Grid `maze[n][n]` with `0` (blocked) / `1` (free).
* Start `(0,0)`, goal `(n-1,n-1)`.
* Moves allowed: **U**, **D**, **L**, **R** (no diagonals).
* **Can’t revisit** a cell in the same path.
* Return **all** paths as strings, **lexicographically** smallest order; return `[]` if no path.

### Why backtracking (DFS)?

We’re enumerating **all** simple paths in a tiny grid (n ≤ 5 per prompt), which screams **DFS + visited**. At each cell, recursively try the four directions, mark/unmark visited to enforce “no revisits”.

### Lexicographic order

Character order is `'D' < 'L' < 'R' < 'U'` (ASCII).
If we explore in this order, we’ll naturally generate lexicographically sorted paths and can **skip the final sort**. (If you forget, you can always `sort()` once at the end.)

### Dry run (Example 1)

```
maze =
1 0 0 0
1 1 0 1
1 1 0 0
0 1 1 1
n = 4, start=(0,0), goal=(3,3)
```

Explore in order D, L, R, U:

* Start (0,0) → mark visited.
* **D** to (1,0) → **D** to (2,0) → **R** blocked? (2,1)=1 so R ok:

  * path “DDR” at (2,1).
  * From (2,1):

    * **D** blocked (3,1)=1 actually OK → “DDRD”, at (3,1).
    * From (3,1): **R** → (3,2)=1 → “DDRDR”, then **R** → (3,3)=1 → **“DDRDRR”** record.
* Backtrack, explore alternative branches:

  * From (1,0), try **R** → (1,1)=1: path “DR”.

    * From (1,1): **D** → (2,1)=1 → “DRD”.

      * **D** → (3,1)=1 → “DRDD”.

        * **R** → (3,2)=1 → “DRDDR”.

          * **R** → (3,3)=1 → **“DRDDRR”** record.
            Other moves either revisit/leave grid/blocked.
            **Final sorted**: `["DDRDRR", "DRDDRR"]`.

---

## 3) Python solutions (two ways)

### A) Brute/clear DFS (uses a fresh `visited` copy at each recursion)

Simple to reason about; slightly heavier on space/time but fine for n≤5.

```python
#User function Template for python3
class Solution:
    def ratInMaze(self, maze):
        """
        Return all paths from (0,0) to (n-1,n-1) as strings using 'U','D','L','R'.
        Brute/clear DFS: pass a copied 'visited' to each recursive call.
        Time  : O(4^(n*n)) in worst-case empty grid (enumeration)
        Space : O(n*n) recursion depth + O(n*n) per path for visited copies
        """
        n = len(maze)
        if n == 0 or maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []

        res = []
        # Direction tuples + their letter, ordered to produce lexicographic output
        dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

        def dfs(r, c, path, visited):
            if r == n - 1 and c == n - 1:
                res.append(path)
                return

            for dr, dc, ch in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    # copy visited for clarity (brute)
                    nxt = [row[:] for row in visited]
                    nxt[nr][nc] = True
                    dfs(nr, nc, path + ch, nxt)

        visited0 = [[False] * n for _ in range(n)]
        visited0[0][0] = True
        dfs(0, 0, "", visited0)

        # Already generated in lexicographic order due to dirs; sorting is safe if unsure:
        # res.sort()
        return res
```

### B) Optimized backtracking (single `visited`, mark/unmark)

Same correctness; much lighter memory footprint and faster.

```python
class Solution:
    def ratInMaze(self, maze):
        """
        Optimized backtracking: single 'visited' grid; mark before recursing, unmark after.
        Explore in order D,L,R,U to naturally emit lexicographically smallest paths.

        Time  : O(4^(n*n)) in worst-case enumeration (but very fast for n<=5)
        Space : O(n*n) for visited + O(n*n) recursion worst depth
        """
        n = len(maze)
        if n == 0 or maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []

        res = []
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        # Ordered as 'D'<'L'<'R'<'U' to match lexicographic requirement
        dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

        def dfs(r, c, path):
            if r == n - 1 and c == n - 1:
                res.append(path)
                return
            for dr, dc, ch in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True          # mark
                    dfs(nr, nc, path + ch)
                    visited[nr][nc] = False         # unmark (backtrack)

        dfs(0, 0, "")
        # No need to sort if you preserved D,L,R,U order; sort() is harmless safety:
        # res.sort()
        return res
```

> In interviews, implement **B**. If asked for “easier to understand”, show **A** first, then optimize to **B** by pointing out that copying `visited` is unnecessary.

---

## 4) Interviewer Q&A (high-yield)

**Q1. Why DFS/backtracking instead of BFS?**
We must **enumerate all paths**, not just shortest. DFS with backtracking is the natural enumerator; BFS is for shortest paths and doesn’t help enumerate all efficiently.

**Q2. How do you ensure no revisits?**
Maintain a `visited` grid; mark the current cell before exploring neighbors and **unmark** (backtrack) when returning.

**Q3. How do you guarantee lexicographic order?**
Explore directions in **lexicographic letter order**: `'D'`, `'L'`, `'R'`, `'U'`. Then the first differing letter between any two paths is emitted in the correct order. (Alternatively, collect and `sort()` once.)

**Q4. Time/Space complexity?**
Worst case (all `1`s) explores an exponential number of simple paths: `O(4^(n*n))` upper bound for branching; recursion depth is `O(n*n)`. For typical constraints `n ≤ 5`, this is fine.

**Q5. Edge cases?**

* Start or goal blocked → `[]`.
* Single cell `n=1`: return `[""]` if it’s `1`, else `[]`.
* Islands of `1`s that don’t connect → `[]`.

**Q6. Can you avoid recursion?**
Yes (explicit stack), but recursion is simpler and idiomatic for backtracking.

**Q7. How would you print one path only (any path)?**
Return immediately after recording the first found path (or use a boolean to short-circuit).

**Q8. How to add diagonal moves?**
Extend `dirs` with the diagonal deltas and letters; everything else remains the same.

---

---

here’s a **runnable, interview-style full program** for **Rat in a Maze** that:

* implements two variants with your exact signature
  `class Solution: def ratInMaze(self, maze): ...`

  * **Brute/clear DFS** (copies `visited` at each recursion)
  * **Optimized backtracking** (single `visited`, mark/unmark)
* prints outputs for a few inputs,
* and uses **timeit** to report **average runtime per call**.

I’ve added **inline comments** detailing **time/space complexity** precisely where they matter.

---

## 5) Full Python Program (with inline complexity notes + timings)

```python
"""
Rat in a Maze — enumerate all paths from (0,0) to (n-1,n-1)
Moves allowed: U, D, L, R (no diagonals)
Cell values: 0 = blocked, 1 = free

We provide two implementations sharing the same public signature:
    class Solution:
        def ratInMaze(self, maze): -> List[str]

A) Brute/clear DFS:
   - Pass a *copied* visited grid to each recursive call (easiest to reason about).
   - Time  : O(4^(n*n)) worst-case enumeration (every cell branches up to 4 ways).
   - Space : O(n*n) recursion depth, plus O(n*n) per call for visited copies.

B) Optimized backtracking:
   - Maintain a single visited grid; mark before recursing, unmark on return.
   - Time  : Same big-O enumeration; strictly faster constants vs A.
   - Space : O(n*n) visited + O(n*n) recursion depth (no per-call copies).

The driver prints outputs for sample mazes and benchmarks the two approaches with timeit.
"""

from typing import List
import timeit


# ------------------------------- A) Brute / clear DFS ------------------------------- #
class SolutionBrute:
    def ratInMaze(self, maze: List[List[int]]) -> List[str]:
        """
        Return all lexicographically ordered paths using a *copying* DFS.

        Implementation notes:
        - We explore neighbors in the order D, L, R, U so that results are produced
          directly in lexicographic order (ASCII 'D'<'L'<'R'<'U'), no sort needed.
        - If unsure about order, you can always res.sort() at the end (adds O(k log k),
          where k is number of solutions).

        Complexity:
        - Let n be grid dimension.
        - Worst-case time  : O(4^(n*n)) paths explored in an all-1s grid.
        - Worst-case space : O(n*n) recursion depth + O(n*n) per call due to copies.
        """
        n = len(maze)
        if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return []

        res: List[str] = []
        dirs = [(+1, 0, 'D'), (0, -1, 'L'), (0, +1, 'R'), (-1, 0, 'U')]  # D,L,R,U

        def dfs(r: int, c: int, path: str, visited: List[List[bool]]) -> None:
            # Base: reached goal — O(1)
            if r == n - 1 and c == n - 1:
                res.append(path)
                return

            # Try up to 4 neighbors — constant factor
            for dr, dc, ch in dirs:
                nr, nc = r + dr, c + dc
                # O(1) bounds and feasibility checks
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    # Copy visited for clarity (brute) — O(n^2) per expansion
                    nxt = [row[:] for row in visited]
                    nxt[nr][nc] = True
                    dfs(nr, nc, path + ch, nxt)

        # Init visited and start DFS — O(n^2)
        visited0 = [[False] * n for _ in range(n)]
        visited0[0][0] = True
        dfs(0, 0, "", visited0)

        # Already lexicographic due to D,L,R,U order; uncomment to be extra safe:
        # res.sort()
        return res


# ------------------------------- B) Optimized backtracking ------------------------------- #
class SolutionOptimized:
    def ratInMaze(self, maze: List[List[int]]) -> List[str]:
        """
        Return all lexicographically ordered paths using a single visited grid, with
        mark/unmark (backtracking) — faster and less memory than the brute copy.

        Complexity:
        - Worst-case time  : O(4^(n*n)) enumeration
        - Worst-case space : O(n*n) visited + O(n*n) recursion stack
        """
        n = len(maze)
        if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return []

        res: List[str] = []
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        dirs = [(+1, 0, 'D'), (0, -1, 'L'), (0, +1, 'R'), (-1, 0, 'U')]  # D,L,R,U

        def dfs(r: int, c: int, path: str) -> None:
            if r == n - 1 and c == n - 1:
                res.append(path)
                return
            for dr, dc, ch in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True       # mark — O(1)
                    dfs(nr, nc, path + ch)       # next recursion
                    visited[nr][nc] = False      # unmark — O(1)

        dfs(0, 0, "")
        # res.sort()  # not needed thanks to D,L,R,U order
        return res


# -------------------------------- timing helper -------------------------------- #
def bench(func, *args, number=5000) -> float:
    """
    Return average seconds per run using timeit.
    For tiny inputs, Python overhead dominates, so treat as *relative* comparison.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------ driver ------------------------------------ #
if __name__ == "__main__":
    print("=== Rat in a Maze — Brute vs Optimized Backtracking ===\n")

    # Example 1 from prompt
    maze1 = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
    ]
    # Expected: ["DDRDRR", "DRDDRR"]

    # Example 2 from prompt (blocked destination -> [])
    maze2 = [
        [1, 0],
        [1, 0],
    ]

    # Example 3 from prompt
    maze3 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    # Expected: ["DDRR", "RRDD"]

    A = SolutionBrute()
    B = SolutionOptimized()

    # Run examples
    print(">>> Example 1")
    print("maze1 =")
    for row in maze1: print(row)
    outA1 = A.ratInMaze(maze1)
    outB1 = B.ratInMaze(maze1)
    print("Brute DFS       :", outA1)
    print("Optimized DFS   :", outB1, "\n")

    print(">>> Example 2")
    for row in maze2: print(row)
    outA2 = A.ratInMaze(maze2)
    outB2 = B.ratInMaze(maze2)
    print("Brute DFS       :", outA2)
    print("Optimized DFS   :", outB2, "\n")

    print(">>> Example 3")
    for row in maze3: print(row)
    outA3 = A.ratInMaze(maze3)
    outB3 = B.ratInMaze(maze3)
    print("Brute DFS       :", outA3)
    print("Optimized DFS   :", outB3, "\n")

    # Micro-benchmarks (average seconds/run)
    print("=== Timings (average seconds per run) ===")
    runs_small = 20000
    tA1 = bench(SolutionBrute().ratInMaze, maze1, number=runs_small)
    tB1 = bench(SolutionOptimized().ratInMaze, maze1, number=runs_small)
    print(f"Example1 runs={runs_small:5d}:  Brute {tA1:.8e}s | Optimized {tB1:.8e}s")

    runs_med = 5000
    tA3 = bench(SolutionBrute().ratInMaze, maze3, number=runs_med)
    tB3 = bench(SolutionOptimized().ratInMaze, maze3, number=runs_med)
    print(f"Example3 runs={runs_med:5d}:  Brute {tA3:.8e}s | Optimized {tB3:.8e}s")

    print("\nNote: numbers vary by machine/Python version. "
          "Optimized backtracking avoids per-call visited copies → fewer allocations/faster.")
```

### What the program prints

* For **Example 1**: both variants output `["DDRDRR", "DRDDRR"]`.
* For **Example 2**: both output `[]`.
* For **Example 3**: both output `["DDRR", "RRDD"]`.
* Then you get **average seconds/run** for the two methods; optimized backtracking is typically faster.

---

## 6) Real-World Use Cases (the important ones)

1. **Robot motion planning in grid worlds (no revisit constraints)**
   Enumerating all feasible routes given blocked cells and movement constraints (useful for validation/testing path planners).

2. **Puzzle/game solvers**
   “Labyrinth”/maze games, level generation validation, or “find all routes” puzzles (backtracking is a natural fit).

3. **Exhaustive test case generation**
   Generate all legal sequences of moves through a state space to fuzz/verify rules (e.g., ensuring constraints prevent revisits).

4. **Education / visualization of search**
   Demonstrates DFS vs backtracking concepts, pruning, and lexicographic ordering directly and visually.