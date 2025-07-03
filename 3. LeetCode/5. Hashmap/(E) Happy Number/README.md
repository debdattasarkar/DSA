
---

# ✅ 202. Happy Number

## Problem Statement

Write an algorithm to determine if a number `n` is a **happy number**.

### A **happy number** is defined as:

* Starting with any **positive integer**, replace the number by the **sum of the squares** of its digits.
* Repeat the process until:

  * the number equals 1 (where it will stay), or
  * it **loops endlessly in a cycle** which does not include 1.
* Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

---

## ✨ Examples

### Example 1:

```
Input: n = 19
Output: true
Explanation:
1² + 9² = 82  
8² + 2² = 68  
6² + 8² = 100  
1² + 0² + 0² = 1
```

### Example 2:

```
Input: n = 2
Output: false
```

---

## 🔒 Constraints:

* $1 \leq n \leq 2^{31} - 1$

---

## 🔍 Step-by-Step Dry Run

### Input: `n = 19`

```
Start: n = 19
Digits: [1, 9] → 1² + 9² = 1 + 81 = 82

n = 82
Digits: [8, 2] → 8² + 2² = 64 + 4 = 68

n = 68
Digits: [6, 8] → 6² + 8² = 36 + 64 = 100

n = 100
Digits: [1, 0, 0] → 1² + 0² + 0² = 1

✅ Result: Happy Number
```

---

## ✅ Optimized Code with Comments

### Python 🐍

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            # Calculate sum of squares of digits
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()  # To detect cycles

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
```

### Time and Space Complexity (Python)

| Step                 | Time Complexity                               | Space Complexity        |
| -------------------- | --------------------------------------------- | ----------------------- |
| `get_next()`         | O(log n) (digits of n)                        | O(1)                    |
| Cycle detection loop | O(log n) per iteration, worst case O(n) steps | O(n) set                |
| **Total**            | **O(k log k)**                                | **O(k)** for `seen` set |

---

### C++ 💻

```cpp
class Solution {
public:
    int getNext(int n) {
        int total = 0;
        while (n > 0) {
            int d = n % 10;
            total += d * d;
            n /= 10;
        }
        return total;
    }

    bool isHappy(int n) {
        unordered_set<int> seen;

        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            n = getNext(n);
        }

        return n == 1;
    }
};
```

---

### JavaScript 🌐

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const seen = new Set();

    const getNext = (num) => {
        let total = 0;
        while (num > 0) {
            const digit = num % 10;
            total += digit * digit;
            num = Math.floor(num / 10);
        }
        return total;
    };

    while (n !== 1 && !seen.has(n)) {
        seen.add(n);
        n = getNext(n);
    }

    return n === 1;
};
```

---

## 💬 Common Interview Questions & Answers

### Q1. What’s the main challenge in the happy number problem?

**A:** Detecting cycles using a set and computing digit squares efficiently.

---

### Q2. Why do we use a set or unordered\_set?

**A:** To detect cycles — if we revisit the same number again, we know we are stuck in an infinite loop.

---

### Q3. Can we do this without extra space?

**A:** Yes — we can use Floyd’s Cycle Detection (slow and fast pointer approach) instead of a set.

---

### Q4. What is the time complexity?

**A:** Worst-case is proportional to the number of unique values before cycle or reaching 1: roughly **O(k log k)**, where `k` is a digit sum sequence.

---

### Q5. What optimization improves this from brute-force?

**A:** Using memoization or detecting early cycles (e.g. using known unhappy loop set: {4, 16, 37, ...}).

---

Here's the **Floyd's Cycle Detection** version for the **Happy Number** problem — optimized for **constant space** and expected in **high-tier interviews** like Google, Meta, etc.

---

## ✅ Floyd's Cycle Detection for Happy Number

### 💡 Why use Floyd’s Algorithm?

Instead of using a `set` to remember all previously seen numbers (which uses O(n) space), we use two pointers:

* `slow`: moves one step at a time.
* `fast`: moves two steps at a time.

If they ever meet and the number is not 1 → there’s a cycle (not happy).
If `fast` reaches 1 → it's a happy number.

---

### 🐍 Python Implementation

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            # Helper to compute sum of squares of digits
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = get_next(n)  # fast moves one extra step ahead

        # Detect cycle
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))  # fast moves two steps

        return fast == 1
