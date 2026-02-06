
# Happiest Triplet

**Difficulty:** Medium  
**Accuracy:** 61.74%  
**Submissions:** 8K+  
**Points:** 4  
**Average Time:** 35m  

---

## Problem Statement

You are given three arrays **a[]**, **b[]**, **c[]** of the same size.  
Find a **triplet** such that the **difference (maximum − minimum)** in that triplet is the **minimum among all possible triplets**.

A triplet must contain:
- **one element from each of the three arrays**.

This triplet is considered the **happiest** among all possible triplets.

### Note
If there are **2 or more triplets** with the same smallest difference, then **the triplet with the smallest sum of its elements should be displayed**.

The result should be printed in **decreasing order**.

---

## Examples

### Example 1
**Input:**  
```

a[] = [5, 2, 8]
b[] = [10, 7, 12]
c[] = [9, 14, 6]

```

**Output:**  
```

[7, 6, 5]

```

**Explanation:**  
The triplet `[5, 7, 6]` has difference `(maximum − minimum) = (7 − 5) = 2`, which is minimum among all triplets.

---

### Example 2
**Input:**  
```

a[] = [15, 12, 18, 9]
b[] = [10, 17, 13, 8]
c[] = [14, 16, 11, 5]

```

**Output:**  
```

[11, 10, 9]

```

**Explanation:**  
Multiple triplets have the same minimum difference, and among them `[11, 10, 9]` has the **smallest sum**, so it is chosen.

---

## Constraints

- `1 ≤ a.size(), b.size(), c.size() ≤ 10^5`
- `1 ≤ a[i], b[i], c[i] ≤ 10^5`

---

## Expected Complexities

- **Time Complexity:** `O(n log n)`
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Arrays  
- Searching  
- Sorting  
- Data Structures  
- Algorithms  

---

## Related Articles

- **Smallest Difference Triplet From Three Arrays**

---

---

## 2) Text explanation (core idea)

We need a triplet `(x from a, y from b, z from c)` such that:

* `diff = max(x,y,z) - min(x,y,z)` is **minimum**
* If multiple triplets have same `diff`, choose the one with **minimum sum** `(x+y+z)`
* Output must be the chosen triplet in **decreasing order**

### Key observation (interview-standard)

If arrays are **sorted**, we can use **3 pointers** (`i, j, k`) to scan them in linear time:

At any moment:

* current triplet = `(a[i], b[j], c[k])`
* compute `current_min`, `current_max`, `diff`, `sum`
* best answer updates if:

  * smaller `diff`, or
  * same `diff` but smaller `sum`
* To reduce `diff`, we should **increase the minimum element**, because:

  * `diff = max - min`
  * decreasing max is impossible with forward pointers (sorted ascending)
  * so move the pointer that points to the current minimum

This gives `O(n)` scan after sorting → overall `O(n log n)`.

---

## Step-by-step dry run (Example 1)

Input:

* `a = [5,2,8]`
* `b = [10,7,12]`
* `c = [9,14,6]`

Sort:

* `a = [2,5,8]`
* `b = [7,10,12]`
* `c = [6,9,14]`

Pointers: `i=j=k=0`

### Step 1: (2, 7, 6)

* min=2, max=7, diff=5, sum=15 → best=(2,7,6)
* min is `2` (from a) → move `i`

### Step 2: (5, 7, 6)

* min=5, max=7, diff=2, sum=18 → better diff → best=(5,7,6)
* min is `5`? Actually min=5 and 6 => min=5 (a) → move `i`

### Step 3: (8, 7, 6)

* min=6, max=8, diff=2, sum=21 → same diff, sum worse → ignore
* min is `6` (c) → move `k`

### Step 4: (8, 7, 9)

* min=7, max=9, diff=2, sum=24 → same diff, sum worse → ignore
* min is `7` (b) → move `j`

### Step 5: (8, 10, 9)

* min=8, max=10, diff=2, sum=27 → worse sum → ignore
* min is `8` (a) → move `i` → i hits end → stop

Best triplet = (5,7,6)
Output in decreasing order: **[7, 6, 5]** ✅

---

## 3) Python solutions (brute + optimized expected)

### A) Brute force (only for understanding)

Try all triplets.

**Time:** `O(n^3)` (too slow for 1e5)
**Space:** `O(1)`

```python
class Solution:
    def smallestDiff(self, a, b, c):
        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = None

        for x in a:
            for y in b:
                for z in c:
                    current_max = max(x, y, z)
                    current_min = min(x, y, z)
                    diff = current_max - current_min
                    s = x + y + z

                    # update based on diff, then sum
                    if diff < best_diff or (diff == best_diff and s < best_sum):
                        best_diff = diff
                        best_sum = s
                        best_triplet = [x, y, z]

        best_triplet.sort(reverse=True)
        return best_triplet
```

---

### B) Most expected (Optimal): Sort + 3 pointers

**Time:** `O(n log n)` due to sorting + `O(n)` scan
**Aux Space:** `O(1)` extra (sorting may use internal memory depending on language)

```python
class Solution:
    def smallestDiff(self, a, b, c):
        # Sort all arrays first
        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0
        n1, n2, n3 = len(a), len(b), len(c)

        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = [0, 0, 0]

        # Move pointers until one array ends
        while i < n1 and j < n2 and k < n3:
            x, y, z = a[i], b[j], c[k]

            current_min = min(x, y, z)
            current_max = max(x, y, z)
            diff = current_max - current_min
            s = x + y + z

            # Update best: smaller diff OR same diff but smaller sum
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                best_triplet = [x, y, z]

            # Move the pointer that has the minimum element
            # because increasing the minimum is the only way to shrink (max - min)
            if current_min == x:
                i += 1
            elif current_min == y:
                j += 1
            else:
                k += 1

        # Output must be in decreasing order
        best_triplet.sort(reverse=True)
        return best_triplet
```

