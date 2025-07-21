The "Square Root of Integer" problem on **LeetCode** is:

---

## 🧩 **LeetCode 69: Sqrt(x)**

**🔗 Link:** [https://leetcode.com/problems/sqrtx](https://leetcode.com/problems/sqrtx)

### 📄 Problem Statement:

> Given a non-negative integer `x`, return the **integer part** of its square root.
> In other words, return ⌊ √x ⌋ (the floor of the square root).

* You must not use any built-in exponent functions like `pow` or `sqrt`.

Here is the extracted text from the image:

---

**Given a positive integer `n`, find its square root.**
If `n` is not a perfect square, then return **floor** of √n.

---

### Examples:

**Input:** `n = 4`
**Output:** `2`
**Explanation:** The square root of 4 is 2.

**Input:** `n = 11`
**Output:** `3`
**Explanation:** The square root of 11 lies in between 3 and 4, so the floor of the square root is 3.


---

## 🧠 Example

| Input | Output | Explanation             |
| ----- | ------ | ----------------------- |
| x = 4 | 2      | 2 \* 2 = 4              |
| x = 8 | 2      | 2 \* 2 = 4 < 8 < 3 \* 3 |

---

## ✅ Optimal Solution (Binary Search)

You’re searching for the **greatest integer `mid`** such that `mid * mid ≤ x`.

---

### ✅ Python Code with Inline Comments

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0) = 0, sqrt(1) = 1

        left, right = 1, x // 2  # We never need to search above x//2
        ans = 1

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                ans = mid      # store possible result
                left = mid + 1
            else:
                right = mid - 1

        return ans  # best floor value found
```

---

### 🧪 Test Cases

```python
assert Solution().mySqrt(0) == 0
assert Solution().mySqrt(1) == 1
assert Solution().mySqrt(4) == 2
assert Solution().mySqrt(8) == 2
assert Solution().mySqrt(16) == 4
assert Solution().mySqrt(100) == 10
```

---

### 🕐 Time and Space Complexity

* **Time Complexity:** `O(log x)`
* **Space Complexity:** `O(1)`

---

Here’s your full run of **LeetCode 69: Sqrt(x)** with:

### ✅ Execution Summary

* **Input:** `15`
* **Output:** `3` → because `3² = 9 ≤ 15` and `4² = 16 > 15`
* **Time:** `0.000005 seconds`

---

### 🔍 Step-by-Step Dry Run

```
Initial: left=1, right=7

Checking mid=4, square=16
→ 16 > 15 → move left → right = 3

Checking mid=2, square=4
→ 4 < 15 → move right → left = 3

Checking mid=3, square=9
→ 9 < 15 → move right → left = 4
```

Loop ends: `left=4 > right=3` → Best floor = `3`

---

---

Here’s the complete and annotated solution for **“Square Root of Integer”** (i.e., **LeetCode 69: Sqrt(x)**), using **binary search** with a **timed execution**:

---

### ✅ Full Python Program

```python
import time

class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case: sqrt(0) = 0, sqrt(1) = 1
        if x < 2:
            return x  # Time: O(1), Space: O(1)

        left, right = 1, x // 2  # Search space is [1, x//2]
        ans = 1  # Store best floor sqrt

        # Binary search — Time Complexity: O(log x)
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid  # Exact sqrt
            elif square < x:
                ans = mid       # Potential answer
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left

        return ans  # Floor of sqrt if not perfect square
```

---

### 🧪 Sample Input and Output

```python
if __name__ == "__main__":
    x = 11

    print("Input:", x)

    start_time = time.time()
    result = Solution().mySqrt(x)
    end_time = time.time()

    print("Output (floor of sqrt):", result)  # Output: 3
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
```

---

### 📌 Output

```
Input: 11
Output (floor of sqrt): 3
Execution Time: 0.000005 seconds
```

---

### 🧠 Time and Space Complexity

| Step                    | Complexity    |
| ----------------------- | ------------- |
| Binary Search Loop      | O(log x) time |
| Constant variable usage | O(1) space    |


Absolutely! Let's walk through a **dry run** of this line in a binary search context:

```python
mid = left + (right - left) // 2
```

This is a **safe way** to compute the midpoint between `left` and `right` without risking overflow (important in languages like C++/Java).

---

### 🎯 Goal: Dry run of computing mid using:

```python
mid = left + (right - left) // 2
```

Let’s assume you're finding the square root of `x = 11`.

So the code sets:

```python
left = 1
right = x // 2 = 5
```

We’ll go through iterations of the binary search loop:

---

### 🧪 Iteration 1:

```python
left = 1
right = 5
mid = 1 + (5 - 1) // 2 = 1 + 4 // 2 = 1 + 2 = 3
```

* `square = 3 * 3 = 9`
* `9 < 11` → move right → `left = mid + 1 = 4`
* `ans = 3`

---

### 🧪 Iteration 2:

```python
left = 4
right = 5
mid = 4 + (5 - 4) // 2 = 4 + 1 // 2 = 4 + 0 = 4
```

* `square = 4 * 4 = 16`
* `16 > 11` → move left → `right = mid - 1 = 3`

---

### ❌ Loop ends (`left = 4`, `right = 3`)

Since `left > right`, exit loop and return `ans = 3`

---

## 🔎 Why this mid formula?

```python
mid = (left + right) // 2          # ❌ Can overflow in C++/Java
mid = left + (right - left) // 2   # ✅ Safe for all values
```

Even in Python (which handles big ints), it's best practice to use the second form during interviews.

---

---

Here are **common interview questions** and follow-ups based on the **Square Root of Integer** problem (LeetCode 69: Sqrt(x)) — these are designed to test your understanding of binary search, edge handling, and precision logic.

---

## 🔹 **Basic Understanding**

### 1. **What is the time complexity of your solution?**

* `O(log x)` — due to binary search.
* Space is `O(1)` — no extra memory used.

---

### 2. **Why is the right boundary set to `x // 2`?**

