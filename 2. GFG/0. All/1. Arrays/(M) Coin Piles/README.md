
---

# 🪙 Coin Piles — Minimize Coins Removed to Satisfy Difference Constraint

**Difficulty:** Medium
**Expected Time:** 20 minutes
**Expected Time Complexity:** `O(n log n)`
**Expected Auxiliary Space:** `O(1)`

---

## 📘 Problem Statement

You are given an integer array `arr[]` where each element represents the number of coins in a pile. You are also given an integer `k`.

Your task is to **remove the minimum number of coins** such that for any two piles `i` and `j` in the final configuration:

```
|arr[i] - arr[j]| ≤ k
```

You can remove:

* Any number of coins from any pile, OR
* Entire piles (i.e., delete all coins in that pile).

---

## 🧠 Key Insight

If the piles are **sorted**, and we fix a pile height `arr[i]` as the reference (after sorting), we want:

* All piles before `i` to be **removed entirely**.
* All piles after `arr[i] + k` to be **reduced** to `arr[i] + k`.

This way, all remaining piles will lie in range `[arr[i], arr[i] + k]`, so their difference is at most `k`.

---

## 🧪 Examples

### Example 1:

**Input:**
`arr = [2, 2, 2, 2], k = 0`
**Output:** `0`
**Explanation:**
All piles already have the same number of coins → difference = 0 ≤ k.

---

### Example 2:

**Input:**
`arr = [1, 5, 1, 2, 5, 1], k = 3`
**Output:** `2`
**Explanation:**
Remove one coin from each of the two piles containing 5 → now all values are within difference ≤ 3.

---

## 📉 Constraints

* `1 ≤ arr.length ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^6`

---

## 🔍 Tags

* Arrays
* Greedy
* Binary Search
* Two-pointer algorithm
* Data Structures

---

## ✅ Optimal Approach (Two-Pointer + Prefix Sum)

1. **Sort** the array
2. Build a **prefix sum** array
3. For each `i`, fix `arr[i]` as the **lower bound** of acceptable range
4. Using binary search or two-pointer, find the rightmost pile such that `arr[j] ≤ arr[i] + k`
5. Cost to:

   * Remove all piles before `i`: `prefix[i]`
   * Reduce piles after `j`: `sum[j+1 to n-1] - (n - j - 1) * (arr[i] + k)`
6. Track the **minimum cost** over all valid `i`

---

## 🔢 Python Code

```python
class Solution:
    def minimumCoins(self, arr, k):
        # code here
        # Step 1: Sort the coin values
        arr.sort()

        # Step 2: Prepare prefix sum array
        n = len(arr)
        pre = [0]
        for x in arr:
            pre.append(pre[-1] + x)

        # Step 3: Initialize result with the sum of all coins
        res = pre[-1]
        j = 0

        # Step 4: Try each coin as base value to compare others with
        for i in range(n):
            # Move j forward until arr[j] > arr[i] + k
            while j < n and arr[j] <= arr[i] + k:
                j += 1

            # Calculate cost to reduce all coins greater than arr[i]+k
            if j < n:
                large = pre[-1] - pre[j] - (n - j) * (arr[i] + k)
            else:
                large = 0

            # Total cost = sum of smaller/equal values + cost to reduce big ones
            res = min(res, pre[i] + large)

        return res
```

---

## 🔁 Dry Run (Grid Style)

For `arr = [1, 5, 1, 2, 5, 1]`, `k = 3`

| Step | Sorted Array   | Prefix Sum         | i | arr\[i] | arr\[i] + k | j (upper bound) | Coins Removed                |
| ---- | -------------- | ------------------ | - | ------- | ----------- | --------------- | ---------------------------- |
| 0    | \[1,1,1,2,5,5] | \[0,1,2,3,5,10,15] | 0 | 1       | 4           | 4               | 3 (left) + (15-10) - 2×4 = 2 |
| 1    | ...            | ...                | 1 | 1       | 4           | 4               | same → 2                     |
| ...  | ...            | ...                |   |         |             |                 |                              |

---

## 💬 Related Interview Problems

* Remove elements from array to satisfy a range condition (Amazon)
* Minimize cost/coins under difference constraint (Microsoft, Meta)

---

Here’s the **correct and optimized solution** for the "Minimum Coins to Equalize Piles with Difference ≤ k" problem, implemented in **Python**, **C++**, and **JavaScript**, with inline comments.

---

## ✅ README Format

### 📘 Problem Summary

You are given an array `arr[]` of integers (coin piles), and a number `k`.
You can remove **any number of coins** from the piles.
Your goal:
Minimize the **total coins removed**, such that for **any two piles**, the **absolute difference ≤ k**.

---

### 🧠 Approach

1. **Sort** the array.
2. Use a **prefix sum** array to get total removed coins for smaller elements.
3. Use **two-pointers** to find the cutoff point where the difference exceeds `k`.
4. For each base value `A[i]`, calculate:

   * Remove all coins before `i`: `pre[i]`
   * Reduce all coins after `A[i] + k`: use prefix sum
5. Track the **minimum** total coins removed.

---

### 🔁 Dry Run Example

Input:

```
arr = [1, 5, 1, 2, 5, 1], k = 3
```

Sorted → `[1, 1, 1, 2, 5, 5]`
Prefix Sum → `[0, 1, 2, 3, 5, 10, 15]`

For base A\[i]=1 (i=0):

* Upper bound `A[i]+k = 4`, j=4 (A\[j]=5)
* Left sum: `pre[0] = 0`, Right adjustment: `(15 - 10) - 2×4 = -3`
* Total = `0 + 0 = 0`

Try for all `i`; minimum becomes **2**

---

## 🐍 Python Code

```python
class Solution:
    def minimumCoins(self, A, k):
        A.sort()
        n = len(A)
        pre = [0]
        for x in A:
            pre.append(pre[-1] + x)

        res = pre[-1]
        j = 0

        for i in range(n):
            while j < n and A[j] <= A[i] + k:
                j += 1
            large = pre[-1] - pre[j] - (n - j) * (A[i] + k) if j < n else 0
            res = min(res, pre[i] + large)

        return res
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int minimumCoins(vector<int>& A, int k) {
        sort(A.begin(), A.end());
        int n = A.size();
        vector<long long> pre(n + 1, 0);

        for (int i = 0; i < n; ++i)
            pre[i + 1] = pre[i] + A[i];

        long long res = pre[n];
        int j = 0;

        for (int i = 0; i < n; ++i) {
            while (j < n && A[j] <= A[i] + k)
                j++;

            long long large = (j < n) ? (pre[n] - pre[j] - 1LL * (n - j) * (A[i] + k)) : 0;
            res = min(res, pre[i] + large);
        }

        return res;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    minimumCoins(A, k) {
        A.sort((a, b) => a - b);
        const n = A.length;
        const pre = [0];

        for (let i = 0; i < n; i++) {
            pre.push(pre[pre.length - 1] + A[i]);
        }

        let res = pre[n];
        let j = 0;

        for (let i = 0; i < n; i++) {
            while (j < n && A[j] <= A[i] + k) j++;

            let large = (j < n) ? (pre[n] - pre[j] - (n - j) * (A[i] + k)) : 0;
            res = Math.min(res, pre[i] + large);
        }

        return res;
    }
}
```

---
