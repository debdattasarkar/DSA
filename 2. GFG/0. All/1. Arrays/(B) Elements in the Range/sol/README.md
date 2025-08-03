
---

## ✅ Problem Summary

Given an array `arr[]` of size `n` and two integers `A` and `B`, check whether **all integers in the inclusive range `[A, B]`** are present in the array.

---

## ✅ Full Python Program

```python
class Solution:
    def check_elements(self, arr, n, A, B):
        # Step 1: Store all array elements in a set for O(1) lookups
        elements = set(arr)  # Time: O(n), Space: O(n)

        # Step 2: Iterate from A to B and check each element in the set
        for x in range(A, B + 1):  # Time: O(B - A + 1)
            if x not in elements:  # Lookup is O(1)
                return False  # If any number is missing, return False
        return True  # All numbers in [A, B] are present


# 🔽 Driver Code to Test
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    arr1 = [1, 4, 5, 2, 7, 8, 3]
    n1 = len(arr1)
    A1, B1 = 2, 5
    print("Input:", arr1, "| Range:", A1, "-", B1)
    print("Output:", sol.check_elements(arr1, n1, A1, B1))  # Expected: True

    # Test Case 2
    arr2 = [1, 4, 5, 2, 7, 8, 3]
    n2 = len(arr2)
    A2, B2 = 2, 6
    print("\nInput:", arr2, "| Range:", A2, "-", B2)
    print("Output:", sol.check_elements(arr2, n2, A2, B2))  # Expected: False
```

---

## 🧠 Explanation with Dry Run

### Input:

```python
arr = [1, 4, 5, 2, 7, 8, 3]
A = 2
B = 5
```

### Step-by-Step:

1. `elements = {1, 2, 3, 4, 5, 7, 8}`
2. Range to check: `2, 3, 4, 5`
3. All these values exist in `elements` → ✅ `return True`

---

## ⏱️ Time and Space Complexity

| Step                               | Time             | Space    |
| ---------------------------------- | ---------------- | -------- |
| Build set from `arr`               | O(n)             | O(n)     |
| Check for presence from `A` to `B` | O(B - A + 1)     | O(1)     |
| **Total**                          | **O(n + (B-A))** | **O(n)** |

---

## ✅ Sample Output

```
Input: [1, 4, 5, 2, 7, 8, 3] | Range: 2 - 5
Output: True

Input: [1, 4, 5, 2, 7, 8, 3] | Range: 2 - 6
Output: False
```

---
