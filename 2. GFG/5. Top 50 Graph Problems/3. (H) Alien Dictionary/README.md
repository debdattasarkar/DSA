Here’s the **full README conversion** of the problem statement you shared, without omitting any part:

---

# Alien Dictionary

**Difficulty:** Hard
**Accuracy:** 47.81%
**Submissions:** 169K+
**Points:** 8

---

## Problem Statement

A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of **words[]** from the alien language’s dictionary, where the words are claimed to be **sorted lexicographically** according to the language’s rules.

Your task is to determine **the correct order of letters** in this alien language based on the given words.

* If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language’s rules.
* If there are multiple valid orders, return any one of them.
* If the given arrangement of words is inconsistent with any possible letter ordering, return an empty string (`""`).

---

### Lexicographic Definition

A string **a** is lexicographically smaller than a string **b** if, at the first position where they differ, the character in **a** appears earlier in the alien language than the corresponding character in **b**.
If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

---

**Note:** Your implementation will be tested using a driver code. It will print **true** if your returned word correctly follows the alien language’s lexicographic rules; otherwise, it will print **false**.

---

## Examples

### Example 1

**Input:**

```
words[] = ["baa", "abcd", "abca", "cab", "cad"]
```

**Output:**

```
true
```

**Explanation:**
A possible correct order of letters in the alien dictionary is `"bdac"`.

* The pair `"baa"` and `"abcd"` suggests `'b'` appears before `'a'`.
* The pair `"abcd"` and `"abca"` suggests `'d'` appears before `'a'`.
* The pair `"abca"` and `"cab"` suggests `'a'` appears before `'c'`.
* The pair `"cab"` and `"cad"` suggests `'b'` appears before `'d'`.

So, `'b' → 'd' → 'a' → 'c'` is a valid ordering.

---

### Example 2

**Input:**

```
words[] = ["caa", "aaa", "aab"]
```

**Output:**

```
true
```

**Explanation:**
A possible correct order of letters in the alien dictionary is `"cab"`.

* The pair `"caa"` and `"aaa"` suggests `'c'` appears before `'a'`.
* The pair `"aaa"` and `"aab"` suggests `'a'` appears before `'b'`.

So, `'c' → 'a' → 'b'` is a valid ordering.

---

### Example 3

**Input:**

```
words[] = ["ab", "cd", "ef", "ad"]
```

**Output:**

```
""
```

**Explanation:**
No valid ordering of letters is possible.

* The pair `"ab"` and `"ef"` suggests `'a'` appears before `'e'`.
* The pair `"ef"` and `"ad"` suggests `'e'` appears before `'a'`.
  This creates a contradiction, so no valid order exists.

---

## Constraints

* (1 \leq \text{words.length} \leq 500)
* (1 \leq \text{words[i].length} \leq 100)
* Each `words[i]` consists only of lowercase English letters.

---

## Expected Complexities

* **Time Complexity:** (O(n \times m)), where *n* = number of words, *m* = average word length.
* **Auxiliary Space:** (O(n \times m)).

---

## Company Tags

* Flipkart
* Amazon
* Microsoft
* OYO Rooms
* Walmart
* Google

---

## Topic Tags

* Strings
* Sorting
* Graph
* Data Structures
* Algorithms

---

## Related Interview Experiences

* Walmart Lab Interview Experience Set 9 Off Campus
* Amazon Interview Experience for SDE 1 (6 Months Internship On Campus)
* Flipkart Interview Set 2 SDE 2
* Flipkart Interview Experience for SDE 2

---

## Related Articles

* Given Sorted Dictionary Find Precedence Characters

---

---

awesome — let’s make this interview-ready: crisp intuition, step-by-step dry run, and multiple Python solutions in your requested template.

---

# 2) Intuition & Step-by-Step Dry Run

## Problem recap

We’re given words already sorted according to an **unknown alien alphabet**.
From every **adjacent pair** of words, the **first differing character** tells us a precedence rule: `u` must appear **before** `v`.
All such rules form a **directed graph** `u → v`. A valid letter order is any **topological ordering** of this graph.
If there’s a **cycle** or an invalid **prefix** case (e.g., “abcd” then “ab”), no valid order exists → return `""`.

### Graph building rules

