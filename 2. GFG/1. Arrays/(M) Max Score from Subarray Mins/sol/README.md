
---

## ✅ Full Python Program with Comments and Timing

```python
import time

class Solution:
    def maxSum(self, arr):
        # Initialize max with the smallest possible value
        ans = float('-inf')  # Time: O(1), Space: O(1)

        # Traverse the array up to second last element
        for i in range(len(arr) - 1):  # Time: O(n-1) ≈ O(n)
            # Sum current and next element
            pair_sum = arr[i] + arr[i + 1]  # Time: O(1), Space: O(1)

            # Update max if current pair sum is greater
            if pair_sum > ans:
                ans = pair_sum  # Time: O(1), Space: O(1)

        return ans  # Return final result — Time: O(1), Space: O(1)
```

---

## 🧪 Driver Code with Input, Output, and Execution Time

```python
if __name__ == "__main__":
    start_time = time.time()

    # Input values
    arr = [4, 2, 1, 10, 23, 3, 1, 0, 20]

    # Create object and compute result
    sol = Solution()
    result = sol.maxSum(arr)

    # Output result
    print("Maximum sum of any two consecutive elements:", result)

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.8f} seconds")
```

---

## ✅ Sample Output

```
Maximum sum of any two consecutive elements: 33
Execution Time: 0.00000453 seconds
```

---

## 📊 Time and Space Complexity Summary

Let **n** be the number of elements in the array:

| Operation                          | Time Complexity | Space Complexity | Notes                              |
| ---------------------------------- | --------------- | ---------------- | ---------------------------------- |
| Loop through array (`n - 1` times) | O(n)            | O(1)             | Only one max value is stored       |
| Pairwise sum and comparison        | O(1)            | O(1)             | Constant time for each comparison  |
| **Total**                          | **O(n)**        | **O(1)**         | Linear scan, constant memory usage |

---

## ✅ Interview Insight

This is a common warm-up or sliding window introduction question.
It’s also a precursor to more complex problems like:

* Max subarray sum (Kadane’s Algorithm)
* Sliding window maximum
* k-group subarray sums
