Here's a well-structured README based on the "Dice Throw" problem:

---

# 🎲 Dice Throw

## Problem Statement

Given `n` dice each with `m` faces, determine the number of ways to get a sum of `x` (the summation of values on each face) when all the dice are thrown.

---

## 🧠 Explanation

This is a classic **Dynamic Programming** problem where we try to count the number of ways to reach a target sum using dice rolls.

Let `dp[i][j]` be the number of ways to get sum `j` using `i` dice.

### Recurrence Relation:

```
dp[i][j] = dp[i-1][j-k] for all k in range(1, m+1) if j-k >= 0
```

### Base Case:

```
dp[0][0] = 1  # 1 way to reach 0 sum with 0 dice
```

---

## 💡 Examples

### Example 1:

**Input:**

```
m = 6, n = 3, x = 12
```

**Output:**

```
25
```

**Explanation:**
There are 25 total ways to get the sum 12 using 3 dice with faces from 1 to 6.

---

### Example 2:

**Input:**

```
m = 2, n = 3, x = 6
```

**Output:**

```
1
```

**Explanation:**
Only one combination gives sum 6: all dice landing on 2.

---

## 📊 Constraints

* 1 ≤ m, n, x ≤ 50

---

## 🧮 Expected Complexities

* Time Complexity: **O(m \* n \* x)**
* Space Complexity: **O(x)**

---

## 🧪 Dry Run

For `m=2`, `n=2`, `x=4`:

* All combinations:

  * \[1,3], \[3,1], \[2,2]
* So total ways = **3**

---

## 🧑‍💻 Code Snippets

### Python

```python
class Solution:
    def findWays(self, m, n, x):
        dp = [[0] * (x+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for dice in range(1, n+1):
            for target in range(1, x+1):
                for face in range(1, m+1):
                    if target - face >= 0:
                        dp[dice][target] += dp[dice-1][target - face]
        return dp[n][x]
```

---

### C++

```cpp
class Solution {
public:
    int findWays(int m, int n, int x) {
        vector<vector<int>> dp(n+1, vector<int>(x+1, 0));
        dp[0][0] = 1;
        
        for (int dice = 1; dice <= n; ++dice) {
            for (int target = 1; target <= x; ++target) {
                for (int face = 1; face <= m; ++face) {
                    if (target - face >= 0)
                        dp[dice][target] += dp[dice-1][target-face];
                }
            }
        }
        return dp[n][x];
    }
};
```

---

### JavaScript

```javascript
class Solution {
    findWays(m, n, x) {
        let dp = Array.from({length: n+1}, () => Array(x+1).fill(0));
        dp[0][0] = 1;

        for (let dice = 1; dice <= n; dice++) {
            for (let target = 1; target <= x; target++) {
                for (let face = 1; face <= m; face++) {
                    if (target - face >= 0)
                        dp[dice][target] += dp[dice-1][target-face];
                }
            }
        }
        return dp[n][x];
    }
}
```

---

## 🏷️ Tags

* Dynamic Programming
* Mathematical
* Arrays
* Algorithms

---

## 🏢 Company Tags

* Amazon
* Microsoft

---

## 📚 Related Articles

* [Dice Throw DP 30](https://www.geeksforgeeks.org/dice-throw-dp-30/)

---

Let me know if you'd like an optimized version using 1D space.
