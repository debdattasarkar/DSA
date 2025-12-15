# Count Indices to Balance Even and Odd Sums 🔢

**Difficulty:** Medium  
**Accuracy:** 78.84%  
**Submissions:** 4K+  
**Points:** 4  

---

## Problem Statement

Given an array `arr[]`, count the **number of indices** such that deleting the element at that index and shifting all elements after it one position left results in an array where the **sum of elements at even indices equals the sum at odd indices**.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 1, 6, 4]`  
**Output:** `1`  

**Explanation:**  
After removing `arr[1]`, the resulting array will be `[2, 6, 4]`.  
- Sum of elements at odd indices is `arr[1] = 6`  
- Sum of elements at even indices is `arr[0] + arr[2] = 2 + 4 = 6`  

Thus, there is exactly one such index.

---

### Example 2

**Input:** `arr[] = [1, 1, 1]`  
**Output:** `3`  

**Explanation:**  
Removing **any** element makes the sum of odd and even indexed elements equal. Hence, there are 3 valid indices.

---

## Constraints

- \(1 \le \text{arr.size()} \le 10^5\)  
- \(0 \le \text{arr}[i] \le 10^4\)


---

---

Nice, this is a fun one. I’ll assume the problem is:

> **Given an array `arr`, count how many indices you can remove such that in the resulting array the sum of elements at even indices equals the sum of elements at odd indices.** ([GeeksforGeeks][1])

We’ll go through explanation + dry run → Python code (brute + optimized) → interview memory + Q&A.

---

## 2. Explanation + Step-by-step dry run

### What happens when we “remove” one index?

* We remove `arr[i]`.
* The elements **before** `i` keep their indices and parity (even/odd).
* All elements **after** `i` shift left by one → their parity flips:

  * old even index → new odd index
  * old odd index → new even index

We want count of indices `i` such that after this removal:

> `sumEven == sumOdd` in the *new* array.

---

### Naive idea (O(n²))

For each index `i`:

1. Pretend we remove `arr[i]`.
2. Rebuild “new indices” from left to right, using a separate index counter.
3. Add numbers to `evenSum` or `oddSum` depending on the new index parity.
4. If `evenSum == oddSum`, increment answer.

Correct but O(n²) because for each `i` you scan the whole array again. ([GeeksforGeeks][1])

---

### Optimized idea (O(n))

We don’t want to rescan the whole array for every `i`. Instead we maintain **running sums** for the “left part” and “right part”.

Definitions (0-based indices on the original array):

* `rightEvenSum` = sum of elements at even indices **from current i onwards**.
* `rightOddSum`  = sum of elements at odd indices **from current i onwards**.
* `leftEvenSum`  = sum of elements at even indices **before i**.
* `leftOddSum`   = sum of elements at odd indices **before i**.

We do it in two passes:

1. **Initial pass**: compute total `rightEvenSum` and `rightOddSum` (whole array).
2. **Single scan `i = 0..n-1`**:

   * First, **remove** `arr[i]` from the right side:

     * if `i` is even → `rightEvenSum -= arr[i]`
     * else         → `rightOddSum  -= arr[i]`
   * After removal, the right side shifts → its parity flips:

     * new even sum = `leftEvenSum + rightOddSum`
     * new odd sum  = `leftOddSum  + rightEvenSum`
   * Check condition:
     `if leftOddSum + rightEvenSum == leftEvenSum + rightOddSum: res += 1`
   * Finally, move `arr[i]` to the left side (for the next iteration):

     * if `i` even → `leftEvenSum += arr[i]`
     * else        → `leftOddSum  += arr[i]`

That’s it: one pass for initial sums (O(n)) + one pass for checking all indices (O(n)) → total O(n). ([GeeksforGeeks][1])

---

### Dry run: `arr = [2, 1, 6, 4]`

Goal: find indices whose removal makes even-sum == odd-sum.

**Step 1 – initial right sums**

Index and parity:

* 0 (even) → 2
* 1 (odd)  → 1
* 2 (even) → 6
* 3 (odd)  → 4

So:

```text
rightEvenSum = 2 + 6 = 8
rightOddSum  = 1 + 4 = 5
leftEvenSum  = 0
leftOddSum   = 0
res = 0
```

---

**i = 0 (removing 2)**

1. Remove from right:

   * i is even → `rightEvenSum = 8 - 2 = 6`, `rightOddSum = 5`.
2. After removal:

   * new even sum  = `leftEvenSum + rightOddSum = 0 + 5 = 5`
   * new odd sum   = `leftOddSum  + rightEvenSum = 0 + 6 = 6`
   * Not equal → don’t count.
3. Move 2 to left:

   * i even → `leftEvenSum = 2`, `leftOddSum = 0`.

---

**i = 1 (removing 1)**

1. Remove from right:

   * i is odd → `rightOddSum = 5 - 1 = 4`, `rightEvenSum = 6`.
2. After removal:

   * new even sum = `leftEvenSum + rightOddSum = 2 + 4 = 6`
   * new odd sum  = `leftOddSum  + rightEvenSum = 0 + 6 = 6`
   * Equal → `res = 1` (index 1 is valid).
3. Move 1 to left:

   * i odd → `leftOddSum = 1`, `leftEvenSum = 2`.

---

**i = 2 (removing 6)**

1. Remove from right:

   * i even → `rightEvenSum = 6 - 6 = 0`, `rightOddSum = 4`.
2. After removal:

   * new even sum = `leftEvenSum + rightOddSum = 2 + 4 = 6`
   * new odd sum  = `leftOddSum  + rightEvenSum = 1 + 0 = 1`
   * Not equal → no increment.
3. Move 6 to left:

   * `leftEvenSum = 8`, `leftOddSum = 1`.

---

**i = 3 (removing 4)**

1. Remove from right:

   * i odd → `rightOddSum = 4 - 4 = 0`, `rightEvenSum = 0`.
2. After removal:

   * new even sum = `leftEvenSum + rightOddSum = 8 + 0 = 8`
   * new odd sum  = `leftOddSum  + rightEvenSum = 1 + 0 = 1`
   * Not equal.
3. Move 4 to left (not needed anymore, loop ends).

Final `res = 1` → only index 1 works (matching example). ([GeeksforGeeks][1])

---

## 3. Python solutions (brute + optimized)

### 3.1 Brute-force solution (clear but O(n²))

```python
from typing import List

