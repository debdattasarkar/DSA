
# Generate Permutations of an Array

**Difficulty:** Medium  
**Accuracy:** 84.42%  
**Submissions:** 5K+  
**Points:** 4  

---

## Problem Statement

Given an array **arr[]** of **unique elements**, generate **all possible permutations** of the elements in the array.

### Note
- You can return the permutations in **any order**.
- The **driver code will print them in sorted order**.

---

## Examples

### Example 1
**Input:**  
```

arr[] = [1, 2, 3]

```

**Output:**  
```

[[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 1, 2],
[3, 2, 1]]

```

**Explanation:**  
There are **6 possible permutations** (`3! = 6`) of the array.

---

### Example 2
**Input:**  
```

arr[] = [1, 3]

```

**Output:**  
```

[[1, 3],
[3, 1]]

```

**Explanation:**  
There are **2 possible permutations** (`2! = 2`) of the array.

---

## Constraints

- `1 ≤ arr.size() ≤ 9`

---

## Expected Complexities

- **Time Complexity:** `O(n! * n)`
- **Auxiliary Space:** `O(n)`

---

## Topic Tags

- Backtracking  
- Arrays  
- Recursion  

---

## Related Articles

- **Print All Possible Permutations Of An Array/Vector Without Duplicates Using Backtracking**

---

---

## 2) Text explanation (core logic)

We must generate **all permutations** of an array of **unique** elements.

A permutation is any arrangement of all elements exactly once.
For `n` elements → total permutations = `n!`.

### Most common interview approach: Backtracking

Build the permutation **one position at a time**:

* Pick an unused element
* Place it in the current position
* Recurse to fill the next position
* Undo (backtrack) and try another element

Since elements are unique, we don’t need duplicate-handling.

---

## Step-by-step dry run (arr = [1, 2, 3])

We’ll use a `current_perm` list + `used[]` flags.

Start:

* `current_perm = []`
* `used = [F, F, F]`

### Level 0 (choose 1st element)

Pick `1`:

* `current_perm = [1]`, `used = [T, F, F]`

### Level 1 (choose 2nd element)

Pick `2`:

* `current_perm = [1,2]`, `used = [T, T, F]`

### Level 2 (choose 3rd element)

Pick `3`:

* `current_perm = [1,2,3]` → length == 3 → **store** `[1,2,3]`

Backtrack (remove last):

* `current_perm = [1,2]`, `used = [T, T, F]`
  No more choices → backtrack again:
* `current_perm = [1]`, `used = [T, F, F]`

Try other option at Level 1:
Pick `3`:

* `current_perm = [1,3]`, `used = [T, F, T]`
  Then pick `2`:
* `current_perm = [1,3,2]` → store

Backtrack to Level 0 and try starting with `2`, then `3` similarly:
Stored permutations:

* [1,2,3]
* [1,3,2]
* [2,1,3]
* [2,3,1]
* [3,1,2]
* [3,2,1]

Total = `3! = 6`

---

## 3) Python codes (different interview-expected ways)

### A) Most expected: Backtracking with `used[]` (clean + easy to explain)

**Time:** `O(n! * n)` (copying each permutation costs `O(n)`)
**Space:** `O(n)` recursion + `used[]` (output excluded)

```python
class Solution:
    def permuteDist(self, arr):
        n = len(arr)
        all_permutations = []

        # used[i] tells whether arr[i] is already taken in current permutation
        used = [False] * n
        current_perm = []

        def backtrack():
            # If current permutation is complete, store a copy
            if len(current_perm) == n:
                all_permutations.append(current_perm[:])  # O(n) copy
                return

            # Try each unused element for the next position
            for i in range(n):
                if used[i]:
                    continue

                # choose
                used[i] = True
                current_perm.append(arr[i])

                # explore
                backtrack()

                # un-choose (backtrack)
                current_perm.pop()
                used[i] = False

        backtrack()
        return all_permutations
```

---

### B) In-place swapping (classic, slightly more optimal memory)

Fix index `pos`, swap each candidate into `pos`, recurse, then swap back.

**Time:** `O(n! * n)` (still copying results)
**Aux space:** `O(n)` recursion (no used[])

```python
class Solution:
    def permuteDist(self, arr):
        n = len(arr)
        all_permutations = []

        def backtrack(pos):
            # If we've fixed all positions, store the arrangement
            if pos == n:
                all_permutations.append(arr[:])  # copy current state
                return

            for i in range(pos, n):
                # place arr[i] at position pos
                arr[pos], arr[i] = arr[i], arr[pos]

                backtrack(pos + 1)

                # undo swap
                arr[pos], arr[i] = arr[i], arr[pos]

        backtrack(0)
        return all_permutations
```

