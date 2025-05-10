To solve the problem of **summing two numbers represented as arrays**, where each array element is a digit, we simulate digit-by-digit addition from the least significant digit (end of arrays) to the most significant digit, handling carry-over.

---

### 🔍 Step-by-Step Dry Run

**Input:**
`arr1 = [5, 6, 3]`
`arr2 = [8, 4, 2]`
These represent 563 and 842.

We add them:

* 3 + 2 = 5 (no carry)
* 6 + 4 = 10 → put 0, carry 1
* 5 + 8 + 1(carry) = 14 → put 4, carry 1
* End of arrays but carry remains → put 1

**Output:** `[1, 4, 0, 5]` (represents 1405)

---

### ✅ Python Code (with inline comments)

```python
class Solution:
    def findSum(self, arr1, arr2):
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result = []

        # Add digits from end of both arrays
        while i >= 0 or j >= 0 or carry:
            digit1 = arr1[i] if i >= 0 else 0
            digit2 = arr2[j] if j >= 0 else 0
            total = digit1 + digit2 + carry

            result.append(total % 10)     # Add last digit of sum
            carry = total // 10           # Carry forward the remaining part

            i -= 1
            j -= 1

        result.reverse()  # Reverse to get the most significant digit first
        return result
```

---

### ✅ C++ Code (with inline comments)

```cpp
class Solution {
  public:
    vector<int> findSum(vector<int> &arr1, vector<int> &arr2) {
        int i = arr1.size() - 1;
        int j = arr2.size() - 1;
        int carry = 0;
        vector<int> result;

        while (i >= 0 || j >= 0 || carry) {
            int digit1 = (i >= 0) ? arr1[i] : 0;
            int digit2 = (j >= 0) ? arr2[j] : 0;
            int total = digit1 + digit2 + carry;

            result.push_back(total % 10); // store unit digit
            carry = total / 10;           // keep carry

            i--;
            j--;
        }

        reverse(result.begin(), result.end());
        return result;
    }
};
```

---

### ✅ JavaScript Code (with inline comments)

```javascript
class Solution {
    findSum(arr1, arr2) {
        let i = arr1.length - 1;
        let j = arr2.length - 1;
        let carry = 0;
        let result = [];

        while (i >= 0 || j >= 0 || carry > 0) {
            let digit1 = i >= 0 ? arr1[i] : 0;
            let digit2 = j >= 0 ? arr2[j] : 0;
            let total = digit1 + digit2 + carry;

            result.push(total % 10); // push the last digit
            carry = Math.floor(total / 10); // update carry

            i--;
            j--;
        }

        result.reverse(); // since we added digits from least to most significant
        return result;
    }
}
```

---


