# Josephus problem

**Difficulty:** Easy  
**Accuracy:** 57.26%  
**Submissions:** 122K+  
**Points:** 2  

---

## Problem Statement

You are playing a game with **n** people standing in a circle, numbered from **1 to n**. Starting from person **1**, every **k-th** person is eliminated in a circular fashion. The process continues until only one person remains.

Given integers **n** and **k**, return the **position (1-based index)** of the person who will survive.

---

## Examples

### Example 1

**Input:**  
```

n = 5, k = 2

```

**Output:**  
```

3

```

**Explanation:**  
Firstly, the person at position **2** is killed, then the person at position **4** is killed, then the person at position **1** is killed.  
Finally, the person at position **5** is killed. So the person at position **3** survives.

---

### Example 2

**Input:**  
```

n = 7, k = 3

```

**Output:**  
```

4

```

**Explanation:**  
The elimination order is `3 → 6 → 2 → 7 → 5 → 1`, and the person at position **4** survives.

---

## Constraints

- 1 ≤ n, k ≤ 500  

---

## Expected Complexities

- **Time Complexity:** O(n)  
- **Auxiliary Space:** O(n)  

---

## Company Tags

- Amazon  
- Microsoft  
- Walmart  

---

## Topic Tags

- Recursion  
- Data Structures  
- Algorithms  

---

## Related Interview Experiences

- *Walmart Labs Interview Experience Set 3 On Campus*  

---

## Related Articles

