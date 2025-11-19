
---

# **Make Strings Equal**

**Difficulty:** Medium
**Accuracy:** 0.0%
**Submissions:** 0
**Points:** 4

---

## **Problem Statement**

You are given two strings **s** and **t**, consisting of lowercase English letters.
You are also given:

* A 2D array **transform[][]** of size `n × 2`, where each entry `[x, y]` means that you are allowed to transform character **x** into character **y**.
* An array **cost[]**, where `cost[i]` is the cost of transforming `transform[i][0]` into `transform[i][1]`.

You can apply any transformation **any number of times** on either string.

Your task is to find the **minimum total cost** required to make the two strings **identical**.

If it is **impossible** to make the two strings identical using the available transformations, return **-1**.

---

## **Examples**

---

### **Example 1**

**Input:**

```
s = "abcc",  
t = "bbcc",  
transform[][] = [['a', 'b'], ['b', 'c'], ['c', 'a']],  
cost[] = [2, 1, 4]
```

**Output:**

```
3
```

**Explanation:**
We can convert both strings into `"bbcc"` with a cost of 3 using these operations:

* Transform at Position 0 in s: `a -> b` (cost 2)
* Transform at Position 1 in s: `b -> c` (cost 1)

Other characters already match.

---

### **Example 2**

**Input:**

```
s = "az",  
t = "dc",  
transform[][] = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['a', 'd'], ['z', 'c']],  
cost[] = [5, 3, 2, 50, 10]
```

**Output:**

```
20
```

**Explanation:**
We can convert both strings into `"dc"` with a cost of 20 using these operations:

* Transform at Position 0 in s: `a -> d` by path `a -> b -> c -> d`
  Total cost = `5 + 3 + 2 = 10`
* Transform at Position 1 in s: `z -> c` (cost 10)

Total = `10 + 10 = 20`.

---

### **Example 3**

**Input:**

```
s = "xyz",  
t = "xzy",  
transform[][] = [['x', 'y'], ['x', 'z']],  
cost[] = [3, 3]
```

**Output:**

```
-1
```

**Explanation:**
It is not possible to make the two strings equal.

---

## **Constraints**

* `1 ≤ s.size() = t.size() ≤ 10⁵`
* `1 ≤ transform.size() = cost.size() ≤ 500`
* `'a' ≤ transform[i][0], transform[i][1] ≤ 'z'`
* `1 ≤ cost[i] ≤ 500`

---

## **Expected Complexities**

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## **Topic Tags**

* Graph
* Shortest Path
* Algorithms

---

---

I’ll structure this as:

1. Intuition + step-by-step dry run
2. Optimized Python solutions (two flavors) in your requested format
3. How to remember in interviews (mnemonics)
4. Likely interviewer Q&A

---

## 2. Intuition + Step-by-Step Explanation

### Problem in my own words

* We have two same-length strings `s` and `t`.
* We can transform characters using directed rules:
  `transform[i] = [x, y]` with cost `cost[i]` means we can change `x -> y` paying `cost[i]`.
* We can apply any transformations, any number of times, on any positions of `s` or `t`.
* Goal: **make `s` and `t` identical** with **minimum total cost**.
* If impossible → return `-1`.

Key observation:

For each index `i`, we have characters `s[i]` and `t[i]`.
We’re allowed to transform them along some paths in a **graph of characters** (26 letters).
We want to make them both some **same letter `c`**, possibly different from both.

So for a fixed position:

> Cost(i) =
> min over all letters `c`
> (cost to transform `s[i] -> c`) + (cost to transform `t[i] -> c`)

If for all `c` either `s[i] -> c` or `t[i] -> c` is impossible, then strings can’t be made equal at all.

So the global problem becomes:

1. For **every pair of letters** `(x, y)` we need to know:

   * the cheapest way to transform `x` into `y` (possibly through intermediates).
2. Then for each position `i`, compute `min_c dist[s[i]][c] + dist[t[i]][c]`, and sum over all `i`.

This is a classic **all-pairs shortest path on a 26-node directed weighted graph**.

---

### How to compute all-pairs shortest paths?

Since we only have 26 letters, the graph is tiny.

Two common ways:

1. **Floyd–Warshall**: DP over all triples (k, i, j) → O(26³) = constant.
2. **Run Dijkstra from every letter**: 26 times Dijkstra → also small.

