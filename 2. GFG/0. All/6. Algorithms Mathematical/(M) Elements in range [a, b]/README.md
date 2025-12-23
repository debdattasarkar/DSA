# Elements in range [a, b]

**Difficulty:** Medium
**Accuracy:** 64.1%
**Submissions:** 7K+
**Points:** 4

## Problem Statement

Given an unsorted array **arr[]** and a 2D array **queries[][]** of size **q**, where each query is in the form of **[a, b]**. For each query, **count how many elements in arr[] lie within the range [a, b]**, i.e., elements satisfying **a ≤ x ≤ b**.

Return the results for all queries as a list of integers, where each integer corresponds to the count of elements in the respective query range.

---

## Examples

### Example 1

**Input:**
arr[] = [1, 4, 2, 8, 5], queries[][] = [[1, 4], [3, 6], [0, 10]]

**Output:**
[3, 2, 5]

**Explanation:**
Query [1, 4]: Elements in range → [1, 4, 2] → Count = 3
Query [3, 6]: Elements in range → [4, 5] → Count = 2
Query [0, 10]: All elements → [1, 4, 2, 8, 5] → Count = 5

---

### Example 2

**Input:**
arr[] = [10, 20, 30, 40, 50], queries[][] = [[5, 15], [25, 45], [10, 50]]

**Output:**
[1, 2, 5]

**Explanation:**
Query [5, 15]: Elements in range → [10] → Count = 1
Query [25, 45]: Elements in range → [30, 40] → Count = 2
Query [10, 50]: Elements in range → [10, 20, 30, 40, 50] → Count = 5

---

## Constraints

* 1 ≤ arr.size(), q ≤ 10<sup>5</sup>
* 0 ≤ arr[i] ≤ 10<sup>6</sup>
* 0 ≤ queries[i][0] ≤ queries[i][1] ≤ 10<sup>6</sup>

---

## Expected Complexities

* **Time Complexity:** O(n log n + q log n)
* **Auxiliary Space:** O(1)

---

## Topic Tags

* Binary Search
* Algorithms

---

## Related Articles

* Count Elements In Range Queries

---

---

## Intuition

You’re given a fixed (static) unsorted array `arr`, and many queries `[a, b]`.
For each query you need: **how many elements `x` satisfy `a ≤ x ≤ b`**.

Two common interview-friendly approaches:

1. **Brute force:** For each query, scan the whole array and count.
2. **Optimized (most expected):** Sort the array once, then for each query use **two binary searches**:

   * first index where value `>= a`  (lower bound)
   * first index where value `> b`   (upper bound)
     Answer = `upper_bound(b) - lower_bound(a)`.

---

## Step-by-step Dry Run (using Example 1)

**arr = [1, 4, 2, 8, 5]**
**queries = [[1, 4], [3, 6], [0, 10]]**

### Optimized idea: Sort + binary search

1. Sort `arr`:

* `sorted_arr = [1, 2, 4, 5, 8]`

2. For each query `[a, b]`, compute:

* `left = first index with value >= a`
* `right = first index with value > b`
* count = `right - left`

---

### Query 1: `[1, 4]`

* `left = lower_bound(1)` in `[1,2,4,5,8]` → index `0` (value 1)
* `right = upper_bound(4)` → index `3` (points to value 5; elements ≤4 are indices 0..2)
* count = `3 - 0 = 3` → elements are `[1, 2, 4]`

### Query 2: `[3, 6]`

* `left = lower_bound(3)` → index `2` (value 4)
* `right = upper_bound(6)` → index `4` (points to value 8; elements ≤6 are indices 0..3)
* count = `4 - 2 = 2` → elements are `[4, 5]`

### Query 3: `[0, 10]`

* `left = lower_bound(0)` → index `0`
* `right = upper_bound(10)` → index `5` (end)
* count = `5 - 0 = 5` → all elements

**Final output:** `[3, 2, 5]`

---

# Python Codes (Brute + Optimized) — interview-style, meaningful names

## 1) Brute Force (easy, but slow)

**Time:** `O(q*n)`
**Space:** `O(1)`

```python
class Solution:
    def cntInRange(self, arr, queries):
        # Brute force: for each query, scan entire array
        results = []

        for left_val, right_val in queries:
            count_in_range = 0
            for num in arr:
                if left_val <= num <= right_val:
                    count_in_range += 1
            results.append(count_in_range)

        return results
```

