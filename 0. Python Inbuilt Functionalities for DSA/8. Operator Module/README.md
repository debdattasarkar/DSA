The **`operator` module** in Python provides **function versions of standard operators** — like `+`, `*`, `<`, and so on — that can be passed around like functions.

It’s especially useful in **DSA**, **sorting**, **functional programming**, and **custom key-based operations**.

---

## 📦 What is the `operator` module?

It gives you **function equivalents** of built-in operators and allows:

* Passing them as arguments (to `map`, `reduce`, `sorted`, etc.)
* Faster alternatives to `lambda`
* Cleaner, more readable code

---

## ✅ Commonly Used Functions in DSA

| Operator Syntax | `operator` Function           | Use Case                     |
| --------------- | ----------------------------- | ---------------------------- |
| `a + b`         | `operator.add(a, b)`          | Element-wise sum, reduce ops |
| `a * b`         | `operator.mul(a, b)`          | Product, matrix ops          |
| `a < b`         | `operator.lt(a, b)`           | Sorting, comparisons         |
| `a == b`        | `operator.eq(a, b)`           | Filtering, grouping          |
| `item[i]`       | `operator.itemgetter(i)`      | Key functions in `sorted()`  |
| `obj.attr`      | `operator.attrgetter('attr')` | OOP sorting/filtering        |

---

# 🧠 DSA Use Cases + Full Programs with Dry Runs

---

## ✅ 1. `operator.add` with `reduce`

### 📌 Problem: Compute sum of array using `reduce`

```python
from functools import reduce
import operator

arr = [1, 2, 3, 4]
total = reduce(operator.add, arr)
print(total)  # Output: 10
```

### 🔁 Dry Run:

```
1 + 2 → 3  
3 + 3 → 6  
6 + 4 → 10
```

---

## ✅ 2. `operator.mul` for product of array

### 📌 Problem: Product of all elements

```python
from functools import reduce
import operator

arr = [2, 3, 4]
product = reduce(operator.mul, arr)
print(product)  # Output: 24
```

---

## ✅ 3. `operator.itemgetter` for sorting tuples

### 📌 Problem: Sort (value, frequency) pairs by frequency

```python
from operator import itemgetter

pairs = [(5, 2), (3, 5), (1, 3)]
sorted_pairs = sorted(pairs, key=itemgetter(1))
print(sorted_pairs)  # Output: [(5, 2), (1, 3), (3, 5)]
```

### 🔁 Dry Run:

Sort by index 1 (frequency):
2 < 3 < 5 → Order preserved

---

## ✅ 4. `operator.attrgetter` for sorting objects

### 📌 Problem: Sort a list of students by score

```python
from operator import attrgetter

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student("Alice", 90),
    Student("Bob", 85),
    Student("Charlie", 95)
]

students_sorted = sorted(students, key=attrgetter('score'))
for s in students_sorted:
    print(s.name, s.score)
```

### 🔁 Dry Run:

Sort by score: 85 < 90 < 95
→ Output:

```
Bob 85  
Alice 90  
Charlie 95
```

---

## ✅ 5. `operator.eq`, `lt`, `gt` for filtering and comparison

```python
import operator

a, b = 5, 10
print(operator.lt(a, b))  # True
print(operator.eq(a, b))  # False
```

Useful in:

* Custom comparisons
* Decision logic
* Functional filters

---

## 🧠 Summary Table

| DSA Task               | `operator` Function  | Usage                  |
| ---------------------- | -------------------- | ---------------------- |
| Sum/product via reduce | `add`, `mul`         | Element-wise reduction |
| Sort tuples            | `itemgetter(i)`      | Sort by index          |
| Sort objects           | `attrgetter('attr')` | Sort by attribute      |
| Filter or compare      | `lt`, `gt`, `eq`     | Conditional logic      |

---

## 🧩 Full DSA Example: Frequency Sort using `Counter` + `itemgetter`

```python
from collections import Counter
from operator import itemgetter

def frequency_sort(arr):
    freq = Counter(arr)
    freq_pairs = list(freq.items())  # (num, frequency)
    freq_pairs.sort(key=itemgetter(1), reverse=True)
    result = []
    for num, f in freq_pairs:
        result.extend([num] * f)
    return result

print(frequency_sort([1, 1, 2, 3, 3, 3, 2, 2]))  
# Output: [2, 2, 2, 3, 3, 3, 1, 1]
```

---