In interviews, **Floyd–Warshall** is very clean here.

---

### Step-by-step dry run (Example 1)

Example:

```txt
s = "abcc"
t = "bbcc"
transform = [['a', 'b'], ['b', 'c'], ['c', 'a']]
cost     = [      2     ,      1     ,      4    ]
```

We want minimum cost to make both strings equal.

#### Step 1: Build graph of letters

Vertices: 26 letters `a..z`.

Directed edges:

* `a -> b` cost 2
* `b -> c` cost 1
* `c -> a` cost 4

We’ll keep a 26×26 matrix `dist[char_from][char_to]`:

* Initialize:

  * `dist[x][x] = 0` for all letters.
  * `dist[x][y] = +inf` for `x != y`.
* For each transform edge `x -> y` with `cost`:

  * `dist[x][y] = min(dist[x][y], cost)` (if multiple edges).

After initialization for relevant letters:

```
    a   b   c
a [ 0,  2, inf]
b [inf, 0,  1 ]
c [ 4, inf, 0 ]
```

All others letters just have 0 to itself and inf to others.

#### Step 2: Floyd–Warshall

We relax through intermediate letters `k`:

For every `k` in all 26 letters:
for every `i`, `j`:
`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

We only care about a,b,c, but logic applies to all.

Use `k = a`:

* Check if we can improve paths via `a`.

Example: `b -> a`:

* Currently `dist[b][a] = inf`
* Via `a`: `dist[b][a]` ?= `dist[b][a]` vs `dist[b][a] + dist[a][a] = inf` → no change.

`c -> b` via `a`:

* `dist[c][b]` ?= `dist[c][a] + dist[a][b] = 4 + 2 = 6`
* So `dist[c][b] = 6`.

Continue similarly for `k=b`, `k=c`.

You’ll eventually get (for letters a,b,c):

```
    a   b   c
a [ 0,  2,  3 ]   # a->c can be a->b->c with cost 2+1=3
b [ 5,  0,  1 ]   # b->a: b->c->a cost 1+4=5
c [ 4,  6,  0 ]   # c->b: c->a->b cost 4+2=6
```

So now for ANY pair (x,y) we know cheapest cost to convert x→y.

#### Step 3: Process each position

We’ll loop i = 0..3.

We also set: if `s[i] == t[i]`, cost can be 0 without transformations.

---

##### Position i = 0

* `s[0] = 'a'`
* `t[0] = 'b'`

We try all letters `c` from `'a'..'z'` and compute:

`dist['a'][c] + dist['b'][c]`, take the min.

Check relevant c:

* c = 'a':

  * `a->a`: 0
  * `b->a`: 5
  * total = 5
* c = 'b':

  * `a->b`: 2
  * `b->b`: 0
  * total = 2   ✅ (best so far)
* c = 'c':

  * `a->c`: 3
  * `b->c`: 1
  * total = 4

Best is **2** (convert both to `'b'`).

Effectively we’ll transform s[0]: `a -> b` cost 2; leave t[0] as `'b'`.

---

##### Position i = 1

* `s[1] = 'b'`
* `t[1] = 'b'`

Already equal → cost 0 (best is just c = 'b').

---

##### Positions i = 2,3

* `s[2]='c', t[2]='c'`
* `s[3]='c', t[3]='c'`

Already equal, cost 0 each.

---

#### Step 4: Sum

Total cost = 2 + 0 + 0 + 0 = **2**.

But the example output in the prompt was **3** because they chose to convert to `"bbcc"` via:

* pos0: a->b cost 2
* pos1: b->c cost 1

That’s a *valid* solution, but **not minimal** under the given transforms we calculated with a->b, b->c, c->a costs. The description in the screenshot is slightly loose; the key is:

> Our algorithm always finds the *true* minimum by checking all common target letters `c`.

(In their example constraints they might not allow using transform on `t`, only `s`, but the core algorithm you’ll give in interviews is what we’ve derived.)

---

## 3. Optimized Python Solutions

We’ll implement:

1. **Floyd–Warshall** (recommended / clean answer)
2. **Alternative: Dijkstra-from-each-letter** (also valid in interviews)

Both in your required format:

```python
class Solution:
    def minCost(self, s, t, transform, cost):
        # code here
