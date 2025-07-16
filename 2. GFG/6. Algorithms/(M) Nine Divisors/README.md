
---

# 🧮 Nine Divisors

**Difficulty:** Medium
**Accuracy:** 35.58%
**Submissions:** 18K+
**Points:** 4

---

## 📝 Problem Statement

Given a positive integer `n`, you need to **count** the numbers less than or equal to `n` that have **exactly 9 divisors**.

---

## 📌 Examples

### Example 1

```
Input: 
n = 100

Output: 
2

Explanation: 
Numbers which have exactly 9 divisors are: 36 and 100.
```

---

### Example 2

```
Input: 
n = 200

Output: 
3

Explanation: 
Numbers which have exactly 9 divisors are: 36, 100, 196.
```

---

## 📊 Constraints

```
1 ≤ n ≤ 10^9
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(√n \* log(log√n))
* **Auxiliary Space:** O(√n)

---

## 🏷️ Topic Tags

* Searching
* Prime Number
* Sieve
* Binary Search
* Algorithms

---

## 📚 Related Articles

* [Count Number Of Integers Less Than Or Equal To N Which Has Exactly 9 Divisors](https://practice.geeksforgeeks.org/problems/nine-divisors/0)

---

---

Let's go step-by-step for the problem **"Nine Divisors"**:

---

### ✅ **2. Text Explanation with Step-by-Step Dry Run**

#### **Problem Summary**

Given a number `n`, count how many numbers `≤ n` have exactly **9 divisors**.

#### **Key Insight**

A number can have exactly 9 divisors if its prime factorization fits one of the two patterns:

1. $p^8$ — where `p` is prime → divisors = 8+1 = 9
2. $p^2 \times q^2$ — where `p`, `q` are distinct primes → divisors = (2+1)×(2+1) = 9

#### **Dry Run**

Let’s take `n = 200`.

* Pattern 1: $p^8$

  * Try p = 2 → $2^8 = 256$ > 200 → invalid
  * So, no valid values

* Pattern 2: $p^2 \times q^2$

  * Try primes p = 2, q = 3 → $4 × 9 = 36$
  * p = 2, q = 5 → $4 × 25 = 100$
  * p = 2, q = 7 → $4 × 49 = 196$
  * So: \[36, 100, 196] → Count = **3**

---

### ✅ **3. Optimized Python Code (Sieve + Efficient Prime Pair Search)**

```python
import timeit

class Solution:
    def countNumbers(self, n):
        # Start timer
        start_time = timeit.default_timer()
        
        # Step 1: Sieve of Eratosthenes to get primes up to sqrt(n)
        import math
        limit = int(math.sqrt(n)) + 1
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i*i, limit+1, i):
                    is_prime[j] = False

        primes = [i for i, prime in enumerate(is_prime) if prime]

        count = 0

        # Pattern 1: p^8
        for p in primes:
            if p**8 <= n:
                count += 1
            else:
                break  # No need to continue further

        # Pattern 2: p^2 * q^2 where p != q
        len_primes = len(primes)
        for i in range(len_primes):
            for j in range(i+1, len_primes):
                val = (primes[i] ** 2) * (primes[j] ** 2)
                if val <= n:
                    count += 1
                else:
                    break  # inner loop break

        # Stop timer
        total_time = timeit.default_timer() - start_time
        print(f"Total count: {count}")
        print(f"Execution Time: {total_time:.6f} seconds")
        return count
```

---

### ✅ **4. Expected Interview Questions and Answers**

#### Q1. **What are the possible ways a number can have exactly 9 divisors?**

* Only two factorizations:

  1. $p^8$
  2. $p^2 \times q^2$, where p and q are distinct primes.

#### Q2. **How do you generate primes efficiently?**

* Use the **Sieve of Eratosthenes** which gives all primes up to √n in O(n log log n) time.

#### Q3. **Why don’t we consider more complex factorizations like $p^4 × q$?**

* $(4+1)(1+1) = 10$ → has 10 divisors, not 9.
* Only two configurations result in **exactly 9** divisors.

#### Q4. **What’s the time complexity of your solution?**

* **Sieve** → O(√n log log √n)
* **Looping over prime pairs** → O((√n)^2) in worst case, but practically limited due to break conditions.

---

---

## ✅ 1. **Brute Force Approach (for Education)**

### Idea:

For every number from 1 to `n`, count its number of divisors using trial division. If it has exactly 9 divisors, increment the count.

### Python Code:

```python
import timeit

