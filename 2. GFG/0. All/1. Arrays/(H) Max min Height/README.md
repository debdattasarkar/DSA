
---

# 📈 Max Min Height

**Difficulty**: Hard
**Accuracy**: 62.86%
**Submissions**: 17K+
**Points**: 8

---

## 🧩 Problem Statement

Given a garden with **n** flowers planted in a row, represented by an array `arr[]`, where `arr[i]` denotes the height of the `iᵗʰ` flower.
You will water them for `k` days. In one day, you can water `w` continuous flowers.
Whenever you water a flower, its **height increases by 1 unit**.

You have to **maximize the minimum height** of all flowers **after** `k` days of watering.

---

## 🔍 Examples

### Example 1:

```
Input:  arr[] = [2, 3, 4, 5, 1], k = 2, w = 2
Output: 2

Explanation:
The minimum height after watering is 2.
Day 1: Water the last two flowers  -> arr becomes [2, 3, 4, 6, 2]
Day 2: Water the last two flowers  -> arr becomes [2, 3, 4, 7, 3]
```

### Example 2:

```
Input:  arr[] = [5, 8], k = 5, w = 1
Output: 9

Explanation:
The minimum height after watering is 9.
Day 1 - Day 4: Water the first flower   -> arr becomes [9, 8]
Day 5:         Water the second flower  -> arr becomes [9, 9]
```

---

## ✅ Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ w ≤ arr.size()`
* `1 ≤ k ≤ 10^9`
* `1 ≤ arr[i] ≤ 10^9`

---

## 🧠 Expected Complexities

* **Time Complexity**: `O(n * log m)`
* **Auxiliary Space**: `O(n)`

---

## 🏷️ Tags

* Arrays
* Dynamic Programming
* Binary Search
* Data Structures
* Algorithms

---

## 🏢 Company Tags

> No explicit company tags provided in this snapshot.

---

## 📚 Related Articles

* [Maximizing Smallest Flower Height In Garden With Watering Constraint](#)

---

### ✅ 1. Text Explanation + Step-by-Step Dry Run

#### 🧠 **Problem Summary**

You are given:

* An array `arr[]` representing initial flower heights.
* `k` days to water the flowers.
* `w` is the width of a watering operation: each day you can increase the height of `w` **contiguous** flowers by **1**.

You need to **maximize the minimum height** of all flowers after `k` days.

---

### 🧩 **Approach**: Binary Search + Greedy Simulation

#### 💡 Idea:

Use **binary search** on the answer space to find the **maximum minimum height** you can achieve within `k` watering operations.

* Set `low = min(arr)` and `high = max(arr) + k`
* For each `mid` value in binary search, check if it is possible to bring all flowers to **at least** `mid` height with ≤ `k` operations.

#### 🛠️ How to check if a given height is achievable?

Use a greedy strategy + **difference array** for efficient range updates.

---

### 🔍 Dry Run

Example:
`arr = [2, 3, 4, 5, 1], k = 2, w = 2`

#### Binary Search Range: low = 1, high = 1e9+2

Try `mid = 2`:
We need to make all elements ≥ 2.

* Position 0: already ≥ 2 → skip
* Position 1: already ≥ 2 → skip
* Position 2: already ≥ 2 → skip
* Position 3: already ≥ 2 → skip
* Position 4: 1 < 2 → need to add 1 at \[4,5) → affects \[4] & \[5 invalid]

Total water used = 1 ≤ k = 2 → **valid**

Try `mid = 3`:
Now positions \[0, 1, 2, 3, 4] need more water
→ total water needed exceeds `k` → **invalid**

So max min height = **2**

---

### ✅ 2. Code Implementations

---

### ✅ Python

```python
class Solution():
    def maxMinHeight(self, arr, k, w):
        def is_possible(min_height):
            n = len(arr)
            water = [0] * (n + 1)
            ops = 0
            curr_add = 0

            for i in range(n):
                curr_add += water[i]
                actual_height = arr[i] + curr_add
                if actual_height < min_height:
                    needed = min_height - actual_height
                    ops += needed
                    if ops > k:
                        return False
                    curr_add += needed
                    if i + w < len(water):  # 🔧 fix to avoid index error
                        water[i + w] -= needed
            return True

        low, high = min(arr), max(arr) + k
        result = low

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
```

---

### 🧠 3. Interview Questions & Expected Answers

| **Question**                                    | **Expected Answer**                                                                                                    |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| How did you decide the range for binary search? | The min possible height is `min(arr)`, and the max is `max(arr) + k` since we can increase any element by at most `k`. |
| Why did you use a difference array?             | It allows efficient O(1) range updates to simulate watering without modifying the entire subarray repeatedly.          |
| What's the time complexity?                     | O(n log m), where `m` is the difference between max and min height + k.                                                |
| Could you do this without binary search?        | A brute-force approach would be O(n \* maxHeight) and not feasible for large inputs.                                   |
| Can you simulate without difference array?      | Yes, but with O(nw) time per binary check, which becomes inefficient.                                                  |

---