```

---

### 3.1 Floyd–Warshall Solution (recommended)

```python
from typing import List

class Solution:
    def minCost(self, s: str, t: str,
                transform: List[List[str]],
                cost: List[int]) -> int:
        """
        Make strings s and t equal with minimum total transformation cost.

        Approach:
        ---------
        1) Model 26 letters as nodes in a directed weighted graph.
           Edge (x -> y) with weight w means we can transform x into y with cost w.
        2) Run Floyd–Warshall to compute all-pairs shortest paths on this 26-node graph.
           dist[u][v] = minimal cost to transform char u into char v.
        3) For each index i, compute:
               best_cost_i = min over c ( dist[s[i]][c] + dist[t[i]][c] )
           Sum all best_cost_i. If for some i all paths are impossible,
           return -1.

        Time Complexity:
            - Building dist:     O(#transforms)  ≤ 500
            - Floyd–Warshall:   O(26^3) ≈ constant
            - Per-character sum: O(n * 26)
            => Overall: O(n * 26) ~ O(n)
        Space Complexity:
            - dist matrix: O(26^2) (constant)
        """

        n = len(s)
        if n != len(t):
            # Problem states they are equal, but we guard anyway
            return -1

        ALPHABET = 26
        INF = 10**18  # large enough

        # Helper to map 'a'..'z' -> 0..25
        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        # 1) Initialize distance matrix
        #    dist[u][v] = minimal cost to go u -> v
        dist = [[INF] * ALPHABET for _ in range(ALPHABET)]

        # Zero cost from a letter to itself
        for u in range(ALPHABET):
            dist[u][u] = 0

        # Add direct transformation edges
        # Multiple edges between same pair: keep the cheapest.
        for (x, y), w in zip(transform, cost):
            u = idx(x)
            v = idx(y)
            if w < dist[u][v]:
                dist[u][v] = w

        # 2) Floyd–Warshall: try all intermediate letters k
        #    For each triple (i, j, k):
        #        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        #
        #    Time: O(26^3) ~ constant
        for k in range(ALPHABET):
            dk = dist[k]   # small micro-optimization (row reference)
            for i in range(ALPHABET):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                # Relax edges i -> j via k
                for j in range(ALPHABET):
                    via_k = dik + dk[j]
                    if via_k < di[j]:
                        di[j] = via_k

        # 3) For each position i in strings:
        #       if s[i] == t[i], cost_i = 0 (already equal)
        #       else:
        #           best_i = min_c dist[s[i]][c] + dist[t[i]][c]
        #           if best_i == INF, impossible -> return -1
        total_cost = 0

        for i in range(n):
            ch_s = s[i]
            ch_t = t[i]

            if ch_s == ch_t:
                # No cost needed; we can just keep both as they are.
                continue

            u = idx(ch_s)
            v = idx(ch_t)

            best_here = INF

            # Try all possible target letters c (0..25)
            for c in range(ALPHABET):
                cost_s_to_c = dist[u][c]
                cost_t_to_c = dist[v][c]
                if cost_s_to_c == INF or cost_t_to_c == INF:
                    # At least one is impossible -> skip this c
                    continue
                candidate = cost_s_to_c + cost_t_to_c
                if candidate < best_here:
                    best_here = candidate

            if best_here == INF:
                # There is no common letter we can transform both into.
                return -1

            total_cost += best_here

        return total_cost
```

---

### 3.2 Alternative: Dijkstra from Each Letter

Instead of Floyd–Warshall, we can:

* Build adjacency list `graph[26]`.
* For each letter `u` in `a..z`, run Dijkstra to get shortest cost `dist[u][*]`.
* Complexity is still small, but conceptually “brute-ish” compared to Floyd.

```python
from typing import List
import heapq

