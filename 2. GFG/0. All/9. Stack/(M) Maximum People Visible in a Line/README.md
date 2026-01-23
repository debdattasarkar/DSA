
# Maximum People Visible in a Line

**Difficulty:** Medium  
**Accuracy:** 34.92%  
**Submissions:** 529+  
**Points:** 4  

---

## Problem Statement

You are given an array **arr[]**, where `arr[i]` represents the height of the *i-th* person standing in a line.

A person **i** can see another person **j** if:

- `height[j] < height[i]`, and  
- There is **no person k standing between them** such that  
  `height[k] ≥ height[j]`.

Each person can see in **both directions** (front and back).

Your task is to find the **maximum number of people that any single person can see (including themselves)**.

---

## Examples

### Example 1

**Input:**  
```

arr[] = [6, 2, 5, 4, 5, 1, 6]

```

**Output:**  
```

6

```

**Explanation:**  

- Person 1 (height = 6) can see five other people at positions  
  (2, 3, 4, 5, 6) in addition to himself, i.e. total **6**.
- Person 2 (height = 2) can see only himself.
- Person 3 (height = 5) is able to see people 2nd, 3rd, and 4th person.
- Person 4 (height = 4) can see himself.
- Person 5 (height = 5) can see people 4th, 5th, and 6th.
- Person 6 (height = 1) can only see himself.
- Person 7 (height = 6) can see 2nd, 3rd, 4th, 5th, 6th, and 7th people.

A maximum of **six** people can be seen by **Person 1** and **Person 7**.

---

### Example 2

**Input:**  
```

arr[] = [1, 3, 6, 4]

```

**Output:**  
```

4

```

**Explanation:**  

Person with height **6** can see persons with heights **1, 3** on the left and **4** on the right, along with himself, giving a total of **4**.

---

## Constraints

- 1 ≤ arr.size() ≤ 10⁴  
- 1 ≤ arr[i] ≤ 10⁵  

---

## Expected Complexities

- **Time Complexity:** O(n)  
- **Auxiliary Space:** O(n)  

---

## Topic Tags

- Stack  
- Arrays  
- Data Structures  

---

## Related Articles

- *Maximum People A Person Can See While Standing In a Line In Both Direction*

---

---

## 2) Text explanation (what “visible” really means)

A person **i** (height `h = arr[i]`) can see another person **j** if:

* `arr[j] < arr[i]` (j is shorter), and
* **between i and j**, there is **no person with height ≥ arr[i]**.

So from person `i`, looking **left**:

* You can keep seeing people until you hit the **first person whose height ≥ arr[i]** (that person blocks the view and is not visible because it’s not shorter).
* Everyone **before that blocker** is visible (they’re all < `arr[i]`).

Same on the **right**.

### Key reduction

Let:

* `L = index of previous person to the left with height >= arr[i]` (blocking on left), else `-1`
* `R = index of next person to the right with height >= arr[i]` (blocking on right), else `n`

Then person `i` can see:

* left side: `i - L - 1` people
* right side: `R - i - 1` people
* plus themselves: `+1`

So total visible (including self):

[
\text{visible}[i] = (i-L-1) + (R-i-1) + 1 = R - L - 1
]

So the answer is:

[
\max_i (,nextGreaterOrEqual[i] - prevGreaterOrEqual[i] - 1,)
]

We can compute `prevGreaterOrEqual` and `nextGreaterOrEqual` in **O(n)** using a **monotonic decreasing stack**.

---

## Step-by-step dry run (Example 1)

`arr = [6, 2, 5, 4, 5, 1, 6]`, `n=7`

We find for each index `i`:

* `L = previous index with height >= arr[i]`
* `R = next index with height >= arr[i]`
* visible = `R - L - 1`

### For i = 0, arr[i]=6

* Left blocker `L = -1` (none)
* Right blocker `R = 6` (arr[6]=6 is >= 6)
* visible = `6 - (-1) - 1 = 6` ✅ (sees indices 0..5, includes self)

### For i = 2, arr[i]=5

