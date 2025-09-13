
---

# 🪙 Coin Change (Count Ways)

**Difficulty:** Medium
**Accuracy:** 43.1%
**Submissions:** 299K+
**Points:** 4
**Average Time to Solve:** 30m

---

## 🧾 Problem Statement

Given an integer array `coins[]` representing different denominations of currency and an integer `sum`, find the number of ways you can make `sum` using **different combinations** from `coins[]`.

> 📝 Note:
>
> * You have an **infinite supply** of each type of coin.
> * You can use any coin **as many times** as needed.
> * Answers are guaranteed to fit into a **32-bit integer**.

---

## 📥 Input

* `coins[]`: An array of integers (1 ≤ `coins[i]` ≤ 10⁴)
* `sum`: Target sum to achieve (1 ≤ `sum` ≤ 10³)
* `coins.size()` ≤ 10³

---

## 📤 Output

Return an integer representing the **total number of combinations** that make the sum.

---

## 🧪 Examples

### Example 1:

```
Input:
coins[] = [1, 2, 3]
sum = 4

Output:
4

Explanation:
The four combinations are:
[1,1,1,1], [1,1,2], [2,2], [1,3]
```

---

### Example 2:

```
Input:
coins[] = [2, 5, 3, 6]
sum = 10

Output:
5

Explanation:
Combinations are:
[2,2,2,2,2], [2,2,3,3], [2,2,6], [2,3,5], [5,5]
```

---

### Example 3:

```
Input:
coins[] = [5, 10]
sum = 3

Output:
0

Explanation:
All denominations are greater than 3; no combination possible.
```

---

## ✅ Constraints

* `1 ≤ sum ≤ 10³`
* `1 ≤ coins[i] ≤ 10⁴`
* `1 ≤ coins.size() ≤ 10³`

---

## 💡 Expected Time and Space Complexity

* **Time Complexity:** `O(n * sum)`
  (where `n` is the number of coins)
* **Auxiliary Space:** `O(sum)`

---

## 🏢 Company Tags

> Paytm, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft, OYO Rooms, Samsung, Snapdeal, Zoho

---

## 🧠 Topic Tags

> Arrays, Dynamic Programming, Data Structures, Algorithms

---

## 💼 Related Interview Experiences

* Accolite Interview Experience Set 15 (Campus)
* Paytm Interview Experience Set 4 (Walk-In Drive)
* Flipkart Interview Experience for SDE 1 (On Campus 2019)

---

## 📚 Related Articles

