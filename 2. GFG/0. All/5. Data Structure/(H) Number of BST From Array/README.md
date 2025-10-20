
---

# 🌳 Number of BST From Array

**Difficulty:** Hard
**Accuracy:** 86.6%
**Submissions:** 411+
**Points:** 8

---

## 🧩 Problem Statement

You are given an integer array **arr[]** containing **distinct elements**.

Your task is to return an array where the **ith element** denotes the **number of unique BSTs** that can be formed **when arr[i] is chosen as the root**.

---

## 🧠 Example

### Example 1

#### Input:

```
arr[] = [2, 1, 3]
```

#### Output:

```
[1, 2, 2]
```

#### Explanation:

| Root | Unique BSTs Possible                                             | Visualization |
| ---- | ---------------------------------------------------------------- | ------------- |
| 1    | Only one BST possible with 1 as root (right subtree has 2 and 3) | ![1 as root]  |
| 2    | Two BSTs possible with 2 as root — (1 left, 3 right)             | ![2 as root]  |
| 3    | Two BSTs possible with 3 as root — (left subtree has 1 and 2)    | ![3 as root]  |

So,
**BSTs with root 1 → 1**,
**BSTs with root 2 → 2**,
**BSTs with root 3 → 2**,
Hence, **Output = [1, 2, 2]**

---

### Example 2

#### Input:

```
arr[] = [2, 1]
```

#### Output:

```
[1, 1]
```

#### Explanation:

* If 1 is root → 2 is in the right subtree (only 1 BST)
* If 2 is root → 1 is in the left subtree (only 1 BST)
* Output → [1, 1]

---

## 🧮 Constraints

| Parameter            | Constraint |
| -------------------- | ---------- |
| `1 ≤ arr.size() ≤ 6` |            |
| `1 ≤ arr[i] ≤ 15`    |            |

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log n) |
| **Auxiliary Space** | O(n)       |

---

## 🧩 Key Concept Explanation

For every element `arr[i]` as the **root**, the number of unique BSTs that can be formed is the product of:

```
num_BSTs(left_subtree_size) × num_BSTs(right_subtree_size)
```

Because in a BST:

* All smaller elements go to the **left subtree**.
* All larger elements go to the **right subtree**.

The total number of **unique BSTs** with `n` distinct elements is given by the **Catalan Number**:

[
C_n = \frac{(2n)!}{(n+1)!n!}
]

For each root position `i`, the number of unique BSTs possible is:
[
C_{i-1} \times C_{n-i}
]

---

## 🧮 Mathematical Relation (Recursive Definition)

```
numBST(n) = Σ numBST(i-1) × numBST(n-i)   for i = 1 to n
```

Base case:

```
numBST(0) = 1, numBST(1) = 1
```

---

## 📚 Topic Tags

* **Binary Search Tree**
* **Mathematical**
* **Algorithms**

---

## 🔗 Related Articles

* **Total Number Of BSTs Using Array Elements**

---

---

Great problem — it’s a tiny Catalan-number gem in BST clothing. Here’s everything you need: intuition, dry run, multiple Python solutions in the requested format, interview crib notes, real-world angles, and a runnable/timed script.

---

## 2) Intuition + Step-by-Step Dry Run

**What are we asked?**
For each value `arr[i]` (all values are **distinct**), if we choose it as the **root** of a BST built from **all** array values, how many **unique BSTs** can be formed?

**Key observation (why Catalan?)**
A BST with distinct keys is fully determined by:

* which keys go to the **left** (all keys **smaller** than root), and
* which keys go to the **right** (all keys **greater** than root).
  The **shape** of the left subtree depends only on how many nodes go left, not on their concrete values (same for right).
  If the left subtree has size `L` and the right subtree size `R`, then:

```
#BSTs_with_this_root = Catalan(L) * Catalan(R)
```

because the left and right shapes are independent.

**How to get L and R for root arr[i]?**
Sort the values once. Let `rank[v]` be the index (0-based) of value `v` in the sorted array.

```
L = rank[arr[i]]
R = n - 1 - L
ans[i] = C[L] * C[R]     (C[k] = k-th Catalan number)
```

### Dry run (Example 1)

`arr = [2, 1, 3]`, `n=3`
Sorted: `[1, 2, 3]` → ranks: `{1:0, 2:1, 3:2}`
Catalan numbers: `C0=1, C1=1, C2=2, ...`

* Root = `2` → `L=1`, `R=1` → `C1*C1 = 1*1 = 1`
* Root = `1` → `L=0`, `R=2` → `C0*C2 = 1*2 = 2`
* Root = `3` → `L=2`, `R=0` → `C2*C0 = 2*1 = 2`

Output (same order as input): `[1, 2, 2]` ✅

