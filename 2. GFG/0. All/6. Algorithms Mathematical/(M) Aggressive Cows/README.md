
---

# 🐄 Aggressive Cows

### Difficulty: Medium

**Accuracy**: 59.57%
**Submissions**: 149K+
**Points**: 4
**Average Time**: 30m

---

## 🧠 Problem Statement

You are given an array with unique elements of `stalls[]`, which denote the position of a **stall**. You are also given an integer `k` which denotes the number of **aggressive cows**.

Your task is to assign **stalls** to `k` cows such that the **minimum distance** between any two of them is the **maximum possible**.

---

## 📦 Examples

### Example 1:

```
Input:
stalls[] = [1, 2, 4, 8, 9], k = 3

Output:
3

Explanation:
The first cow can be placed at stalls[0] = 1  
The second cow can be placed at stalls[2] = 4  
The third cow can be placed at stalls[3] = 8  

The minimum distance between cows is 3, which also is the largest among all possible configurations.
```

---

### Example 2:

```
Input:
stalls[] = [10, 1, 2, 7, 5], k = 3

Output:
4

Explanation:
Place cows at stalls[0]=1, stalls[1]=5, and stalls[4]=10.  
Minimum distance is 4, which is the maximum achievable.
```

---

### Example 3:

```
Input:
stalls[] = [2, 12, 11, 3, 26, 7], k = 5

Output:
1

Explanation:
Each cow can be placed in any of the stalls, since the number of cows = number of stalls.  
The minimum distance in this case is 1 (the lowest possible between any two adjacent placements).
```

---

## 📌 Constraints:

* 2 ≤ `stalls.size()` ≤ 10⁶
* 0 ≤ `stalls[i]` ≤ 10⁸
* 2 ≤ `k` ≤ `stalls.size()`

---

## 📈 Expected Time & Space Complexities

* **Time Complexity**: O(n log m), where m is the maximum stall distance
* **Auxiliary Space**: O(1)

---

## 🏷️ Tags

* Binary Search
* Algorithms

---

## 🔗 Related Articles

* [Assign Stalls To K Cows To Maximize The Minimum Distance Between Them](https://www.geeksforgeeks.org/aggressive-cows-dynamic-programming-question/)

---

---

### ✅ 2. Explanation + Dry Run

#### Problem Summary:

Given:

* An array `stalls[]` of size `n`, each element is a position of a stall.
* An integer `k`, the number of cows.

**Goal:** Place `k` cows in the stalls so that the minimum distance between any two cows is **as large as possible**.

---

### 🔍 Strategy: Binary Search on Answer

We use binary search on the **"minimum possible distance"** between cows:

* Start with `low = 1`, and `high = max(stalls) - min(stalls)`
* For each mid (candidate distance), check **can we place k cows** with at least this distance.

  * If yes: try a larger distance → `low = mid + 1`
  * If no: try a smaller distance → `high = mid - 1`

---

### 🔁 Dry Run

**Input:** `stalls = [1, 2, 4, 8, 9]`, `k = 3`

Sorted stalls: `[1, 2, 4, 8, 9]`

* Binary search range: `low = 1`, `high = 8`
* Try `mid = 4`:

  * Place 1st cow at 1
  * Next cow can go at 8 (distance ≥ 4)
  * Only 2 cows placed → ❌
* Try `mid = 3`:

  * 1st at 1
  * 2nd at 4
  * 3rd at 8 → ✅
* Try `mid = 4` again → fails

✅ Max distance = **3**

---

### ✅ 3. Python Code (Optimized – Interview Friendly)

```python
from timeit import default_timer as timer

class Solution:
    def aggressiveCows(self, stalls, k):
        # Time: O(n log m), where m = max(stalls) - min(stalls)
        # Space: O(1) auxiliary
        stalls.sort()  # O(n log n)

        def canPlaceCows(min_gap):
            countCows = 1  # Place first cow at the first stall
            prev_stall_loc = 0
            no_of_stalls = len(stalls)
            for curr_stall_loc in range(1, no_of_stalls):
                if stalls[curr_stall_loc] - stalls[prev_stall_loc] >= min_gap:
                    countCows += 1
                    prev_stall_loc = curr_stall_loc
                if countCows >= k:
                    return True
            return False

        left, right = 0, stalls[-1] - stalls[0]
        maxGap = 0

        while left <= right:
            gap = (left + right) // 2
            if canPlaceCows(gap):
                maxGap = gap
                left = gap + 1  # Try for larger min distance
            else:
                right = gap - 1  # Try smaller distance
        return maxGap

# Main program with timing
if __name__ == "__main__":
    start = timer()
    stalls = [1, 2, 4, 8, 9]
    k = 3
    sol = Solution()
    result = sol.aggressiveCows(stalls, k)
    end = timer()
    print(f"Max Min Distance: {result}")
    print(f"Time taken: {end - start:.6f} seconds")
```

---

### 📚 4. Interview-Focused Q\&A

**Q1: Why binary search?**

> Because the problem asks to **maximize the minimum distance** — a classic case for **searching on answer**.

**Q2: Why do we sort the stalls?**

> We must place cows in increasing stall positions to properly evaluate distances.

**Q3: What's the time complexity?**

> * Sorting: O(n log n)
> * Binary search: O(log(max\_dist))
> * Each check: O(n) → Total = O(n log(max\_dist))

**Q4: Can we solve this with brute force?**

> Yes, but it’s exponential in nature (combinations of stall positions). Infeasible for large `n`.

**Q5: What if stalls had duplicate positions?**

> We must ensure stalls are unique, or deduplicate if necessary. Otherwise, 0 distance becomes a valid placement.

---

### 🌍 Real-World Use Cases (Important Ones)

1. **Wi-Fi Router Placement:** Place `k` routers in `n` buildings such that signal interference (min distance) is maximized.
2. **Server Allocation in Data Centers:** Place `k` servers in `n` slots to maximize airflow/cooling space.
3. **Classroom or Seat Assignment:** Allocate seats to maximize social distancing or privacy.

