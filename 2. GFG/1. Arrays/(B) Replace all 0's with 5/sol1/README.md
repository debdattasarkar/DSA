
---

## ✅ Full Python Program

```python
import time

class Solution:
    def convertFive(self, n):
        # Edge case: if number is 0, return 5
        if n == 0:
            return 5

        result = 0     # Final number with 0s replaced by 5
        place = 1      # Used to build number from right to left

        while n > 0:
            digit = n % 10  # Extract last digit

            if digit == 0:
                digit = 5   # Replace 0 with 5

            # Rebuild the number from right to left
            result += digit * place

            # Move to next digit
            place *= 10
            n //= 10

        return result
```

---

## 🧪 Driver Code + Timer

```python
if __name__ == "__main__":
    sol = Solution()

    # Sample input
    test_numbers = [102, 0, 1004, 9000, 12345, 5050]
    
    for n in test_numbers:
        print(f"\nInput: {n}")
        start_time = time.time()  # Start timer

        result = sol.convertFive(n)

        end_time = time.time()    # End timer

        print(f"Output: {result}")
        print(f"Execution Time: {end_time - start_time:.8f} seconds")
```

---

## 🧠 Dry Run Example

For `n = 102`:

* Initial: `result = 0`, `place = 1`
* 102 % 10 = 2 → result = 2 × 1 = 2
* 10 % 10 = 0 → convert to 5 → result += 5 × 10 = 50 + 2 = 52
* 1 % 10 = 1 → result += 1 × 100 = 100 + 52 = 152

**Final Output: `152`**

---

## ⏱ Time & Space Complexity

| Step                       | Time Complexity | Space Complexity | Notes                         |
| -------------------------- | --------------- | ---------------- | ----------------------------- |
| Extract and rebuild digits | O(d)            | O(1)             | `d` = number of digits in `n` |
| Total                      | **O(log₁₀n)**   | **O(1)**         | Efficient digit-wise solution |

---

## ✅ Sample Output

```
Input: 102
Output: 152
Execution Time: 0.000000XX seconds

Input: 0
Output: 5
Execution Time: 0.000000XX seconds

Input: 1004
Output: 1554
Execution Time: 0.000000XX seconds

Input: 9000
Output: 9555
Execution Time: 0.000000XX seconds

Input: 12345
Output: 12345
Execution Time: 0.000000XX seconds

Input: 5050
Output: 5555
Execution Time: 0.000000XX seconds
```

---

Here's your program annotated with **time and space complexity for each line** showing how complexity evolves throughout execution:

---

```python
import time  # O(1) import — no runtime complexity

class Solution:
    def convertFive(self, n):
        # Edge case: if number is 0, return 5
        if n == 0:
            return 5
        # Time: O(1), Space: O(1)

        result = 0     # Initialize result variable
        place = 1      # Place value tracker (1, 10, 100...)
        # Time: O(1), Space: O(1) — both are simple scalar variables

        while n > 0:
            digit = n % 10          # Extract last digit
            # Time: O(1), Space: O(1)

            if digit == 0:
                digit = 5           # Replace 0 with 5
            # Time: O(1), Space: O(1)

            result += digit * place  # Add to result
            # Time: O(1), Space: O(1)

            place *= 10             # Increase place value
            # Time: O(1), Space: O(1)

            n //= 10                # Remove last digit
            # Time: O(1), Space: O(1)

        return result
        # Time: O(1), Space: O(1)
```

---

### 🧠 Accumulated Time & Space Complexity

Let’s denote `d = number of digits in n`.

| Loop Iterations           | Time Complexity | Space Complexity    |
| ------------------------- | --------------- | ------------------- |
| While loop runs `d` times | O(d) overall    | O(1) scalar storage |

---

### ✅ Final Time and Space Complexity

* **Time Complexity**: `O(log₁₀ n)` ≈ `O(d)`, where `d` is the number of digits in `n`
* **Space Complexity**: `O(1)` — only fixed-size integer variables (`result`, `place`, `digit`)

---

Here's your program with **time and space complexity increases shown line-by-line** in the form of comments:

```python
import time  # O(1) time & space for importing module

class Solution:
    def convertFive(self, n):
        # Edge case: if number is 0, return 5
        if n == 0:                      # O(1) time, O(1) space
            return 5                    # O(1) time, O(1) space

        result = 0     # Final number with 0s replaced by 5
        place = 1      # Used to build number from right to left
        # Both are O(1) space, initialized once

        while n > 0:                    # Loop runs for d digits → O(d) time
            digit = n % 10              # O(1) time, O(1) space (single int)

            if digit == 0:              # O(1)
                digit = 5               # O(1)

            result += digit * place     # O(1) time per digit
            place *= 10                 # O(1)
            n //= 10                    # O(1)

        return result                   # O(1)
```

---

## 🔍 Line-by-Line Time and Space Complexity Summary

| Line                         | Time per operation | Cumulative Time | Space Impact |
| ---------------------------- | ------------------ | --------------- | ------------ |
| `if n == 0:`                 | O(1)               | O(1)            | O(1)         |
| `result = 0; place = 1`      | O(1)               | O(1)            | O(1)         |
| `while n > 0:` loop          | O(d)               | O(d)            | O(1)         |
| → `digit = n % 10`           | O(1)               | O(d)            | O(1)         |
| → `if digit == 0: digit = 5` | O(1)               | O(d)            | O(1)         |
| → `result += digit * place`  | O(1)               | O(d)            | O(1)         |
| → `place *= 10`              | O(1)               | O(d)            | O(1)         |
| → `n //= 10`                 | O(1)               | O(d)            | O(1)         |
| `return result`              | O(1)               | O(d)            | O(1)         |

---

## 🧠 Final Complexity

* **Time Complexity**: `O(d)`
  where `d = number of digits in n` ⇒ `O(log₁₀n)`
* **Space Complexity**: `O(1)`
  only constant variables used (`result`, `place`, `digit`)

Let me know if you'd like the same for the string-based version!

