To solve the **Split Array Largest Sum** problem, we use **Binary Search** on the answer space combined with a **greedy validation** function.

---

### ✅ Problem Overview

**Goal:**
Split an array into `K` non-empty **contiguous** subarrays such that the **maximum subarray sum** among the `K` parts is **minimized**.

---

### 🔍 Dry Run (Example 1)

**Input:**
`arr = [1, 2, 3, 4]`, `K = 3`

**Optimal Split:**

* Split as `[1, 2]`, `[3]`, `[4]`
* Subarray sums = 3, 3, 4 → max = 4 ✅

---

### 💡 Key Idea: Binary Search + Greedy

**Why binary search?**
The answer lies between:

* **low = max(arr)** → can't have a split smaller than largest number
* **high = sum(arr)** → max possible when 1 subarray

We do binary search on this range and check feasibility.

#### 🧪 Feasibility Check:

* Try splitting array with current `mid` as max sum per part.
* If you need more than `K` parts → too small → search higher.
* Else → try lower.

---

### ✅ Python Implementation

```python
class Solution:
    def splitArray(self, arr, N, K):
        def isValid(mid):
            subarrays = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > mid:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return subarrays <= K

        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
```

---

### ✅ C++ Implementation

```cpp
class Solution {
  public:
    bool isValid(int arr[], int n, int k, int mid) {
        int subarrays = 1, curr_sum = 0;
        for (int i = 0; i < n; ++i) {
            if (curr_sum + arr[i] > mid) {
                subarrays++;
                curr_sum = arr[i];
            } else {
                curr_sum += arr[i];
            }
        }
        return subarrays <= k;
    }

    int splitArray(int arr[], int N, int K) {
        int low = *max_element(arr, arr + N);
        int high = accumulate(arr, arr + N, 0);
        int result = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isValid(arr, N, K, mid)) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return result;
    }
};
```

---

### ✅ JavaScript Implementation

```javascript
class Solution {
    splitArray(arr, N, K) {
        const isValid = (mid) => {
            let count = 1, curr_sum = 0;
            for (let num of arr) {
                if (curr_sum + num > mid) {
                    count++;
                    curr_sum = num;
                } else {
                    curr_sum += num;
                }
            }
            return count <= K;
        };

        let low = Math.max(...arr), high = arr.reduce((a, b) => a + b), result = high;

        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (isValid(mid)) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return result;
    }
}
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(N \* log(sum))
* **Space:** O(1)

# 29 June 2025

Here is the complete README-style markdown for the **"Split Array Largest Sum"** problem based on the image:

---

# Problem: Split Array Largest Sum

**Difficulty:** Hard
**Accuracy:** 58.9%
**Submissions:** 52K+
**Points:** 8

---

## 🧩 Problem Statement

Given an array `arr[]` and an integer `k`, divide the array into **k contiguous subarrays** such that the **maximum sum among these subarrays is minimized**. Find this **minimum possible maximum sum**.

---

## 🧪 Examples

### Example 1:

```
Input: arr[] = [1, 2, 3, 4], k = 3  
Output: 4  
Explanation: Optimal split is [1, 2], [3], [4].  
Maximum sum of all subarrays is 4, which is the minimum possible for 3 splits.
```

### Example 2:

```
Input: arr[] = [1, 1, 2], k = 2  
Output: 2  
Explanation: Splitting the array as [1, 1] and [2] is optimal.  
This results in a maximum sum subarray of 2.
```

---

## 📌 Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^4`

---

## 📈 Expected Complexities

* **Time Complexity:** O(n \* log(sum))
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

* Google

---

## 🏷️ Topic Tags