---

## 2) Optimized (Most expected): Sort once + 2 Binary Searches per query

**Time:** `O(n log n + q log n)`
**Space:** `O(1)` extra (ignoring sort’s internal usage)

```python
from bisect import bisect_left, bisect_right

class Solution:
    def cntInRange(self, arr, queries):
        # Sort once so we can binary search ranges quickly
        sorted_arr = sorted(arr)

        results = []
        for left_val, right_val in queries:
            # first position where value >= left_val
            left_index = bisect_left(sorted_arr, left_val)

            # first position where value > right_val
            right_index = bisect_right(sorted_arr, right_val)

            # elements in [left_val, right_val] are within [left_index, right_index)
            results.append(right_index - left_index)

        return results
```

Why `bisect_right` for `b`?
Because we want **inclusive** `<= b`. `bisect_right` returns the index **after the last `b`**.

---

## 3) Alternative Optimized (when values are bounded): Frequency + Prefix Sum

If `arr[i]` and query values are within `0..10^6`, you can do:

* Build frequency array
* Build prefix sum
* Each query becomes O(1)

**Time:** `O(n + MAX + q)`
**Space:** `O(MAX)` (here ~ 1e6)

```python
class Solution:
    def cntInRange(self, arr, queries):
        # Works great if max value is not too large (here up to 1e6)
        if not arr and not queries:
            return []

        max_value = 0
        for x in arr:
            if x > max_value:
                max_value = x
        for a, b in queries:
            if b > max_value:
                max_value = b

        # freq[v] = how many times value v appears
        freq = [0] * (max_value + 1)
        for x in arr:
            freq[x] += 1

        # prefix[v] = count of elements with value <= v
        prefix = [0] * (max_value + 1)
        running = 0
        for v in range(max_value + 1):
            running += freq[v]
            prefix[v] = running

        results = []
        for a, b in queries:
            if a == 0:
                results.append(prefix[b])
            else:
                results.append(prefix[b] - prefix[a - 1])

        return results
```

When to mention this in interviews:

* “If values are small/bounded, we can do prefix counts for O(1) queries.”

---

# How to remember and present it quickly in an interview

### The 10-second plan

1. “Many range count queries on static array → preprocess.”
2. “Sort the array once.”
3. “For each query `[a,b]`, answer = `upper_bound(b) - lower_bound(a)`.”
4. “That’s `O(n log n + q log n)`.”

### Mnemonic

**“Sort → Two Bisections → Subtract.”**

* Left boundary: `>= a`
* Right boundary: `> b`
* Subtract indices

---

# Interviewer-style Q&A (common follow-ups)

**Q1. Why do we sort the array?**
A. Sorting enables binary searching the boundary positions for any value range. Then each query is `O(log n)` instead of scanning `O(n)`.

**Q2. How do you count elements in `[a, b]` using binary search?**
A. Find:

* `L = first index with value >= a` (lower bound)
* `R = first index with value > b` (upper bound)
  Count = `R - L`.

**Q3. Why `upper_bound(b)` and not `lower_bound(b)`?**
A. Range is inclusive (`<= b`). `upper_bound(b)` returns index after the last `b`, which correctly counts duplicates of `b`.

**Q4. What’s the time complexity of the optimized solution?**
A. Sorting: `O(n log n)`. Each query: `O(log n)`. Total: `O(n log n + q log n)`.

**Q5. What edge cases should we handle?**
A.

* `a > b` (if possible) → answer 0 (though constraints often ensure `a <= b`)
* `arr` contains duplicates → handled naturally by bisect
* query outside range (e.g., `[0, 10^6]`) → bisect returns boundaries safely

**Q6. Can we do better than `O(q log n)` per query?**
A. Yes, if values are bounded (like up to `10^6`), use frequency + prefix sums to answer each query in `O(1)`, at the cost of `O(MAX)` memory.

**Q7. Why is brute force not acceptable here?**
A. With `n, q` up to `1e5`, brute force can be `1e10` operations, which is too slow.

---

---

## 5) Real-World Use Cases (few, relatable)

1. **E-commerce “Price filter” analytics**
   Given a list of product prices, answer queries like “How many products are priced between ₹500 and ₹1000?” (fast filtering + showing counts on UI).

2. **Monitoring / SRE (latency SLO checks)**
   From a big batch of API latencies, answer “How many requests were between 200ms and 500ms?” across multiple dashboards quickly.

