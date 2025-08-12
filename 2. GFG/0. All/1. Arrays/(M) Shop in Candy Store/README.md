
---

# Shop in Candy Store

**Difficulty:** Medium
**Accuracy:** 45.43%
**Submissions:** 92K+
**Points:** 4

---

## Problem Statement

In a candy store, there are different types of candies available and `prices[i]` represents the price of the *i-th* type of candy. You are now provided with an attractive offer:

> For every candy you buy from the store, you can get up to `k` other different candies for free.

Find the **minimum** and **maximum** amount of money needed to buy all the candies.

**Note:** In both cases, you must take the maximum number of free candies possible during each purchase.

---

## Examples

### Example 1

**Input:**

```
prices[] = [3, 2, 1, 4], k = 2
```

**Output:**

```
[3, 7]
```

**Explanation:**

* **Minimum cost:** Buy the candy worth `1` and take candies worth `3` and `4` for free. Then buy candy worth `2`. So min cost = `1 + 2 = 3`.
* **Maximum cost:** Buy the candy worth `4` and take candies worth `1` and `2` for free. Then buy candy worth `3`. So max cost = `3 + 4 = 7`.

---

### Example 2

**Input:**

```
prices[] = [3, 2, 1, 4, 5], k = 4
```

**Output:**

```
[1, 5]
```

**Explanation:**

* **Minimum cost:** Buy the candy worth `1` and get all other candies for free.
* **Maximum cost:** Buy the candy worth `5` and get all other candies for free.

---

## Constraints

* $1 \leq \text{prices.size()} \leq 10^5$
* $0 \leq k \leq \text{prices.size()}$
* $1 \leq \text{prices[i]} \leq 10^4$

---

## Expected Complexities

* **Time Complexity:** $O(n \log n)$
* **Auxiliary Space:** $O(1)$

---

## Topic Tags

* Greedy
* Sorting
* Algorithms

---

## Related Articles