* Left blocker `L = 0` (arr[0]=6 >= 5)
* Right blocker `R = 4` (arr[4]=5 >= 5)
* visible = `4 - 0 - 1 = 3` → indices {1,2,3} (2,5,4)

### For i = 6, arr[i]=6

* Left blocker `L = 0` (arr[0]=6 >= 6)
* Right blocker `R = 7` (none)
* visible = `7 - 0 - 1 = 6` ✅

Maximum visible = **6** (matches output).

---

## 3) Python codes (brute + optimized)

### (A) Brute force (easy to explain) — O(n²)

```python
class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        best = 1

        for i in range(n):
            height_i = arr[i]

            # Count visible to the left until blocker (>= height_i)
            left_visible = 0
            j = i - 1
            while j >= 0 and arr[j] < height_i:
                left_visible += 1
                j -= 1

            # Count visible to the right until blocker (>= height_i)
            right_visible = 0
            j = i + 1
            while j < n and arr[j] < height_i:
                right_visible += 1
                j += 1

            # +1 to include self
            best = max(best, left_visible + right_visible + 1)

        return best
```

---

### (B) Optimized (most expected in interviews) — O(n) using monotonic stack

We compute nearest **greater-or-equal** on both sides.

```python
class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        prev_ge = [-1] * n   # previous index with arr[idx] >= arr[i]
        next_ge = [n] * n    # next index with arr[idx] >= arr[i]

        # -------- prev greater-or-equal (>=) using decreasing stack --------
        # Stack stores indices with heights in NON-increasing order.
        stack = []
        for i in range(n):
            # pop strictly smaller, because they can't block current or future >= queries
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            prev_ge[i] = stack[-1] if stack else -1
            stack.append(i)

        # -------- next greater-or-equal (>=) from right --------
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_ge[i] = stack[-1] if stack else n
            stack.append(i)

        # visible[i] = next_ge[i] - prev_ge[i] - 1
        best = 1
        for i in range(n):
            visible = next_ge[i] - prev_ge[i] - 1
            if visible > best:
                best = visible

        return best
```

**Why this works:** the first person with height `>= arr[i]` blocks the view; everyone between the blockers is shorter than `arr[i]`, hence visible.

---

## 4) Interview “quick remember” + expected Q&A

### Fast memory trick (10 seconds)

**“Nearest taller-or-equal on both sides.”**
Answer for i is just the **gap length**:

[
\text{visible}[i] = R - L - 1
]

Where:

* `L = prev >=`
* `R = next >=`

### Mnemonic for stack

**“Pop smaller, keep bigger/equal as blockers.”**
(because blocker condition is `>= arr[i]`)

---

### Common interviewer Q&A

**Q1. What blocks visibility?**
**A.** The first person in that direction whose height is **>= current person’s height**.

**Q2. Why is the count just a continuous segment?**
**A.** Because once you hit a `>= arr[i]` person, anyone beyond is blocked by that person (and the blocker itself isn’t visible since it’s not shorter).

**Q3. What do you compute in O(n)?**
**A.** For each index, the nearest `>=` element to left and to right using monotonic stacks.

**Q4. Why “>=” and not “>”?**
**A.** Equal height also blocks because it violates the “shorter” condition (`arr[j] < arr[i]`) and acts as a blocker for further people.

**Q5. Complexity?**
**A.** Stack approach: **O(n)** time (each index pushed/popped once), **O(n)** space.

---

---

## 5) Real-World Use Cases (few, interviewer-relatable)

1. **Crowd visibility / event planning (line-of-sight in a queue)**
   In a queue at a concert/security check, a tall person can “see” how many people are in view before another tall person blocks. Helps reason about **visibility, supervision, or signage placement**.

2. **Camera / sensor occlusion in robotics (1D simplification)**
   Heights represent obstacles; a robot/camera can detect targets until a **blocking obstacle** (≥ height threshold) appears. This is a clean 1D model of **occlusion boundaries**.

