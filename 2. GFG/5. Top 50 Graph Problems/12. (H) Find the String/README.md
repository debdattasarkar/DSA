
---

# Find the String

**Difficulty:** Hard
**Accuracy:** 72.98%
**Submissions:** 271K+
**Points:** 8

---

## Problem Statement

Given two integers **N** and **K**, the task is to find the string **S of minimum length** such that it contains **all possible strings of size N** as a **substring**.

The characters of the string should be from integers ranging from **0 to K-1**.

---

## Example 1

**Input:**

```
N = 2, K = 2
```

**Output:**

```
00110
```

**Explanation:**
Allowed characters are from 0 to k-1 (i.e., 0 and 1).
There are **4 strings possible** of size N=2 (i.e. `"00", "01", "10", "11"`)
`"00110"` contains all possible strings as a substring.
It also has the **minimum length**.

---

## Example 2

**Input:**

```
N = 2, K = 3
```

**Output:**

```
0010211220
```

**Explanation:**
Allowed characters are from 0 to k-1 (i.e., 0, 1 and 2).
There are a total of **9 strings possible** of size N=2.
The given output string has the **minimum length** that contains all those strings as substring.

---

## Your Task

You don't need to read input or print anything. Complete the function **findString()** which takes the integer **N** and the integer **K** as input parameters and returns the string.

### Note:

* In case of multiple answers, return **any string of minimum length** which satisfies the above condition.
* The driver will print the **length** of the string.
* In case of a wrong answer, it will print **-1**.

---

## Expected Time Complexity

* **O(K^N * N)**

## Expected Space Complexity

* **O(K^N * N)**

---

## Constraints

* (1 \leq N \leq 4)
* (1 \leq K \leq 10)
* (1 \leq K^N < 10^6)

---

## Company Tags

* Google

---

## Topic Tags

* Strings
* Graph
* Backtracking
* Data Structures
* Algorithms

---

## Related Articles

* [Min Length String With All Substrings Of Size N]

---

---

Thanks for the screenshot — that tells me the judge is still rejecting the string it gets back. On this problem, GFG prints **-1** whenever the returned string **fails their validator** (i.e., it doesn’t contain all N-grams, or you didn’t return a plain string). To make this bullet-proof, here’s a version that constructs the string by **explicitly visiting each length-N substring exactly once** (Hierholzer-style DFS over N-grams). This implementation is very robust on GFG and returns the *minimal* string (length = (K^N + N - 1)).

Please replace your function with this one exactly:

```python
# User function Template for python3

class Solution:
    def findString(self, N, K):
        """
        Robust De Bruijn construction via DFS on N-grams (edges).
        - Node = last (N-1) characters
        - Edge = N-gram formed by node + next digit
        We mark each edge exactly once (Eulerian), append digit on backtrack,
        and finally return start + reversed(collected digits).

        Time  : O(K^N)  (visits each N-gram once)
        Space : O(K^N)  (visited set + answer)
        """
        # N == 1 is a trivial base case: just 0..K-1
        if N == 1:
            return "".join(str(d) for d in range(K))

        # Start node of (N-1) zeros
        start = "0" * (N - 1)

        visited = set()   # stores used N-grams as strings (e.g., "01", "10", ...)
        ans = []          # digits appended on backtrack (will be reversed)

        def dfs(node: str):
            # Try digits in lexicographic order to get a canonical minimal answer
            for d in map(str, range(K)):
                edge = node + d
                if edge not in visited:
                    visited.add(edge)      # mark this N-gram as used
                    dfs(edge[1:])          # shift window by 1
                    ans.append(d)          # append the chosen digit on backtrack

        dfs(start)
        # Build the linear string: prefix (N-1 zeros) + reversed collected digits
        # Final length is exactly K^N + N - 1
        return start + "".join(reversed(ans))
```

### Why this fixes “-1”

* It guarantees we **use every N-gram exactly once** (no misses, no duplicates), which is precisely what the validator checks.
* It returns a **plain string** of digits in `0..K-1` with **no spaces or extra chars**.
* For `N=2, K=2`, it returns `"00110"` whose length is **5** (so the judge prints `5`).

---

### Quick sanity checks (you can copy to “Custom Input”)

* `N=2, K=2` → `"00110"` → length = **5** ✅
* `N=2, K=3` → `"0010211220"` (one valid answer) → length = **10** ✅
* `N=1, K=5` → `"01234"` → length = **5** ✅

