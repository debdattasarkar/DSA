Here is the complete **README conversion** of the problem exactly as shown in the image, without omitting any part.

---

# 📌 Find the closest pair from two arrays

**Difficulty:** Easy
**Accuracy:** 18.01%
**Submissions:** 68K+
**Points:** 2

---

## 📝 Problem Statement

Given two **sorted arrays** `arr1[]` and `arr2[]` of size `n` and `m` and a number `x`, find the pair whose **sum is closest to x** and the pair has an element from each array.

In the case of multiple closest pairs return **any one of them**.

---

### 🔎 Note

In the driver code, the **absolute difference** between the sum of the closest pair and `x` is printed.

---

## 📚 Examples

### Example 1

```id="1x7yq9"
Input:
arr1[] = [1, 4, 5, 7]
arr2[] = [10, 20, 30, 40]
x = 32

Output:
[1, 30]
```

**Explanation:**
The closest pair whose sum is closest to 32 is `[1, 30] = 31`.

---

### Example 2

```id="4b9k2p"
Input:
arr1[] = [1, 4, 5, 7]
arr2[] = [10, 20, 30, 40]
x = 50

Output:
[7, 40]
```

**Explanation:**
The closest pair whose sum is closest to 50 is `[7, 40] = 47`.

---

## 🔒 Constraints

* `1 ≤ arr1.size(), arr2.size() ≤ 10^5`
* `1 ≤ arr1[i], arr2[i] ≤ 10^9`
* `1 ≤ x ≤ 10^9`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(1)`

---

## 🏷 Topic Tags

* Arrays
* Searching
* Data Structures
* Algorithms

---

## 📖 Related Articles

* Given Two Sorted Arrays Number X Find Pair Whose Sum Closest X

---

---

Below is the full answer **based on the `@staticmethod` version (no `self`)**.

---

## 2) Text Explanation (Two Pointers on Sorted Arrays)

We are given two **sorted** arrays `arr1`, `arr2` and a number `x`.
We need a pair `(a from arr1, b from arr2)` such that `a + b` is **closest to x**.
If multiple pairs have same closeness, return **any**.

### Why two pointers works

Because arrays are sorted:

* If we increase `arr1[i]`, the sum increases.
* If we decrease `arr2[j]`, the sum decreases.

So we can start from an extreme pair and move in the right direction:

**Start**

* `i = 0`  → smallest in `arr1`
* `j = m-1` → largest in `arr2`

At each step:

1. Compute `sum = arr1[i] + arr2[j]`
2. Update best pair if `abs(sum - x)` is smaller
3. Move pointer:

   * If `sum > x` → need smaller sum → `j -= 1`
   * Else (`sum < x`) → need larger sum → `i += 1`
   * If `sum == x` → perfect match → return immediately

**Time:** `O(n+m)` because `i` moves at most `n` steps and `j` moves at most `m` steps.
**Space:** `O(1)`.

---

## Step-by-step Dry Run

### Example

`arr1 = [1, 4, 5, 7]`
`arr2 = [10, 20, 30, 40]`
`x = 32`

Initialize:

* `i = 0` (`arr1[i]=1`)
* `j = 3` (`arr2[j]=40`)
* best = `[1, 40]`, bestDiff = |41-32| = 9

Now iterate:

1. `sum = 1 + 40 = 41`, diff=9
   best stays `[1,40]`
   `sum > x` → `j--` → `j=2` (`30`)

2. `sum = 1 + 30 = 31`, diff=1
   best becomes `[1,30]`, bestDiff=1
   `sum < x` → `i++` → `i=1` (`4`)

3. `sum = 4 + 30 = 34`, diff=2
   best still `[1,30]`
   `sum > x` → `j--` → `j=1` (`20`)

4. `sum = 4 + 20 = 24`, diff=8
   best still `[1,30]`
   `sum < x` → `i++` → `i=2` (`5`)

5. `sum = 5 + 20 = 25`, diff=7
   best still `[1,30]`
   `sum < x` → `i++` → `i=3` (`7`)

6. `sum = 7 + 20 = 27`, diff=5
   best still `[1,30]`
   `sum < x` → `i++` → `i=4` stop

✅ Answer = `[1, 30]` (sum=31 is closest to 32)

---

## 3) Python Codes (Brute + Interview-Expected Optimized)

### A) Brute Force (baseline)

**Time:** `O(n*m)`
**Space:** `O(1)`

```python
class Solution:
    @staticmethod
    def findClosestPair(arr1, arr2, x):
        # Brute force: try every pair (a from arr1, b from arr2)
        # Time: O(n*m), Space: O(1)

        best_pair = [arr1[0], arr2[0]]
        best_diff = abs(arr1[0] + arr2[0] - x)

        for value1 in arr1:
            for value2 in arr2:
                current_sum = value1 + value2
                current_diff = abs(current_sum - x)

                if current_diff < best_diff:
                    best_diff = current_diff
                    best_pair = [value1, value2]

        return best_pair
