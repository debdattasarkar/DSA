# Remove K Digits

**Difficulty:** Medium
**Accuracy:** 26.8%
**Submissions:** 86K+
**Points:** 4

---

## Problem Statement

Given a **non-negative integer `s` represented as a string** and an integer **`k`**, remove **exactly `k` digits** from the string such that the resulting number is the **smallest possible**, while **maintaining the relative order** of the remaining digits.

---

### Important Notes

* The resulting number **must not contain leading zeros**.
* If the resulting number becomes an **empty string** after removing `k` digits, return **`"0"`**.

---

## Examples

### Example 1

**Input:**

```
s = "4325043", k = 3
```

**Output:**

```
2043
```

**Explanation:**
Remove the three digits **4, 3, and 5** to form the new number `"2043"`, which is the smallest among all possible removals.

---

### Example 2

**Input:**

```
s = "765028321", k = 5
```

**Output:**

```
221
```

**Explanation:**
Remove the five digits **7, 6, 5, 8, and 3** to form the new number `"0221"`.
Since we are **not supposed to keep leading zeros**, the final answer is `"221"`.

---

## Constraints

* `1 ≤ k ≤ |s| ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n + k)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Microsoft

---

## Topic Tags

* Stack
* Data Structures
* Greedy
* Deque

---

## Related Articles

* [**Build Lowest Number By Removing N Digits From A Given Number**](https://www.geeksforgeeks.org/build-lowest-number-by-removing-n-digits-from-a-given-number/)

---

---

## 2) Text explanation (core idea)

We must remove exactly `k` digits from string `s` to make the **smallest possible number**, while keeping the **relative order** of remaining digits.

### Greedy insight

To make a number small, we want the leftmost digits to be as small as possible.

So while scanning digits left → right:

* If the current digit is **smaller than the last chosen digit**, it’s beneficial to remove that larger last digit (if we still can remove digits).
* This is exactly what a **monotonic increasing stack** does.

### High-level steps

1. Use a stack (list) to build the smallest number.
2. For each digit `ch` in `s`:

   * While `k > 0` and stack not empty and `stack[-1] > ch`:

     * pop stack (remove a bigger digit earlier)
     * decrement `k`
   * push `ch`
3. If `k` still > 0 after processing all digits, remove from the end (largest suffix).
4. Remove leading zeros.
5. If empty → return `"0"`.

**Why it works:**
Any time we see a smaller digit, removing a larger digit before it makes the number smaller at the earliest position (most impactful).

---

## Step-by-step dry run

### Example 1

`s = "4325043", k = 3`

Stack shown as digits:

* Start: `stack = []`, k=3

1. ch='4'
   stack empty → push → `[4]`

2. ch='3'
   stack[-1]='4' > '3' and k>0 → pop '4', k=2
   push '3' → `[3]`

3. ch='2'
   '3' > '2' and k>0 → pop '3', k=1
   push '2' → `[2]`

4. ch='5'
   '2' > '5'? no → push → `[2,5]`

5. ch='0'
   '5' > '0' and k>0 → pop '5', k=0
   push '0' → `[2,0]`

6. ch='4'
   k=0 → no pops → push → `[2,0,4]`

7. ch='3'
   push → `[2,0,4,3]`

Now k=0, build number: `"2043"`
Leading zeros? none → answer `"2043"`

---

### Example 2

`s="765028321", k=5`

* stack=[], k=5

Read digits:

* '7' push → [7]
* '6' pop 7 (k=4), push 6 → [6]
* '5' pop 6 (k=3), push 5 → [5]
* '0' pop 5 (k=2), push 0 → [0]
* '2' push → [0,2]
* '8' push → [0,2,8]
* '3' pop 8 (k=1), push 3 → [0,2,3]
* '2' pop 3 (k=0), push 2 → [0,2,2]
* '1' push → [0,2,2,1]

Result string: `"0221"` → strip leading zeros → `"221"`

---

## 3) Python codes (brute + interview-expected optimized)

### A) Brute force / easy (not for constraints, but conceptually simplest)

Remove one digit at a time by trying all removals (very slow).
This is **O(k·n²)** if done naively—won’t pass for `10^6`, but okay to mention as baseline.

```python
class Solution:
    def removeKdig(self, s, k):
        # Brute idea: remove one digit at a time (choose best removal each step)
        # Not suitable for large constraints.
        
        digits = list(s)
        
        while k > 0 and digits:
            # Find first position i where digits[i] > digits[i+1]
            # Removing digits[i] reduces number earliest.
            remove_index = len(digits) - 1  # default: remove last digit
            for i in range(len(digits) - 1):
                if digits[i] > digits[i + 1]:
                    remove_index = i
                    break
            
            digits.pop(remove_index)
            k -= 1
        
        # Remove leading zeros
        result = "".join(digits).lstrip('0')
        return result if result else "0"
