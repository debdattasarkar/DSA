# Search insert position of K in a sorted array 🔎

**Difficulty:** Easy  
**Accuracy:** 38.99%  
**Submissions:** 98K+  
**Points:** 2  

---

## Problem Statement

Given a sorted array `arr[]` (0-index based) of distinct integers and an integer `k`, find the **index of `k`** if it is present in the `arr[]`.  
If not, return the index where `k` should be inserted to maintain the **sorted order**.

---

## Examples

### Example 1
**Input:** `arr[] = [1, 3, 5, 6], k = 5`  
**Output:** `2`  
**Explanation:** Since `5` is found at index `2` as `arr[2] = 5`, the output is `2`.

---

### Example 2
**Input:** `arr[] = [1, 3, 5, 6], k = 2`  
**Output:** `1`  
**Explanation:** The element `2` is not present in the array, but inserting it at index `1` will maintain the sorted order.

---

### Example 3
**Input:** `arr[] = [2, 6, 7, 10, 14], k = 15`  
**Output:** `5`  
**Explanation:** The element `15` is not present in the array, but inserting it after index `4` will maintain the sorted order.

---

## Constraints

- `1 ≤ arr.size() < 10^4`
- `-10^3 ≤ arr[i] ≤ 10^3`
- `-10^3 ≤ k ≤ 10^3`

---

## Expected Complexities

- **Time Complexity:** `O(log n)`
- **Auxiliary Space:** `O(1)`

---

## Company Tags

- Microsoft

---

## Topic Tags

- Searching
- Algorithms

---

## Related Articles

- Search Insert Position Of K In A Sorted Array


---

---

## 2. Text explanation + step-by-step dry run

### What you need to return

Given a **sorted** array `arr` (0-indexed, distinct ints) and an integer `k`:

* If `k` exists → return its index.
* If not → return the index where `k` should be inserted to keep the array sorted.

This is exactly the **lower bound** position:

> first index `i` such that `arr[i] >= k`
> If no such index exists, answer is `n` (insert at end).

---

### Why Binary Search works

Array is sorted → we can locate the first position where values become `>= k` in `O(log n)`.

We maintain a search range `[left, right]` and keep shrinking it.

A robust pattern (easy to remember) is:

* `left = 0`, `right = n` (notice right is **n**, not n-1)
* while `left < right`:

  * mid = (left + right) // 2
  * if `arr[mid] < k` → left = mid + 1
  * else → right = mid
* answer = left

This returns the correct insert position even if `k` doesn’t exist.

---

### Dry run 1

`arr = [1, 3, 5, 6], k = 5`

n=4
left=0, right=4

* mid=2 → arr[2]=5

  * arr[mid] < k ? 5<5 ❌
  * so right=2
* left=0, right=2

  * mid=1 → arr[1]=3
  * 3<5 ✅ → left=2
* left=2, right=2 stop

Answer = 2 ✅ (k found at index 2)

---

### Dry run 2

`arr = [1, 3, 5, 6], k = 2`

left=0, right=4

* mid=2 → arr[2]=5

  * 5<2 ❌ → right=2
* left=0, right=2

  * mid=1 → arr[1]=3
  * 3<2 ❌ → right=1
* left=0, right=1

  * mid=0 → arr[0]=1
  * 1<2 ✅ → left=1
    stop

Answer = 1 ✅ (insert at index 1)

---

### Dry run 3

`arr = [2, 6, 7, 10, 14], k = 15`

left=0, right=5

* mid=2 → arr[2]=7 <15 ✅ → left=3
* left=3, right=5

  * mid=4 → arr[4]=14 <15 ✅ → left=5
    stop

Answer = 5 ✅ (insert at end)

---

## 3. Python codes (brute + optimized)

### 3.1 Brute force (easy, but O(n))

Scan from left until you find `>= k`.

```python
class Solution:
    def searchInsertK_bruteforce(self, arr, k):
        """
        Brute force:
        - Find first index where arr[i] >= k.
        - If not found, return n.

        Time:  O(n)
        Space: O(1)
        """
        for i, value in enumerate(arr):
            if value >= k:
                return i
        return len(arr)
```

---

### 3.2 Optimized Binary Search (expected in interviews) — O(log n)

```python
class Solution:
    def searchInsertK(self, arr, k):
        """
        Binary Search (Lower Bound):
        Return the first index i such that arr[i] >= k.
        If all elements < k, returns n.

        Time:  O(log n)
        Space: O(1)
        """
        n = len(arr)

        # Search in [left, right) => right is n (not n-1)
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < k:
                # k must be to the right of mid
                left = mid + 1
            else:
                # arr[mid] >= k, possible answer -> move left side
                right = mid

        # left is the first position where arr[left] >= k, or n if none
        return left
```

