Let's explore **Leetcode 344 – Reverse String**, a simple and classic **Two Pointer** problem.

---

## 🔍 Problem Statement

> Write a function that reverses a string.
> The input string is given as an array of characters `s`.
>
> You must do this **in-place** with **O(1)** extra memory.

---

### 🧪 Example

```python
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

---

## ✅ Approach: Two Pointer (In-Place Swap)

### 💡 Strategy:

* Use two pointers: `left = 0`, `right = len(s) - 1`
* Swap characters at `left` and `right`, then move inward
* Stop when `left >= right`

---

## 🧑‍💻 Python Code with Inline Comments

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Swap characters at left and right
            s[left], s[right] = s[right], s[left]
            
            # Move pointers inward
            left += 1
            right -= 1
```

---

## ⏱ Time and Space Complexity

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n)            |
| Space  | O(1) (in-place) |

---

## 🧠 Dry Run

Input:

```python
s = ["h", "e", "l", "l", "o"]
```

| Step | Left | Right | Swap  | Result                     |
| ---- | ---- | ----- | ----- | -------------------------- |
| 1    | 0    | 4     | h ↔ o | \["o", "e", "l", "l", "h"] |
| 2    | 1    | 3     | e ↔ l | \["o", "l", "l", "e", "h"] |
| 3    | 2    | 2     | done  | stop                       |

✅ Final Output: `["o", "l", "l", "e", "h"]`

---

## ❓ Interview Q\&A

| Question                            | Answer                                             |
| ----------------------------------- | -------------------------------------------------- |
| Can you return a new array?         | No, must modify `s` in-place                       |
| What if input is string, not array? | Strings are immutable — convert to list first      |
| Can this be done recursively?       | Yes, but loses O(1) space requirement (stack used) |

---

## 📦 Real-World Use Cases

* Reversing **input buffers** (e.g., stream read from end)
* Processing **palindromes**
* Low-level in-place string reversal (e.g., char arrays in C)

---
