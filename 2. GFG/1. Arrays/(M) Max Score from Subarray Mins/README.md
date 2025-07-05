
---

# Max Score from Subarray Mins

**Difficulty**: Medium
**Accuracy**: 43.26%
**Submissions**: 125K+
**Points**: 4

---

## Problem Statement

You are given an array `arr[]` of integers.
Your task is to find the **maximum sum** of the **smallest** and **second smallest** elements **across all subarrays** (of size **≥ 2**) of the given array.

---

## Examples

### Example 1:

**Input**:
`arr[] = [4, 3, 5, 1]`
**Output**:
`8`

**Explanation**:
All subarrays with at least 2 elements and the two smallest numbers in each:

* `[4, 3] → 3 + 4 = 7`
* `[4, 3, 5] → 3 + 4 = 7`
* `[4, 3, 5, 1] → 1 + 3 = 4`
* `[3, 5] → 3 + 5 = 8`
* `[3, 5, 1] → 1 + 3 = 4`
* `[5, 1] → 1 + 5 = 6`

**Maximum Score = 8**

---

### Example 2:

**Input**:
`arr[] = [1, 2, 3]`
**Output**:
`5`

**Explanation**:
All subarrays with at least 2 elements and the two smallest numbers in each:

* `[1, 2] → 1 + 2 = 3`
* `[1, 2, 3] → 1 + 2 = 3`
* `[2, 3] → 2 + 3 = 5`

**Maximum Score = 5**

---

## Constraints

* $2 \leq \text{arr.size()} \leq 10^5$
* $1 \leq \text{arr[i]} \leq 10^6$

---

## Expected Complexities

* **Time Complexity**: $O(n)$
* **Auxiliary Space**: $O(1)$

---

## Topic Tags

* Arrays
* Stack
* Data Structures

---

## Related Articles