class SolutionDijkstra:
    def minCost(self, s: str, t: str,
                transform: List[List[str]],
                cost: List[int]) -> int:
        """
        Alternative solution using repeated Dijkstra.

        Steps:
        ------
        1) Build adjacency list for the 26-letter graph.
        2) For each letter u, run Dijkstra to compute dist[u][*].
        3) Same per-position logic as in the Floyd–Warshall solution.

        Time Complexity:
            - For each of 26 sources, Dijkstra:
              O( E log V ) where E ≤ #transforms ≤ 500, V = 26
              => about 26 * 500 * log(26) ~ tiny constant
            - Per-character processing: O(n * 26)
            => Total ~ O(n * 26) ~ O(n)
        """

        n = len(s)
        if n != len(t):
            return -1

        ALPHABET = 26
        INF = 10**18

        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        # 1) Build adjacency list: graph[u] = list of (v, w)
        graph = [[] for _ in range(ALPHABET)]
        for (x, y), w in zip(transform, cost):
            u = idx(x)
            v = idx(y)
            graph[u].append((v, w))

        # 2) All-pairs shortest paths via Dijkstra per source letter
        dist = [[INF] * ALPHABET for _ in range(ALPHABET)]

        for src in range(ALPHABET):
            # Dijkstra from src
            dist[src][src] = 0
            heap = [(0, src)]  # (current_cost, node)

            while heap:
                curr_cost, u = heapq.heappop(heap)
                if curr_cost > dist[src][u]:
                    continue

                for v, w in graph[u]:
                    new_cost = curr_cost + w
                    if new_cost < dist[src][v]:
                        dist[src][v] = new_cost
                        heapq.heappush(heap, (new_cost, v))

        # 3) Same per-position accumulation as before
        total_cost = 0

        for i in range(n):
            if s[i] == t[i]:
                continue

            u = idx(s[i])
            v = idx(t[i])

            best_here = INF
            for c in range(ALPHABET):
                if dist[u][c] == INF or dist[v][c] == INF:
                    continue
                candidate = dist[u][c] + dist[v][c]
                if candidate < best_here:
                    best_here = candidate

            if best_here == INF:
                return -1

            total_cost += best_here

        return total_cost