```

---

### 💻 C++ Implementation

```cpp
class Solution {
public:
    int getNext(int n) {
        int total = 0;
        while (n > 0) {
            int d = n % 10;
            total += d * d;
            n /= 10;
        }
        return total;
    }

    bool isHappy(int n) {
        int slow = n;
        int fast = getNext(n);

        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }

        return fast == 1;
    }
};
```

---

### 🌐 JavaScript Implementation

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const getNext = (num) => {
        let total = 0;
        while (num > 0) {
            const digit = num % 10;
            total += digit * digit;
            num = Math.floor(num / 10);
        }
        return total;
    };

    let slow = n;
    let fast = getNext(n);

    while (fast !== 1 && slow !== fast) {
        slow = getNext(slow);
        fast = getNext(getNext(fast));
    }

    return fast === 1;
};
```

---

## ⏱ Time and Space Complexity

| Step               | Time Complexity     | Space Complexity |
| ------------------ | ------------------- | ---------------- |
| `get_next()`       | O(log n)            | O(1)             |
| Floyd’s cycle loop | O(k log k), bounded | O(1) ✅           |

* The number of digits is log(n).
* The number of iterations is bounded since the sequence of digit-squares eventually falls into a known cycle or reaches 1.
* No `set` needed: we use two pointers instead.

---

Here’s a clear comparison of the **Set-Based Approach** vs **Floyd's Cycle Detection (Slow-Fast Pointers)** for the **Happy Number** problem:

---

### 🔁 Common Core Logic:

Both approaches compute a sequence by repeatedly replacing a number with the **sum of the squares of its digits**.

---

## 🧠 1. **Set-Based Cycle Detection**

### ✅ Logic:

* Keep a `set` to store seen numbers.
* If a number repeats → cycle detected → return False.
* If number becomes 1 → return True.

### 🧩 Code Snippet (Python):

```python
seen = set()
while n != 1:
    n = get_next(n)
    if n in seen:
        return False
    seen.add(n)
return True
```

### 📊 Time and Space:

* **Time Complexity:** O(k log k) (same sequence generation).
* **Space Complexity:** O(k) → storing all intermediate numbers.

### ✅ Pros:

* Simple and easy to understand.
* Clear detection of previously visited values.

### ❌ Cons:

* Extra space usage: unbounded set growth in worst-case.

---

## 🏃 2. **Floyd’s Cycle Detection (Slow-Fast Pointers)**

### ✅ Logic:

* Use two pointers:

  * `slow`: advances one step at a time.
  * `fast`: advances two steps at a time.
* If `slow == fast` and not 1 → cycle detected.
* If `fast == 1` → return True.

### 🧩 Code Snippet (Python):

```python
slow = n
fast = get_next(n)
while fast != 1 and slow != fast:
    slow = get_next(slow)
    fast = get_next(get_next(fast))
return fast == 1
```

### 📊 Time and Space:

* **Time Complexity:** O(k log k) (same sequence traversal).
* **Space Complexity:** O(1) ✅ constant memory.

### ✅ Pros:

* Highly optimized for space.
* No extra memory usage for storing visited states.

### ❌ Cons:

* Slightly harder to grasp at first (needs understanding of Floyd’s algorithm).

---

## 🧮 Summary Table:

| Feature                    | **Set-Based**                 | **Floyd's Cycle Detection**          |
| -------------------------- | ----------------------------- | ------------------------------------ |
| Cycle Detection Method     | Use a `set` to detect repeats | Use two pointers (slow & fast)       |
| Space Complexity           | O(k)                          | O(1) ✅                               |
| Time Complexity            | O(k log k)                    | O(k log k)                           |
| Simplicity                 | ⭐⭐⭐⭐⭐ (easy to understand)    | ⭐⭐⭐ (needs some algorithm knowledge) |
| Suitability for interviews | ✅ Good                        | ✅✅ Excellent                         |
| Real-world analogy         | Memory map                    | Tortoise and hare race 🐢🐇          |

---

## ✅ When to Use What?

* **Set-Based** is ideal for:

  * Beginner-friendly explanations
  * Readability and clarity
* **Floyd’s Algorithm** is preferred:

  * In high-level interviews (FAANG)
  * When minimizing memory usage is key