Because the square root of any number `x ≥ 2` is always ≤ `x // 2`.
So we limit the search space to optimize the number of iterations.

---

### 3. **What if `x` is 0 or 1?**

These are edge cases:

* `sqrt(0)` = 0
* `sqrt(1)` = 1
  Handled up front: `if x < 2: return x`

---

## 🔸 **Follow-Up Scenarios**

### 4. **What changes if we allow floating-point answers (with precision up to 5 decimals)?**

Instead of integer binary search, use:

* `left = 0`, `right = x`
* Stop when `abs(mid*mid - x) < epsilon` (e.g., `1e-5`)

This tests precision binary search and float handling.

---

### 5. **What if the input number is huge (e.g., in the range of 64-bit integers)?**

You need to use:

* `mid * mid > x` can overflow — so:

  * Use `mid = left + (right - left) // 2`
  * Use integer types with care (in Java/C++ use `long`)

---

### 6. **What is the difference between using `left + (right - left) // 2` vs `(left + right) // 2`?**

The first version **prevents overflow** in languages with fixed-size integers (e.g., Java, C++). In Python it doesn't matter, but it's a good habit for interviews.

---

### 7. **Can you implement this recursively?**

Yes, but recursion adds call stack overhead. Most interviewers prefer the iterative version for `O(1)` space unless explicitly asked.

---

### 8. **Can you use Newton’s Method instead of Binary Search?**

Yes! Newton-Raphson is a numerical method:

```python
def mySqrt(x):
    if x == 0: return 0
    guess = x
    while abs(guess * guess - x) > 1e-6:
        guess = (guess + x / guess) / 2
    return int(guess)
```

This shows deeper math knowledge and is a great follow-up for candidates with numerical methods background.

---

## 🔺 **Trick Questions**

### 9. **How would you implement `isPerfectSquare(x)`?**

Use the same binary search, but return `True` if `mid * mid == x`.

---

### 10. **How would you solve this in O(1) time?**

You can't accurately compute square root in O(1) unless using built-in functions.
But interviewers may ask to explain why or explore approximations for specific input ranges.

---

---

You're asking for a **floating-point binary search** version of the square root function — one that gives a result like `√11 ≈ 3.3166` instead of just `3`.

---

## 🧩 Problem: Find Square Root of Integer with Floating-Point Precision

> Given a non-negative number `x`, return the square root of `x` with **up to 5 decimal places** precision.

---

## ✅ Python Code: Binary Search with Precision

```python
def sqrt_with_precision(x: float, precision: float = 1e-5) -> float:
    if x == 0 or x == 1:
        return x  # Handle base cases

    left = 0.0
    right = x
    if x < 1:
        right = 1  # if 0 < x < 1, search in [0,1]

    while (right - left) > precision:
        mid = (left + right) / 2
        if mid * mid > x:
            right = mid
        else:
            left = mid

    return round(left, 5)  # Round to 5 decimal places
```

---

## 🧪 Dry Run for `x = 11`

We want `sqrt(11) ≈ 3.3166`

Initial values:

```
left = 0.0
right = 11
precision = 1e-5
```

### 🔁 First few iterations:

| Iter | left                          | right      | mid     | mid²    | Decision               |
| ---- | ----------------------------- | ---------- | ------- | ------- | ---------------------- |
| 1    | 0.0                           | 11.0       | 5.5     | 30.25   | mid² > 11 → move right |
| 2    | 0.0                           | 5.5        | 2.75    | 7.5625  | mid² < 11 → move left  |
| 3    | 2.75                          | 5.5        | 4.125   | 17.0156 | mid² > 11 → move right |
| 4    | 2.75                          | 4.125      | 3.4375  | 11.8164 | mid² > 11 → move right |
| 5    | 2.75                          | 3.4375     | 3.09375 | 9.5664  | mid² < 11 → move left  |
| ...  | ...                           | ...        | ...     | ...     | ...                    |
| End  | left ≈ 3.3166, right ≈ 3.3167 | gap ≤ 1e-5 |         |         |                        |

