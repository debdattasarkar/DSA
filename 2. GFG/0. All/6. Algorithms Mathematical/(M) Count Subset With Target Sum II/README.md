# Count Subset With Target Sum II

**Difficulty:** Medium  
**Accuracy:** 14.25%  
**Submissions:** 1K+  
**Points:** 4  

---

## Problem Statement

Given an array **arr[]** and an integer **k**, find the **count of subsets** whose sum is equals to **k**.

### Note
It is guaranteed that the no of valid subsets will fit within a **32-bit integer**.

---

## Examples

### Example 1
**Input:** `arr[] = [1, 3, 2], k = 3`  
**Output:** `2`  
**Explanation:** The two subsets whose sum is equals to k are `[1, 2]` and `[3]`.

---

### Example 2
**Input:** `arr[] = [4, 2, 3, 1, 2], k = 4`  
**Output:** `3`  
**Explanation:** The three subsets whose sum is equals to k are `[4]`, `[2, 2]` and `[3, 1]`.

---

### Example 3
**Input:** `arr[] = [10, 20, 30], k = 25`  
**Output:** `0`  
**Explanation:** No subsets exits with sum equals to k.

---

## Constraints

- `1 ≤ arr.size() ≤ 40`
- `-10^7 < arr[i], k < 10^7`

---

## Expected Complexities

- **Time Complexity:** `O(2^(n/2))`
- **Auxiliary Space:** `O(n)`

---

## Topic Tags

- Recursion  
- Algorithms  

---

---

## 2) Text explanation (best approach for this problem)

We need **count of subsets** whose sum equals `k`.

* A subset = choose or not choose each element (order doesn’t matter).
* Naive recursion is `O(2^n)` which is too big for `n=40`.
* Also `arr[i]` and `k` can be **negative**, so classic DP-by-sum (knap DP table) is not practical.

### Expected trick (because `n ≤ 40`): **Meet-in-the-Middle**

Split array into two halves:

* left half size ≈ `n/2`
* right half size ≈ `n/2`

Compute **all subset sums** of each half:

* left has up to `2^(n/2)` sums
* right has up to `2^(n/2)` sums

Then count pairs:

* If `left_sum + right_sum = k`
* For each `left_sum`, we need `right_sum = k - left_sum`

Use a hashmap (frequency map) for right sums → total count fast.

**Time:** `O(2^(n/2))` (matches expected)
**Space:** `O(2^(n/2))` (practically required to store sums/frequencies)

> Assumption: empty subset is allowed (standard subset definition). If a platform wanted non-empty subsets, you’d adjust when `k == 0`.

---

## Step-by-step dry run (Example: arr = [1, 3, 2], k = 3)

Split:

* left = `[1]`
* right = `[3, 2]`

### Step 1: All subset sums of left

Subsets of `[1]`:

* `{}` sum = 0
* `{1}` sum = 1
  So: `left_sums = [0, 1]`

### Step 2: All subset sums of right + frequency map

Subsets of `[3,2]`:

* `{}` sum=0
* `{3}` sum=3
* `{2}` sum=2
* `{3,2}` sum=5

Frequency map:

* `right_count = {0:1, 3:1, 2:1, 5:1}`

### Step 3: Count pairs to reach k

For each `sL` in left:

* If `sL = 0`, need `3 - 0 = 3` → add `right_count[3] = 1`
* If `sL = 1`, need `3 - 1 = 2` → add `right_count[2] = 1`

Total count = `1 + 1 = 2`
Subsets are: `[3]` and `[1,2]`

---

## 3) Python solutions (brute + interview-expected optimized)

### A) Brute force recursion (easy, but exponential `O(2^n)`)

Good for explaining baseline.

```python
class Solution:
    def countSubset(self, arr, k):
        n = len(arr)

        # Time: O(2^n)  (each element picked/not picked)
        # Space: O(n)   (recursion depth)
        def dfs(index, current_sum):
            # If we've decided for all elements
            if index == n:
                return 1 if current_sum == k else 0

            # Choice 1: don't take arr[index]
            ways_without = dfs(index + 1, current_sum)

            # Choice 2: take arr[index]
            ways_with = dfs(index + 1, current_sum + arr[index])

            return ways_without + ways_with

        return dfs(0, 0)
```

---

### B) Optimized (Most expected here): Meet-in-the-Middle `O(2^(n/2))`

Handles negatives naturally.

```python
class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2

        left_part = arr[:mid]
        right_part = arr[mid:]

        # Generate all subset sums for a list, return list of sums
        # Time: O(2^m), Space: O(2^m)
        def generate_sums(nums):
            sums = []

            def dfs(i, running_sum):
                if i == len(nums):
                    sums.append(running_sum)
                    return
                # not take
                dfs(i + 1, running_sum)
                # take
                dfs(i + 1, running_sum + nums[i])

            dfs(0, 0)
            return sums

        left_sums = generate_sums(left_part)     # size up to 2^(n/2)
        right_sums = generate_sums(right_part)   # size up to 2^(n/2)

        # Build frequency map of right sums
        right_count = {}
        for s in right_sums:
            right_count[s] = right_count.get(s, 0) + 1

        # For each left sum, add how many right sums make total k
        total_ways = 0
        for sL in left_sums:
            needed = k - sL
            total_ways += right_count.get(needed, 0)

        return total_ways
```

**Complexities (MITM):**