1. Collect the **set of unique letters** that appear anywhere in the input.
2. For each adjacent pair `(w1, w2)`:

   * Scan from left to right until the first differing position `i`.
   * Add edge `w1[i] → w2[i]` (meaning `w1[i]` precedes `w2[i]`).
   * If **no** diff and `len(w1) > len(w2)`, invalid (prefix violation) → return `""`.

### How to get an order

* **Kahn’s Algorithm (BFS topological sort):**

  * Compute `indegree` of each node.
  * Push all nodes with `indegree=0` to a queue.
  * Repeatedly pop from queue, append to answer, and decrement indegrees of neighbors; any that drop to `0` join the queue.
  * If answer length < number of unique letters → there’s a cycle → return `""`.
  * If multiple zero-indegree choices exist, **any** order is acceptable (problem allows multiple valid answers).

* **DFS topological sort:**

  * Standard white/gray/black coloring to detect cycles.
  * Postorder stack reversed gives a valid order.

---

## Dry Run (Example 1)

`words = ["baa", "abcd", "abca", "cab", "cad"]`

**Step A: unique letters**
`{a, b, c, d}`

**Step B: compare adjacent pairs**

1. `"baa"` vs `"abcd"`
   First diff at i=0: `'b'` vs `'a'` ⇒ edge **b → a**
2. `"abcd"` vs `"abca"`
   First diff at i=3: `'d'` vs `'a'` ⇒ edge **d → a**
3. `"abca"` vs `"cab"`
   First diff at i=0: `'a'` vs `'c'` ⇒ edge **a → c**
4. `"cab"` vs `"cad"`
   First diff at i=2: `'b'` vs `'d'` ⇒ edge **b → d**

**Graph edges:** `b→a`, `d→a`, `a→c`, `b→d`
**Indegrees:**

* a: 2 (from b, d)
* b: 0
* c: 1 (from a)
* d: 1 (from b)

**Kahn BFS:**

* Start queue: `[b]`
* Pop `b` → output `b`; decrement indegree of `a` (1), `d` (0). Enqueue `d`.
* Pop `d` → output `bd`; decrement indegree of `a` (0). Enqueue `a`.
* Pop `a` → output `bda`; decrement indegree of `c` (0). Enqueue `c`.
* Pop `c` → output `bdac`.
  All 4 letters placed → `"bdac"` (valid).

---

# 3) Python solutions (what interviewers expect)

### A) Kahn’s BFS Toposort (primary / most common)

```python
from collections import defaultdict, deque

class Solution:
    def findOrder(self, words):
        """
        Return one valid alien letter order or "" if impossible.

        Steps:
          1) Gather all unique letters.
          2) Build graph from adjacent word pairs using the first differing char.
             - If w1 is a strict prefix of w2 => OK
             - If w2 is a strict prefix of w1 (no diff, len(w1) > len(w2)) => invalid -> ""
          3) Kahn's BFS topological sort over letters (nodes).
          4) If we placed all letters, return the order. Else, there's a cycle -> "".

        Time:  O(n * m + V + E)  ; n=#words, m=avg length, V<=26, E<=25*? (small)
        Space: O(V + E)
        """
        if not words:
            return ""

        # 1) Unique letters
        letters = set(ch for w in words for ch in w)

        # 2) Build graph
        adj = defaultdict(set)           # u -> set of v
        indeg = {ch: 0 for ch in letters}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # prefix check if needed
            minlen = min(len(w1), len(w2))
            j = 0
            while j < minlen and w1[j] == w2[j]:
                j += 1
            if j == minlen:
                # No differing char in overlap; if w1 longer than w2 => invalid
                if len(w1) > len(w2):
                    return ""
                continue
            # First differing chars create an edge w1[j] -> w2[j]
            u, v = w1[j], w2[j]
            if v not in adj[u]:          # avoid double-indegree
                adj[u].add(v)
                indeg[v] += 1

        # 3) Kahn's BFS
        q = deque([c for c in indeg if indeg[c] == 0])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # 4) Cycle check
        if len(order) != len(letters):
            return ""  # cycle or unreachable nodes
        return "".join(order)
```

---

### B) DFS Toposort with cycle detection (equally acceptable)

