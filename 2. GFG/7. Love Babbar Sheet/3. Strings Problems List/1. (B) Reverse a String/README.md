# Reverse a String 🔁

**Difficulty:** Basic  
**Accuracy:** 69.49%  
**Submissions:** 427K+  
**Points:** 1  
**Average Time:** 15m  

---

## Problem Statement

You are given a string `s`, and your task is to reverse the string.

---

## Examples

### Example 1
**Input:** `s = "Geeks"`  
**Output:** `"skeeG"`

### Example 2
**Input:** `s = "for"`  
**Output:** `"rof"`

### Example 3
**Input:** `s = "a"`  
**Output:** `"a"`

---

## Constraints

- `1 <= s.size() <= 10^6`
- `s` contains only alphabetic characters (both uppercase and lowercase).

---

## Expected Complexities

- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

## Topic Tags

- Strings
- Data Structures

---

## Related Articles

- Cpp Program To Print Reverse Of A String Using Recursion
- Reverse A String In C Cpp Different Methods
- Reverse A String In Java
- String Reverse

---

---

## 2. Text explanation + step-by-step dry run

### What does “reverse a string” mean?

If `s = "Geeks"`, reversing means reading characters from end to start:

`"Geeks" → "skeeG"`

### Common approaches

1. **Two-pointer swap (in-place idea)**

   * Put one pointer at start (`left`) and one at end (`right`)
   * Swap characters, move inward
2. **Python slicing**

   * `s[::-1]` gives reversed string (clean + fastest to type)
3. **Build using loop**

   * Append characters from end to start (easy but may be slower if done naively with string concatenation)

---

### Dry run (two-pointer) for `s = "Geeks"`

We treat string as a list because Python strings are immutable.

Initial: `['G','e','e','k','s']`
`left = 0`, `right = 4`

1. Swap index 0 and 4
   `['s','e','e','k','G']`
   `left=1`, `right=3`

2. Swap index 1 and 3
   `['s','k','e','e','G']`
   `left=2`, `right=2`

Stop because `left >= right`

Join → `"skeeG"`

---

## 3. Python codes (brute + interview-expected optimized)

### ✅ Method 1: Most expected in interviews (Two pointers)

This shows the real logic (not just a shortcut).

```python
# User function Template for python3

class Solution:
    def reverseString(self, s: str) -> str:
        """
        Two-pointer reversal.

        Time:  O(n)  (each character swapped once)
        Space: O(n)  (Python strings are immutable, so we use a list copy)
        """
        # Convert string to list so we can swap characters
        characters = list(s)

        left = 0
        right = len(characters) - 1

        # Swap from outside to inside
        while left < right:
            characters[left], characters[right] = characters[right], characters[left]
            left += 1
            right -= 1

        # Convert back to string
        return "".join(characters)
```

---

### ✅ Method 2: Pythonic (shortest and common)

Great for real interviews if allowed.

```python
class Solution:
    def reverseString(self, s: str) -> str:
        """
        Python slicing.

        Time:  O(n)
        Space: O(n)  (creates a new string)
        """
        return s[::-1]
```

---

### ✅ Method 3: Using `reversed()` (clean + readable)

Also commonly accepted.

```python
class Solution:
    def reverseString(self, s: str) -> str:
        """
        reversed() + join.

        Time:  O(n)
        Space: O(n)
        """
        return "".join(reversed(s))
```

---

### ⚠️ Method 4: “Brute / naive” concatenation (NOT recommended for big n)

If you do `ans += char` repeatedly, it can degrade due to repeated allocations.

```python
class Solution:
    def reverseString(self, s: str) -> str:
        """
        Naive loop build (can be slower for large strings).

        Time:  O(n^2) worst-case in Python due to repeated concatenation
        Space: O(n)
        """
        reversed_string = ""
        for ch in s:
            reversed_string = ch + reversed_string
        return reversed_string
```

---

## 4. Interview: How to remember quickly + expected Q&A

### Quick memory trick

Think:

> **“Swap ends, move inward.”**
> (two pointers: `left`, `right`)

### 5-line pseudo template (easy recall)

```text
convert string to list
left=0, right=n-1
while left < right:
    swap(list[left], list[right])
    left++, right--
join list to string and return
```

---

### Expected Interview Questions & Answers

**Q1. Why convert to list in Python?**
✅ Because Python strings are **immutable**, you can’t swap characters in-place.

---

**Q2. What’s the time complexity?**
✅ All good methods take **O(n)** time because each character is processed once.

---

**Q3. What’s the space complexity?**
✅ In Python, reversing creates a new string anyway → typically **O(n)** space.

---

**Q4. Which method would you choose in a coding interview?**
✅ If interviewer wants logic: **two-pointer swap**.
✅ If they accept Python built-ins: `s[::-1]` is simplest and clean.

---

**Q5. Why is repeated concatenation bad?**
✅ Strings are immutable → every concatenation allocates a new string → can become **O(n²)**.

---

---

## 5. Real-World Use Cases (few, very relatable)

1. **Palindrome / Symmetry checks**

   * Many validation tasks check if a string reads the same forward/backward (usernames, IDs, patterns).
   * Reversal is the first step: compare `s` with `reverse(s)`.

2. **Text processing / formatting**

   * Reversing tokens or strings is common in editors/compilers (e.g., reversing a word, reversing a buffer, undo-like transformations).

3. **Low-level data transformations**

   * In systems/embedded contexts, you often reverse character buffers for tasks like converting numbers to strings (build digits backward, then reverse).

---

## 6. Full Program (with timing + inline time/space complexity comments)

This full runnable program:

* reads a string `s`
* reverses it using the **two-pointer** method (interview-friendly logic)
* prints the reversed string
* prints runtime (algorithm runtime)

```python
import time


# User function Template for python3
class Solution:
    def reverseString(self, s: str) -> str:
        """
        Two-pointer reversal (interview-friendly).

        Time:  O(n)  -> each character swapped at most once
        Space: O(n)  -> Python strings are immutable; list copy is needed
        """
        # Step 1: Convert to list so we can swap characters
        # Time:  O(n)
        # Space: O(n)
        chars = list(s)

        # Step 2: Two pointers
        # Time:  O(1)
        # Space: O(1)
        left = 0
        right = len(chars) - 1

        # Step 3: Swap inward
        # Loop runs about n/2 times => O(n)
        # Space inside loop: O(1)
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        # Step 4: Join back to string
        # Time:  O(n)
        # Space: O(n) for final string
        return "".join(chars)


def main():
    """
    Input:
        A single string s (can contain uppercase/lowercase alphabets)
    Output:
        Reversed string

    Example Input:
        Geeks
    Example Output:
        skeeG
    """

    print("Enter string s:")
    s = input().strip()

    solver = Solution()

    # Start timing the algorithm run (not the user typing time)
    start_time = time.perf_counter()

    reversed_s = solver.reverseString(s)

    end_time = time.perf_counter()

    print("\nReversed string:", reversed_s)
    print(f"Total elapsed time (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

### Sample Run

**Input**

```text
Geeks
```

**Output**

```text
Reversed string: skeeG
Total elapsed time (seconds): 0.0000xx
```