class Solution:
    def cntWays_bruteforce(self, arr: List[int]) -> int:
        """
        Brute-force:
        For each index i, simulate removal of arr[i],
        recompute even/odd sums in the resulting array
        using a new index counter.

        Time  : O(n^2)  (n indices * up to n elements summed)
        Space : O(1)    (only counters)
        """
        n = len(arr)
        valid_indices = 0

        # Try removing each index i
        for remove_idx in range(n):
            even_sum = 0
            odd_sum = 0
            new_index = 0  # index in the "new" array after removal

            for j in range(n):
                # Skip the removed index
                if j == remove_idx:
                    continue

                if new_index % 2 == 0:
                    even_sum += arr[j]
                else:
                    odd_sum += arr[j]

                new_index += 1

            if even_sum == odd_sum:
                valid_indices += 1

        return valid_indices
```

---

### 3.2 Optimized O(n) prefix-sum style solution (what you should use)

```python
from typing import List

class Solution:
    def cntWays(self, arr: List[int]) -> int:
        """
        Optimized solution using prefix/suffix-like sums.

        Idea:
            - Precompute total sum of elements at even and odd indices.
            - Traverse array once, treating each index as "removed":
                * Subtract arr[i] from the appropriate right-side sum
                  (even or odd, based on i % 2).
                * After removal, the right side's parity flips:
                      new_even_sum = leftEvenSum + rightOddSum
                      new_odd_sum  = leftOddSum  + rightEvenSum
                * If new_even_sum == new_odd_sum, this index is valid.
                * Then add arr[i] into the leftEvenSum/leftOddSum
                  for next iterations.

        Time  : O(n)
        Space : O(1)  (just a handful of counters)
        """
        n = len(arr)
        if n == 0:
            return 0

        # 1) Compute initial right-side sums (even and odd indices)
        right_even_sum = 0
        right_odd_sum = 0
        for i, value in enumerate(arr):
            if i % 2 == 0:
                right_even_sum += value
            else:
                right_odd_sum += value

        # 2) Left-side sums start at zero
        left_even_sum = 0
        left_odd_sum = 0

        valid_indices = 0

        # 3) Iterate treating each index as the removed one
        for i, value in enumerate(arr):
            # Remove current value from the right side
            if i % 2 == 0:
                right_even_sum -= value
            else:
                right_odd_sum -= value

            # After removal, right side shifts:
            # old-right-odd -> new-even, old-right-even -> new-odd
            new_even_sum = left_even_sum + right_odd_sum
            new_odd_sum = left_odd_sum + right_even_sum

            if new_even_sum == new_odd_sum:
                valid_indices += 1

            # Add current element to left side for next positions
            if i % 2 == 0:
                left_even_sum += value
            else:
                left_odd_sum += value

        return valid_indices