### Dry run (Example 2)

`arr = [2, 1]`, sorted `[1,2]`, ranks `{1:0,2:1}`, `C0=1, C1=1`

* Root `2`: `L=1, R=0` → `1*1=1`
* Root `1`: `L=0, R=1` → `1*1=1`
  Output: `[1, 1]` ✅

---

## 3) Python solutions (brute-ish & optimal), with interview-style comments

All variants follow your signature:

```python
class Solution:
    def countBSTs(self, arr):
        # Code here
```

### A) Straightforward & Optimal (sort + Catalan DP)

```python
class Solution:
    def countBSTs(self, arr):
        """
        Strategy:
          1) Sort to get rank of each value -> L (#smaller), R (#greater).
          2) Precompute Catalan numbers up to n.
          3) Answer[i] = C[L] * C[R].

        Time  : O(n log n) for sort + O(n^2) for Catalan DP (or O(n) if using direct formula w/ big ints)
        Space : O(n)
        """
        n = len(arr)
        if n == 0:
            return []

        # 1) ranks
        sorted_vals = sorted(arr)                                 # O(n log n)
        rank = {v: i for i, v in enumerate(sorted_vals)}          # O(n)

        # 2) Catalan numbers up to n
        C = [0] * (n + 1)
        C[0] = 1
        for k in range(1, n + 1):                                 # O(n^2)
            total = 0
            # Ck = sum_{i=0..k-1} (Ci * C_{k-1-i})
            for i in range(k):
                total += C[i] * C[k - 1 - i]
            C[k] = total

        # 3) compute answers
        ans = []
        for x in arr:                                             # O(n)
            L = rank[x]
            R = n - 1 - L
            ans.append(C[L] * C[R])
        return ans
```

**Why interviewers like this one**

* Clean mapping to Catalan numbers.
* Correctly separates *ordering* (rank) from *shape counting*.
* Time and space are clearly argued.

---

### B) “Brute” (recursive Catalan with memo) + ranks

This looks “recursive” (more brute-flavored) but computes the same Catalans.

```python
class Solution:
    def countBSTs(self, arr):
        """
        Brute-ish (recursive Catalan with memo):
          - Still uses L = #smaller, R = #greater via ranks.
          - Computes Catalan(n) by recursion + memoization.

        Time  : O(n^2) overall for all Catalan up to n
        Space : O(n) for memo
        """
        n = len(arr)
        if n == 0:
            return []

        sorted_vals = sorted(arr)
        rank = {v: i for i, v in enumerate(sorted_vals)}

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def cat(k: int) -> int:
            if k <= 1:
                return 1
            s = 0
            for i in range(k):
                s += cat(i) * cat(k - 1 - i)
            return s

        ans = []
        for x in arr:
            L = rank[x]
            R = n - 1 - L
            ans.append(cat(L) * cat(R))
        return ans
```

> Good if they ask you to “derive from the Catalan recurrence on the spot.”

---

### C) If n is small (as in constraints) you can also use direct binomial formula

[
C_n = \frac{1}{n+1}\binom{2n}{n}
]

```python
import math

class Solution:
    def countBSTs(self, arr):
        """
        Catalan via closed-form (binomial coefficients) — exact with Python big ints.
        Time : O(n log n) for sort + O(n) Catalans (math.comb is ~O(n) internally)
        Space: O(n)
        """
        n = len(arr)
        if n == 0:
            return []

        sorted_vals = sorted(arr)
        rank = {v: i for i, v in enumerate(sorted_vals)}

        def catalan(k: int) -> int:
            return math.comb(2*k, k) // (k + 1)

        ans = []
        for x in arr:
            L = rank[x]
            R = n - 1 - L
            ans.append(catalan(L) * catalan(R))
        return ans
```

> Mention this if they probe “can you do it faster than O(n²) DP for Catalan?”.

---

## 4) Interview quick-memory + Q&A

### 5-line pseudo-code (skeleton)

```
sort A; rank[v] = index
precompute Catalan C[0..n]
for each x in A:
    L = rank[x]; R = n-1-L
    ans[i] = C[L] * C[R]
return ans
```

### 60-second recall

* **BST + distinct** ⇒ **left = smaller count, right = greater count**.
* **Independent subtrees** ⇒ multiply **Catalan(L) × Catalan(R)**.
* Use **ranks** from the **sorted** array to get `L` and `R`.
* Precompute **Catalans** once; fill answers.

### Likely questions

* **Q: Why Catalan numbers?**
  A: Number of unique BST shapes with `n` distinct keys equals the `n`-th Catalan number, by the recurrence splitting on the root.

* **Q: Do the actual values matter?**
  A: Only the **relative order** (ranks) matters for BST shape counts.

