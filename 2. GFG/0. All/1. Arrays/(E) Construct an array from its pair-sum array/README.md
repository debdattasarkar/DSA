# Construct an array from its pair-sum array 🧮

**Difficulty:** Easy  
**Accuracy:** 55.06%  
**Submissions:** 6K+  
**Points:** 2  
**Average Time:** 10m  

---

## Problem Statement

Given a **pair-sum** array `arr[]` construct the **original array**.

A pair-sum array for an array is the array that contains **sum of all pairs** in ordered form, i.e.:

- `arr[0]` is sum of `res[0]` and `res[1]`
- `arr[1]` is sum of `res[0]` and `res[2]`
- and so on.

Let the original array be `res[]`.

> **Note:**  
> If the size of original array `res[]` is `n`, then the size of pair-sum array `arr[]` would be  
> \[
> \frac{n \times (n - 1)}{2}
> \]  
> We may assume that the pair-sum array `arr[]` is appropriate in size.

Note that, if the original array is correct then the driver code will print **`true`**, else **`false`**.

---

## Examples

### Example 1

**Input:** `arr[] = [4, 5, 3]`  
**Output:** `true`  

**Explanation:**  
A valid original array is `[3, 1, 2]`, pairwise sums are:

- `(3 + 1)`
- `(3 + 2)`
- `(1 + 2)`

which gives `[4, 5, 3]`.

---

### Example 2

**Input:** `arr[] = [3]`  
**Output:** `true`  

**Explanation:**  
One of the valid original arrays is `[1, 2]` (since `1 + 2 = 3`).

---

## Constraints

- \( 1 \le n \le 10^3 \)  
- \( 1 \le \text{arr}[i] \le 10^9 \)

---

## Expected Complexities

- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Mathematical  
- Arrays  

---

## Related Articles

- Construct Array Pair Sum Array  

---

---

I’ll follow your numbering and keep the logic “interview-ready”.

---

## 2. Explanation + Step-by-step dry run

### What is given?

* `arr` is **not** the original array.
* It is the **pair-sum array** of some original array `res`.

If the original array is:

```text
res = [r0, r1, r2, ..., r(n-1)]
```

then `arr` contains **all pair sums** in this order:

```text
arr[0]   = r0 + r1
arr[1]   = r0 + r2
...
arr[n-2] = r0 + r(n-1)
arr[n-1] = r1 + r2
arr[n]   = r1 + r3
...
```

(First all pairs with index 0, then with index 1, and so on, with i < j.)

If the original length is `n`, pair-sum length is

[
m = \frac{n(n-1)}{2}
]

We can recover `n` from `m = len(arr)` using the quadratic formula:

[
n = \frac{1 + \sqrt{1 + 8m}}{2}
]

They guarantee `arr` is consistent, so `n` will be an integer.

---

### Key observation

Look at **only three pair sums** involving the first three elements `r0, r1, r2`:

```text
S01 = r0 + r1  = arr[0]          # first pair
S02 = r0 + r2  = arr[1]          # second pair
S12 = r1 + r2  = arr[n-1]        # first pair of row starting at index 1
```

Now:

```text
S01 + S02 - S12
= (r0 + r1) + (r0 + r2) - (r1 + r2)
= 2 * r0
```

So we can **directly compute**:

```text
r0 = (S01 + S02 - S12) / 2
r1 = S01 - r0
r2 = S02 - r0
```

Once we know `r0`, all other elements are easy:

For `j >= 3`, we know the pair sum `r0 + rj` is in the first “row”:

```text
arr[j-1] = r0 + rj       # because arr[0]=(0,1), arr[1]=(0,2), ..., arr[j-1]=(0,j)
=> rj = arr[j-1] - r0
```

So we can recover the whole original array in **O(n)** time using **only the first row and the first pair of the second row**.

---

### Dry run on the example

`arr = [4, 5, 3]`

We first compute `n` (original size):

* `m = len(arr) = 3`
* `1 + 8m = 1 + 24 = 25`
* `sqrt(25) = 5`
* `n = (1 + 5)/2 = 3` → original has 3 elements: `r0, r1, r2`.

