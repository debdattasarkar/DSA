# Subset XOR

**Difficulty:** Medium  
**Accuracy:** 72.34%  
**Submissions:** 8K+  
**Points:** 4  

---

## Problem Statement

Given an positive integer **n**, find a subset of numbers from **1 to n (inclusive)**, where each number can be used at most once, such that:

- The XOR of all elements in the subset is exactly **n**.  
- The size of the subset is as large as possible.  
- If multiple such subsets exist, choose the **lexicographically smallest** one.

---

## Lexicographical Order

**Lexicographical Order :**  
A subset **A[]** is lexicographically smaller than subset **B[]** if at the first index where they differ, **A[i] < B[i]** (based on character ASCII/Unicode values).  
If all elements match but one subset ends earlier, the shorter subset is considered smaller.

---

## Examples

### Example 1

**Input:** `n = 4`  
**Output:** `[1, 2, 3, 4]`  

**Explanation:**  
We choose all the elements from 1 to 4. Its xor value is equal to n.  
This is the maximum possible size of the subset.

---

### Example 2

**Input:** `n = 3`  
**Output:** `[1, 2]`  

**Explanation:**  
`1 ^ 2 = 3`, This is the smallest lexicographical answer possible with maximum size of subset i.e 2.

---

## Constraints

\[
1 \le n \le 10^5
\]

---

## Expected Complexities

- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Bit Magic  
- implementation  

---

---

I’ll break it into exactly what you asked:

---

## 2. Explanation + step-by-step idea

We are given an integer `n`.
We must pick a subset of numbers from `1` to `n` (each number at most once) such that:

1. XOR of all chosen numbers is exactly `n`.
2. Number of elements in the subset is **maximum** possible.
3. If multiple maximum-size subsets exist, choose the **lexicographically smallest** (when the subset is sorted ascending).

Key observations:

1. **Maximum possible size**
   We can never have more than `n` elements because the pool is `{1, 2, ..., n}`.
   So maximum size is either:

   * `n` (we take all numbers), or
   * `n-1` (we drop exactly one number),
     Because if you drop 2 or more numbers, size becomes ≤ `n-2`, which is worse than `n` or `n-1`.

2. **Start by trying “take all numbers”**
   Let
   [
   T = 1 \oplus 2 \oplus 3 \oplus \dots \oplus n
   ]
   (XOR from `1` to `n`).

   * If `T == n`, then taking all numbers `{1, 2, ..., n}` already gives XOR `n`.

     * Size is `n` (maximum possible).
     * There is no other subset of size `n` (all `n` elements are fixed), so this is automatically the lexicographically smallest.
     * We’re done.

   * If `T != n`, then we cannot use **all** numbers. We must drop at least one element.

3. **Try dropping exactly one number**

   Suppose we start with all numbers `{1, 2, ..., n}` (XOR is `T`) and we **remove** some number `x`.
   New XOR becomes:
   [
   T \oplus x
   ]
   because removing an element in XOR is the same as XORing with it again.

   We want:
   [
   T \oplus x = n
   \Rightarrow x = T \oplus n
   ]

   So the only candidate “single number to remove” is:
   [
   x = T \oplus n
   ]

   If this `x` is in the range `[1, n]`, then the subset
   [
   {1,2,\dots,n} \setminus {x}
   ]
   has:

   * size `n-1`
   * XOR exactly `n`
   * and it’s the **only** subset of size `n-1` whose XOR is `n` (because `x` is uniquely fixed), so it’s automatically lexicographically smallest among size `n-1` subsets.

   For this particular problem, it turns out that whenever `T != n`, this `x` is **always** in `[1, n]`, so we *always* can reach size `n-1`.

4. **How to compute `T = XOR(1..n)` quickly**

   Classic bit trick:

   ```
   n % 4 == 0  -> XOR(1..n) = n
   n % 4 == 1  -> XOR(1..n) = 1
   n % 4 == 2  -> XOR(1..n) = n + 1
   n % 4 == 3  -> XOR(1..n) = 0
   ```

   So we can get `T` in O(1) time.