```

You can keep both methods in the same class for practice; on sites like GFG you’d submit only `cntWays`.

---

## 4. Interview: how to remember & what they might ask

### Quick memory hook

Try to remember just this sentence:

> **“Maintain left/right sums for even/odd; on remove `i`, flip right parity and compare.”**

Or as a tiny formula:

* **New even sum**  = `leftEven + rightOdd`
* **New odd sum**   = `leftOdd + rightEven`
* Check `new_even == new_odd`.

And the flow:

1. Precompute total `rightEven`, `rightOdd`.
2. For each index `i`:

   * subtract `arr[i]` from either `rightEven` or `rightOdd`,
   * compare `leftOdd + rightEven` vs `leftEven + rightOdd`,
   * then add `arr[i]` to `leftEven` or `leftOdd`.

If you can recall **“LE + RO vs LO + RE”** (LeftEven + RightOdd vs LeftOdd + RightEven), you can re-derive the rest.

---

### Likely interview Q&A

---

**Q1. What is the naive solution and its complexity?**

**A:**
Naively, for each index `i`, we simulate removing `arr[i]`, recompute the sums at even and odd indices in the new array using a fresh index counter, and check if they’re equal. That’s O(n) work for each of n indices, so O(n²) time with O(1) extra space. ([GeeksforGeeks][1])

---

**Q2. How does the optimized O(n) approach work in one pass?**

**A:**
We precompute the sum of elements at even and odd indices over the entire array (`rightEvenSum`, `rightOddSum`). As we scan index `i`:

* We subtract `arr[i]` from the corresponding right sum (even or odd).
* After removal, all elements to the right shift left, so the right side’s parity flips:

  * old right odd → new even,
  * old right even → new odd.
* Thus after removal:

  * `newEvenSum = leftEvenSum + rightOddSum`
  * `newOddSum  = leftOddSum  + rightEvenSum`
* If these two are equal, index `i` is valid.
* Then we add `arr[i]` to `leftEvenSum` or `leftOddSum` depending on its original parity and move on. ([GeeksforGeeks][1])

This does constant work per index → O(n).

---

**Q3. Why does the right side’s parity flip after removal?**

**A:**
Because we use 0-based indexing. When we remove element at index `i`, every element originally at index `j > i` moves to index `j-1`. Their new parity is `(j-1) % 2`, which is the opposite of `j % 2`. So all right-side even indices become odd, and vice versa.

---

**Q4. What are the time and space complexities of your optimized solution?**

**A:**

* Time: One pass to compute initial sums (O(n)), one pass to check each index (O(n)) → total **O(n)**.
* Space: Only four running sums and a counter, so **O(1)** auxiliary space.

---

**Q5. Could you also do this with explicit prefix arrays instead of four running sums?**

**A:**
Yes. We could precompute:

* `prefixEven[i]`, `prefixOdd[i]` – sums up to index i.
* From them, derive left sums and right sums in O(1) per index.

But that takes O(n) extra space. The four-sum method is just a compressed prefix/suffix approach with O(1) space.

---

If you keep the picture **“LE + RO == LO + RE after removing i”** in your head, you’ll be able to recreate the solution and code confidently in an interview.

[1]: https://www.geeksforgeeks.org/dsa/count-ways-to-make-sum-of-odd-and-even-indexed-elements-equal-by-removing-an-array-element/ "Equal Odd-Even Sum After Removal - GeeksforGeeks"

---

---

Nice, let’s close this one.

I’ll stick to the same problem we already discussed:

> **Count indices `i` such that if you remove `arr[i]`, the resulting array has equal sum at even and odd indices.**

---

## 5. Real-World Use Cases (easy to talk about)

These are more *analogies* than literal “delete index to balance sums”, but they map nicely and interviewers like them.

1. **Fair load balancing across 2 shards / queues**

   * Suppose a system splits requests into **two queues**:

     * even-indexed requests → shard A,
     * odd-indexed requests → shard B.
   * If one request is corrupted or can be dropped, which one can we drop so that the **total work** sent to A and B is equal?
   * Our algorithm: treat A’s work as “even-index sum” and B’s as “odd-index sum”; we find the indices whose removal balances them.

2. **Balanced team assignments by position**

   * People are seated in a line; even positions belong to Team X, odd positions to Team Y.
   * One person is allowed to leave (or be moved) – which position can change so that total “skill points” on each team become equal?
   * Exactly the same computation: positions are indices, skill is `arr[i]`.

3. **Memory bank / channel balancing with a single exclusion**

   * Imagine interleaving memory accesses alternating between **two channels** (even/odd index).
   * You must drop one request to achieve balanced total bandwidth between these channels.
   * Again, we’re computing which index to drop so that sum on each channel becomes equal.

In an interview you can summarize:

> “Any time data is split by index parity into two groups (two servers, two teams, two channels) and you want to drop exactly one element to make the totals equal, this algorithm applies.”

---

## 6. Full Python Program with Timing & Complexity Comments

This is a complete, runnable script:

* Reads `n` and the array.
* Uses the **O(n)** `cntWays` solution.
* Prints the count and total runtime.

```python
import time
from typing import List


