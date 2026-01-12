# Bus Ticket Change

**Difficulty:** Easy
**Accuracy:** 52.02%
**Submissions:** 49K+
**Points:** 2
**Average Time:** 30m

---

## Problem Statement

You are given an array **arr[]** representing passengers in a queue. Each bus ticket costs **5 coins**, and `arr[i]` denotes the note a passenger uses to pay (which can be **5, 10, or 20**).

You must serve the passengers in the given order and always provide the correct change so that each passenger effectively pays exactly **5 coins**.

Your task is to determine whether it is possible to serve **all passengers** in the queue without ever running out of change.

---

## Examples

### Example 1

**Input:**
`arr[] = [5, 5, 5, 10, 20]`

**Output:**
`true`

**Explanation:**
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change we return true.

---

### Example 2

**Input:**
`arr[] = [5, 5, 10, 10, 20]`

**Output:**
`false`

**Explanation:**
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

---

## Constraints

* 1 ≤ `arr.size()` ≤ 10<sup>5</sup>
* `arr[i]` contains only `{5, 10, 20}`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Arrays
* Greedy
* Data Structures
* Algorithms

---

## Related Articles

* [**Lemonade Stand Change Challenge**](https://www.geeksforgeeks.org/lemonade-stand-change-challenge/)


---

---

## 2) Text explanation (Greedy idea)

Ticket cost = **5**.

People pay with `{5, 10, 20}`:

* Pay **5** → no change needed → we gain one `5`
* Pay **10** → need `5` change → must have at least one `5`
* Pay **20** → need `15` change → either:

  * give `10 + 5` (best, saves 5s), or
  * give `5 + 5 + 5` (only if no 10 available)

So we only need to track how many **5 coins** and **10 coins** we currently have.

**Greedy rule for 20:**
Always prefer `10+5` over `5+5+5` because 5-coins are more flexible for future 10 payments.

---

## Step-by-step Dry Run

### Example 1

`arr = [5, 5, 5, 10, 20]`

Maintain:

* `five_count = 0`
* `ten_count = 0`

1. pay 5 → `five=1`, `ten=0`
2. pay 5 → `five=2`, `ten=0`
3. pay 5 → `five=3`, `ten=0`
4. pay 10 → need 5 → `five=2`, `ten=1`
5. pay 20 → need 15:

   * have 10 and 5 → give `10+5` → `five=1`, `ten=0`
     ✅ Served all → **true**

---

### Example 2

`arr = [5, 5, 10, 10, 20]`

Start `five=0`, `ten=0`

1. 5 → `five=1`
2. 5 → `five=2`
3. 10 → give 5 → `five=1`, `ten=1`
4. 10 → give 5 → `five=0`, `ten=2`
5. 20 → need 15:

   * `10+5` not possible (no 5)
   * `5+5+5` not possible
     ❌ fail → **false**

---

## 3) Python solutions (easy + interview-expected)

### A) Brute-ish simulation with a “wallet” (still O(n), but less clean)

Stores counts in a dict. Same logic, just more verbose.

```python
class Solution:
    def canServe(self, arr):
        # wallet[note] = how many of that note we have
        wallet = {5: 0, 10: 0, 20: 0}

        for paid in arr:
            wallet[paid] += 1

            if paid == 10:
                # need 5 change
                if wallet[5] == 0:
                    return False
                wallet[5] -= 1

            elif paid == 20:
                # need 15 change, prefer (10+5)
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False

        return True
```

---

### B) Most expected (Greedy with two counters) ✅

**Time:** `O(n)`
**Space:** `O(1)`

```python
class Solution:
    def canServe(self, arr):
        five_count = 0   # number of 5 coins we have
        ten_count = 0    # number of 10 coins we have

        for paid in arr:
            if paid == 5:
                # No change needed, just collect the 5
                five_count += 1

            elif paid == 10:
                # Need to give back 5
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1

            else:  # paid == 20
                # Need to give back 15
                # Greedy: prefer giving 10+5 if possible
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False

        return True
```

---

## 4) Interview: how to remember + expected Q&A

### 5-line pseudo-code template (memorize)

```
five=0, ten=0
for x in arr:
  if x==5: five++
  elif x==10: if five==0: fail; else five--, ten++
  else: if ten>0 and five>0: ten--, five-- else if five>=3: five-=3 else fail
return true
```

### Mnemonic

**“Take 5, Give 5, For 20: 10+5 else 5+5+5”**
(Or simply: **“20 wants 15 → prefer 10+5”**)

---

## Expected interviewer questions (with answers)

**Q1. Why greedy “10+5” first for 20?**
A. Because 5 coins are needed to serve 10 payments. Saving 5s increases future feasibility.

**Q2. What variables do you need? Why not store all money?**
A. Only counts of 5 and 10 matter. 20 is never used as change.

**Q3. Complexity?**
A. O(n) time, O(1) extra space.

**Q4. What fails earliest?**
A. A 10 with no 5 available, or a 20 when you can’t make 15 using (10+5) or (5+5+5).

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Cashier / POS systems (making change in order)**

   * Real shops must give correct change sequentially as customers arrive. This models whether a counter can keep operating without running out of smaller notes.

2. **Ticketing kiosks / vending machines**

   * Machines accept limited denominations and must return exact change. This checks feasibility of serving a queue without restocking.

3. **Resource allocation with limited “small units”**

   * Think of `5` as a scarce resource unit; larger payments require breaking into smaller units. Similar to allocating limited credits/tokens in streaming systems.

4. **Queue-based service guarantees**

   * In any sequential service system, early decisions affect future ability to serve (greedy policy to preserve flexibility).

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This program:

* Reads `arr` from input
* Runs the greedy solution (`O(n)` time, `O(1)` space)
* Prints input and output (`True/False`)
* Prints total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: space-separated notes (only 5/10/20)

  * Example: `5 5 5 10 20`

If no stdin, demo runs Example 1.

```python
import sys
import time


class Solution:
    def canServe(self, arr):
        """
        Greedy approach.
        Time: O(n)  (single pass over customers)
        Aux Space: O(1)  (only two counters)
        """
        five_count = 0  # count of 5 coins available for change
        ten_count = 0   # count of 10 coins available for change

        # Process each passenger once -> O(n)
        for paid in arr:
            if paid == 5:
                # No change needed
                five_count += 1  # O(1)

            elif paid == 10:
                # Need to give back 5
                if five_count == 0:
                    return False
                five_count -= 1  # give one 5 as change
                ten_count += 1   # collect a 10

            else:  # paid == 20
                # Need to give back 15
                # Best: 10 + 5 (preserves 5 coins)
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                # Else: 5 + 5 + 5
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False

        return True


def main():
    # Total runtime timing: parse + compute + print
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [5, 5, 5, 10, 20]
    else:
        # ---------------- INPUT MODE ----------------
        # Time: O(n) to parse tokens, Space: O(n) for arr storage
        arr = list(map(int, data.split()))

    # Solve
    # Time: O(n), Space: O(1) extra
    answer = solver.canServe(arr)

    print("Input:")
    print("arr =", arr)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

Input: `[5, 5, 5, 10, 20]`
Output: `True` (+ runtime)

---
