
---

# Tower Of Hanoi

**Difficulty:** Medium
**Accuracy:** 35.23%
**Submissions:** 174K+
**Points:** 4

---

You are given **n** disks placed on a starting rod (**from**), with the smallest disk on top and the largest at the bottom.

There are three rods:

* **starting rod** (**from**)
* **target rod** (**to**)
* **auxiliary rod** (**aux**)

You have to calculate the total number of **moves** required to transfer all **n** disks from the starting rod to the target rod, **following these rules**:

1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or on an empty rod.

Return the number of moves needed to complete the task.

---

## Examples:

**Example 1:**

```
Input: n = 2
Output: 3
Explanation: For n = 2, steps will be as follows:
move disk 1 from rod 1 to rod 2  
move disk 2 from rod 1 to rod 3  
move disk 1 from rod 2 to rod 3  
Total steps taken = 3.
```

**Example 2:**

```
Input: n = 3
Output: 7
Explanation: For n = 3, steps will be as follows:
move disk 1 from rod 1 to rod 3  
move disk 2 from rod 1 to rod 2  
move disk 1 from rod 3 to rod 2  
move disk 3 from rod 1 to rod 3  
move disk 1 from rod 2 to rod 1  
move disk 2 from rod 2 to rod 3  
move disk 1 from rod 1 to rod 3  
Total steps taken = 7.
```

**Example 3:**

```
Input: n = 0
Output: 0
Explanation: Total 0 steps will be taken.
```

---

## Constraints:

```
0 ≤ n ≤ 20
```

---

## Expected Complexities:

* **Time Complexity:** O(2^n)
* **Auxiliary Space:** O(n)

---

## Company Tags:

* Flipkart
* Microsoft

---

## Topic Tags:

* Recursion
* Algorithms

---

## Related Interview Experiences:

* Flipkart Interview Experience On Campus Internship

---

## Related Articles:

* [C Program For Tower Of Hanoi](https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/)

---

---

Here’s the **summary** of the working solution you’ve provided for the **Tower of Hanoi** problem:

---

## **Tower of Hanoi – Summary (Based on Working Solution)**

### **Goal**

Given `n` disks and three rods:

* **fromm** → Starting rod (source)
* **to** → Target rod (destination)
* **aux** → Auxiliary rod (helper)

Find the **minimum number of moves** required to move all `n` disks from `fromm` to `to` following these rules:

1. Only **one disk** can be moved at a time.
2. A disk can only be placed **on top of a larger disk** or an empty rod.

---

### **Logic**

* The Tower of Hanoi problem is solved using **recursion**.
* For `n` disks:

  1. Move `n-1` disks from `fromm` → `aux` (using `to` as helper).
  2. Move the largest disk from `fromm` → `to`.
  3. Move `n-1` disks from `aux` → `to` (using `fromm` as helper).

---

### **Code Explanation**

```python
class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        moves = []  # store all moves as tuples (disk_number, from_rod, to_rod)

        def solve(k, a, b, c):
            if k == 0:  # base case: no disk to move
                return
            solve(k - 1, a, c, b)      # Step 1
            moves.append((k, a, b))    # Step 2
            solve(k - 1, c, b, a)      # Step 3

        solve(n, fromm, to, aux)
        return len(moves)  # total moves made
```

---

### **Dry Run (n = 2, from = 1, to = 3, aux = 2)**

1. Move disk 1: **1 → 2**
2. Move disk 2: **1 → 3**
3. Move disk 1: **2 → 3**

`moves = [(1,1,2), (2,1,3), (1,2,3)]`
**Output:** `3`

---

### **Time & Space Complexity**

* **Time Complexity:**

  * `O(2^n)` → Because each disk move triggers 2 recursive calls except the base case.
* **Space Complexity:**

  * `O(n)` → Recursion stack depth (ignoring storage of moves since we only return the count).

---

### **Key Formula**

The minimal number of moves for `n` disks:

$$
\text{Moves} = 2^n - 1
$$

---

---

# 4) Interview‑style Questions & Answers

**Q1. What’s the recurrence and time complexity?**
A. Let T(n) be moves for n disks.
T(n) = T(n−1) + 1 + T(n−1) = 2·T(n−1) + 1 ⇒ T(n) = 2ⁿ − 1.
Time = Θ(2ⁿ) moves. Space (recursion depth) = Θ(n).

**Q2. Why is 2ⁿ−1 minimal?**
A. By induction: to move the largest disk you must first move the top n−1 disks off the source (needs at least T(n−1) moves), then move the largest disk once, then move those n−1 onto the destination (another T(n−1)). Any legal solution needs ≥ 2·T(n−1)+1 moves. With T(1)=1 this solves to 2ⁿ−1 and the canonical recursive algorithm achieves it—so it’s optimal.

