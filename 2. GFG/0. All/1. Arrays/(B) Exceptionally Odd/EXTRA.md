
Perfect!  
You want the **twist version** where **TWO numbers** occur odd number of times — and the code for **C++** and **JavaScript**.

Let's do it 🔥:

---

## 🧠 Problem: Two Numbers Occur Odd Number of Times

Given an array where:
- Exactly **two numbers occur odd number of times**.
- All other numbers occur even times.

**Find both numbers.**

---

### 🔥 Key Idea:
- XOR of the entire array gives `xor = num1 ^ num2`.
- Now, find any **set bit** in `xor` (means `num1` and `num2` differ at that bit).
- Divide elements into **two groups** based on that bit and XOR separately.

---

### ✅ C++ Code:
```cpp
#include <vector>
using namespace std;

vector<int> twoOddNumbers(const vector<int>& arr) {
    int xor_all = 0;
    for (int num : arr) {
        xor_all ^= num;
    }

    int set_bit = xor_all & ~(xor_all - 1);  // Find rightmost set bit

    int num1 = 0, num2 = 0;
    for (int num : arr) {
        if (num & set_bit)
            num1 ^= num;
        else
            num2 ^= num;
    }

    return {max(num1, num2), min(num1, num2)};  // Larger first
}
```

### 🧪 Example Usage in C++:
```cpp
#include <iostream>

int main() {
    vector<int> arr = {4, 2, 4, 5, 2, 3, 3, 1};
    vector<int> res = twoOddNumbers(arr);
    cout << res[0] << " " << res[1] << endl;  // Output: 5 1
}
```

---

### ✅ JavaScript Code:
```javascript
function twoOddNumbers(arr) {
    let xor_all = 0;
    for (let num of arr) {
        xor_all ^= num;
    }

    let set_bit = xor_all & ~(xor_all - 1);

    let num1 = 0, num2 = 0;
    for (let num of arr) {
        if (num & set_bit) {
            num1 ^= num;
        } else {
            num2 ^= num;
        }
    }

    return [Math.max(num1, num2), Math.min(num1, num2)];
}
```

### 🧪 Example Usage in JavaScript:
```javascript
console.log(twoOddNumbers([4, 2, 4, 5, 2, 3, 3, 1]));
// Output: [5, 1]
```

---

### 📈 Quick Recap of Steps:
1. XOR all elements → gives `num1 ^ num2`.
2. Find a **set bit** where `num1` and `num2` differ.
3. Separate numbers into **two groups** based on the set bit.
4. XOR inside each group to find `num1` and `num2`.

✅ Final answer!

---

Would you like a **diagram** showing how this division happens between two groups visually? 📊 (makes it super intuitive!) 🚀