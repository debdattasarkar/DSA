
---

# 📌 Missing Element in Range

**Difficulty:** Medium
**Accuracy:** 50.89%
**Submissions:** 2K+
**Points:** 4
**Average Time:** 20m

---

## 📝 Problem Statement

Given an array `arr[]` of distinct integers and a range `[low, high]`, find all the numbers within the range that are **not present** in the array. Return the missing numbers in **sorted order**.

---

## 📚 Examples

### Example 1

```
Input:  arr[] = [10, 12, 11, 15], low = 10, high = 15
Output: [13, 14]
```

**Explanation:**
Numbers 13 and 14 lie in the range `[10, 15]` but are not present in the array.

---

### Example 2

```
Input:  arr[] = [1, 4, 11, 51, 15], low = 50, high = 55
Output: [52, 53, 54, 55]
```

**Explanation:**
Numbers 52, 53, 54 and 55 lie in the range `[50, 55]` but are not present in the array.

---

## 🔒 Constraints

* `1 ≤ arr.size(), low, high ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n + (high - low + 1))`
* **Auxiliary Space:** `O(n)`

---

## 📖 Related Articles

* Find Missing Elements Of A Range

---

---

## 2) Explanation (Logic)

We are given:

* `arr[]` (distinct integers)
* a range `[low, high]`

We must return **all numbers in [low, high] that are NOT in arr**, in **sorted order**.

### Main idea (most expected)

1. Put all array elements into a **set** for **O(1)** average lookup.
2. Loop from `low` to `high`:

   * if the number is not in the set → it’s missing → add to answer.

This directly matches the expected complexity:
`O(n + (high-low+1))`

---

## Step-by-step Dry Run

### Example 1

`arr = [10, 12, 11, 15], low = 10, high = 15`

1. Make set: `{10, 11, 12, 15}`
2. Check each number from 10 to 15:

   * 10 → present ✅
   * 11 → present ✅
   * 12 → present ✅
   * 13 → missing ❌ → add `13`
   * 14 → missing ❌ → add `14`
   * 15 → present ✅
3. Answer = `[13, 14]`

---

### Example 2

`arr = [1, 4, 11, 51, 15], low = 50, high = 55`

Set = `{1, 4, 11, 15, 51}`
Check 50..55:

* 50 missing → add
* 51 present
* 52 missing → add
* 53 missing → add
* 54 missing → add
* 55 missing → add
  Answer = `[50, 52, 53, 54, 55]`

(But note: screenshot output starts from 52 because `50` is in range and missing? Actually 50 is not in arr, so it *should* be missing. The screenshot’s example says output `[52, 53, 54, 55]` with low=50, so it implies 50 and 51? Wait: 51 is present, but 50 is not—yet they didn’t include 50. This is likely a screenshot typo OR they intended low=51. I’ll still follow the written statement: **include all missing in [low, high]**.)

---

## 3) Python Solutions (Brute + Interview-Expected Optimized)

### A) Brute (no extra DS) — simplest but slow

**Time:** `O((high-low+1) * n)`
**Space:** `O(1)`

```python
class Solution:
    def missingRange(self, arr, low, high):
        # Brute force: for each number in range, linearly scan arr
        # Time: O((high-low+1) * n)
        # Space: O(1)

        missing_numbers = []

        for value in range(low, high + 1):
            found = False
            for element in arr:
                if element == value:
                    found = True
                    break
            if not found:
                missing_numbers.append(value)

        return missing_numbers
```

---

### B) Optimized (Most Expected): Set lookup ✅

**Time:** `O(n + (high-low+1))`
**Space:** `O(n)`

```python
class Solution:
    def missingRange(self, arr, low, high):
        # Build a hash set for O(1) average membership checks
        # Time: O(n)
        # Space: O(n)
        present_values = set(arr)

        # Scan the full range and collect missing values
        # Time: O(high-low+1)
        # Space: O(k) for output list
        missing_numbers = []
        for value in range(low, high + 1):
            if value not in present_values:
                missing_numbers.append(value)

        return missing_numbers
```

---

### C) Alternative Optimized: Boolean presence array (fast if bounds known)

Since constraints say values are up to `1e5`, we can mark presence in an array.
**Time:** `O(n + (high-low+1))`
**Space:** `O(1e5)` (bounded)