---

### 3.3 Alternative optimized (classic binary search with answer variable)

Some interviewers like this explicit “store answer” style.

```python
class Solution:
    def searchInsertK_alt(self, arr, k):
        """
        Another binary search style using an 'answer' variable.

        Time:  O(log n)
        Space: O(1)
        """
        left, right = 0, len(arr) - 1
        answer = len(arr)  # default insert at end

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] >= k:
                answer = mid          # candidate position
                right = mid - 1       # try to find earlier position
            else:
                left = mid + 1

        return answer
```

---

## 4. Interview: How to remember quickly + expected Q&A

### Fast memory trick (30 seconds)

Just remember:

> **“This is lower_bound.”**
> **“Find first index where value ≥ k.”**

And the loop:

* if `arr[mid] < k` → go right
* else → go left (keep candidate)

### 5-line pseudo recall

```text
left=0, right=n
while left<right:
  mid=(left+right)//2
  if arr[mid] < k: left=mid+1
  else: right=mid
return left
```

---

### Common interviewer questions & best answers

**Q1. Why not return -1 when not found?**
**A:** Problem asks for the index where `k` should be inserted to keep sorted order, so we return the insert position (lower bound), not -1.

---

**Q2. What does your algorithm return if k is larger than all elements?**
**A:** It returns `n`, meaning insert at the end.

---

**Q3. What is “lower bound”?**
**A:** The smallest index `i` such that `arr[i] >= k`. If none exists, it’s `n`.

---

**Q4. Complexity?**
**A:** Binary search takes `O(log n)` time and `O(1)` extra space.

---

**Q5. What changes if duplicates are allowed?**
**A:** This exact algorithm still works and returns the **first occurrence** position (leftmost insert point). That’s the standard definition of lower bound.

---

---

## 5. Real-World Use Cases (few, very relatable)

1. **Maintaining a Sorted Leaderboard / Rankings**

   * You keep scores sorted.
   * When a new score `k` arrives, you need the index where it should be inserted to keep the order.
   * This is exactly “search insert position”.

2. **Order Book in Trading (Bid/Ask levels)**

   * Price levels are stored sorted.
   * When a new price level comes in, you find its insertion position fast (`O(log n)`), then insert/update.

3. **Database Indexing / Autocomplete Suggestions**

   * Many systems store keys/words in sorted order.
   * To insert a new key while keeping order, you first find the correct index using binary search (lower bound).

---

## 6. Full Python Program (with timing + inline time/space comments)

This program:

* Reads input array and `k`
* Runs optimized binary search (lower bound)
* Prints the index
* Prints runtime using `time.perf_counter()`

```python
import time
from typing import List


class Solution:
    def searchInsertK(self, arr: List[int], k: int) -> int:
        """
        Return the index of k if present, else the insertion index to keep array sorted.
        This is the classic LOWER_BOUND:
            first index i such that arr[i] >= k

        Complexity:
            Time:  O(log n)  (binary search)
            Space: O(1)
        """
        n = len(arr)

        # Search on range [left, right) (right is exclusive)
        # Time: O(1), Space: O(1)
        left, right = 0, n

        # Binary search loop runs O(log n) times
        while left < right:
            # mid computation: O(1)
            mid = (left + right) // 2

            if arr[mid] < k:
                # k must be to the right side
                left = mid + 1
            else:
                # arr[mid] >= k, mid could be answer -> shrink right
                right = mid

        # left is the insertion position (or exact index if arr[left]==k)
        return left


def main():
    """
    Input format (simple):
        n
        arr elements (space-separated)
        k

    Example Input:
        4
        1 3 5 6
        5

    Example Output:
        Insert/Found index: 2
        Total elapsed time (seconds): 0.0000xx
    """

    print("Enter n:")
    n = int(input().strip())

    print(f"Enter {n} sorted distinct integers:")
    arr = list(map(int, input().split()))
    arr = arr[:n]  # defensive trim

    print("Enter k:")
    k = int(input().strip())

    solver = Solution()

    # Start timing JUST before algorithm
    start_time = time.perf_counter()

    # Core computation: O(log n) time, O(1) space
    index = solver.searchInsertK(arr, k)

    # Stop timing right after
    end_time = time.perf_counter()

    print("\nInsert/Found index:", index)
    print(f"Total elapsed time (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

### Sample Run (Output Illustration)

Input:

```text
4
1 3 5 6
2
```

Output:

```text
Insert/Found index: 1
Total elapsed time (seconds): 0.0000xx
```