* **Q: What if duplicates are allowed?**
  A: Problem states **distinct**. With duplicates, standard BST definition breaks or needs a tie policy; counts change.

* **Q: Complexity?**
  A: Sorting `O(n log n)`. Catalan DP `O(n²)` or `O(n)` calls to `math.comb`. Final loop `O(n)`.

* **Q: Can you prove `#BSTs(n) = Catalan(n)`?**
  A: Yes—Catalan recurrence:
  `BST(n) = Σ BST(i) * BST(n-1-i)` over `i=0..n-1` (choose root position), with `BST(0)=BST(1)=1`.

---

## 5) Real-World Use Cases (relatable)

* **Binary search tree shape counting** in randomized algorithms analysis (e.g., average BST height depends on Catalan structures).
* **Compiler parsing / parenthesization counting**: Catalan numbers also count valid parse trees — same recurrence shows up.
* **Network/Tree topology enumeration**: Counting non-isomorphic binary trees with labeled nodes (shapes × label distributions).
* **Testing frameworks**: Knowing the number of unique shapes helps in generating diverse BST test cases without duplication.

(You can say: *“We’re effectively counting binary tree shapes; Catalans appear in many tree-like enumeration tasks.”*)

---

## 6) Full runnable program with timings (using your API)

```python
#!/usr/bin/env python3
"""
Number of BST From Array
------------------------
Given array of DISTINCT elements arr[], for each arr[i] as root,
the number of unique BSTs formed is Catalan(L) * Catalan(R),
where L=#elements smaller than arr[i] and R=#greater than arr[i].

We provide:
  - Optimal solution with Catalan DP (O(n^2) for Catalans) + sort for ranks.
  - Demo, correctness checks on examples, and timing.

Time:
  - sort: O(n log n)
  - Catalan DP: O(n^2)   (or use fast comb-based catalan if preferred)
  - final fill: O(n)

Space:
  - O(n) for ranks and Catalan table
"""

from time import perf_counter
import timeit
from typing import List

class Solution:
    def countBSTs(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return []

        # 1) Sort to get ranks (L=#smaller, R=#greater for each value)
        sorted_vals = sorted(arr)                          # O(n log n)
        rank = {v: i for i, v in enumerate(sorted_vals)}   # O(n)

        # 2) Catalan numbers up to n (DP)
        C = [0] * (n + 1)
        C[0] = 1
        for k in range(1, n + 1):                          # O(n^2)
            s = 0
            for i in range(k):
                s += C[i] * C[k - 1 - i]
            C[k] = s

        # 3) Build answers in original order
        ans = []
        for x in arr:                                      # O(n)
            L = rank[x]
            R = n - 1 - L
            ans.append(C[L] * C[R])
        return ans


# ---------------------------- Demo & Timing ----------------------------

def run_once(arr):
    sol = Solution()
    t0 = perf_counter()
    out = sol.countBSTs(arr)
    t1 = perf_counter()
    print(f"arr = {arr}\nans = {out}\nElapsed = {(t1 - t0)*1e6:.1f} µs\n")

def avg_time(arr, runs=5):
    setup = (
        "from __main__ import Solution, arr\n"
        "sol = Solution()"
    )
    stmt = "sol.countBSTs(arr)"
    return timeit.timeit(stmt=stmt, setup=setup, number=runs, globals={'arr': arr}) / runs

if __name__ == "__main__":
    print("Number of BST From Array\n")

    # Examples from prompt
    run_once([2, 1, 3])  # expected [1, 2, 2]
    run_once([2, 1])     # expected [1, 1]

    # Some extra checks
    run_once([1])        # [1]
    run_once([3, 1, 2, 4])   # ranks: 3->2 => C2*C1=2*1=2, 1->0 => C0*C3=1*5=5, etc.

    big = list(range(1, 13))   # n=12 to show runtime still tiny (Catalan DP O(n^2))
    avg = avg_time(big, runs=10)
    print(f"Average time over 10 runs on n={len(big)}: {avg:.6f} s")

    print("\nComplexities (DP version):")
    print("  Time  : O(n^2) for Catalans + O(n log n) for sort")
    print("  Space : O(n)")
```

**Notes**

* For small `n` (≤6 in your constraints), all versions are instant.
* If you prefer, swap the DP Catalan for the binomial closed-form to get rid of the `O(n^2)` Catalan loop.

---

### One-liner to say before you code

> “For each root we split keys into smaller and greater: sizes `L` and `R`.
> Unique BSTs = `Catalan(L) * Catalan(R)`. I’ll sort to get ranks, precompute Catalans, and fill answers in O(n²) (or O(n) with binomial) after an O(n log n) sort.”


