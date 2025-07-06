
---

# Celebrity Problem

**Difficulty:** Medium
**Accuracy:** 38.33%
**Submissions:** 312K+
**Points:** 4
**Average Time:** 30m

---

## 🧠 Problem Statement

A **celebrity** is a person who is known to **everyone** but **does not know anyone** at a party.

A party is being organized by some people. A square matrix `mat[][]` of size `n*n` is used to represent people at the party.

If an element at **row `i` and column `j`** is set to **1**, it means the **ith person knows the jth person**.

You need to **return the index of the celebrity** in the party. If the celebrity does not exist, return **-1**.

> **Note:** Follow 0-based indexing.

---

## ✨ Examples

### Example 1:

**Input:**

```
mat[][] = [[1, 1, 0], 
           [0, 1, 0], 
           [0, 1, 1]]
```

**Output:**

```
1
```

**Explanation:**
0th and 2nd person both know 1st person.
Therefore, **1** is the celebrity.

---

### Example 2:

**Input:**

```
mat[][] = [[1, 1], 
           [1, 1]]
```

**Output:**

```
-1
```

**Explanation:**
Since both people at the party know each other, there is **no celebrity**.

---

### Example 3:

**Input:**

```
mat[][] = [[1]]
```

**Output:**

```
0
```

---

## ✅ Constraints

* $1 \leq \text{mat.size()} \leq 1000$
* $0 \leq \text{mat}[i][j] \leq 1$
* $\text{mat}[i][i] == 1$

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷 Topic Tags

* Arrays
* Stack
* Data Structures

---

## 🏢 Company Tags

* Zoho
* Flipkart
* Amazon
* Microsoft
* Google
* Fab.com
* One97
* United Health Group

---

## 📚 Related Articles

* [The Celebrity Problem](https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1)

---

---


Here's your full request for **The Celebrity Problem**, including explanation, dry run, optimized Python code, and common interview Q\&A.

---

## 📘 Text Explanation

In a party of `n` people, a **celebrity** is someone who:

* Is **known by everyone else**, and
* **Knows no one** else.

You're given a matrix `mat[][]` of size `n x n`, where:

* `mat[i][j] == 1` means person `i` knows person `j`.
* `mat[i][j] == 0` means person `i` does not know person `j`.

### Task:

Return the **index of the celebrity**, or `-1` if no celebrity exists.

> **Note:** Self-knowledge (`mat[i][i]`) is always 1 and irrelevant to the celebrity condition.

---

## 🔍 Step-by-Step Dry Run

### Example:

```python
mat = [
 [1, 1, 0],
 [0, 1, 0],
 [0, 1, 1]
]
```

### Step 1: Start with all people → Possible candidates: 0, 1, 2

### Step 2: Eliminate based on knowing each other

* Person 0 knows 1 → 0 **cannot be celebrity**
* Person 1 does not know 0 → 1 **might be celebrity**
* Person 2 knows 1 → 2 **cannot be celebrity**

Candidate: 1

### Step 3: Validate Candidate (person 1)

* Row 1: `mat[1][0] == 0` ✅ (doesn’t know anyone)
* Column 1: `mat[0][1] == 1` and `mat[2][1] == 1` ✅ (everyone else knows 1)

✅ Output: **1**

---

## ✅ Optimized Python Solutions

### 🔸 Brute-Force Approach (O(n²)) — Check every person

```python
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        for i in range(n):
            is_celebrity = True
            for j in range(n):
                if i == j:
                    continue
                # If i knows j or j doesn't know i => i is not celebrity
                if mat[i][j] == 1 or mat[j][i] == 0:
                    is_celebrity = False
                    break
            if is_celebrity:
                return i
        return -1
```

🟡 **Time:** O(n²)
🟡 **Space:** O(1)

---

### ✅ Python Code with Inline Comments

```python
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        a, b = 0, n - 1

        # Step 1: Eliminate non-celebrities
        # Time: O(n)
        while a < b:
            if mat[a][b] == 1:
                # a knows b → a can't be celebrity
                a += 1
            else:
                # a doesn't know b → b can't be celebrity
                b -= 1

        candidate = a  # Possible celebrity

        # Step 2: Verify the candidate
        # Time: O(n)
        for i in range(n):
            if i != candidate:
                # Candidate must not know i
                # Everyone else must know candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate
```

That's an excellent and **interview-optimal** solution — known as the **Two-Pointer Elimination Approach**. Let's break it down with:

---

### ✅ **How it Works**

#### **Step 1: Elimination Phase**

You use two pointers `a` and `b`:

