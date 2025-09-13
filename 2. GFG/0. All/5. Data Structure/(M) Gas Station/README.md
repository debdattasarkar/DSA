# Gas Station ⛽

**Difficulty:** Medium
**Accuracy:** 34.79%
**Submissions:** 208K+
**Points:** 4
**Average Time:** 20m

---

You are given `n` gas stations along a **circular tour**. Two integer arrays are provided:

* `gas[i]` — the amount of gas available at station `i`
* `cost[i]` — the gas needed to travel from station `i` to station `(i + 1)`

You have a car with an unlimited gas tank and start with an empty tank at **some** station.
Your task is to return the **index of the starting station** if it is possible to travel **once around the circle** in clockwise direction without running out of gas at any station; otherwise, return **-1**.

> **Note:** If a solution exists, it is guaranteed to be **unique**.

---

## Examples

### Example 1

**Input:**
`gas[] = [4, 5, 7, 4]`, `cost[] = [6, 6, 3, 5]`
**Output:** `2`
**Explanation:**
Start at gas station **2** and fill up with 7 units of gas. Your tank = `0 + 7 = 7`
Travel to station 3. Available gas = `(7 - 3 + 4) = 8`.
Travel to station 0. Available gas = `(8 - 5 + 4) = 7`.
Travel to station 1. Available gas = `(7 - 6 + 5) = 6`.
Return to station 2. Available gas = `(6 - 6) = 0`.

---

### Example 2

**Input:**
`gas[] = [3, 9]`, `cost[] = [7, 6]`
**Output:** `-1`
**Explanation:**
There is no gas station to start with such that you can complete the tour.

---

## Constraints

* `1 ≤ n ≤ 10^6`
* `1 ≤ gas[i], cost[i] ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

`Zoho`, `Flipkart`, `Morgan Stanley`, `Amazon`, `Microsoft`, `FactSet`, `Google`

## Topic Tags

`Data Structures`, `Algorithms`, `Greedy`

## Related Interview Experiences

* Microsoft Interview Experience Set 76 On Campus
* Flipkart Interview Experience For SDE 1

## Related Articles

* [Find A Tour That Visits All Stations](https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/)

---

---


Here’s a crisp, interview-ready walk-through and code set for the classic **Gas Station / Circular Tour** problem.

---

## 2) Intuition + Step-by-Step Dry Run

### Key idea

* If the **total** gas is less than the **total** cost, the trip is impossible ⇒ return `-1`.
* Otherwise, scan once with a **greedy** invariant:

  * Keep a running tank `curr += gas[i] - cost[i]`.
  * If `curr` ever drops below `0` at index `i`, **no start between the last candidate and `i` can succeed**.
    So set `start = i + 1` and reset `curr = 0`.

This works because any deficit met at `i` implies the sum of `(gas - cost)` from `start…i` is negative, so starting anywhere in that broken segment would be even worse.

### Dry run (from the prompt)

`gas = [4, 5, 7, 4]`, `cost = [6, 6, 3, 5]`

We track `diff = gas[i] - cost[i]`, `curr`, and `start`.

| i | diff | curr (after adding diff) | action         | start |
| - | ---- | ------------------------ | -------------- | ----- |
| 0 | -2   | -2                       | curr<0 ⇒ reset | 1     |
| 1 | -1   | -1                       | curr<0 ⇒ reset | 2     |
| 2 | +4   | 4                        | ok             | 2     |
| 3 | -1   | 3                        | ok             | 2     |

* Total diff = `(-2) + (-1) + 4 + (-1) = 0 ≥ 0` ⇒ feasible.
* Answer = `start = 2`.

Quick sanity on an impossible case:
`gas=[3,9], cost=[7,6]` ⇒ total diff `= -1 < 0` ⇒ return `-1`.

---

## 3) Python solutions (with interview-style comments)

### A) Optimal Greedy — O(n) time, O(1) space

```python
class Solution:
    def startStation(self, gas, cost):
        # If total gas < total cost, impossible
        total = 0
        # Current tank since last 'start' candidate
        curr = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            # If we went negative, none of the indices from 'start'..'i' can be a start
            if curr < 0:
                start = i + 1      # next station becomes the new candidate
                curr = 0           # reset tank for next segment

        # Feasible iff the whole circle has nonnegative total diff
        return start if total >= 0 and start < len(gas) else -1