3. **Network signal / skyline obstruction (1D model)**
   Heights as buildings/terrain: how far “visibility” goes before a **blocking ridge/building**. Used as a simplified model for **coverage estimation**.

---

## 6) Full Program (Optimized O(n) + runtime timing + sample I/O)

* Computes nearest **greater-or-equal** on left and right using monotonic stacks.
* Visible count for person `i` = `next_ge[i] - prev_ge[i] - 1`
* Prints runtime to **stderr** (so judged output stays clean).

```python
import sys
import time


class Solution:
    def maxPeople(self, arr):
        """
        Optimized approach using monotonic stacks.

        Key idea:
        For each i, let:
          L = previous index with arr[L] >= arr[i]  (blocks on left)
          R = next index with arr[R] >= arr[i]      (blocks on right)
        Then visible including self:
          visible[i] = (i-L-1) + (R-i-1) + 1 = R - L - 1

        Time:  O(n)   (each index pushed/popped at most once per pass)
        Space: O(n)   (arrays + stack)
        """
        n = len(arr)
        if n == 0:
            return 0

        # Space: O(n)
        prev_ge = [-1] * n  # prev greater-or-equal index
        next_ge = [n] * n   # next greater-or-equal index

        # ------------------------------------------------------------
        # 1) Compute prev_ge in one left-to-right pass
        # Monotonic stack (non-increasing heights by index)
        # Time:  O(n)
        # Space: O(n) stack
        # ------------------------------------------------------------
        stack = []
        for i in range(n):
            # Pop strictly smaller elements; they cannot be blockers for current/future
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            prev_ge[i] = stack[-1] if stack else -1
            stack.append(i)

        # ------------------------------------------------------------
        # 2) Compute next_ge in one right-to-left pass
        # Time:  O(n)
        # Space: O(n) stack
        # ------------------------------------------------------------
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_ge[i] = stack[-1] if stack else n
            stack.append(i)

        # ------------------------------------------------------------
        # 3) Compute maximum visible count
        # Time:  O(n)
        # Space: O(1) extra
        # ------------------------------------------------------------
        best = 1
        for i in range(n):
            visible = next_ge[i] - prev_ge[i] - 1
            if visible > best:
                best = visible

        return best


def _try_parse_as_gfg_tests(tokens):
    """
    Try parsing as:
      t
      n
      n numbers
      ...
    Return list of arrays if successful, else None.
    """
    idx = 0
    if idx >= len(tokens):
        return None

    t = tokens[idx]
    idx += 1

    testcases = []
    for _ in range(t):
        if idx >= len(tokens):
            return None
        n = tokens[idx]
        idx += 1
        if idx + n > len(tokens):
            return None
        arr = tokens[idx:idx + n]
        idx += n
        testcases.append(arr)

    if idx != len(tokens):
        return None
    return testcases


def main():
    # ------------------------------------------------------------
    # Measure FULL program runtime (input parse + compute + output)
    # ------------------------------------------------------------
    start_time = time.perf_counter()

    data = sys.stdin.buffer.read().split()
    if not data:
        return

    tokens = list(map(int, data))

    # Prefer GFG-style multi-test parsing if it fits
    testcases = _try_parse_as_gfg_tests(tokens)

    # Fallback: single testcase format => n then n elements
    if testcases is None:
        idx = 0
        n = tokens[idx]
        idx += 1
        arr = tokens[idx:idx + n]
        testcases = [arr]

    solver = Solution()

    # Each test runs in O(n)
    outputs = []
    for arr in testcases:
        outputs.append(str(solver.maxPeople(arr)))

    # Print only answers to stdout (judge-friendly)
    sys.stdout.write("\n".join(outputs))

    end_time = time.perf_counter()
    # Print runtime to stderr (won't affect judged output)
    print(f"\n[Runtime] {end_time - start_time:.6f} seconds", file=sys.stderr)


if __name__ == "__main__":
    main()


"""
Sample Input 1 (GFG-style):
1
7
6 2 5 4 5 1 6

Sample Output 1:
6

Sample Input 2:
1
4
1 3 6 4

Sample Output 2:
4
"""
```
