# Travelling Salesman Problem 🧳

**Difficulty:** Hard  
**Accuracy:** 46.35%  
**Submissions:** 35K+  
**Points:** 8  
**Average Time:** 25m  

---

## Problem Statement

Given a 2D matrix **cost[][]** of size **n** where `cost[i][j]` denotes the cost of moving from city **i** to city **j**.  

Your task is to complete a tour from **city 0** (0-based index) to all other cities such that you visit each city **exactly once** and then at the end come back to city 0 at **minimum cost**.

---

## Examples

### Example 1

**Input:**  
`cost[][] = [[0, 111],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[112, 0]]`

**Output:**  
`223`

**Explanation:**  
We can visit `0 -> 1 -> 0` and cost = `111 + 112`.

---

### Example 2

**Input:**  
`cost[][] = [[0, 1000, 5000],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[5000, 0, 1000],`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1000, 5000, 0]]`

**Output:**  
`3000`

**Explanation:**  
We can visit `0 -> 1 -> 2 -> 0` and cost = `1000 + 1000 + 1000 = 3000`.

---

## Constraints

- \( 1 \leq \text{cost.size()} \leq 15 \)  
- \( 0 \leq \text{cost}[i][j] \leq 10^4 \)

---

## Expected Complexities

- **Time Complexity:** \( O(n^2 \cdot 2^n) \)  
- **Auxiliary Space:** \( O(n \cdot 2^n) \)

---

## Company Tags

- Microsoft  
- Samsung  
- Google  
- Opera  

---

## Topic Tags

- Matrix  
- Dynamic Programming  
- Bit Magic  
- Arrays  
- Data Structures  
- Algorithms  

---

## Related Interview Experiences

- Samsung Interview Experience Set 30 Campus  
- Samsung Bangalore Interview Experience For Research Profile  
- Samsung Interview Experience On Campus For Software Engineer September 2018  

---

## Related Articles

- Traveling Salesman Problem Tsp Implementation  
- Travelling Salesman Problem Using Dynamic Programming  

---

---

Got it — let’s focus around that fixed DP solution.

---

## 2. Explanation + Step-by-Step Dry Run

### Problem recap

* `cost[i][j]` = cost of going from city `i` to city `j`.
* Start at city **0**, visit every city **exactly once**, then return to city **0**.
* Minimize total cost.

This is the classic **Travelling Salesman Problem (TSP)** with `n ≤ 15`, perfect for **bitmask DP**.

---

### Core DP idea

We track **which cities we’ve visited** and **where we currently are**.

Let:

> `dp[mask][u]` = minimum cost to
>   start at city `0`, visit exactly the set of cities in `mask`, and end at city `u`.

* `mask` is a bitmask of length `n`:

  * Bit `i` is 1 if city `i` has been visited.
* City `0` is always included (we start from 0).

**Transition**

From state `(mask, u)` we can go to any city `v` not yet visited:

```text
new_mask = mask | (1 << v)
dp[new_mask][v] = min(
    dp[new_mask][v],
    dp[mask][u] + cost[u][v]
)
```

**Base case**

Only city 0 visited and we are at city 0:

```text
dp[1 << 0][0] = 0
```

(all other entries start as +∞)

**Answer**

All cities visited: `FULL_MASK = (1 << n) - 1`.

We can end at any city `u` and then go back to `0`:

```text
ans = min over u: dp[FULL_MASK][u] + cost[u][0]
```

(We include `u = 0` to handle `n = 1` correctly.)

---

### Dry run on Example 1

```python
cost = [
  [0,   111],
  [112,   0]
]
n = 2
```

We must go `0 -> 1 -> 0`.

* Bits: `[city1 city0]`
* `FULL_MASK = (1<<2) - 1 = 3` (0b11)

Initialize `dp` as 4x2 table (mask from 0..3, city 0..1) with `INF`, then:

```text
dp[01][0] = 0   # only city 0 visited, at city 0
```

All other `dp[mask][u] = INF`.

---

#### 1) mask = 0 (00)

* City 0 not in mask → skip (we always require 0 in mask).

#### 2) mask = 1 (01)

* City 0 in mask → process.

For `u = 0`:

* `dp[01][0] = 0`, reachable.

Try all `v`:

* `v = 0` is already in mask → skip.
* `v = 1` not visited:

  * `new_mask = 01 | 10 = 11`
  * `new_cost = dp[01][0] + cost[0][1] = 0 + 111 = 111`
  * Update:

    ```text
    dp[11][1] = min(INF, 111) = 111
    ```

For `u = 1`:

* `dp[01][1] = INF` → unreachable → skip.

#### 3) mask = 2 (10)

* Bit 0 not set → skip (we force start city 0 to be in mask).

#### 4) mask = 3 (11)

* Bit 0 set.

For `u = 0`: `dp[11][0] = INF` → skip.

For `u = 1`: `dp[11][1] = 111`, reachable.

Try all `v`:

* `v = 0` is already visited? yes (mask=11), so skip.
* `v = 1` is also visited, skip.

No new masks.

---

#### Final answer

Now all cities visited (`FULL_MASK = 11`).

We compute:

```text
answer = min over u:
  u = 0: dp[11][0] + cost[0][0] = INF + 0 = INF  (ignored)
  u = 1: dp[11][1] + cost[1][0] = 111 + 112 = 223