```python
class Solution:
    def missingRange(self, arr, low, high):
        # Presence array approach (good when max value is bounded)
        # Time: O(n + (high-low+1))
        # Space: O(MAX_VAL)

        MAX_VAL = 100000  # from constraints
        is_present = [False] * (MAX_VAL + 1)

        # Mark elements that appear in arr
        for x in arr:
            if 0 <= x <= MAX_VAL:
                is_present[x] = True

        # Collect missing numbers in the required range
        missing_numbers = []
        for value in range(low, high + 1):
            if value <= MAX_VAL and not is_present[value]:
                missing_numbers.append(value)

        return missing_numbers
```

---

## 4) Interview Quick Recall + Expected Q&A

### 5-line pseudo-code skeleton (memorize)

```text
put all arr elements into a set
ans = []
for x from low to high:
    if x not in set: ans.append(x)
return ans
```

### Mnemonic

**“Set + Sweep”**

* **Set** for fast presence check
* **Sweep** through the range and collect missing

---

## Common Interview Questions & Answers

**Q1. Why use a set?**
A1. Membership checks become O(1) average, so scanning the range becomes efficient.

**Q2. What’s the complexity?**
A2. Building the set is `O(n)`. Checking numbers from `low..high` costs `O(high-low+1)`. Total: `O(n + (high-low+1))`.

**Q3. Do we need sorting?**
A3. No, because we generate numbers in increasing order from `low` to `high`, so output is automatically sorted.

**Q4. What if the range is huge (e.g., high-low is big)?**
A4. Then output itself can be huge, so time must be at least proportional to `(high-low+1)` if we must list all missing numbers. If interviewer only wanted count, we could optimize differently.

**Q5. Why is `arr` distinct important?**
A5. It avoids duplicates but doesn’t change correctness for set-based solution; duplicates would be naturally handled by the set anyway.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Inventory / SKU audit in a given ID range**
   You expect product IDs from `low..high`, but some are missing in the database → find missing IDs to investigate.

2. **Attendance / roll-number gap detection**
   Student roll numbers should be continuous in a range; missing roll numbers indicate absent/unregistered entries.

3. **Log / packet sequence validation**
   Events/packets are expected to have sequence numbers in `[low, high]`; missing numbers indicate **dropped logs/packets**.

4. **Ticket / invoice number reconciliation**
   Invoices should be sequential in a range; missing ones may indicate cancellation, fraud checks, or system issues.

---

## 6) Full Program (timed end-to-end + sample input/output)

* Uses the **interview-expected** solution: **Set + Sweep**
* Prints missing numbers in sorted order (as produced by the sweep)
* Prints total runtime using `time.perf_counter()`

### ✅ Input Format (for this program)

```
t
n low high
a1 a2 a3 ... an
(repeat for t test cases)
```

### ✅ Sample Input

```
2
4 10 15
10 12 11 15
5 50 55
1 4 11 51 15
```

### ✅ Sample Output

```
13 14
50 52 53 54 55
Total runtime (seconds): 0.0000xxxx
```

---

```python
import time

class Solution:
    def missingRange(self, arr, low, high):
        """
        Return all missing numbers in [low, high] not present in arr (distinct ints).
        Output must be sorted -> scanning low..high naturally produces sorted output.

        Time Complexity:
          - Build set from arr: O(n)
          - Scan range [low..high]: O(high - low + 1)
          => Total: O(n + (high - low + 1))

        Auxiliary Space:
          - Set storage: O(n)
          - Output list: O(k) where k = number of missing elements
        """

        # Step 1: Put all array elements into a set for fast lookup
        # Time: O(n), Space: O(n)
        present_values = set(arr)

        # Step 2: Sweep through the range and collect missing numbers
        # Time: O(high-low+1), Space: O(k) for output
        missing_numbers = []
        for value in range(low, high + 1):
            if value not in present_values:
                missing_numbers.append(value)

        return missing_numbers


def main():
    # Measure full program runtime (I/O + computation)
    program_start = time.perf_counter()  # Time: O(1), Space: O(1)

    # Read test cases
    t = int(input().strip())  # Time: O(1)

    solver = Solution()

    # Process each test case
    # Total time across tests: Σ (O(n + range))
    for _ in range(t):
        # Read n, low, high
        # Time: O(1)
        n, low, high = map(int, input().split())

        # Read array of size n
        # Time: O(n), Space: O(n)
        arr = list(map(int, input().split()))

        # Compute missing values
        # Time: O(n + (high-low+1))
        missing = solver.missingRange(arr, low, high)

        # Print result
        # Time: O(k) to print k missing numbers
        if missing:
            print(*missing)
        else:
            print()  # print empty line if nothing missing

    program_end = time.perf_counter()
    print(f"Total runtime (seconds): {program_end - program_start:.8f}")


if __name__ == "__main__":
    main()
```
