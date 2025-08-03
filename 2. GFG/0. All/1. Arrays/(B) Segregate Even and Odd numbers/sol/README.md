
---

## ✅ Full Python Program

```python
class Solution:

    def segregateEvenOdd(self, arr):
        n = len(arr)

        # Step 1: Partition all even numbers to the front
        i = 0
        for j in range(n):
            if arr[j] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # At this point:
        # arr[0:i] → all even numbers (unordered)
        # arr[i:n] → all odd numbers (unordered)

        # Step 2: Sort both parts in-place
        arr[:i] = sorted(arr[:i])   # sort even numbers
        arr[i:] = sorted(arr[i:])   # sort odd numbers
```

---

## 🧪 Example Driver Code

```python
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    arr1 = [12, 34, 45, 9, 8, 90, 3]
    print("Original:", arr1)
    sol.segregateEvenOdd(arr1)
    print("Modified:", arr1)  # Expected: [8, 12, 34, 90, 3, 9, 45]

    # Test case 2
    arr2 = [0, 1, 2, 3, 4]
    print("\nOriginal:", arr2)
    sol.segregateEvenOdd(arr2)
    print("Modified:", arr2)  # Expected: [0, 2, 4, 1, 3]

    # Test case 3
    arr3 = [10, 22, 4, 6]
    print("\nOriginal:", arr3)
    sol.segregateEvenOdd(arr3)
    print("Modified:", arr3)  # Expected: [4, 6, 10, 22]
```

---

## 🧠 Dry Run: Example 1

### Input:

```python
arr = [12, 34, 45, 9, 8, 90, 3]
```

### Step 1: Partition

Move even numbers to the front:

```python
After partition: [12, 34, 8, 90, 9, 45, 3]
                 ↑   ↑   ↑   ↑
                 evens at indices 0 to 3 (i=4)
```

### Step 2: Sort sections

* `arr[0:4]` → sort → \[8, 12, 34, 90]
* `arr[4:]` → sort → \[3, 9, 45]

### Output:

```python
arr = [8, 12, 34, 90, 3, 9, 45]
```

---

## 📈 Time & Space Complexity

| Step                   | Time Complexity                                            | Space Complexity                  |
| ---------------------- | ---------------------------------------------------------- | --------------------------------- |
| Partition step         | O(n)                                                       | O(1) (in-place)                   |
| Sorting evens and odds | O(e log e + o log o) where e and o are even and odd counts | O(1) extra (in-place sort slices) |
| **Total**              | **O(n log n)**                                             | **O(1)**                          |

---

## ✅ Output Summary

```
Original: [12, 34, 45, 9, 8, 90, 3]
Modified: [8, 12, 34, 90, 3, 9, 45]

Original: [0, 1, 2, 3, 4]
Modified: [0, 2, 4, 1, 3]

Original: [10, 22, 4, 6]
Modified: [4, 6, 10, 22]
```

---