```

So `answer = 223`, which matches the sample.

For `n=1`, we’d have:

* `FULL_MASK = 1`
* `dp[1][0] = 0`
* final loop:

  * `u=0` → `dp[1][0] + cost[0][0] = 0 + 0 = 0` → answer = 0

So edge-case is handled too.

---

## 3. Python Codes (brute + optimized variants)

### 3.1 Brute Force (permutations) – for understanding

```python
from itertools import permutations

class Solution:
    def tsp_bruteforce(self, cost):
        """
        Brute-force TSP:
        - Try all permutations of cities except 0.
        - Compute tour cost for each permutation.
        - Return minimum.

        Let n be number of cities.
        Time  : O((n-1)! * n)        # factorial, not for n=15 in practice
        Space : O(n) for temporary permutation and some counters.
        """
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return 0  # start at 0, end at 0, no movement

        cities = list(range(1, n))  # all cities except 0
        best_cost = float('inf')

        # Generate every permutation of visiting order
        for perm in permutations(cities):
            total_cost = 0
            current = 0

            # Move along the permutation
            for nxt in perm:
                total_cost += cost[current][nxt]
                current = nxt

            # Return to starting city
            total_cost += cost[current][0]

            if total_cost < best_cost:
                best_cost = total_cost

        return best_cost
```

Not for large constraints, but good to mention as baseline.

---

### 3.2 Bottom-up DP with Bitmask (the GFG / interview classic)

This is the **corrected** version you referred to.

```python
class Solution:
    def tsp(self, cost):
        """
        DP with bitmask solution to TSP starting and ending at city 0.

        State:
            dp[mask][u] = min cost to start at 0, visit exactly the cities in 'mask',
                          and end at city u.  'mask' is a bitmask of visited cities.

        Transition:
            From (mask, u) go to any unvisited v:
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

        Initialization:
            dp[1 << 0][0] = 0   # only city 0 visited, at city 0

        Answer:
            FULL = (1 << n) - 1
            ans  = min over u: dp[FULL][u] + cost[u][0]

        Complexity:
            n cities, M = 2^n masks
            Time  : O(n^2 * M)
            Space : O(n * M)
        """
        n = len(cost)
        if n == 0:
            return 0

        FULL_MASK = (1 << n) - 1
        INF = 10**18

        # dp[mask][u] table
        dp = [[INF] * n for _ in range(1 << n)]

        # Only city 0 visited, at city 0
        dp[1][0] = 0   # mask 000...001

        # Iterate over all masks
        for mask in range(1 << n):
            # We must always include city 0 (bit 0) in the path
            if not (mask & 1):
                continue

            for u in range(n):
                if dp[mask][u] == INF:
                    # This state hasn't been reached
                    continue

                # Try to go to each city v that is not yet visited in 'mask'
                for v in range(n):
                    if mask & (1 << v):   # bit v already set => city v visited
                        continue

                    new_mask = mask | (1 << v)
                    new_cost = dp[mask][u] + cost[u][v]

                    if new_cost < dp[new_mask][v]:
                        dp[new_mask][v] = new_cost

        # Close tour: all cities visited, return to 0
        answer = INF
        for u in range(n):   # include u=0 so n=1 works
            if dp[FULL_MASK][u] == INF:
                continue
            total_cost = dp[FULL_MASK][u] + cost[u][0]
            if total_cost < answer:
                answer = total_cost

        # Safety fallback (should not happen for valid TSP)
        if answer == INF:
            return 0
        return answer
