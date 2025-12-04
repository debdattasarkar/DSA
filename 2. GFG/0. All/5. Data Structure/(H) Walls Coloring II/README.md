# Walls Coloring II 🎨

**Difficulty:** Hard  
**Accuracy:** 50.15%  
**Submissions:** 26K+  
**Points:** 8  

---

## Problem Statement

You are given **n** walls arranged in a row, and each wall must be painted using one of the **k** available colors.  
The cost of painting **i-th** wall with **j-th** color is given by **costs[i][j]**.  

Your task is to determine the **minimum total cost** required to paint all the walls in such a way that **no two adjacent walls share the same color**.  

If it is impossible to paint the walls under this condition, you must return **-1**.

---

## Examples

### Example 1

**Input:**  
`n = 4, k = 3`  
`costs[][] = [[1, 5, 7],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[5, 8, 4],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[3, 2, 9],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1, 2, 4]]`

**Output:**  
`8`

**Explanation:**  

- Paint wall 0 with color 0. Cost = 1  
- Paint wall 1 with color 2. Cost = 4  
- Paint wall 2 with color 1. Cost = 2  
- Paint wall 3 with color 0. Cost = 1  

Total Cost = `1 + 4 + 2 + 1 = 8`.

---

### Example 2

**Input:**  
`n = 5, k = 1`  
`costs[][] = [[5],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[4],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[9],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[2],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1]]`

**Output:**  
`-1`

**Explanation:**  
It is not possible to color all the walls under the given conditions (with only one color and the restriction that adjacent walls cannot share the same color).

---

## Constraints

- \( 0 \le n \le 10^3 \)  
- \( 0 \le k \le 10^3 \)  
- \( 1 \le \text{costs}[i][j] \le 10^5 \)

---

## Expected Complexities

- **Time Complexity:** `O(n * k)`  
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Dynamic Programming  

---

## Related Articles

