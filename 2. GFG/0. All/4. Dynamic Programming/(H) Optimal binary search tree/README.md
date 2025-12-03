# Optimal Binary Search Tree 🌳

**Difficulty:** Hard  
**Accuracy:** 50.02%  
**Submissions:** 12K+  
**Points:** 8  

---

## Problem Statement

You are given a set of distinct keys in sorted order, which is represented by **keys[]**.  
Each key `kᵢ` represents a data record that is accessed during a search operation.  

For all the keys, you are also given a frequency array **freq[]**, which denotes how many times key `kᵢ` is searched for.

The **cost** of accessing a key in a binary search tree is calculated by **multiplying** its access frequency by the **level** at which it appears in the tree. Therefore, different arrangements of keys in the BST give different total search costs.

Your task is to calculate the **minimum total search cost** required to construct a binary search tree containing all the keys.

> **Note:** Consider the root of the BST is at **level 1**.

---

## Examples

### Example 1

**Input:**  
`keys[] = [10, 12]`, `freq[] = [34, 50]`  

**Output:**  
`118`  

**Explanation:**  

There can be the following two possible BSTs:

1. Tree I (10 as root, 12 as right child):  

   - Cost of tree I = `34 * 1 + 50 * 2 = 134`

2. Tree II (12 as root, 10 as left child):  

   - Cost of tree II = `50 * 1 + 34 * 2 = 118`

Among these, the minimum cost is **118**.

---

### Example 2

**Input:**  
`keys[] = [10, 12, 20]`, `freq[] = [34, 8, 50]`  

**Output:**  
`142`  

**Explanation:**  

There can be many possible BSTs with keys `10`, `12`, `20`.  
Among all possible BSTs, the cost of the 5th BST (in the illustration) is minimum.

For that BST, the total search cost is:

\[
1 * 50 + 2 * 34 + 3 * 8 = 142
\]

So, the minimum possible cost is **142**.

---

## Constraints

- \( 1 \le \text{keys.size()} = \text{freq.size()} \le 100 \)  
- \( 1 \le \text{keys}[i], \text{freq}[i] \le 10^4 \)

---

## Expected Complexities

- **Time Complexity:** `O(n^3)`  
- **Auxiliary Space:** `O(n^2)`

---

## Topic Tags

- Dynamic Programming  
- Binary Search Tree  
- Data Structures  
- Algorithms  

---

## Related Articles

- Optimal Binary Search Tree Dp 24

---

---

Let’s go step by step.

---

## 2. Explanation + Step-by-Step Dry Run

### Problem in plain words

* We have sorted keys: `keys[0..n-1]`.
* Each key `keys[i]` is searched `freq[i]` times.
* If a key is at **level L** in the BST (root = level 1), its **cost contribution** is
  `freq[i] * L`.
* **Total cost** = sum of `freq[i] * level_of_key_i` for all keys.
* Different BST shapes (with the same in-order sequence) give different total costs.
* We must build a BST that has **minimum total search cost**.

---

### Important observation

If we pick key `keys[r]` as the **root** of some subtree that contains keys `keys[i..j]`:

* All keys in the **left subtree** are `keys[i..r-1]`.
* All keys in the **right subtree** are `keys[r+1..j]`.
* Whatever cost their subtrees had before, **every node in those subtrees moves down by 1 level** because we put a new root above them.

So:

* Let `cost_left` = total cost for an optimal BST built from keys `i..r-1` if its root were at level 1.
* Let `cost_right` = total cost for an optimal BST built from keys `r+1..j` if its root were at level 1.
* When this subtree is attached under some parent (one level deeper), **each node’s level increases by 1** → total cost of the subtree increases by **sum of frequencies in `i..j`**.

This leads to:

> **Cost of subtree `[i..j]` with root at `r`**
> = `cost_left + cost_right + sum(freq[i..j])`

Because:

* `cost_left` & `cost_right` assume root at level 1,
* but real level is +1 → every key in `[i..j]` gets `+freq[k]` added → that’s exactly `sum(freq[i..j])`.

So to get the **optimal** cost for keys `[i..j]`, we try **all possible roots `r` in `[i..j]`** and take the minimum.

---

### DP definition

Let:

> `dp[i][j]` = **minimum total cost** of an optimal BST built from keys `keys[i..j]`
> (assume its root is at level 1 inside this subtree)

Then:

* **Base case**: single key

  ```text
  dp[i][i] = freq[i]
  ```

  (that key is root → level 1 → cost = freq[i] * 1)

* **Transition** (for range `i..j`, `i < j`):

  ```text
  dp[i][j] = min over r in [i..j] of (
                dp[i][r-1]  +   # left subtree cost (0 if empty)
                dp[r+1][j]  +   # right subtree cost (0 if empty)
                sum(freq[i..j]) # all nodes go down by 1 level
            )
  ```

To make this efficient we precompute:

```text
prefixFreq[k] = freq[0] + freq[1] + ... + freq[k-1]
sum(i..j)     = prefixFreq[j+1] - prefixFreq[i]
```

Then we can compute `sum(freq[i..j])` in **O(1)**.

We fill `dp` by increasing segment length (gap = j-i).

---

### Dry run: `keys = [10, 12, 20]`, `freq = [34, 8, 50]`

We want the minimal total cost.

1. Precompute prefix sums of freq:

   ```text
   prefixFreq[0] = 0
   prefixFreq[1] = 34
   prefixFreq[2] = 34 + 8  = 42
   prefixFreq[3] = 42 + 50 = 92

   sum(i..j) = prefixFreq[j+1] - prefixFreq[i]
   ```

2. Initialize `dp[i][i] = freq[i]` (subarrays of length 1):

   ```text
   dp[0][0] = 34      # only key 10
   dp[1][1] = 8       # only key 12
   dp[2][2] = 50      # only key 20
   ```

3. Length = 2 (gap = 1)

   * Subarray `[0..1]` → keys `[10,12]`, sum of freq = `sum(0..1) = 42`.

     Try each root:

     * Root at `r = 0` (key 10):

       ```text
       left  = dp[0][-1] = 0   (empty)
       right = dp[1][1]  = 8
       cost  = left + right + sum(freq[0..1])
             = 0 + 8 + 42 = 50
       ```

     * Root at `r = 1` (key 12):

       ```text
       left  = dp[0][0] = 34
       right = dp[2][1] = 0   (empty)
       cost  = 34 + 0 + 42 = 76
       ```

     Min is `50` → `dp[0][1] = 50`.

   * Subarray `[1..2]` → keys `[12,20]`, sum = `sum(1..2) = 58`.

     * Root at `r = 1` (key 12):

       ```text
       left  = 0
       right = dp[2][2] = 50
       cost  = 0 + 50 + 58 = 108
       ```

     * Root at `r = 2` (key 20):

       ```text
       left  = dp[1][1] = 8
       right = 0
       cost  = 8 + 0 + 58 = 66
       ```

     Min is `66` → `dp[1][2] = 66`.

4. Length = 3 (gap = 2): full range `[0..2]`, sum = `sum(0..2) = 92`.

   Try roots:

   * Root `r = 0` (10):

     ```text
     left  = 0
     right = dp[1][2] = 66
     cost  = 0 + 66 + 92 = 158
     ```

   * Root `r = 1` (12):

     ```text
     left  = dp[0][0] = 34
     right = dp[2][2] = 50
     cost  = 34 + 50 + 92 = 176
     ```

   * Root `r = 2` (20):

     ```text
     left  = dp[0][1] = 50
     right = 0
     cost  = 50 + 0 + 92 = 142
     ```

   Minimum cost = **142** with root at 20, which matches the example.

---

## 3. Python Solutions

We’ll implement:

1. **Brute-force recursive** (clear but exponential).
2. **Optimized DP with memo (top-down)**.
3. **Optimized DP bottom-up with prefix sums** – this is what’s usually expected in interviews and matches `O(n³)` requirement.

Your function signature:

```python
class Solution:
    def minCost(self, keys, freq):
        # code here
```

### 3.1 Brute-force recursion (for understanding – exponential)

```python
class Solution:
    # ----- BRUTE FORCE (EXPLANATION-ONLY VERSION) -----
    def _minCostRecursive(self, freq, i, j):
        """
        Return minimum cost of optimal BST using keys in index range [i..j].
        Cost definition:
            - root is at level 1 in this subtree.
        This is pure recursion without memoization.

        Time complexity:
            Exponential in n (O(Catalan-like)), not suitable for n up to 100.
        Space complexity:
            O(n) recursion depth.
        """
        if i > j:
            return 0
        if i == j:
            # Only one key: cost = freq[i] * 1
            return freq[i]

        # Sum of frequencies freq[i..j]
        total_freq = sum(freq[i:j+1])

        min_cost = float('inf')
        # Try each key as root
        for r in range(i, j + 1):
            left_cost = self._minCostRecursive(freq, i, r - 1)
            right_cost = self._minCostRecursive(freq, r + 1, j)
            cost = left_cost + right_cost + total_freq
            min_cost = min(min_cost, cost)

        return min_cost
```