```

---

### B) Optimized (Most Expected): Two Pointers ✅

**Time:** `O(n+m)`
**Space:** `O(1)`

```python
class Solution:
    @staticmethod
    def findClosestPair(arr1, arr2, x):
        # Two pointers because both arrays are sorted
        # Time: O(n + m), Space: O(1)

        left_index = 0                 # start of arr1 (small -> large)
        right_index = len(arr2) - 1    # end of arr2 (large -> small)

        # Initialize best using the first considered pair
        best_pair = [arr1[left_index], arr2[right_index]]
        best_diff = abs(arr1[left_index] + arr2[right_index] - x)

        while left_index < len(arr1) and right_index >= 0:
            current_sum = arr1[left_index] + arr2[right_index]
            current_diff = abs(current_sum - x)

            # Update best pair if we found a closer sum
            if current_diff < best_diff:
                best_diff = current_diff
                best_pair = [arr1[left_index], arr2[right_index]]

            # Perfect match: can't do better than diff = 0
            if current_sum == x:
                return [arr1[left_index], arr2[right_index]]

            # Adjust pointers to move sum toward x
            if current_sum > x:
                right_index -= 1   # decrease sum
            else:
                left_index += 1    # increase sum

        return best_pair
```

---

### C) Alternative (also common): Binary search on arr2 for each arr1 element

**Time:** `O(n log m)`
**Space:** `O(1)`

```python
import bisect

class Solution:
    @staticmethod
    def findClosestPair(arr1, arr2, x):
        # For each arr1[i], search closest (x - arr1[i]) in arr2
        # Time: O(n log m), Space: O(1)

        best_pair = [arr1[0], arr2[0]]
        best_diff = abs(arr1[0] + arr2[0] - x)

        for value1 in arr1:
            target = x - value1
            pos = bisect.bisect_left(arr2, target)

            # Check nearest candidates around pos
            for idx in (pos, pos - 1):
                if 0 <= idx < len(arr2):
                    value2 = arr2[idx]
                    current_diff = abs(value1 + value2 - x)

                    if current_diff < best_diff:
                        best_diff = current_diff
                        best_pair = [value1, value2]

        return best_pair
```

---

## 4) Interview: Quick Recall + Expected Q&A

### 5-line pseudo-code template (memorize)

```text
i = 0, j = m-1
bestDiff = INF, bestPair = []
while i<n and j>=0:
  update best using abs(arr1[i] + arr2[j] - x)
  if sum > x: j-- else if sum < x: i++ else return pair
