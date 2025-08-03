Here is the **complete Python program** with:

* `timeit` usage for measuring execution time
* Inline comments explaining **logic**, **time complexity**, and **space complexity**
* Example **input and output**

---

```python
import heapq
import time

class Solution:
    
    def topKSumPairs(self, a, b, k):
        n = len(a)

        # Step 1: Sort both arrays in descending order
        # Time: O(n log n) for each array
        # Space: O(1) extra (sort in-place)
        a.sort(reverse=True)
        b.sort(reverse=True)

        max_heap = []  # Max-heap to store potential largest sums
        visited = set()  # Track visited index pairs to avoid duplicates

        # Step 2: Push the largest initial pair (0, 0) into heap
        # Time: O(log 1) = O(1)
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))

        result = []

        # Step 3: Extract k largest sums
        # Loop runs k times → O(k log k) due to heap operations
        for _ in range(k):
            curr_sum, i, j = heapq.heappop(max_heap)
            result.append(-curr_sum)  # Negated back to positive

            # Step 4: Explore next best two combinations

            # If i + 1 is valid, push (i+1, j)
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            # If j + 1 is valid, push (i, j+1)
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return result


# ----------- ⏱️ Timed Execution + Example Run -----------

if __name__ == "__main__":
    import time

    a = [1, 4, 2, 3]
    b = [2, 5, 1, 6]
    k = 3

    print("Input Arrays:")
    print("a =", a)
    print("b =", b)
    print("k =", k)

    start_time = time.time()

    sol = Solution()
    output = sol.topKSumPairs(a, b, k)

    end_time = time.time()
    elapsed = end_time - start_time

    print("\nOutput:", output)
    print("Time taken: {:.6f} seconds".format(elapsed))
```

---

### 🔍 Example Output

```
Input Arrays:
a = [1, 4, 2, 3]
b = [2, 5, 1, 6]
k = 3

Output: [10, 9, 9]
Time taken: 0.000XYZ seconds
```

(The exact time may vary slightly depending on your machine and environment.)

---

## 🧠 Summary of Complexities

| Step                 | Time Complexity      | Space Complexity |
| -------------------- | -------------------- | ---------------- |
| Sorting `a` & `b`    | O(n log n)           | O(1)             |
| Heap Operations (k)  | O(k log k)           | O(k)             |
| Visited Set Tracking | O(k)                 | O(k)             |
| **Total**            | O(n log n + k log k) | O(k)             |