You wouldn’t submit this, but it’s a good “first idea”.

---

### 3.2 Optimized Top-Down DP (memoization + prefix sums)

```python
from functools import lru_cache

class Solution:
    def minCost_topdown(self, keys, freq):
        """
        Top-down DP with memoization for Optimal BST.

        Time  : O(n^3)   (n^2 states * O(n) roots per state)
        Space : O(n^2)   for memo table + O(n) recursion stack
        """
        n = len(keys)
        if n == 0:
            return 0

        # Precompute prefix sums of frequencies:
        # prefixFreq[i] = sum of freq[0..i-1]
        prefixFreq = [0] * (n + 1)
        for i in range(n):
            prefixFreq[i + 1] = prefixFreq[i] + freq[i]

        def range_sum(i, j):
            """Return sum of freq[i..j] in O(1)."""
            if i > j:
                return 0
            return prefixFreq[j + 1] - prefixFreq[i]

        @lru_cache(maxsize=None)
        def solve(i, j):
            """
            Minimum cost for optimal BST using keys[i..j],
            assuming root of this subtree is at level 1.
            """
            if i > j:
                return 0
            if i == j:
                return freq[i]  # single node at level 1

            total_freq = range_sum(i, j)
            best = float('inf')

            # Try each key[i..j] as root
            for r in range(i, j + 1):
                left_cost = solve(i, r - 1)
                right_cost = solve(r + 1, j)
                cost = left_cost + right_cost + total_freq
                if cost < best:
                    best = cost

            return best

        return solve(0, n - 1)
```

---

### 3.3 Optimized Bottom-Up DP (iterative, GFG-style)

This is usually what interviewers expect when they say “DP, O(n³)”:

```python
class Solution:
    def minCost(self, keys, freq):
        """
        Bottom-up DP for Optimal Binary Search Tree.

        keys: sorted list of keys (not actually used in cost formula here)
        freq: corresponding frequencies of each key

        We build dp[i][j] = min cost of optimal BST using keys[i..j],
        assuming root of this subtree is at level 1.

        Recurrence:
            dp[i][i] = freq[i]
            dp[i][j] = min over r in [i..j] of (
                            dp[i][r-1] + dp[r+1][j] + sum(freq[i..j])
                       )

        Implementation details:
        - We precompute prefix sums of freq to get sum(i..j) in O(1).
        - We fill dp by increasing segment length (gap).

        Complexity:
            Let n = len(keys)
            - Subproblems: n^2 (i,j)
            - For each (i,j): iterate r from i..j  => O(n)
            => Time  : O(n^3)
            => Space : O(n^2)
        """

        n = len(keys)
        if n == 0:
            return 0

        # Step 1: prefix sums of frequencies, O(n) time, O(n) space
        prefixFreq = [0] * (n + 1)
        for i in range(n):
            prefixFreq[i + 1] = prefixFreq[i] + freq[i]

        def range_sum(i, j):
            """Return sum of freq[i..j] in O(1)."""
            if i > j:
                return 0
            return prefixFreq[j + 1] - prefixFreq[i]

        # Step 2: initialize dp table, O(n^2) space
        dp = [[0] * n for _ in range(n)]

        # Base cases: single key
        for i in range(n):
            dp[i][i] = freq[i]

        # Step 3: fill for increasing lengths
        # gap = j - i
        for gap in range(1, n):  # gap = 1 means length 2, ..., n-1 means length n
            for i in range(0, n - gap):
                j = i + gap

                total_freq = range_sum(i, j)
                best = float('inf')

                # Try each key as root for interval [i..j]
                for r in range(i, j + 1):
                    left_cost = dp[i][r - 1] if r > i else 0
                    right_cost = dp[r + 1][j] if r < j else 0

                    cost = left_cost + right_cost + total_freq
                    if cost < best:
                        best = cost

                dp[i][j] = best

        return dp[0][n - 1]
```

This is the version you’d typically submit on GFG / LeetCode style platforms.

---