Now:

```text
S01 = arr[0]   = 4   # r0 + r1
S02 = arr[1]   = 5   # r0 + r2
S12 = arr[n-1] = arr[2] = 3  # r1 + r2
```

Compute:

```text
r0 = (S01 + S02 - S12) / 2
   = (4 + 5 - 3) / 2
   = 6 / 2 = 3

r1 = S01 - r0 = 4 - 3 = 1
r2 = S02 - r0 = 5 - 3 = 2
```

We get original array: `[3, 1, 2]`.

Check pair sums:

* r0 + r1 = 3 + 1 = 4 → arr[0]
* r0 + r2 = 3 + 2 = 5 → arr[1]
* r1 + r2 = 1 + 2 = 3 → arr[2]

Matches the input pair-sum array ✅

---

## 3. Python solutions

We’ll give:

1. A **simple brute-ish** version that reconstructs and **also verifies all pair sums** (O(n²) check).
2. The **optimized O(n)** reconstruction you actually want to use (expected in interviews).

The function signature you asked for:

```python
class Solution:
    def constructArr(self, arr):
        # code here
```

### Helper: compute original length from pair-sum length

We’ll reuse this in both methods.

```python
import math

def original_length_from_pairs(pair_count: int) -> int:
    """
    Given m = number of pair sums, solve n(n-1)/2 = m for n.

    n^2 - n - 2m = 0 -> n = (1 + sqrt(1 + 8m)) / 2

    We assume input is valid so the result is an integer.
    """
    if pair_count == 0:
        return 1  # if no pair sums, original could be length 1
    disc = 1 + 8 * pair_count
    root = math.isqrt(disc)
    # In valid test cases, root*root == disc
    return (1 + root) // 2
```

---

### 3.1 “Brute” version – reconstruct + verify all pair sums (O(n²))

```python
from typing import List

class Solution:
    def constructArr_bruteforce(self, arr: List[int]) -> List[int]:
        """
        Brute-style solution:
        - Use the same formula to reconstruct the original array.
        - Additionally, verify that all pair sums match the given arr[]
          (in the prescribed order).

        This verification step makes it O(n^2), since there are ~n^2/2 pair sums.

        Time  : O(n^2) to recompute and check all pair sums
        Space : O(n) to store the original array
        """
        m = len(arr)
        n = original_length_from_pairs(m)

        # Handle small n separately
        if n == 1:
            # No pair sums; arr is empty. Any single-element array works.
            return [0]

        if n == 2:
            # arr[0] = r0 + r1. Choose something simple, e.g., [0, arr[0]]
            original = [0, arr[0]]
        else:
            # Use the formula for n >= 3
            S01 = arr[0]
            S02 = arr[1]
            S12 = arr[n - 1]  # r1 + r2

            r0 = (S01 + S02 - S12) // 2
            r1 = S01 - r0
            r2 = S02 - r0

            original = [0] * n
            original[0] = r0
            original[1] = r1
            original[2] = r2

            # Remaining elements (j = 3..n-1): arr[j-1] = r0 + rj
            for j in range(3, n):
                original[j] = arr[j - 1] - r0

        # ----- Optional brute verification: recompute all pair sums -----
        # This is just to show correctness and counts as "brute" work.
        # In the optimized method we will skip this.

        recomputed = []
        for i in range(n):
            for j in range(i + 1, n):
                recomputed.append(original[i] + original[j])

        # The driver on GFG would do this check instead of us.
        # Here we could compare and raise an error if needed.
        if len(recomputed) != m or any(recomputed[k] != arr[k] for k in range(m)):
            # If something went wrong, we could raise or adjust.
            # For this demo, just return an empty list.
            return []

        return original
```

---

### 3.2 Optimized O(n) reconstruction (what you’d actually use)