---

### C) Alternative expected approach: Fix two arrays with pointers, binary search in third

Works but usually worse than 3-pointer. Still interview-acceptable.

**Time:** `O(n log n)`
**Space:** `O(1)`

Idea: sort all arrays; for each pair `(a[i], b[j])` pick `c` closest to their range via binary search. (More complex; 3-pointer is best.)

---

## 4) Interview quick recall + expected Q&A

### How to remember quickly

Trigger words: **“minimize max-min across 3 arrays”** → think:
**Sort + 3 pointers** (classic “smallest range covering elements” style)

Mnemonic:
**“Range = max-min → move the MIN pointer”**

### 5-line pseudo template

```text
sort a,b,c
i=j=k=0; best=(diff=inf,sum=inf)
while i,j,k in bounds:
  diff = max(a[i],b[j],c[k]) - min(...)
  update best by diff then sum
  move pointer of the current minimum
return best triplet sorted desc
```

---

## Expected interviewer questions & answers

**Q1) Why do we move the pointer at the minimum element?**
**A:** `diff = max - min`. With sorted arrays, max can only stay or increase if we move any pointer forward. The only chance to reduce diff is to increase the min.

**Q2) What’s the complexity?**
**A:** Sorting: `O(n log n)`. Scan: `O(n)` (each pointer moves at most n times). Total `O(n log n)`.

**Q3) How do you handle tie-breaking?**
**A:** Keep `best_diff` and `best_sum`. Update if `diff < best_diff` OR (`diff == best_diff` and `sum < best_sum`).

**Q4) Why output in decreasing order?**
**A:** Problem requirement; after choosing triplet, sort it in reverse.

**Q5) What if arrays have different sizes?**
**A:** Same logic works; bounds are per-array.

**Q6) Is there any scenario where moving min doesn’t help?**
**A:** It’s still the correct greedy step; if the optimal range exists, advancing min is the only move that can possibly shrink the current range.

---

---

## 5) Real-world use cases (few, very relatable)

1. **Synchronizing 3 data sources by timestamp (logs/sensors/market feeds)**

   * Each array = timestamps from a source. Pick one from each so the time window (`max-min`) is minimal → best “aligned” snapshot.

2. **Nearest matching across 3 services (latency / QoS matching)**

   * Each array = response times from 3 microservices. Choose one request from each to minimize spread → most consistent performance window.

3. **Product pricing / vendor quote alignment**

   * Each array = quotes from 3 vendors. Pick a combination with smallest price spread (max-min) → “closest agreement” among vendors.

---

## 6) Full Python program (timed) + inline complexity notes + sample I/O

### Input format

* Line 1: `n` (size of arrays)
* Line 2: `n` integers of `a`
* Line 3: `n` integers of `b`
* Line 4: `n` integers of `c`

### Output

* The happiest triplet in **decreasing order** (space-separated)

> Execution time is printed to **stderr** to keep stdout clean.

```python
import sys
import time

class Solution:
    def smallestDiff(self, a, b, c):
        """
        Find triplet (one from each array) minimizing (max-min).
        Tie-breaker: smaller sum of elements.
        Output: triplet in decreasing order.

        Time Complexity:
          Sorting: O(n log n)
          3-pointer scan: O(n)
          Total: O(n log n)

        Auxiliary Space:
          O(1) extra (excluding sort internals)
        """
        # Step 1: Sort arrays
        # Time: O(n log n), Space: depends on language sort implementation
        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0
        n1, n2, n3 = len(a), len(b), len(c)

        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = [0, 0, 0]

        # Step 2: 3-pointer scan
        # Time: O(n) because each pointer moves forward at most n times
        # Space: O(1)
        while i < n1 and j < n2 and k < n3:
            x, y, z = a[i], b[j], c[k]

            current_min = min(x, y, z)
            current_max = max(x, y, z)

            diff = current_max - current_min
            s = x + y + z

            # Step 3: Update best using diff, then sum tie-break
            # Time: O(1)
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                best_triplet = [x, y, z]

            # Step 4: Move pointer of the minimum element
            # Reason: only increasing the minimum can potentially reduce (max-min)
            # Time: O(1)
            if current_min == x:
                i += 1
            elif current_min == y:
                j += 1
            else:
                k += 1

        # Step 5: Output requires decreasing order
        # Time: O(1) (only 3 elements)
        best_triplet.sort(reverse=True)
        return best_triplet


def main():
    """
    Reads input, computes happiest triplet, prints it.
    Also prints total runtime to stderr.
    """
    start_time = time.perf_counter()  # full program runtime timer

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Step A: Parse input
    # Time: O(n), Space: O(n)
    n = int(data[0])
    idx = 1

    a = list(map(int, data[idx:idx + n])); idx += n
    b = list(map(int, data[idx:idx + n])); idx += n
    c = list(map(int, data[idx:idx + n])); idx += n

    solver = Solution()

    # Step B: Solve
    # Time: O(n log n), Space: O(1) extra (excluding sort internals)
    ans = solver.smallestDiff(a, b, c)

    # Step C: Print output (stdout)
    # Time: O(1)
    print(" ".join(map(str, ans)))

    end_time = time.perf_counter()
    print(f"[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
3
5 2 8
10 7 12
9 14 6

Expected Output:
7 6 5
"""
```
