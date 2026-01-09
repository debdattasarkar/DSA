# Count Subarray with k odds

**Difficulty:** Medium
**Accuracy:** 59.71%
**Submissions:** 8K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

You are given an array **arr[]** of positive integers and an integer **k**.
You have to **count** the number of subarrays that contain **exactly k odd numbers**.

---

## Examples

### Example 1

**Input:**
`arr[] = [2, 5, 6, 9], k = 2`

**Output:**
`2`

**Explanation:**
There are 2 subarrays with 2 odds:
`[2, 5, 6, 9]` and `[5, 6, 9]`.

---

### Example 2

**Input:**
`arr[] = [2, 2, 5, 6, 9, 2, 11], k = 2`

**Output:**
`8`

**Explanation:**
There are 8 subarrays with 2 odds:
`[2, 2, 5, 6, 9]`, `[2, 5, 6, 9]`, `[5, 6, 9]`, `[2, 2, 5, 6, 9, 2]`,
`[2, 5, 6, 9, 2]`, `[5, 6, 9, 2]`, `[6, 9, 2, 11]` and `[9, 2, 11]`.

---

## Constraint

* 1 ≤ `k` ≤ `arr.size()` ≤ 10<sup>5</sup>
* 1 ≤ `arr[i]` ≤ 10<sup>9</sup>

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* prefix-sum
* Hash
* Algorithms
* sliding-window
* two-pointer-algorithm

---

## Related Articles

