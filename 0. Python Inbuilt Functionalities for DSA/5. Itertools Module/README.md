The **`itertools` module** in Python is a built-in library that provides **fast, memory-efficient tools** for iterating over data — especially useful in **DSA, combinatorics, and optimization problems**.

---

## 📦 What is `itertools`?

`itertools` provides **iterator building blocks** — you can generate permutations, combinations, Cartesian products, and more, without writing complex loops.

---

## 🔧 Commonly Used Functions

| Function                          | Purpose                          | Use in DSA                         |
| --------------------------------- | -------------------------------- | ---------------------------------- |
| `product()`                       | Cartesian product                | All combinations of k lists        |
| `permutations()`                  | All possible orderings           | Generate all paths/orders          |
| `combinations()`                  | Unique element groups (no order) | Subset generation                  |
| `combinations_with_replacement()` | Allows repetition                | Multichoice groupings              |
| `accumulate()`                    | Running totals / prefix sums     | Range sum queries                  |
| `groupby()`                       | Group consecutive elements       | Frequency block/group detection    |
| `cycle(), count(), repeat()`      | Infinite iterators               | Simulations, stream-based problems |

---

## ✅ 1. `combinations()` — Pick r out of n (unordered, no repeat)

### 💡 DSA Use: Subset sums, Knapsack variants

```python
from itertools import combinations

nums = [1, 2, 3]
for comb in combinations(nums, 2):
    print(comb)
```

🧪 Output:

```
(1, 2)
(1, 3)
(2, 3)
```

---

## ✅ 2. `permutations()` — All ordered arrangements

### 💡 DSA Use: TSP, generate all strings

```python
from itertools import permutations

for p in permutations([1, 2, 3]):
    print(p)
```

🧪 Output:

```
(1, 2, 3)
(1, 3, 2)
...
```

---

## ✅ 3. `product()` — Cartesian product (with repetition)

### 💡 DSA Use: Multi-loop generation, n-digit numbers

```python
from itertools import product

for p in product([0, 1], repeat=3):
    print(p)
```

🧪 Output:

```
(0, 0, 0)
(0, 0, 1)
...
(1, 1, 1)
```

---

## ✅ 4. `accumulate()` — Prefix sum, max, or custom ops

### 💡 DSA Use: Prefix sums, cumulative products

```python
from itertools import accumulate

nums = [1, 2, 3, 4]
print(list(accumulate(nums)))  # Sum: [1, 3, 6, 10]
```

Or with `max`:

```python
from itertools import accumulate
print(list(accumulate([1, 5, 2, 8], func=max)))
# Output: [1, 5, 5, 8]
```

---

## ✅ 5. `groupby()` — Group consecutive elements

### 💡 DSA Use: Run-length encoding, segment grouping

```python
from itertools import groupby

s = "aaabbccddd"
for key, group in groupby(s):
    print(key, list(group))
```

🧪 Output:

```
a ['a', 'a', 'a']
b ['b', 'b']
c ['c', 'c']
d ['d', 'd', 'd']
```

---

## ✅ 6. `count()` — Infinite counter

### 💡 DSA Use: Index generator, simulation

```python
from itertools import count

for i in count(10):
    if i > 15:
        break
    print(i)
```

🧪 Output:

```
10, 11, 12, 13, 14, 15
```

---

## ✅ 7. `repeat()` — Repeat value

### 💡 DSA Use: Fill test arrays or fixed repetition

```python
from itertools import repeat

for x in repeat("A", 3):
    print(x)
```

🧪 Output:

```
A
A
A
```

---

## 🧩 Full DSA Problem Example: Subset Sum from Unique Combinations

> Find how many subsets of size 2 in `[2, 4, 6, 10]` sum up to 16

```python
from itertools import combinations

def count_target_subsets(nums, k, target):
    count = 0
    for comb in combinations(nums, k):
        if sum(comb) == target:
            count += 1
    return count

print(count_target_subsets([2, 4, 6, 10], 2, 16))  # Output: 1 → (6,10)
```

---

## 🧠 Summary Table

| Task                          | Use Function        |
| ----------------------------- | ------------------- |
| Generate all r-sized subsets  | `combinations()`    |
| All orderings of elements     | `permutations()`    |
| All combinations with repeats | `product()`         |
| Compute prefix sums or max    | `accumulate()`      |
| Group repeated values         | `groupby()`         |
| Simulate counters or loops    | `count(), repeat()` |

---