return bestPair
```

### Mnemonic

**“Small + Big → Adjust”**

* Start with **smallest** from arr1 and **biggest** from arr2
* If sum too big → move the **big** pointer left
* If sum too small → move the **small** pointer right

---

### Common Interview Questions & Answers

**Q1. Why does two-pointer guarantee we don’t miss the best pair?**
A1. Because moving `i` only increases sum, moving `j` only decreases sum. Each step moves the sum toward `x` in a monotonic way while exploring all relevant frontier pairs.

**Q2. Complexity?**
A2. `O(n+m)` time, `O(1)` extra space.

**Q3. What if multiple pairs have same closest difference?**
A3. Problem says return any. If needed, we can tie-break (e.g., smallest first element, lexicographically smallest pair).

**Q4. What if arrays weren’t sorted?**
A4. We’d sort them first (`O(n log n + m log m)`) then apply two pointers.

**Q5. Any edge cases?**
A5. One array length 1, exact match exists, very large values, negative values (still works if arrays are sorted).

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **E-commerce pricing / budget matching**

* You have two sorted lists: **item prices** and **coupon/discount values**. Pick one from each so that `price + discount` is closest to a target budget.

2. **Two-system latency alignment**

* Two sorted arrays of latencies from two services. Find a pair (one from each) whose combined latency is closest to an SLA threshold.

3. **Portfolio hedging / risk balancing**

* Two sorted sets of exposures (e.g., long vs hedge instruments). Pick one from each so that combined exposure is closest to a target.

4. **Resource allocation**

* Two sorted lists of resource sizes (CPU blocks and RAM blocks). Choose one of each to get total closest to required capacity.

---

## 6) Full Program (timed end-to-end, staticmethod, with sample I/O)

### ✅ Input Format (for this program)

```
t
n m x
arr1 elements...
arr2 elements...
(repeat for t test cases)
```

### ✅ Sample Input

```
2
4 4 32
1 4 5 7
10 20 30 40
4 4 50
1 4 5 7
10 20 30 40
```

### ✅ Sample Output

```
1 30
7 40
Total runtime (seconds): 0.0000xxxx
```

---

```python
import time

class Solution:
    @staticmethod
    def findClosestPair(arr1, arr2, x):
        """
        Find a pair (one from arr1, one from arr2) such that their sum is closest to x.
        Arrays are sorted.

        Time Complexity:
          - Two pointer scan: O(n + m)

        Auxiliary Space:
          - O(1)
        """

        # Step 0: Initialize pointers
        # Time: O(1), Space: O(1)
        left_index = 0
        right_index = len(arr2) - 1

        # Step 1: Initialize best pair using current pointers
        # Time: O(1), Space: O(1)
        best_pair = [arr1[left_index], arr2[right_index]]
        best_diff = abs(arr1[left_index] + arr2[right_index] - x)

        # Step 2: Move pointers until one runs out
        # Time: O(n + m) (each pointer moves at most its array length)
        while left_index < len(arr1) and right_index >= 0:
            current_sum = arr1[left_index] + arr2[right_index]
            current_diff = abs(current_sum - x)

            # Update answer if current pair is closer
            # Time: O(1)
            if current_diff < best_diff:
                best_diff = current_diff
                best_pair = [arr1[left_index], arr2[right_index]]

            # Perfect match => closest possible
            if current_sum == x:
                return [arr1[left_index], arr2[right_index]]

            # Adjust pointers to move sum toward x
            # Time: O(1)
            if current_sum > x:
                right_index -= 1   # decrease sum
            else:
                left_index += 1    # increase sum

        return best_pair


def main():
    # Measure full program runtime (includes I/O + computation)
    program_start = time.perf_counter()  # Time: O(1)

    t = int(input().strip())  # Time: O(1)

    # Total time across all test cases: Σ O(n + m)
    for _ in range(t):
        # Read n, m, x
        # Time: O(1)
        n, m, x = map(int, input().split())

        # Read arrays
        # Time: O(n + m), Space: O(n + m) for storing input
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        # Compute closest pair
        # Time: O(n + m), Space: O(1) extra
        result = Solution.findClosestPair(arr1, arr2, x)

        # Print the pair (driver might compute abs diff externally)
        print(result[0], result[1])

    program_end = time.perf_counter()
    print(f"Total runtime (seconds): {program_end - program_start:.8f}")


if __name__ == "__main__":
    main()
```
