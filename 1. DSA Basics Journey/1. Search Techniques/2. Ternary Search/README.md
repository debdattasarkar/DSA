Ternary Search is a powerful technique for **unimodal functions** — problems where the function increases up to a point and then decreases (or vice versa). It’s especially useful for **continuous search spaces** or **discrete convex/concave problems**.

---

## ✅ Ternary Search: Quick Primer

### When to Use:

* To find **maximum/minimum** of a function in a **monotonically increasing then decreasing** pattern (or vice versa).
* The function must be **unimodal** (only one peak or trough).

---

## 🗂️ Problem List (Progressive Difficulty)

### 🔹 Basic / Introductory

1. **Find maximum of a unimodal function** (continuous, e.g., parabola)
2. **Find minimum in unimodal array** (discrete)
3. **Find max value of f(x) = -ax² + bx + c** in integer domain

### 🔹 Medium

4. **Aggressive Cows** (solvable by Binary Search, but ternary idea applies to "maximize min distance")
5. **Minimize Time to Paint Boards** (Painter’s Partition — variation)
6. **Optimal Location for Warehouse** (minimize sum of distances)

### 🔹 Hard / Optimization Focused

7. **Geometric optimization** – minimize sum of distances from a point to several given points (Fermat point)
8. **Maximize Ratio / Minimize Cost per Unit** in convex cost problems
9. **Find point on a curve closest to a line** (continuous ternary on distance function)

---

---

Awesome! Let’s start with a **ternary search implementation template** for both:

---

## 🛠️ Ternary Search Templates

---

### ✅ 1. **Continuous Domain (Floating Point)**

Used when the answer lies in a **real-valued function** (like `f(x) = -x² + 3x`), and we want to **maximize or minimize** it.

#### ▶️ Template (Minimizing a Function)

```python
def ternary_search_float(f, left, right, eps=1e-7):
    """
    f: function to minimize
    left, right: search interval
    eps: precision
    """
    while right - left > eps:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        if f(mid1) < f(mid2):  # For MINIMUM
            right = mid2
        else:
            left = mid1
    return (left + right) / 2  # Approximate minimum
```

📌 Use `f(mid1) > f(mid2)` if you want to **maximize**.

---

### ✅ 2. **Discrete Domain (Integers)**

Used when the domain is integers (like positions, indices, etc.).

#### ▶️ Template (Maximizing or Minimizing)

```python
def ternary_search_discrete(f, left, right):
    """
    f: unimodal function defined on integers
    left, right: integer bounds
    """
    while right - left > 3:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if f(mid1) < f(mid2):  # For MAXIMUM
            left = mid1
        else:
            right = mid2

    # Final brute force check in small interval
    best = left
    for i in range(left + 1, right + 1):
        if f(i) > f(best):  # Change to < if minimizing
            best = i
    return best
```

---

## 🧪 Example: Max of f(x) = -x² + 6x + 3

```python
def f(x): return -x**2 + 6*x + 3
res = ternary_search_discrete(f, 0, 10)
print("Max at x =", res, "Value:", f(res))
```

✅ Output:

```
Max at x = 3, Value: 12
```

---

## 🧠 Summary

| Use Case        | Type    | Return             |
| --------------- | ------- | ------------------ |
| Function over ℝ | Float   | `(left + right)/2` |
| Function over ℤ | Integer | Best `x` in range  |

---

---

Great! Here's a **curated list** of popular and interview-relevant **Ternary Search** DSA problems (from basic to hard), mainly focused on **unimodal functions**, **optimization over continuous domains**, or **peak-like structures**.

---

## ✅ Basic to Intermediate Ternary Search Problems

### 1. **Find the Maximum/Minimum Value of a Unimodal Function**

* 📌 **Type:** Classic Ternary Search
* 🎯 **Goal:** Find max/min in unimodal array or convex function
* 🧠 **Used for:** Cost minimization, profit maximization

> ✅ Common setup:

```python
def f(x): return (x - 3)**2 + 7  # convex function

left, right = 0, 10
while right - left > 1e-6:
    m1 = left + (right - left) / 3
    m2 = right - (right - left) / 3
    if f(m1) < f(m2):
        right = m2
    else:
        left = m1
```

---

### 2. **\[GFG] Minimum Time to Complete Tasks with Given Speeds**

* 🔗 [Link](https://www.geeksforgeeks.org/minimum-time-required-to-produce-m-items/)
* 🎯 Given multiple workers with different speeds, minimize the time to produce `m` items.
* 🧠 Use ternary search on time.

---

### 3. **\[Leetcode 875] Koko Eating Bananas** *(use binary or ternary)*

* 🎯 Find the **minimum eating speed** such that she can eat all bananas in `h` hours.
* Can also use ternary search on integer speed.
* 🔥 Related to cost optimization over discrete values.

---

## 🔷 Advanced/Hard Ternary Search Problems

### 4. **\[GFG] Maximum Value of an Arithmetic Expression With Parentheses**

* 🔗 [Link](https://www.geeksforgeeks.org/maximum-value-expression/)
* 🎯 Use ternary search when evaluating expression values over floating domains.

---

### 5. **\[Leetcode 4] Median of Two Sorted Arrays (variant)**

* ✅ Ternary search-based idea to minimize the median difference (less common in interviews, more theoretical).

---

### 6. **\[Codeforces] Find Point of Minimum Distance Between Two Functions**

* 🎯 Given two functions `f1(x)` and `f2(x)`, find `x` minimizing `|f1(x) - f2(x)|`
* ⏱️ Ternary search on `x` from `l` to `r`.

---

### 7. **\[GFG] Aggressive Cows Variant — Maximize Distance with Cost Penalty**

* 🎯 Minimize `(distance_penalty * k + placement_cost)`
* Combines binary/ternary with DP/Greedy.

---