```

---

### 3.3 Top-down (recursive) DP with memoization (same complexity, often easier to code)

Some interviewers like the recursive mask DP, so here’s that variant too:

```python
from functools import lru_cache

class Solution:
    def tsp_topdown(self, cost):
        """
        Top-down recursive DP with bitmask (same logic as bottom-up).

        State:
            solve(mask, u) = minimum extra cost to:
                - start at city u,
                - visit all cities not yet visited in 'mask',
                - and finally return to city 0.
            'mask' contains the set of cities visited so far.

        We call solve(1, 0) initially (only city 0 visited, starting at 0).

        Time  : O(n^2 * 2^n)
        Space : O(n * 2^n) for memoization (stack depth O(n)).
        """
        n = len(cost)
        FULL_MASK = (1 << n) - 1

        @lru_cache(maxsize=None)
        def solve(mask, u):
            # If all cities visited, return cost to go back to 0
            if mask == FULL_MASK:
                return cost[u][0]

            best = float('inf')

            # Try visiting each unvisited city v next
            for v in range(n):
                if mask & (1 << v):
                    continue   # already visited
                new_mask = mask | (1 << v)
                candidate = cost[u][v] + solve(new_mask, v)
                if candidate < best:
                    best = candidate

            return best

        # Start from city 0, only city 0 visited
        return solve(1, 0)
```

You can mention this as an alternative that uses recursion + memo.

---

## 4. Interview Memory Tricks + Expected Q&A

### 4.1 Super-short mental template

**Phrase to remember:**

> **“State = (mask, last); transition tries all unvisited; final min + return to 0.”**

Or:

> **“0 fixed, mask grows, last moves.”**

If you remember just that, you can reconstruct the DP.

---

### 4.2 5-line pseudo-code template

```text
dp[1<<0][0] = 0
for mask in 0..(1<<n)-1 with bit0 set:
    for u in 0..n-1 with dp[mask][u] < INF:
        for v in 0..n-1 where v not in mask:
            dp[mask | (1<<v)][v] = min(dp[mask | (1<<v)][v], dp[mask][u] + cost[u][v])