- [*Josephus Problem*](https://www.geeksforgeeks.org/josephus-problem/)

---

---

## 2) Explanation + step-by-step dry run

### What’s happening

* People are in a circle `1..n`.
* Start from person `1`.
* Count `k` each time (including the current person as count 1), eliminate the `k-th`.
* Continue from the next person after the eliminated one.
* Return the **last remaining position (1-based)**.

---

## Two common ways to solve

### A) Simulation (easy/brute)

Maintain a circular list and keep removing every `k-th` person.
Time is ~O(n²) if you use Python list pops in the middle.

### B) Classic Josephus recurrence (optimized, interview favorite)

Let `f(n, k)` be the winner position in **0-based** indexing (positions `0..n-1`).

Base:

* `f(1, k) = 0`

Recurrence:

* When you remove one person, circle shrinks from `n` to `n-1`.
* Winner of smaller circle shifts by `k`.

[
f(n,k) = (f(n-1,k) + k) \bmod n
]

Final answer in 1-based:
[
f(n,k) + 1
]

This runs in **O(n)** time and **O(1)** space if done iteratively.

---

## Dry Run (n=5, k=2)

We compute in 0-based using recurrence:

* `f(1)=0`
* `f(2)=(0+2)%2=0`
* `f(3)=(0+2)%3=2`
* `f(4)=(2+2)%4=0`
* `f(5)=(0+2)%5=2`

Convert to 1-based: `2 + 1 = 3` ✅

Matches example (winner is position 3).

---

## Dry Run (n=7, k=3)

* `f(1)=0`
* `f(2)=(0+3)%2=1`
* `f(3)=(1+3)%3=1`
* `f(4)=(1+3)%4=0`
* `f(5)=(0+3)%5=3`
* `f(6)=(3+3)%6=0`
* `f(7)=(0+3)%7=3`

1-based: `3+1=4` ✅

---

# 3) Python codes (brute + optimized) in required format

---

## (A) Brute / Simulation (easy to understand) — O(n²)

```python
class Solution:
    def josephus(self, n, k):
        # Create people in a circle (1-based labels)
        people = list(range(1, n + 1))

        # We'll keep an index that represents "where counting starts"
        current_index = 0

        # Keep eliminating until one remains
        while len(people) > 1:
            # Move (k-1) steps ahead because current person counts as 1
            current_index = (current_index + (k - 1)) % len(people)

            # Remove the k-th person
            people.pop(current_index)

            # Next counting starts from the same index (because list shrinks)
        return people[0]
```

---

## (B) Optimized iterative recurrence (most expected) — O(n), O(1)

```python
class Solution:
    def josephus(self, n, k):
        # winner_index is 0-based winner for current circle size
        winner_index = 0  # f(1) = 0

        # Build answer from size=2 to n using recurrence:
        # f(size) = (f(size-1) + k) % size
        for size in range(2, n + 1):
            winner_index = (winner_index + k) % size

        # Convert 0-based to 1-based
        return winner_index + 1
```

---

## (C) Optimized recursion (classic, also common) — O(n) time, O(n) recursion stack

```python
class Solution:
    def josephus(self, n, k):
        def josephus_zero_based(size, step):
            # Base: only one person (0)
            if size == 1:
                return 0
            # Recurrence
            return (josephus_zero_based(size - 1, step) + step) % size

        return josephus_zero_based(n, k) + 1
```

---

# 4) Interview: quick recall + expected Q&A

## Quick recall (10 seconds)

1. Convert to 0-based winner `f`.
2. Memorize: **`f(1)=0`**
3. Recurrence: **`f(n) = (f(n-1) + k) % n`**
4. Return **`f(n)+1`**

Mnemonic: **“Shift by k, wrap by n”**.

---

## Common interviewer questions + strong answers

**Q1. Why does the recurrence work?**
**A.** After eliminating the k-th person, the circle size reduces to `n-1`. The winner in that reduced circle is shifted by `k` positions when mapping back to the original circle. Mod by `n` wraps around.

---

**Q2. What is the time complexity of the recurrence solution?**
**A.** O(n), because we compute winner for sizes 2..n once each.

---

**Q3. Why do we use 0-based indexing?**
**A.** It makes the recurrence clean with modulo. Then we convert to 1-based at the end.

---

**Q4. Can you do it with simulation? Complexity?**
**A.** Yes, using a list/circle and removing every k-th. With Python list `pop` in the middle it can become O(n²).

---

**Q5. Edge cases?**
**A.**

* `n=1` → answer 1
* `k=1` → elimination in order, winner is `n`
* large `k` → modulo naturally handles it

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Round-robin scheduling (OS / servers / load balancers)**
   Tasks/threads are visited cyclically and every *k-th* gets preempted/removed/selected next. Josephus models “who survives last” after repeated cyclic removals.

2. **Fault handling / leader election in a ring network**
   Nodes arranged logically in a ring; every k-th node fails/is removed. Josephus helps reason about the final remaining “leader” under deterministic removal.

3. **Game mechanics / token passing elimination**
   Classic party/game elimination where players are removed at fixed count intervals—direct Josephus.

---

## 6) Full Program (Optimized O(n) + runtime timing + sample I/O)

* Uses the **iterative recurrence** (most interview-expected and fastest).
* Prints runtime to **stderr** so normal output stays clean.

```python
import sys
import time


class Solution:
    def josephus(self, n, k):
        """
        Optimized Josephus using recurrence (iterative).

        Recurrence in 0-based index:
            f(1) = 0
            f(size) = (f(size-1) + k) % size

        Return 1-based: f(n) + 1

        Time:  O(n)
        Space: O(1)
        """
        winner_index = 0  # f(1) = 0 (0-based)

        # Time: O(n) loop from 2..n
        # Space: O(1) only one variable
        for size in range(2, n + 1):
            winner_index = (winner_index + k) % size

        return winner_index + 1  # convert to 1-based


def _try_parse_as_gfg_tests(tokens):
    """
    Try parsing as:
        t
        n k
        n k
        ...
    Return list of (n,k) if successful, else None.
    """
    idx = 0
    if idx >= len(tokens):
        return None

    t = tokens[idx]
    idx += 1
    pairs = []

    for _ in range(t):
        if idx + 1 >= len(tokens):
            return None
        n = tokens[idx]
        k = tokens[idx + 1]
        idx += 2
        pairs.append((n, k))

    if idx != len(tokens):
        return None
    return pairs


def main():
    # ------------------------------------------------------------
    # Measure FULL program runtime (parse + compute + print)
    # ------------------------------------------------------------
    start_time = time.perf_counter()

    data = sys.stdin.buffer.read().split()
    if not data:
        return

    tokens = list(map(int, data))

    # Prefer multi-test format if it matches perfectly
    testcases = _try_parse_as_gfg_tests(tokens)

    # Fallback: single test => just "n k"
    if testcases is None:
        if len(tokens) < 2:
            return
        testcases = [(tokens[0], tokens[1])]

    solver = Solution()

    # ------------------------------------------------------------
    # Solve each test
    # Time:  sum of O(n) per test
    # Space: O(1) per test
    # ------------------------------------------------------------
    outputs = []
    for n, k in testcases:
        outputs.append(str(solver.josephus(n, k)))

    # Print answers only (judge-friendly)
    sys.stdout.write("\n".join(outputs))

    end_time = time.perf_counter()
    # Print runtime to stderr (won't affect judged output)
    print(f"\n[Runtime] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input 1 (multi-test):
2
5 2
7 3

Sample Output 1:
3
4

Sample Input 2 (single test):
5 2

Sample Output 2:
3
"""
```

