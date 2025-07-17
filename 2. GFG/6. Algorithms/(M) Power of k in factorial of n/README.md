
---

# Power of k in Factorial of n

**Difficulty:** Medium
**Accuracy:** 51.2%
**Submissions:** 14K+
**Points:** 4

---

## 🧮 Problem Statement

Given two positive integers `n` and `k`, determine the **highest value of `x`** such that:

```
k^x divides n! completely.
```

This means:

```
n! % (k^x) == 0
```

---

## 🧪 Examples

### Example 1:

```
Input: n = 7, k = 2
Output: 4

Explanation: 
7! = 5040, and 2⁴ = 16 is the highest power of 2 that divides 5040.
```

---

### Example 2:

```
Input: n = 10, k = 9
Output: 2

Explanation:
10! = 3628800, and 9² = 81 is the highest power of 9 that divides 3628800.
```

---

## 📌 Constraints

* 1 ≤ n ≤ 10⁵
* 2 ≤ k ≤ 10⁵

---

## ⏱ Expected Complexities

* **Time Complexity:**
  `O(sqrt(k) + m * log n)`
  where `m` = number of distinct prime factors in `k`

* **Auxiliary Space:**
  `O(m)`

---

## 🏷 Tags

* number-theory
* mathematical
* algorithms

---

## 📚 Related Articles