ans = min over u: dp[ALL][u] + cost[u][0]
return ans
```

You can rehearse that on the way into the interview.

---

### 4.3 Typical Interview Questions & Answers

---

**Q1: What’s the brute-force solution and its complexity?**

**A:**
Enumerate all permutations of cities `[1..n-1]` with city 0 fixed as start and end. For each permutation compute the tour cost and take the minimum. There are `(n-1)!` permutations, each costing `O(n)` to evaluate, so the time complexity is `O((n-1)! * n)`, which becomes impractical past `n ≈ 10`.

---

**Q2: What is your DP state and why?**

**A:**
I use `dp[mask][u]`, where `mask` is the set of visited cities and `u` is the current city. This naturally captures “where we’ve been” plus “where we are now”, which is exactly the information we need to decide valid next moves and compute remaining cost. Using a bitmask makes the set efficient to store and index.

---

**Q3: How do you derive the transition formula?**

**A:**
From `dp[mask][u]` we can move to any city `v` not yet in `mask`. The new visited set is `new_mask = mask | (1 << v)`, and the cost to reach `(new_mask, v)` is the old cost plus `cost[u][v]`. So:
[
dp[new_mask][v] = \min\left(dp[new_mask][v], dp[mask][u] + cost[u][v]\right)
]

---

**Q4: Why do you always force city 0 to be in the mask?**

**A:**
We always start from city 0, and it must be visited in every valid tour. For efficiency and to avoid symmetric duplicates, I restrict DP to masks where bit 0 is set — this removes a factor of `n` redundancy without changing optimal cost.

---

**Q5: What are time and space complexities of your DP solution?**

**A:**
There are `2^n` masks and for each mask up to `n` possible ending cities `u`. From each `(mask, u)` I consider up to `n` next cities `v`. So time is `O(n^2 * 2^n)`. The DP table has `2^n * n` entries, so space is `O(n * 2^n)`.

---

**Q6: How do you handle edge cases like `n = 1`?**

**A:**
We still do the same DP. `FULL_MASK = 1`, `dp[1][0] = 0`. In the final loop, I iterate `u` from `0` to `n-1` inclusive, so I consider `u = 0` and compute `dp[1][0] + cost[0][0] = 0`. That returns the correct answer of `0` instead of leaving the answer as infinity.

---

**Q7: Could you instead implement this top-down?**

**A:**
Yes. Define a recursive function `solve(mask, u)` returning the minimal extra cost to visit all remaining cities from `u` given `mask`. If all bits are set, return `cost[u][0]`. Otherwise try all unvisited `v` and return:
[
\min_{v \text{ not in mask}} cost[u][v] + solve(mask \cup {v}, v)
]
Memoizing `solve(mask, u)` gives the same `O(n^2 * 2^n)` complexity as the bottom-up DP.

---

If you keep in your head:

> “Start at 0, `dp[mask][u]`, grow mask by unvisited v, final min back to 0.”

and the small pseudo-code loop, you’ll be able to explain and code the TSP DP comfortably in an interview.

---

---

Let’s focus on the bottom-up DP with bitmask version you referenced.

---

## 5. Real-World Use Cases (few, but powerful & interview-friendly)

You can mention **2–3** of these and you’re good:

1. **Delivery / Courier Route Optimization**

   * Cities = customers or depots, `cost[i][j]` = distance / fuel / time.
   * A van must start at a warehouse, visit each customer exactly once, then return.
   * Finding the minimal tour is exactly **TSP**, and the bitmask DP is used when the number of stops is small (VIP customers, high-value deliveries).

2. **PCB Drilling / CNC Machine Path**

   * “Cities” = drill holes or machining points.
   * `cost[i][j]` = time to move the drill head from point `i` to `j`.
   * To minimize machine runtime and wear, we want the shortest cycle visiting all points → again TSP.

3. **Warehouse Robot Item Picking**

   * Robot must pick items at several shelf locations and return to the dock.
   * Locations = nodes, `cost[i][j]` = travel time between shelves.
   * Optimizing the robot’s tour is TSP; for a small number of picks per trip, the bitmask DP is an exact solver.

Keep them short in the interview:

> “This exact DP is used as the exact solver when the number of stops is small – e.g., a robot picking 10–15 items in a warehouse, a delivery van visiting VIP customers, or a CNC drill visiting all holes on a PCB.”

---

## 6. Full Python Program (with timing + detailed complexity comments)

This is a **complete, runnable** script using the bottom-up DP with bitmask solution you pointed to.

```python
import time


