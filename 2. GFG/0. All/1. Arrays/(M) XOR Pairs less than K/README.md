# XOR Pairs less than K ⚡

**Difficulty:** Medium  
**Accuracy:** 61.87%  
**Submissions:** 4K+  
**Points:** 4  

---

## Problem Statement

Given an array **arr[]** and an integer **k**, we need to count the number of pairs from the given array such that the **Bitwise XOR** of each pair is **less than k**.

---

## Examples

### Example 1

**Input:** `arr = [1, 2, 3, 5], k = 5`  
**Output:** `4`  

**Explanation:**  
Bitwise XOR of all possible pairs that satisfy the given conditions are:  

- `arr[0] ^ arr[1] = 1 ^ 2 = 3`  
- `arr[0] ^ arr[2] = 1 ^ 3 = 2`  
- `arr[0] ^ arr[3] = 1 ^ 5 = 4`  
- `arr[1] ^ arr[2] = 2 ^ 3 = 1`  

Therefore, the required output is **4**.

---

### Example 2

**Input:** `arr[] = [3, 5, 6, 8], k = 7`  
**Output:** `3`  

**Explanation:**  
Bitwise XOR of all possible pairs that satisfy the given conditions are:  

- `arr[0] ^ arr[1] = 6`  
- `arr[0] ^ arr[2] = 5`  
- `arr[1] ^ arr[2] = 3`  

Therefore, the required output is **3**.

---

## Constraints

\[
1 \leq \text{arr.size()} ,\; k \leq 5 \times 10^4
\]  

\[
1 \leq \text{arr[i]} \leq 5 \times 10^4
\]

---

## Expected Complexities

- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(n)`

---

## Related Articles

- Count Pairs Having Bitwise Xor Less Than K From Given Array


---

---

I’ll go in order: explanation + dry run → Python brute + optimized trie → interview memory tricks + Q&A.

---

## 2. Explanation + Step-by-Step Dry Run

**Task:**
Given `arr[]` and integer `k`, count how many **pairs (i < j)** satisfy:

[
(arr[i] \oplus arr[j]) < k
]

---

### 2.1 Brute Force Idea (simple but slow)

* For every pair `(i, j)` with `i < j`, compute `arr[i] ^ arr[j]`.
* If it’s `< k`, increment a counter.

**Time:** `O(n²)` – too slow when `n` is big (expected is `O(n)` / `O(n log MaxVal)`).

---

### 2.2 Optimized Idea – **Bitwise Trie**

We need something like `O(n log MaxVal)`.

We process the array **left to right**, and for each value `x = arr[i]`:

1. We count how many **previous** elements `y` (already inserted into a structure) satisfy `x ^ y < k`.
2. Then we **insert `x`** into the structure.

If we do that, each pair `(i, j)` is counted exactly once when we process `j`.

The tricky part: how to count “#y such that `x ^ y < k`” fast?

#### Use a binary Trie (also called bitwise prefix tree)

* Each number is stored as a path of bits from MSB → LSB.
* Each node has up to 2 children: bit `0` and bit `1`.
* Every node stores a `count` = how many numbers go through this node (subtree size).

Now, we need a function:

> `countLessThan(x, k)`:
> How many numbers `y` in the trie satisfy `x ^ y < k`?

We walk from the **most significant bit** downwards:

For a bit position `b`:

* Let `bit_x = (x >> b) & 1`
* Let `bit_k = (k >> b) & 1`

We consider how XOR compares **bit by bit** to `k`:

#### Case 1: `bit_k == 0`

* For XOR result `< k`, at this bit we **cannot exceed** `k`.
* If higher bits are equal so far, we must have `xor_bit = 0` here.
* `xor_bit = bit_x ^ bit_y = 0` ⇒ `bit_y = bit_x`.
* So we **must** go to the child with bit `bit_x`.
  No counting yet, we just continue.

#### Case 2: `bit_k == 1`

* At this bit, XOR is allowed to be either:

  * `0` (prefix smaller than k only later), or
  * `1` (prefix equals k here, we must stay tight for lower bits).

Split it:

* **Branch with XOR bit 0**: `bit_y = bit_x`

  * Then `xor_bit = 0` while `k` has `1` at this bit.
  * So up to this bit, `xor_prefix < k_prefix` already.
  * All numbers under this branch are **guaranteed** to produce XOR `< k` regardless of lower bits.
    ⇒ **Add the full subtree count** of child `bit_x` to answer.

* **Branch with XOR bit 1**: `bit_y = 1 - bit_x`

  * Here `xor_bit = 1` matches `k`’s bit `1`.
  * Prefix up to this bit is equal to k’s prefix, so we must continue carefully on lower bits.
    ⇒ Move `node` to child `1 - bit_x` and continue loop (tight comparison).

If a required child doesn’t exist, we stop that path.

Do this from highest bit down to 0 → complexity per query: `O(#bits)`.

For values `<= 5 * 10^4`, `#bits` ~ 16, so overall `O(n * 16)`.

---

### 2.3 Dry Run: `arr = [1, 2, 3, 5]`, `k = 5`

We’ll use 3 bits because `5 < 8`:

* `1 = 001`
* `2 = 010`
* `3 = 011`
* `5 = 101`
* `k = 101`

We process array left to right.

#### Step 1: `x = 1 (001)`

* Trie is **empty**.
* `countLessThan(1, 5)` = 0.
* Insert `001` into trie (increment counts along path `0 -> 0 -> 1` from MSB to LSB).

#### Step 2: `x = 2 (010)`

Now trie contains `{1}`.

Compute `countLessThan(010, 101)`:

Bits from MSB (bit 2) to LSB (bit 0):

* **bit 2**: `bit_x=0`, `bit_k=1`
  Case 2 (`bit_k=1`):

  * Branch XOR=0 → `bit_y=0` child: this is root’s `0` child, has subtree count 1 (`{1}`).
    Add 1 to answer.
  * Branch XOR=1 → `bit_y=1` child: doesn’t exist → cannot continue this branch.
    Node becomes `None` → stop.
    So `countLessThan(2, 5) = 1`.

This 1 corresponds to pair (1, 2):

* `1 ^ 2 = 3 < 5`.

Insert `010` into trie (`0 -> 1 -> 0`).

**Total pairs so far: 1**

---

#### Step 3: `x = 3 (011)`

Trie has `{1, 2}`.

Compute `countLessThan(3, 5)`:

* **bit 2**: `bit_x=0`, `bit_k=1`:

  * Branch XOR=0 → use child `0`: subtree has 2 numbers (`1` and `2`) → add 2.
  * Branch XOR=1 → child `1` doesn’t exist → stop.

So `countLessThan(3, 5) = 2`:

* `1 ^ 3 = 2 < 5`
* `2 ^ 3 = 1 < 5`

Insert `011`.

**Total pairs so far: 1 + 2 = 3**

---

#### Step 4: `x = 5 (101)`

Trie has `{1, 2, 3}`.

Compute `countLessThan(5, 5)`:

* **bit 2**: `bit_x=1`, `bit_k=1`:

  * Branch XOR=0: needs `bit_y=1` child; but all numbers start with `0` at bit2 ⇒ child `1` is empty; add 0.
  * Branch XOR=1: go to child `0` (since `bit_y = 0` gives xor=1).
* **bit 1**: now at nodes for numbers `{1,2,3}`.
  `bit_x=0`, `bit_k=0`:

  * Must keep XOR bit=0 → we must go to child `bit_y=0` (i.e., `bit_y = 0`)
    That corresponds to numbers with second bit 0 → `{1}`.
* **bit 0**: at node representing numbers `{1}`.
  `bit_x=1`, `bit_k=1`:

  * Branch XOR=0 → `bit_y=1` child? For number 1 (001), bit0=1, so child exists with count 1.
    Add 1 to answer.
  * Branch XOR=1 → child with `bit_y=0`? none → stop.

So `countLessThan(5, 5) = 1` → pair: `(2, 5)`? No, check:

Pairs with 5:

* `1 ^ 5 = 4 < 5` ✅
* `2 ^ 5 = 7 >= 5` ❌
* `3 ^ 5 = 6 >= 5` ❌

So only `1` is counted → correct.

**Final total pairs = 1 + 2 + 1 = 4**, matching the example.

---

## 3. Python Solutions

### 3.1 Brute Force – Simple O(n²)

```python
class Solution:
    def cntPairs_bruteforce(self, arr, k):
        """
        Brute-force method:
        - Check every pair (i < j).
        - Count how many have XOR < k.

        Time  : O(n^2)
        Space : O(1) extra
        """
        n = len(arr)
        valid_pair_count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] ^ arr[j]) < k:
                    valid_pair_count += 1

        return valid_pair_count
```

Nice for understanding, not for large `n`.

---

### 3.2 Optimized – Binary Trie (bitwise prefix tree)

We’ll use up to 16 bits (`2^16 = 65536 > 5*10^4`), so safe for constraints.

#### Helper Trie Node

```python
class TrieNode:
    def __init__(self):
        # children[0] for bit 0, children[1] for bit 1
        self.children = [None, None]
        # how many numbers pass through this node (subtree size)
        self.count = 0
```

#### Main Solution

```python
class Solution:
    def __init__(self):
        # maximum bit position we care about (15 covers values up to 2^16-1)
        self.MAX_BIT = 15

    def cntPairs(self, arr, k):
        """
        Count number of pairs (i < j) such that arr[i] ^ arr[j] < k.

        Approach:
        - Maintain a binary Trie of previously seen numbers.
        - For each number x in arr (from left to right):
            * Query the Trie: how many previous y have x ^ y < k ?
            * Insert x into the Trie.
        - Sum all these counts.

        Time complexity:
            - For each of n numbers, we do:
                * query: O(#bits) = O(log MaxValue)
                * insert: O(#bits)
            -> Total O(n log MaxValue), with MaxValue <= 5*10^4 (≈ 16 bits)
        Space complexity:
            - Trie nodes: at most one node per distinct (prefix, bit) combination.
            - In worst case O(n * #bits) = O(n log MaxValue).
        """

        root = TrieNode()
        total_pairs = 0
        trie_built = False  # helps explain; not strictly required

        for value in arr:
            if trie_built:
                # Count how many previous numbers y satisfy value ^ y < k
                total_pairs += self._count_less_than(root, value, k)

            # Insert current value into the Trie, so it can pair with future numbers
            self._insert(root, value)
            trie_built = True

        return total_pairs

    # ---------- Trie insert ----------
    def _insert(self, root, number):
        """
        Insert 'number' into the binary Trie.

        Time  : O(#bits)
        Space : O(#bits) for new nodes (amortized)
        """
        node = root
        node.count += 1  # root also counts this number

        # Process bits from most significant to least significant
        for bit_pos in range(self.MAX_BIT, -1, -1):
            bit = (number >> bit_pos) & 1

            # Create child node if necessary
            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            # Move to child and increment its count
            node = node.children[bit]
            node.count += 1

    # ---------- Count y such that (number ^ y) < k ----------
    def _count_less_than(self, root, number, k):
        """
        Given the current Trie of previously inserted numbers,
        return count of numbers y such that (number ^ y) < k.

        Time : O(#bits)
        """
        node = root
        if node is None:
            return 0

        result = 0

        for bit_pos in range(self.MAX_BIT, -1, -1):
            if node is None:
                break  # no more numbers in this path

            bit_x = (number >> bit_pos) & 1
            bit_k = (k >> bit_pos) & 1

            if bit_k == 0:
                # XOR bit must be 0 (otherwise we'd exceed k at this position)
                # So y must have the same bit as x at this position.
                node = node.children[bit_x]
            else:
                # bit_k == 1

                # 1) Branch where XOR bit = 0 -> y_bit = bit_x
                #    This makes prefix < k because k has 1 here.
                #    So all numbers in that subtree are valid.
                same_child = node.children[bit_x]
                if same_child is not None:
                    result += same_child.count

                # 2) Branch where XOR bit = 1 -> y_bit = 1 - bit_x
                #    This keeps prefix equal to k, so we must continue exploring.
                node = node.children[1 - bit_x]

        return result
```

This is the version you want to describe in interviews.

---

## 4. Interview Memory Tricks + Likely Q&A

### 4.1 5-Line Pseudo-Code Template (Outer Logic)

```text
root = empty trie
ans = 0
for each x in arr:
    ans += countLess(root, x, k)   // how many y so far have x^y < k
    insert(root, x)
return ans
```

### 4.2 5-Line Pseudo-Code Template (countLess function)

```text
node = root; res = 0
for bit from MAX_BIT down to 0:
    bx = (x>>bit)&1; bk = (k>>bit)&1
    if bk == 1:
        res += count(child(node, bx))        // XOR bit 0 branch
        node = child(node, 1-bx)             // stay tight with XOR bit 1
    else:
        node = child(node, bx)               // XOR bit must be 0
return res
```

If you remember these 2 skeletons, you can regenerate full code quickly.

---

### 4.3 Easy Mnemonic

Think: **“Past Trie, Less-Than K” → “Bit-by-Bit Split”**

Or the phrase:

> **“For each x: query-then-insert; in query, when k bit is 1, add same-bit branch and follow diff-bit branch.”**

Break it mentally into 3 steps:

1. **Build:** Keep a **trie of past numbers**.
2. **Query:** For each new number `x`, walk bits from MSB to LSB:

   * If `k` bit is `0` → must take equal bit.
   * If `k` bit is `1` →

     * **add** subtree where XOR bit is 0 (safe smaller prefix),
     * **go down** subtree where XOR bit is 1 (still equal prefix).
3. **Insert:** Insert `x` into trie for later numbers.

---

### 4.4 Likely Interview Q&A

---

**Q1: What’s the brute-force solution? Complexity?**

**A:**
Loop over all pairs `(i, j)` with `i < j`, compute `arr[i] ^ arr[j]`, check if it’s `< k`, and count.

* Time complexity: `O(n²)`
* Space complexity: `O(1)`
  This doesn’t meet the expected constraints for large `n`.

---

**Q2: How does the optimized approach work at a high level?**

**A:**
I process the array left to right while maintaining a binary trie of previously seen numbers. For each new value `x`, I query the trie to count how many previous values `y` satisfy `x ^ y < k`, then insert `x` into the trie. The key is a bitwise traversal that compares `(x ^ y)` with `k` from the most significant bit downward.

---

**Q3: How do you count `#y` such that `x ^ y < k` using the trie?**

**A:**
At each bit position:

* Let `bx` be the bit of `x`, `bk` be the bit of `k`.
* If `bk == 0`, XOR at this bit must be 0, otherwise `(x ^ y)` would exceed `k` here, so I must follow child `bx`.
* If `bk == 1`:

  * Branch with XOR bit 0 (`y` having bit `bx`) makes prefix strictly smaller than `k`, so all numbers in that subtree are valid; I add its count to result.
  * Branch with XOR bit 1 (`y` having bit `1 - bx`) keeps prefix equal to `k`, so I continue traversal from that child.

If a needed child is missing, I simply stop exploring that branch.

---

**Q4: Why do you store a `count` at every trie node?**

**A:**
When `bk == 1` and I go down the “XOR bit 0” branch, the entire subtree under that child is guaranteed to produce XOR `< k`. Storing a `count` at each node lets me add all those numbers in O(1) instead of traversing the subtree.

---

**Q5: What’s the time and space complexity of your optimized solution?**

**A:**
If `B` is the number of bits (here `B ≈ 16`):

* Each insertion and each query takes `O(B)`.
* For `n` numbers, we do both, so time is `O(n * B)` → `O(n log MaxVal)`.
* The trie has at most `O(n * B)` nodes in the worst case, so space is `O(n log MaxVal)`.

Given constraints (`arr[i], k ≤ 5*10^4`), `B` is small and it behaves like `O(n)`.

---

**Q6: Could this be solved with sorting instead of a trie?**

**A:**
Not in a straightforward way. Sorting helps in counting pairs under relations like `<`, `<=`, or difference constraints, but XOR is not monotonic with respect to value. So having `a < b` does not tell us about `a ^ x` vs `b ^ x`. That’s why specialized bit structures like tries (or binary indexed tries) are more suitable.

---

If you rehearse:

> “**Past trie**; for each `x`: `ans += countLess(x, k)`; when `k bit = 1`, **add same-bit branch, follow diff-bit**”

you’ll be able to reconstruct both the explanation and the optimized code confidently in an interview.

---

---

Let’s finish this one nicely.

---

## 5. Real-World Use Cases (easy to relate in interviews)

You’re counting **pairs whose XOR is below a threshold**. XOR + thresholds shows up a lot in systems work:

1. **Similarity on Bitmasks / Feature Flags**

   * Suppose each integer encodes a set of features or permissions as bits.
   * `x ^ y` tells you **which bits differ**.
   * If `x ^ y < k`, the number of high bits / magnitude of difference is small → the two configurations are “similar enough”.
   * Used in **A/B testing configs**, **feature-flag rollouts**, or **permission templates** to quickly count “almost identical” configurations.

2. **Network / Hardware Configuration Compatibility**

   * Device capabilities are often stored as bitmasks.
   * To pair devices, you might require that their XOR (capability differences) is under some bound `k`.
   * Counting such pairs helps estimate **how many device pairs are compatible** in a network or cluster.

3. **Approximate Matching / Hamming Distance in Hash Space**

   * In some approximate search schemes, items are mapped to bit codes (e.g., LSH, binary embeddings).
   * XOR acts like Hamming distance (if you then count bits).
   * A constraint like `x ^ y < k` can approximate “distance under a threshold” in binary embedding space – useful for **near-duplicate detection** or **similar content retrieval**.

These are short, realistic stories that show you understand why XOR + counts matter beyond just DSA.

---

## 6. Full Python Program (optimized Trie)

*With inline complexity comments + timing using `time.perf_counter()`*

```python
import time


class TrieNode:
    def __init__(self):
        # children[0] for bit 0, children[1] for bit 1
        # Access is O(1)
        self.children = [None, None]

        # Number of values that pass through this node (subtree size)
        # Needed to count entire subtrees in O(1)
        self.count = 0


class Solution:
    def __init__(self):
        # Values and k are <= 5*10^4, so 16 bits are enough (2^16 = 65536)
        # We'll use bit positions 15..0
        self.MAX_BIT = 15

    def cntPairs(self, arr, k):
        """
        Count pairs (i < j) such that arr[i] ^ arr[j] < k.

        Approach:
        - Maintain a binary Trie (bitwise tree) of numbers we've already seen.
        - For each value x in arr (left to right):
            1. Query the Trie: how many previous values y satisfy (x ^ y) < k?
            2. Insert x into the Trie.
        - Sum up all such counts.

        Let:
            n = len(arr), B = number of bits (here <= 16)

        Time complexity:
            - For each of n numbers, we do:
                * one query:  O(B)
                * one insert: O(B)
            => O(n * B) ≈ O(n) for given constraints.

        Space complexity:
            - In the worst case, each distinct bit prefix creates a node.
            - At most O(n * B) nodes.
            => O(n * B) ≈ O(n) auxiliary space.
        """

        root = TrieNode()      # O(1) space
        total_pairs = 0        # O(1) space
        trie_has_values = False

        # Process each number in order
        for value in arr:
            if trie_has_values:
                # Query time: O(B)
                total_pairs += self._count_less_than(root, value, k)

            # Insert this value for future queries
            # Insert time: O(B)
            self._insert(root, value)
            trie_has_values = True

        return total_pairs

    # ----------------- Trie helper: insert -----------------
    def _insert(self, root, number):
        """
        Insert 'number' into the binary Trie.

        Time per insert:
            - We walk B bits from MSB to LSB.
            => O(B)

        Space:
            - At most B new nodes created the first time each prefix appears.
            => O(B) additional nodes in worst case for this call.
        """
        node = root
        node.count += 1  # root also counts this number; O(1)

        # Process bits from most significant to least significant
        for bit_pos in range(self.MAX_BIT, -1, -1):
            bit = (number >> bit_pos) & 1  # extract bit: O(1)

            # Create child if missing: O(1)
            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            # Move to child and update its count
            node = node.children[bit]
            node.count += 1  # O(1)

    # ----------------- Trie helper: count values y with (x ^ y) < k -----------------
    def _count_less_than(self, root, x, k):
        """
        Given Trie of previous numbers, count how many y satisfy (x ^ y) < k.

        Bit-by-bit logic:
            Let bx = bit of x, bk = bit of k at current position.
            - If bk == 0:
                * XOR must have 0 at this bit to remain < k
                  => y's bit must equal bx.
                  => We must go to child bx; no counting yet.
            - If bk == 1:
                * XOR can be 0 (strictly smaller at this bit) or 1 (still equal so far).
                * XOR bit 0 branch => y's bit = bx:
                      - prefix gets smaller than k here
                      - all numbers in this subtree are valid
                      - add subtree count
                * XOR bit 1 branch => y's bit = 1 - bx:
                      - prefix equals k here
                      - must continue exploring lower bits on this branch only.

        Time per query:
            - We walk B bits, constant work per bit.
            => O(B)
        """
        node = root
        if node is None:
            return 0

        count_valid = 0  # result accumulator

        # Go from MSB down to LSB
        for bit_pos in range(self.MAX_BIT, -1, -1):
            if node is None:
                # No more numbers in this path
                break

            bx = (x >> bit_pos) & 1  # bit of x: O(1)
            bk = (k >> bit_pos) & 1  # bit of k: O(1)

            if bk == 0:
                # XOR must be 0 here => y's bit must equal x's bit
                node = node.children[bx]
            else:
                # bk == 1

                # 1) XOR bit 0 branch: y's bit = bx
                #    This makes xor_prefix < k_prefix at this bit.
                same_child = node.children[bx]
                if same_child is not None:
                    # We can count entire subtree in O(1)
                    count_valid += same_child.count

                # 2) XOR bit 1 branch: y's bit = 1 - bx
                #    Prefix remains equal to k; continue from that child.
                node = node.children[1 - bx]

        return count_valid


# ----------------- Driver / Main with timing -----------------
def main():
    """
    Main driver to:
        - Read input from user
        - Call cntPairs
        - Print result and elapsed time

    I/O format (simple, interactive style):
        n
        a1 a2 a3 ... an
        k
    """

    print("Enter n (size of array):")
    # Reading n is O(1)
    n = int(input().strip())

    print(f"Enter {n} integers for the array, space-separated:")
    # Reading and splitting is O(n)
    arr = list(map(int, input().split()))
    if len(arr) != n:
        print(f"Warning: expected {n} elements, got {len(arr)}. Using the first {n}.")
        arr = arr[:n]

    print("Enter k:")
    # Reading k is O(1)
    k = int(input().strip())

    # Start timing from just before creating the solver and calling cntPairs
    start_time = time.perf_counter()

    solver = Solution()
    # Core algorithm: O(n * B), approximately linear in n for given constraints
    result = solver.cntPairs(arr, k)

    end_time = time.perf_counter()

    # Output result
    print(f"\nNumber of pairs (i < j) with arr[i] ^ arr[j] < {k}: {result}")

    elapsed = end_time - start_time
    print(f"Total elapsed time (seconds): {elapsed:.6f}")


if __name__ == "__main__":
    main()
```

### Conceptual Example Run

If you run and input:

```text
4
1 2 3 5
5
```

You’d see something like:

```text
Enter n (size of array):
4
Enter 4 integers for the array, space-separated:
1 2 3 5
Enter k:
5

Number of pairs (i < j) with arr[i] ^ arr[j] < 5: 4
Total elapsed time (seconds): 0.0000xx
```

You can reuse this structure for practice; in an interview or online judge you’ll usually just implement the `Solution` class with `cntPairs`, but having this full script helps you test + profile locally.