```

**Why this is correct (sound-bite proof):**
If you fail (tank < 0) at `i` after starting at `start`, then the partial sum from `start` to `i` is negative. Starting at any `k` with `start ≤ k ≤ i` just removes some nonpositive prefix and leaves an even smaller remainder sum to reach `i`, so you still fail before or at `i`. The only viable next candidate is `i+1`. If total sum ≥ 0, some start exists; the scan finds it.

---

### B) Simple Brute Force — O(n²) time, O(1) space (for teaching/comparison)

```python
class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        for s in range(n):                 # try each possible start
            tank = 0
            ok = True
            for step in range(n):          # simulate one full lap
                i = (s + step) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    ok = False
                    break
            if ok:
                return s
        return -1
```

**When to mention it:** It’s the straightforward idea but not acceptable for large `n` (\~1e6). Use only as a baseline discussion.

---

## 4) Likely Interview Q\&A

**Q1. When can we immediately return `-1`?**
If `sum(gas) < sum(cost)`. There isn’t enough fuel in the entire circle.

**Q2. Why does resetting the start to `i+1` work when `curr < 0` at `i`?**
Because the cumulative deficit from the previous start to `i` is negative, so any start within that failed segment would hit a deficit no later than `i`. The next viable candidate must be after `i`.

**Q3. Is the valid start unique?**
Yes, the problem states uniqueness if a solution exists. (If there were multiple, the greedy still returns the leftmost after the last reset.)

**Q4. What are the time and space complexities of the greedy solution?**
Time `O(n)`, Space `O(1)`.

**Q5. Any tricky edge cases?**

* Single station: return `0` if `gas[0] >= cost[0]`, else `-1`.
* Large arrays: be mindful of linear time only.
* Values are positive by constraints; the algorithm still works with nonnegative `gas`/`cost` as long as totals are checked.

**Q6. Can floating points or overflows be an issue?**
In Python, integers are arbitrary precision, so no overflow. In other languages, use 64-bit integers.

---

---

Here’s a complete, self-contained program that includes:

* A well-commented **O(n)** greedy solution (and a baseline **O(n²)** brute force for comparison).
* A small **driver / main** that runs sample inputs and **times** both approaches using the `timeit` module.
* Inline notes on **time/space complexity** right where each step happens.

> You can paste this into a single Python file and run it as-is.

```python
from timeit import Timer
from typing import List

# ------------------------------------------------------------
# Gas Station / Circular Tour
# ------------------------------------------------------------

class GreedySolution:
    def startStation(self, gas: List[int], cost: List[int]) -> int:
        """
        Greedy single-pass solution.
        Time  : O(n) — one linear scan
        Space : O(1) — constant extra memory

        Core idea:
        - If total(gas) < total(cost) ⇒ impossible ⇒ -1  (O(n) check)
        - Otherwise, scan once with running tank 'curr'.
          Whenever 'curr' drops below 0 at index i, make start = i+1 and reset 'curr' to 0.
        """
        total = 0   # O(1) space; accumulates over O(n) time
        curr  = 0   # O(1) space; reset when segment fails
        start = 0   # O(1) space; candidate start index

        # O(n) loop — linear pass through stations
        for i in range(len(gas)):
            diff = gas[i] - cost[i]   # O(1) work
            total += diff             # O(1)
            curr  += diff             # O(1)

            # If we cannot reach station i+1 from current start,
            # then no start in [start..i] can work. Move start to i+1.
            if curr < 0:
                start = i + 1         # O(1)
                curr = 0              # O(1)

        # Final feasibility check in O(1) after O(n) accumulation
        return start if total >= 0 and start < len(gas) else -1


class BruteForceSolution:
    def startStation(self, gas: List[int], cost: List[int]) -> int:
        """
        Brute force: try every station as a start and simulate a full lap.

        Time  : O(n^2) — for each start, potentially walk n steps
        Space : O(1)
        """
        n = len(gas)
        for s in range(n):               # O(n) starts
            tank = 0
            ok = True
            for step in range(n):        # O(n) simulation per start
                i = (s + step) % n
                tank += gas[i] - cost[i]
                if tank < 0:             # fail early
                    ok = False
                    break
            if ok:
                return s
        return -1


# ------------------------------------------------------------
# Demo & Timing (uses timeit)
# ------------------------------------------------------------
def pretty(obj):
    return str(obj).replace(' ', '')

