
---

# 🧩 Union-Find

**Difficulty:** Easy
**Accuracy:** 60.8%
**Submissions:** 26K+
**Points:** 2
**Average Time:** 15 minutes

---

## 📝 Problem Statement

This problem is to implement **Disjoint Set Union (Union-Find)**.
There will be 2 incomplete functions, namely `union()` and `isConnected()`.
You have to complete these functions.

---

### 🔹 Union:

Join two subsets into a single set.

### 🔹 isConnected:

Determine which subset a particular element is in.
This can be used for determining if two elements are in the same subset.

---

## 📘 Example 1

**Input:**

```
N = 5  
q = 4  
Queries =  
Union(1,3)  
isConnected(1,2)  
Union(1,5)  
isConnected(3,5)
```

**Output:**

```
0  
1
```

**Explanation:**

* Initially, all nodes 1 2 3 4 5 are not connected.
* After `Union(1,3)`, node 1 and 3 will be connected.
* When we do `isConnected(1,2)`, as node 1 and 2 are not connected, it will return `0`.
* After `Union(1,5)`, node 1 and 5 will be connected.
* When we do `isConnected(3,5)`, as node 1 and 3 are connected, and node 1 and 5 are connected, hence 3 and 5 are connected.
  Thus, it will return `1`.

---

## 📘 Example 2

**Input:**

```
N = 5  
q = 4  
Queries =  
Union(1,4)  
Union(1,5)  
isConnected(2,3)  
Union(3,4)
```

**Output:**

```
0
```

**Explanation:**

* Initially, all nodes are independent.
* After `Union(1,4)` and `Union(1,5)`, the group is {1,4,5}.
* `isConnected(2,3)` → no connection, returns 0.
* Even after `Union(3,4)`, 2 and 3 remain unconnected initially.
  Final answer is `0`.

---

## 🎯 Your Task

You have to complete the following functions:

* **`union_(node1, node2)`** — merges the sets of `node1` and `node2`.
* **`isConnected(node1, node2)`** — returns whether the two nodes are connected.

Both functions will contain two arrays:

* `par[]` → parent array
* `rank1[]` → rank array

Initially:

```
par[i] = i  
rank1[i] = 1
```

---

## 📈 Expected Time and Space Complexity

* **Expected Time Complexity:** O(N + Q)
* **Expected Auxiliary Space:** O(1)

---

## ⚙️ Constraints

```
1 ≤ N ≤ 10⁵  
1 ≤ Q ≤ 10⁵  
1 ≤ node1, node2 ≤ N
```

---

## 🧠 Topic Tags

* Graph
* Disjoint Set
* Data Structures

---

## 📚 Related Articles

