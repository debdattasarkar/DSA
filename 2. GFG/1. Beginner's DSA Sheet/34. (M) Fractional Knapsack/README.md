
---

# Fractional Knapsack 👜

**Difficulty:** Medium
**Accuracy:** 32.46%
**Submissions:** 358K+
**Points:** 4

---

## Problem Statement

Given two arrays, `val[]` and `wt[]`, representing the values and weights of items, and an integer `capacity` representing the maximum weight a knapsack can hold, determine the **maximum total value** that can be achieved by putting items in the knapsack.

You are allowed to **break items into fractions** if necessary.

Return the **maximum value as a double**, rounded to **6 decimal places**.

---

## Examples

### Example 1:

**Input:**

```
val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
```

**Output:**

```
240.000000
```

**Explanation:**
By taking items of weight 10 and 20, and 2/3 fraction of 30 kg.
Hence, total price = `60 + 100 + (2/3)(120) = 240`.

---

### Example 2:

**Input:**

```
val[] = [500], wt[] = [30], capacity = 10
```

**Output:**

```
166.670000
```

**Explanation:**
Since the item’s weight (30) exceeds capacity (10),
we take a fraction `10/30` of it, yielding value = `500 * (10/30) = 166.67`.

---

## Constraints

* `1 ≤ val.size = wt.size ≤ 10^5`
* `1 ≤ capacity ≤ 10^9`
* `1 ≤ val[i], wt[i] ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Microsoft

---

## Topic Tags

* Greedy
* Algorithms

---

## Related Articles

* [Fractional Knapsack Problem](https://www.geeksforgeeks.org/fractional-knapsack-problem/)

---

---

# Fractional Knapsack — interview-style guide (Python)

## Problem recap

You’re given:

* `val[i]`: value of item `i`
* `wt[i]`: weight of item `i`
* `capacity`: capacity of the knapsack

You **may take fractions** of items. Return the **maximum total value**, rounded to **6 decimals**.

Greedy key insight: when fractions are allowed, always take items in **decreasing value-to-weight ratio** (`v/w`). This is provably optimal (exchange argument below).

---

## Step-by-step solution idea

1. Compute each item’s ratio `r = val[i]/wt[i]`.
2. Sort items by `r` descending.
3. Traverse this order:

   * If the whole item fits, take it and decrease remaining capacity.
   * Otherwise take just the fraction that fits and stop.
4. Round to 6 decimals.

**Time:** `O(n log n)` for sorting
**Space:** `O(n)` for the list of (ratio, v, w)

---

## Dry run (walkthrough)

### Example 1

`val=[60,100,120], wt=[10,20,30], capacity=50`

Ratios:

* item0: `60/10 = 6`
* item1: `100/20 = 5`
* item2: `120/30 = 4`

Order: `(6),(5),(4)`

* Take item0 fully: value `+60`, remaining `40`.
* Take item1 fully: value `+100`, remaining `20`.
* Item2 (w=30) doesn’t fully fit. Take `20/30` of it: value `+120*(20/30)=+80`.
* Total `= 60+100+80 = 240.000000`.

### Example 2

`val=[500], wt=[30], capacity=10`
Ratio `= 16.666…`
Take `10/30` of it → `500*(10/30)=166.6667` (rounded to 6 decimals).

---

## Python implementations (brute & optimized)

```python
class Solution:
    # Optimized Greedy (sort by value/weight)
    def fractionalKnapsack(self, val, wt, capacity):
        """
        Time:  O(n log n) due to sorting
        Space: O(n) to store (ratio, value, weight)
        """
        items = [(val[i]/wt[i], val[i], wt[i]) for i in range(len(val))]
        items.sort(key=lambda x: x[0], reverse=True)  # by ratio desc

        total, remaining = 0.0, capacity
        for ratio, v, w in items:
            if remaining == 0:
                break
            if w <= remaining:         # take whole item
                total += v
                remaining -= w
            else:                      # take fractional part and stop
                total += v * (remaining / w)
                remaining = 0
                break

        return round(total, 6)

    # Brute/Easy (no sort; repeatedly pick best ratio by linear scan)
    def fractionalKnapsack_brutish(self, val, wt, capacity):
        """
        Time:  O(k*n) (worst-case O(n^2)), Space: O(n)
        Repeatedly find the unused max-ratio item by scanning.
        """
        n, used = len(val), [False]*len(val)
        total, remaining = 0.0, capacity

        while remaining > 0:
            best, idx = -1.0, -1
            for i in range(n):
                if not used[i]:
                    r = val[i]/wt[i]
                    if r > best:
                        best, idx = r, i
            if idx == -1:  # nothing left
                break

            used[idx] = True
            if wt[idx] <= remaining:
                total += val[idx]
                remaining -= wt[idx]
            else:
                total += val[idx] * (remaining / wt[idx])
                remaining = 0
                break

        return round(total, 6)

    # Heap-based Greedy (priority queue by ratio)
    def fractionalKnapsack_heap(self, val, wt, capacity):
        """
        Time:  O(n log n), Space: O(n)
        Uses a max-heap (implemented as negatives in Python).
        """
        import heapq
        heap = [(-(v/w), v, w) for v, w in zip(val, wt)]
        heapq.heapify(heap)

        total, remaining = 0.0, capacity
        while heap and remaining > 0:
            _, v, w = heapq.heappop(heap)
            if w <= remaining:
                total += v
                remaining -= w
            else:
                total += v * (remaining / w)
                remaining = 0
        return round(total, 6)
