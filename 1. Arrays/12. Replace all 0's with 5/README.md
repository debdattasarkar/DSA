The problem is simple but fun — it’s called **“Replace all 0's with 5”**. Let’s break it down and solve it across **C++**, **Python**, and **JavaScript** 🧠💡

---

## ✅ **Problem Summary**
You are given an integer `n`. Replace **every digit `0`** in `n` with **`5`**, and return the modified number.

---

## 🧮 Constraints:
- `0 <= n <= 10^4`  
- Time: `O(k)`, where `k = number of digits`  
- Space: `O(1)`

---

## ✅ Example:
```text
Input:  1004
Output: 1554

Input:  121
Output: 121
```

---

## 🧑‍💻 C++ Code (With Inline Comments)
```cpp
#include <iostream>
using namespace std;

int convertZeroToFive(int n) {
    if (n == 0)
        return 5;

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

int main() {
    int n;
    cin >> n;
    cout << convertZeroToFive(n) << endl;
    return 0;
}
```

---

## 🐍 Python Code (With Inline Comments)
```python
def convert_zero_to_five(n):
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

# Example usage
n = int(input())
print(convert_zero_to_five(n))
```

---

## 🌐 JavaScript Code (With Inline Comments)
```javascript
function convertZeroToFive(n) {
    if (n === 0) return 5;

    let result = 0;
    let place = 1;

    while (n > 0) {
        let digit = n % 10;
        if (digit === 0) digit = 5;
        result += digit * place;
        place *= 10;
        n = Math.floor(n / 10);
    }

    return result;
}

// Example usage
let n = parseInt(prompt("Enter number:"));
console.log(convertZeroToFive(n));
```

---

### 🧠 Key Insight
We don’t convert the number to string (though you could). This approach uses **mathematical digit manipulation**, making it efficient and suitable for larger inputs with constant space.

### String-based solution:

---

Awesome! Let's now solve the **“Replace all 0's with 5”** problem using a **string-based approach**. This can be a bit more intuitive, especially for beginners, and it's still efficient for the input range in this problem.

---

### ✅ Logic (String-Based):
1. Convert the number to a string.
2. Replace all `'0'` characters with `'5'`.
3. Convert the modified string back to an integer.

---

## 🧑‍💻 C++ (String-Based)

```cpp
#include <iostream>
#include <string>
using namespace std;

int convertZeroToFive(int n) {
    // Edge case: if input is 0, return 5 directly
    if (n == 0) return 5;

    string s = to_string(n);
    for (char &ch : s) {
        if (ch == '0')
            ch = '5';
    }
    return stoi(s); // Convert back to integer
}

int main() {
    int n;
    cin >> n;
    cout << convertZeroToFive(n) << endl;
    return 0;
}
```

---

## 🐍 Python (String-Based)

```python
def convert_zero_to_five(n):
    # Convert to string, replace '0' with '5', then convert back to int
    return int(str(n).replace('0', '5')) if n != 0 else 5

# Example usage
n = int(input())
print(convert_zero_to_five(n))
```

---

## 🌐 JavaScript (String-Based)

```javascript
function convertZeroToFive(n) {
    if (n === 0) return 5;

    // Convert number to string, replace '0' with '5', then parse back to int
    return parseInt(n.toString().replace(/0/g, '5'));
}

// Example usage
let n = parseInt(prompt("Enter number:"));
console.log(convertZeroToFive(n));
```

---

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