```python
from collections import defaultdict

class Solution:
    def findOrder(self, words):
        """
        DFS topo with colors:
          0=unvisited, 1=visiting (gray), 2=done (black).
        If we see an edge to gray => cycle => invalid.

        Time:  O(n*m + V+E) , Space: O(V+E)
        """
        if not words:
            return ""

        letters = set(ch for w in words for ch in w)
        adj = defaultdict(set)

        # Build edges with prefix rule
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            j = 0
            while j < minlen and w1[j] == w2[j]:
                j += 1
            if j == minlen:
                if len(w1) > len(w2):   # "abcd" before "ab"
                    return ""
                continue
            u, v = w1[j], w2[j]
            adj[u].add(v)

        color = {c: 0 for c in letters}
        out = []
        has_cycle = False

        def dfs(u):
            nonlocal has_cycle
            if has_cycle:
                return
            color[u] = 1  # gray
            for v in adj[u]:
                if color[v] == 0:
                    dfs(v)
                elif color[v] == 1:  # back-edge
                    has_cycle = True
                    return
            color[u] = 2  # black
            out.append(u)  # postorder

        for c in letters:
            if color[c] == 0:
                dfs(c)
                if has_cycle:
                    return ""

        out.reverse()
        return "".join(out)
```

---

### C) “Brute-for-learning” backtracking over letters (NOT for production)

Try all permutations of only the **appearing** letters (not all 26), and check if they keep the input words sorted under that order. Exponential in `k = #letters` (k!); fine only when `k` is tiny. This demonstrates correctness reasoning but is not expected to pass large cases.

```python
from itertools import permutations

class Solution:
    def findOrder(self, words):
        """
        Brute: try all permutations of involved letters and validate.
        Time:  O(k! * n*m)  (k = unique letters)  => impractical for big k
        """
        letters = sorted(set(ch for w in words for ch in w))
        if not letters:
            return ""

        def valid(order):
            rank = {c: i for i, c in enumerate(order)}  # O(k)
            # Check sortedness pairwise                   O(n*m)
            for i in range(len(words) - 1):
                a, b = words[i], words[i + 1]
                # compare by rank
                j = 0
                while j < len(a) and j < len(b) and a[j] == b[j]:
                    j += 1
                if j == len(a) or j == len(b):
                    if len(a) > len(b):
                        return False  # prefix violation
                    continue
                if rank[a[j]] > rank[b[j]]:
                    return False
            return True

        for perm in permutations(letters):
            if valid(perm):
                return "".join(perm)
        return ""
```

> In interviews, mention this approach as a conceptual baseline, then pivot to topo-sort as the scalable solution.

---

# 4) Interview Q&A (high-yield)

**Q1. How do you extract ordering constraints from the words?**
Compare each **adjacent pair** and take the **first differing character**: that letter in the first word must precede the letter in the second word. Those become directed edges in a graph.

**Q2. What about the prefix case?**
If `w1` is longer than `w2` and `w1` starts with `w2`, the input is **invalid** (you cannot have “abcd” before “ab” in a lexicographically sorted list). Return `""`.

**Q3. Why does topological sorting apply?**
The constraints form a partial order (`u` must come before `v`). A **topological order** of the directed acyclic graph (DAG) is exactly a linear extension of that partial order, i.e., a valid alphabet.

**Q4. How do you detect contradictions?**
A **cycle** in the graph (via Kahn’s incomplete output or DFS gray-edge detection) means no linear order can satisfy the constraints → return `""`.

**Q5. What are the complexities?**
Building edges is `O(n*m)` where `n` is number of words and `m` their average length. Toposort is `O(V+E)`. Since `V ≤ 26`, the dominating term is `O(n*m)`. Space is `O(V+E)`.

**Q6. Multiple valid orders exist—what do we return?**
Any one. To make output deterministic, you could use a **min-heap** in Kahn’s algorithm to always pick the smallest lexicographic zero-indegree letter (if the platform requires).

**Q7. Can there be isolated letters (no edges)?**
Yes. They just have indegree `0` and can appear anywhere consistent with constraints. Ensure they’re included in the result.

**Q8. What if a letter appears in the words but never in any edge?**
It still must be present in the final order. Kahn/DFS both include all nodes (letters), not just those with edges.