```python
from typing import List
import math

class Solution:
    def constructArr(self, arr: List[int]) -> List[int]:
        """
        Optimized O(n) solution to reconstruct one valid original array
        from its pair-sum array.

        Steps:
            1) Determine n (original length) from m = len(arr) using:
                   n = (1 + sqrt(1 + 8m)) / 2
            2) Handle small cases n = 1, 2.
            3) Use first three relevant pair sums for n >= 3:
                   S01 = r0 + r1     = arr[0]
                   S02 = r0 + r2     = arr[1]
                   S12 = r1 + r2     = arr[n-1]
               Derive:
                   r0 = (S01 + S02 - S12) / 2
                   r1 = S01 - r0
                   r2 = S02 - r0
            4) For j >= 3:
                   arr[j-1] = r0 + rj  ->  rj = arr[j-1] - r0

        Time  : O(n) where n is original array length
        Space : O(n) to store the original array (no extra big structures)
        """
        m = len(arr)
        n = original_length_from_pairs(m)

        # n == 1: no pair sums; any 1-element array works
        if n == 1:
            return [0]

        # n == 2: only one pair r0 + r1 = arr[0],
        # choose e.g. r0 = 0, r1 = arr[0]
        if n == 2:
            return [0, arr[0]]

        # n >= 3:
        S01 = arr[0]       # r0 + r1
        S02 = arr[1]       # r0 + r2
        S12 = arr[n - 1]   # r1 + r2  (first pair in the second row)

        # Compute r0, r1, r2
        r0 = (S01 + S02 - S12) // 2
        r1 = S01 - r0
        r2 = S02 - r0

        original = [0] * n
        original[0] = r0
        original[1] = r1
        original[2] = r2

        # Compute remaining elements using sums with r0
        for j in range(3, n):
            # arr[j-1] stores r0 + rj
            original[j] = arr[j - 1] - r0

        return original
```

This is the clean solution interviewers are usually looking for.

---

## 4. Interview tips: how to remember + Q&A

### Mental “hook” to remember the logic

Think:

> **“Use three pair sums to find first element; then subtract from row-0 sums.”**

In formula:

1. `S01 = arr[0] = r0 + r1`
2. `S02 = arr[1] = r0 + r2`
3. `S12 = arr[n-1] = r1 + r2`
4. `r0 = (S01 + S02 - S12) / 2`
5. `rj = arr[j-1] - r0` for `j >= 1`.

If you can recall the idea **“S01 + S02 - S12 = 2r0”**, you can derive everything in the interview.

---

### 5-line pseudo-code template (to memorize)

```text
m = len(arr)
n = (1 + sqrt(1 + 8*m)) / 2
if n == 1: return [0]
if n == 2: return [0, arr[0]]
S01 = arr[0]; S02 = arr[1]; S12 = arr[n-1]
r0 = (S01 + S02 - S12) / 2; r1 = S01 - r0; r2 = S02 - r0; res[0..2] = ...
for j from 3 to n-1: res[j] = arr[j-1] - r0
```

You can rebuild full Python/C++/Java code from this in under a minute.

---

### Typical interview questions & answers

---

**Q1: How do you get the original length from the pair-sum array?**

**A:**
Let `n` be original length, `m` be number of pair sums.
We have:

[
m = \frac{n(n-1)}{2} \Rightarrow n^2 - n - 2m = 0
]

Solving quadratic:

[
n = \frac{1 + \sqrt{1 + 8m}}{2}
]

Since the input is guaranteed to be valid, this yields an integer.

---

**Q2: How do you get the first element `r0`?**

**A:**
Use three pair sums involving `r0, r1, r2`:

```text
S01 = r0 + r1   (arr[0])
S02 = r0 + r2   (arr[1])
S12 = r1 + r2   (arr[n-1])
```

Then:

```text
S01 + S02 - S12 = (r0 + r1) + (r0 + r2) - (r1 + r2) = 2 * r0
=> r0 = (S01 + S02 - S12) / 2
```

From there:

```text
r1 = S01 - r0
r2 = S02 - r0
```

---

**Q3: Once you know `r0`, how do you find all other elements?**

**A:**
For any `j >= 1`, we know there is a pair sum `r0 + rj` in the first row:

