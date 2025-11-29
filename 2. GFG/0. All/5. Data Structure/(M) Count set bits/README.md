# Count set bits

**Difficulty:** Medium  
**Accuracy:** 35.77%  
**Submissions:** 248K+  
**Points:** 4  

---

## Problem Statement

You are given a number **n**. Find the total count of set bits for all numbers from **1 to n (both inclusive)**.

---

## Examples

### Example 1

**Input:** `n = 4`  
**Output:** `5`  

**Explanation:**  
For numbers from 1 to 4.  
- for 1: `0 0 1` => 1 set bit,  
- for 2: `0 1 0` => 1 set bit,  
- for 3: `0 1 1` => 2 set bits,  
- for 4: `1 0 0` => 1 set bit.  

Therefore, the total set bits are **5**.

---

### Example 2

**Input:** `n = 17`  
**Output:** `35`  

**Explanation:**  
From numbers 1 to 17 (both inclusive), the total number of set bits are **35**.

---

## Constraints

\[
1 \le n \le 10^8
\]

---

## Expected Complexities

- **Time Complexity:** `O(log n)`  
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Bit Magic  
- Data Structures  

---

## Related Articles

- [Count Total Set Bits In All Numbers From 1 To N](https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n/)

---

---

I’ll follow your numbering.

---

## 2. Explanation + step-by-step dry run

We want:

> Total number of **1-bits** in binary representation of every integer from `1` to `n` (inclusive).

Example `n = 4`:

* `1 = 001` → 1
* `2 = 010` → 1
* `3 = 011` → 2
* `4 = 100` → 1

Total = `1 + 1 + 2 + 1 = 5`.

Brute force is easy but too slow for `n` up to `10^8`, so we need an `O(log n)` idea.

---

### Key idea (optimized): use powers of 2 and patterns

Binary patterns repeat very regularly.

Take a fixed bit position (say the least significant bit):

* For numbers from `0` upwards, it goes: `0,1,0,1,0,1,...`
* So in any block of 2 numbers, **exactly one** has that bit set.

For the 2nd bit (value 2):

* Pattern: `00,01,10,11` → as we count up, each block of 4 numbers has bit-1 set in exactly 2 numbers.

In general, for bit `i` (value `2^i`), in each block of length `2^(i+1)`:

* bit `i` is `0` for the first `2^i` numbers,
* then `1` for the next `2^i` numbers.

But there is an even cleaner formula based on the **highest power of two ≤ n** (the classical GFG formula).

---

### Formula using highest power of 2

Let `f(n)` = total set bits from `1` to `n`.

1. Let `x` be the **largest exponent** such that `2^x ≤ n`.
   (So `2^x` is the highest power of 2 ≤ n.)

2. Consider the range `1 .. 2^x - 1`

   * This includes all `x`-bit numbers below `2^x`.
   * In this range, **each bit position from 0 to x-1 is set exactly in half of the numbers**.
   * Number of integers in this range is `(2^x - 1)`, but easy formula for total set bits here is:
     [
     x \times 2^{x-1}
     ]
     (Each of the `x` bit positions contributes `2^{x-1}` ones.)

3. Consider the range `2^x .. n`

   * For every number in this range, the **MSB bit (bit x)** is `1`.
   * Count of such numbers = `(n - 2^x + 1)`.
   * So MSB contributes `(n - 2^x + 1)` set bits.

4. Remaining lower bits in `2^x .. n`

   * If you subtract `2^x` from every number in `2^x..n`, you get numbers from `0 .. (n - 2^x)`.
   * The lower bits pattern is **exactly the same** as counting set bits from `0 .. (n - 2^x)`.
   * We only need `1..(n - 2^x)`, but `0` has 0 bits, so:
     [
     \text{lower bits contribution} = f(n - 2^x)
     ]

So we get recurrence:

[
f(n) = x \cdot 2^{x-1} ;+; (n - 2^x + 1) ;+; f(n - 2^x)
]

Base: `f(0) = 0`.