* If `mat[a][b] == 1`: person `a` knows person `b`, so `a` cannot be the celebrity → move `a` forward
* Else: person `a` does **not** know person `b`, so `b` cannot be the celebrity → move `b` backward

This guarantees that at the end of the loop, **only one candidate remains** (either `a` or `b`) who could possibly be the celebrity.

---

#### **Step 2: Verification Phase**

Once a candidate is found, validate that:

* The candidate knows **no one**: `mat[candidate][i] == 0` for all `i ≠ candidate`
* Everyone else knows the candidate: `mat[i][candidate] == 1` for all `i ≠ candidate`

---

### 🧠 Time & Space Complexity

| Phase        | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Elimination  | O(n)            | O(1)             |
| Verification | O(n)            | O(1)             |
| **Total**    | O(n)            | O(1)             |

This is **asymptotically optimal** for this problem.

### 🔹 Another



---

### 🔁 Example Dry Run

Input:

```python
mat = [
 [1, 1, 0],
 [0, 1, 0],
 [0, 1, 1]
]
```

* a = 0, b = 2

  * mat\[0]\[2] = 0 → b = 1
* a = 0, b = 1

  * mat\[0]\[1] = 1 → a = 1

Candidate = 1
Verify:

* mat\[1]\[0] = 0 and mat\[0]\[1] = 1 ✅
* mat\[1]\[2] = 0 and mat\[2]\[1] = 1 ✅
  ✅ Return: **1**

---

### ✅ Verdict

This solution is **clean**, **intuitive**, and **space-efficient**, and it’s a **favorite in interviews** due to its elimination logic and optimal performance.


```python
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        candidate = 0

        # Step 1: Find a potential candidate
        for i in range(1, n):
            # If candidate knows i, they can't be celebrity
            if mat[candidate][i] == 1:
                candidate = i

        # Step 2: Validate candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know i, and everyone should know candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate
```

✅ **Time:** O(n)
✅ **Space:** O(1)

---

## 📚 Example Test Case

```python
mat = [[1, 1, 0], 
       [0, 1, 0], 
       [0, 1, 1]]

sol = Solution()
print("Celebrity Index:", sol.celebrity(mat))  # Output: 1
```

---

## 🧠 Interview Q\&A

---

### ❓ Q1: Why does the brute-force method take O(n²)?

**A:** Because for each person, we check all others to confirm they don’t know anyone and are known by all.

---

### ❓ Q2: How does the two-pointer technique reduce time to O(n)?

**A:** It progressively eliminates non-celebrity candidates in one pass by checking if current candidate knows the next person.

---

### ❓ Q3: Can there be multiple celebrities?

**A:** No. By definition, only one person can be known by everyone and not know anyone else.

---

### ❓ Q4: What if `mat[i][i]` is 1?

**A:** This is ignored. Self-knowledge isn’t relevant to celebrity condition.

---

### ❓ Q5: What are edge cases?

* `n = 1`: The only person is trivially a celebrity.
* Everyone knows everyone: No celebrity.
* One person is known by all and knows none: Valid case.

---

---

Here’s the **full program** using your provided class `Solution`, with:

* ✅ **Inline comments** explaining time and space complexity for each step
* ✅ **`time.time()`** used to measure actual runtime
* ✅ **Example input and printed output**

---

```python
import time

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        
        # Step 1: Find a potential celebrity candidate
        # Time: O(n)
        # Space: O(1)
        candidate = 0
        for i in range(1, n):
            # If candidate knows i, candidate can't be celebrity
            # So make i the new candidate
            if mat[candidate][i] == 1:
                candidate = i
        
        # Step 2: Validate candidate
        # Time: O(n)
        # Space: O(1)
        for i in range(n):
            if i != candidate:
                # Candidate should not know anyone
                # And everyone should know candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1  # No celebrity found

        return candidate  # Valid celebrity

# ---------- 🧪 Example Execution and Timing ----------

if __name__ == "__main__":
    # Example input
    mat = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    
    print("Input Matrix:")
    for row in mat:
        print(row)

    # Start timer
    start = time.time()

    sol = Solution()
    result = sol.celebrity(mat)

    # End timer
    end = time.time()

    print("\nOutput (Celebrity Index):", result)
    print("Execution Time: {:.6f} seconds".format(end - start))
```

---

## ✅ Output for the Given Example

```
Input Matrix:
[1, 1, 0]
[0, 1, 0]
[0, 1, 1]

Output (Celebrity Index): 1
Execution Time: 0.0000XX seconds
```

---

### 🧠 Complexity Summary

| Step                 | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Finding Candidate    | O(n)            | O(1)             |
| Validating Candidate | O(n)            | O(1)             |
| **Total**            | O(n)            | O(1)             |
