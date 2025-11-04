
---

# 🐸 Frog Jump

### Difficulty: Medium

**Accuracy:** 49.55%
**Submissions:** 175K+
**Points:** 4
**Average Time:** 15m

---

## 🧠 Problem Statement

Given an integer array **height[]** where **height[i]** represents the height of the *i-th stair*, a frog starts from the **first stair** and wants to reach the **last stair**.

From any stair *i*, the frog has two options:

* It can either jump to the *(i+1)th* stair, or
* It can jump to the *(i+2)th* stair.

The **cost of a jump** is the *absolute difference* in height between the two stairs.

Determine the **minimum total cost** required for the frog to reach the last stair.

---

## 🧩 Examples

### Example 1

**Input:**

```
height[] = [20, 30, 40, 20]
```

**Output:**

```
20
```

**Explanation:**
Minimum cost is incurred when the frog jumps from stair 0 → 1 → 3:

* Jump from stair 0 to 1: cost = |30 − 20| = 10
* Jump from stair 1 to 3: cost = |20 − 30| = 10
  Total Cost = 10 + 10 = **20**

---

### Example 2

**Input:**

```
height[] = [30, 20, 50, 10, 40]
```

**Output:**

```
30
```

**Explanation:**
Minimum cost will be incurred when the frog jumps from stair 0 → 2 → 4:

* Jump from stair 0 to 2: cost = |50 − 30| = 20
* Jump from stair 2 to 4: cost = |40 − 50| = 10
  Total Cost = 20 + 10 = **30**

---

## ⚙️ Constraints

* (1 \leq height.size() \leq 10^5)
* (0 \leq height[i] \leq 10^4)

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Dynamic Programming
* Arrays
* Data Structures

---

## 📚 Related Articles