* `arr[j-1] = r0 + rj`

So:

```text
rj = arr[j-1] - r0
```

We do this for all `j = 3..n-1`.

---

**Q4: What is the time and space complexity of your solution?**

**A:**

* Time:

  * Computing `n` is O(1).
  * Computing the original `n` elements is O(n).
    → Overall **O(n)** where `n` is original length.

* Space:

  * We store only the output array of size `n`.
    → **O(n)** extra space, **O(1)** auxiliary beyond the result.

---

**Q5: Do you need to check all pair sums? Why/why not?**

**A:**
The problem statement guarantees that the given pair-sum array is “appropriate in size”. We only need to **construct one original array** that’s consistent. The judge/driver can recompute all pair sums and verify; we don’t need to spend O(n²) time for that in our function. That’s why our reconstruction can be O(n).

(If we wanted to fully validate ourselves, we could recompute all `n(n-1)/2` pair sums and compare, which would be O(n²).)

---

If you keep in mind:

> **“S01 + S02 - S12 = 2 * first element; others = row-0 sums minus first.”**

you’ll be able to derive the solution and code it confidently during interviews.

---

---

Nice one, this is a cute math / reconstruction problem.

I’ll give you (5) real-world-ish contexts, then (6) a full runnable Python program with timing and heavy inline complexity comments.

---

## 5. Real-World Use Cases (easy to explain to interviewer)

Think of situations where **only pairwise sums** are stored or transmitted, but we later need to reconstruct individual values.

1. **Compressed / Privacy-Preserving Telemetry**

   * A small IoT device sends only *pairwise sums* of sensor readings (to obfuscate each reading slightly).
   * On the server, we know the structure of the pair-sum array, so we can reconstruct the original readings using exactly this logic.
   * Good when you want lightweight encoding + a bit of privacy.

2. **Recovering Original Scores from Aggregated Pairwise Matches**

   * Suppose we have three players `A, B, C` and we only store pairwise **total scores** `A+B`, `A+C`, `B+C` for a round.
   * Later we want to reconstruct individual scores; the system uses the same math:

     * `A = (AB + AC − BC)/2`, etc.
   * The same generalizes to `n` players when the pair sums are stored in a specific order.

3. **Integrity / Consistency Check for Stored Data**

   * A database stores:

     * an “original” list of values
     * plus a **pair-sum array** as a redundancy / checksum.
   * When restoring or validating, you can reconstruct one from the other and verify they match — this is exactly what the online judge does (it recomputes pair sums from your reconstructed `res` and checks).

In the interview you can summarize:

> “Any situation where only pairwise sums are stored — e.g., obfuscated telemetry, aggregated pair scores, or redundant checksums — can use this exact reconstruction trick.”

---

## 6. Full Python Program (with timing & complexity comments)

This is a complete script:

* Reads input:

  * First line: `m` = length of pair-sum array.
  * Second line: `m` integers for `arr`.
* Reconstructs one valid original array.
* Prints the reconstructed array and total runtime.

