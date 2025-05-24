Here's the complete `README.md` file based on the **Pythagorean Triplet** problem statement from GeeksforGeeks:

---

# 🧮 Pythagorean Triplet

### Difficulty: Medium

**Accuracy**: 24.77%
**Average Time**: 20 mins
**Points**: 4

## 📝 Problem Statement

Given an array `arr[]`, determine whether there exists a **triplet (a, b, c)** such that:

$$
a^2 + b^2 = c^2
$$

where `a`, `b`, and `c` are elements of the array at **distinct indices**.

Return **`true`** if such a triplet exists, otherwise return **`false`**.

---

## 💡 Examples

### Example 1:

```text
Input: arr[] = [3, 2, 4, 6, 5]
Output: true
Explanation: a = 3, b = 4, c = 5 → 3² + 4² = 5² → 9 + 16 = 25 ✅
```

### Example 2:

```text
Input: arr[] = [3, 8, 5]
Output: false
Explanation: No Pythagorean triplet present ❌
```

### Example 3:

```text
Input: arr[] = [1, 1, 1]
Output: false
Explanation: No such combination possible ❌
```

---

## 📋 Constraints

* `1 ≤ arr.size() ≤ 10⁵`
* `1 ≤ arr[i] ≤ 10³`

---

## ⏱️ Expected Time & Space Complexity

* **Time Complexity**: `O(n + max(arr[i])²)`
* **Auxiliary Space**: `O(max(arr[i]))`

---

## ⚙️ Approach

### Step-by-Step Explanation:

1. **Square all elements** in the array.
2. **Sort** the squared elements in non-decreasing order.
3. For each element `c²` (starting from the end), use **two-pointer** approach to find two other elements `a²` and `b²` such that:

   $$
   a^2 + b^2 = c^2
   $$
4. If any such pair exists, return `true`.

### Dry Run:

For `arr = [3, 2, 4, 6, 5]`

* Squared: `[9, 4, 16, 36, 25]`
* Sorted: `[4, 9, 16, 25, 36]`
* Check if 4 + 9 = 13 ≠ 36 → continue...
* Check 9 + 16 = 25 → ✅ Found.

---

## 🧑‍💻 Function Signature

### Python

```python
class Solution:
    def checkTriplet(self, arr: list[int], n: int) -> bool:
        # Your code here
```

### C++

```cpp
class Solution {
  public:
    bool checkTriplet(int arr[], int n) {
        // Your code here
    }
};
```

### JavaScript

```javascript
class Solution {
    /**
     * @param {number[]} arr
     * @param {number} n
     * @return {boolean}
     */
    checkTriplet(arr, n) {
        // Your code here
    }
}
```

---

## 🧪 Sample Usage

```python
arr = [3, 2, 4, 6, 5]
sol = Solution()
print(sol.checkTriplet(arr, len(arr)))  # Output: True
```

---

## 🏷️ Tags

`Arrays` · `Data Structures`

---

## 🔗 Related Articles

* [Find Pythagorean Triplet In An Unsorted Array](https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/)

---

Let me know if you want code implementations with inline comments in Python, C++, or JavaScript!