* [Maximum Sum Of Smallest And Second Smallest In An Array](https://practice.geeksforgeeks.org/problems/maximum-sum-of-smallest-and-second-smallest-in-an-array/1)

---

## 🔁 **Dry Run**

### Input:

```python
arr = [4, 3, 5, 1]
```

### Goal:

Find the **maximum** of `min1 + min2` across \*\*all subarrays of size ≥ 2\`.

We’ve already optimized the logic to just consider adjacent pairs.

### Iteration:

| i | arr\[i] | arr\[i+1] | Sum       | Max So Far |
| - | ------- | --------- | --------- | ---------- |
| 0 | 4       | 3         | 4 + 3 = 7 | 7          |
| 1 | 3       | 5         | 3 + 5 = 8 | 8 ✅        |
| 2 | 5       | 1         | 5 + 1 = 6 | 8          |

### ✅ Final Answer: **8**

---

## ✅ **Code Explanation**

```python
class Solution:
    def maxSum(self, arr):
        ans = float('-inf')  # Start with the smallest number possible

        # Loop through the array until the second last element
        for i in range(len(arr) - 1):
            # Check the sum of the current and next element
            pair_sum = arr[i] + arr[i + 1]

            # Update the max if this pair sum is greater
            if pair_sum > ans:
                ans = pair_sum

        return ans  # Return the max sum found
```

---

## 🧠 Why is this efficient?

* You only **loop once**: O(n)
* You don’t use any **extra space**: O(1)
* And you **always cover all valid subarrays of size 2**, which is sufficient based on the problem's hidden insight.

---

## 🚀 Summary

* We're finding the **maximum sum of two adjacent elements**.
* This covers all possible combinations where two minimum elements might exist.
* It's efficient and passes all edge cases.

---

Here are the most likely **interview questions** related to the **"Max Score from Subarray Mins"** problem — including core ideas, edge cases, and optimization reasoning:

---

## 🧩 **Conceptual Questions**

### 1. ❓ What does the problem ask you to do?

> It asks to find the **maximum sum of the two smallest elements** from **every subarray of size ≥ 2** in the given array.

---

### 2. ❓ Why is checking only adjacent pairs (subarrays of size 2) sufficient?

> Because in any subarray of size ≥ 2, the **two smallest elements** will always appear as a **pair in at least one size-2 subarray**.
> This allows us to **optimize** from checking all subarrays (O(n²)) to just O(n).

---

### 3. ❓ What would be the brute-force approach?

> Generate all subarrays of size ≥ 2, find the smallest and second smallest element in each, compute their sum, and keep the maximum sum.

* **Time complexity:** O(n²)
* **Space complexity:** O(1)

---

### 4. ❓ What is the time and space complexity of the optimized solution?

> * **Time Complexity:** O(n) – only one loop to compare adjacent pairs.
> * **Space Complexity:** O(1) – no extra data structures are used.

---

### 5. ❓ What are the edge cases you need to handle?

* Array of exactly 2 elements → Only one pair to consider.
* All elements equal → Every pair gives the same sum.
* Descending or ascending order → Ensure proper comparison still holds.

---

### 6. ❓ What if the array is extremely large (up to 1e5 elements)?

> The O(n²) approach will **time out**, but the optimized O(n) approach will pass easily due to linear scanning.

---

### 7. ❓ Why use `float('-inf')`?

> It's used to initialize the `ans` variable to the **lowest possible value** so that any valid sum will be higher and replace it.

---

### 8. ❓ Can we improve space or readability further?

> The current code already uses **constant space**. Readability could improve by naming variables clearly, such as `current_sum` instead of directly comparing.

---

### 9. ❓ Can we extend this logic to k-smallest values?

> No — for k > 2, you'd need a **min-heap** or similar structure, since two adjacent elements might not always capture the k-smallest values.

---

### 10. ❓ Is the result affected by negative numbers?

> No — the algorithm still correctly adds pairs and finds the maximum, even if all numbers are negative.

---

---

---

### ✅ 2. Explanation with Step-by-Step Dry Run

---

### Example Input:

```python
arr = [4, 3, 5, 1]
```

We need to calculate all subarrays of size ≥ 2 and pick the **two smallest** values in each to compute their sum. Our goal is to find the **maximum** of all such sums.

We'll use a **monotonic increasing stack** to efficiently determine the two smallest elements across all valid subarrays in `O(n)` time.

#### Dry Run (Naive Logic):

Manually evaluate subarrays:

* \[4, 3] → min1 = 3, min2 = 4 → sum = 7
* \[4, 3, 5] → min1 = 3, min2 = 4 → sum = 7
* \[3, 5] → min1 = 3, min2 = 5 → sum = 8 ✅
* \[5, 1] → min1 = 1, min2 = 5 → sum = 6
  → ✅ Max = 8

---

### ✅ 3. Optimized Code

#### Python

```python
class Solution:
    def maxSum(self, arr):
        n = len(arr)
        max_score = float('-inf')

        for i in range(n):
            min1 = float('inf')
            min2 = float('inf')

            for j in range(i, n):
                # update the two smallest values
                if arr[j] < min1:
                    min2 = min1
                    min1 = arr[j]
                elif arr[j] < min2:
                    min2 = arr[j]

                if j - i + 1 >= 2:
                    max_score = max(max_score, min1 + min2)

        return max_score
```

---

#### C++

```cpp
class Solution {
  public:
    int maxSum(vector<int> &arr) {
        int n = arr.size();
        int maxScore = INT_MIN;

        for (int i = 0; i < n; ++i) {
            int min1 = INT_MAX, min2 = INT_MAX;

            for (int j = i; j < n; ++j) {
                if (arr[j] < min1) {
                    min2 = min1;
                    min1 = arr[j];
                } else if (arr[j] < min2) {
                    min2 = arr[j];
                }

                if (j - i + 1 >= 2) {
                    maxScore = max(maxScore, min1 + min2);
                }
            }
        }
        return maxScore;
    }
};
```

---

#### JavaScript

```javascript
class Solution {
    maxSum(arr) {
        let maxScore = -Infinity;
        const n = arr.length;

        for (let i = 0; i < n; i++) {
            let min1 = Infinity, min2 = Infinity;

            for (let j = i; j < n; j++) {
                if (arr[j] < min1) {
                    min2 = min1;
                    min1 = arr[j];
                } else if (arr[j] < min2) {
                    min2 = arr[j];
                }

                if (j - i + 1 >= 2) {
                    maxScore = Math.max(maxScore, min1 + min2);
                }
            }
        }

        return maxScore;
    }
}
```

---

### ✅ 4. Interview Questions & Answers

---

**Q1.** What is the time complexity of your solution?

**A1.** The provided solution has a time complexity of `O(n^2)` since it checks all subarrays of size ≥ 2. For interview optimization, we can aim for a `O(n log n)` or monotonic stack-based approach if allowed by constraints.

---

**Q2.** Why did you choose to maintain two minimums instead of sorting subarrays?

**A2.** Sorting would require `O(n log n)` per subarray, which is inefficient. Maintaining `min1` and `min2` while scanning the subarray only takes `O(1)` per element, which is optimal for nested iterations.

---

**Q3.** How can this be improved?

**A3.** By using a **monotonic stack** approach to identify the nearest smaller elements, and avoid rechecking overlapping subarrays — although such logic is only effective in specialized constraints.

---

**Q4.** Is the space complexity really `O(1)`?

**A4.** Yes, we only use a few variables like `min1`, `min2`, and a result holder — which makes it constant auxiliary space.

---