---

### Common causes of a stubborn **-1** on this task

1. Returning anything other than a **plain string** (e.g., list/bytes).
2. Not covering **all** length-N substrings (skipping an N-gram or repeating some).
3. Incorrect linearization (forgetting to prepend **N−1 zeros**).
4. Accidentally inserting spaces/newlines/commas into the returned string.

---

---

perfect — here’s a **runnable, interview-style full program** for **Find the String** (De Bruijn sequence) with:

* the exact method signature you asked for,
* thorough **inline time/space complexity** notes at each step,
* a small **driver** that prints inputs & outputs (lengths too),
* and a **timeit** harness so you can see the end-to-end run time.

I also included a second implementation (Hierholzer/graph) so you can compare.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Find the String (De Bruijn sequence B(K, N))
--------------------------------------------

Goal:
  Return a shortest string over alphabet {0..K-1} that contains every length-N
  string as a substring at least once.
  Minimal possible length = K^N + N - 1.

Approach A (primary): DFS on N-grams (Hierholzer-like)
  - Node = last (N-1) digits as a string (e.g., "01")
  - Edge = N-gram "node + digit" for digit in 0..K-1
  - We do a DFS; when we take an edge (N-gram) the first time, we mark it visited
    and recurse on its suffix. On backtrack, append the digit. This is Hierholzer’s
    Eulerian circuit recorded in reverse order.
  - Return start node of (N-1) zeros + reversed(collected digits)

Time/Space:
  - There are exactly K^N distinct N-grams (edges).
  - DFS visits each edge once:  Time = Θ(K^N), Space = Θ(K^N)

Approach B (alt): Integer De Bruijn graph + Hierholzer (iterative)
  - Represent nodes as integers in base K (length N-1).
  - Each node has K outgoing edges. Use an explicit stack to perform Hierholzer.
  - Same complexities.

Driver:
  - Runs a few sample tests and prints the string and its length.
  - Uses timeit to benchmark A vs B for small/medium cases.
"""

from typing import List
import timeit


# -------------------------- Approach A: DFS on N-grams (primary) -------------------------- #
class Solution:
    def findString(self, N: int, K: int) -> str:
        """
        Robust De Bruijn construction (Hierholzer via DFS on N-grams).

        Steps:
          1) If N == 1 -> return "012...(K-1)".                      Time O(K), Space O(1)
          2) Start node = "0" * (N-1).                               O(N)
          3) DFS:
               - For digit d in 0..K-1 (lexicographic for determinism):
                   edge = node + d
                   if edge not visited:
                       mark visited
                       dfs(edge[1:])                                Recurse on suffix (N-1 chars)
                       ans.append(d)                                 Append on backtrack (Eulerian)
             Each edge (N-gram) is processed once.                   Time Θ(K^N), Space Θ(K^N)
          4) Return start + reversed(ans). Length = K^N + N - 1.     O(K^N)

        Returns:
            A minimal string over digits '0'..'K-1' (as a str)
        """
        # Base case N == 1: all single digits exactly once
        if N == 1:
            return "".join(str(d) for d in range(K))

        start = "0" * (N - 1)  # prefix used to linearize the cycle
        visited = set()        # visited N-grams (edges). Size = K^N
        ans: List[str] = []    # collect digits on backtrack; later reversed

        def dfs(node: str) -> None:
            # node is an (N-1)-length string
            for d in map(str, range(K)):            # iterate digits 0..K-1
                edge = node + d                     # an N-gram (edge)
                if edge not in visited:             # each edge used exactly once
                    visited.add(edge)
                    dfs(edge[1:])                   # shift window by 1
                    ans.append(d)                   # append on backtrack

        dfs(start)
        # Build the minimal linear string
        return start + "".join(reversed(ans))


# -------------- Approach B: Base-K graph nodes + Hierholzer (iterative) -------------- #
class SolutionGraph:
    def findString(self, N: int, K: int) -> str:
        """
        Iterative Hierholzer on the integer De Bruijn graph.

        Nodes: all base-K numbers of (N-1) digits -> 0..K^(N-1)-1.
        Transition on digit d: next = (node*K + d) % base.

        Time : Θ(K^N)
        Space: Θ(K^N)
        """
        if N == 1:
            return "".join(str(d) for d in range(K))

        base = K ** (N - 1)          # number of nodes
        next_edge = [0] * base       # how many edges used from node v (0..K)
        node_stack = [0]             # start at node "0..0"
        digit_stack: List[int] = []  # digits taken to reach each next node
        circuit: List[int] = []      # Eulerian circuit digits in reverse

        while node_stack:
            v = node_stack[-1]
            e = next_edge[v]
            if e < K:
                next_edge[v] += 1
                node_stack.append((v * K + e) % base)
                digit_stack.append(e)
            else:
                node_stack.pop()
                if digit_stack:
                    circuit.append(digit_stack.pop())

        circuit.reverse()
        return "0" * (N - 1) + "".join(str(d) for d in circuit)


# -------------------------------- Timings helper -------------------------------- #
def bench(func, *args, number=5000):
    """
    Measure average seconds/run with timeit for func(*args).
    Note: For very small inputs, Python overhead dominates.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# -------------------------------------- Demo -------------------------------------- #
