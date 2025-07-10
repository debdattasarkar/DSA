
---

### 🧩 Problem Theme: Introduction to Sliding Window

The sliding window pattern helps solve problems that involve:

* **Contiguous subarrays or substrings**
* With conditions like maximum, minimum, or distinct properties
* Optimally in **O(n)** time instead of brute-force **O(n²)**

---

### 🧠 About the Pattern

* The idea is to **move a window** over the array/string to maintain a valid subarray or substring.
* You **expand** the window by moving the right pointer and **contract** (or shift start) as needed from the left.
* Conditions inside the window help decide whether to grow, shrink, or calculate something.

---

### 💡 Steps to Apply Sliding Window

1. **Identify** if the problem involves contiguous subarrays/substrings.
2. **Determine** the window condition (e.g., sum, max, unique characters, etc.).
3. **Use two pointers**: `start` and `end`.
4. Adjust window size based on whether the current window satisfies the condition.
5. **Track answers** while adjusting the window (e.g., max length, count, etc.).

---

### ✅ Example Use Case

#### 🍪 Example: Max sum of size k

Given:

```python
nums = [2, 1, 5, 1, 3, 2], k = 3
```

The window slides across the array and sums values of size `k`:

* \[2, 1, 5] → sum = 8
* \[1, 5, 1] → sum = 7
* \[5, 1, 3] → sum = 9 (max)
* \[1, 3, 2] → sum = 6

✅ Final result = 9

---

### 🧪 Another Example

## 🧩 Problem: Longest Substring Without Repeating Characters

### 📄 Problem Statement

Given a string:

```
string = "abcdbea"
```

We are asked to find the **length of the longest substring** such that:

* No characters repeat.
* The substring consists of **contiguous** characters from the original string.

---

### 🧠 Input Representation

The string can be viewed as:

```
Index:   0   1   2   3   4   5   6
Chars:   a   b   c   d   b   e   a
```

---

### ✅ Goal

Find the length of the **longest substring** where all characters are **unique**.

---

### 🔍 Example Analysis

* From index `0` to `3`: "abcd" is valid → length = 4
* At index `4`, we see 'b' again, which is a duplicate
* A new window starts, and the process continues...

**Answer:** `4` (substring `"abcd"` is the longest with all distinct characters)

---

### 🛠️ Sliding Window Setup

To solve the problem efficiently, we use the **Sliding Window** technique with two pointers:

* `left` – marks the start of the current window
* `right` – expands the window as we move through the string

---

### 🔧 Initialization

* Both `left` and `right` pointers start at **index 0**
* We will grow the window by moving the `right` pointer
* If we encounter a **repeated character**, we'll move the `left` pointer forward to maintain a valid substring (all unique characters)

---

This is the basis of our dynamic sliding window which adapts in size as we scan through the input string `"abcdbea"`.

---

### 🔍 Example Progress – Handling Duplicates

Given: `string = "abcdbea"`

#### Current Window:

* `left` = 2
* `right` = 4
* Current window: `"cdbe"`

#### Seen Characters:

* `a → 0`
* `b → 4` ← duplicate at new position
* `c → 2`
* `d → 3`

#### Lengths:

* `current length = right - left = 4 - 2 = 2`
* `max length = 4` ← stays the same because `current < max`

#### Action:

* We **do not update** `max length` since the new window is shorter
* The `right` pointer will keep moving forward
* We are maintaining a dictionary `seen` to store the last seen index of each character

This helps ensure we always keep a valid window with **non-repeating characters**.

---

### 🧠 Sliding Window – Final Update Step

**String:** `"abcdbea"`

#### Current State:

* `left = 2`
* `right = 6`
* Current window: `"cdbea"`

#### Character Map (`seen`):

| Character | Last Seen Index |
| --------- | --------------- |
| a         | 0               |
| b         | 4               |
| c         | 2               |
| d         | 3               |
| e         | 5               |

---

### 🔁 Logic:

* Character `'a'` at index `6` is already in the `seen` map at index `0`.
* But since `0 < left (2)`, `'a'` is **outside the current window**.
* This means we can safely **update** its position to `6` and continue.

---

### 📏 Lengths:

* `current length = right - left + 1 = 6 - 2 + 1 = 5`
* `max length = 4`

✅ As `current length > max length`, we **update `max length` to 5**.

---

This illustrates how the sliding window intelligently maintains the **longest substring without repeating characters** by:

* Updating `left` when duplicates **within** the window are found
* Skipping updates if duplicates are **outside** the current window
* Tracking all seen characters with their latest index

---

### ✅ Final Step: Return Result

**String:** `"abcdbea"`

---

### 🔍 Traversal Recap

| Index | Character | Seen Map Updated To           |
| ----- | --------- | ----------------------------- |
| 0     | a         | a → 0                         |
| 1     | b         | b → 1                         |
| 2     | c         | c → 2                         |
| 3     | d         | d → 3                         |
| 4     | b         | b → 4 (window shifted)        |
| 5     | e         | e → 5                         |
| 6     | a         | a → 6 (not in window, update) |

---

### 📌 Final Variables:

* `left = 2`
* `right = 6`
* `current length = right - left + 1 = 5`
* `max length = 5`

---

### 🧾 Result:

* The entire string has been traversed.
* ✅ Return the **`max length = 5`** as the **length of the longest substring without repeating characters**.

---

---

### 🔍 Strategy Check: Does My Problem Match?

**Questions to ask yourself**:

* Are we dealing with subarrays/substrings?
* Do we care about the **length, sum, max, min, uniqueness** of elements inside a window?
* Are elements **contiguous**?

If yes → 🎯 Apply sliding window.

---

### 🛠️ Real-World Problems That Use Sliding Window

* Maximum sum subarray of size k
* Longest substring with k distinct characters
* Smallest subarray with sum ≥ target
* Fixed-bound subarrays (like the one you analyzed earlier)

---

### 🎯 Summary of Key Points

* Use when **contiguous segments** are involved
* Keep track of conditions within the window (e.g. sum, set size, frequency)
* Optimal for many array/string problems
* Turns brute force O(n²) to efficient O(n)

---