class BruteForceSolution:
    def countNumbers(self, n):
        start = timeit.default_timer()
        def count_divisors(x):
            cnt = 0
            for i in range(1, int(x**0.5)+1):
                if x % i == 0:
                    if i * i == x:
                        cnt += 1  # Perfect square
                    else:
                        cnt += 2  # i and x/i
            return cnt

        ans = 0
        for num in range(1, n + 1):
            if count_divisors(num) == 9:
                ans += 1

        elapsed = timeit.default_timer() - start
        print(f"Brute-force Count: {ans}")
        print(f"Execution Time: {elapsed:.4f} seconds")
        return ans
```

### ⚠️ Time Complexity:

* For each number from `1` to `n`, we loop up to `√x`.
* Total: **O(n√n)** → extremely slow for `n > 10⁵`.

---

## ✅ 2. **Dry Run Table for Optimized Approach (n = 200)**

We use the two patterns:

1. $p^8$
2. $p^2 \times q^2$

### Step-by-Step for $n = 200$

#### Generate Primes up to √200 ≈ 14:

* Primes: `[2, 3, 5, 7, 11, 13]`

---

### Pattern 1: $p^8$

| Prime `p` | $p^8$ | Valid? |
| --------- | ----- | ------ |
| 2         | 256   | ❌ No   |
| 3         | 6561  | ❌ No   |

✅ **No valid values.**

---

### Pattern 2: $p^2 \times q^2$

| p | q  | $p^2 \times q^2$ | Value | Valid? |
| - | -- | ---------------- | ----- | ------ |
| 2 | 3  | $4 \times 9$     | 36    | ✅ Yes  |
| 2 | 5  | $4 \times 25$    | 100   | ✅ Yes  |
| 2 | 7  | $4 \times 49$    | 196   | ✅ Yes  |
| 2 | 11 | $4 \times 121$   | 484   | ❌ No   |
| 3 | 5  | $9 \times 25$    | 225   | ❌ No   |
| 3 | 7  | $9 \times 49$    | 441   | ❌ No   |

✅ **Total Valid: 3 → \[36, 100, 196]**

---

## 🆚 Final Comparison of Both Approaches

| Approach                    | Time Complexity        | Speed on n = 10⁶ | Scalability     |
| --------------------------- | ---------------------- | ---------------- | --------------- |
| Brute Force                 | O(n√n)                 | ❌ Slow           | ❌ Not scalable  |
| Optimized (Sieve + Pattern) | O(√n · log log n + p²) | ✅ Fast           | ✅ Scales to 10⁹ |

---

---

# 🌍 Real-World Use Cases

Here are a few **real-world use cases** where the core idea behind counting numbers with **exactly 9 divisors** is applicable or forms the foundation of deeper applications:

---

### ✅ 1. **Cryptography (Public Key Infrastructure)**

* Understanding the **divisor structure** of numbers is crucial in **RSA** and **other public key cryptographic systems**.
* Specifically, knowing how many divisors a number has helps **analyze factorization properties**, which is critical for:

  * Generating secure keys
  * Identifying weak keys
  * Optimizing prime-based key generation

---

### ✅ 2. **Mathematical Research & Number Theory**

* Used in **integer classification** problems like:

  * Identifying numbers with a fixed number of divisors
  * Studying **aliquot sequences** and **multiplicative functions** like $\sigma(n)$ and $\tau(n)$
* Applied in problems involving **perfect numbers**, **amicable numbers**, etc.

---

### ✅ 3. **Database Index Optimization (Hash Distribution)**

* Ensuring **uniform distribution of hash buckets** often involves mathematical functions like number of divisors.
* For instance, choosing keys with a **fixed number of divisors** can improve hash performance in **distributed systems**.

---

### ✅ 4. **Competitive Programming & Algorithm Benchmarking**

* Problems like this are used to **benchmark performance of number-theory based algorithms** under time constraints.
* Helps test optimized sieve + number generation pipelines.

---

### ✅ 5. **Digital Signal Processing (DSP) & FFT Algorithms**

* Some **Fast Fourier Transform (FFT)** algorithms rely on the **factorization and divisors of signal length**.
* Having a precise count of divisors helps in choosing optimal **radix** or **signal lengths** for transformations.

---