```

---

## Expected interviewer Q\&A

* **Q: Why does the greedy ratio sort work?**
  **A:** With fractions allowed, any solution can be transformed (exchange argument) to one where higher `v/w` items are never replaced by lower `v/w` weight while not decreasing value. Thus, taking from highest `v/w` first is optimal.

* **Q: What’s the complexity?**
  **A:** Sorting `n` items → `O(n log n)` time, `O(n)` extra space. The picking loop is `O(n)`.

* **Q: How does this differ from 0/1 knapsack?**
  **A:** 0/1 knapsack **disallows fractions** and requires DP (`O(n*W)` or `O(n*V)` or optimized variants). Greedy by ratio is **not** optimal for 0/1.

* **Q: Any corner cases?**
  **A:** `capacity == 0` ⇒ answer 0. All weights are positive (common constraint). If capacity ≥ sum of all weights, take all items.

* **Q: Can we avoid sorting?**
  **A:** Yes—use a **max-heap** by ratio (still `O(n log n)`), or a simple **repeated scan** (`O(n^2)`) for easy implementation.

* **Q: Stability/precision?**
  **A:** Use float arithmetic; finally `round(ans, 6)` as required.

---

## Full program with inline complexity notes + timing

I’ve executed the following program so you can see real output and timings.

\[Open the run output above ⬆️]

It:

* Implements `Solution.fractionalKnapsack` (optimized), `fractionalKnapsack_heap`, and a simple `fractionalKnapsack_brutish`.
* Runs the two sample cases.
* Uses `timeit.default_timer()` to time one full run of each version on generated data (smaller `n` for the `O(n^2)` method).

You can copy the code shown in the run for your local use; it already prints results and per-method timings.

---

## Real-world use cases (a few high-impact ones)

* **Cargo loading with divisible goods** (grain, fuel, chemicals): load by highest profit per kg/liter first.
* **Bandwidth allocation**: split limited bandwidth among data streams based on value per Mbps.
* **Budget allocation**: fund fractions of initiatives ranked by value per dollar until the budget is exhausted.
* **Manufacturing blends**: choose proportions of inputs (ore grades, ingredients) to maximize value under capacity/weight limits.

---

---

All set! I’ve created and executed a **full, self-contained Python program** that:

* Implements optimized, heap, and easy (brutish) versions.
* Prints **inputs and outputs** for the sample cases.
* Includes **inline comments** with **time/space complexity** at each step.
* Uses `timeit.default_timer()` to report the **total runtime of the main program**, plus a small extra timing on a random test.

**Download the script:** [fractional\_knapsack\_full.py](fractional_knapsack_full.py)

You can run it as-is:

```bash
python3 fractional_knapsack_full.py
```

You’ll see the same outputs that were printed above (including the total main runtime).

---

## 6) Real-World Use Cases (high impact)

* **Divisible cargo loading:** Load grain/fuel/chemicals into a vehicle or tank by **highest profit per unit weight/volume** until capacity is hit.
* **Bandwidth allocation:** Split limited bandwidth across streams by **value per Mbps**, allowing fractional allocation.
* **Budgeting/portfolio slices:** Allocate part of a budget across initiatives or assets by **value per dollar**, funding fractional portions.
* **Manufacturing blends:** Choose proportions of inputs (e.g., ore grades, ingredients) to maximize output value under capacity constraints.

If you want the same program in **C++** with precise I/O formatting for common judges (GfG/LeetCode style), say the word and I’ll drop it in.
