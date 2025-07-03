
---

## 📦 What is the `collections` module?

`collections` is a built-in Python module that provides **specialized data structures** designed for **efficient operations**. It's heavily used in **DSA problems** where performance and cleaner code are critical.

---

## 🔧 We'll focus on 3 essential tools:

| Tool          | Purpose                                 | Common Use in DSA   |
| ------------- | --------------------------------------- | ------------------- |
| `deque`       | Fast double-ended queue (O(1) ops)      | Sliding window, BFS |
| `Counter`     | Frequency map                           | Majority, Anagrams  |
| `defaultdict` | Dictionary with auto-initialized values | Graphs, Grouping    |

---

## ✅ 1. `deque` — Double-Ended Queue

### 💡 What it does:

* Efficient `append()` and `popleft()` in **O(1)** time.
* Ideal for sliding window problems and BFS.

---

### 📌 DSA Example: Sliding Window Maximum

> Given an array and window size `k`, return the max of each sliding window.

### 🔢 Input:

```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
```

### 🧠 Output:

```
[3, 3, 5, 5, 6, 7]
```

---

### ✅ Code:

```python
from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()
    result = []

    for i, num in enumerate(nums):
        # Remove out-of-window indices
        if q and q[0] <= i - k:
            q.popleft()

        # Maintain decreasing order
        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        # Save max when window hits size k
        if i >= k - 1:
            result.append(nums[q[0]])
    
    return result
```

---

### 🔁 Dry Run:

Window = `[1, 3, -1]` → max = `3`
Window = `[3, -1, -3]` → max = `3`
...

---

## ✅ 2. `Counter` — Frequency Counter

### 💡 What it does:

* Automatically counts frequency of elements.
* Useful for mode, majority, anagram check.

---

### 📌 DSA Example: Majority Element (> n/2 times)

### 🔢 Input:

```python
nums = [2, 2, 1, 1, 1, 2, 2]
```

### 🧠 Output:

```
2
```

---

### ✅ Code:

```python
from collections import Counter

def majorityElement(nums):
    count = Counter(nums)
    for num, freq in count.items():
        if freq > len(nums) // 2:
            return num
```

---

### 🔁 Dry Run:

```
Counter = {2: 4, 1: 3}
Length = 7 → majority > 3
2 is majority
```

---

## ✅ 3. `defaultdict` — Auto-Initializing Dictionary

### 💡 What it does:

* Avoids key errors
* Auto-creates default values like list, int, etc.

---

### 📌 DSA Example: Group Anagrams

> Group words that are anagrams of each other.

### 🔢 Input:

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

### 🧠 Output:

```
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

### ✅ Code:

```python
from collections import defaultdict

def groupAnagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))  # Anagram signature
        groups[key].append(word)
    return list(groups.values())
```

---

### 🔁 Dry Run:

* Key for "eat" → "aet"
* Key for "tea" → "aet" → grouped with "eat"
* Key for "tan" → "ant"

Final groups: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`

---

## 🧠 Summary Table

| Tool          | What It Solves           | Common DSA Use                |
| ------------- | ------------------------ | ----------------------------- |
| `deque`       | Fast front/back ops      | BFS, sliding window, LRU      |
| `Counter`     | Count occurrences        | Mode, frequency, anagram      |
| `defaultdict` | Auto-init nested/grouped | Graphs, grouping, bucket sort |

---

---

# Short Version

Let’s go beyond the basics and see **real-world DSA examples** using:

1. `deque`
2. `Counter`
3. `defaultdict`

---

## 🔁 1. `deque`: Double-ended Queue (O(1) append & pop both sides)

### ✅ Use Case: **Sliding Window Maximum**

```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque()
    res = []

    for i, num in enumerate(nums):
        # Remove indices out of the window
        while q and q[0] <= i - k:
            q.popleft()

        # Remove smaller values at the back
        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res
```

### 💡 Time: O(n)

📌 Stores indices, not values → efficient

---

## 📊 2. `Counter`: Frequency Map

### ✅ Use Case: **Find majority element**

```python
from collections import Counter

def majority_element(nums):
    count = Counter(nums)
    for num, freq in count.items():
        if freq > len(nums) // 2:
            return num
```

### ✅ Use Case: **Anagram check**

```python
def is_anagram(a, b):
    return Counter(a) == Counter(b)
```

---

## 🧰 3. `defaultdict`: Auto-initializing Dictionary

### ✅ Use Case: **Group words by anagram class**

```python
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
```

### ✅ Use Case: **Graph adjacency list**

```python
from collections import defaultdict

graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4)]

for u, v in edges:
    graph[u].append(v)

# graph = {1: [2, 3], 2: [4]}
```

---

## 💡 Bonus: Other Useful Structures

### 4. `OrderedDict`: Preserves insertion order (Python 3.6+ does this natively too)

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
```

---

## 🔥 Summary Table

| Structure     | Time Complexity | Best For                               |
| ------------- | --------------- | -------------------------------------- |
| `deque`       | O(1) append/pop | Sliding window, BFS, LRU cache         |
| `Counter`     | O(n) counting   | Frequencies, majority, mode, histogram |
| `defaultdict` | O(1) insert/get | Graphs, grouping, cleaner code         |
| `OrderedDict` | O(1) access     | Ordered mappings, LRU-style logic      |

---
