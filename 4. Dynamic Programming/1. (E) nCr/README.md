Here's a full explanation, dry run, and Python/C++/JavaScript solutions for the **nCr (Binomial Coefficient)** problem.

---

### 🔍 Problem Summary

Given two integers `n` and `r`, compute the binomial coefficient:

$$
^nC_r = \frac{n!}{r!(n-r)!}
$$

Return `0` if `r > n`.

### ✅ Constraints

* `1 ≤ n, r ≤ 100`
* Answer fits in 32-bit integer

---

### 🧠 Explanation

We use a dynamic programming approach to avoid computing full factorials which can be expensive and cause overflow.

Let’s define a 1D array `C` where `C[j]` will hold the value of `nCr` for current `i`.

We use the recurrence:

$$
C(j) = C(j) + C(j-1)
$$

It uses the identity:

$$
^nC_r = ^{n-1}C_r + ^{n-1}C_{r-1}
$$

This builds the Pascal’s Triangle iteratively.

---

### 🧪 Step-by-Step Dry Run (n = 5, r = 2)

We want:

$$
^5C_2 = \frac{5!}{2!(5-2)!} = \frac{120}{2 \cdot 6} = 10
$$

DP array updates like:

```
i = 0: [1]
i = 1: [1, 1]
i = 2: [1, 2, 1]
i = 3: [1, 3, 3]
i = 4: [1, 4, 6]
i = 5: [1, 5, 10]
```

Answer = 10

---

### 🐍 Python Code (with inline comments)

```python
class Solution:
    def nCr(self, n, r):
        # Return 0 if r > n (invalid case)
        if r > n:
            return 0

        # Initialize DP array
        C = [0] * (r + 1)
        C[0] = 1  # Base case: nC0 = 1

        for i in range(1, n + 1):
            # Fill the array from right to left
            for j in range(min(i, r), 0, -1):
                C[j] = C[j] + C[j - 1]

        return C[r]
```

---

### 💠 C++ Code

```cpp
class Solution {
  public:
    int nCr(int n, int r) {
        if (r > n) return 0;
        int C[r + 1];
        memset(C, 0, sizeof(C));
        C[0] = 1;

        for (int i = 1; i <= n; i++) {
            for (int j = min(i, r); j > 0; j--) {
                C[j] = C[j] + C[j - 1];
            }
        }

        return C[r];
    }
};
```

---

### 🌐 JavaScript Code

```javascript
class Solution {
    nCr(n, r) {
        if (r > n) return 0;
        let C = new Array(r + 1).fill(0);
        C[0] = 1;

        for (let i = 1; i <= n; i++) {
            for (let j = Math.min(i, r); j > 0; j--) {
                C[j] = C[j] + C[j - 1];
            }
        }

        return C[r];
    }
}
```

---

Let me know if you'd like to see the factorial-based implementation or a modulo version (often used in competitive programming).