---

### Step-by-step Dry Run

Let’s dry run for **n = 5**.

We want subset of `{1, 2, 3, 4, 5}`:

1. Compute `T = XOR(1..5)` using `n % 4` rule.

   * `5 % 4 = 1` → `T = 1`.

2. Compare `T` with `n`:

   * `T = 1`, `n = 5`, so `T != n`.
     We cannot take all `[1, 2, 3, 4, 5]`.

3. Compute element to remove:
   [
   x = T \oplus n = 1 \oplus 5
   ]
   Binary:

   * `1 = 001`
   * `5 = 101`
   * `001 XOR 101 = 100 (4)`
     So `x = 4`.

4. Build the answer as all numbers `1..5` except `4`:

   * `result = [1, 2, 3, 5]`.

5. Verify XOR:

   * `1 ^ 2 = 3`
   * `3 ^ 3 = 0`
   * `0 ^ 5 = 5` = `n`. ✅

So for `n = 5`, answer is `[1, 2, 3, 5]` (size 4 = `n-1`).

---

Another quick dry run: **n = 4**

1. `4 % 4 = 0` → `T = 4`.
2. `T == n`, so we can take all numbers.
3. Answer: `[1, 2, 3, 4]`.
4. Check: `1 ^ 2 ^ 3 ^ 4 = 4`. ✅

---

## 3. Python solutions

### 3.1 Brute-force (only for understanding, not for constraints)

**Idea:**
Try **all subsets** of `{1..n}`, track:

* those with XOR = `n`,
* pick the ones with maximum size,
* and among them choose lexicographically smallest.

This is O(2^n * n) and works only for very small `n` (like `n ≤ 20`).
But it’s good to understand the problem behavior.

```python
from itertools import combinations

class Solution:
    def subsetXOR_bruteforce(self, n: int):
        numbers = list(range(1, n + 1))
        best_subset = []

        # r is the size of subset we are trying
        for r in range(1, n + 1):
            # generate all subsets of size r
            for subset in combinations(numbers, r):
                xor_value = 0
                for value in subset:
                    xor_value ^= value

                if xor_value == n:
                    # Found a valid subset
                    if len(subset) > len(best_subset):
                        best_subset = list(subset)
                    elif len(subset) == len(best_subset) and list(subset) < best_subset:
                        # lexicographically smaller
                        best_subset = list(subset)

        # if nothing found (theoretically impossible because {n} always works), return [n]
        if not best_subset:
            return [n]

        return best_subset
```

This is **not** what you use in an interview for this problem, but it helps you see why the optimized solution aims for size `n` or `n-1`.

---

### 3.2 Optimized Solution – XOR pattern + remove one element

This is what you should present in interviews.

#### Version A – using XOR pattern (O(1) to get XOR(1..n))

```python
class Solution:
    def subsetXOR(self, n: int):
        # Step 1: compute XOR of all numbers from 1 to n using n % 4 pattern
        remainder = n % 4
        if remainder == 0:
            xor_1_to_n = n
        elif remainder == 1:
            xor_1_to_n = 1
        elif remainder == 2:
            xor_1_to_n = n + 1
        else:  # remainder == 3
            xor_1_to_n = 0

        # Step 2: if XOR(1..n) == n, we can take all numbers
        if xor_1_to_n == n:
            # return [1, 2, ..., n]
            return [value for value in range(1, n + 1)]

        # Step 3: otherwise, drop exactly one element x such that:
        # XOR(1..n without x) = n
        # x = xor_1_to_n ^ n
        element_to_remove = xor_1_to_n ^ n

        # Step 4: build the subset skipping this element
        result_subset = []
        for value in range(1, n + 1):
            if value != element_to_remove:
                result_subset.append(value)

        # This subset has size n-1 and XOR exactly n.
        # It is unique for this size, so automatically lexicographically smallest.
        return result_subset
```

