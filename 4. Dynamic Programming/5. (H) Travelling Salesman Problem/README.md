Here's the **detailed explanation, dry run**, and **code for the Travelling Salesman Problem (TSP)** using **Dynamic Programming + Bitmasking**, in **Python, C++ and JavaScript**, including inline comments.

---

### 🧠 Problem Overview:

Given a cost matrix `cost[i][j]` where `cost[i][j]` is the cost of traveling from city `i` to `j`, your task is to start at city `0`, visit every city exactly once, and return to city `0`, with **minimum total cost**.

---

### 👨‍🏫 Step-by-Step Explanation

We use **Dynamic Programming with Bitmasking**:

* Let `dp[mask][i]` be the **minimum cost** to reach city `i` having visited cities represented by `mask`.
* `mask` is a bitmask where the `j-th` bit is 1 if city `j` has been visited.
* We initialize with: `dp[1<<0][0] = 0` (start at city 0)
* For each `mask`, for each current city `u`, we try to go to `v` (unvisited), update cost:

```python
dp[mask | (1<<v)][v] = min(dp[mask | (1<<v)][v], dp[mask][u] + cost[u][v])
```

* Final answer is the minimum over all `dp[(1<<n)-1][i] + cost[i][0]` (return to start).

---

### ✍️ Dry Run

For `cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]]`

Cities: 0 → 1 → 2 → 0
Cost = 1000 + 1000 + 1000 = 3000

---

### ✅ Python Code

```python
class Solution:
    def tsp(self, cost):
        from functools import lru_cache
        n = len(cost)
        
        @lru_cache(None)
        def dfs(mask, pos):
            if mask == (1 << n) - 1:
                return cost[pos][0]  # return to start

            ans = float('inf')
            for city in range(n):
                if not (mask & (1 << city)):
                    ans = min(ans, cost[pos][city] + dfs(mask | (1 << city), city))
            return ans

        return dfs(1, 0)  # start at city 0, only city 0 is visited (mask=1)
```

---

### ✅ C++ Code

```cpp
class Solution {
  public:
    int tsp(vector<vector<int>>& cost) {
        int n = cost.size();
        int VISITED_ALL = (1 << n) - 1;
        vector<vector<int>> dp(1 << n, vector<int>(n, -1));

        function<int(int, int)> dfs = [&](int mask, int pos) {
            if (mask == VISITED_ALL) return cost[pos][0];
            if (dp[mask][pos] != -1) return dp[mask][pos];

            int ans = INT_MAX;
            for (int city = 0; city < n; ++city) {
                if (!(mask & (1 << city)))
                    ans = min(ans, cost[pos][city] + dfs(mask | (1 << city), city));
            }
            return dp[mask][pos] = ans;
        };

        return dfs(1, 0);
    }
};
```

---

### ✅ JavaScript Code

```javascript
class Solution {
    tsp(cost) {
        const n = cost.length;
        const VISITED_ALL = (1 << n) - 1;
        const dp = Array.from({ length: 1 << n }, () => Array(n).fill(-1));

        const dfs = (mask, pos) => {
            if (mask === VISITED_ALL) return cost[pos][0];
            if (dp[mask][pos] !== -1) return dp[mask][pos];

            let ans = Infinity;
            for (let city = 0; city < n; city++) {
                if ((mask & (1 << city)) === 0) {
                    ans = Math.min(ans, cost[pos][city] + dfs(mask | (1 << city), city));
                }
            }
            dp[mask][pos] = ans;
            return ans;
        };

        return dfs(1, 0); // Start at city 0, only 0 visited
    }
}
```

---

### 🧠 Time & Space Complexity

* **Time Complexity:** `O(2^n * n)`
* **Space Complexity:** `O(2^n * n)` for memoization table

---

Let me know if you’d like to see a visualization or example trace of how bitmasking works step-by-step!