- [*Min Cost To Color All Walls Such That No Adjacent Walls Have Same Color*](https://www.geeksforgeeks.org/min-cost-to-color-all-walls-such-that-no-adjacent-walls-have-same-color/)

---

---

I’ll follow your numbering: explanation + dry run → Python (brute + optimized) → interview memory + Q&A.

---

## 2. Explanation + Step-by-Step Dry Run

### Problem recap

* We have `n` walls in a row.
* There are `k` available colors.
* `costs[i][c]` = cost of painting **wall i** with **color c**.
* We must paint every wall such that:

  * **No two adjacent walls have the same color.**
  * Total cost is **minimum**.
* If it’s impossible (e.g., `k = 1` and `n > 1`), return `-1`.

Indices (0-based):

* walls: `i = 0 .. n-1`
* colors: `c = 0 .. k-1`

---

### DP idea (basic)

Define:

> `dp[i][c]` = minimum cost to paint walls `0..i`
> such that wall `i` is painted with color `c`.

Then:

* For the **first wall** (`i = 0`):

  ```text
  dp[0][c] = costs[0][c]
  ```

* For any later wall (`i > 0`):

  ```text
  dp[i][c] = costs[i][c] + min(dp[i-1][p] for all p != c)
  ```

Explanation:

* We want wall `i` to be color `c`.
* The previous wall `i-1` must have **any color `p` except `c`**.
* So we take the best cost among all those `p` and add `costs[i][c]`.

Naively, for each `(i, c)` we scan all `k` colors on row `i-1`, giving `O(n * k^2)`.

But `n, k` can be up to `10^3`, so `n * k^2` can be ~10^9 operations → too slow.

---

### Optimization trick to get O(n * k)

Key observation:

For each row `i-1`, we only ever need:

1. **The smallest value** in `dp[i-1][*]`: `min1_val`, with color index `min1_color`.
2. **The second smallest value**: `min2_val`.

Then for row `i` and color `c`:

* If `c` is **not** the color that achieved `min1_val` on row `i-1`:

  ```text
  dp[i][c] = costs[i][c] + min1_val
  ```

  because we can safely use the global minimum from previous row.

* If `c` **is** `min1_color`, we can’t reuse the same color on adjacent walls, so we must use `min2_val`:

  ```text
  dp[i][c] = costs[i][c] + min2_val
  ```

Thus each row is processed in O(k):

* One pass to know `min1_val`, `min2_val`, `min1_color`.
* Another pass to compute all `dp[i][c]`.

Total complexity: **O(n * k)**.

---

### Edge cases

* `n == 0`: no walls → cost 0.
* `k == 0` and `n > 0`: cannot paint any wall → return `-1`.
* `k == 1`:

  * If `n == 0` or `n == 1`, we can paint (just use the only color).
  * If `n > 1`, impossible (adjacent walls would share same color) → return `-1`.

---

### Dry Run on Example 1

```text
n = 4, k = 3
costs = [
  [1, 5, 7],
  [5, 8, 4],
  [3, 2, 9],
  [1, 2, 4]
]
```

We will maintain `dp` row by row.

#### Row 0 (wall 0)

For the first wall, cost is just the painting cost:

```text
dp[0] = [1, 5, 7]
min1_val = 1 (color 0)
min2_val = 5 (color 1)
min1_color = 0
```

#### Row 1 (wall 1)

We build `dp[1][c]`:

* For color 0:

  * previous color cannot be 0 → use `min2_val = 5`.
  * `dp[1][0] = costs[1][0] + min2_val = 5 + 5 = 10`
* For color 1:

  * previous color can be 0 (which is min1) because 1 != 0 → use `min1_val = 1`.
  * `dp[1][1] = 8 + 1 = 9`
* For color 2:

  * previous color can be 0 → `dp[1][2] = 4 + 1 = 5`

Now `dp[1] = [10, 9, 5]`.

Find smallest & second smallest in `dp[1]`:

* `min1_val = 5`, `min1_color = 2`
* `min2_val = 9`

#### Row 2 (wall 2)

Use min1/min2 from row 1:

* For color 0 (≠ 2): `dp[2][0] = 3 + min1_val(5) = 8`
* For color 1 (≠ 2): `dp[2][1] = 2 + 5 = 7`
* For color 2 (= 2): must use `min2_val(9)` → `dp[2][2] = 9 + 9 = 18`

`dp[2] = [8, 7, 18]`

New mins:

* `min1_val = 7`, `min1_color = 1`
* `min2_val = 8`

#### Row 3 (wall 3)

* Color 0 (≠ 1): `dp[3][0] = 1 + 7 = 8`
* Color 1 (= 1): use second min → `dp[3][1] = 2 + 8 = 10`
* Color 2 (≠ 1): `dp[3][2] = 4 + 7 = 11`

`dp[3] = [8, 10, 11]`

Answer is min over last row: `min(dp[3]) = 8`.

Matches the example.

---

## 3. Python Solutions

We’ll write:

1. **Brute-force DP:** O(n * k²) – simple but slower.
2. **Optimized DP with two minima:** O(n * k) – expected in interviews.

All code with meaningful names and comments.

### 3.1 Brute-force DP (O(n * k²))

```python
from typing import List

class Solution:
    def minCost_bruteforce(self, costs: List[List[int]]) -> int:
        """
        Brute-force DP: O(n * k^2)

        dp[i][c] = min cost to paint walls 0..i where wall i has color c,
                   with no two adjacent walls of the same color.
        Transition:
            dp[i][c] = costs[i][c] + min(dp[i-1][p] for all p != c)

        Time  : O(n * k^2)
        Space : O(n * k)  (can be reduced to O(k) with rolling arrays)
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0]) if costs[0] else 0

        # Impossible cases
        if k == 0 and n > 0:
            return -1
        if k == 1 and n > 1:
            return -1

        # dp table: n rows, k colors
        dp = [[0] * k for _ in range(n)]

        # Base row
        for c in range(k):
            dp[0][c] = costs[0][c]

        # Fill DP
        for i in range(1, n):
            for c in range(k):
                # Find minimum among previous colors != c
                min_prev = float("inf")
                for p in range(k):
                    if p == c:
                        continue
                    if dp[i-1][p] < min_prev:
                        min_prev = dp[i-1][p]
                dp[i][c] = costs[i][c] + min_prev

        # Answer = minimum cost among last wall colors
        answer = min(dp[n-1])
        return answer
```

---

### 3.2 Optimized O(n * k) DP (tracking min1 & min2) – **final answer**

```python
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        Optimized DP for "Walls Coloring II"

        Let n = number of walls, k = number of colors.

        dp[i][c] = minimal total cost to paint walls 0..i, with wall i painted color c,
                   and no two adjacent walls sharing the same color.

        Naive transition:
            dp[i][c] = costs[i][c] + min(dp[i-1][p] for p != c)
        is O(k) per (i, c) => O(n * k^2) total.

        Optimization:
            For each row i-1, track:
                - min1_val: smallest dp[i-1][*]
                - min1_color: color index that gives min1_val
                - min2_val: second smallest dp[i-1][*]
            Then:
                if c != min1_color:
                    dp[i][c] = costs[i][c] + min1_val
                else:
                    dp[i][c] = costs[i][c] + min2_val

            So we do O(k) work per row:
                - One pass to compute min1 and min2.
                - One pass to fill row i.
            Total complexity: O(n * k).

        Edge cases:
            - If n == 0: return 0.
            - If k == 0 and n > 0: impossible -> -1.
            - If k == 1 and n > 1: impossible (adjacent walls must differ) -> -1.

        Time  : O(n * k)
        Space : O(k) using rolling array for previous row.
        """
        n = len(costs)
        if n == 0:
            return 0

        # Number of colors
        k = len(costs[0]) if costs[0] else 0

        # Impossible configurations
        if k == 0 and n > 0:
            return -1
        if k == 1:
            # Possible only if at most one wall
            if n == 1:
                return costs[0][0]
            else:
                return -1

        # prev_dp[c] = dp value for previous wall (i-1) with color c
        prev_dp = [0] * k

        # Initialize for first wall: cost equals painting cost
        for c in range(k):
            prev_dp[c] = costs[0][c]

        # Process walls 1..n-1
        for i in range(1, n):
            # -------- Find smallest and second smallest from prev_dp --------
            min1_val = float("inf")
            min2_val = float("inf")
            min1_color = -1

            # One pass O(k)
            for c in range(k):
                val = prev_dp[c]
                if val < min1_val:
                    # current best becomes second best
                    min2_val = min1_val
                    min1_val = val
                    min1_color = c
                elif val < min2_val:
                    min2_val = val

            # -------- Compute new dp row for wall i --------
            curr_dp = [0] * k
            for c in range(k):
                # If we choose same color as previous row's global min,
                # we must use second min to satisfy adjacency constraint.
                if c == min1_color:
                    curr_dp[c] = costs[i][c] + min2_val
                else:
                    curr_dp[c] = costs[i][c] + min1_val

            # Move current row into prev_dp for next iteration
            prev_dp = curr_dp

        # Final answer: minimum cost among all colors for last wall
        return min(prev_dp)
```

This is the one you’d submit.

---

## 4. Interview Memory Tricks + Expected Q&A

### 4.1 Quick memory hook

Phrase to remember:

> **“Row DP + two minima: min1, min2, min1_color.”**

Algorithm in your head:

1. Maintain DP row for previous wall: `prev_dp`.
2. For each new wall:

   * Scan `prev_dp` to get:

     * `min1_val`, `min1_color` (smallest)
     * `min2_val` (second smallest)
   * For each color `c`:

     * If `c != min1_color`: use `min1_val`.
     * Else: use `min2_val`.
3. Update `prev_dp` and repeat.

That’s it.

---

### 4.2 5-line pseudo-code template

```text
if k == 1 and n > 1: return -1
prev_dp[c] = costs[0][c] for all c
for i from 1 to n-1:
    find (min1_val, min1_color, min2_val) from prev_dp
    for each color c:
        dp[i][c] = costs[i][c] + (min1_val if c != min1_color else min2_val)
    prev_dp = dp[i]
answer = min(prev_dp)
```

You can rebuild full code from this in any language in ~30–60 seconds.

---

### 4.3 Likely Interview Questions & Answers

---

**Q1: What’s the brute-force DP solution and its complexity?**

**A:**
Use `dp[i][c]` = min cost up to wall `i` with wall `i` color `c`.
Transition:

```text
dp[i][c] = costs[i][c] + min(dp[i-1][p] for p != c)
```

Computing that min for each `(i, c)` costs O(k) → overall `O(n * k^2)` time and `O(n * k)` space.

---

**Q2: Why do we need an optimization and what’s the idea?**

**A:**
For `n, k` up to 1000, `O(n * k^2)` can be around 10⁹ operations, too slow.
We note that for each row `i`, the recurrence only needs the **minimum** and **second minimum** values from the previous row. If color `c` is not the color that gave the minimum, we can use the minimum; otherwise, we must use the second minimum. This reduces complexity to `O(n * k)`.

---

**Q3: Can you explain how you maintain the two minima?**

**A:**
In a single pass over `prev_dp`:

```text
min1_val = +∞, min2_val = +∞, min1_color = -1
for each color c:
    val = prev_dp[c]
    if val < min1_val:
        min2_val = min1_val
        min1_val = val
        min1_color = c
    elif val < min2_val:
        min2_val = val
```

Then:

* If current color `c == min1_color`, use `min2_val`.
* Else, use `min1_val`.

---

**Q4: What are the time and space complexities of your optimized solution?**

**A:**

* Time:

  * For each of `n` walls, we scan `k` colors to find `min1`/`min2` and then another `k` to fill the new row → `O(n * k)`.
* Space:

  * We only store two rows (`prev_dp`, `curr_dp`) of length `k` → `O(k)` extra space.

---

**Q5: How do you handle edge cases like `k = 1`?**

**A:**
If there’s only one color:

* If `n == 0`: cost is 0.
* If `n == 1`: we can paint the only wall with that color.
* If `n > 1`: impossible to avoid adjacent equal colors, so we return `-1`.

I also handle `k = 0, n > 0` similarly as impossible.

---

**Q6: Can you summarize the algorithm in one sentence?**

**A:**
“Use dynamic programming per wall and per color, but to keep it O(n * k), track the smallest and second smallest costs from the previous wall so that each new state can use either the best or second-best previous color depending on whether it matches the current color.”

---

If you keep in mind:

> **“dp per row, track min1/min2, reuse min1 unless same color, else min2”**

you’ll be able to reconstruct the code quickly and explain it confidently in an interview.

---

---

Let’s finish this one cleanly.

---

## 5. Real-World Use Cases (easy to tell an interviewer)

Think **“rows of things, many options (colors), but neighbors must differ”**.

1. **Painting Apartments / Hotel Rooms in a Corridor**

   * Each wall/room must be painted one of `k` colors.
   * Adjacent rooms can’t be the same color (aesthetic rule).
   * Different paints have different costs per room.
   * We want the minimum total painting cost → this exact problem.

2. **Server / Rack Assignment with Cooling Zones**

   * Racks in a row; each rack can host one of `k` server types (“colors”).
   * Adjacent racks can’t run the same high-heat server type (to avoid hot spots).
   * Different types have different deployment costs on each rack (power, license, etc.).
   * Choose server type per rack minimizing cost while avoiding identical neighbors.

3. **Scheduling Shifts with Adjacent Constraints**

   * Time slots (walls) in a day/week, employees or roles as “colors”.
   * Adjacent slots cannot be filled by the same role/employee (rest, rotation requirement).
   * Cost per (slot, role) combination differs (overtime, weekends, etc.).
   * Find minimum total staffing cost with no identical adjacent slots.

These are short and relatable; mentioning one or two is enough.

---

## 6. Full Python Program with Timing + Complexity Comments

Below is a complete script:

* Uses the **O(n·k)** optimized DP (tracking best and second-best previous colors).
* Includes a `main()` that:

  * reads `n`, `k`, then the `n x k` cost matrix,
  * runs `Solution.minCost`,
  * prints result and total runtime.

```python
import time
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        Optimized DP for 'Walls Coloring II'.

        costs: 2D list where costs[i][c] = cost to paint wall i with color c.
               n = len(costs)    -> number of walls
               k = len(costs[0]) -> number of colors (if n > 0)

        IDEA:
            dp[i][c] = minimum total cost to paint walls 0..i
                       such that wall i is painted color c,
                       and no two adjacent walls share the same color.

            Naive recurrence:
                dp[i][c] = costs[i][c] + min(dp[i-1][p] for p != c)
            This is O(k) per (i,c) => O(n * k^2).

            Optimization:
                For each row i-1, only two values matter:
                    - min1_val, min1_col = smallest dp[i-1][*] and its color
                    - min2_val           = second smallest dp[i-1][*]
                Then:
                    if c != min1_col:
                        dp[i][c] = costs[i][c] + min1_val
                    else:
                        dp[i][c] = costs[i][c] + min2_val

        COMPLEXITY:
            Let n = number of walls, k = number of colors.
            - For each of n rows:
                * O(k) to find min1 and min2.
                * O(k) to compute new dp row.
            => Time  : O(n * k)
            - We only store one dp row and build the next one.
            => Space : O(k)
        """
        n = len(costs)
        if n == 0:
            # No walls, no cost.
            # Time: O(1), Space: O(1)
            return 0

        k = len(costs[0]) if costs[0] else 0

        # --------- Edge / impossible cases (O(1) time) ----------
        if k == 0:
            # There are walls but no colors to paint them.
            return -1 if n > 0 else 0

        if k == 1:
            # Only one color:
            # - If there is more than one wall, adjacency rule is impossible.
            # - If exactly one wall, cost is simply that cell.
            if n == 1:
                return costs[0][0]
            else:
                return -1

        # prev_dp[c] = minimum cost for painting up to previous wall
        #             with previous wall painted in color c.
        # Initialize for the first wall (i = 0).
        # Time: O(k), Space: O(k)
        prev_dp = [0] * k
        for c in range(k):
            prev_dp[c] = costs[0][c]

        # --------- Process remaining walls one by one ----------
        # Outer loop runs n-1 times: O(n)
        for i in range(1, n):
            # -------- Find min1 and min2 on prev_dp: O(k) --------
            min1_val = float("inf")
            min2_val = float("inf")
            min1_color = -1

            for c in range(k):
                val = prev_dp[c]
                if val < min1_val:
                    # Update both min1 and min2
                    min2_val = min1_val
                    min1_val = val
                    min1_color = c
                elif val < min2_val:
                    min2_val = val

            # -------- Build current dp row using min1/min2: O(k) --------
            curr_dp = [0] * k
            for c in range(k):
                # If we pick the same color as the previous minimum,
                # we must use second-best prev value to avoid same color adjacency.
                if c == min1_color:
                    curr_dp[c] = costs[i][c] + min2_val
                else:
                    curr_dp[c] = costs[i][c] + min1_val

            # Move current row into prev_dp for next iteration.
            prev_dp = curr_dp

        # Final answer: minimum cost across all colors for the last wall.
        # Time: O(k)
        return min(prev_dp)


# ---------------------- DRIVER WITH TIMING ---------------------- #

def main():
    """
    Driver function for local testing.

    Input format (simple, competitive-style):

        n k
        row0_cost_0 row0_cost_1 ... row0_cost_(k-1)
        row1_cost_0 row1_cost_1 ... row1_cost_(k-1)
        ...
        row(n-1)_cost_0 ...       row(n-1)_cost_(k-1)

    Example:
        4 3
        1 5 7
        5 8 4
        3 2 9
        1 2 4

    Complexity of this function (excluding the solver itself):
        - Input reading: O(n * k)
        - Printing:      O(1)
    """

    print("Enter n (walls) and k (colors):")
    first_line = input().strip()
    if not first_line:
        print("No input provided.")
        return

    n, k = map(int, first_line.split())

    costs = []
    if n > 0 and k > 0:
        print(f"Enter the {n}x{k} cost matrix (one row per line):")
    for i in range(n):
        row = list(map(int, input().split()))
        # If row has fewer than k elements, pad with large numbers (or 0) defensively.
        if len(row) < k:
            row += [10**9] * (k - len(row))
        # If row has more than k elements, truncate.
        if len(row) > k:
            row = row[:k]
        costs.append(row)

    solver = Solution()

    # Start timing right before the algorithm.
    start = time.perf_counter()

    # Core algorithm: O(n * k) time, O(k) space.
    result = solver.minCost(costs)

    # Stop timing after computation.
    end = time.perf_counter()

    print("\nMinimum total painting cost:", result)
    print(f"Total elapsed time (seconds): {end - start:.6f}")


if __name__ == "__main__":
    main()
```

### How a sample run looks (conceptually)

Input:

```text
4 3
1 5 7
5 8 4
3 2 9
1 2 4
```

Output (typical):

```text
Enter n (walls) and k (colors):
4 3
Enter the 4x3 cost matrix (one row per line):
1 5 7
5 8 4
3 2 9
1 2 4

Minimum total painting cost: 8
Total elapsed time (seconds): 0.0000xx
```

You can copy-paste this whole script to run locally.
In an interview or coding platform, you’d usually just include the `Solution` class with the `minCost` method, but this full program helps you test and profile your solution end-to-end.