**Time complexity:** O(n) – we must at least output up to `n` numbers.
**Space complexity:** O(1) extra (besides the output list).

---

#### Version B – same logic but computing XOR(1..n) in a simple loop

This is slightly less “bit magic”, easier if you forget the n%4 pattern.
Still O(n) (acceptable for `n ≤ 10^5`).

```python
class Solution:
    def subsetXOR_loop(self, n: int):
        # Step 1: compute XOR from 1 to n using a simple loop
        xor_1_to_n = 0
        for value in range(1, n + 1):
            xor_1_to_n ^= value

        # Step 2: if XOR(1..n) equals n, we can take all numbers
        if xor_1_to_n == n:
            return [value for value in range(1, n + 1)]

        # Step 3: otherwise remove a single element: x = xor_1_to_n ^ n
        element_to_remove = xor_1_to_n ^ n

        # Step 4: generate all numbers except this one
        result_subset = []
        for value in range(1, n + 1):
            if value != element_to_remove:
                result_subset.append(value)

        return result_subset
```

This is conceptually the same as Version A, just replacing the bit-pattern shortcut with a loop.

---

## 4. Interview memory tips + likely Q&A

### How to remember quickly in an interview

Think in 4 steps:

1. **“Full set first” idea**
   Always ask: what happens if I take all numbers `1..n`?

   * Compute `T = XOR(1..n)` (use `n % 4` trick).
   * If `T == n`, done: answer is `[1..n]`.

2. **“Drop one element” idea**
   If not equal, try dropping only one element to keep size maximum:

   * Need `T ^ x = n`, so `x = T ^ n`.

3. **Check range**
   For this problem, you can argue that `x` will always lie in `[1, n]` (based on the `n % 4` cases), so you *always* get a size `n-1` subset.

4. **Uniqueness → lexicographically smallest**
   Since the size-`n-1` solution is unique (only one choice of `x`), there is no competing same-size subset; lexicographical condition is automatically satisfied.

A slogan to remember:

> “Take 1..n, XOR them.
> If the XOR is n → keep all.
> Else remove `XOR(1..n) ^ n`.”

---

### Likely Interview Questions & Short Answers

---

**Q1: What is your high-level strategy for this problem?**

**A:**
I first consider taking the entire range `[1..n]`. I compute the XOR of all numbers from 1 to n.

* If this XOR is already `n`, then the maximum subset of size `n` is valid.
* If it isn’t, I keep as many numbers as possible by dropping exactly one number `x` so that the XOR of the remaining numbers becomes `n`. That means `x = XOR(1..n) ^ n`. I then return all numbers from `1..n` except this `x`.

---

**Q2: How do you compute XOR from 1 to n quickly?**

**A:**
There’s a known pattern based on `n % 4`:

* If `n % 4 == 0` → `XOR(1..n) = n`
* If `n % 4 == 1` → `XOR(1..n) = 1`
* If `n % 4 == 2` → `XOR(1..n) = n + 1`
* If `n % 4 == 3` → `XOR(1..n) = 0`

This comes from grouping 4 consecutive numbers at a time and observing the repeating XOR pattern.

---

**Q3: Why are you sure the maximum size is either n or n-1?**

**A:**
We have only `n` distinct numbers. So the absolute maximum size is `n`.

* If `XOR(1..n) == n`, we achieve size `n`.
* Otherwise, at least one number must be excluded, so the best we can hope for is `n-1`.
  I show that dropping exactly one cleverly chosen number always gives XOR `n`, so we can always get `n-1`. Any subset with size ≤ `n-2` is strictly worse.

---

**Q4: Why does removing `x = XOR(1..n) ^ n` work?**