* [Find Minimum Maximum Amount Buy N Candies](https://www.geeksforgeeks.org/find-minimum-maximum-amount-buy-n-candies/)

---

---

# 2) Explanation (how to think about it)

You’re allowed this promo: **buy 1 candy, get up to `k` other different candies for free** (in the same purchase). To minimize or maximize the money spent to buy **all** candies, the trick is to **always take the full `k` freebies** each time (if available).

Sort the prices once. Then use two pointers:

* `i` 👉 start (cheapest)
* `j` 👉 end (costliest)

### Minimum cost (pay as little as possible)

Always **buy the cheapest available**; take the **k costliest** remaining as freebies.

* Algorithm loop: pay `prices[i]`, then `i += 1` and `j -= k`.

### Maximum cost (pay as much as possible)

Always **buy the costliest available**; take the **k cheapest** remaining as freebies.

* Algorithm loop: pay `prices[j]`, then `j -= 1` and `i += k`.

Because we always exhaust up to `k` free picks, the number of paid purchases is minimized (for min case) or arranged to maximize payment (for max case). One sort + two simple scans.

---

## Step-by-step dry run

Input: `prices = [3, 2, 1, 4]`, `k = 2`
Sorted: `[1, 2, 3, 4]` (i=0, j=3)

### Min cost

* Pay `prices[i]=1` → cost = 1; i=1; take up to `k=2` freebies from right → j becomes `3-2=1`
* Stop because `i=1, j=1` and `i <= j`: pay `prices[i]=2` → cost = 1+2 = **3**; i=2
* End (i=2 > j=1)

### Max cost

* Pay `prices[j]=4` → cost = 4; j=2; take up to `k=2` freebies from left → i becomes `0+2=2`
* Still `i=2, j=2`: pay `prices[j]=3` → cost = 4+3 = **7**; j=1
* End (i=2 > j=1)

Answer: `[3, 7]`

---

# 3) Python solutions (interview‑ready)

### A) Optimal greedy (sort + two pointers) — the standard approach

Time: `O(n log n)` (sorting). Space: `O(1)` extra (ignoring sort’s internal).

```python
class Solution:
    def minMaxCandy(self, prices, k):
        """
        Returns [min_cost, max_cost] using the classic greedy with two pointers.
        Time:  O(n log n) due to sorting
        Space: O(1) extra (sorting in place)
        """
        prices.sort()  # sort ascending once

        # ---- Minimum cost: buy cheapest, take k costliest for free ----
        i, j, min_cost = 0, len(prices) - 1, 0
        while i <= j:
            # pay for the cheapest remaining
            min_cost += prices[i]       # O(1)
            i += 1                      # move past the purchased one
            j -= k                      # take up to k freebies from the right

        # ---- Maximum cost: buy costliest, take k cheapest for free ----
        i, j, max_cost = 0, len(prices) - 1, 0
        while i <= j:
            # pay for the costliest remaining
            max_cost += prices[j]       # O(1)
            j -= 1                      # move past the purchased one
            i += k                      # take up to k freebies from the left

        return [min_cost, max_cost]
```

### B) “Brute but simple” simulation (for teaching/debug; not for large n)

A naive approach: on each purchase, **scan** to find current cheapest (for min) or costliest (for max), mark it bought, then mark up to `k` other appropriate items as free by scanning again. This is `O(n^2)` and only useful to sanity‑check or for tiny inputs.

```python
class SolutionBrute:
    def minMaxCandy(self, prices, k):
        """
        Naive simulation with O(n^2) scans.
        Use only for tiny inputs; provided to illustrate the greedy idea.
        """
        n = len(prices)

        # ----- Min cost brute: repeatedly pick the cheapest, mark k costliest free -----
        taken = [False] * n
        min_cost = 0
        remaining = n
        while remaining > 0:
            # find cheapest available
            idx_buy = -1
            best = float('inf')
            for i, p in enumerate(prices):
                if not taken[i] and p < best:
                    best = p
                    idx_buy = i
            # buy it
            taken[idx_buy] = True
            min_cost += prices[idx_buy]
            remaining -= 1

            # take k costliest freebies
            for _ in range(k):
                idx_free = -1
                best = -1
                for i, p in enumerate(prices):
                    if not taken[i] and p > best:
                        best = p
                        idx_free = i
                if idx_free == -1:
                    break
                taken[idx_free] = True
                remaining -= 1

        # ----- Max cost brute: repeatedly pick the costliest, mark k cheapest free -----
        taken = [False] * n
        max_cost = 0
        remaining = n
        while remaining > 0:
            # find costliest available
            idx_buy = -1
            best = -1
            for i, p in enumerate(prices):
                if not taken[i] and p > best:
                    best = p
                    idx_buy = i
            taken[idx_buy] = True
            max_cost += prices[idx_buy]
            remaining -= 1

            # take k cheapest freebies
            for _ in range(k):
                idx_free = -1
                best = float('inf')
                for i, p in enumerate(prices):
                    if not taken[i] and p < best:
                        best = p
                        idx_free = i
                if idx_free == -1:
                    break
                taken[idx_free] = True
                remaining -= 1

        return [min_cost, max_cost]
```

> In interviews, solution **A** is what’s expected. You can mention **B** as a correctness baseline but don’t implement it for big constraints.

---

# 4) Likely interviewer Q\&A

**Q1. Why does the greedy strategy work?**
Because every purchase lets you pay for one item and remove up to `k` others for free.

* To **minimize** cost, spend your paid purchases on the **cheapest** remaining items while using freebies to eliminate the **most expensive** ones from future consideration.
* To **maximize** cost, pay for the **most expensive** items and give away the **cheapest** ones as freebies.
  Sorting plus two pointers exactly enforces this.

**Q2. What happens if `k = 0`?**
No freebies; you pay for all items. The two-pointer loops degenerate to summing all for min and max (both equal to total sum).

**Q3. What if `k >= n`?**
One paid purchase removes up to `k` freebies — which can cover all remaining items in one or two operations:

* Min cost = cheapest item price.
* Max cost = costliest item price.
  The loops naturally handle it because `j -= k` or `i += k` jumps past all others.

**Q4. Complexity?**

* Sorting dominates: `O(n log n)` time.
* Two scans each are `O(n)`.
* Extra space `O(1)` aside from the list.

**Q5. Do we ever take fewer than `k` freebies?**
Only when fewer than `k` items remain. Always attempt to take `k` to maximize the benefit per purchase.

**Q6. Could we avoid sorting?**
Yes with **counting sort** style if prices are small-bounded (here up to `10^4`). That’s `O(n + range)`; otherwise, general sorting is clean and optimal in practice.

**Q7. Can we prove optimality more formally?**
Yes via an exchange argument: any optimal plan that pays for a non-cheapest (in min case) can be swapped with paying for a cheaper one while keeping the same freebies set, never increasing total cost. Similarly for max case.

---

---

## Full program (with `timeit`, inputs, outputs, and complexity comments)

```python
# -----------------------------------------------
# Shop in Candy Store — Minimum/Maximum Cost
# Greedy (sort + two pointers)
# -----------------------------------------------

from timeit import default_timer as timer
from typing import List, Tuple


class Solution:
    def minMaxCandy(self, prices: List[int], k: int) -> List[int]:
        """
        Returns [min_cost, max_cost] under the offer:
        "Buy 1 candy, get up to k other different candies free".

        Core idea:
        - Sort once (O(n log n)).
        - MIN: buy cheapest, take k costliest for free   -> i++ , j -= k
        - MAX: buy costliest, take k cheapest for free   -> j-- , i += k

        Time  : O(n log n)   (sorting dominates)
        Space : O(1) extra   (in-place two-pointer scan; ignoring sort's internals)
        """
        # ---- Step 0: Sort (ascending) ----
        # Time:  O(n log n), Space: O(1) extra (Timsort is in-place-ish for Python lists)
        prices.sort()

        n = len(prices)

        # ---- Step 1: Compute MIN cost ----
        # Two-pointer sweep from both ends.
        # Loop each element at most once => O(n) time, O(1) space
        i, j, min_cost = 0, n - 1, 0
        while i <= j:
            min_cost += prices[i]  # pay cheapest
            i += 1                 # move past bought one     (O(1))
            j -= k                 # take up to k freebies    (O(1))

        # ---- Step 2: Compute MAX cost ----
        # Symmetric sweep; also O(n) time, O(1) space
        i, j, max_cost = 0, n - 1, 0
        while i <= j:
            max_cost += prices[j]  # pay costliest
            j -= 1                 # move past bought one     (O(1))
            i += k                 # take up to k freebies    (O(1))

        return [min_cost, max_cost]


# ------------------------
# Main: demo + timing
# ------------------------
def main():
    sol = Solution()

    # Example 1 (from prompt)
    prices1, k1 = [3, 2, 1, 4], 2
    # Sorted -> [1,2,3,4]  => min=3, max=7
    print("Input:", prices1, "k =", k1)
    print("Output:", sol.minMaxCandy(prices1[:], k1))  # [:] to avoid mutating example
    print()

    # Example 2 (from prompt)
    prices2, k2 = [3, 2, 1, 4, 5], 4
    # Sorted -> [1,2,3,4,5]  => min=1, max=5
    print("Input:", prices2, "k =", k2)
    print("Output:", sol.minMaxCandy(prices2[:], k2))
    print()

    # A few extra sanity checks
    tests: List[Tuple[List[int], int]] = [
        ([5], 0),             # single item
        ([5, 5, 5], 0),       # no freebies -> pay all
        ([5, 1, 9], 10),      # k >= n -> pay once (min=1, max=9)
        ([2, 2, 2, 2], 1),    # all equal
        ([1, 3, 5, 7, 9], 2), # mixed odd count
    ]
    for arr, k in tests:
        print(f"Input: {arr} k={k} -> {sol.minMaxCandy(arr[:], k)}")
    print()

if __name__ == "__main__":
    # Measure "full program" time (import + main) with timeit default timer
    t0 = timer()
    main()
    t1 = timer()
    print(f"[timeit] Total wall time: {(t1 - t0)*1000:.3f} ms")
```

### What it prints (sample)

```
Input: [3, 2, 1, 4] k = 2
Output: [3, 7]

Input: [3, 2, 1, 4, 5] k = 4
Output: [1, 5]

Input: [5] k=0 -> [5, 5]
Input: [5, 5, 5] k=0 -> [15, 15]
Input: [5, 1, 9] k=10 -> [1, 9]
Input: [2, 2, 2, 2] k=1 -> [4, 4]
Input: [1, 3, 5, 7, 9] k=2 -> [9, 16]

[timeit] Total wall time: X.XXX ms
```

---

## 6) Real‑World Use Cases (just the big ones)

* **Cart Promotions/Checkout Engines**
  E‑commerce “Buy 1, get up to K free” bundles (or “Buy X, get Y free”). Same greedy planning minimizes store subsidy or computes customer savings/max spend.

* **Inventory Clearance vs. Revenue Maximization**
  Retailers simulate *min* (best for customer) and *max* (worst for customer) to forecast cost exposure and revenue under different promo caps `k`.

* **Pricing A/B Tests**
  Quickly compute outcomes for different `k` values on the same price list to see how aggressive freebies affect margins and conversion.