```

**Note:** This “greedy remove-one-step” is still greedy but implemented without stack; it’s simpler to understand but not optimal.

---

### B) Optimized (most expected): Monotonic increasing stack, O(n)

This is the standard interview solution.

```python
class Solution:
    def removeKdig(self, s, k):
        # Greedy + Monotonic stack
        # Time:  O(n)  (each digit pushed/popped at most once)
        # Space: O(n)  (stack)

        stack = []  # will store digits in increasing order as much as possible

        for ch in s:
            # While we can remove digits and last digit is bigger than current,
            # remove it to make number smaller earlier.
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If still need to remove digits, remove from end (largest suffix)
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Build string and remove leading zeros
        result = "".join(stack).lstrip("0")

        # If empty, return "0"
        return result if result else "0"
```

---

### C) Optimized variant (same logic, avoids second while by slicing)

Cleaner in interviews.

```python
class Solution:
    def removeKdig(self, s, k):
        # Time: O(n)
        # Space: O(n)

        stack = []

        for ch in s:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If k remains, just trim from the end
        if k > 0:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")
        return result if result else "0"
```

---

## 4) Interview recall + expected Q&A

### Quick memory trick (what to say)

**“Make the number increasing from left: pop bigger digits when a smaller digit arrives.”**

Mnemonic:

> **“Pop bigger-left, push current, trim end, strip zeros.”**

Or short:

> **“Monotonic increasing stack for smallest number.”**

---

## 60-second interview explanation script

1. “To minimize the number, the earliest digits matter most.”
2. “When a smaller digit appears, I should delete any bigger digit just before it (if removals left).”
3. “So I use a stack and keep it increasing.”
4. “For each digit: while k>0 and top>digit → pop, k--.”
5. “Push digit.”
6. “If k remains, remove from end.”
7. “Strip leading zeros; if empty, return 0.”

---

## Expected interviewer questions & answers

### Q1. Why greedy works?

**A:** If `stack[-1] > current_digit`, removing `stack[-1]` makes the number smaller at the earliest differing position, which is always beneficial for minimization.

### Q2. Why stack?

**A:** It efficiently removes previous digits when a smaller digit arrives; each digit is pushed and popped once → linear time.

### Q3. Why remove remaining k from the end?

**A:** After scanning, stack is as increasing as possible; the largest digits are at the end, so removing from end minimizes the number.

### Q4. What about leading zeros?

**A:** After removals, the smallest number might start with zeros; we strip them because output must not contain leading zeros. If nothing remains → `"0"`.

### Q5. Complexity?

**A:** `O(n)` time because each digit is pushed/popped at most once. Space `O(n)` for stack.

### Q6. Edge cases?

**A:**

* `k == len(s)` → empty → `"0"`
* already increasing string `"12345"` → remove last k digits
* all zeros / leading zeros after removals → strip to `"0"` if empty

---

---

## 5) Real-world use cases (few, very relatable)

1. **FinTech / Billing: Minimizing an ID or amount after removing invalid digits**
   Suppose a payment reference or invoice number is generated as a string, and you must drop exactly `k` “noisy/invalid” digits (while keeping order) to get the smallest canonical identifier for dedup / matching.

2. **Data Cleaning / Compression: Keeping the smallest representation**
   When storing large numeric strings (logs, telemetry counters), you may remove `k` digits (lossy compression) to retain the smallest possible number as a conservative estimate while preserving sequence order.

3. **Product / Ranking: Removing k characters to get minimal lexicographic numeric key**
   Building a minimal “key” from a numeric string while preserving order (like forming smallest sortable key) is the same pattern used in generating normalized keys for sorting/indexing.

---

## 6) Full Python program (with input/output + runtime timing)

* Works for **single test**:

  * `s k` on one line (or on separate lines)
* Also supports **T testcases**:

  * `T`
  * then `s k` per test

Prints answers (one per line).
Prints runtime to **stderr** so normal output remains clean.

```python
import sys
import time