**A:**
Let `T = XOR(1..n)`.
If I remove element `x`, new XOR is `T ^ x`.
We want: `T ^ x = n`.
Solving for `x`: `x = T ^ n`.
So that is the unique element whose removal adjusts the XOR to exactly `n`.

---

**Q5: Are you sure this `x` always lies between 1 and n?**

**A (short version):**
Yes, based on the 4 cases of `n % 4`:

1. `n % 4 == 0` → `T = n`. This is the case we handle separately (`T == n`), so we never compute `x` here.
2. `n % 4 == 1` → `T = 1`, `x = 1 ^ n`. Here `n` is odd, so `x = n-1` which is in `[1, n]`.
3. `n % 4 == 2` → `T = n + 1`, `x = (n + 1) ^ n = 1`, also in `[1, n]`.
4. `n % 4 == 3` → `T = 0`, `x = 0 ^ n = n`, also in `[1, n]`.

So whenever we go to the “drop one element” branch, `x` is valid.

---

**Q6: How do you argue about lexicographical minimality?**

**A:**

* If `XOR(1..n) == n`, the subset of size `n` is unique; no other subset has size `n`, so it’s automatically lexicographically smallest among maximum-size subsets.
* If `XOR(1..n) != n`, every size-`n-1` subset is `[1..n]` with exactly one element removed. For the XOR to be `n`, that removed element must be exactly `x = XOR(1..n) ^ n`. That makes the maximum-size solution unique again, so the lexicographical condition is automatically satisfied.

---

**Q7: What is the time and space complexity of your solution?**

**A:**

* Computing `XOR(1..n)` via the pattern is O(1).
* Building the answer list (either `[1..n]` or `[1..n]` without one element) costs O(n).
  So total **time complexity** is **O(n)**.
  Extra **space complexity** is O(1) besides the output list.

---

If you walk through these points once or twice, the problem becomes:

> “Compute `T = XOR(1..n)` →
> If `T == n`, answer is `[1..n]`
> Else answer is `[1..n]` except `T ^ n`.”


---

---

### 5. Real-World Use Cases (a few, but easy to talk about)

You probably won’t see **exactly** this problem in production, but the *pattern* (XOR + choose many elements) really appears a lot. Here are a few interview-friendly analogies:

1. **Hardware / Feature-Flag Configuration**

   * Imagine a device where each bit position corresponds to a small feature flag / register between `1..n`.
   * You want to turn on as many flags as possible, but the final XOR of all active flags must equal a specific control code `n` (maybe enforced by firmware).
   * This problem is exactly that: pick many flags from `1..n` such that their XOR is a fixed target.
   * Maximizing count = using the richest configuration of flags while still respecting the XOR constraint.

2. **Network Coding / Parity Checks**

   * In XOR-based error detection or RAID-like systems, parity blocks/packets are XORs of many data blocks.
   * Sometimes you want to choose a large subset of blocks so that their XOR equals a known parity checksum (here, `n`) to reconstruct or verify data.
   * This problem models choosing such a subset of blocks while maximizing redundancy (more blocks involved).

3. **Debugging Bit-wise Bugs / Test-Case Design**

   * When debugging bitwise logic or security keys, you might know that XOR of some subset of operations equals a known bad key.
   * You can model operations as numbers `1..n` and choose a large subset whose XOR equals the bug signature `n`.
   * The “max size subset” idea mimics trying to include as many operations as possible in a failing test case for better reproduction.

These are good to mention briefly to show you recognize XOR is heavily used in **parity, coding, and configuration** problems.

---

### 6. Full Python Program

*With inline comments for logic + time/space complexity + runtime measurement*

Below is a complete, ready-to-run Python program:

* Uses the **optimized** XOR-pattern solution (expected in interviews).
* Follows the required `class Solution:` structure.
* Measures total runtime of main logic using `time.perf_counter()`.