---

### C) “Brute-ish & simplest to write” using Python library

Often acceptable to mention, but many interviewers prefer backtracking.

```python
from itertools import permutations

class Solution:
    def permuteDist(self, arr):
        # permutations(arr) returns tuples, convert to lists
        return [list(p) for p in permutations(arr)]
```

---

## 4) Interview quick-recall + expected Q&A

### 30-second memory template (what to say)

**“Fix a position, try every unused element there, recurse, then undo.”**

Two common variants:

* **used[] method**: build `current_perm`
* **swap method**: fix `pos` in-place

### Tiny pseudocode you can rebuild fast

```text
ans = []
backtrack(state):
  if complete: ans.add(copy(state))
  for each choice not used:
    choose
    backtrack
    undo
return ans
```

---

## Expected Interview Questions & Answers

### Q1) What’s the total number of permutations?

**A:** `n!` for `n` unique elements.

### Q2) Why is time complexity `O(n! * n)`?

**A:** There are `n!` permutations, and storing each requires copying `n` elements.

### Q3) Difference between used[] and swapping?

**A:**

* `used[]`: clearer, doesn’t modify input, uses extra `O(n)` for used array.
* swapping: modifies array in-place, saves `used[]`, still `O(n)` recursion stack.

### Q4) How to handle duplicates if array wasn’t unique?

**A:** Sort the array and skip duplicates in the same level (or use a frequency map).

### Q5) Can we return in any order?

**A:** Yes. Problem states driver will print sorted order.

### Q6) What’s the auxiliary space?

**A:** `O(n)` recursion depth (+ `O(n)` for `used[]` if using that method). Output space is `O(n! * n)`.

---

---

## 5) Real-world use cases (few, very relatable)

1. **Scheduling / ordering problems**

   * Trying all possible orders of tasks/meetings/jobs to find the best sequence (small `n`), e.g., minimize total setup time.

2. **Testing & QA (permutation testing)**

   * Checking software behavior under different orders of actions/events (login→pay→logout vs pay→login→logout) to catch edge-case bugs.

3. **Route / path exploration for small sets**

   * For a small number of locations/stops, generating all orders to brute-force the shortest route (mini Traveling Salesman style).

---

## 6) Full Python program (timed, with inline time/space notes + sample I/O)

* Uses the **most interview-expected** approach: backtracking with `used[]`.
* Prints the runtime to **stderr** so stdout remains clean.

```python
import sys
import time

class Solution:
    def permuteDist(self, arr):
        """
        Generate all permutations of a list of unique elements.

        Time Complexity:
          - There are n! permutations
          - Storing each permutation costs O(n) (copy)
          => Total: O(n! * n)

        Auxiliary Space (excluding output):
          - used[] : O(n)
          - recursion stack depth : O(n)
          => O(n)
        """
        n = len(arr)

        # Step 1: Prepare containers
        # Time: O(1), Space: O(n) for used + O(n) for path (max)
        all_permutations = []
        used = [False] * n
        current_perm = []

        def backtrack():
            # Step 2: If permutation complete, store a copy
            # Time: O(n) for copying current_perm, Space: O(n) for stored result
            if len(current_perm) == n:
                all_permutations.append(current_perm[:])
                return

            # Step 3: Try placing each unused element next
            # Each level loops over n, but total work over tree -> O(n! * n)
            for i in range(n):
                if used[i]:
                    continue

                # choose
                used[i] = True
                current_perm.append(arr[i])

                # explore
                backtrack()

                # un-choose (backtrack)
                current_perm.pop()
                used[i] = False

        # Step 4: Start recursion
        # Time: O(n! * n), Space: O(n) recursion depth
        backtrack()

        return all_permutations


def main():
    """
    Input format (simple, interview/CP style):
    - First line: n (size of array)
    - Second line: n space-separated integers

    Output:
    - Prints permutations line by line (order may differ from sample;
      problem allows any order; driver prints sorted order in platform)
    """
    start_time = time.perf_counter()  # measure full program runtime

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Step A: Read input
    # Time: O(n), Space: O(n)
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))

    solver = Solution()

    # Step B: Compute permutations
    # Time: O(n! * n), Auxiliary Space: O(n) (output excluded)
    result = solver.permuteDist(arr)

    # Step C: Print output
    # Time: O(n! * n) to print everything
    for perm in result:
        print(perm)

    end_time = time.perf_counter()
    # Print timing to stderr so it doesn't affect judge output expectations
    print(f"\n[Execution Time] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input:
3
1 2 3

One Possible Output:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
"""
```