## 4. Interview Strategy: How to Remember & Q&A

### A. Quick memory hook

Two key sentences:

1. **“Interval DP on [i..j], try each root r, add sum(freq[i..j]).”**
2. **“Cost of subtree = left + right + sum(freq) because all nodes drop one level.”**

If you remember just this, you can reconstruct the recurrence.

---

### B. 5-line pseudo-code template

```text
compute prefixFreq[]
for i in 0..n-1: dp[i][i] = freq[i]
for len in 2..n:
    for i in 0..n-len:
        j = i + len - 1
        dp[i][j] = min over r in [i..j] of (
                       dp[i][r-1] + dp[r+1][j] + sumFreq(i..j)
                   )
return dp[0][n-1]
```

Where `sumFreq(i..j)` comes from prefix sums.

---

### C. Likely Interview Questions & Answers

---

**Q1: What is the brute-force solution and its complexity?**

**A:**
Try all BST shapes that preserve the in-order sequence. For each subarray `[i..j]`, try every key `r` as root and recursively build left and right trees. Without memoization, this leads to an exponential number of subproblems (similar to Catalan numbers) → not feasible for `n = 100`.

---

**Q2: What is your DP state and recurrence?**

**A:**
I define `dp[i][j]` as the minimum search cost of an optimal BST built from keys `keys[i..j]` with its root considered at level 1. Then:

* `dp[i][i] = freq[i]`
* For `i < j`:

  [
  dp[i][j] = \min_{r=i}^{j} \big( dp[i][r-1] + dp[r+1][j] + \text{sum}(freq[i..j]) \big)
  ]

The `sum(freq[i..j])` term accounts for all nodes in `[i..j]` shifting one level deeper when this subtree is attached under some parent.

---

**Q3: Why do you add `sum(freq[i..j])` for every root choice?**

**A:**
Consider the subtree `[i..j]` as a whole. If its root is at level 1 inside this subtree, all costs inside are computed correctly. When we attach this subtree one level under some parent in the full tree, **every key in `[i..j]` moves one level deeper**, adding `freq[k]` to its cost. Summed over k from i..j, this extra cost is exactly `sum(freq[i..j])`, independent of which key is chosen as root. So we add it once per interval.

---

**Q4: How do you achieve `O(n³)` time instead of recomputing sums every time?**

**A:**
If I recompute `sum(freq[i..j])` in a loop, that adds another factor of `O(n)` → `O(n⁴)`. Instead, I precompute prefix sums:

[
prefixFreq[p] = \sum_{k=0}^{p-1} freq[k]
]

Then:

[
sum(freq[i..j]) = prefixFreq[j+1] - prefixFreq[i]
]

in `O(1)`. Overall, there are `O(n²)` states `(i, j)` and for each we try `O(n)` roots, so time is `O(n³)`.

---

**Q5: What’s the space complexity and why?**

**A:**
We store an `n x n` DP table `dp[i][j]` for all intervals. That’s `O(n²)` space. We also store a prefix array of length `n+1`, which is `O(n)`. So total auxiliary space is `O(n²)`.

---

**Q6: How is this related to Huffman coding?**

**A:**
Both aim to minimize a weighted path length (frequency × depth), but:

* **Huffman** ignores the key ordering and can freely build an optimal prefix code tree in `O(n log n)`.
* **Optimal BST** must respect **sorted order of keys in in-order traversal**, so we cannot rearrange leaves arbitrarily; this constraint makes the problem need `O(n³)` DP rather than a greedy algorithm.

---

**Q7: How would you explain the algorithm in one sentence to a non-expert?**

**A:**
“Among all ways to choose a root between i and j, pick the one that gives the smallest total cost of left subtree + right subtree + total frequency of keys in that range, and compute this for every subrange using dynamic programming.”

---

If you rehearse:

> “`dp[i][j]`: optimal cost on interval, try each root, add `sum(freq[i..j])`.”

and keep the 5-line pseudo-code in mind, you’ll be able to derive the full code very quickly in an interview.

---

---

Nice, this is a great one to have in your toolbox.

---

## 5. Real-World Use Cases (easy to mention in interviews)

You can tie Optimal BST to places where **search frequency is skewed** and keys are in **sorted order**:

1. **Compiler Symbol Tables / Interpreters**

   * Identifiers (variable names, function names) are stored in a table.
   * Some identifiers are accessed far more often than others.
   * If you implement the table as a BST, arranging frequent identifiers near the root minimizes average lookup cost.
   * Optimal BST gives the **minimum possible expected search time** given known frequencies.