class Solution:
    def tsp(self, cost):
        """
        Travelling Salesman Problem using DP + bitmask.

        cost: n x n matrix, cost[i][j] = cost to go from city i to city j.
        We must:
            - start at city 0,
            - visit every city exactly once,
            - return to city 0,
            - minimize total cost.

        STATE:
            dp[mask][u] = minimum cost to:
                - start at city 0,
                - visit exactly the cities in 'mask',
                - end at city u.
            Here:
                - 'mask' is an integer bitmask of length n.
                - bit i is 1 if city i is visited.
                - city 0 is always included in valid masks.

        TRANSITION:
            From (mask, u), try to go to every city v not in 'mask':
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(
                    dp[new_mask][v],
                    dp[mask][u] + cost[u][v]
                )

        INITIALIZATION:
            Only city 0 visited, at city 0:
                dp[1 << 0][0] = 0

        ANSWER:
            FULL_MASK = (1 << n) - 1  # all cities visited
            answer = min over u: dp[FULL_MASK][u] + cost[u][0]

        COMPLEXITY (let n be number of cities, M = 2^n):
            - dp table size:  M * n  => O(n * 2^n) space.
            - Outer mask loop:   M   masks
            - For each mask:     up to n values of u
            - For each (mask,u): up to n transitions v
            => Time: O(n^2 * 2^n)
        """

        n = len(cost)
        if n == 0:
            # No cities: trivial cost 0
            return 0

        FULL_MASK = (1 << n) - 1
        INF = 10**18  # a large sentinel for "infinite" cost

        # ------------------ Allocate DP table ------------------
        # dp[mask][u]: (2^n) x n table
        # Time to init: O(n * 2^n)
        # Space:        O(n * 2^n)
        dp = [[INF] * n for _ in range(1 << n)]

        # ------------------ Base case ------------------
        # Only city 0 is visited (mask = 000...001), we are at city 0.
        # This is the starting state with cost 0.
        dp[1][0] = 0

        # ------------------ Fill DP table ------------------
        # Iterate over all masks (subsets of cities).
        # Time: 2^n masks
        for mask in range(1 << n):
            # Optimization: every valid path must include city 0.
            # If bit 0 is not set, this mask is not part of our search space.
            if not (mask & 1):
                continue

            # For each possible ending city u in this mask
            # Time over all masks: O(n * 2^n)
            for u in range(n):
                current_cost = dp[mask][u]
                if current_cost == INF:
                    # This (mask, u) state was never reached.
                    continue

                # Try going from u to every city v not yet visited in 'mask'
                # Time over all (mask,u): O(n)
                for v in range(n):
                    # If bit v is already set in mask, city v is visited
                    if mask & (1 << v):
                        continue

                    new_mask = mask | (1 << v)
                    new_cost = current_cost + cost[u][v]

                    # Relax (update) dp[new_mask][v] if we found a cheaper path
                    if new_cost < dp[new_mask][v]:
                        dp[new_mask][v] = new_cost

        # ------------------ Close the tour ------------------
        # All cities visited: mask = FULL_MASK
        # We must return from last city u back to city 0.
        answer = INF
        for u in range(n):
            if dp[FULL_MASK][u] == INF:
                # Never reached state with all cities visited and ending at u
                continue

            # Total tour cost: cost to reach u + cost(u -> 0)
            total_cost = dp[FULL_MASK][u] + cost[u][0]
            if total_cost < answer:
                answer = total_cost

        # Safety fallback: if no valid tour found (shouldn't happen on valid input),
        # return 0 instead of INF.
        if answer == INF:
            return 0

        return answer


# ------------------ Driver with timing ------------------ #

def main():
    """
    Driver function:
    - Reads input matrix.
    - Calls Solution().tsp().
    - Prints result and total elapsed time.

    Input format (simple competitive-style):
        n
        row0_0 row0_1 ... row0_(n-1)
        row1_0 row1_1 ... row1_(n-1)
        ...
        row(n-1)_0 ...   row(n-1)_(n-1)

    Example:
        2
        0 111
        112 0

    Complexity of this I/O:
        - Reading n:          O(1)
        - Reading n^2 values: O(n^2)
        - Printing:           O(1)
    """

    print("Enter number of cities n:")
    n_line = input().strip()
    if not n_line:
        print("No input provided.")
        return
    n = int(n_line)

    print(f"Enter the {n}x{n} cost matrix row by row:")
    cost = []
    for i in range(n):
        # Read one row of n integers
        row = list(map(int, input().split()))
        # If row length is not exactly n, we trim or pad zeros (defensive)
        if len(row) < n:
            row = row + [0] * (n - len(row))
        elif len(row) > n:
            row = row[:n]
        cost.append(row)

    solver = Solution()

    # Start timer right before calling tsp (core algorithm)
    start = time.perf_counter()

    # Core DP: O(n^2 * 2^n)
    result = solver.tsp(cost)

    # Stop timer right after the computation
    end = time.perf_counter()

    print("\nMinimum tour cost:", result)
    print(f"Total elapsed time (seconds): {end - start:.6f}")


if __name__ == "__main__":
    main()
```

### How a sample run looks

Input:

```text
2
0 111
112 0
```

Output (typical):

```text
Enter number of cities n:
2
Enter the 2x2 cost matrix row by row:
0 111
112 0

Minimum tour cost: 223
Total elapsed time (seconds): 0.0000xx
```

You can reuse this exact structure when practicing; in a coding round you’d usually only paste the `Solution` class with `tsp`, but having a full timed driver is great to check performance and understand how the DP behaves.
