Here's a complete README-style explanation and implementation for **Leetcode 134 – Gas Station**, including dry run and code in **Python**, **C++**, and **JavaScript** with inline comments.

---

# ⛽ Gas Station (Leetcode #134)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Greedy`

---

## 📘 Problem Statement

You're given two integer arrays `gas` and `cost`.

* `gas[i]`: Amount of gas at station `i`
* `cost[i]`: Gas needed to travel from station `i` to `(i + 1) % n`

Start at any gas station and travel clockwise.
Return the index of the **starting station** if you can travel the whole circuit once, otherwise return `-1`.

💡 It is **guaranteed** that **at most one solution exists**.

---

## ✅ Greedy Intuition

* If **total gas < total cost**, it's **impossible** to complete the loop → return `-1`.
* Else, there **exists a solution**, and it can be found with a **greedy approach**.

---

## 🧠 Greedy Strategy

1. Track the total balance (`total_tank`) and current balance (`curr_tank`).
2. If at any point `curr_tank < 0`, we **reset** and try starting from the next station.
3. The next valid start is the **only possible solution**.

---

## 🧪 Dry Run

**Input:** `gas = [1,2,3,4,5], cost = [3,4,5,1,2]`

| i | gas\[i] | cost\[i] | curr\_tank | total\_tank | start         |
| - | ------- | -------- | ---------- | ----------- | ------------- |
| 0 | 1       | 3        | -2         | -2          | 1     ← reset |
| 1 | 2       | 4        | -2         | -4          | 2     ← reset |
| 2 | 3       | 5        | -2         | -6          | 3     ← reset |
| 3 | 4       | 1        | 3          | -3          |               |
| 4 | 5       | 2        | 6          | 0           |               |

✅ Start from station **3**

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            # If we can't reach station i + 1
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0, curr = 0, start = 0;

        for (int i = 0; i < gas.size(); ++i) {
            int diff = gas[i] - cost[i];
            total += diff;
            curr += diff;

            if (curr < 0) {
                start = i + 1;
                curr = 0;
            }
        }

        return total >= 0 ? start : -1;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let total = 0, curr = 0, start = 0;

    for (let i = 0; i < gas.length; i++) {
        let diff = gas[i] - cost[i];
        total += diff;
        curr += diff;

        if (curr < 0) {
            start = i + 1;
            curr = 0;
        }
    }

    return total >= 0 ? start : -1;
};
```

---

## ✅ Summary

| Feature          | Value                              |
| ---------------- | ---------------------------------- |
| Time Complexity  | O(n)                               |
| Space Complexity | O(1)                               |
| Technique        | Greedy                             |
| Edge Case        | Sum(gas) < Sum(cost) → return `-1` |

---