**Q9. How would you test this quickly?**

* Normal cases (examples).
* Cycle: `["z","x","z"]`.
* Prefix invalid: `["abc","ab"]`.
* Isolated letters: `["x","x"]` or `["a","a","b"]`.
* Large equal-prefix chains to test edge extraction.

**Q10. Why store adjacency as sets?**
To avoid duplicate edges inflating indegrees, which would corrupt Kahn’s counts and could falsely cause cycles.

---

---

awesome — here’s a **runnable, interview-style full program** for *Alien Dictionary* with:

* clean Kahn’s BFS solution (primary),
* optional DFS parity check,
* inline **time/space complexity** notes on each step,
* a simple **driver** that prints inputs & outputs,
* and **timeit** benchmarks.

I’ve also added a short list of high-value real-world use cases.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Alien Dictionary — find one valid order of letters given words sorted by an unknown alphabet.

Primary approach:
  - Build precedence constraints by comparing each adjacent word pair at the first differing char.
  - Detect invalid prefix cases (e.g., ["abcd","ab"]).
  - Run topological sort (Kahn's BFS). If we place all letters, return the order; else return "".

High-level complexities:
  - Building edges: O(n * m)       # n = #words, m = average length
  - Toposort (V letters, E edges): O(V + E)  # V <= 26 typically
  - Space: O(V + E)
"""

from collections import defaultdict, deque
import timeit
from typing import List


class Solution:
    # -----------------------------------------------------------------------------------
    # Return one valid alien order string (or "" if impossible) using Kahn's BFS topo.
    # -----------------------------------------------------------------------------------
    def findOrder(self, words: List[str]) -> str:
        """
        Steps:
          1) Gather unique letters  ------------------------------ Time: O(total chars), Space: O(V)
          2) Build graph from adjacent pairs --------------------- Time: O(n*m), Space: O(E)
             - If first differing char is u in w1 and v in w2, add edge u->v.
             - If w1 is longer and is a prefix of w2 => invalid -> "".
          3) Kahn's BFS (queue of indegree==0) ------------------- Time: O(V + E), Space: O(V)
          4) If we output all letters, return them; else "".
        """
        if not words:
            return ""

        # (1) Collect unique letters: ---------------------------- O(total chars), O(V)
        letters = set(ch for w in words for ch in w)

        # (2) Build adjacency list + indegree -------------------- O(n*m) to compare pairs
        adj = defaultdict(set)                        # u -> {v, ...}
        indeg = {c: 0 for c in letters}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # Compare up to shorter length ----------------------- O(min(len(w1), len(w2)))
            j = 0
            L = min(len(w1), len(w2))
            while j < L and w1[j] == w2[j]:
                j += 1

            if j == L:
                # All equal up to min; if w1 longer than w2 -> invalid prefix case
                if len(w1) > len(w2):
                    return ""                               # contradiction
                continue

            u, v = w1[j], w2[j]                            # first difference gives u->v
            # Avoid duplicate edges (which would overcount indegree)
            if v not in adj[u]:
                adj[u].add(v)
                indeg[v] += 1

        # (3) Kahn's BFS: push all zero-indegree nodes ---------- O(V)
        q = deque([c for c in indeg if indeg[c] == 0])
        order = []

        # Process nodes; each edge considered once -------------- O(V + E)
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # (4) Cycle/contradiction check
        if len(order) != len(letters):
            return ""                                        # cycle present
        return "".join(order)


# ----------------------------- Optional: DFS topo for parity -----------------------------
class SolutionDFS:
    def findOrder(self, words: List[str]) -> str:
        """
        DFS topological sort with 3-color cycle detection.
        Time:  O(n*m + V + E)
        Space: O(V + E) for graph and recursion stack
        """
        if not words:
            return ""

        letters = set(ch for w in words for ch in w)
        adj = defaultdict(set)

        # Build constraints and handle the prefix rule ----------- O(n*m)
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            j, L = 0, min(len(a), len(b))
            while j < L and a[j] == b[j]:
                j += 1
            if j == L:
                if len(a) > len(b):
                    return ""
                continue
            adj[a[j]].add(b[j])

        color = {c: 0 for c in letters}  # 0=unvisited,1=visiting,2=done
        out = []
        has_cycle = False

        def dfs(u: str):
            nonlocal has_cycle
            if has_cycle:
                return
            color[u] = 1
            for v in adj[u]:
                if color[v] == 0:
                    dfs(v)
                elif color[v] == 1:      # back edge -> cycle
                    has_cycle = True
                    return
            color[u] = 2
            out.append(u)                 # postorder push

        for c in letters:
            if color[c] == 0:
                dfs(c)
                if has_cycle:
                    return ""

        out.reverse()
        return "".join(out)


# ----------------------------- Benchmark helper using timeit -----------------------------
def bench(func, *args, number=10000):
    """
    Measure average seconds per run for func(*args) over 'number' iterations.
    Note: for very small inputs, micro-benchmarks are dominated by overheads.
    """
    t = timeit.timeit(lambda: func(*args), number=number)
    avg = t / number
    return avg


# ----------------------------- Main Program: inputs, outputs, timings -----------------------------
if __name__ == "__main__":
    tests = [
        # (words, expectation_info_only)
        (["baa", "abcd", "abca", "cab", "cad"], 'valid (e.g., "bdac")'),
        (["caa", "aaa", "aab"], 'valid (e.g., "cab")'),
        (["ab", "cd", "ef", "ad"], 'invalid -> ""'),
        (["z", "z"], 'single letter, valid "z"'),
        (["abc", "ab"], 'invalid prefix -> ""'),
        (["x", "xy", "xyz"], 'valid chain'),
    ]

    print("=== Alien Dictionary ===\n")
    solver = Solution()
    solver_dfs = SolutionDFS()

    for words, note in tests:
        out_bfs = solver.findOrder(words)
        out_dfs = solver_dfs.findOrder(words)
        print(f"Input words: {words}")
        print(f"Kahn BFS order : {out_bfs!r}")
        print(f"DFS topo order : {out_dfs!r}")
        print(f"Note (expectation): {note}")
        print(f"Both methods agree? {out_bfs == out_dfs}\n")

    # ---------------- Timings ----------------
    print("=== Timings (average seconds per run) ===")
    small = ["baa", "abcd", "abca", "cab", "cad"]
    medium = ["a" * 50 + "b", "a" * 50 + "c", "b" * 40 + "a", "b" * 40 + "c"]  # longer words

    runs_small = 20000
    runs_medium = 5000

    t_bfs_small = bench(solver.findOrder, small, number=runs_small)
    t_dfs_small = bench(solver_dfs.findOrder, small, number=runs_small)
    print(f"Input size ~ small, runs={runs_small}")
    print(f"BFS avg: {t_bfs_small:.8e} s")
    print(f"DFS avg: {t_dfs_small:.8e} s")

    t_bfs_med = bench(solver.findOrder, medium, number=runs_medium)
    t_dfs_med = bench(solver_dfs.findOrder, medium, number=runs_medium)
    print(f"\nInput size ~ medium, runs={runs_medium}")
    print(f"BFS avg: {t_bfs_med:.8e} s")
    print(f"DFS avg: {t_dfs_med:.8e} s")

    print("\nNote: absolute timings vary by machine and Python version.")
```

### What the program prints

* For each test case, it shows:

  * **Input words**,
  * the **BFS** order,
  * the **DFS** order,
  * whether they **agree**, and the expectation note.
* Then it prints **timeit** averages for both BFS and DFS versions on small/medium inputs.

---

## 6) Real-World Use Cases (the important ones)

1. **Inferring Build/Deployment Order**
   When components’ pairwise precedence can be observed (e.g., logs or manifests), recover a valid **build/install order** respecting dependencies.

2. **Version/Schema Migration Planning**
   Given observed constraints like “apply migration A before B” extracted from tools or scripts, derive a consistent **migration sequence** or detect **cycles**.

3. **Natural-Language / Phonetic Ordering from Corpora**
   From sorted word lists in lesser-documented languages, reconstruct **alphabet order** (linguistics/digital humanities) or phoneme precedence.

4. **UI/Workflow Step Recovery**
   From usage traces that imply “step X occurs before step Y” for successful sessions, infer a **valid onboarding/flow order** and flag contradictory flows.