class Solution:
    def removeKdig(self, s, k):
        """
        Greedy + Monotonic Increasing Stack

        Overall Time:  O(n)   (each digit pushed/popped at most once)
        Overall Space: O(n)   (stack)
        """

        # Step 1: Build smallest number using a stack
        # Time:  O(n)
        # Space: O(n)
        stack = []

        for ch in s:
            # While we can remove digits and top is bigger than current digit,
            # pop it to make number smaller earlier.
            # Each digit can be popped once -> total pops across loop is O(n)
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # Step 2: If we still need to remove digits, remove from the end
        # Time:  O(k) (but overall still O(n))
        # Space: O(1) extra
        if k > 0:
            stack = stack[:-k]

        # Step 3: Remove leading zeros
        # Time:  O(n) (string join + lstrip)
        # Space: O(n) for final string
        result = "".join(stack).lstrip("0")

        # Step 4: If empty, return "0"
        # Time:  O(1)
        # Space: O(1)
        return result if result else "0"


def parse_input(tokens):
    """
    Supports:
    1) Single test:
       s k
    2) Multiple tests:
       T
       s k
       s k
       ...
    Returns list of (s, k)
    """
    if not tokens:
        return []

    # Try to parse as T testcases
    # If parsing fails, fallback to single testcase.
    idx = 0
    tests = []

    # If only 2 tokens, it's surely single test
    if len(tokens) == 2:
        return [(tokens[0], int(tokens[1]))]

    # Attempt T format
    try:
        t = int(tokens[0])
        idx = 1
        for _ in range(t):
            s = tokens[idx]
            k = int(tokens[idx + 1])
            idx += 2
            tests.append((s, k))

        # If consumed all tokens perfectly, it's valid T-format
        if idx == len(tokens):
            return tests
    except:
        pass

    # Fallback: single test (first two tokens)
    return [(tokens[0], int(tokens[1]))]


def main():
    # -------- Input reading --------
    data = sys.stdin.buffer.read().split()
    tokens = [x.decode() for x in data]

    # If no input, show a demo run (helpful locally)
    if not tokens:
        demo_s = "4325043"
        demo_k = 3

        print("Demo Input:")
        print(demo_s, demo_k)

        start = time.perf_counter()
        ans = Solution().removeKdig(demo_s, demo_k)
        end = time.perf_counter()

        print("Demo Output:")
        print(ans)
        sys.stderr.write(f"[Runtime] {end - start:.6f} seconds\n")
        return

    tests = parse_input(tokens)
    solver = Solution()

    # -------- Time the full solve (excluding parsing is optional; here includes solve only) --------
    start_time = time.perf_counter()

    outputs = []
    for s, k in tests:
        outputs.append(solver.removeKdig(s, k))

    end_time = time.perf_counter()

    # -------- Output --------
    print("\n".join(outputs))

    # Print runtime to stderr (does not affect judged output)
    sys.stderr.write(f"[Runtime] {end_time - start_time:.6f} seconds\n")


if __name__ == "__main__":
    main()


"""
========================
Sample Input (single test)
========================
4325043 3

Output:
2043

========================
Sample Input (multiple tests)
========================
2
4325043 3
765028321 5

Output:
2043
221
"""
```
