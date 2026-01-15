# Candy

**Difficulty:** Hard
**Accuracy:** 55.27%
**Submissions:** 47K+
**Points:** 8
**Average Time:** 45m

---

## Problem Statement

There are **n children** standing in a line. Each child is assigned a **rating value** given in the integer array **arr[]**. You are giving candies to these children subject to the following requirements:

* Each child must have **at least one candy**.
* Children with a **higher rating than their neighbors** must get **more candies than their neighbors**.

Your task is to **return the minimum number of candies** you need to distribute such that all the above conditions are satisfied.

> **Note:** The answer will always fit into a **32-bit integer**.

---

## Examples

### Example 1

**Input:**
`arr[] = [1, 0, 2]`

**Output:**
`5`

**Explanation:**
Children at index `0` and `2` will get `2` candies each as their rating is higher than index `1`,
and index `1` will get `1` candy.
Thus total candies = `2 + 1 + 2 = 5`.

---

### Example 2

**Input:**
`arr[] = [1, 2, 2]`

**Output:**
`4`

**Explanation:**
You can allocate candies as follows:

* First child → 1 candy
* Second child → 2 candies
* Third child → 1 candy

The third child gets `1` candy because it satisfies both conditions.
Total candies = `1 + 2 + 1 = 4`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^9`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Arrays
* Greedy
* Divide and Conquer
* Data Structures
* Algorithms

---

## Related Articles

* [**Minimum Number Of Candies Required To Distribute Among Children Based On Given Conditions**](https://www.geeksforgeeks.org/minimum-number-of-candies-required-to-distribute-among-children-based-on-given-conditions/)

---

---

## 2) Text explanation (core idea)

We must give candies such that:

1. Everyone gets **at least 1**
2. If `arr[i] > arr[i-1]` then `candies[i] > candies[i-1]`
3. If `arr[i] > arr[i+1]` then `candies[i] > candies[i+1]`

This is a “local constraints” problem. The standard greedy insight:

* **Left-to-right pass** ensures the “higher than left neighbor” rule.
* **Right-to-left pass** ensures the “higher than right neighbor” rule.
* Take the **max** of the two requirements at each index.

That yields the **minimum** total because we only increase when forced by a neighbor relationship.

---

## Step-by-step Dry Run

### Example 1: `arr = [1, 0, 2]`

Initialize candies = `[1, 1, 1]`

#### Pass 1: Left → Right (fix increasing vs left)

* i=1: arr[1]=0 is not > arr[0]=1 → no change
* i=2: arr[2]=2 > arr[1]=0 → candies[2] = candies[1] + 1 = 2
  Candies now: `[1, 1, 2]`

#### Pass 2: Right → Left (fix increasing vs right)

* i=1: arr[1]=0 is not > arr[2]=2 → no change
* i=0: arr[0]=1 > arr[1]=0 → candies[0] = max(candies[0], candies[1]+1)
  = max(1, 2) = 2
  Candies now: `[2, 1, 2]`

Sum = `2+1+2 = 5` ✅

---

### Example 2: `arr = [1, 2, 2]`

Start candies `[1,1,1]`

Left → Right:

* i=1: 2>1 → candies[1]=2 → `[1,2,1]`
* i=2: 2>2? no → `[1,2,1]`

Right → Left:

* i=1: 2>2? no
* i=0: 1>2? no
  Sum = `1+2+1 = 4` ✅

---

## 3) Python solutions (easy + optimized interview-style)

### A) Brute-ish “fix until stable” (educational, not recommended)

Keep adjusting until no violations.
**Worst time:** can degrade badly (`O(n^2)`), so avoid in interviews.

---

### B) Most expected (Two-pass greedy) ✅

**Time:** `O(n)`
**Space:** `O(n)` (candies array)

```python
class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Everyone gets at least 1 candy
        candies = [1] * n  # Space: O(n)

        # 1) Left to Right: if rating increases, candies must increase
        # Time: O(n)
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1

        # 2) Right to Left: if rating increases from right, fix using max
        # Time: O(n)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Sum candies
        # Time: O(n)
        return sum(candies)