* [**Number Subarrays M Odd Numbers**](https://www.geeksforgeeks.org/number-subarrays-m-odd-numbers/)

---

---

## 2) Text explanation (exactly `k` odd numbers)

We only care whether each number is **odd (1)** or **even (0)**.

Let `odd_prefix` = number of odd elements seen so far (prefix odd count).

For any subarray `l..r`:

* odds in subarray = `odd_prefix[r] - odd_prefix[l-1]`

We want:
`odd_prefix[r] - odd_prefix[l-1] = k`
➡️ `odd_prefix[l-1] = odd_prefix[r] - k`

So, for each index `r`, if we know how many previous prefixes had value `(odd_prefix - k)`, we can add them to the answer.

This is **Prefix Sum + Hash Frequency**.

---

## Step-by-step Dry Run (Example 2)

`arr = [2, 2, 5, 6, 9, 2, 11], k = 2`

Maintain:

* `odd_prefix`
* `prefix_frequency` map
* `answer`

Initialize:

* `odd_prefix = 0`
* `prefix_frequency = {0: 1}`  (empty prefix)
* `answer = 0`

Process each element:

| idx | val | odd? | odd_prefix | need = odd_prefix-k | add freq[need] | answer | update freq |
| --- | --- | ---- | ---------- | ------------------- | -------------- | ------ | ----------- |
| 0   | 2   | 0    | 0          | -2                  | 0              | 0      | freq[0]=2   |
| 1   | 2   | 0    | 0          | -2                  | 0              | 0      | freq[0]=3   |
| 2   | 5   | 1    | 1          | -1                  | 0              | 0      | freq[1]=1   |
| 3   | 6   | 0    | 1          | -1                  | 0              | 0      | freq[1]=2   |
| 4   | 9   | 1    | 2          | 0                   | 3              | 3      | freq[2]=1   |
| 5   | 2   | 0    | 2          | 0                   | 3              | 6      | freq[2]=2   |
| 6   | 11  | 1    | 3          | 1                   | 2              | 8      | freq[3]=1   |

✅ Final answer = **8** (matches example)

---

## 3) Python codes (brute + optimized)

### A) Brute force (easy baseline)

Count odds in every subarray and check if it equals k.

**Time:** `O(n^2)`
**Space:** `O(1)`

```python
class Solution:
    def countSubarrays(self, arr, k):
        n = len(arr)
        total_subarrays = 0

        for start in range(n):
            odd_count = 0
            for end in range(start, n):
                if arr[end] % 2 == 1:
                    odd_count += 1

                if odd_count == k:
                    total_subarrays += 1
                elif odd_count > k:
                    break  # extending further only increases odd_count

        return total_subarrays
```

---

### B) Most expected: Prefix odd-count + hashmap frequency

**Time:** `O(n)`
**Space:** `O(n)` (frequency map)

```python
class Solution:
    def countSubarrays(self, arr, k):
        # prefix_frequency[p] = number of times we've seen odd_prefix == p
        prefix_frequency = {0: 1}  # empty prefix has 0 odds
        odd_prefix = 0
        total_subarrays = 0

        for value in arr:
            # Update prefix odd count
            if value % 2 == 1:
                odd_prefix += 1

            # If previous prefix had (odd_prefix - k), subarray between has k odds
            needed_prefix = odd_prefix - k
            total_subarrays += prefix_frequency.get(needed_prefix, 0)

            # Record current prefix
            prefix_frequency[odd_prefix] = prefix_frequency.get(odd_prefix, 0) + 1

        return total_subarrays
```

---

### C) O(1) space alternative: Two pointers using “AtMost” trick

Exactly(k) = AtMost(k) - AtMost(k-1)

**Time:** `O(n)`
**Space:** `O(1)`

```python
class Solution:
    def countSubarrays(self, arr, k):

        # Count subarrays with at most 'limit' odd numbers
        def count_at_most(limit):
            if limit < 0:
                return 0

            left = 0
            odd_count = 0
            total = 0

            for right in range(len(arr)):
                if arr[right] % 2 == 1:
                    odd_count += 1

                # Shrink until window is valid (<= limit odds)
                while odd_count > limit:
                    if arr[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                # All subarrays ending at right starting from left..right are valid
                total += (right - left + 1)

            return total

        return count_at_most(k) - count_at_most(k - 1)
```

---

## 4) Interview: how to remember + Q&A

### 5-line pseudo-code template (prefix method)

```
freq[0]=1; odd=0; ans=0
for x in arr:
    odd += (x is odd)
    ans += freq[odd-k]
    freq[odd]++
return ans
```

### Mnemonics

* **Prefix method:** **“ODD PREFIX → NEED (odd-k) → ADD freq”**
* **Two-pointer method:** **“EXACT = ATMOST(k) − ATMOST(k−1)”**

### 60-second interview script

1. “Convert problem into counting odds in subarrays.”
2. “Use prefix odd counts.”
3. “Subarray has k odds if prefix difference is k.”
4. “For each index, add number of previous prefixes equal to currentOdd-k.”
5. “O(n) time; or O(1) space using atMost difference.”

---

## Expected interviewer questions & answers

**Q1. Why does prefix frequency work?**
A. Because odds in subarray = difference of prefix odd counts; counting prior prefixes gives number of valid starts.

**Q2. Complexity?**
A. Prefix+hash: `O(n)` time, `O(n)` space. Two-pointer atMost: `O(n)` time, `O(1)` space.

**Q3. How would you handle k=0?**
A. Prefix method: need `odd_prefix - 0` → counts all-even subarrays. Two-pointer also works.

**Q4. Why “exactly k = atMost(k) - atMost(k-1)”?**
A. atMost(k) includes all with ≤k odds; subtract those with ≤k-1 leaves exactly k.

**Q5. Any pitfalls?**
A. Must initialize `freq[0]=1` so subarrays starting at index 0 are counted correctly.

If you want, I can next provide **(5) real-world use cases + (6) full timed runnable program + sketch-note** for this problem too.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Quality monitoring in production streams**

   * Count subarrays (time windows) with exactly `k` “bad events” (odd = event flag) to detect patterns like “exactly 2 failures within a burst”.

2. **Fraud / risk detection**

   * Map transactions to `1` if “suspicious” else `0`. Count periods with exactly `k` suspicious events.

3. **User behavior analytics**

   * Map actions to `1` if “high-intent action” else `0`. Count sessions/subsessions with exactly `k` high-intent actions.

4. **Sensor / embedded signals**

   * Mark samples as `1` if they cross a threshold. Count contiguous segments with exactly `k` threshold crossings.

---

## 6) Full Program (timed run + inline complexity + sample I/O)

This runnable program:

* Reads array `arr` and integer `k`
* Computes number of subarrays with **exactly k odd numbers**
* Uses **O(1) extra space** approach: `exactly(k) = atMost(k) - atMost(k-1)`
* Prints input + output + total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: array values space-separated
* Line 2: k

If no stdin, demo uses:

* `arr = [2, 2, 5, 6, 9, 2, 11]`, `k = 2` → output `8`

```python
import sys
import time


class Solution:
    def countSubarrays(self, arr, k):
        """
        Count subarrays with exactly k odd numbers.

        Trick:
        exactly(k) = atMost(k) - atMost(k-1)

        Time: O(n)
        Auxiliary Space: O(1)
        """

        # Count subarrays with at most 'limit' odd numbers
        def count_at_most(limit):
            # Time: O(n), Space: O(1)
            if limit < 0:
                return 0

            left = 0
            odd_count = 0
            total = 0

            for right in range(len(arr)):
                # Add incoming element
                if arr[right] % 2 == 1:
                    odd_count += 1

                # Shrink window until it has <= limit odds
                while odd_count > limit:
                    if arr[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                # All subarrays ending at 'right' starting from left..right are valid
                total += (right - left + 1)

            return total

        # Exactly k = AtMost(k) - AtMost(k-1)
        return count_at_most(k) - count_at_most(k - 1)


def main():
    # Measure full program runtime (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [2, 2, 5, 6, 9, 2, 11]
        k = 2
    else:
        # ---------------- INPUT MODE ----------------
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        arr = list(map(int, lines[0].split()))
        k = int(lines[1])

    # Solve
    # Time: O(n), Aux Space: O(1)
    answer = solver.countSubarrays(arr, k)

    print("Input:")
    print("arr =", arr)
    print("k =", k)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

Input: `arr=[2,2,5,6,9,2,11], k=2`
Output: `8` (+ runtime)

---
