# Bus Conductor 🚌

**Difficulty:** Easy  
**Accuracy:** 75.3%  
**Submissions:** 24K+  
**Points:** 2  

---

## Problem Statement

You are conductor of a bus. You are given two arrays **chairs[]** and **passengers[]** of equal length, where:

- `chairs[i]` is the position of the **i-th chair**
- `passengers[j]` is the position of the **j-th passenger**

You may perform the following move any number of times:

- **Increase or decrease** the position of the **i-th passenger** by **1**  
  (i.e., move the i-th passenger from position `x` to `x+1` or `x-1`)

Return the **minimum number of moves** required to move **each passenger** to get a chair.

> **Note:** Although multiple chairs can occupy the same position, **each passenger must be assigned to exactly one unique chair**.

---

## Examples

### Example 1

**Input:**  
`chairs[] = [3, 1, 5], passengers[] = [2, 7, 4]`

**Output:**  
`4`

**Explanation:** The passengers are moved as follows:
- The first passenger is moved from position **2** to position **1** using **1 move**.
- The second passenger is moved from position **7** to position **5** using **2 moves**.
- The third passenger is moved from position **4** to position **3** using **1 move**.

In total, `1 + 2 + 1 = 4` moves were used.

---

### Example 2

**Input:**  
`chairs[] = [2, 2, 6, 6], passengers[] = [1, 3, 2, 6]`

**Output:**  
`4`

**Explanation:** Note that there are two chairs at position **2** and two chairs at position **6**.  
The passengers are moved as follows:
- The first passenger is moved from position **1** to position **2** using **1 move**.
- The second passenger is moved from position **3** to position **6** using **3 moves**.
- The third passenger is not moved.
- The fourth passenger is not moved.

In total, `1 + 3 + 0 + 0 = 4` moves were used.

---

## Constraints

- `1 ≤ n ≤ 10^5`
- `1 ≤ chairs[i], passengers[j] ≤ 10^4`

---

## Expected Complexities

- **Time Complexity:** `O(n log n)`
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Arrays
- Sorting

---

## Related Articles

- Minimize The Number Of Moves Required To Seat Each Passenger In A Chair

---

---

## 2. Explanation + step-by-step dry run

### Problem in simple words

You have `n` chair positions and `n` passenger positions.
In **one move**, a passenger can shift by `+1` or `-1`.
Each passenger must be assigned to a **unique chair** (even if chairs share same position).
Goal: **minimum total moves**.

This is a classic **minimum cost matching on a line**.

### Key idea (why sorting works)

On a number line, the optimal way to minimize total absolute distance is:

> **Sort chairs and passengers, then match i-th passenger with i-th chair.**

Because if you ever “cross match” (a smaller passenger matched to a larger chair while a larger passenger matched to a smaller chair), swapping those assignments never increases and usually decreases the total distance.

So answer is:

```text
sort(chairs)
sort(passengers)
sum(|chairs[i] - passengers[i]| for i in range(n))
```

---

### Dry run 1

**chairs = [3, 1, 5]**
**passengers = [2, 7, 4]**

Sort both:

* chairs → `[1, 3, 5]`
* passengers → `[2, 4, 7]`

Pair and sum distances:

* |1 - 2| = 1
* |3 - 4| = 1
* |5 - 7| = 2

Total = 1 + 1 + 2 = **4** ✅

---

### Dry run 2

**chairs = [2, 2, 6, 6]**
**passengers = [1, 3, 2, 6]**

Sort:

* chairs → `[2, 2, 6, 6]`
* passengers → `[1, 2, 3, 6]`

Pair:

* |2 - 1| = 1
* |2 - 2| = 0
* |6 - 3| = 3
* |6 - 6| = 0

Total = 1 + 0 + 3 + 0 = **4** ✅

---

## 3. Python solutions (brute + optimized)

### 3.1 Brute force (try all assignments) — only for understanding

This is **not** usable for big `n` (n up to 1e5).
But good to mention as baseline.

```python
import itertools

class Solution:
    def findMoves_bruteforce(self, chairs, passengers):
        """
        Brute force:
        Try every permutation of chair assignments for passengers.

        Time:  O(n! * n)  (impossible for large n)
        Space: O(1) extra
        """
        n = len(chairs)
        best = float("inf")

        for perm in itertools.permutations(chairs):
            total_moves = 0
            for i in range(n):
                total_moves += abs(passengers[i] - perm[i])
            best = min(best, total_moves)

        return best
```

---

### 3.2 Optimized (expected in interviews): sort + pair

This is the main solution.

```python
class Solution:
    def findMoves(self, chairs, passengers):
        """
        Optimized approach:
          1) Sort chairs and passengers
          2) Pair i-th passenger with i-th chair
          3) Sum absolute differences

        Time:
          Sorting chairs:     O(n log n)
          Sorting passengers: O(n log n)
          Pairing sum:        O(n)
          Total:              O(n log n)

        Space:
          If sorting in place: O(1) auxiliary (Python's sort has small overhead)
        """
        # Sort both lists so nearest-by-order positions match
        chairs.sort()
        passengers.sort()

        total_moves = 0

        # Sum distances between matched pairs
        for chair_pos, passenger_pos in zip(chairs, passengers):
            total_moves += abs(chair_pos - passenger_pos)

        return total_moves
```

---

### 3.3 Alternative optimized (Counting sort style) when positions are small

Constraints say positions up to `1e4`, so we can do frequency-based greedy matching too.
This can be near **O(maxPos)** time.

(Interview note: this is optional “extra credit”.)