---

### Dry run: `n = 17`

We’ll compute `f(17)`.

1. **Find largest power of 2 ≤ 17**

   * `2^4 = 16`, `2^5 = 32 > 17`, so `x = 4`, `p = 2^x = 16`.

2. **Bits in range 1..15 (`1..(p-1)`):**

   * `x * 2^(x-1) = 4 * 8 = 32` set bits.

3. **MSB bits for numbers 16..17:**

   * Count of numbers in this range: `n - p + 1 = 17 - 16 + 1 = 2`.
   * So contribution of MSB = `2`.

4. **Remaining lower bits from 16..17:**

   * Map 16..17 to 0..1 by subtracting 16: we need `f(1)` here.
   * So `f(17) = 32 + 2 + f(1)`.

5. Compute `f(1)` (recursive call):

   * Largest power of 2 ≤ 1: `x = 0`, `p = 1`.
   * Range 1..0 is empty → `x * 2^(x-1)` = `0 * 2^-1` = `0` (we can just treat as 0).
   * MSB bits from 1..1: `n - p + 1 = 1 - 1 + 1 = 1`.
   * Remaining: `n - p = 1 - 1 = 0`, so `f(0) = 0`.

   So `f(1) = 0 + 1 + 0 = 1`.

6. Back to `f(17)`:

   * `f(17) = 32 + 2 + 1 = 35`.

Matches the example.

---

## 3. Python solutions

### 3.1 Brute Force (for understanding, not for constraints)

**Idea:** Iterate from `1` to `n`, count bits of each number (using Kernighan’s trick or `bin(x).count("1")`), sum them.

* Time: `O(n log n)` (log bits per number)
* Too slow for `n = 10^8`, but conceptually simple.

```python
class Solution:
    def countSetBits_bruteforce(self, n: int) -> int:
        """
        Brute-force method:
        For each number from 1 to n, count set bits and sum them.

        Time  : O(n * log n)  (each number has up to log n bits)
        Space : O(1) extra
        """

        total_set_bits = 0

        for value in range(1, n + 1):
            # Kernighan's algorithm to count set bits in current value
            current = value
            bits_in_value = 0
            while current > 0:
                # Remove the lowest set bit
                current &= (current - 1)
                bits_in_value += 1

            total_set_bits += bits_in_value

        return total_set_bits
```

---

### 3.2 Optimized Recursive Solution (classic interview one)

Uses the formula with highest power of 2 ≤ n.

```python
class Solution:
    def countSetBits(self, n: int) -> int:
        """
        Optimized method using highest power of 2 <= n and recursion.

        Recurrence:
            f(n) = x * 2^(x-1) + (n - 2^x + 1) + f(n - 2^x)
        where 2^x <= n < 2^(x+1)

        Time  : O(log n)  (each recursive step reduces n roughly by half)
        Space : O(log n) recursion stack, O(1) extra otherwise
        """

        # Base case: no numbers => no set bits
        if n == 0:
            return 0

        # ---------- Step 1: find highest power of 2 <= n ----------
        # We find x such that 2^x <= n < 2^(x+1)
        x = self._highest_power_exponent(n)
        power_of_two = 1 << x  # 2^x

        # ---------- Step 2: count bits from 1 to (2^x - 1) ----------
        # In this range, each of x lower bits is set exactly 2^(x-1) times
        bits_before_power = x * (1 << (x - 1)) if x > 0 else 0

        # ---------- Step 3: count MSB bits for numbers from 2^x to n ----------
        # All numbers in [2^x, n] have MSB (bit x) set
        msb_bits = n - power_of_two + 1

        # ---------- Step 4: recursively count lower bits contribution ----------
        # Map [2^x, n] to [0, n - 2^x] and reuse f()
        remaining = n - power_of_two
        lower_bits = self.countSetBits(remaining)

        # Total = contribution from:
        # (1) 1..(2^x-1)
        # (2) MSBs in 2^x..n
        # (3) lower bits in 2^x..n (same as f(remaining))
        return bits_before_power + msb_bits + lower_bits

    def _highest_power_exponent(self, n: int) -> int:
        """
        Returns the exponent x such that 2^x <= n < 2^(x+1).

        Simple loop: O(log n) but called only once per recursion level.
        """
        x = 0
        while (1 << (x + 1)) <= n:
            x += 1
        return x
```