2. **Database Index Structures (when using ordered trees)**

   * A B-tree or BST-like index over sorted keys (e.g., product IDs).
   * If query statistics show some keys are accessed much more frequently, building an optimal BST for a small hot subset can reduce average disk/page reads.

3. **Dictionary / Autocomplete Engines**

   * Words are stored in sorted order.
   * Common words (“the”, “and”, etc.) have very high frequency.
   * An optimal BST over a small vocabulary or over prefix nodes makes frequent words appear at shallower depths, improving average lookup latency.

4. **Cache / Routing Tables in Networking**

   * Routing entries or cache entries (e.g., URLs) can be stored as ordered keys.
   * Access frequencies are often known or estimated.
   * An optimal BST layout can minimize average search steps in software routers or proxies.

When asked “Where is this useful?”, a compact answer:

> “Anywhere you have sorted keys with known query frequencies and want to minimize average lookup time — e.g., compiler symbol tables, small hot database indexes, or dictionary/autocomplete data structures.”

---

## 6. Full Python Program with Timing + Complexity Comments

This uses the **bottom-up DP with prefix sums** (`O(n³)` time, `O(n²)` space), plus a small driver to read input, run, and time the execution.

```python
import time


class Solution:
    def minCost(self, keys, freq):
        """
        Bottom-up DP for Optimal Binary Search Tree.

        keys: sorted list of distinct keys (not directly used in formula,
              but in real use they'd enforce order).
        freq: list of access frequencies corresponding to keys[i].

        We compute:
            dp[i][j] = minimum search cost of an optimal BST built from
                       keys[i..j], assuming the root of this subtree is at level 1.

        Recurrence:
            - Base: dp[i][i] = freq[i]
            - For i < j:
                dp[i][j] = min over r in [i..j] of:
                           dp[i][r-1] + dp[r+1][j] + sum(freq[i..j])

        Complexity:
            Let n = len(keys)
            - There are O(n^2) intervals (i, j)
            - For each interval we try up to O(n) roots r
            => Time  : O(n^3)
            - DP table size is n x n
            => Space : O(n^2)
        """

        n = len(keys)
        if n == 0:
            # No keys => no cost
            return 0

        # ------------- Step 1: Prefix sums of freq -------------
        # prefixFreq[i] = sum_{k = 0..i-1} freq[k]
        # Time: O(n), Space: O(n)
        prefixFreq = [0] * (n + 1)
        for i in range(n):  # O(n)
            prefixFreq[i + 1] = prefixFreq[i] + freq[i]

        def range_sum(i, j):
            """
            Return sum(freq[i..j]) in O(1) using prefix sums.

            Time per call: O(1)
            """
            if i > j:
                return 0
            return prefixFreq[j + 1] - prefixFreq[i]

        # ------------- Step 2: DP table initialization -------------
        # dp is an n x n table; we only use i <= j
        # Time to allocate: O(n^2)
        # Space: O(n^2)
        dp = [[0] * n for _ in range(n)]

        # Base case: single key trees
        # dp[i][i] = freq[i] * level(=1) = freq[i]
        # Time: O(n)
        for i in range(n):
            dp[i][i] = freq[i]

        # ------------- Step 3: Fill DP for increasing lengths -------------
        # 'gap' = j - i, so gap = 1 => length 2, ..., gap = n-1 => length n.
        #
        # Outer loop over gaps: O(n)
        for gap in range(1, n):
            # For each starting index i (0-based) such that j = i + gap < n
            # This nested loop over i: total O(n^2) across all gaps
            for i in range(0, n - gap):
                j = i + gap

                # Total freq of this interval; added once for all roots
                # Time per call: O(1), overall: O(n^2)
                total_freq = range_sum(i, j)

                best_cost = float('inf')

                # Try each key in i..j as root: O(n) per interval
                for r in range(i, j + 1):
                    # Cost of left subtree if it exists, else 0
                    left_cost = dp[i][r - 1] if r > i else 0
                    # Cost of right subtree if it exists, else 0
                    right_cost = dp[r + 1][j] if r < j else 0

                    # Every node in [i..j] moves one level deeper when we
                    # attach this subtree, so we add total_freq.
                    current_cost = left_cost + right_cost + total_freq

                    if current_cost < best_cost:
                        best_cost = current_cost

                # Final optimal cost for interval [i..j]
                dp[i][j] = best_cost

        # Answer is optimal cost for interval covering all keys [0..n-1]
        return dp[0][n - 1]


# ---------------------- Driver + Timing ---------------------- #

def main():
    """
    Driver code to:
    - Read input.
    - Call Solution().minCost().
    - Print result and timing.

    Expected input format (simple, competitive style):

        n
        k0 k1 k2 ... k(n-1)
        f0 f1 f2 ... f(n-1)

    Example:
        3
        10 12 20
        34 8 50

    Complexity of main (excluding DP):
        - Reading n: O(1)
        - Reading keys & freq: O(n)
        - Printing output: O(1)
    """

    print("Enter number of keys n:")
    line = input().strip()
    if not line:
        print("No input provided.")
        return
    n = int(line)

    print(f"Enter {n} sorted keys:")
    keys = list(map(int, input().split()))
    if len(keys) != n:
        keys = keys[:n]  # defensive slice

    print(f"Enter {n} frequencies:")
    freq = list(map(int, input().split()))
    if len(freq) != n:
        freq = freq[:n]

    solver = Solution()

    # Start timing just before the main algorithm.
    start_time = time.perf_counter()

    # Core algorithm: O(n^3) time, O(n^2) space.
    answer = solver.minCost(keys, freq)

    end_time = time.perf_counter()

    print("\nMinimum total search cost (Optimal BST):", answer)
    print(f"Total elapsed time (seconds): {end_time - start_time:.6f}")


if __name__ == "__main__":
    main()
```