```python
import time


class Solution:
    def subsetXOR(self, n: int):
        """
        Returns a subset of [1..n] such that:
        - XOR of all elements in subset == n
        - Size of subset is maximum possible
        - If multiple, lexicographically smallest is chosen

        Overall time complexity of this function:
        - O(1) to compute XOR(1..n) using n % 4 pattern
        - O(n) to build the resulting subset list
        => O(n) total time

        Space complexity:
        - O(1) extra space (ignoring output list)
        - Output list itself can have n elements in worst case -> O(n) output space
        """

        # ---------- Step 1: Compute XOR from 1 to n using n % 4 pattern ----------
        # Time: O(1), Space: O(1)
        remainder = n % 4

        if remainder == 0:
            xor_1_to_n = n
        elif remainder == 1:
            xor_1_to_n = 1
        elif remainder == 2:
            xor_1_to_n = n + 1
        else:  # remainder == 3
            xor_1_to_n = 0

        # ---------- Step 2: If XOR(1..n) already equals n, take full range ----------
        # Condition check: O(1)
        if xor_1_to_n == n:
            # Building list [1, 2, ..., n]
            # Time: O(n), Space: O(n) output
            full_subset = [value for value in range(1, n + 1)]
            return full_subset

        # ---------- Step 3: Otherwise, remove exactly one element ----------
        # We want XOR(1..n without x) = n
        # Let T = XOR(1..n). Then: T ^ x = n  => x = T ^ n
        # Time: O(1), Space: O(1)
        element_to_remove = xor_1_to_n ^ n

        # ---------- Step 4: Build subset of [1..n] excluding element_to_remove ----------
        # Time: O(n), Space: O(n) output
        result_subset = []
        for value in range(1, n + 1):
            # Each loop iteration is O(1)
            if value != element_to_remove:
                result_subset.append(value)

        # This subset:
        # - Has size n-1
        # - Has XOR exactly n (by construction)
        # - Is unique for size n-1, so it's lexicographically smallest among max-size subsets
        return result_subset


def main():
    """
    Main driver:
    - Reads an integer n from input
    - Calls Solution().subsetXOR(n)
    - Prints the resulting subset and timing information

    Complexity:
    - Input reading: O(1)
    - Calling subsetXOR: O(n)
    - Printing output: O(n) (since we print up to n numbers)
    => Overall time for main: O(n)
    => Extra space: O(n) for the result list
    """

    # Example prompt for clarity (not necessary for online judges)
    print("Enter value for n (e.g. 4 or 5):")

    # Start measuring total time from just before we process input and compute output
    start_time = time.perf_counter()

    # Reading the input value for n
    # Time: O(1)
    n = int(input().strip())

    # Create solution object and compute the subset
    # subsetXOR: O(n) time, O(n) output space
    solver = Solution()
    subset = solver.subsetXOR(n)

    # Stop timing after computation (and right before printing)
    end_time = time.perf_counter()

    # Print the resulting subset
    # Printing the list (converted to string) is O(n)
    print("Subset with XOR equal to n and maximum size:")
    print(subset)

    # Print elapsed time
    elapsed_seconds = end_time - start_time
    print(f"Total elapsed time (seconds): {elapsed_seconds:.6f}")


# Standard guard to allow import without running main
if __name__ == "__main__":
    main()
```

#### How an example run looks (conceptually)

* **Input**

  ```text
  4
  ```

* **Output (typical)**

  ```text
  Enter value for n (e.g. 4 or 5):
  Subset with XOR equal to n and maximum size:
  [1, 2, 3, 4]
  Total elapsed time (seconds): 0.0000xx
  ```

* For `n = 5` you’d see:

  ```text
  Enter value for n (e.g. 4 or 5):
  5
  Subset with XOR equal to n and maximum size:
  [1, 2, 3, 5]
  Total elapsed time (seconds): 0.0000xx
  ```

This program is interview-ready: clean class, clear logic, explicit complexities, and a simple runtime measurement you can mention if they ask about performance in practice.