* Arrays
* Binary Search
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Split The Given Array Into K Sub Arrays Such That Maximum Sum Of All Sub Arrays Is Minimum](https://practice.geeksforgeeks.org/problems/split-the-array/)

---

Here’s a complete breakdown for the **Split Array Largest Sum** problem:

---

### ✅ 1. Text Explanation with Step-by-Step Dry Run

#### 🔹 Problem Summary:

You are given an array `arr[]` and an integer `k`. Divide the array into `k` **contiguous** subarrays such that the **maximum sum** among those `k` subarrays is **minimized**. Return that **minimum possible maximum sum**.

#### 🔹 Idea:

* Use **binary search** on the answer space.
* Minimum possible value = max element (we can’t split smaller than this).
* Maximum possible value = sum of all elements (1 subarray).
* Use a **greedy check** to see whether a given mid value can allow the array to be split into ≤ `k` subarrays with max sum ≤ mid.

---

### ✅ Step-by-Step Dry Run

#### Example:

```python
arr = [1, 2, 3, 4, 5], k = 2
```

**Binary Search Space:**

* Low = max(arr) = 5
* High = sum(arr) = 15

**Mid = (5 + 15)//2 = 10**

👉 Can we split into ≤ 2 parts such that max sum ≤ 10?

* First subarray: \[1, 2, 3, 4] → sum = 10
* Second subarray: \[5] → sum = 5

✅ Yes! Try lower → `high = 10`

---

**Mid = (5 + 10)//2 = 7**

👉 Try with max sum = 7

* \[1, 2, 3] = 6 ✅
* \[4] = 4 ✅
* \[5] = 5 ✅
  Too many splits → ❌

Try higher → `low = 8`

---

**Mid = 9**

* \[1, 2, 3] = 6 ✅
* \[4, 5] = 9 ✅
  2 splits ✅

Try lower → `high = 9`

---

**Mid = 8**

* \[1, 2, 3] = 6 ✅
* \[4] = 4 ✅
* \[5] = 5 ✅
  Too many splits → ❌

Try higher → `low = 9`

---

Now, `low == high == 9` → ✅ **Answer = 9**

---

### ✅ 2. Code in Python, C++, JavaScript with Explanation

---

#### ✅ Python

```python
class Solution:
    def splitArray(self, arr, k):
        def isValid(mid):
            count = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k

        low = max(arr)
        high = sum(arr)
        while low < high:
            mid = (low + high) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

---

#### ✅ C++

```cpp
class Solution {
  public:
    bool isValid(vector<int>& arr, int k, int mid) {
        int count = 1, curr_sum = 0;
        for (int num : arr) {
            if (curr_sum + num > mid) {
                count++;
                curr_sum = num;
            } else {
                curr_sum += num;
            }
        }
        return count <= k;
    }

    int splitArray(vector<int>& arr, int k) {
        int low = *max_element(arr.begin(), arr.end());
        int high = accumulate(arr.begin(), arr.end(), 0);

        while (low < high) {
            int mid = (low + high) / 2;
            if (isValid(arr, k, mid))
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
};
```

---

#### ✅ JavaScript

```javascript
class Solution {
    splitArray(arr, k) {
        const isValid = (mid) => {
            let count = 1, curr_sum = 0;
            for (let num of arr) {
                if (curr_sum + num > mid) {
                    count++;
                    curr_sum = num;
                } else {
                    curr_sum += num;
                }
            }
            return count <= k;
        };

        let low = Math.max(...arr);
        let high = arr.reduce((a, b) => a + b, 0);

        while (low < high) {
            let mid = Math.floor((low + high) / 2);
            if (isValid(mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
```

---

### ✅ 3. Expected Interview Questions & Answers

| **Question**                                         | **Answer**                                                                                               |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| What is the brute-force way to solve this?           | Try all possible ways to split the array into `k` parts and take min of max sum – O(2^n) – not feasible. |
| Why use binary search?                               | We are minimizing the *maximum sum*. This gives a **monotonic function** – use binary search on answer.  |
| What’s the binary search range?                      | \[max(arr), sum(arr)]                                                                                    |
| What is the role of the greedy `isValid()` function? | It tells us if a given max sum (`mid`) can be used to split into ≤ `k` parts.                            |
| Can the array have negative numbers?                 | Not for this problem – constraints say `1 ≤ arr[i]`.                                                     |
| What’s the time complexity?                          | `O(n * log(sum))`, where `sum` = sum of all elements.                                                    |
| Can we do it in-place?                               | Yes, constant space besides input array.                                                                 |

---