### Sample run (mentally)

Input:

```text
3
10 12 20
34 8 50
```

Output will be roughly:

```text
Enter number of keys n:
3
Enter 3 sorted keys:
10 12 20
Enter 3 frequencies:
34 8 50

Minimum total search cost (Optimal BST): 142
Total elapsed time (seconds): 0.0000xx
```

You can use exactly this structure for local practice; in a platform / interview you’d usually only paste the `Solution` class with `minCost`, but having the full program plus timing is very handy to test and internalize the algorithm.

---

---

Gotcha—let’s bundle this cleanly for Optimal BST.

---

## 5. Real-World Use Cases (short, interviewer-friendly)

You want places where:

* Keys are **sorted**, and
* You know or can estimate **search frequencies**.

Here are a few good ones to mention:

1. **Compiler / Interpreter Symbol Tables**

   * Identifiers (variables, functions) are keys.
   * Some are looked up far more often (e.g., loop counters, common library calls).
   * If the symbol table is implemented as a BST, arranging frequently used identifiers closer to the root minimizes average lookup time.
     ➜ Optimal BST gives the *best possible* average lookup cost given those frequencies.

2. **Small Hot Indexes in Databases**

   * Think of a small in-memory index for hot rows (e.g., top-selling products).
   * Keys are sorted (IDs, timestamps), and query frequencies are known from logs.
   * Building an Optimal BST for this hot set reduces average query latency for that index.

3. **Dictionary / Autocomplete Lookups**

   * Words (or prefixes) kept in sorted order.
   * Very common words like “the”, “and”, “of” have much higher frequency.
   * Using an Optimal BST ensures high-frequency words sit near the root, improving average query time for text editors / IDEs / search boxes.

A compact way to say it:

> “Optimal BST is useful whenever you have sorted keys with known query frequencies and want to minimize average lookup cost—like compiler symbol tables, hot database indexes, or word dictionaries for autocomplete.”

---

## 6. Full Python Program (with timing + inline complexity comments)

This is a full, runnable script using the standard **bottom-up DP with prefix sums** (`O(n³)` time, `O(n²)` space) plus a simple input/output and timing harness.

