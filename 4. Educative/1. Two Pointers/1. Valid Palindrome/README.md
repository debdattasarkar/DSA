
---

## 🧪 Sample Example 1

### 🔹 Input

```text
s = "Madam, in Eden, Im Adam"
```

---

### 🔸 Output

```text
TRUE
```

---

### ✅ Explanation

The phrase is a **palindrome** because, when ignoring:

* **Punctuation**
* **Spaces**
* **Letter casing**

…it reads the same **forward and backward**.

In this case:

```
Original: "Madam, in Eden, Im Adam"
Normalized: "madaminedenimadam"
Reversed:  "madaminedenimadam"
```

✅ Both match → It is a **valid palindrome**.

---

Here are the **key interview pointers** from the provided page on the **Valid Palindrome** problem:

---

## ✅ Interview Pointers to Remember: Valid Palindrome

### 📌 Problem Understanding

* You're given a string and asked to **return `True` if it's a palindrome**.
* Must **ignore non-alphanumeric characters** and **ignore case**.

---

### 🧠 Key Concepts to Know

1. **Palindrome Check Logic**:

   * A string that reads the same **forward and backward**.

2. **Normalization**:

   * Strip non-alphanumeric characters (`isalnum()`).
   * Convert everything to lowercase.

3. **Two-Pointer Technique**:

   * Use two indices (`left` and `right`) to compare characters from both ends.
   * Move inward, skipping non-alphanumeric characters.

---

### 💡 Steps in the Optimized Approach

1. **Initialize two pointers**: `left = 0`, `right = len(s) - 1`
2. **Skip non-alphanumeric** characters using `while not s[left].isalnum()` and `while not s[right].isalnum()`
3. **Convert characters to lowercase** for comparison
4. **Check characters** at both ends

   * If mismatch → `return False`
   * Else, move inward
5. If loop completes → `return True`

---

### 📈 Time and Space Complexity

* **Time Complexity**: `O(n)` — One pass through the string.
* **Space Complexity**: `O(1)` — No extra space used (if done in-place).

---

### ⚠️ Common Pitfalls

* Not converting characters to **lowercase** before comparison.
* Not properly **skipping punctuation** and spaces.
* Using extra space unnecessarily when asked for an **in-place** solution.

---

### 🧪 Sample Input to Practice

```text
Input: "A man, a plan, a canal: Panama"
Output: True
```

---