---

### 3.3 Optimized Iterative per-bit solution (also O(log n))

Here we treat each bit independently. For bit `i`:

* cycle length `block_len = 2^(i+1)`
* in each full block, bit `i` is `1` for `2^i` numbers
* number of full blocks: `full_blocks = (n + 1) // block_len`
* remaining part length: `remainder = (n + 1) % block_len`
* extra ones from partial block: `max(0, remainder - 2^i)`

Total ones for bit `i`:

[
\text{ones}_i = full_blocks * 2^i + \max(0, remainder - 2^i)
]

Sum over all bit positions that can appear in `n`.

```python
class Solution:
    def countSetBits_iterative(self, n: int) -> int:
        """
        Another optimized O(log n) method.
        We count, for each bit position i, how many numbers from 1..n
        have that bit set, using the repeating block pattern.

        Time  : O(log n)  (we loop over bit positions only)
        Space : O(1)
        """

        total_set_bits = 0
        bit_position = 0

        # We loop while (1 << bit_position) <= n
        while (1 << bit_position) <= n:
            bit_value = 1 << bit_position         # 2^i

            # Length of one full 0-then-1 pattern block at this bit
            block_length = bit_value << 1         # 2^(i+1)

            # Numbers we're considering: 0 .. n  (that's n+1 numbers)
            total_numbers = n + 1

            # Number of complete blocks for this bit
            full_blocks = total_numbers // block_length

            # Each full block contributes bit_value ones
            total_set_bits += full_blocks * bit_value

            # Remaining part that doesn't form a full block
            remainder = total_numbers % block_length

            # In the incomplete block, bit i is 1 for at most (remainder - bit_value) numbers
            # but not less than 0
            extra_ones = max(0, remainder - bit_value)

            total_set_bits += extra_ones

            bit_position += 1

        # We included number 0, but it has 0 bits, so range 1..n is unchanged.
        return total_set_bits
```

Either recursive or iterative version is perfectly fine for interviews; the recursive “highest power of 2” one is especially common on GFG/LeetCode-type questions.

---

## 4. Interview memory tricks + likely Q&A

### Quick memory hook

Think: **“Big Power, Three Parts”**

1. **Big Power** – find largest `2^x` ≤ `n`.
2. **Three Parts**:

   * **Before** power: bits from `1..(2^x - 1)` → `x * 2^(x-1)`
   * **MSB part**: numbers `2^x..n` → `(n - 2^x + 1)` MSB bits
   * **Rest**: recurse on `n - 2^x`

In your head:

> `f(n) = bits_before + msb_bits + f(n - 2^x)`

where
`bits_before = x * 2^(x-1)` (if x>0, else 0)
`msb_bits = n - 2^x + 1`.

If you can recall *“highest power of 2” + “three contributions”*, the whole solution comes back.

---

### 5–line pseudo-code template (recurrence version)

```text
if n == 0: return 0
x = largest exponent with (1<<x) <= n
bits_before = x * 2^(x-1)
msb_bits = n - 2^x + 1
return bits_before + msb_bits + f(n - 2^x)
```

---

### Likely Interview Questions & Short Answers

---

**Q1: What’s your brute-force approach? Complexity?**

**A:**
Iterate `i` from `1` to `n`. For each `i`, count the set bits (using Kernighan’s method `while i>0: i &= i-1`) and add to a global counter.

* Time: `O(n log n)` (each number has up to log n bits).
* Space: `O(1)` extra.
  This is simple but too slow when `n` can be as large as `10^8`.

---

**Q2: How does your optimized approach work in one line?**

**A:**
I repeatedly find the highest power of 2 ≤ `n` and split the answer into three parts:

1. total bits in `1..(2^x - 1)`,
2. MSB bits from `2^x..n`, and
3. recursively count bits in the remaining lower numbers `n - 2^x`.

---

**Q3: Why is `bits_before = x * 2^(x-1)`?**

**A:**
In the range `0..(2^x - 1)` there are `2^x` numbers, each with `x` bits. For each bit position `i` in `0..x-1`, that bit is `1` exactly half the time (every alternate block of length `2^i`). So it is set in `2^(x-1)` numbers. Summing over `x` bit positions:
[
x \times 2^{x-1}
]
Number 0 doesn’t contribute any bits, so the same formula holds for `1..(2^x - 1)`.

---

**Q4: Why are there `(n - 2^x + 1)` MSB bits?**

**A:**
Every number in the range `[2^x, n]` has its most significant bit (bit `x`) set to `1`. The count of numbers there is `n - 2^x + 1`. Each contributes exactly one MSB bit, so that’s the MSB contribution.

---

**Q5: Why do you recurse on `n - 2^x`?**

**A:**
If we subtract `2^x` from each number in `[2^x, n]`, we get numbers in `[0, n - 2^x]`. In this new range the MSB is removed, so the **lower bits pattern** is identical to numbers `0` to `n - 2^x`. The total lower-bit count is exactly `f(n - 2^x)`. Since 0 has zero bits, we effectively count bits from `1` to `n - 2^x`.

---

**Q6: What is the time and space complexity of your optimized solution?**

**A:**
In each recursion step, `n` is reduced by at least half (subtracting the highest power of 2), so the recursion depth is `O(log n)`.

* Time: `O(log n)`
* Space: `O(log n)` due to recursion stack (iterative version can be `O(1)` space).

---

**Q7: Could you do it iteratively instead of recursively?**

**A:**
Yes. One way is to loop over bit positions and, for each bit, use the repeating 0/1 pattern in blocks of size `2^(i+1)` to count how many ones appear in the range `1..n`. That also runs in `O(log n)` time and uses `O(1)` extra space.

---

If you rehearse:

> “**Big Power + 3 parts**: `before + msb + recursion`”

and the 5-line pseudo-code once or twice, you’ll be able to reconstruct both the explanation and the code confidently in an interview.

---

---

Let’s finish this one off nicely.

---

## 5. Real-World Use Cases (easy to talk about)

You can mention **where “count of set bits” or “population count” matters**:

1. **Bitmap / Bitset Indexes in Databases**

   * Large analytics systems store flags (is_active, has_feature_X, etc.) as bitmaps.
   * Counting set bits over a range gives you **how many users/rows match certain criteria**.
   * This problem is like asking: *“If I had IDs 1..n as bit positions, what’s the total number of 1s in all those IDs?”*
   * Shows understanding of **bit-level storage** and **cardinality estimation**.

2. **CPU / GPU Performance Counters & Masks**

   * Hardware often uses bitmasks to represent active cores, active lanes, or enabled features.
   * Counting how many bits are set tells you **how many lanes/cores/features are active** across a range of configurations.
   * Our function is an abstract version of summing population counts across many masks.

3. **Error-Correcting Codes & Parity Checks**

   * In XOR/parity-based codes, the number of set bits matters for **Hamming weight** and error detection.
   * Summing set bits across packet indices or codewords is similar to this problem and shows comfort with **bit manipulation in coding theory / networking**.

4. **Compression / Bit Allocation Analysis**

   * When designing encoding schemes, you might want to estimate **how many bits are 1** in numbers 1..n to reason about entropy or compression behavior.
   * This problem is essentially computing that aggregate Hamming weight.

These are all short, believable, and close enough to what interviewers expect when they ask for “real use cases of bit manipulation”.

---

## 6. Full Python Program (with timing + inline complexity notes)

This uses the **optimized recursive highest-power-of-2 method** (O(log n)) and measures runtime with `time.perf_counter()`.