```python
import math
import time
from typing import List


def original_length_from_pairs(pair_count: int) -> int:
    """
    Given m = pair_count = n*(n-1)/2, solve for n.

    Equation:
        n^2 - n - 2m = 0
        n = (1 + sqrt(1 + 8m)) / 2

    Time  : O(1)
    Space : O(1)
    """
    if pair_count == 0:
        # Theoretically, this would mean n = 1 (no pairs).
        return 1
    disc = 1 + 8 * pair_count          # O(1)
    root = math.isqrt(disc)            # integer square root, O(1) for our sizes
    return (1 + root) // 2             # n should be an integer for valid input


class Solution:
    def constructArr(self, arr: List[int]) -> List[int]:
        """
        Reconstruct one valid original array from its pair-sum array 'arr'.

        arr: list of length m = n*(n-1)/2 containing sums of all distinct pairs
             (i < j) of the original array in the given order.

        Approach:
            1. Compute n (original length) from m = len(arr).
            2. For n = 2:
                   arr[0] = r0 + r1.
                   We can pick any valid pair, e.g., r0 = 0, r1 = arr[0].
            3. For n >= 3:
                   Use the first three relevant pair sums:
                       S01 = r0 + r1 = arr[0]
                       S02 = r0 + r2 = arr[1]
                       S12 = r1 + r2 = arr[n-1]
                   Algebra:
                       S01 + S02 - S12 = 2*r0
                       => r0 = (S01 + S02 - S12)/2
                       r1 = S01 - r0
                       r2 = S02 - r0
                   Then for j >= 3:
                       arr[j-1] = r0 + rj
                       => rj = arr[j-1] - r0

        Complexity:
            Let n be the length of the original array.

            - Computing n:      O(1)
            - Computing r0,r1,r2 and the rest:
                                O(n)
            - Total Time:       O(n)
            - Extra Space:      O(n) for the output array
        """
        m = len(arr)
        n = original_length_from_pairs(m)   # O(1)

        # Edge case: n == 1 (not expected here since m >= 1 in constraints,
        # but we keep this for logical completeness).
        if n == 1:
            # No pair sums; any single-element array works.
            # We choose [0] as a canonical choice.
            return [0]

        # n == 2: only one pair sum, arr[0] = r0 + r1.
        # We can choose any valid decomposition. E.g., r0 = 0, r1 = arr[0].
        if n == 2:
            return [0, arr[0]]

        # n >= 3: use the algebra trick on the first three pair sums.
        S01 = arr[0]         # r0 + r1
        S02 = arr[1]         # r0 + r2
        S12 = arr[n - 1]     # r1 + r2 (first pair from "row" starting with r1)

        # Compute first three original elements:
        # Time: O(1)
        r0 = (S01 + S02 - S12) // 2
        r1 = S01 - r0
        r2 = S02 - r0

        # Allocate output array
        # Time: O(n) for initialization; Space: O(n)
        original = [0] * n
        original[0] = r0
        original[1] = r1
        original[2] = r2

        # Fill the remaining elements using arr[j-1] = r0 + rj
        # Loop runs (n-3) times => O(n)
        for j in range(3, n):
            original[j] = arr[j - 1] - r0

        return original


# ----------------------------- Driver Code ----------------------------- #

def main():
    """
    Driver to:
        - Read input for the pair-sum array.
        - Reconstruct the original array using Solution.constructArr().
        - Print the original array and total runtime.

    Input format (simple):
        m
        a0 a1 a2 ... a(m-1)

    Example:
        3
        4 5 3

    represents arr = [4, 5, 3], whose original can be [3, 1, 2].
    """

    print("Enter length m of pair-sum array:")
    first_line = input().strip()
    if not first_line:
        print("No input provided.")
        return

    m = int(first_line)

    print(f"Enter {m} integers for the pair-sum array:")
    if m > 0:
        arr_values = list(map(int, input().split()))
        # Trim or pad (defensively) if user doesn't give exactly m numbers:
        if len(arr_values) < m:
            arr_values += [0] * (m - len(arr_values))
        elif len(arr_values) > m:
            arr_values = arr_values[:m]
    else:
        arr_values = []

    solver = Solution()

    # Start timing right before the algorithm
    start_time = time.perf_counter()

    # Core logic: O(n) reconstruction
    original = solver.constructArr(arr_values)

    # Stop timing after reconstruction
    end_time = time.perf_counter()

    print("\nReconstructed original array:")
    print(original)
    print(f"\nTotal elapsed time (seconds): {end_time - start_time:.6f}")


if __name__ == "__main__":
    main()
```

### Example run (mentally)

Input:

```text
3
4 5 3
```

Output (typical):

```text
Enter length m of pair-sum array:
3
Enter 3 integers for the pair-sum array:
4 5 3

Reconstructed original array:
[3, 1, 2]

Total elapsed time (seconds): 0.0000xx
```

You can paste this script into a file (`construct_pair_sum.py`), run it, and experiment with different pair-sum arrays. For coding platforms, you’d only submit the `Solution` class with `constructArr`; the driver and timing are for your own practice and performance intuition.