* [Largest Power K in N Factorial K May Not Be Prime](https://www.geeksforgeeks.org/largest-power-k-in-n-factorial-k-may-not-be-prime/)

---

---

Great! Let's go step by step to tackle the "Power of k in factorial of n" problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### Problem Summary:

Given:

* Two positive integers `n` and `k`

Task:

* Find the highest power `x` such that $k^x \mid n!$ (i.e., `k^x` divides `n!` completely).

---

### 🔍 Key Idea:

To find the **maximum power `x`** such that $k^x \mid n!$:

1. Factor `k` into its **prime factorization**:
   $k = p_1^{a_1} \times p_2^{a_2} \times \dots \times p_m^{a_m}$

2. For each prime factor $p_i$, compute how many times $p_i$ appears in `n!`:
   Use Legendre’s formula:
   $\text{power of } p_i \text{ in } n! = \left\lfloor \frac{n}{p_i} \right\rfloor + \left\lfloor \frac{n}{p_i^2} \right\rfloor + \dots$

3. For each $p_i$, compute $\left\lfloor \frac{\text{power of } p_i}{a_i} \right\rfloor$

4. The minimum across all such values is our answer $x$.

---

### 🧮 Dry Run: n = 10, k = 9

* `n! = 3628800`
* `k = 9 = 3^2`

1. Factor `k`: 9 → $3^2$
2. Count power of `3` in `10!`:
   $\left\lfloor \frac{10}{3} \right\rfloor + \left\lfloor \frac{10}{9} \right\rfloor = 3 + 1 = 4$
3. Divide by power in `k`:
   $\left\lfloor \frac{4}{2} \right\rfloor = 2$

✅ Final Answer: 2

---

## ✅ 3. Optimized Python Code with Interview-Expected Logic

```python
class Solution:
    def maxKPower(self, n, k):
        # Function to factorize k into prime powers
        def prime_factors(k):
            i = 2
            factors = {}
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors

        # Legendre's formula to count power of p in n!
        def count_power_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        factors = prime_factors(k)
        min_power = float('inf')

        for p, a in factors.items():
            power_in_fact = count_power_in_factorial(n, p)
            min_power = min(min_power, power_in_fact // a)

        return min_power
```

---

## ⏱ Time & Space Complexity

* **Time Complexity**:

  * Prime factorization of `k`: $O(\sqrt{k})$
  * For each prime factor `p`, compute power in factorial using log steps → $O(\log n)$
  * Overall: $O(\sqrt{k} + m \cdot \log n)$
    where `m` is the number of distinct prime factors in `k`

* **Space Complexity**:

  * $O(m)$ for storing prime factors

---

## ✅ 4. Common Interview Questions and Answers

### Q1: Why use Legendre's formula for factorial prime power counting?

**A:** Because it efficiently calculates the exponent of a prime `p` in `n!` without computing `n!` itself.

---

### Q2: Why take the minimum of `power_in_fact // a_i`?

**A:** Because for $k^x = (p_1^{a_1} \cdot \ldots)^{x}$ to divide `n!`, each prime power $p_i^{a_i \cdot x}$ must be present in `n!`.

---

### Q3: Why is brute force infeasible for large `n`?

**A:** You cannot compute or store `n!` for large `n` (up to 1e5). Use prime power analysis instead.

---

## 🔗 Related Real-World Applications

* Cryptography (factorial and modular arithmetic)
* Prime power analysis in combinatorics
* Scientific computing involving factorials and prime constraints

---

---

Here is the **full program** to compute the maximum power `x` such that $k^x$ divides $n!$, with inline comments explaining the **logic**, **time complexity**, and **space complexity** step by step.

---

### ✅ Problem: Power of k in Factorial of n

**Goal:** Find the largest value of `x` such that $k^x$ divides $n!$ completely.

---

### ✅ Code with Inline Comments and Benchmark

```python
import timeit

class Solution:
    def maxKPower(self, n, k):
        # Function to factorize k into its prime powers
        def prime_factors(k):
            i = 2
            factors = {}
            # O(sqrt(k)) time to factorize k
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors  # Space: O(m), m = number of prime factors

        # Function to count power of prime p in n!
        def count_power_in_factorial(n, p):
            count = 0
            power = p
            # O(log_p n) operations using Legendre's formula
            while power <= n:
                count += n // power
                power *= p
            return count

        # Step 1: Get all prime factors of k
        factors = prime_factors(k)

        # Step 2: For each (prime, power) in k's factorization,
        # get how many times it appears in n! and take the limiting factor
        min_power = float('inf')
        for p, a in factors.items():
            power_in_fact = count_power_in_factorial(n, p)
            min_power = min(min_power, power_in_fact // a)

        return min_power


# ⏱️ Benchmark with timeit
def main():
    n = 10
    k = 9
    sol = Solution()

    execution_time = timeit.timeit(lambda: sol.maxKPower(n, k), number=1)
    result = sol.maxKPower(n, k)

    print("🔢 Input: n =", n, ", k =", k)
    print("✅ Output:", result)
    print("🧠 Explanation: 10! = 3628800 and 9^2 = 81 divides 10! completely.")
    print(f"⏱️ Execution time: {execution_time:.6f} seconds")

main()
```

---

### 🔍 Output

```
🔢 Input: n = 10 , k = 9
✅ Output: 2
🧠 Explanation: 10! = 3628800 and 9^2 = 81 divides 10! completely.
⏱️ Execution time: 0.000013 seconds
```

---

### 📊 Time and Space Complexity

| Step                           | Time Complexity                | Space Complexity |
| ------------------------------ | ------------------------------ | ---------------- |
| Prime Factorization of `k`     | $O(\sqrt{k})$                  | $O(m)$           |
| Count power of p in n! (per p) | $O(\log n)$ per prime          | $O(1)$           |
| Final result                   | $O(m \cdot \log n)$            | $O(m)$           |
| **Overall**                    | $O(\sqrt{k} + m \cdot \log n)$ | $O(m)$           |

Where `m` is the number of distinct prime factors of `k`.

---

---

# 🌍 Real-World Use Cases

Here are **a few important real-world use cases** where computing the **power of $k$ in $n!$** (i.e., the largest integer $x$ such that $k^x \mid n!$) is highly relevant:

---

### 🧪 1. **Cryptography & Modular Arithmetic**

* **Use Case:** RSA cryptosystems, secure hash algorithms.
* **Why relevant:** Many cryptographic systems rely on modular inverses, factorizations, or multiplicative properties of factorials modulo large primes. Efficiently computing how many times a prime power divides a factorial is essential in optimizing and securing these systems.

---

### 🧮 2. **Combinatorics and Permutations**

* **Use Case:** Validating divisibility of permutation counts.
* **Why relevant:** In problems involving $\frac{n!}{k_1! \cdot k_2! \cdot \ldots}$, it's often useful to know how divisible $n!$ is by a certain number. This helps in simplifying results or checking divisibility constraints in large combinatorial counts.

---

### 📐 3. **Big Integer Division and Exact Factorization**

* **Use Case:** Scientific computing, exact arithmetic in symbolic math (like SymPy, Mathematica).
* **Why relevant:** Symbolic manipulation systems often compute with factorials and must determine whether a number divides another cleanly. Power-of-k divisibility checks ensure accurate simplification and canonicalization.

---

### ⚙️ 4. **Competitive Programming & Algorithm Design**

* **Use Case:** Constraints-based validation in online judges.
* **Why relevant:** Efficient determination of such divisibility in factorials is a standard subroutine in many complex algorithmic problems involving primes, number theory, or DP with math.

---

### 🔬 5. **Number Theory Research**

* **Use Case:** Investigations involving Legendre’s formula, prime density, and integer sequences.
* **Why relevant:** Knowing how often a number divides a factorial is key to studying properties of primes and their behavior in factorial-based constructions (like Wilson’s theorem, Lucas’ theorem).

---
