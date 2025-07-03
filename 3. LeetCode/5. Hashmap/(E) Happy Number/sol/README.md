
---

## ✅ Python Implementation (With Floyd’s Cycle Detection)

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            """
            Compute the next number as the sum of squares of digits of `num`.

            Time Complexity: O(log n)
            Space Complexity: O(1)
            """
            total = 0
            while num > 0:
                digit = num % 10          # Extract last digit
                total += digit * digit    # Square and add to total
                num //= 10                # Remove last digit
            return total

        slow = n                    # Pointer 1 starts at n
        fast = get_next(n)         # Pointer 2 is one step ahead

        # Main loop to detect cycle using Floyd's algorithm
        while fast != 1 and slow != fast:
            slow = get_next(slow)                 # Move slow by 1 step
            fast = get_next(get_next(fast))       # Move fast by 2 steps

        # If fast reaches 1, then it's a happy number
        return fast == 1
```

---

## ✅ Time & Space Complexity

| Step                       | Time Complexity  | Space Complexity | Notes                               |
| -------------------------- | ---------------- | ---------------- | ----------------------------------- |
| `get_next(num)` per call   | O(log n)         | O(1)             | log base 10, for digit iteration    |
| While loop iteration count | O(log n) \* k    | O(1)             | At most k unique states (k ≪ n)     |
| Overall                    | **O(log n × k)** | **O(1)**         | Efficient with constant extra space |

> Where `k` is the number of steps before detecting cycle or reaching 1.

---

## 🧪 Example Input & Output

### Input

```python
n = 19
```

### Dry Run

```
19 → 1² + 9² = 82
82 → 8² + 2² = 68
68 → 6² + 8² = 100
100 → 1² + 0² + 0² = 1 ✅
```

### Output

```python
True
```

---

## 💡 Interview Insight

Interviewers love asking:

* “How would you detect cycles without extra space?”
* “Can you optimize your current solution’s space from O(n) to O(1)?”
* “Why does Floyd’s algorithm work here despite being commonly used on linked lists?”

You should also be ready to explain:

* How the sequence of numbers is bounded (due to digit square sum not growing indefinitely).
* Why the sequence eventually enters a cycle if not happy.

---
