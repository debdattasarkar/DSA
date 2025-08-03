
---

# Replace all 0's with 5

### Difficulty: Basic

**Accuracy**: 75.55%
**Submissions**: 91K+
**Points**: 1
**Average Time**: 15m

---

## 🧩 Problem Statement

You are given an integer `n`.
You need to **convert all zeroes of `n` to fives**.

---

## 🧪 Examples

### Example 1:

```
Input: 
n = 1004

Output:
1554

Explanation:
There are two zeroes in 1004. On replacing all zeroes with fives, 
the new number will be 1554.
```

---

### Example 2:

```
Input: 
n = 121

Output:
121

Explanation:
Since there are no zeroes in 121, the number remains unchanged.
```

---

## 📚 Constraints:

```
0 <= n <= 10^4
```

---

## ✅ Expected Complexities:

* **Time Complexity**: O(k), where k is the number of digits in `n`.
* **Auxiliary Space**: O(1)

---

## 🏷️ Company Tags:

* Amazon

---

## 🧠 Topic Tags:

* `Arrays`, `Mathematical`, `Data Structures`, `Algorithms`

---

## 📄 Related Articles:

* [Replace 0 5 Input Integer](https://www.geeksforgeeks.org/replace-0-5-input-integer/)

---

---
Here's a complete explanation, dry run, and optimal implementation for the problem **"Replace all 0's with 5"**.

---

## ✅ Step-by-Step Explanation

### Problem:

Given an integer `n`, replace **every `0` digit** in `n` with `5` and return the new number.

### Example 1:

```
Input: n = 1004
Output: 1554

Explanation:
Digits in 1004 → ['1', '0', '0', '4']
Replace 0s → ['1', '5', '5', '4'] → 1554
```

### Example 2:

```
Input: n = 121
Output: 121

Explanation:
No 0s to replace, so return number as is.
```

---

## 🔍 Dry Run (with n = 1004)

**Initial number:** 1004
**Convert to string:** '1004'
**Iterate each character:**

* '1' → keep
* '0' → replace with '5'
* '0' → replace with '5'
* '4' → keep

**Final string:** '1554'
**Convert back to int:** 1554 → ✅

---

## ✅ Optimized Code


## 🐍 Python Code (Mathematical Version)

```python
class Solution:
    def convertFive(self, n):
        if n == 0:
            return 5

        result = 0
        place = 1

        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5
            result += digit * place
            place *= 10
            n //= 10

        return result

```

### 🐍 Python (String-based approach)

```python
# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Convert number to string, replace '0' with '5', and convert back to int
        return int(str(n).replace('0', '5'))
```
---

### 🧑‍💻 C++

```cpp
class Solution {
  public:
    int convertFive(int n) {
        if (n == 0) return 5;

        int result = 0, place = 1;

        while (n > 0) {
            int digit = n % 10;
            if (digit == 0)
                digit = 5;

            result += digit * place;
            place *= 10;
            n /= 10;
        }

        return result;
    }
};
```

---

### 🌐 JavaScript

```javascript
/**
 * @param {number} num
 * @returns {number}
 */
class Solution {
    convertFive(num) {
        // Convert number to string, replace '0' with '5', then parse to int
        return parseInt(num.toString().replace(/0/g, '5'));
    }
}
```

---

## 🎯 Interview Q\&A

### Q1: What is the time and space complexity?

* **Time Complexity:** O(k), where k is the number of digits in `n`
* **Space Complexity:** O(1) if string conversion is constant-space, else O(k)

---

### Q2: Can this problem be solved without string manipulation?

Yes. You can extract each digit using `% 10`, convert 0 to 5, and reconstruct the number. This is shown in the C++ version.

---

### Q3: What happens when n = 0?

Return `5`, because we treat 0 as a digit to replace.

---

### Q4: Can the number have leading zeroes?

No, since `int` type doesn't store leading zeroes. Only internal zeroes are relevant.

---

### Q5: Why use string conversion in Python/JS?

Because string operations like `replace()` are simple and readable for this task, and they're optimal for small inputs like integers.

---

### 🔍 Which is **preferred in interviews**?

| Interview Style                             | Preferred Approach                                 |
| ------------------------------------------- | -------------------------------------------------- |
| **Python developer**                        | String-based (concise, Pythonic)                   |
| **Core DSA/data structure/system roles**    | Arithmetic (shows understanding of number systems) |
| **Embedded/C++/low-level roles**            | Arithmetic (avoid string conversion)               |
| **Competitive coding or tight constraints** | Arithmetic (faster and leaner)                     |

---

### 🔥 Verdict:

**Use the arithmetic version** in interviews unless the interviewer is okay with a Pythonic one-liner. It shows deeper algorithmic understanding and avoids abstracted operations like string handling.


### 🤔 Which approach is better?
- Use **math-based** if you want to avoid strings (e.g., in embedded systems).
- Use **string-based** for simplicity and readability in higher-level languages like Python or JS.

Want to compare their performance side-by-side or test edge cases like `0000` and `1000`?

Awesome! Let’s **compare the math-based and string-based solutions** side-by-side using a few edge test cases to ensure they work as expected across different scenarios like:

- `0` (edge case where input is exactly zero)
- `1000` (multiple zeros)
- `5050` (mix of fives and zeros)
- `9999` (no zeros)
- `0000` (not valid as input, since it's just `0`)

---

### ✅ Test Cases & Expected Output:

| Input  | Expected Output |
|--------|-----------------|
| 0      | 5               |
| 1000   | 1555            |
| 5050   | 5555            |
| 9999   | 9999            |
| 0000   | 5               |

---

## 🐍 Python: Compare Both Approaches

```python
def math_based(n):
    if n == 0:
        return 5

    result = 0
    place = 1
    while n > 0:
        digit = n % 10
        if digit == 0:
            digit = 5
        result += digit * place
        place *= 10
        n //= 10
    return result

def string_based(n):
    return int(str(n).replace('0', '5')) if n != 0 else 5

# Test all cases
test_cases = [0, 1000, 5050, 9999, int("0000")]

print("Input | Math-Based | String-Based | Same?")
print("------|------------|--------------|------")
for n in test_cases:
    m = math_based(n)
    s = string_based(n)
    print(f"{n:<5} | {m:<10} | {s:<12} | {'✅' if m == s else '❌'}")
```

---

### ✅ Output
```
Input | Math-Based | String-Based | Same?
------|------------|--------------|------
0     | 5          | 5            | ✅
1000  | 1555       | 1555         | ✅
5050  | 5555       | 5555         | ✅
9999  | 9999       | 9999         | ✅
0     | 5          | 5            | ✅
```

✅ **Both approaches produce identical results**, even on tricky edge cases!

---
Excellent question! Let's break down the **time and space complexity** for both approaches — **Math-Based** and **String-Based** — to help you understand their performance trade-offs ⚖️

---

## ⚙️ **Time & Space Complexity Analysis**

Let:
- `n` be the input number
- `k` be the number of digits in `n` (i.e., `k = log₁₀(n) + 1`)

---

### ✅ **Math-Based Approach**

#### Code Logic Recap:
- Use `% 10` and `/ 10` to extract and modify digits.
- Rebuild the number using `digit * place`.

#### ⏱️ Time Complexity:
- `O(k)` → One pass through all digits.

#### 🧠 Space Complexity:
- `O(1)` → Uses a few integer variables: `result`, `place`, `digit`.

#### ✅ Pros:
- Very memory-efficient.
- Great for constrained environments (e.g., embedded systems).

#### ❌ Cons:
- Slightly more complex to write/read than the string method.

---

### ✅ **String-Based Approach**

#### Code Logic Recap:
- Convert number to string, replace `'0'` with `'5'`, convert back to int.

#### ⏱️ Time Complexity:
- `O(k)` → String conversion, traversal, and replacement are linear in number of digits.

#### 🧠 Space Complexity:
- `O(k)` → Needs extra space to hold the string version of the number.

#### ✅ Pros:
- Easier to write and understand.
- More readable, especially in high-level languages like Python/JavaScript.

#### ❌ Cons:
- Slightly higher memory usage due to string construction.
- Not ideal for systems with limited memory.

---

## 📊 **Complexity Comparison Table**

| Approach       | Time Complexity | Space Complexity | Simplicity | Efficiency |
|----------------|------------------|-------------------|------------|------------|
| Math-Based     | O(k)             | O(1)              | ❌ Medium  | ✅ Best     |
| String-Based   | O(k)             | O(k)              | ✅ Easy    | ⚠️ Moderate |

---

## 🧠 When to Use What?

- **Math-Based**:
  - When memory is tight (e.g., competitive coding, embedded systems).
  - When you want full control over number manipulation.

- **String-Based**:
  - When code clarity and speed of development matter more.
  - Ideal in Python, JavaScript, and scripting-heavy tasks.