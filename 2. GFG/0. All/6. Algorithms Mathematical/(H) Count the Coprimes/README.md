
---

# 🧮 Count the Coprimes

**Difficulty:** Hard
**Accuracy:** 49.35%
**Submissions:** 18K+
**Points:** 8

---

## 📘 Problem Statement

You are given an array `arr[]` of positive integers.

Your task is to count the number of **unordered pairs** of indices **(i, j)** such that:

* $0 \leq i < j \leq n-1$
* $\gcd(arr[i], arr[j]) = 1$

In other words, count how many pairs of indices `(i, j)` exist such that the elements at those indices are **co-prime** (i.e., have a Greatest Common Divisor of 1).

---

## 📌 Examples

### 🔹 Example 1:

**Input:**
`arr[] = [1, 2, 3]`
**Output:**
`3`
**Explanation:**
The valid coprime pairs are:

* (0, 1): gcd(1, 2) = 1
* (0, 2): gcd(1, 3) = 1
* (1, 2): gcd(2, 3) = 1

---

### 🔹 Example 2:

**Input:**
`arr[] = [4, 8, 3, 9]`
**Output:**
`4`
**Explanation:**
Valid coprime pairs:

* (0, 2): gcd(4, 3) = 1
* (0, 3): gcd(4, 9) = 1
* (1, 2): gcd(8, 3) = 1
* (1, 3): gcd(8, 9) = 1

---

## ✅ Constraints

* $2 \leq arr.size() \leq 10^4$
* $1 \leq arr[i] \leq 10^4$

---

## 🧠 Expected Complexity

* **Time Complexity:**
  $O(n + M \log M)$, where $M = \max(arr[i])$

* **Auxiliary Space:**
  $O(M)$, where $M = \max(arr[i])$

---

## 🏷️ Topic Tags

* Number Theory
* Mathematical
* Sieve
* Inclusion-Exclusion
* Algorithms

---

## 🔗 Related Articles