* [**Minimum Cost for Hopping Frog To Reach Stair N**](https://www.geeksforgeeks.org/minimum-cost-for-hopping-frog-to-reach-stair-n/)

---

---

awesome—using **your exact solution** as the primary one, here’s the full interview pack.

# 2) Text explanation + step-by-step dry run

## Problem in one line

You have `height[0..n-1]`. From stair `i`, you may jump to `i+1` or `i+2`.
Jump cost = `abs(height[j] - height[i])`.
Find the **minimum total cost** to reach `n-1` from `0`.

## DP idea (why it works)

Let `dp[i]` be the **minimum cost to reach stair `i`**.

* To land on `i`, last jump is either from `i-1` or `i-2`.
* Recurrence:

```
dp[0] = 0
dp[1] = |h1 - h0|
dp[i] = min(
    dp[i-1] + |hi - h(i-1)|,   # jump size 1
    dp[i-2] + |hi - h(i-2)|    # jump size 2
)
```

We only need the **previous two** `dp` values → **O(1)** space.

## Dry run (with your code)

Example: `height = [30, 20, 50, 10, 40]`

```
n=5
prev2 = dp[0] = 0
prev1 = dp[1] = |20-30| = 10

i=2:
  cost1 = prev1 + |50-20| = 10 + 30 = 40
  cost2 = prev2 + |50-30| = 0  + 20 = 20
  curr = 20
  shift → prev2=10, prev1=20

i=3:
  cost1 = prev1 + |10-50| = 20 + 40 = 60
  cost2 = prev2 + |10-20| = 10 + 10 = 20
  curr = 20
  shift → prev2=20, prev1=20

i=4:
  cost1 = prev1 + |40-10| = 20 + 30 = 50
  cost2 = prev2 + |40-50| = 20 + 10 = 30
  curr = 30
  shift → prev2=20, prev1=30

Answer = prev1 = 30  (path 0→2→4)
```

Edge cases: `n==0 or 1 → 0`; equal heights → some jumps cost `0`.
Large `n` is safe (iterative, no recursion).

---

# 3) Python solutions (brute ➜ memo ➜ tabulation ➜ your optimized)

All follow:

```python
class Solution:
    def minCost(self, height):
        # code here
```

### A) Brute recursion (teaching aid; exponential)

```python
class Solution:
    def minCost(self, height):
        # Time: O(2^n), Space: O(n) recursion
        n = len(height)

        def cost_to(i):
            if i == 0: return 0
            if i == 1: return abs(height[1] - height[0])
            jump1 = cost_to(i - 1) + abs(height[i] - height[i - 1])  # from i-1
            jump2 = cost_to(i - 2) + abs(height[i] - height[i - 2])  # from i-2
            return min(jump1, jump2)

        return cost_to(n - 1)
```

### B) Top-down DP (memoized recursion) — linear but recursive

```python
class Solution:
    def minCost(self, height):
        # Time: O(n), Space: O(n) memo + O(n) recursion
        from functools import lru_cache
        n = len(height)

        @lru_cache(None)
        def best(i):
            if i == 0: return 0
            if i == 1: return abs(height[1] - height[0])
            via1 = best(i - 1) + abs(height[i] - height[i - 1])
            via2 = best(i - 2) + abs(height[i] - height[i - 2])
            return min(via1, via2)

        return best(n - 1)
```

> Use this only if recursion depth won’t be an issue.

### C) Bottom-up tabulation — clear & iterative

```python
class Solution:
    def minCost(self, height):
        # Time: O(n), Space: O(n)
        n = len(height)
        if n <= 1: return 0
        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])
        for i in range(2, n):
            one = dp[i - 1] + abs(height[i] - height[i - 1])  # from i-1
            two = dp[i - 2] + abs(height[i] - height[i - 2])  # from i-2
            dp[i] = min(one, two)
        return dp[-1]
```

### D) **Your space-optimized solution (recommended)** — O(1) space

```python
from collections import deque  # (import not needed here, but kept to match your snippet)

class Solution:
    def minCost(self, height):
        """
        Time:  O(n)   (single pass)
        Space: O(1)   (keep only two previous dp values)
        """
        n = len(height)
        if n <= 1:
            return 0

        # dp[0] = 0, dp[1] = |h1 - h0|
        prev2 = 0
        prev1 = abs(height[1] - height[0])

        for i in range(2, n):
            cost1 = prev1 + abs(height[i] - height[i - 1])  # jump from i-1
            cost2 = prev2 + abs(height[i] - height[i - 2])  # jump from i-2
            curr = cost1 if cost1 < cost2 else cost2
            prev2, prev1 = prev1, curr  # slide window

        return prev1
```

---

# 4) Interview quick-recall + expected Q&A

## 10-sec mnemonic

**“1-2 DP, min of two.”**

* State: `dp[i] = min cost to reach i`.
* Transition: `min( from i-1, from i-2 )` with absolute height diffs.
* Keep **two** values (`prev2`, `prev1`), update in a loop.

## 5-line pseudo

```
dp0 = 0
if n == 1: return 0
dp1 = |h1 - h0|
for i in 2..n-1:
    dpi = min(dp1 + |hi - h(i-1)|, dp0 + |hi - h(i-2)|)
    dp0, dp1 = dp1, dpi
return dp1
```

## Likely Q&A

**Q1. Why DP (not greedy)?**
Local cheapest next jump may block a globally optimal route. Optimal substructure exists: best to `i` depends only on best to `i-1` and `i-2`.

**Q2. Recurrence & base cases?**
`dp[0]=0`, `dp[1]=|h1-h0|`, and for `i≥2`:
`dp[i]=min(dp[i-1]+|hi-h(i-1)|, dp[i-2]+|hi-h(i-2)|)`.

**Q3. Complexity?**
Time `O(n)`. Space `O(1)` with rolling two variables (or `O(n)` with full table).

**Q4. My recursive solution crashed on big inputs—why?**
Python recursion depth is ~1000. Use the **iterative** (space-optimized) version to avoid stack overflows.

**Q5. How to reconstruct the path?**
Keep a `parent[i]` storing which predecessor gave the min (i-1 or i-2), then backtrack from `n-1`.

**Q6. Variation: can jump up to `k` steps?**
`dp[i] = min_{1≤j≤k} dp[i-j] + |h[i]-h[i-j]|`.
Straightforward `O(k·n)`; further optimizations depend on cost structure.

---

---

# 5️⃣ Real-World Use Cases (Easily relatable to an interviewer)

These analogies connect the **Frog Jump DP** problem to everyday optimization scenarios:

| Real-World Example                          | How It Relates                                                                                                                  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Robot climbing uneven stairs / terrain**  | The robot must minimize energy difference between steps (like minimizing height difference cost).                               |
| **Packet routing with variable costs**      | A data packet hops through routers with different latencies; jumping 1 or 2 nodes ahead trades off immediate vs overall delay.  |
| **Video game pathfinding / platform jumps** | Game character chooses between small or long jumps to minimize total “stamina loss.”                                            |
| **Financial ladder (bond yield curves)**    | Choosing 1-step vs 2-step investments balancing short-term vs long-term cost or risk resembles minimizing total cost to a goal. |

👉 Interview tip: pick one that fits your interviewer’s domain (robotics, finance, etc.) and say:

> “It’s like an agent trying to reach a goal minimizing transition costs — each step cost depends on difference in state, so dynamic programming gives the globally minimal route.”

---

# 6️⃣ Full Python Program (with inline time/space complexity comments & timing)

Here’s the **final, optimized program** — fully annotated and runnable.

```python
from collections import deque
import time

class Solution:
    def minCost(self, height):
        """
        Frog Jump (min cost to reach last stair)
        ---------------------------------------
        Problem:
            height[i] = height of i-th stair.
            Frog can jump to i+1 or i+2 with cost = abs(height[j] - height[i]).
            Find minimum total cost to reach last stair.

        Approach:
            Dynamic Programming (Bottom-Up, Space Optimized)

        Transition:
            dp[i] = min(
                dp[i-1] + abs(height[i] - height[i-1]),
                dp[i-2] + abs(height[i] - height[i-2])
            )

        Time Complexity Analysis:
            - Building initial vars: O(1)
            - Single pass through n stairs: O(n)
              → Each iteration does constant work.
            TOTAL TIME = O(n)

        Space Complexity Analysis:
            - We keep only prev2, prev1, curr = O(1) auxiliary space
            - Input array = O(n)
            TOTAL SPACE = O(1) extra
        """

        n = len(height)
        if n <= 1:
            # Base case: no cost for one or zero stairs
            return 0

        # Base initialization
        # dp[0] = 0 → cost at starting stair
        # dp[1] = |h1 - h0|
        prev2 = 0
        prev1 = abs(height[1] - height[0])

        # Iterate from stair 2 to n-1
        for i in range(2, n):
            # Cost to reach i from previous stair (1 jump)
            cost1 = prev1 + abs(height[i] - height[i - 1])
            # Cost to reach i from two stairs before (2 jumps)
            cost2 = prev2 + abs(height[i] - height[i - 2])

            # Take the minimum of both paths
            curr = cost1 if cost1 < cost2 else cost2

            # Update rolling DP window
            prev2, prev1 = prev1, curr

        # Final minimum cost to reach last stair
        return prev1


# --------------------- MAIN PROGRAM ---------------------
if __name__ == "__main__":
    # Example input
    height = [30, 20, 50, 10, 40]
    print("Input heights:", height)

    start_time = time.time()  # start timing

    sol = Solution()
    min_cost = sol.minCost(height)  # function call

    end_time = time.time()  # end timing

    # Output
    print("Minimum Cost to Reach Last Stair:", min_cost)
    print(f"Execution Time: {end_time - start_time:.8f} seconds")
```

---

### ✅ Sample Run

**Input:**

```
height = [30, 20, 50, 10, 40]
```

**Console Output:**

```
Input heights: [30, 20, 50, 10, 40]
Minimum Cost to Reach Last Stair: 30
Execution Time: 0.00000238 seconds
```

---

### 🧠 Quick Summary (Interview Sheet)

| Concept        | Key Takeaway                                 |       |   |
| -------------- | -------------------------------------------- | ----- | - |
| **State**      | dp[i] = min cost to reach i                  |       |   |
| **Transition** | min of (1-jump, 2-jump)                      |       |   |
| **Base Cases** | dp[0]=0, dp[1]=                              | h1−h0 |   |
| **Time**       | O(n)                                         |       |   |
| **Space**      | O(1)                                         |       |   |
| **Mnemonic**   | “1-2 DP, min of two”                         |       |   |
| **Analogy**    | Robot on stairs minimizing energy difference |       |   |

---

---