```python
import time


class Solution:
    def countSetBits(self, n: int) -> int:
        """
        Optimized method using highest power of 2 <= n and recursion.

        Recurrence:
            f(n) = x * 2^(x-1) + (n - 2^x + 1) + f(n - 2^x)
        where 2^x <= n < 2^(x+1)

        Overall complexity of this function:
        - Time  : O(log n)  (n shrinks roughly by half each recursive call)
        - Space : O(log n) recursion stack, O(1) extra memory otherwise
        """

        # ---------- Base Case ----------
        # Time: O(1), Space: O(1)
        if n == 0:
            return 0

        # ---------- Step 1: Find highest power of 2 <= n ----------
        # We find x such that 2^x <= n < 2^(x+1).
        # Loop runs at most O(log n) times per call.
        x = self._highest_power_exponent(n)  # Time: O(log n), Space: O(1)
        highest_power = 1 << x               # 2^x, Time: O(1)

        # ---------- Step 2: Count bits from 1 to (2^x - 1) ----------
        # In 1..(2^x - 1), each of the x bit positions appears as '1'
        # exactly 2^(x-1) times.
        #
        # So contribution = x * 2^(x-1)
        #
        # Time: O(1), Space: O(1)
        bits_before_power = x * (1 << (x - 1)) if x > 0 else 0

        # ---------- Step 3: Count MSB bits from 2^x to n ----------
        # All numbers in [2^x, n] have the MSB (bit x) set.
        # Count of such numbers = (n - 2^x + 1).
        #
        # Time: O(1), Space: O(1)
        msb_bits = n - highest_power + 1

        # ---------- Step 4: Recurse on remaining numbers ----------
        # Remaining numbers after removing MSB: n - 2^x
        # Lower bits of 2^x..n correspond exactly to numbers 0..(n - 2^x).
        # So we add f(n - 2^x).
        #
        # Time: T(n - 2^x), Space: extra recursion frame
        remaining = n - highest_power
        lower_bits = self.countSetBits(remaining)

        # ---------- Step 5: Combine contributions ----------
        # Time: O(1)
        total = bits_before_power + msb_bits + lower_bits
        return total

    def _highest_power_exponent(self, n: int) -> int:
        """
        Returns x such that 2^x <= n < 2^(x+1).

        Implementation: simple loop doubling power.
        Time: O(log n) per call
        Space: O(1)
        """
        x = 0
        # (1 << (x + 1)) is 2^(x+1)
        while (1 << (x + 1)) <= n:
            x += 1
        return x


def main():
    """
    Driver function:
    - Reads n from input
    - Measures time to compute total set bits from 1 to n
    - Prints result and elapsed time

    Complexity of main (excluding input I/O and printing):
    - Calls countSetBits(n) once: O(log n) time, O(log n) stack space
    - I/O and printing are O(1) relative to n (ignoring number of digits)
    """

    print("Enter n (e.g. 4, 17, 100000000):")

    # Start timer just before reading input and doing the computation.
    start_time = time.perf_counter()

    # ----- Input read -----
    # Time: O(1), Space: O(1)
    n = int(input().strip())

    solver = Solution()

    # ----- Core computation -----
    # Time: O(log n), Space: O(log n) recursion stack
    total_bits = solver.countSetBits(n)

    # Stop timer right after computation.
    end_time = time.perf_counter()

    # ----- Output section -----
    # Printing is O(1) w.r.t. n (ignoring digits length)
    print(f"Total count of set bits from 1 to {n}: {total_bits}")

    elapsed_seconds = end_time - start_time
    print(f"Total elapsed time (seconds): {elapsed_seconds:.6f}")


if __name__ == "__main__":
    main()
```

### How a sample run looks (conceptually)

**Input**

```text
17
```

**Output**

```text
Enter n (e.g. 4, 17, 100000000):
Total count of set bits from 1 to 17: 35
Total elapsed time (seconds): 0.0000xx
```

You can reuse this exact structure in coding rounds; just strip the prints if they want only the function.