* [Find Number of Co-Prime Pairs in an Array](#)

---

---

Here is a complete, interview-ready breakdown of the **"Count the Coprimes"** problem using the **optimized solution** (Mobius-style inclusion-exclusion approach):

---

## ✅ 1. Problem Summary (Based on Image)

Given an array `arr[]` of positive integers, count the number of unordered index pairs `(i, j)` such that:

* `0 ≤ i < j < n`
* `gcd(arr[i], arr[j]) == 1` (i.e., they are **co-prime**)

---

## ✅ 2. Step-by-Step Text Explanation + Dry Run

### 🧠 Key Idea:

Count **all unordered pairs** and subtract the number of pairs that are **not coprime** using a sieve-style method.

---

### 🧮 Step-by-Step Process:

#### 🔹 Step 1: Count frequency of each number in `arr`

```python
l[x] += 1
```

* Example: `arr = [4, 8, 3, 9]`
* Frequencies (`l`) will be:

  ```
  l[3] = 1
  l[4] = 1
  l[8] = 1
  l[9] = 1
  ```

#### 🔹 Step 2: Iterate from `m` down to `1` and count pairs divisible by `i`

```python
for i in range(m, 0, -1):
    for j in range(i, m + 1, i):
        c += l[j]
        r[i] -= r[j]
    r[i] += c * (c - 1) // 2
```

* For `i = 1`, you consider how many pairs are divisible by `1`, `2`, ..., and subtract overcounted ones.
* This is a reverse inclusion-exclusion.

#### 🔹 Step 3: Result is `r[1]` – number of **unordered co-prime pairs**

---

### 🧪 Dry Run on Input: `[1, 2, 3]`

All unordered pairs:

* (1, 2) → gcd = 1 ✅
* (1, 3) → gcd = 1 ✅
* (2, 3) → gcd = 1 ✅

So, expected output is `3`.

Code builds up:

* `total_pairs = 3`
* `r[1] = 3` after subtracting non-coprime pairs (which are 0)

---

## ✅ 3. Optimized Code (Interview Format)

```python
class Solution:
    def cntCoprime(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        m = max(arr)

        # l[x] stores how many times x appears in arr
        l = [0] * (m + 1)
        for x in arr:
            l[x] += 1

        # r[i] stores number of unordered pairs where both numbers divisible by i
        r = [0] * (m + 1)

        # Inclusion-Exclusion: count total pairs divisible by i
        for i in range(m, 0, -1):
            c = 0
            for j in range(i, m + 1, i):
                r[i] -= r[j]  # subtract overcounted pairs
                c += l[j]     # count elements divisible by i
            r[i] += (c * (c - 1)) // 2  # unordered pairs

        return r[1]  # count of coprime pairs
```

---

### ⏱️ Time & Space Complexity

| Metric           | Complexity                            |
| ---------------- | ------------------------------------- |
| Time Complexity  | `O(n + M log M)` where `M = max(arr)` |
| Space Complexity | `O(M)`                                |

---

## ✅ 4. Interview Questions & Answers

### ❓ Q1: What does `gcd(a, b) == 1` mean?

🟢 A1: It means `a` and `b` are **coprime** – they have no common positive divisors except `1`.

---

### ❓ Q2: Why can't we use brute-force for large inputs?

🟢 A2: Brute-force takes `O(n^2)`, which is too slow for `n ≈ 10^4`. The optimized version uses **sieve + frequency** to reduce the time to `O(n + M log M)`.

---

### ❓ Q3: What algorithm is being used in this optimized version?

🟢 A3: It uses **Mobius-style Inclusion-Exclusion Principle**, similar to sieve optimizations, to avoid repeated pairwise GCD calculations.

---

### ❓ Q4: What’s the significance of `r[1]`?

🟢 A4: It stores total number of unordered pairs with **gcd = 1**, i.e., coprime pairs — which is our final answer.

---

### ❓ Q5: How does `r[i] -= r[j]` help?

🟢 A5: It subtracts over-counted values for multiples of `i`, following the reverse of Inclusion-Exclusion to avoid double-counting.

---

---

### ✅ Full Summary with Code, Explanation, and Real-World Use Cases

---

### ✅ Problem: Count the Coprimes

Given an array `arr[]` of **positive integers**, find the number of **unordered pairs** `(i, j)` such that:

* `0 ≤ i < j < n`
* `gcd(arr[i], arr[j]) == 1` → the numbers are **coprime**

---

### ✅ Step-by-Step Text Explanation

We aim to efficiently count unordered coprime pairs in the array using an **optimized number-theoretic approach**:

#### 🧠 Key Observations:

* Brute force checking `gcd(a, b)` for every pair is **O(n²)** → not feasible for large `n`.
* Instead, use a **reverse Inclusion-Exclusion + Sieve approach** to efficiently count non-coprime pairs and subtract from total.

---

### ✅ Dry Run for arr = \[1, 2, 3]

Total pairs = (3 × 2) // 2 = 3
Pairs: (1,2), (1,3), (2,3)

GCDs:

* gcd(1,2) = 1 → coprime ✅
* gcd(1,3) = 1 → coprime ✅
* gcd(2,3) = 1 → coprime ✅

Result = 3 coprime pairs ✅

---

### ✅ Python Optimized Code (Using Sieve + Inclusion-Exclusion)

```python
from timeit import default_timer as timer

class Solution:
    def cntCoprime(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        m = max(arr)  # Step 1: max element

        # Step 2: Frequency count
        l = [0] * (m + 1)
        for x in arr:
            l[x] += 1  # O(n)

        # Step 3: Initialize coprime helper array
        r = [0] * (m + 1)

        # Step 4: Inclusion-Exclusion
        for i in range(m, 0, -1):  # O(m log m)
            c = 0
            for j in range(i, m + 1, i):
                r[i] -= r[j]
                c += l[j]
            r[i] += (c * (c - 1)) // 2  # combinations

        return r[1]  # Total coprime pairs
```

---

### ✅ Main Driver with Timing

```python
def main():
    arr = [1, 2, 3]
    print("Input array:", arr)

    solution = Solution()
    
    start = timer()
    result = solution.cntCoprime(arr)
    end = timer()

    print("Number of co-prime pairs:", result)
    print("Execution time (seconds):", end - start)

main()
```

---

### ✅ Time and Space Complexity

| Aspect           | Complexity                          |
| ---------------- | ----------------------------------- |
| Time Complexity  | `O(n + M log M)` where M = max(arr) |
| Space Complexity | `O(M)`                              |

---

### ✅ Interview Expected Questions & Answers

| Question                          | Answer                                                       |
| --------------------------------- | ------------------------------------------------------------ |
| What is the naive approach?       | Check all pairs `(i, j)` with `gcd(a[i], a[j]) == 1`, O(n²). |
| Why is brute-force not good here? | Time limit exceeds for `n > 10^3` due to quadratic pairs.    |
| What optimization did you use?    | Inclusion-Exclusion principle + Sieve-style precomputation.  |
| Why do you use `r[i] -= r[j]`?    | To subtract overcounted pairs from multiples of `i`.         |
| What does `r[1]` give?            | Total number of unordered co-prime pairs.                    |

---

### ✅ Real-World Use Cases (Only Most Important)

| Use Case               | Description                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| **Cryptography**       | Coprime numbers are core to RSA and other encryption systems (e.g., key generation).              |
| **Modular Arithmetic** | Coprime relations are required for modular inverse calculations, e.g., Chinese Remainder Theorem. |
| **Scheduling Systems** | Coprimality in time intervals helps avoid collision in resource sharing or job scheduling.        |
| **Music Theory**       | Rhythmic patterns involving beats in co-prime lengths help in constructing polymeters.            |

---
