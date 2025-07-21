
---

## 🧮 **\[GFG] Maximum Value of an Arithmetic Expression With Parentheses**

🔗 [GeeksforGeeks link](https://www.geeksforgeeks.org/maximum-value-of-an-arithmetic-expression/)

### ✅ Problem Statement:

You’re given a mathematical expression with **numbers and binary operators** (`+`, `-`, `*`). Your task is to find the **maximum value** the expression can take by adding parentheses in different ways.

For example:

```
Input: "1+2*3+4*5"
Output: 105
Explanation:
  Possible Parentheses: ((1 + 2) * (3 + 4)) * 5 = 105 (maximum)
```

---

## 🔎 Key Insight:

We need to:

* Evaluate **all valid ways of parenthesizing** the expression
* Use **recursion + memoization**
* (Ternary search is typically used in numeric/continuous domains. Here we use **DP + recursion**)

But there's also a **ternary-like recursive structure**: try splitting at every operator.

---

## ✍️ Step-by-Step Approach:

1. Parse the expression into tokens: `[1, '+', 2, '*', 3, '+', 4, '*', 5]`
2. Define a recursive function `solve(i, j)` to evaluate the **max value** from `i` to `j`.
3. For every operator at position `k` (where `k % 2 == 1`):

   * Split expression into two parts: `solve(i, k-1)` and `solve(k+1, j)`
   * Combine using the operator at `k`
4. Use memoization to avoid recomputation.

---

## ✅ Python Code (With Comments)

```python
def max_expression_value(expr: str) -> int:
    import functools

    # Parse the input string into list of tokens
    tokens = []
    num = ''
    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            tokens.append(int(num))
            tokens.append(ch)
            num = ''
    tokens.append(int(num))

    n = len(tokens)

    @functools.lru_cache(None)
    def solve(i, j):
        if i == j:
            return tokens[i]

        max_val = float('-inf')

        # Split at each operator
        for k in range(i + 1, j, 2):
            left = solve(i, k - 1)
            right = solve(k + 1, j)
            op = tokens[k]

            if op == '+':
                result = left + right
            elif op == '-':
                result = left - right
            elif op == '*':
                result = left * right
            else:
                continue

            max_val = max(max_val, result)

        return max_val

    return solve(0, n - 1)
```

---

## ✅ Example

```python
expr = "1+2*3+4*5"
print(max_expression_value(expr))  # Output: 105
```

---

## ⏱️ Time & Space Complexity

* **Time Complexity:** `O(n^3)` — `n^2` subproblems × `O(n)` operators
* **Space Complexity:** `O(n^2)` for recursion stack + cache

---

## ✅ Interview-Level Questions

| Question                                      | Answer                                                          |
| --------------------------------------------- | --------------------------------------------------------------- |
| What is the brute force approach?             | Try all valid parenthesizations recursively                     |
| Can this be optimized?                        | Yes, using memoization (DP)                                     |
| Does operator precedence matter?              | No. We are allowed to insert parentheses anywhere               |
| Is it possible to also return the expression? | Yes, store the string along with value in memo                  |
| Any real-world use?                           | Compilers evaluating expression trees, symbolic algebra systems |

---

---

Great question — and important clarification:

---

## ❓ Is This a Ternary Search Technique?

**No**, this problem **does not** use **ternary search** in the algorithmic sense.

---

### ✅ Let's Distinguish:

| **Ternary Search**                                                                              | **This Problem**                                                                 |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Used on **continuous or monotonic functions** (like min or max of `f(x)` where `f` is unimodal) | Operates on **discrete symbolic expressions**                                    |
| Divides the search space into **three parts** (`left`, `mid1`, `mid2`, `right`)                 | Splits the expression at every **binary operator** (e.g., at every `'+'`, `'*'`) |
| Used when there's a clear numeric function to optimize                                          | Uses **divide-and-conquer + memoization**, not search over a domain              |

---

### 📌 What This Actually Uses:

This is a classic example of:

* **Divide and Conquer**
* **Recursive DP with memoization**
* Similar to the **Matrix Chain Multiplication** or **Boolean Parenthesization** problems

---

## 🧠 Why the Confusion?

Some may call this "**ternary-like structure**" because:

* You **split** the expression at each operator, forming left and right parts
* You **evaluate and combine** — but it's always **binary**, not ternary in the search space sense

---

## ✅ In Summary

* ❌ **Not ternary search**
* ✅ **Recursive DP with operator-splitting**
* ✅ Splits on operators and uses memoization to store subresults

---

---

The problem **“Maximum Value of an Arithmetic Expression with Parentheses”** is fundamentally about **evaluating symbolic expressions**, not finding a numeric optimum in a unimodal function, which is where **ternary search** applies.

However, since you requested an example that **uses ternary search in spirit**, let's pivot to a **real mathematical optimization** problem where **ternary search** is **actually applicable**.

---

## ✅ Example Problem (Uses Ternary Search):

### 🔢 Problem:

> Given a **continuous unimodal function** `f(x) = (x - 3)^2 + 7`, find the value of `x` in a given interval `[a, b]` where `f(x)` is **minimum** using **ternary search**.

This **does use the ternary technique**, and it's common in:

* **Competitive programming**
* **Gradient-free optimization**
* **Physics simulations** where an objective has a clear minimum/maximum

---

## ✅ Python Code Using Ternary Search (on Continuous Domain)

```python
def f(x):
    # Unimodal function (parabola) — min at x=3
    return (x - 3)**2 + 7

def ternary_search_real(f, left, right, eps=1e-6):
    while right - left > eps:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3

        if f(m1) < f(m2):
            right = m2
        else:
            left = m1

    return (left + right) / 2  # Approximate minimum x
```

### 🔁 Usage:

```python
min_x = ternary_search_real(f, 0, 10)
print(f"Minimum value at x ≈ {min_x:.6f}, f(x) ≈ {f(min_x):.6f}")
```

---

## 🧠 Why This Is True Ternary Search

| Feature                 | Present in Code                     |
| ----------------------- | ----------------------------------- |
| Continuous input space  | ✅ `x ∈ [0, 10]`                     |
| Unimodal function       | ✅ Parabola                          |
| Division into thirds    | ✅ `m1`, `m2`                        |
| Shrinking interval      | ✅ `left`, `right` based on f values |
| Stopping with precision | ✅ via `eps`                         |

---

## 📌 If You're Looking for Ternary in Expression Evaluation…

You won’t be able to apply **ternary search** directly on:

* Symbolic expressions like `"1+2*3"`
* Boolean parenthesization
* Min/max with symbolic parsing

Those are best solved using:

* **Recursion + Memoization**
* **Dynamic Programming**
* Sometimes **catalan structures** (for counting)

---