```python
class Solution:
    def findMoves_counting(self, chairs, passengers):
        """
        Counting-based greedy matching (works because positions are small <= 1e4).

        Time:  O(maxPos + n)
        Space: O(maxPos)

        Approach:
          - Count how many chairs and passengers at each position
          - Walk positions in increasing order and match counts
        """
        MAX_POS = 10000

        chair_count = [0] * (MAX_POS + 1)
        passenger_count = [0] * (MAX_POS + 1)

        for c in chairs:
            chair_count[c] += 1
        for p in passengers:
            passenger_count[p] += 1

        # Build expanded sorted lists using counts (still O(maxPos + n))
        sorted_chairs = []
        sorted_passengers = []

        for pos in range(1, MAX_POS + 1):
            if chair_count[pos]:
                sorted_chairs.extend([pos] * chair_count[pos])
            if passenger_count[pos]:
                sorted_passengers.extend([pos] * passenger_count[pos])

        total_moves = 0
        for c, p in zip(sorted_chairs, sorted_passengers):
            total_moves += abs(c - p)

        return total_moves
```

---

## 4. Interview: how to remember quickly + expected Q&A

### Quick memory trick

Think:

> **“1D matching → sort both → pair by index.”**

Or even shorter:

> **“Sort & zip → sum abs.”**

---

### Common interviewer questions (with answers)

**Q1. Why does sorting give the minimum?**
**A:** Because on a line, crossing assignments are never optimal.
If passenger `a < b` and chairs `x < y`, matching `a→y` and `b→x` “crosses”.
Swapping to `a→x`, `b→y` reduces (or keeps) total distance. Repeating removes all crossings → sorted pairing.

---

**Q2. What’s the time complexity?**
**A:** Sorting dominates: `O(n log n)`. Pairing sum is `O(n)`.

---

**Q3. What if multiple chairs have the same position?**
**A:** Still fine. Sorting keeps duplicates together, and we still assign uniquely by index (each chair instance is separate).

---

**Q4. Can we do better than O(n log n)?**
**A:** If positions are bounded (here ≤ 1e4), we can use counting sort / frequency matching in about `O(maxPos + n)`.

---

**Q5. What’s the brute force approach?**
**A:** Try all permutations of chair assignments → `O(n! * n)`, not feasible.

---

---

## 5. Real-World Use Cases (few, very relatable)

1. **Seating / Resource Allocation in a Line**

   * People must be assigned to seats along a corridor (cinema row, exam hall row, bus/train coach aisle).
   * Moving cost is “steps walked” → minimize total walking by sorting both positions and pairing in order.

2. **Warehouse Picking / Dock Assignment**

   * Workers (or robots) start at certain positions on a line of shelves; pickup docks are fixed positions.
   * Assign each worker to one dock minimizing total travel distance → same “sort + pair” minimum absolute distance matching.

3. **Load Balancing Across Linear Slots**

   * Think of tasks (passengers) and CPU time slots (chairs) on a timeline or ordered queue positions.
   * Moving a task to a slot has cost proportional to displacement → sort + match gives minimal total adjustment.

---

## 6. Full Program (with timing + inline complexity notes)

This program:

* Reads input
* Computes minimum moves using the **optimized sort + pair** method
* Prints output
* Prints total runtime (algorithm runtime, not including user typing time)

```python
import time
from typing import List


class Solution:
    def findMoves(self, chairs: List[int], passengers: List[int]) -> int:
        """
        Optimized approach:
            1) Sort chairs and passengers
            2) Pair i-th passenger with i-th chair
            3) Sum absolute differences

        Why it works:
            On a number line, the minimum total absolute distance matching
            is achieved by sorting both sides and pairing in order.

        Complexity:
            Let n = len(chairs) = len(passengers)

            Sorting chairs:     O(n log n)
            Sorting passengers: O(n log n)
            Pairing sum:        O(n)
            Total Time:         O(n log n)

            Auxiliary Space:    O(1) extra (in-place sort, aside from output variables)
        """
        # Step 1: Sort both lists
        # Time: O(n log n) each, Space: O(1) auxiliary
        chairs.sort()
        passengers.sort()

        # Step 2: Sum absolute differences of paired positions
        # Time: O(n), Space: O(1)
        total_moves = 0
        for chair_pos, passenger_pos in zip(chairs, passengers):
            total_moves += abs(chair_pos - passenger_pos)

        return total_moves


def main():
    """
    Input format:
        n
        chairs (n integers)
        passengers (n integers)

    Example:
        3
        3 1 5
        2 7 4

    Output:
        Minimum moves: 4
        Elapsed time: ...
    """

    # -------------------- Read Input -------------------- #
    print("Enter n:")
    n = int(input().strip())

    print(f"Enter {n} chair positions:")
    chairs = list(map(int, input().split()))
    chairs = chairs[:n]  # defensive trim if extra values

    print(f"Enter {n} passenger positions:")
    passengers = list(map(int, input().split()))
    passengers = passengers[:n]

    # -------------------- Run + Time -------------------- #
    solver = Solution()

    # Start timing (only algorithm execution time)
    start = time.perf_counter()

    # Core computation:
    # Time: O(n log n), Space: O(1) auxiliary
    answer = solver.findMoves(chairs, passengers)

    end = time.perf_counter()

    # -------------------- Output -------------------- #
    print("\nMinimum moves:", answer)
    print(f"Total elapsed time (seconds): {end - start:.8f}")


if __name__ == "__main__":
    main()
```

### Sample Input / Output

**Input**

```text
3
3 1 5
2 7 4
```

**Output**

```text
Minimum moves: 4
Total elapsed time (seconds): 0.0000xx
```

If you want, I can also provide a **counting-sort style** full program (since positions ≤ 1e4) to achieve near `O(n + 10000)` time.
