# All numbers with specific difference

**Difficulty:** Hard  
**Accuracy:** 34.44%  
**Submissions:** 5K+  
**Points:** 8  

---

## Problem Statement

Given a positive number **n** and a number **d**, find the **count of positive numbers smaller or equal to n** such that the difference between the number and the **sum of its digits** is **greater than or equal to** the given specific value **d**.

---

## Examples

### Example 1
**Input:**  
`n = 13, d = 2`  

**Output:**  
`4`  

**Explanation:**  
There are 4 numbers satisfying the conditions.  
These are: `10, 11, 12 and 13`.

---

### Example 2
**Input:**  
`n = 14, d = 3`  

**Output:**  
`5`  

**Explanation:**  
There are 5 numbers satisfying the conditions.  
These are: `10, 11, 12, 13 and 14`.

---

## Constraints

- `1 ≤ n ≤ 10^9`
- `1 ≤ d ≤ 10^9`

---

## Expected Complexities

- **Time Complexity:** `O(log n)`
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Mathematical  
- Binary Search  
- Algorithms  

---

## Related Articles

- **Count Numbers Difference Number Digit Sum Greater Specific Value**

---

---

## 2) Text explanation (key trick)

We want to count numbers `x` such that:

* `1 ≤ x ≤ n`
* `x - digitSum(x) ≥ d`

Rearrange:

* `x ≥ d + digitSum(x)`

### Why binary search works

As `x` increases, `x - digitSum(x)` **never decreases** (it’s monotonic non-decreasing).
Intuition: when you do `x -> x+1`, the value increases by `+1` but digit sum usually increases small, sometimes drops on carry (e.g., 199→200 digit sum drops). So `x - digitSum(x)` increases or stays.

Because it’s monotonic, we can find the **smallest x** that satisfies the condition.
Let that smallest valid number be `first_ok`.
Then all numbers from `first_ok ... n` are valid.

So answer is:

* `0` if no valid number exists
* else `n - first_ok + 1`

Constraints are up to `1e9`, so `O(log n)` binary search is perfect.

---

## Step-by-step dry run

### Example 1: `n = 13, d = 2`

We need `x - digitSum(x) ≥ 2`.

Check quickly:

* `1..9`: `x - digitSum(x) = 0` (not enough)
* `10`: digitSum=1 → 10-1 = 9 ✅
  So the first valid is `10`.

Then valid numbers are `10,11,12,13` → count = `13 - 10 + 1 = 4`.

### Binary search view (high-level)

Search in `[1, 13]` for first `x` s.t. `x - digitSum(x) >= 2`:

* mid=7: 7-7=0 ❌ → go right
* mid=10: 10-1=9 ✅ → go left to find earlier
* mid=9: 9-9=0 ❌ → go right
  So first_ok = 10.

Answer = 4 ✅

---

## 3) Python solutions (brute + optimized)

### Helper: digit sum

```python
def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
```

---

### A) Brute force (too slow for 1e9, only for understanding)

**Time:** `O(n * digits)`
**Space:** `O(1)`

```python
class Solution:
    def getCount(self, n, d):
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        count = 0
        for x in range(1, n + 1):
            if x - digit_sum(x) >= d:
                count += 1
        return count
```

---

### B) Most expected (Optimal): Binary Search for first valid x

**Time:** `O(log n * digits)` → effectively `O(log n)`
**Space:** `O(1)`

```python
class Solution:
    def getCount(self, n, d):
        # Compute digit sum in O(number_of_digits)
        # Time: O(log10(x)), Space: O(1)
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        # Check function: is x valid?
        # Time: O(digits), Space: O(1)
        def is_valid(x):
            return x - digit_sum(x) >= d

        # Binary search for smallest x in [1..n] that is valid
        # Time: O(log n) checks, each check O(digits)
        left, right = 1, n
        first_ok = -1

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                first_ok = mid       # mid works, try to find smaller
                right = mid - 1
            else:
                left = mid + 1       # mid doesn't work, go bigger

        # If none found, answer is 0
        if first_ok == -1:
            return 0

        # All numbers from first_ok to n are valid
        return n - first_ok + 1
```

---

### C) Small optimization: start search near n - 9*digits

Because digitSum(x) ≤ 9 * number_of_digits(x).
For n up to 1e9, digits <= 10, so max digit sum is 90.
So if `x - digitSum(x) >= d`, then roughly `x >= d` anyway, but we can tighten left bound:

`x - 9*digits(n) >= d  => x >= d + 9*digits(n)` isn’t always safe as tight bound, but we can use:
`left = max(1, d)` as a safe starting point (works, but binary search is already fast).

---

## 4) Interview quick recall + expected Q&A

### How to remember quickly (mnemonic)

**“Monotonic → First True → Count suffix”**

1. Condition: `x - sumDigits(x) >= d`
2. It’s monotonic non-decreasing with `x`
3. Binary search first `x` that passes
4. Answer = `n - first + 1`

### 5-line pseudo template

```text
f(x) = x - digitSum(x)
binary search smallest x in [1..n] with f(x) >= d
if not found: return 0
return n - x + 1
```

---

## Expected interviewer questions & answers

**Q1) Why binary search works here?**
**A:** Because `f(x)=x-digitSum(x)` is monotonic non-decreasing as x increases, so the predicate `f(x) >= d` is “false…false…true…true”.

**Q2) What’s the complexity?**
**A:** `O(log n)` iterations; each needs digit sum `O(digits)` (≤10 for 1e9), so very fast.

**Q3) Can `f(x)` ever decrease?**
**A:** No. When x increases by 1, digit sum increases slightly or drops on carry, so `x - digitSum(x)` increases or stays.

**Q4) Why answer is `n - first_ok + 1`?**
**A:** Once the predicate becomes true at `first_ok`, it stays true for all larger x up to n.

**Q5) Edge cases?**
**A:** If no number satisfies condition (e.g., very large d), return 0. Works also when first_ok = 1.

---

---

## 5) Real-world use cases (few, very relatable)

1. **Fraud / anomaly scoring with a “digit-sum penalty”**

   * Some scoring systems penalize numbers with “high digit sums” (proxy for patterns), and you want to count how many IDs/scores exceed a threshold after penalty.

2. **Rule-based filtering on large integer ranges**

   * When evaluating a condition over `[1..n]` is expensive, you look for monotonic properties to count valid items fast (binary-search first valid, then count suffix).

3. **Capacity / quota thresholds with a small correction factor**

   * Think of `x - correction(x) >= d`, where `correction(x)` is bounded and easy (digit sum). Many systems use similar “base - adjustment” thresholds.

---

## 6) Full Python program (timed) + inline complexity notes + sample I/O

### Input format

* Line 1: `n d`

### Output

* Count of numbers `x (1..n)` such that `x - digitSum(x) >= d`

> Execution time printed to **stderr** so stdout stays clean.

```python
import sys
import time

class Solution:
    def getCount(self, n, d):
        """
        Count numbers x in [1..n] such that x - digitSum(x) >= d.

        Approach: Binary search the smallest x that satisfies predicate,
        then answer = n - x + 1.

        Time Complexity:
          - Binary search: O(log n) iterations
          - Each check computes digit sum: O(number_of_digits) <= 10 for n<=1e9
          => Overall: O(log n)

        Auxiliary Space: O(1)
        """

        # Compute digit sum of x
        # Time: O(digits), Space: O(1)
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        # Predicate: is x valid?
        # Time: O(digits), Space: O(1)
        def is_valid(x):
            return x - digit_sum(x) >= d

        # Step 1: Binary search for first valid x in [1..n]
        # Time: O(log n) checks, Space: O(1)
        left, right = 1, n
        first_ok = -1

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                first_ok = mid       # mid works, try smaller
                right = mid - 1
            else:
                left = mid + 1       # mid fails, need bigger

        # Step 2: If no valid number, return 0
        # Time: O(1)
        if first_ok == -1:
            return 0

        # Step 3: Count all valid numbers from first_ok to n
        # Time: O(1)
        return n - first_ok + 1


def main():
    """
    Input:
      n d

    Output:
      count

    Example:
      Input:  13 2
      Output: 4
    """
    start_time = time.perf_counter()  # full program runtime timer

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Step A: Parse input
    # Time: O(1), Space: O(1)
    n = int(data[0])
    d = int(data[1])

    solver = Solution()

    # Step B: Solve
    # Time: O(log n), Space: O(1)
    ans = solver.getCount(n, d)

    # Step C: Print output
    # Time: O(1)
    print(ans)

    end_time = time.perf_counter()
    # Print runtime to stderr so it doesn't affect expected stdout
    print(f"[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
13 2

Expected Output:
4

Explanation:
Valid numbers are 10, 11, 12, 13.
"""
```