class Solution:
    def cntWays(self, arr: List[int]) -> int:
        """
        Optimized solution using prefix/suffix-like sums.

        Let n = len(arr).

        IDEA:
            - Treat even and odd indices as two "buckets".
            - Precompute total sum of values in even positions (right_even_sum)
              and odd positions (right_odd_sum).
            - We'll scan from left to right and conceptually "remove" arr[i].
              After removal, all elements to the right shift left by one,
              so their parity flips (even <-> odd).

            - Maintain:
                left_even_sum: sum of values at even indices to the LEFT of i
                left_odd_sum : sum of values at odd  indices to the LEFT of i
                right_even_sum, right_odd_sum: as defined above, but for i..end

            - For each index i:
                1) Subtract arr[i] from the appropriate right_* sum.
                2) After this removal, the new sums become:
                       new_even_sum = left_even_sum + right_odd_sum
                       new_odd_sum  = left_odd_sum  + right_even_sum
                3) If new_even_sum == new_odd_sum, this index is a valid answer.
                4) Add arr[i] to left_even_sum or left_odd_sum for next i.

        COMPLEXITY:
            - First loop to compute right_even_sum/right_odd_sum:  O(n)
            - Second loop to test each index:                       O(n)
            => Time  : O(n)
            - Sums and counters only:                               O(1) extra space
        """
        n = len(arr)
        if n == 0:
            return 0

        # ------------------------ 1) Initial right sums ------------------------ #
        # Time: O(n), Space: O(1)
        right_even_sum = 0
        right_odd_sum = 0
        for i, value in enumerate(arr):
            if i % 2 == 0:
                right_even_sum += value
            else:
                right_odd_sum += value

        # Left sums start at zero (no elements on the left initially).
        left_even_sum = 0
        left_odd_sum = 0

        valid_indices = 0

        # ------------------ 2) Scan each index as "removed" ------------------- #
        # Single pass, O(n) time.
        for i, value in enumerate(arr):
            # Remove current value from right-side sums: O(1)
            if i % 2 == 0:
                right_even_sum -= value
            else:
                right_odd_sum -= value

            # After removal, the right segment shifts left by 1:
            #   old-right-odd --> new-even
            #   old-right-even --> new-odd
            # So in the *new* array:
            #   new_even_sum = left_even_sum + right_odd_sum
            #   new_odd_sum  = left_odd_sum  + right_even_sum
            new_even_sum = left_even_sum + right_odd_sum
            new_odd_sum = left_odd_sum + right_even_sum

            # Check balance: O(1)
            if new_even_sum == new_odd_sum:
                valid_indices += 1

            # Move current value from "right" to "left" for next iterations: O(1)
            if i % 2 == 0:
                left_even_sum += value
            else:
                left_odd_sum += value

        return valid_indices


# --------------------------- Driver with timing --------------------------- #

def main():
    """
    Driver to:
        - Read input.
        - Run Solution.cntWays(arr).
        - Print result and total runtime.

    Input format (simple):
        n
        a0 a1 a2 ... a(n-1)

    Example:
        4
        2 1 6 4

    Explanation:
        Removing index 1 -> new array [2, 6, 4]
        Even indices: 2 + 4 = 6
        Odd indices:  6
        Balanced, so answer is 1.
    """
    print("Enter n (size of array):")
    line = input().strip()
    if not line:
        print("No input provided.")
        return
    n = int(line)

    print(f"Enter {n} integers for the array:")
    arr_str = input().split()
    # Defensive: trim or pad to size n
    arr = list(map(int, arr_str[:n]))
    if len(arr) < n:
        arr.extend([0] * (n - len(arr)))  # pad zeros if not enough numbers

    solver = Solution()

    # Start timing just before the algorithm: high-resolution perf counter.
    start_time = time.perf_counter()

    # Core algorithm: O(n) time, O(1) extra space
    ways = solver.cntWays(arr)

    # Stop timing after algorithm.
    end_time = time.perf_counter()

    print("\nNumber of indices whose removal balances even/odd sums:")
    print(ways)

    print(f"\nTotal elapsed time (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

### Example run (mentally)

Input:

```text
4
2 1 6 4
```

Output (typical):

```text
Enter n (size of array):
4
Enter 4 integers for the array:
2 1 6 4

Number of indices whose removal balances even/odd sums:
1

Total elapsed time (seconds): 0.00000xx
```

You can paste this into a `.py` file and run directly.
For a coding platform, you’d normally only submit the `Solution` class with `cntWays`, but this full script is perfect for practice, verifying behavior, and seeing actual runtime.