```

Either of these is completely acceptable in an interview.
I’d **lead** with Floyd–Warshall because it’s mathematically neat and tiny.

---

## 4. Interview Memory Trick + Expected Q&A

### 4.1 3-Step Mental Template (to recall quickly)

Think of the problem as:

> **Char Graph → All-Pairs Shortest Path → Per-Index Merge**

Use this 3-word mnemonic: **“Graph → AllPairs → Merge”**

1. **Graph**

   * 26 nodes, edges from transforms.
2. **AllPairs**

   * Run Floyd–Warshall or 26×Dijkstra to get `dist[u][v]`.
3. **Merge**

   * For each index `i`, try every letter `c` as meeting point:
     `min_c dist[s[i]][c] + dist[t[i]][c]`.

### 60-second explanation you can say out loud

> “We have transformations between letters with costs, applied any number of times.
> So I treat each letter ‘a’..‘z’ as a graph node, with edges for the transforms.
> I compute all-pairs shortest paths on this 26-node graph using Floyd–Warshall.
> Then for each position i, I choose the best target letter c that both s[i] and t[i] can reach, minimizing dist[s[i]][c] + dist[t[i]][c].
> I sum that over all positions; if for some i there is no reachable c, I return −1.”

Say that, and then start coding.

---

### 4.2 Likely Interview Questions & Answers

---

**Q1. Why do you use Floyd–Warshall / all-pairs shortest path?**

> Because we need the cheapest way to transform **any letter to any other letter**, not just from one specific source. There are only 26 letters, so computing all-pairs shortest paths in O(26³) is effectively constant time. After that, each index of the string can be processed in O(26), choosing the best common target letter.

---

**Q2. What is the overall time and space complexity?**

> * Building the transform graph: O(#transforms)
> * Floyd–Warshall: O(26³) (constant)
> * For each of n positions, we scan 26 letters → O(26n)
>   So overall time is O(n).
>   Space: O(26²) for the distance matrix → constant.

---

**Q3. What if there is no way to transform a character to match?**

> In the distance matrix, those are stored as infinity.
> For an index `i`, if for every letter `c`, at least one of `dist[s[i]][c]` or `dist[t[i]][c]` is infinity, then there is no common letter they can become. In that case, we immediately return −1.

---

**Q4. Are transformations symmetric? If you can do x→y, can you also do y→x?**

> No, they are **directed**.
> `[x, y]` only allows `x -> y` at given cost, not `y -> x` unless another rule explicitly says so. The graph is directed; Floyd–Warshall/Dijkstra handle directed edges naturally.

---

**Q5. Why not just transform both characters directly into each other?**

> Sometimes going through a third letter is cheaper.
> Example: a→b cost 100, a→c cost 1, c→b cost 1.
> The cheapest way for `a` and `b` to become equal is to transform `b` to `a` through `c` or both to `c`, not directly.
> That’s why we need shortest paths in the graph, not just direct edges.

---

**Q6. Could you precompute best cost for each pair (x, y) once?**

> Yes. After we have `dist[u][v]`, for each pair `(x, y)` we can precompute:
>
> ```text
> bestMerge[x][y] = min_c ( dist[x][c] + dist[y][c] )
> ```
>
> That’s 26³ operations, still constant. Then each index lookup becomes O(1).
> But this micro-optimization isn’t necessary; both are O(n) overall.

---

**Q7. What changes if we had uppercase + lowercase (52 letters)?**

> The algorithm is identical; we just have 52 nodes instead of 26.
> Floyd–Warshall becomes O(52³), still very small (~140k operations).
> Only the char→index mapping changes.

---

---

Let’s finish this one cleanly.

---

## 5. Real-World Use Cases (easy to talk about)

Think in terms of **“mapping symbols with costs”**.

### a) Keyboard Layout Remapping / Typo Normalization

* Different users type the same word with different nearby keys or layouts (QWERTY vs AZERTY).
* Each key substitution has a **cost** proportional to how far the fingers move or how error-prone it is.
* We want to **normalize** two versions of a typed word to the **same canonical spelling** with **minimum total correction cost**.
* Characters = keys; transforms = allowed key corrections; cost = penalty for each substitution.

---

### b) Migrating Between Legacy Encodings / Abbreviations

* Suppose old systems store text using legacy abbreviations (`u` → `you`, `r` → `are`, etc.), and a new system uses different ones.
* Each replacement has a cost (CPU time, memory, risk of ambiguity).
* We want to **standardize two strings** coming from different sources to be identical with **minimal total conversion effort**.
* Characters = tokens / abbrev codes; directed transforms = allowed conversions with different costs.

---

### c) DNA / Protein Editing with Different Mutation Costs

* Each character is a base (`A,C,G,T`) or amino acid.
* Some mutations are **easy** (cheap) and some are **rare or risky** (expensive).
* When comparing two sequences from different experiments, we may want to **mutate both sequences** to a common “consensus” with minimal total mutation cost.
* Characters = nucleotides; transform graph = allowed mutations; cost = energy/risk.

These examples map nicely to:

> “Letters are nodes, transformations are directed edges with costs; we find cheapest ways to normalize two sequences.”

---

## 6. Full Python Program with Timing & Complexity Comments

This is a **standalone script**:

* Uses **Floyd–Warshall** (all-pairs shortest path on 26 letters).
* Contains **inline comments** about time and space at each major step.
* Uses a sample input (Example 2) and **times the run** with `timeit.default_timer`.

```python
"""
Make Strings Equal - Full Program with Timing

Given two strings s and t, and a set of directed letter transformations with costs,
find the minimum total cost to make the strings identical, or -1 if impossible.

Algorithm:
    - Build a 26x26 cost matrix for letters 'a'..'z' (graph of transformations).
    - Run Floyd–Warshall to compute all-pairs shortest paths on this tiny graph.
    - For each index i, choose the best target letter c that both s[i] and t[i]
      can be transformed into; sum their minimal costs.

Overall Complexity:
    - Floyd–Warshall: O(26^3) ≈ constant.
    - Per-position processing: O(n * 26) = O(n).
    - Space: O(26^2) = constant.
"""

from typing import List
from timeit import default_timer as timer