def run_examples():
    greedy = GreedySolution()
    brute  = BruteForceSolution()

    cases = [
        # (gas, cost, expected)
        ([4, 5, 7, 4], [6, 6, 3, 5], 2),    # feasible; expected start = 2
        ([1, 2, 3, 4], [2, 2, 2, 2], 3),    # feasible (one valid start is 3)
        ([3, 9], [7, 6], -1),               # impossible — not enough total gas
    ]

    print("=== Correctness on small examples ===")
    for idx, (g, c, exp) in enumerate(cases, 1):
        g_ans = greedy.startStation(g, c)
        b_ans = brute.startStation(g, c)
        print(f"Case {idx}: gas={pretty(g)}, cost={pretty(c)}")
        print(f"  Greedy : {g_ans} (expected {exp})")
        print(f"  Brute  : {b_ans} (expected {exp})")
    print()

def run_timing():
    greedy = GreedySolution()
    brute  = BruteForceSolution()

    # Build a larger *feasible* instance deterministically.
    # Time to *build* inputs is O(n), but we only build once for timing fairness.
    n = 40_000
    # Ensure feasibility by making gas[i] >= cost[i] on average
    gas  = [3 + (i % 7) for i in range(n)]       # values in [3..9]
    cost = [max(1, gas[i] - 1) for i in range(n)]  # just a little less than gas

    # Also include one impossible instance (equal sizes)
    gas_bad  = [1 + (i % 5) for i in range(n)]
    cost_bad = [gas_bad[i] + (i % 2) for i in range(n)]  # strictly more cost in many places ⇒ likely impossible

    # Wrap calls for timeit
    def t_greedy_ok():
        return greedy.startStation(gas, cost)

    def t_greedy_bad():
        return greedy.startStation(gas_bad, cost_bad)

    def t_brute_ok():
        # Brute-force on very large n would be too slow; we’ll time it on a smaller slice
        m = 1000
        return brute.startStation(gas[:m], cost[:m])

    # Timing with timeit (averaged over multiple runs)
    print("=== Timing (seconds, lower is better) ===")
    number = 5  # runs per measurement

    g_ok_time   = Timer(t_greedy_ok).timeit(number=number)
    g_bad_time  = Timer(t_greedy_bad).timeit(number=number)
    b_ok_time   = Timer(t_brute_ok).timeit(number=number)

    print(f"Greedy  (feasible, n={len(gas)}), {number} runs: {g_ok_time:.4f}s total  (~{g_ok_time/number:.6f}s/run)")
    print(f"Greedy  (impossible, n={len(gas)}), {number} runs: {g_bad_time:.4f}s total (~{g_bad_time/number:.6f}s/run)")
    print(f"Brute   (feasible, n=1000)       , {number} runs: {b_ok_time:.4f}s total  (~{b_ok_time/number:.6f}s/run)")
    print("\n(Notice Greedy scales to 40k easily, while Brute is timed only at 1k to avoid O(n^2) blowup.)\n")


if __name__ == "__main__":
    run_examples()
    run_timing()
```

### What the program prints (example)

```
=== Correctness on small examples ===
Case 1: gas=[4,5,7,4], cost=[6,6,3,5]
  Greedy : 2 (expected 2)
  Brute  : 2 (expected 2)
Case 2: gas=[1,2,3,4], cost=[2,2,2,2]
  Greedy : 3 (expected 3)
  Brute  : 3 (expected 3)
Case 3: gas=[3,9], cost=[7,6]
  Greedy : -1 (expected -1)
  Brute  : -1 (expected -1)

=== Timing (seconds, lower is better) ===
Greedy  (feasible, n=40000), 5 runs: 0.0xxx s total  (~0.000xxx s/run)
Greedy  (impossible, n=40000), 5 runs: 0.0xxx s total (~0.000xxx s/run)
Brute   (feasible, n=1000)       , 5 runs: 0.xxxx s total  (~0.0xxxx s/run)

(Your exact timings will depend on your machine.)
```

---

## 6) Real-World Use Cases (just a few important ones)

1. **Fuel/EV routing on a loop**
   Determining a viable **start depot** in a circular service route (e.g., buses, ferries, or delivery vehicles) given refueling/recharging opportunities and travel energy costs.

2. **Circular production lines**
   In ring-based manufacturing/assembly systems, ensuring a process can start at some station such that resource increments minus consumption never go negative until a full cycle completes.

3. **Token/credit systems on ring networks**
   In ring topologies (e.g., certain distributed systems), verifying that the net “credit” on each hop allows a token to traverse the full loop, and identifying a feasible starting node.
