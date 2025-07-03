Absolutely! Here's a compact, well-organized **Python Cheat Sheet for DSA Modules**, covering all the ones you've asked about:

---

# 🧠 Python Cheat Sheet for DSA 📘

Includes: `math`, `collections`, `itertools`, `heapq`, `bisect`, `functools`, `operator`, `array`, `random`, and `numpy`

---

## 🔢 `math` – Fast math operations

| Function               | Use                                  |
| ---------------------- | ------------------------------------ |
| `gcd(a, b)`            | Greatest common divisor              |
| `lcm(a, b)`            | Least common multiple                |
| `sqrt(x)` / `isqrt(x)` | Square root (float/int)              |
| `factorial(n)`         | n! used in permutations/combinations |
| `comb(n, r)`           | nCr combinations                     |
| `log(x, base)`         | Logarithm                            |
| `ceil(x)` / `floor(x)` | Round up/down                        |
| `inf`, `pi`            | Constants                            |

---

## 🧰 `collections` – Optimized Data Structures

| Structure           | Use Case                               |
| ------------------- | -------------------------------------- |
| `deque()`           | O(1) queue/stack – BFS, sliding window |
| `Counter()`         | Frequency map – majority, mode         |
| `defaultdict(type)` | Grouping – graphs, anagrams            |

---

## 🔁 `itertools` – Combinatorics & Iterators

| Function                         | Use                                 |
| -------------------------------- | ----------------------------------- |
| `combinations(iter, r)`          | r-length unique subsets             |
| `permutations(iter, r)`          | r-length orderings                  |
| `product(iter, repeat=r)`        | Cartesian product (with repetition) |
| `accumulate(iter)`               | Prefix sum, cumulative ops          |
| `groupby(iter)`                  | Grouping by key                     |
| `count()`, `cycle()`, `repeat()` | Infinite iterators                  |

---

## 📐 `heapq` – Priority Queue (Min Heap)

| Function                 | Use Case                  |
| ------------------------ | ------------------------- |
| `heapify(list)`          | Convert list to min-heap  |
| `heappush(heap, x)`      | Add element               |
| `heappop(heap)`          | Remove smallest element   |
| `nlargest(k, iterable)`  | Top K elements (max heap) |
| `nsmallest(k, iterable)` | Bottom K elements         |

---

## 🔍 `bisect` – Binary Search on Sorted Lists

| Function               | Use Case                 |
| ---------------------- | ------------------------ |
| `bisect_left(arr, x)`  | Insert before duplicates |
| `bisect_right(arr, x)` | Insert after duplicates  |
| `insort_left(arr, x)`  | Insert keeping order     |
| `insort_right(arr, x)` | Insert after duplicates  |

---

## 🧩 `functools` – Functional Programming Utilities

| Function                    | Use                             |
| --------------------------- | ------------------------------- |
| `@lru_cache()`              | Memoize recursive DP            |
| `reduce(func, seq)`         | Accumulate to single value      |
| `partial(func, fixed_args)` | Create pre-filled functions     |
| `cmp_to_key(func)`          | Custom sort key from comparator |

---

## ➗ `operator` – Functional Operator Alternatives

| Operator   | Equivalent Function  |
| ---------- | -------------------- |
| `a + b`    | `operator.add(a, b)` |
| `a * b`    | `operator.mul(a, b)` |
| `a < b`    | `operator.lt(a, b)`  |
| `item[i]`  | `itemgetter(i)`      |
| `obj.attr` | `attrgetter('attr')` |

---

## 📦 `array` – Lightweight Typed Arrays

| Code                    | Description               |
| ----------------------- | ------------------------- |
| `array('i', [1,2,3])`   | Integer array             |
| `array('f', [...])`     | Float array               |
| `.append(x)` / `.pop()` | Similar to list ops       |
| Used in:                | Segment tree, prefix sums |

---

## 🧮 `numpy` – Powerful Vector Math (for larger use cases)

| Function/Feature          | Use Case                 |
| ------------------------- | ------------------------ |
| `np.array([..])`          | Fast vectorized array    |
| `arr.mean()`, `arr.sum()` | Stats and aggregates     |
| `arr[arr > x]`            | Fast filtering (masking) |
| `np.dot(A, B)`            | Matrix multiplication    |
| `np.unique(arr)`          | Get unique elements      |

---

## 🎲 `random` – For randomized algorithms

| Function        | Use                             |
| --------------- | ------------------------------- |
| `randint(a, b)` | Random int in range             |
| `shuffle(arr)`  | In-place shuffle                |
| `choice(seq)`   | Random pick from sequence       |
| Used in:        | QuickSelect, Reservoir Sampling |

---

## 🧠 Suggested Combos (DSA Style)

| Task                          | Modules to Combine       |
| ----------------------------- | ------------------------ |
| Top-K Frequent Elements       | `Counter + heapq`        |
| Sliding Window Max            | `deque`                  |
| K-th Smallest Pair Distance   | `bisect + binary search` |
| Memoized DP                   | `lru_cache`              |
| Subset/Permutation generation | `itertools`              |
| Sorted Frequency Map          | `Counter + itemgetter`   |

---