class Solution:
    def minCost(self, s: str, t: str,
                transform: List[List[str]],
                cost: List[int]) -> int:
        """
        Compute minimum cost to make strings s and t equal.

        Parameters
        ----------
        s, t : str
            Input strings (same length).
        transform : List[List[str]]
            Each [x, y] means we can transform x -> y.
        cost : List[int]
            cost[i] is the cost of transform[i].

        Returns
        -------
        int
            Minimum total cost, or -1 if impossible.

        Time Complexity (high level)
        ----------------------------
        - Build cost matrix:  O(#transforms)
        - Floyd–Warshall:     O(26^3)  (constant)
        - Per character:      O(n * 26)
        => Overall:           O(n)

        Space Complexity
        ----------------
        - Distance matrix: O(26^2)  (constant)
        """

        n = len(s)
        if n != len(t):
            # Problem states s and t have same size, but safe-guard anyway.
            return -1

        ALPHABET = 26
        INF = 10**18

        # Helper: map 'a'..'z' -> 0..25 (O(1))
        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        # -------------------------------------------------------------
        # 1) Initialize distance matrix dist[u][v]
        #    dist[u][v] = minimal cost to transform letter u into letter v.
        #
        #    Time:  O(26^2) to init (constant)
        #    Space: O(26^2)
        # -------------------------------------------------------------
        dist = [[INF] * ALPHABET for _ in range(ALPHABET)]

        # Zero cost to stay the same: u -> u
        for u in range(ALPHABET):
            dist[u][u] = 0

        # Fill direct transform edges from input
        # Time: O(#transforms) ≤ 500
        for (x, y), w in zip(transform, cost):
            u = idx(x)
            v = idx(y)
            # Keep the cheapest direct edge if duplicates appear
            if w < dist[u][v]:
                dist[u][v] = w

        # -------------------------------------------------------------
        # 2) Floyd–Warshall algorithm: Relax all-pairs shortest paths.
        #
        #    for k in letters:
        #      for i in letters:
        #        for j in letters:
        #          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        #
        #    Time:  O(26^3) ≈ 17,576 operations (constant)
        #    Space: Reuses the dist matrix (no extra asymptotic space).
        # -------------------------------------------------------------
        for k in range(ALPHABET):
            dk = dist[k]  # micro-optimization: row reference
            for i in range(ALPHABET):
                dik = dist[i][k]
                if dik == INF:
                    # No path i->k; skip inner j loop
                    continue
                di = dist[i]
                for j in range(ALPHABET):
                    # Candidate path i -> k -> j
                    via_k = dik + dk[j]
                    if via_k < di[j]:
                        di[j] = via_k

        # -------------------------------------------------------------
        # 3) For each position i in strings:
        #       - If s[i] == t[i], no cost needed.
        #       - Else, try all 26 letters c as "meeting point":
        #             cost_i = min_c( dist[s[i]][c] + dist[t[i]][c] )
        #       - If for some i no such c exists => return -1.
        #
        #    Time:  O(n * 26) since we try 26 letters for each position.
        #    Space: O(1) extra (a few scalars).
        # -------------------------------------------------------------
        total_cost = 0

        for i in range(n):
            ch_s = s[i]
            ch_t = t[i]

            # Already equal => 0 cost (no transformation necessary)
            if ch_s == ch_t:
                continue

            u = idx(ch_s)
            v = idx(ch_t)

            best_here = INF

            # Try all possible meeting letters c (0..25)
            for c in range(ALPHABET):
                cost_s_to_c = dist[u][c]
                cost_t_to_c = dist[v][c]
                # If either is impossible, skip that c
                if cost_s_to_c == INF or cost_t_to_c == INF:
                    continue
                candidate = cost_s_to_c + cost_t_to_c
                if candidate < best_here:
                    best_here = candidate

            if best_here == INF:
                # There is no letter c that both characters can become.
                return -1

            total_cost += best_here

        return total_cost


# ---------------------------------------------------------------------
# Example usage + timing
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Example input (from the statement's second example)
    s = "az"
    t = "dc"
    transform = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['a', 'd'], ['z', 'c']]
    cost = [5, 3, 2, 50, 10]

    print("Input:")
    print("s        =", s)
    print("t        =", t)
    print("transform =", transform)
    print("cost      =", cost)

    # Time the execution of minCost on this input.
    start_time = timer()
    sol = Solution()
    answer = sol.minCost(s, t, transform, cost)
    end_time = timer()

    print("\nOutput:")
    print("Minimum total cost to make strings equal:", answer)

    elapsed = end_time - start_time
    print("\nElapsed time (seconds):", elapsed)
```

When you run this script, you’ll see something like:

```text
Input:
s        = az
t        = dc
transform = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['a', 'd'], ['z', 'c']]
cost      = [5, 3, 2, 50, 10]

Output:
Minimum total cost to make strings equal: 20

Elapsed time (seconds): 3.4e-05
```

(Exact time will vary, but it will be extremely small.)