```

> Note: Many platforms accept `O(n)` auxiliary; even though prompt says `O(1)`, the safest interview answer is this one (most common + easiest to prove).

---

### C) Optimized Space (True O(1) extra) — slope counting trick

This is a known optimization: treat ratings as **up slopes** and **down slopes** and sum contributions without storing an array.

**Idea**

* When ratings go up: increase `up_len`
* When go down: increase `down_len`
* For a “mountain”, candies count is:

  * up contributes `1+2+...+up`
  * down contributes `1+2+...+down`
  * peak must be max(up,down) (avoid double counting)
* Reset slopes when trend changes.

**Time:** `O(n)`
**Aux Space:** `O(1)`

```python
class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Helper: sum of 1..k
        def tri(k):
            return k * (k + 1) // 2

        total_candies = 1  # first child gets 1
        up_len = 0         # length of current increasing slope
        down_len = 0       # length of current decreasing slope
        prev_slope = 0     # -1 (down), 0 (flat), +1 (up)

        for i in range(1, n):
            # current slope based on rating comparison
            if arr[i] > arr[i - 1]:
                curr_slope = 1
            elif arr[i] < arr[i - 1]:
                curr_slope = -1
            else:
                curr_slope = 0

            # If we just ended a mountain/valley, finalize its contribution
            if (prev_slope > 0 and curr_slope == 0) or (prev_slope < 0 and curr_slope >= 0):
                total_candies += tri(up_len) + tri(down_len) + max(up_len, down_len)
                up_len = 0
                down_len = 0

            # Expand current slope
            if curr_slope > 0:
                up_len += 1
            elif curr_slope < 0:
                down_len += 1
            else:
                # flat: current child just gets 1
                total_candies += 1

            prev_slope = curr_slope

        # finalize last mountain if exists
        total_candies += tri(up_len) + tri(down_len) + max(up_len, down_len)
        return total_candies
```

---

## 4) Interview memory + expected Q&A

### 5-line pseudo-code template (memorize)

```
candies = [1]*n
for i=1..n-1: if a[i]>a[i-1]: candies[i]=candies[i-1]+1
for i=n-2..0: if a[i]>a[i+1]: candies[i]=max(candies[i], candies[i+1]+1)
return sum(candies)
```

### Mnemonic

**“Two neighbors → two passes”**
or **“L→R fixes left, R→L fixes right.”**

### 60-second recall script

1. “Everyone gets 1.”
2. “Left-to-right ensures higher than left gets more.”
3. “Right-to-left ensures higher than right gets more.”
4. “Use max to satisfy both constraints minimally.”
5. “Sum candies. O(n).”

---

## Expected interviewer questions & crisp answers

**Q1. Why two passes are enough?**
A. Constraints are only with immediate neighbors. L→R enforces left constraint; R→L enforces right constraint. Taking max gives minimal that satisfies both.

**Q2. Why `max()` in the second pass?**
A. Because first pass may have already set a larger value due to left neighbor; we must not reduce it.

**Q3. What about equal ratings?**
A. No “must be greater” constraint, so 1 candy is enough unless forced by the other side.

**Q4. Can you do it in O(1) extra space?**
A. Yes using slope/mountain counting (up/down runs), but two-pass array is the most common and simplest to prove.

**Q5. Edge cases?**
A. n=1 → 1 candy; strictly increasing → 1..n; strictly decreasing → n..1; plateaus handled naturally.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Bonus / reward distribution in a team lineup**

   * People have performance ratings; rules say “better than adjacent teammate must get higher bonus”. Need minimum total budget.

2. **Resource allocation with local fairness constraints**

   * Assign CPU credits / bandwidth tokens across servers arranged in a chain where higher load than neighbors must get more capacity, but keep total minimal.

3. **Gamification / points allocation**

   * Players in a ranked sequence get points; higher rank than neighbors must get more points, but you want minimum total points issued.

4. **School grading incentives**

   * Students in a row get tokens; higher score than neighbor must get more tokens; minimize total tokens given out.

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This runnable program:

* Reads `arr` (ratings)
* Computes minimum candies using the **two-pass greedy** approach (most interview expected)
* Prints input and output
* Prints total runtime for the whole program run using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: ratings array (space-separated)

  * Example: `1 0 2`

If no stdin, demo uses Example 1: `[1, 0, 2]` → output `5`

```python
import sys
import time


class Solution:
    def minCandy(self, arr):
        """
        Two-pass greedy.
        Time: O(n)
        Auxiliary Space: O(n) for candies array
        """
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: Everyone gets at least 1 candy
        # Time: O(n), Space: O(n)
        candies = [1] * n

        # Step 2: Left -> Right pass
        # If rating increases compared to left neighbor, increase candies
        # Time: O(n), Space: O(1) extra
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right -> Left pass
        # If rating increases compared to right neighbor, ensure candies[i] > candies[i+1]
        # Use max because we must not break left->right constraints
        # Time: O(n), Space: O(1) extra
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Sum total candies
        # Time: O(n), Space: O(1) extra
        return sum(candies)


def main():
    # Measure total program runtime (parse + solve + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [1, 0, 2]
    else:
        # ---------------- INPUT MODE ----------------
        # Time: O(n) parse, Space: O(n) to store arr
        arr = list(map(int, data.split()))

    # Solve
    # Time: O(n), Space: O(n) due to candies array
    answer = solver.minCandy(arr)

    print("Input:")
    print("arr =", arr)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

**Input:** `arr = [1, 0, 2]`
**Output:** `5` (+ runtime)

---


