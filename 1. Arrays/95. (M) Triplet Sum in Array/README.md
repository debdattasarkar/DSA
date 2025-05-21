Here’s the generated **README** in Markdown format for the **Triplet Sum in Array** problem from GeeksforGeeks:

---

# 🔢 Triplet Sum in Array

## 🧩 Problem Statement

Given an array `arr[]` and an integer `target`, determine whether there exists a triplet in the array whose sum equals the given target.

Return `true` if such a triplet exists, otherwise return `false`.

---

## 📘 Examples

### Example 1

**Input:**
`arr[] = [1, 4, 45, 6, 10, 8]`, `target = 13`
**Output:**
`true`
**Explanation:**
Triplet `{1, 4, 8}` adds up to 13.

---

### Example 2

**Input:**
`arr[] = [1, 2, 4, 3, 6, 7]`, `target = 10`
**Output:**
`true`
**Explanation:**
Triplets `{1, 3, 6}` and `{1, 2, 7}` both add to 10.

---

### Example 3

**Input:**
`arr[] = [40, 20, 10, 3, 6, 7]`, `target = 24`
**Output:**
`false`
**Explanation:**
No triplet sums up to 24.

---

## 🔍 Constraints

* `3 ≤ arr.length ≤ 10^3`
* `1 ≤ arr[i] ≤ 10^5`

---

## 🧠 Approach

1. **Sort** the array.
2. Iterate through the array with index `i`.
3. Use **two pointers** `left` and `right` starting from `i + 1` and `end` respectively.
4. Check if `arr[i] + arr[left] + arr[right] == target`.
5. Adjust pointers based on comparison and continue until triplet is found or pointers cross.

---

## 🔢 Dry Run

**Input:**
`arr[] = [1, 4, 45, 6, 10, 8]`, `target = 13`
**Sorted:**
`[1, 4, 6, 8, 10, 45]`

* i = 0, arr\[i] = 1
  left = 1 (arr\[left] = 4), right = 5 (arr\[right] = 45)
  1 + 4 + 45 = 50 → too big → move `right--`
  ...
  Try 1 + 4 + 8 = 13 ✅ → return `true`

---

## ⏱️ Complexity

* **Time Complexity:** O(n²)
* **Auxiliary Space:** O(1) (ignoring sort space)

---

## 💻 Python Code

```python
class Solution:
    def find3Numbers(self, A, n, X):
        A.sort()
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                total = A[i] + A[l] + A[r]
                if total == X:
                    return True
                elif total < X:
                    l += 1
                else:
                    r -= 1
        return False
```

---

## 💻 C++ Code

```cpp
class Solution {
public:
    bool find3Numbers(vector<int> A, int n, int X) {
        sort(A.begin(), A.end());
        for (int i = 0; i < n - 2; i++) {
            int l = i + 1, r = n - 1;
            while (l < r) {
                int total = A[i] + A[l] + A[r];
                if (total == X) return true;
                else if (total < X) l++;
                else r--;
            }
        }
        return false;
    }
};
```

---

## 💻 JavaScript Code

```javascript
class Solution {
    find3Numbers(arr, n, X) {
        arr.sort((a, b) => a - b);
        for (let i = 0; i < n - 2; i++) {
            let l = i + 1, r = n - 1;
            while (l < r) {
                const total = arr[i] + arr[l] + arr[r];
                if (total === X) return true;
                else if (total < X) l++;
                else r--;
            }
        }
        return false;
    }
}
```

---

## 🏷️ Tags

`two-pointer-algorithm` • `Arrays` • `Hashing` • `Sorting` • `Algorithms` • `Data Structures`

---

Here’s the detailed explanation and step-by-step dry run for the **Triplet Sum in Array** problem from GeeksforGeeks, followed by implementations in **Python**, **C++**, and **JavaScript**.

---

## 🧠 Problem Understanding

Given an array `arr[]` and an integer `target`, check if there exists **any triplet** such that the **sum of the triplet equals the target**.

---

## 🔍 Approach

1. **Sort** the array.
2. For each element `arr[i]`, use a **two-pointer** technique to find if there exists a pair `(arr[l], arr[r])` such that `arr[i] + arr[l] + arr[r] == target`.
3. Return `True` if such a triplet is found.
4. If the loop ends without finding such a triplet, return `False`.

---

## 🧪 Dry Run

### Example:

**Input:** `arr = [1, 2, 4, 3, 6, 7]`, `target = 10`

**Sorted:** `[1, 2, 3, 4, 6, 7]`

Try each index:

* i = 0 (arr\[i] = 1), l = 1, r = 5

  * 1+2+7 = 10 → ✅ Found!

**Output:** `True`

---

## 🧮 Time & Space Complexity

* **Time Complexity:** O(n²) — due to nested loop with two-pointer.
* **Space Complexity:** O(1) — no extra space used.

---

## ✅ Python Code

```python
#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        arr.sort()  # Step 1: Sort the array
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]

                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return False  # No triplet found
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    bool hasTripletSum(vector<int> &arr, int target) {
        sort(arr.begin(), arr.end()); // Step 1: Sort array
        int n = arr.size();

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = arr[i] + arr[left] + arr[right];

                if (sum == target)
                    return true;
                else if (sum < target)
                    left++;
                else
                    right--;
            }
        }

        return false; // No such triplet found
    }
};
```

---

## ✅ JavaScript Code

```javascript
// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} target
 * @returns {boolean}
 */
class Solution {
    // Function to find if there exists a triplet in the array arr[] which sums up to target
    hasTripletSum(arr, target) {
        arr.sort((a, b) => a - b); // Step 1: Sort the array
        let n = arr.length;

        for (let i = 0; i < n - 2; i++) {
            let left = i + 1;
            let right = n - 1;

            while (left < right) {
                let sum = arr[i] + arr[left] + arr[right];

                if (sum === target)
                    return true;
                else if (sum < target)
                    left++;
                else
                    right--;
            }
        }

        return false; // No triplet found
    }
}
```

---

Let me know if you’d like the driver code or sample inputs for testing.