3. **Finance / Trading (price band / volume in range)**
   From a list of executed trade prices, queries like “How many trades happened in the ₹195–₹205 band?” (market microstructure analysis).

4. **Manufacturing / IoT (sensor tolerances)**
   From sensor readings, queries like “How many readings are within acceptable tolerance [a,b]?” (quality checks).

---

## 6) Full Program (timed run + inline complexity comments + sample I/O)

Below is a complete Python program using the **optimized interview-expected approach** (Sort + 2 binary searches per query).
It supports:

* **Demo mode** (no stdin): runs the sample input and prints output
* **Input mode** (stdin): supports common competitive formats:

  * `n, arr, q, q pairs` (single test)
  * or `t` testcases (each testcase same format)

```python
import sys
import time
from bisect import bisect_left, bisect_right


class Solution:
    def cntInRange(self, arr, queries):
        """
        Optimized approach:
        - Sort array once.
        - For each query [a, b], answer = upper_bound(b) - lower_bound(a)

        Overall Time: O(n log n + q log n)
        Extra Space: O(n) for sorted copy (Python's sorted creates a new list)
        """

        # Step 1: sort once
        # Time: O(n log n), Space: O(n)
        sorted_arr = sorted(arr)

        results = []
        # Step 2: answer each query using 2 binary searches
        # Each query time: O(log n), Total query time: O(q log n)
        # Extra space for results: O(q)
        for left_val, right_val in queries:
            left_index = bisect_left(sorted_arr, left_val)     # first index with value >= left_val
            right_index = bisect_right(sorted_arr, right_val)  # first index with value > right_val
            results.append(right_index - left_index)

        return results


def try_parse_multi_test(tokens):
    """
    Try parse format:
    t
    n
    n integers (arr)
    q
    q pairs (a b)

    Returns: list of (arr, queries) if successful else None
    """
    if not tokens:
        return None

    idx = 0
    t = tokens[idx]
    idx += 1
    testcases = []

    for _ in range(t):
        if idx >= len(tokens):
            return None

        n = tokens[idx]
        idx += 1

        if idx + n > len(tokens):
            return None
        arr = tokens[idx: idx + n]
        idx += n

        if idx >= len(tokens):
            return None
        q = tokens[idx]
        idx += 1

        if idx + 2 * q > len(tokens):
            return None
        queries = []
        for _ in range(q):
            a = tokens[idx]
            b = tokens[idx + 1]
            idx += 2
            queries.append([a, b])

        testcases.append((arr, queries))

    # If there are extra tokens left, this parse likely isn't correct
    if idx != len(tokens):
        return None

    return testcases


def parse_single_test(tokens):
    """
    Parse format:
    n
    n integers (arr)
    q
    q pairs (a b)

    Returns: (arr, queries)
    """
    idx = 0
    n = tokens[idx]
    idx += 1

    arr = tokens[idx: idx + n]
    idx += n

    q = tokens[idx]
    idx += 1

    queries = []
    for _ in range(q):
        a = tokens[idx]
        b = tokens[idx + 1]
        idx += 2
        queries.append([a, b])

    return arr, queries


def main():
    # Measure entire program runtime (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        # Sample Input:
        # arr = [1, 4, 2, 8, 5]
        # queries = [[1, 4], [3, 6], [0, 10]]
        arr = [1, 4, 2, 8, 5]
        queries = [[1, 4], [3, 6], [0, 10]]

        # Time: O(n log n + q log n)
        result = solver.cntInRange(arr, queries)

        # Print input + output clearly
        print("Input:")
        print("arr =", arr)
        print("queries =", queries)
        print("\nOutput:")
        print(result)

    else:
        # ---------------- INPUT MODE ----------------
        # Read all integers
        # Time: O(total_tokens), Space: O(total_tokens)
        tokens = list(map(int, data.split()))

        # Try multi-test first, else fallback to single-test
        testcases = try_parse_multi_test(tokens)
        if testcases is None:
            # Single test
            arr, queries = parse_single_test(tokens)
            result = solver.cntInRange(arr, queries)
            print(*result)  # print as space-separated counts
        else:
            # Multiple tests
            for arr, queries in testcases:
                result = solver.cntInRange(arr, queries)
                print(*result)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Example demo output (when you run with no stdin)

* It will print the sample `arr`, `queries`, and output `[3, 2, 5]`, plus total runtime in ms.
