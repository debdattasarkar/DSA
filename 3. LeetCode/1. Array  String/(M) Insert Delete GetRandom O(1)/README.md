Here is a README-style explanation for **Leetcode 380 – Insert Delete GetRandom O(1)**, including a dry run and full implementations in **Python**, **C++**, and **JavaScript** with inline comments.

---

# 🎲 Insert Delete GetRandom O(1) (Leetcode #380)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Hash Table`, `Design`, `Math`, `Randomized`

---

## 📘 Problem Statement

Implement the `RandomizedSet` class:

### Methods:

* `insert(val)` → Inserts `val` if not already present. Returns `True` if inserted.
* `remove(val)` → Removes `val` if present. Returns `True` if removed.
* `getRandom()` → Returns a random element from the set (all elements equally likely).

### Constraints:

* All operations must run in **average O(1)** time.
* `getRandom()` will always be called when at least one element exists.

---

## 🧠 Core Idea: HashMap + Array

To achieve O(1) for all operations:

| Operation   | Data Structure             |
| ----------- | -------------------------- |
| `insert`    | HashMap to check existence |
| `remove`    | Swap + pop from array      |
| `getRandom` | Random index from array    |

### Key Structures:

* `dict[val] = index` → tracks the position of each element
* `list[]` → stores the actual elements

---

## 🧪 Dry Run

```python
Operations: insert(1), insert(2), remove(1), getRandom()
State:
- insert(1) → list = [1], dict = {1: 0}
- insert(2) → list = [1, 2], dict = {1: 0, 2: 1}
- remove(1):
    - Swap 1 with last (2), pop last → list = [2], dict = {2: 0}
- getRandom() → returns 2 (only element)
```

---

## 🐍 Python Code

```python
import random

class RandomizedSet:

    def __init__(self):
        self.idx_map = {}  # val -> index
        self.nums = []     # stores values

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        # Move last element to val's position and pop last
        last_val = self.nums[-1]
        idx = self.idx_map[val]
        self.nums[idx] = last_val
        self.idx_map[last_val] = idx
        self.nums.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

---

## 💠 C++ Code

```cpp
class RandomizedSet {
    unordered_map<int, int> idx_map;
    vector<int> nums;

public:
    RandomizedSet() {}

    bool insert(int val) {
        if (idx_map.count(val)) return false;
        idx_map[val] = nums.size();
        nums.push_back(val);
        return true;
    }

    bool remove(int val) {
        if (!idx_map.count(val)) return false;
        int last = nums.back();
        int idx = idx_map[val];
        nums[idx] = last;
        idx_map[last] = idx;
        nums.pop_back();
        idx_map.erase(val);
        return true;
    }

    int getRandom() {
        return nums[rand() % nums.size()];
    }
};
```

---

## 🌐 JavaScript Code

```javascript
var RandomizedSet = function() {
    this.map = new Map();
    this.nums = [];
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (this.map.has(val)) return false;
    this.map.set(val, this.nums.length);
    this.nums.push(val);
    return true;
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (!this.map.has(val)) return false;
    let idx = this.map.get(val);
    let last = this.nums[this.nums.length - 1];

    this.nums[idx] = last;
    this.map.set(last, idx);
    this.nums.pop();
    this.map.delete(val);
    return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    return this.nums[Math.floor(Math.random() * this.nums.length)];
};
```

---

## ✅ Summary

| Operation   | Time Complexity |
| ----------- | --------------- |
| `insert`    | O(1) average    |
| `remove`    | O(1) average    |
| `getRandom` | O(1)            |