* [Coin Change DP 7 (GeeksforGeeks)](https://www.geeksforgeeks.org/coin-change-dp-7/)

---

---

Let's walk through each part of the request for the **Coin Change (Count Ways)** problem.

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### Problem Recap:

You're given:

* A list of coin denominations `coins[]`.
* A target sum `sum`.

Your goal is to find the **number of distinct combinations** (using unlimited supply of coins) that sum up to the given `sum`.

---

### Intuition:

This is a **Dynamic Programming** (unbounded knapsack) problem, where:

* You try **every coin** for every possible amount from `1` to `sum`.
* You accumulate the **number of ways** to make a particular sum.

---

### Dry Run Example:

**Input:**

```python
coins = [1, 2, 3]
sum = 4
```

**Initialize:**
We use a 1D DP array `dp` of size `sum + 1` where:

* `dp[i]` = number of ways to make sum `i`
* `dp[0] = 1` (base case – one way to make sum 0)

**Process each coin one by one:**

#### 1. Using coin = 1:

```
dp[1] += dp[1-1] = dp[1] + dp[0] = 0 + 1 = 1
dp[2] += dp[2-1] = 0 + 1 = 1
dp[3] += dp[3-1] = 0 + 1 = 1
dp[4] += dp[4-1] = 0 + 1 = 1

dp = [1, 1, 1, 1, 1]
```

#### 2. Using coin = 2:

```
dp[2] += dp[0] = 1 + 1 = 2
dp[3] += dp[1] = 1 + 1 = 2
dp[4] += dp[2] = 1 + 2 = 3

dp = [1, 1, 2, 2, 3]
```

#### 3. Using coin = 3:

```
dp[3] += dp[0] = 2 + 1 = 3
dp[4] += dp[1] = 3 + 1 = 4

dp = [1, 1, 2, 3, 4]
```

**Answer: `dp[4] = 4`**

---

## ✅ 3. Optimized Python Code (Expected in Interviews)

### 🔹 Most Optimal DP Approach (Bottom-Up)

```python
class Solution:
    def count(self, coins, target_sum):
        # Number of coins
        n = len(coins)

        # Step 1: Initialize DP array
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # Base case: One way to make sum 0

        # Step 2: Iterate over each coin
        for coin in coins:
            for i in range(coin, target_sum + 1):
                dp[i] += dp[i - coin]  # Add ways to make (i - coin)

        return dp[target_sum]
```

### ⏱ Time and Space Complexity

* **Time:** `O(n * sum)` where `n` is the number of coins
* **Space:** `O(sum)` for 1D DP array

---

## 🪜 Alternate Brute Force (Only for understanding; not suitable for large inputs)

### 🔹 Recursive with Memoization

```python
class Solution:
    def count(self, coins, target_sum):
        from functools import lru_cache
        
        @lru_cache(None)
        def helper(i, total):
            if total == 0:
                return 1
            if i >= len(coins) or total < 0:
                return 0
            # Include coin[i] (infinite times) or skip to next
            return helper(i, total - coins[i]) + helper(i + 1, total)

        return helper(0, target_sum)
```

* **Time:** Exponential without memo, `O(n * sum)` with memo
* **Space:** O(n + sum) recursion stack and memo table

---

## ✅ 4. Interviewer Questions and Answers

### Q1: What’s the difference between coin permutations vs combinations?

**A:** Combinations count unique sets regardless of order. `[1,2]` and `[2,1]` are the same in combination. We solve using combinations.

---

### Q2: Why do we use a 1D DP array instead of 2D?

**A:** To reduce space complexity from `O(n * sum)` to `O(sum)` by overwriting results after using each coin.

---

### Q3: How would you modify the code to return all combinations?

**A:** You’d have to backtrack and store paths during DP updates, increasing time and space complexity.

---

### Q4: What happens if we reverse the loop order (sum loop outside)?

**A:** It would change the logic from **combinations** to **permutations**, giving wrong answers in this case.

---

### Q5: Can this be solved with greedy?

**A:** No, greedy does not work here. Example: `coins = [1, 3, 4]`, `sum = 6`. Greedy picks 4 + 1 + 1 = 3 coins, but 3 + 3 is better (only 2 coins if optimizing for min coins).

---

---

Here's the complete Python program to solve the **Coin Change (Count Ways)** problem with inline comments, detailed time and space complexities, input/output, and runtime measurement using `timeit`.

---

### ✅ Full Python Program

```python
import timeit

class Solution:
    def count(self, coins, target_sum):
        # Number of coin types
        n = len(coins)

        # Step 1: Initialize DP array
        # dp[i] will store the number of ways to form sum 'i'
        dp = [0] * (target_sum + 1)

        # Base case: There is 1 way to make sum 0 (select no coin)
        dp[0] = 1

        # Step 2: Build the dp table using bottom-up approach
        for coin in coins:
            for i in range(coin, target_sum + 1):
                dp[i] += dp[i - coin]
                # Add ways using current coin

        # Time Complexity: O(n * target_sum)
        # - n = number of coins
        # - target_sum = the target sum to be formed
        # Space Complexity: O(target_sum)
        return dp[target_sum]

# ---------------------------
# 🧪 Input and Execution
coins = [1, 2, 3]
target_sum = 4

# Start the timer
start_time = timeit.default_timer()

# Create an instance of the Solution class
sol = Solution()

# Call the method and get the result
ways = sol.count(coins, target_sum)

# End the timer
end_time = timeit.default_timer()
execution_time = end_time - start_time

# 📤 Output the result
print("Coins:", coins)
print("Target Sum:", target_sum)
print("Number of Ways to Make the Sum:", ways)
print("Execution Time (in seconds):", execution_time)
```

---

### 🔍 Sample Output

```
Coins: [1, 2, 3]
Target Sum: 4
Number of Ways to Make the Sum: 4
Execution Time (in seconds): 0.00011
```

---

### 🧠 Breakdown of Time and Space Complexity

| Step                    | Time Complexity     | Space Complexity |
| ----------------------- | ------------------- | ---------------- |
| Initializing DP array   | O(target\_sum)      | O(target\_sum)   |
| Nested loop (coin-wise) | O(n \* target\_sum) | -                |
| Total                   | O(n \* target\_sum) | O(target\_sum)   |

---

---

Here are **real-world use cases** where the **Coin Change (Count Ways)** problem directly applies or maps conceptually to important computational and business problems:

---

### 🏦 1. **Digital Wallet Transactions & Micro-Payments**

* **Use case:** Determining how many different ways a total transaction amount can be split across various denominations of stored wallet credits, loyalty points, or coupons.
* **Industry:** FinTech (Paytm, PhonePe, Google Pay, etc.)
* **Why relevant:** Optimizing redemption or conversion strategies.

---

### 📦 2. **Inventory Packaging & Resource Allocation**

* **Use case:** You have containers or resources of different sizes (e.g., boxes of 2L, 5L, 10L) and need to figure out how many combinations make up a target volume.
* **Industry:** Supply Chain, Logistics, Manufacturing
* **Why relevant:** Efficient use of packaging materials and logistics constraints.

---

### 💳 3. **ATM Currency Dispensing Algorithms**

* **Use case:** An ATM must determine the number of possible ways to dispense money using available denominations.
* **Industry:** Banking
* **Why relevant:** To maintain fairness and optimize currency availability across denominations.

---

### 📈 4. **Dynamic Pricing Models with Vouchers**

* **Use case:** E-commerce platforms offer various coupon values. Finding how many different combinations of coupons can be applied to reach a certain price target.
* **Industry:** E-commerce (Amazon, Flipkart)
* **Why relevant:** Enables marketing teams to analyze customer flexibility and create tailored offers.

---

### 🔐 5. **Security & Cryptography (Subset Sum Variant)**

* **Use case:** Similar combinatorial techniques are used in cryptographic algorithms (e.g., knapsack-based public key systems).
* **Industry:** Cybersecurity, Cryptography
* **Why relevant:** Helps in solving decision problems in secure data encoding or decryption.

---
