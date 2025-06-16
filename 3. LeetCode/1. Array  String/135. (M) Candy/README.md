Here's a complete README-style explanation for **Leetcode 135 – Candy**, including a dry run and code in **Python**, **C++**, and **JavaScript** with inline comments.

---

# 🍬 Candy (Leetcode #135)

### 🔴 Difficulty: Hard

**Tags**: `Array`, `Greedy`

---

## 📘 Problem Statement

There are `n` children standing in a line.
Each child has a **rating**. You must distribute candies to children following:

1. Every child must get **at least one** candy.
2. Children with **higher rating than their neighbors** must get **more candies** than them.

Return the **minimum number of candies** required.

---

## 🧪 Examples

### Example 1:

```
Input:  ratings = [1, 0, 2]
Output: 5
Explanation: Distribute [2, 1, 2]
```

### Example 2:

```
Input:  ratings = [1, 2, 2]
Output: 4
Explanation: Distribute [1, 2, 1]
```

---

## 🧠 Greedy Strategy (Two Passes)

1. Initialize `candies[i] = 1` for all
2. Left → Right:

   * If `ratings[i] > ratings[i-1]`, then `candies[i] = candies[i-1] + 1`
3. Right → Left:

   * If `ratings[i] > ratings[i+1]`, then `candies[i] = max(candies[i], candies[i+1] + 1)`

Finally, return `sum(candies)`

---

## 🧪 Dry Run

**Input:** `[1, 0, 2]`

### Step 1: Init → `[1, 1, 1]`

**Left to Right**:

* i=1: 0 < 1 → no change
* i=2: 2 > 0 → `candies[2] = 2` → `[1, 1, 2]`

**Right to Left**:

* i=1: 0 < 2 → no change
* i=0: 1 > 0 → `candies[0] = max(1, 1+1) = 2` → `[2, 1, 2]`

✅ Total = `2 + 1 + 2 = 5`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candies(n, 1);

        // Left to right
        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i - 1])
                candies[i] = candies[i - 1] + 1;
        }

        // Right to left
        for (int i = n - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1])
                candies[i] = max(candies[i], candies[i + 1] + 1);
        }

        return accumulate(candies.begin(), candies.end(), 0);
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    const n = ratings.length;
    const candies = Array(n).fill(1);

    // Left to right
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    // Right to left
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
    }

    return candies.reduce((a, b) => a + b);
};
```

---

## ✅ Summary

| Metric           | Value           |
| ---------------- | --------------- |
| Time Complexity  | `O(n)`          |
| Space Complexity | `O(n)`          |
| Method           | Greedy Two-Pass |

---

