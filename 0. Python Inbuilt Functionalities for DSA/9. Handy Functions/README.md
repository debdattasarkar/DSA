
---

## 🔤 1. `sorted(iterable, key=..., reverse=...)`

### ✅ Use Case: Sort by frequency, custom value

```python
arr = [(5, 2), (3, 5), (1, 3)]
sorted_arr = sorted(arr, key=lambda x: x[1])
print(sorted_arr)  # Output: [(5, 2), (1, 3), (3, 5)]
```

**DSA Application**: Sort items by frequency, score, or value.

---

## 🔽 2. `min()` / `max()`

### ✅ Use Case: Find max element or min in a subarray

```python
arr = [3, 7, 2, 9, 5]
print(min(arr), max(arr))  # Output: 2 9
```

**DSA Application**: Finding max/min in sliding window, prefix/suffix comparisons.

---

## 🔢 3. `sum()`

### ✅ Use Case: Prefix sum, subarray sum

```python
arr = [1, 2, 3, 4]
print(sum(arr))  # Output: 10
```

**DSA Application**: Range queries, cumulative sums, optimization.

---

## 🔍 4. `any()` / `all()`

### ✅ Use Case: Check if any element satisfies a condition

```python
nums = [1, 2, 3, 4]
print(any(x > 3 for x in nums))  # True
print(all(x < 10 for x in nums))  # True
```

**DSA Application**: Constraint satisfaction, early exit checks.

---

## 🧮 5. `zip()` — Pair multiple arrays

### ✅ Use Case: Combine arrays element-wise

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

**DSA Application**: Group values and metadata together (e.g., value + index).

---

## 🔢 6. `enumerate()` — Index + Value Loop

### ✅ Use Case: Traverse with index

```python
arr = ['a', 'b', 'c']
for i, val in enumerate(arr):
    print(i, val)
```

**DSA Application**: Index tracking in prefix/suffix processing, DP.

---

## 🔄 7. `map()` — Apply function to all items

### ✅ Use Case: Fast transformation

```python
nums = ["1", "2", "3"]
ints = list(map(int, nums))  # [1, 2, 3]
```

**DSA Application**: Fast parsing or input transformation.

---

## 🧼 8. `filter()` — Keep only matching items

### ✅ Use Case: Clean data under a condition

```python
arr = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, arr))  # [2, 4]
```

**DSA Application**: Data pruning for subproblems (e.g., filter out negatives).

---

## 🔁 9. `set()` — Unique elements

### ✅ Use Case: Remove duplicates, set logic

```python
arr = [1, 2, 2, 3, 4]
print(set(arr))  # {1, 2, 3, 4}
```

**DSA Application**: Cycle detection, membership checks in O(1)

---

## 🧱 10. `list()`, `dict()`

* `list()` is used to convert any iterable to list.
* `dict()` used in key-value structure creation.

```python
pairs = [(1, 'a'), (2, 'b')]
print(dict(pairs))  # {1: 'a', 2: 'b'}
```

**DSA Application**: Build graphs, maps, counts, DP memo tables.

---

## 🔃 11. `range()` — Efficient loop control

```python
for i in range(3, 10, 2):
    print(i)  # 3 5 7 9
```

**DSA Application**: Fast iteration, reverse/backward traversal, grid traversal.

---

## 🧠 Summary Table

| Built-in          | Use In DSA                                     |
| ----------------- | ---------------------------------------------- |
| `sorted()`        | Custom sorting, greedy scheduling              |
| `min()` / `max()` | Sliding window, prefix/suffix comparison       |
| `sum()`           | Subarray sums, optimizations                   |
| `any()` / `all()` | Constraint checking                            |
| `zip()`           | Pairing values and indices                     |
| `enumerate()`     | Index-aware loops                              |
| `map()`           | Fast parsing/transformation                    |
| `filter()`        | Clean input, remove unwanted values            |
| `set()`           | Unique values, O(1) membership, hashing        |
| `dict()`          | Adjacency list, frequency maps, DP memoization |
| `range()`         | Control flow, loops, matrix/grid traversal     |

---

