
---

## ✅ Full Python Program

```python
class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):
        from collections import Counter

        # Step 1: Count frequency of each element in array 'a'
        freq = Counter(a)  # Time: O(n), Space: O(n), where n = len(a)

        # Step 2: For each element in array 'b', check and consume from freq map
        for num in b:  # Time: O(m), where m = len(b)
            if freq[num] == 0:
                return False  # Element missing or already consumed
            freq[num] -= 1  # Use one occurrence of that element

        return True  # All elements in b[] are accounted for in a[]
```

---

## 🧪 Driver Code

```python
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    a1 = [11, 1, 13, 21, 3, 7]
    b1 = [11, 3, 7, 1]
    print("a:", a1)
    print("b:", b1)
    print("Output:", sol.isSubset(a1, b1))  # Expected: True

    # Test Case 2
    a2 = [1, 2, 3, 4, 5]
    b2 = [1, 2, 6]
    print("\na:", a2)
    print("b:", b2)
    print("Output:", sol.isSubset(a2, b2))  # Expected: False

    # Test Case 3 (duplicates)
    a3 = [2, 2, 3, 4]
    b3 = [2, 2, 3]
    print("\na:", a3)
    print("b:", b3)
    print("Output:", sol.isSubset(a3, b3))  # Expected: True

    # Test Case 4 (b has more of an element than a)
    a4 = [2, 3, 2]
    b4 = [2, 2, 2]
    print("\na:", a4)
    print("b:", b4)
    print("Output:", sol.isSubset(a4, b4))  # Expected: False
```

---

## 🧠 Dry Run: Test Case 3

```python
a = [2, 2, 3, 4]
b = [2, 2, 3]
```

### Step-by-step:

1. `freq = Counter({2: 2, 3: 1, 4: 1})`
2. Loop through `b`:

   * 2 → exists → `freq[2] → 1`
   * 2 → exists → `freq[2] → 0`
   * 3 → exists → `freq[3] → 0`
3. All elements in `b` found → ✅ return `True`

---

## ⏱ Time and Space Complexity

| Step           | Time         | Space    | Notes                      |
| -------------- | ------------ | -------- | -------------------------- |
| Counter(a)     | O(n)         | O(n)     | n = length of `a`          |
| Iterate over b | O(m)         | O(1)     | m = length of `b`          |
| **Total**      | **O(n + m)** | **O(n)** | Efficient for large inputs |

---

## ✅ Output

```
a: [11, 1, 13, 21, 3, 7]
b: [11, 3, 7, 1]
Output: True

a: [1, 2, 3, 4, 5]
b: [1, 2, 6]
Output: False

a: [2, 2, 3, 4]
b: [2, 2, 3]
Output: True

a: [2, 3, 2]
b: [2, 2, 2]
Output: False
```

---