```python
import time


class Solution:
    def minCost(self, keys, freq):
        """
        Compute the minimum total search cost of an Optimal Binary Search Tree.

        keys: sorted list of distinct keys (their order matters but not used directly)
        freq: list where freq[i] is the search frequency of keys[i]

        DP idea:
            dp[i][j] = minimum cost of an optimal BST built from keys[i..j],
                       assuming the root of this subtree is at level 1.

        Recurrence:
            Base: dp[i][i] = freq[i]
            For i < j:
                dp[i][j] = min over r in [i..j] (
                                dp[i][r-1] + dp[r+1][j] + sum(freq[i..j])
                            )

        Complexity:
            Let n = len(keys)
            States: O(n^2) intervals (i, j)
            For each (i, j), we try O(n) roots r
            => Time  : O(n^3)
            => Space : O(n^2) for the dp table
        """

        n = len(keys)
        if n == 0:
            # No keys => no cost
            return 0

        # -------- Step 1: Prefix sums for freq (to get range sums in O(1)) --------
        # prefixFreq[i] = sum of freq[0..i-1]
        # Time: O(n), Space: O(n)
        prefixFreq = [0] * (n + 1)
        for i in range(n):  # O(n)
            prefixFreq[i + 1] = prefixFreq[i] + freq[i]

        def range_sum(i, j):
            """
            Return sum(freq[i..j]) in O(1) using prefix sums.

            Time per call: O(1)
            """
            if i > j:
                return 0
            return prefixFreq[j + 1] - prefixFreq[i]

        # -------- Step 2: Allocate DP table --------
        # dp[i][j] will store minimal cost for keys[i..j].
        # Only i <= j are meaningful.
        # Time to allocate: O(n^2), Space: O(n^2)
        dp = [[0] * n for _ in range(n)]

        # Base case: single-key subtrees
        # dp[i][i] = freq[i] (key is root at level 1)
        # Time: O(n)
        for i in range(n):
            dp[i][i] = freq[i]

        # -------- Step 3: Fill DP for increasing interval lengths --------
        # 'gap' represents (j - i):
        #   gap = 1  => length 2
        #   gap = 2  => length 3, ... , gap = n-1 => length n
        #
        # Outer loop gap: O(n)
        for gap in range(1, n):
            # Inner loop i: across all gaps, total O(n^2) pairs (i, j)
            for i in range(0, n - gap):
                j = i + gap

                # Sum of frequencies freq[i..j], used in every root choice
                # Time: O(1) per interval, so O(n^2) overall
                total_freq = range_sum(i, j)

                best_cost = float('inf')

                # Try each key r in [i..j] as root: O(n) per interval
                for r in range(i, j + 1):
                    # Cost of left subtree (empty if r == i)
                    left_cost = dp[i][r - 1] if r > i else 0
                    # Cost of right subtree (empty if r == j)
                    right_cost = dp[r + 1][j] if r < j else 0

                    # All nodes in [i..j] move one level deeper when this
                    # subtree is attached up, so we add total_freq.
                    current = left_cost + right_cost + total_freq

                    if current < best_cost:
                        best_cost = current

                # Record the optimal cost for interval [i..j]
                dp[i][j] = best_cost

        # Final answer: optimal cost for entire range [0..n-1]
        return dp[0][n - 1]


# ---------------- Driver with timing ---------------- #

def main():
    """
    Simple driver:

    Input format:
        n
        k0 k1 k2 ... k(n-1)
        f0 f1 f2 ... f(n-1)

    Example:
        3
        10 12 20
        34 8 50

    Overall complexity of this function (excluding DP):
        - Reading input: O(n)
        - Printing results: O(1)
    """

    print("Enter number of keys n:")
    line = input().strip()
    if not line:
        print("No input provided.")
        return
    n = int(line)

    print(f"Enter {n} sorted keys:")
    keys = list(map(int, input().split()))
    if len(keys) != n:
        keys = keys[:n]  # defensive trim if needed

    print(f"Enter {n} frequencies:")
    freq = list(map(int, input().split()))
    if len(freq) != n:
        freq = freq[:n]

    solver = Solution()

    # Start timing right before calling the algorithm
    start_time = time.perf_counter()

    # Core algorithm: O(n^3) time, O(n^2) space
    result = solver.minCost(keys, freq)

    # Stop timing after computation
    end_time = time.perf_counter()

    print("\nMinimum total search cost (Optimal BST):", result)
    print(f"Total elapsed time (seconds): {end_time - start_time:.6f}")


if __name__ == "__main__":
    main()
```

### Example run (conceptual)

Input:

```text
3
10 12 20
34 8 50
```

Output:

```text
Enter number of keys n:
3
Enter 3 sorted keys:
10 12 20
Enter 3 frequencies:
34 8 50

Minimum total search cost (Optimal BST): 142
Total elapsed time (seconds): 0.0000xx
```

You can use this exact script to practice; in the actual interview / online judge you’d typically just drop the `Solution` class with `minCost`, but having this full, timed version helps you internalize both performance and behavior.