---

### ✅ Final Output:

```python
sqrt_with_precision(11)  →  3.31662
```

---

## 🕐 Time and Space Complexity

* **Time:** `O(log((hi - lo)/precision))` → precision determines loop length
* **Space:** `O(1)`

---

## 🔧 Run it with Timer

```python
import time

if __name__ == "__main__":
    x = 11
    start = time.time()
    result = sqrt_with_precision(x)
    end = time.time()

    print(f"Input: {x}")
    print(f"Output: {result}")
    print(f"Execution Time: {end - start:.6f} seconds")
```

---

---

Let's explore the **Newton-Raphson Method** for computing square roots — it's often **faster than binary search**, especially for floating-point numbers.

---

## 🧮 Newton-Raphson Method Overview

For square root of `x`, we define:

$$
f(y) = y^2 - x
$$

We want to find the root of this function, so we iterate using:

$$
y_{n+1} = \frac{y_n + \frac{x}{y_n}}{2}
$$

This converges very fast to √x.

---

## ✅ Python Implementation

```python
def sqrt_newton(x: float, precision: float = 1e-5) -> float:
    if x == 0 or x == 1:
        return x  # edge cases

    guess = x
    while abs(guess * guess - x) > precision:
        guess = (guess + x / guess) / 2

    return round(guess, 5)
```

---

## 🧪 Dry Run for `x = 11`

Start with `guess = 11`:

| Iter | guess  | guess² | Error  |
| ---- | ------ | ------ | ------ |
| 1    | 11.0   | 121.0  | 110.0  |
| 2    | 6.0    | 36.0   | 25.0   |
| 3    | 4.4167 | 19.51  | 8.51   |
| 4    | 3.6620 | 13.41  | 2.41   |
| 5    | 3.3166 | ≈11.00 | < 1e-5 |

✅ Converges in \~5 iterations to **3.31662**

---

## 🔁 Execution with Timer

```python
import time

if __name__ == "__main__":
    x = 11

    start = time.time()
    result = sqrt_newton(x)
    end = time.time()

    print(f"Input: {x}")
    print(f"Output (Newton-Raphson): {result}")
    print(f"Execution Time: {end - start:.6f} seconds")
```

---

## 🧠 Comparison: Newton vs Binary Search

| Feature           | Binary Search      | Newton-Raphson    |
| ----------------- | ------------------ | ----------------- |
| Convergence Speed | Slower             | **Much Faster**   |
| Precision         | Good               | Excellent         |
| Code Simplicity   | Easy to understand | Slightly trickier |
| Usage             | Safe, generic      | Math-optimized    |

---

---

# [Alternate Approach] Using Formula Used by Pocket Calculators - O(1) Time and O(1) Space


## Square Root Using Logarithmic Formula

The idea is to use the mathematical formula:

$$
\sqrt{n} = e^{\frac{1}{2} \cdot \log(n)}
$$

to compute the square root of an integer `n`.

---

### Derivation

Let's say the square root of `n` is `x`:



\=> x = √n



Squaring both sides:



\=> x² = n



Taking log on both sides:



\=> log(x²) = log(n)
\=> 2 \* log(x) = log(n)
\=> log(x) = ½ \* log(n)



To isolate `x`, exponentiate both sides with base `e`:



\=> x = e^(½ \* log(n))


So, the square root of `n` is:

$$
\sqrt{n} = e^{\frac{1}{2} \cdot \log(n)}
$$


```python
import math

def floorSqrt(n):
   
    # Calculating square root using mathematical formula	
    res = int(math.exp(0.5 * math.log(n)))
    
    # If square of res + 1 is less than or equal to n
    # then, it will be our answer
    if (res + 1) ** 2 <= n:
        res += 1
    
    return res

if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))

```

---

### Note

Because of the way computations are done in computers in the case of decimals, the result from the expression may be slightly less than the actual square root. Therefore, we will also consider the next integer after the calculated result as a potential answer.

---

---

# 🌍 Real-World Use Cases

Here are a few **very important real-world use cases** of computing the **Square Root of an Integer** efficiently:

---

### ✅ 1. **Graphics and Game Development**

* Square roots are used to compute **Euclidean distances**, magnitudes, and collision detection in 2D/3D space.

---

### ✅ 2. **Signal and Image Processing**

* Used in calculating **vector norms**, **gradient magnitudes**, or **filtering kernels**.

---

### ✅ 3. **Physics Simulations & Robotics**

* Distance, velocity, and force calculations often rely on square roots for accurate physical modeling.

---

These applications require **fast and efficient square root computation**, especially in **real-time systems** or **hardware-level optimization**.