* Time: `O(2^(n/2))`
* Space: `O(2^(n/2))` (to store sums / frequency map)
* Recursion depth: `O(n)` (small)

---

## 4) Interview quick-recall + expected Q&A

### How to remember quickly (30-second plan)

**Trigger:** `n ≤ 40` + subset sum count + negatives → **Meet-in-the-Middle**

Mnemonic:
**“Split → Sums → Count complements”**

1. Split array in half
2. Generate all subset sums for each half
3. Hash right sums
4. For each left sum, add `count[k-left]`

### 5-line pseudo you can say while coding

```text
split arr into L and R
LS = all subset sums of L
RS = all subset sums of R; build freq map
ans = Σ freq[k - s] for s in LS
return ans
```

---

### Expected interviewer questions & answers

**Q1) Why not normal DP (knapsack dp[sum])?**
**A:** Values and `k` can be negative and range up to `1e7`, so sum-range DP is not feasible in memory/time.

**Q2) Why meet-in-the-middle works well for n=40?**
**A:** `2^40` is too big, but splitting gives `2^20 + 2^20` which is about ~1 million sums—manageable.

**Q3) Complexity of MITM?**
**A:** Time `O(2^(n/2))`, space `O(2^(n/2))`.

**Q4) Does it handle duplicates in array?**
**A:** Yes, because subset choices are by index; duplicates just create multiple valid subsets and are correctly counted via frequencies.

**Q5) Is empty subset counted?**
**A:** Standard definition includes it. If they want non-empty subsets, subtract 1 when `k == 0` (because empty subset sum is 0).

**Q6) Can we avoid storing all right sums?**
**A:** You can store only the frequency map (still `O(2^(n/2))` keys in worst case). Storing is basically necessary for fast counting.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Budget / Target allocation counting**

   * “How many ways can I pick a subset of transactions/items whose total equals a target budget?”
   * Example: choose a set of refunds/credits/debits to match a reconciliation target (can include negatives).

2. **Feature toggle / configuration combinations**

   * “How many combinations of enabled components add up to a target resource limit (CPU/memory/credits)?”
   * When effects can be positive/negative (enable saves cost, disable adds cost), MITM still works.

3. **Risk / Portfolio subset selection**

   * Count how many subsets of positions (profits/losses can be negative) sum to a target exposure.
   * Used in quick what-if analysis for small/medium sets of instruments.

---

## 6) Full program (Meet-in-the-Middle) + timing + sample I/O

* Input format (simple CP style):

  * Line 1: `n`
  * Line 2: `n` integers (array)
  * Line 3: `k`
* Output:

  * Single integer: count of subsets with sum = `k`
* Runtime printed to **stderr** (so stdout remains clean for judges).

```python
import sys
import time

class Solution:
    def countSubset(self, arr, k):
        """
        Meet-in-the-Middle counting subsets with sum == k.

        Why MITM:
        - n <= 40, but values can be negative => sum-range DP is not feasible.
        - Split into halves => enumerate subset sums in O(2^(n/2)).

        Time Complexity: O(2^(n/2))
        Space Complexity: O(2^(n/2))  (frequency map of subset sums)
        """
        n = len(arr)
        mid = n // 2

        left_part = arr[:mid]
        right_part = arr[mid:]

        # Generate all subset sums of 'nums' using recursion.
        # If len(nums)=m: generates 2^m sums.
        # Time: O(2^m), Space: O(2^m) for list + O(m) recursion depth
        def generate_subset_sums(nums):
            sums = []

            def dfs(index, running_sum):
                if index == len(nums):
                    sums.append(running_sum)
                    return
                # Choice 1: exclude nums[index]
                dfs(index + 1, running_sum)
                # Choice 2: include nums[index]
                dfs(index + 1, running_sum + nums[index])

            dfs(0, 0)
            return sums

        # Step 1: Enumerate all subset sums of left and right halves
        # Time: O(2^(n/2)), Space: O(2^(n/2))
        left_sums = generate_subset_sums(left_part)
        right_sums = generate_subset_sums(right_part)

        # Step 2: Build frequency map for right sums
        # Time: O(2^(n/2)), Space: O(2^(n/2))
        right_freq = {}
        for s in right_sums:
            right_freq[s] = right_freq.get(s, 0) + 1

        # Step 3: Count pairs (left_sum + right_sum == k)
        # For each left_sum, add count of right_sum = (k - left_sum)
        # Time: O(2^(n/2)), Space: O(1) extra
        total_count = 0
        for left_sum in left_sums:
            needed = k - left_sum
            total_count += right_freq.get(needed, 0)

        return total_count


def main():
    """
    Input:
      n
      a1 a2 ... an
      k

    Output:
      count_of_subsets_with_sum_k
    """
    start_time = time.perf_counter()  # measure full program runtime

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Step A: Parse input
    # Time: O(n), Space: O(n)
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    k = int(data[1 + n])

    # Step B: Solve
    # Time: O(2^(n/2)), Space: O(2^(n/2))
    solver = Solution()
    answer = solver.countSubset(arr, k)

    # Step C: Print output (stdout)
    # Time: O(1)
    print(answer)

    end_time = time.perf_counter()
    # Print timing to stderr so stdout remains clean
    print(f"[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
3
1 3 2
3

Expected Output:
2

Explanation:
Subsets summing to 3 are [3] and [1,2].
"""
```
