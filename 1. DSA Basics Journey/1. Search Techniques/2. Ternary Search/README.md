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