* [Introduction to Disjoint Set Data Structure or Union-Find Algorithm](https://www.geeksforgeeks.org/union-find/)

---

✅ **Summary:**
Implement `union()` and `isConnected()` using **Union-Find (Disjoint Set Union)** with path compression and union by rank for efficiency.

---

---

perfect — here’s everything you need to ace **Union–Find (Disjoint Set Union)** interviews:

* crisp intuition + a **walkthrough dry run**
* two Python variants in your requested signature:

  1. **Optimized DSU** (path compression + union by rank) — what interviewers expect
  2. **Brute/naïve DSU** (no compression, no rank) — to contrast why optimizations matter
* tight **interviewer Q&A** at the end

---

## 2) Intuition & Step-by-Step Dry Run

### What is DSU?

A data structure maintaining a partition of elements into disjoint sets with two core ops:

* **find(x)** → returns the **representative (root)** of x’s set
* **union(a, b)** → merges the sets containing a and b

With **path compression** (in `find`) and **union by rank/size**, both operations run in **amortized near O(1)** (formally `O(α(N))`, inverse Ackermann).

### How it works

* Each node has a `parent` pointer. Roots are nodes whose parent is themselves.
* `rank` (or `size`) estimates tree height (or size). When unioning, attach **smaller rank** tree under **larger rank** tree to keep trees shallow.
* **Path compression:** during `find(x)`, make every node on the path point **directly to the root**.

### Dry run (based on Example 1)

```
Initial:
par = [1,2,3,4,5]  # 1-based; each node is its own parent
rank1 = [1,1,1,1,1]

Operations:
1) Union(1,3)
   find(1) -> 1, find(3) -> 3
   ranks equal → make 3's parent 1; rank1[1]++ => 2
   par: [1,2,1,4,5], rank1: [2,1,1,1,1]   (writing 1-based conceptual)

2) isConnected(1,2)?
   find(1) -> 1
   find(2) -> 2
   1 != 2 → return 0

3) Union(1,5)
   find(1) -> 1, find(5) -> 5
   rank1[1]=2 > rank1[5]=1 → attach 5 under 1
   par: [1,2,1,4,1]

4) isConnected(3,5)?
   find(3) -> follow par[3]=1 → root 1 (path compress sets par[3]=1)
   find(5) -> follow par[5]=1 → root 1
   Equal → return 1
```

Outputs: `0`, then `1` — as expected.

---

## 3) Python Codes (Brute & Optimized)

Below is your required class/signature. I show **Optimized** first (what interviewers expect), then a **Brute** version for comparison.

### ✅ Optimized DSU (Path Compression + Union by Rank)

```python
# User function Template for python3

class Solution:
    
    # ----- helper: find with path compression -----
    def _find(self, x, par):
        """
        Finds the root (representative) of x.
        Path compression makes future finds almost O(1).
        Amortized time: O(α(N)).
        """
        if par[x] != x:
            par[x] = self._find(par[x], par)  # compress path
        return par[x]
    
    # Function to merge two nodes a and b.
    def union_(self, a, b, par, rank1):
        """
        Union by rank:
        - Attach the lower-rank tree under the higher-rank tree.
        - If ranks equal, pick one as root and increment its rank.
        
        Amortized time per union: O(α(N)), space: O(1) extra.
        """
        ra = self._find(a, par)
        rb = self._find(b, par)
        if ra == rb:
            return  # already in same set
        
        # attach smaller-rank root under larger-rank root
        if rank1[ra] < rank1[rb]:
            par[ra] = rb
        elif rank1[rb] < rank1[ra]:
            par[rb] = ra
        else:
            # ranks equal: pick one root (say ra), increase its rank
            par[rb] = ra
            rank1[ra] += 1
    
    # Function to check whether 2 nodes are connected or not.
    def isConnected(self, x, y, par, rank1):
        """
        Connected iff their roots are equal.
        Each find is amortized O(α(N)).
        """
        return 1 if self._find(x, par) == self._find(y, par) else 0
```

#### How to initialize `par` and `rank1`

* Use **1-based** or **0-based** consistently.
* For 1-based (common in GFG):

```python
# N given
par = [i for i in range(N+1)]
rank1 = [1] * (N+1)
```

* For 0-based: size `N`, `par[i] = i`, `rank1[i] = 1`.

---

### 🐢 Brute / Naïve DSU (no compression, no rank)

```python
class Solution:
    
    def _find(self, x, par):
        """
        Naïve find: climb parent pointers until root.
        Worst-case time: O(N).
        """
        while par[x] != x:
            x = par[x]
        return x
    
    def union_(self, a, b, par, rank1):
        """
        Naïve union: make root of b point to root of a (no rank/size).
        Can create tall chains -> O(N) operations.
        """
        ra = self._find(a, par)
        rb = self._find(b, par)
        if ra != rb:
            par[rb] = ra  # arbitrary choice
    
    def isConnected(self, x, y, par, rank1):
        """
        Naïve connectivity check.
        """
        return 1 if self._find(x, par) == self._find(y, par) else 0
```

> Use the **optimized** version in interviews. If asked for improvements, mention both **path compression** and **union by rank/size** and explain how they keep trees shallow.

---

## 4) Interview Q&A (laser-focused)

**Q1. What’s the time complexity of DSU with optimizations?**
Amortized **near O(1)** per operation; formally **O(α(N))**, where α is the inverse Ackermann function (grows < 5 for any realistic N).

**Q2. Why do we need both path compression and union by rank?**

* **Union by rank/size** keeps trees shallow **as we build** them.
* **Path compression** flattens trees **as we query** them.
  Together they guarantee near-constant amortized time.

**Q3. Rank vs size — any difference?**
Both work similarly. **Size** counts nodes; **rank** approximates height. Either is acceptable.

**Q4. What happens if you only do one of them?**
Still faster than naive, but not optimal. Only compression without rank can still lead to temporarily tall trees; only rank without compression leaves long paths on queries.

**Q5. How would you detect if two nodes are already connected before union?**
Compare `find(a)` and `find(b)`; if equal, they belong to the same set → union is a no-op.

**Q6. Applications of DSU?**

* **Kruskal’s algorithm** for MST
* Detecting **cycles** in undirected graphs
* **Connected components** in dynamic graphs
* **Percolation**, **image segmentation**, **friend circles**, **equivalence classes** problems

**Q7. Memory footprint?**
Two arrays of length N: `par[N]`, `rank[N]` (or `size[N]`) → **O(N)** space.

**Q8. Can DSU support deletions/splits?**
Not in standard DSU. It’s great for **merges** and **queries**, but not for splitting sets.

---

---

awesome — here’s a **runnable, interview-style full program** for **Union–Find (Disjoint Set Union)** that:

* implements the exact signature you asked for (`union_`, `isConnected`) with **path compression + union-by-rank**,
* prints outputs for the two sample scenarios from the prompt,
* and uses **timeit** to report **average runtime per call** on a small synthetic workload.

I’ve put **time/space complexity comments inline** right where the operations happen.

---

## 5) Full Python Program (with inline complexity notes + timings)

```python
"""
Union–Find (Disjoint Set Union) — Full Demo with Timing
-------------------------------------------------------

Core operations:
  - find(x): return representative/root of x's set (with PATH COMPRESSION)
  - union(a,b): merge the two sets by attaching lower-rank root under higher-rank root
  - isConnected(x,y): True (1) if find(x) == find(y), else False (0)

Complexities (with path compression + union by rank):
  - Amortized time per operation : O(α(N))   where α is inverse Ackermann (< 5 in practice)
  - Space                         : O(N)     for parent[] and rank[]

Driver:
  * Runs Example 1 and Example 2 from the prompt, showing outputs.
  * Benchmarks union/find on a small synthetic sequence using timeit.
"""

from typing import List
import timeit
import random


# -------------------------- User function Template for python3 -------------------------- #
class Solution:
    # ----- helper: find with path compression -----
    def _find(self, x: int, par: List[int]) -> int:
        """
        Return root of x's set.
        Path compression flattens the tree for all nodes on the path,
        ensuring future queries are almost O(1).
        Time (amortized): O(α(N)); Space: O(1) extra.
        """
        if par[x] != x:
            par[x] = self._find(par[x], par)  # compress path
        return par[x]

    # Function to merge two nodes a and b.
    def union_(self, a: int, b: int, par: List[int], rank1: List[int]) -> None:
        """
        Union by rank: attach the lower-rank root under the higher-rank root.
        If ranks are equal, pick one as new root and increase its rank by 1.

        Time (amortized): O(α(N)); Space: O(1) extra.
        """
        ra = self._find(a, par)
        rb = self._find(b, par)
        if ra == rb:
            return  # already in same set

        # attach smaller-rank under larger-rank
        if rank1[ra] < rank1[rb]:
            par[ra] = rb
        elif rank1[rb] < rank1[ra]:
            par[rb] = ra
        else:
            par[rb] = ra
            rank1[ra] += 1

    # Function to check whether 2 nodes are connected or not.
    def isConnected(self, x: int, y: int, par: List[int], rank1: List[int]) -> int:
        """
        Two nodes are connected iff their roots are equal.
        Time (amortized): O(α(N)); Space: O(1) extra.
        """
        return 1 if self._find(x, par) == self._find(y, par) else 0


# -------------------------------- utility: run a query set -------------------------------- #
def run_queries(N: int, queries: List[str]) -> List[int]:
    """
    Execute textual queries of the form:
      'Union(a,b)'
      'isConnected(x,y)'
    on a DSU initialized for 1..N.

    Returns a list of results for all isConnected() queries (0/1).
    """
    # Initialize DSU arrays (1-based as per examples)
    par = [i for i in range(N + 1)]   # Space: O(N)
    rank1 = [1] * (N + 1)             # Space: O(N)
    sol = Solution()

    out = []
    for q in queries:
        q = q.strip()
        if q.startswith("Union"):
            a, b = q[q.find("(")+1:q.find(")")].split(",")
            sol.union_(int(a), int(b), par, rank1)
        elif q.startswith("isConnected"):
            x, y = q[q.find("(")+1:q.find(")")].split(",")
            out.append(sol.isConnected(int(x), int(y), par, rank1))
    return out


# ------------------------------------------ demo ------------------------------------------ #
if __name__ == "__main__":
    print("=== Union–Find (DSU) — with Path Compression + Union by Rank ===\n")

    # ---------------- Example 1 (from prompt) ----------------
    N1 = 5
    queries1 = [
        "Union(1,3)",
        "isConnected(1,2)",
        "Union(1,5)",
        "isConnected(3,5)"
    ]
    print(">>> Example 1")
    print("N =", N1)
    print("Queries:")
    for q in queries1: print(" ", q)
    out1 = run_queries(N1, queries1)
    print("Output:")
    for r in out1: print(r)   # Expected: 0, 1
    print()

    # ---------------- Example 2 (from prompt) ----------------
    N2 = 5
    queries2 = [
        "Union(1,4)",
        "Union(1,5)",
        "isConnected(2,3)",
        "Union(3,4)"
    ]
    print(">>> Example 2")
    print("N =", N2)
    print("Queries:")
    for q in queries2: print(" ", q)
    out2 = run_queries(N2, queries2)
    print("Output:")
    for r in out2: print(r)   # Expected: 0
    print()

    # ---------------- small synthetic timing benchmark ----------------
    print("=== Timings (average seconds per run) ===")

    # Build a reproducible random workload of unions/finds
    random.seed(7)
    N = 10_000
    # make a mix of 70% unions and 30% connectivity checks
    mixed_queries = []
    for _ in range(600):
        a = random.randint(1, N)
        b = random.randint(1, N)
        mixed_queries.append(f"Union({a},{b})")
    for _ in range(250):
        x = random.randint(1, N)
        y = random.randint(1, N)
        mixed_queries.append(f"isConnected({x},{y})")
    random.shuffle(mixed_queries)

    # We'll benchmark run_queries on this workload
    runs = 25
    avg = timeit.timeit(lambda: run_queries(N, mixed_queries), number=runs) / runs
    print(f"Run run_queries(N={N}, |queries|={len(mixed_queries)}) "
          f"{runs} times -> avg {avg:.6f} s/run")

    print("\nNotes:")
    print(" • DSU operations are amortized near O(1); the above timing includes Python overhead.")
    print(" • Space used is O(N) for parent[] and rank[].")
```

### What the program prints

* **Example 1 Output:**

  ```
  0
  1
  ```
* **Example 2 Output:**

  ```
  0
  ```
* A timing line like:

  ```
  Run run_queries(N=10000, |queries|=850) 25 times -> avg 0.0xyz s/run
  ```

  (Exact numbers vary by machine/Python version.)

---

## 6) Real-World Use Cases (the important ones)

1. **Minimum Spanning Tree (Kruskal’s Algorithm)**
   DSU quickly tells whether adding an edge will create a cycle, enabling `O(E log E)` MST.

2. **Dynamic Connectivity / Friend Circles / Social Groups**
   Merge groups on the fly and query “are A and B in the same group?” in near O(1).

3. **Cycle Detection in Undirected Graphs**
   If two endpoints of an edge already have the same root, adding the edge forms a cycle.

4. **Percolation / Image Segmentation / Network Components**
   Union neighboring pixels/nodes to find connected components efficiently.

5. **Equivalence Relations / Type Unification**
   Maintain sets of equivalent items (e.g., compiler unification, constraint solving).