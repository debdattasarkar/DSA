# Shortest Prime Path

**Difficulty:** Medium
**Accuracy:** 39.46% **Submissions:** 3K+ **Points:** 4

You are given two four digit prime numbers **Num1** and **Num2**. Find the distance of the shortest path from **Num1** to **Num2** that can be attained by altering only a single digit at a time such that **every intermediate number is also a four-digit prime** with **no leading zeros**.

---

### Example 1

**Input:**
Num1 = `1033`
Num2 = `8179`

**Output:**
`6`

**Explanation:**
`1033 -> 1733 -> 3733 -> 3739 -> 3779 -> 8779 -> 8179`
There are only 6 steps required to reach **Num2** from **Num1**, and all the intermediate numbers are 4-digit prime numbers.

---

### Example 2

**Input:**
Num1 = `1033`
Num2 = `1033`

**Output:**
`0`

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`solve()`** which takes two integers **Num1** and **Num2** as input parameters and returns the distance of the shortest path from **Num1** to **Num2**. If it is unreachable then return **-1**.

---

## Expected Time Complexity

O(1)

## Expected Auxiliary Space

O(1)

> (In practice, an implementation typically uses BFS over the 4-digit primes set, which runs in roughly O(#primes × 10 × 4), but the platform marks it as constant relative to test limits.)

---

## Constraints

```
1000 <= Num1, Num2 <= 9999
Num1 and Num2 are prime numbers.
```

---

## Company Tags

Adobe

## Topic Tags

Prime Number • Shortest Path • BFS • Algorithms

## Related Interview Experiences

* Adobe Interview Experience 4

## Related Articles

* [Shortest Path Reach One Prime Changing Single Digit Time](https://www.geeksforgeeks.org/shortest-path-reach-one-prime-changing-single-digit-time/)

---

---

Here’s everything you need for **Shortest Prime Path**—a clear explanation + dry run, then two interview-ready Python solutions (straight BFS and a bidirectional BFS optimization), and finally a quick interviewer Q&A.

---

# 2) Problem intuition + step-by-step dry run

**What are we doing?**
We have two 4-digit primes `Num1` and `Num2`. In one *move* you may change **exactly one digit** (thousands, hundreds, tens, or ones). The new number must:

* still be a 4-digit number (no leading zero), and
* be **prime**.

We want the **minimum number of moves** to go from `Num1` to `Num2`.

That’s a classic **unweighted shortest path** on an **implicit graph**:

* **Nodes**: all 4-digit primes (from 1001…9999).
* **Edge** between two primes if they differ in exactly one digit.

Use **BFS** from `Num1` until we see `Num2`.

### Neighbor generation

From a prime like `p=1033`:

* Consider each position (thousands, hundreds, tens, ones).
* Try replacing it with digits `0..9` (thousands can’t be `0`).
* Skip the original digit.
* Keep only 4-digit **primes**.

### Why BFS works

Each edge has weight 1; BFS explores in layers of distance, so the first time we pop `Num2` we’ve found the shortest number of moves.

---

## Step-by-step dry run (Example)

**Input:** `Num1 = 1033`, `Num2 = 8179`

We’ll show the BFS *frontier* (queue) growth at a high level (showing just the primes that matter for this path).

**Layer 0 (distance 0):**

* start = 1033

**Layer 1 (distance 1):**
Neighbors of 1033 by one-digit change (prime only). One of the valid neighbors is `1733`.

**Layer 2 (distance 2):**
From 1733 → among neighbors is `3733`.

**Layer 3 (distance 3):**
From 3733 → among neighbors is `3739`.

**Layer 4 (distance 4):**
From 3739 → among neighbors is `3779`.

**Layer 5 (distance 5):**
From 3779 → among neighbors is `8779`.

**Layer 6 (distance 6):**
From 8779 → among neighbors is `8179` (target).
We stop and return **6**.

So, a shortest path is:

```
1033 → 1733 → 3733 → 3739 → 3779 → 8779 → 8179
```

---

# 3) Optimized codes (two common interview flavors)

### A) Straight BFS (sieve + on-the-fly neighbor generation) — **most expected**

* Precompute primality for all numbers up to 9999 using a sieve (fast).
* BFS from `Num1`.
* Generate neighbors by changing one digit at a time and checking primality via sieve.
* Use `visited` to avoid revisiting primes.

```python
# User function Template for python3
from collections import deque

class Solution:
    def solve(self, Num1: int, Num2: int) -> int:
        """
        Straight BFS on implicit graph of 4-digit primes.
        Time:  O( P * 40 ) roughly, where P is number of 4-digit primes (~1061)
               Each node generates up to 36-40 candidates (4 positions * up to 10 digits).
        Space: O(P)
        """

        # Quick exit
        if Num1 == Num2:
            return 0

        # 1) Sieve: primality up to 9999 (we only care 1000..9999)
        MAXN = 10000
        is_prime = [True] * MAXN
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(MAXN**0.5) + 1):
            if is_prime[p]:
                step = p
                start = p * p
                for x in range(start, MAXN, step):
                    is_prime[x] = False

        # Ensure inputs fit the domain
        if not (is_prime[Num1] and is_prime[Num2]):
            # Per problem statement both are primes; this is defensive.
            return -1

        # 2) BFS setup
        q = deque()
        q.append((Num1, 0))  # (current_prime, distance)
        visited = set([Num1])

        # Helper to generate one-digit-different prime neighbors
        def neighbors(x: int):
            s = list(str(x))
            for i in range(4):
                original = s[i]
                for d in '0123456789':
                    if d == original:
                        continue
                    if i == 0 and d == '0':  # no leading zero
                        continue
                    s[i] = d
                    y = int(''.join(s))
                    if is_prime[y]:
                        yield y
                s[i] = original

        # 3) BFS loop
        while q:
            cur, dist = q.popleft()
            for nxt in neighbors(cur):
                if nxt in visited:
                    continue
                if nxt == Num2:
                    return dist + 1
                visited.add(nxt)
                q.append((nxt, dist + 1))

        # If unreachable
        return -1
```

---

### B) Bidirectional BFS (often suggested as an optimization)

* BFS from both ends simultaneously.
* Typically reduces explored states (good when graph is large/dense).
* Stop when frontiers meet.

```python
from collections import deque

class Solution:
    def solve(self, Num1: int, Num2: int) -> int:
        """
        Bidirectional BFS between Num1 and Num2.
        Time:  Similar big-O, often faster in practice (search space halves).
        Space: O(P)
        """
        if Num1 == Num2:
            return 0

        # Build sieve once
        MAXN = 10000
        is_prime = [True] * MAXN
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(MAXN**0.5) + 1):
            if is_prime[p]:
                for x in range(p*p, MAXN, p):
                    is_prime[x] = False

        if not (is_prime[Num1] and is_prime[Num2]):
            return -1

        def neighbors(x: int):
            s = list(str(x))
            for i in range(4):
                orig = s[i]
                for d in '0123456789':
                    if d == orig:
                        continue
                    if i == 0 and d == '0':
                        continue
                    s[i] = d
                    y = int(''.join(s))
                    if is_prime[y]:
                        yield y
                s[i] = orig

        # Frontiers and distances from each side
        q1, q2 = deque([Num1]), deque([Num2])
        dist1, dist2 = {Num1: 0}, {Num2: 0}

        while q1 and q2:
            # Expand the smaller frontier to keep search balanced
            if len(q1) <= len(q2):
                for _ in range(len(q1)):
                    cur = q1.popleft()
                    for nxt in neighbors(cur):
                        if nxt in dist1:
                            continue
                        dist1[nxt] = dist1[cur] + 1
                        if nxt in dist2:
                            return dist1[nxt] + dist2[nxt]
                        q1.append(nxt)
            else:
                for _ in range(len(q2)):
                    cur = q2.popleft()
                    for nxt in neighbors(cur):
                        if nxt in dist2:
                            continue
                        dist2[nxt] = dist2[cur] + 1
                        if nxt in dist1:
                            return dist1[nxt] + dist2[nxt]
                        q2.append(nxt)

        return -1
```

---

## Complexity discussion

Let **P** ≈ 1061 be the count of 4-digit primes.

* Each node generates at most ~36–40 candidates.
* **Time:** `O(P * 40)` in the worst case for BFS; bidirectional BFS often visits many fewer nodes in practice.
* **Space:** `O(P)` for `visited`/`distance` + sieve.

---

# 4) Likely interviewer Q&A

**Q1. Why is BFS the right algorithm here?**
A1. The graph is unweighted; BFS finds the shortest path (fewest edges) in linear time relative to the explored nodes.

**Q2. How do you ensure you don’t create a number with a leading zero?**
A2. When mutating the thousands digit, skip `'0'`.

**Q3. How do you test primality efficiently for neighbors?**
A3. Precompute a sieve (0..9999). Then each primality check is O(1).

**Q4. What if `Num1 == Num2`?**
A4. Return `0` immediately—no moves are required.

**Q5. Could there be no valid path?**
A5. Yes. If BFS exhausts all reachable 4-digit primes without hitting the target, return `-1`.

**Q6. Why bidirectional BFS?**
A6. Two frontiers from both ends reduce the search depth to half (roughly), so the number of explored states often drops drastically.

**Q7. Can we prebuild the whole graph?**
A7. You can (P ~ 1061 nodes, degree up to ~40 ⇒ ~20–25K edges). Building edges costs O(P * 40). It’s fine, but on-the-fly neighbor generation + sieve is simpler and equally efficient.

**Q8. Any edge cases to be careful about?**
A8. Thousands digit must remain non-zero; ensure you don’t revisit nodes; keep inputs confirmed as primes; return 0 if start equals target.

---

---