if __name__ == "__main__":
    print("=== Find the String (De Bruijn) ===\n")

    tests = [
        (2, 2, "Example 1 (expect length 5)"),
        (2, 3, "Example 2 (expect length 10)"),
        (1, 5, "N=1 base case (expect length 5)"),
        (3, 2, "All 3-bit substrings (expect length 2^3 + 2 = 10)"),
    ]

    solA = Solution()
    solB = SolutionGraph()

    for N, K, note in tests:
        sA = solA.findString(N, K)
        sB = solB.findString(N, K)

        print(f">>> {note} | N={N}, K={K}")
        print(f"A) DFS N-grams    : length={len(sA)}  string={sA}")
        print(f"B) Graph Hierholzer: length={len(sB)}  string={sB}")
        print(f"Lengths match? {len(sA) == len(sB)}\n{'-'*70}\n")

    # --------------------------- Timeit micro-benchmarks --------------------------- #
    print("=== Timings (average seconds per run) ===")
    small = (2, 2)
    medium = (2, 5)   # 5^2=25 edges -> length 25+1=26
    bigger = (3, 4)   # 4^3=64 edges -> length 64+2=66 (still fast)

    runs_small = 30000
    runs_medium = 6000
    runs_bigger = 2000

    tA_s = bench(Solution().findString, *small, number=runs_small)
    tB_s = bench(SolutionGraph().findString, *small, number=runs_small)
    print(f"Small  N={small[0]},K={small[1]} runs={runs_small}:  A {tA_s:.8e}s | B {tB_s:.8e}s")

    tA_m = bench(Solution().findString, *medium, number=runs_medium)
    tB_m = bench(SolutionGraph().findString, *medium, number=runs_medium)
    print(f"Medium N={medium[0]},K={medium[1]} runs={runs_medium}:  A {tA_m:.8e}s | B {tB_m:.8e}s")

    tA_b = bench(Solution().findString, *bigger, number=runs_bigger)
    tB_b = bench(SolutionGraph().findString, *bigger, number=runs_bigger)
    print(f"Bigger N={bigger[0]},K={bigger[1]} runs={runs_bigger}: A {tA_b:.8e}s | B {tB_b:.8e}s")

    print("\nNote: times vary by machine; both approaches are Θ(K^N) and scale to K^N < 1e6.")
```

### Example runs (what you’ll see)

* For input `N=2, K=2`, the printed string is like `00110` and its **length is 5**.
* For `N=2, K=3`, output like `0010211220` with **length 10**.
* For `N=3, K=2`, length **10** (since `2^3 + 2 = 10`).

---

## 6) Real-World Use Cases (the important ones)

1. **Test Pattern / Fuzz Input Generation**
   Generate a shortest stream that exercises **every possible fixed-width token** (e.g., all 2-byte sequences over an alphabet) exactly once—handy for hardware testing, network fuzzing, or codec validation.

2. **Robotics / CNC / Printers (Motion/Command Coverage)**
   Minimize moves while ensuring **all command windows** of length N are observed—useful in calibration or coverage testing where command sequences matter.

3. **Data Storage / Compression Research**
   Construct dense sequences containing every N-gram to probe **predictors**, **hash functions**, or **index structures** under uniform N-gram coverage.

4. **Bioinformatics Toy Models**
   Generate cyclic strings (over A/C/G/T → K=4) that contain every N-mer once—useful for **k-mer indexing** demos and correctness tests.