**Q3. What’s the base case and why?**
A. `n == 0`: nothing to move → return. This prevents further recursion and correctly handles n=0 (0 moves).

**Q4. Can you do it iteratively?**
A. Yes. Using bit patterns (Gray code style): for n disks, there are 2ⁿ−1 moves; at move m (1‑indexed) the disk to move is the index of the least significant set bit of m. The direction of each disk’s movement depends on parity (odd/even n). Still Θ(2ⁿ) time, Θ(1) extra space.

**Q5. Why do many platforms ask for the **count** instead of the move list?**
A. Because the move list is length 2ⁿ−1 and quickly becomes enormous (e.g., n=25 ⇒ \~33 million moves). Returning only the count avoids massive I/O and memory.

**Q6. What happens with large n (e.g., n>1000) in Python recursion?**
A. Python’s recursion depth (\~1000 by default) will overflow. You’d need an iterative formulation or to increase recursion limits (not recommended for production).

**Q7. What are the rods used in the recursive steps?**
A. Step 1: move n−1 from **fromm** → **aux** using **to**.
Step 2: move largest from **fromm** → **to**.
Step 3: move n−1 from **aux** → **to** using **fromm**.

**Q8. If disks have equal sizes?**
A. The problem assumes strictly decreasing sizes from top to bottom. Equal sizes break the ordering rule and invalidate the model.

---

# 5) Full Python Program (with inline complexity notes + `timeit` main)

```python
"""
Tower of Hanoi — minimal move count
- Time:  Θ(2^n)   (every disk triggers two subproblems plus one move)
- Space: Θ(n)     (recursion stack depth; we only return the count)
"""

from timeit import timeit

class Solution:
    def towerOfHanoi(self, n: int, fromm: int, to: int, aux: int) -> int:
        """
        Returns the minimal number of moves to transfer n disks
        from 'fromm' to 'to' using 'aux'.

        Approach:
          Recursively move n-1 disks to aux, move largest disk to 'to',
          then move n-1 disks from aux to 'to'.

        Time per call:
          - Solve(k-1, ...) twice  -> recurrence T(k) = 2*T(k-1)+1 => Θ(2^k)
        Space per call:
          - One stack frame per disk -> Θ(k)
        """
        moves = []  # Storing moves makes memory Θ(2^n); for count only we could avoid this list.

        def solve(k: int, a: int, b: int, c: int) -> None:
            # Base case: O(1) time, O(1) space (ignoring call frame)
            if k == 0:
                return
            # Step 1: move k-1 from a -> c using b: T(k-1)
            solve(k - 1, a, c, b)

            # Step 2: move largest (disk k) from a -> b: O(1)
            # We append one move (could be a tuple; kept compact):
            moves.append((k, a, b))

            # Step 3: move k-1 from c -> b using a: T(k-1)
            solve(k - 1, c, b, a)

        solve(n, fromm, to, aux)
        # Note: returning len(moves) keeps output small; list length is 2^n - 1.
        return len(moves)


# -------------------------
# Demo / main with timeit
# -------------------------
def run_demo(n: int, fromm: int = 1, to: int = 3, aux: int = 2):
    sol = Solution()
    count = sol.towerOfHanoi(n, fromm, to, aux)
    print(f"Input: n = {n}, from={fromm}, to={to}, aux={aux}")
    print(f"Minimal moves = {count}")  # equals 2^n - 1

if __name__ == "__main__":
    # Example inputs (feel free to change)
    N = 3

    # Time the full program run (including building the moves list)
    t = timeit(lambda: run_demo(N), number=1)
    print(f"\nTotal runtime (timeit, number=1): {t:.6f} sec")
```

### Example output (for `N = 2`)

```
Input: n = 2, from=1, to=3, aux=2
Minimal moves = 3

Total runtime (timeit, number=1): 0.000xxx sec
```

> Tip: If you only need the **count**, replace the `moves` list with a simple integer counter to avoid Θ(2ⁿ) memory. (But many platforms still accept returning the length of the built list as you showed.)

---

# 6) Real‑World Use Cases (a few that actually matter)

1. **Staged migrations / multi‑hop transfers**
   Moving a stack of items (databases, microservices, VMs) through a constrained pipeline (source → staging → destination) where ordering must be preserved and only one unit can move at a time.

2. **Robotics / automated storage**
   Robotic arms stacking/unstaking parts where a smaller part cannot be placed under a larger one, and only one buffer bay is available (the auxiliary rod).

3. **Compiler/register allocation thought model**
   Conceptually similar to spilling/reloading with a limited number of temporary registers/buffers while preserving order constraints.

4. **Backup media re‑stacking / tape libraries**
   Rearranging media in libraries with a single free slot (aux) while maintaining media ordering rules.

These map well to the core constraints of Tower of Hanoi: move one item at a time, obey ordering, and use a limited auxiliary space.
