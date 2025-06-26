
---

## ❓ Main Question: Reverse Words in a String

**Problem Statement**:
You are given a string `sentence` containing words and possibly leading/trailing/multiple spaces.
Return a new string where the **order of the words** is reversed, but the **order of letters within each word remains unchanged**.

### Constraints:

* Only letters, digits, and spaces
* No leading/trailing spaces or multiple spaces in the final result
* $1 \leq \texttt{sentence.length} \leq 10^4$

> 🔹 A **word** is defined as a sequence of **non-space characters**

---

## 📌 Interview Pointers to Remember

### 1. **Trim and Normalize Spaces**

* Remove:

  * Leading/trailing spaces
  * Extra spaces between words (only 1 allowed)
* Example:
  `"  hello   world  "` → `"hello world"`

---

### 2. **Split → Reverse → Join**

* Split the string by spaces
* Reverse the word list
* Join with a single space

```python
"the sky is blue" → ["the", "sky", "is", "blue"] → ["blue", "is", "sky", "the"] → "blue is sky the"
```

---

### 3. **Don’t Reverse Characters**

* Only **reverse the word order**, not characters within words

---

### 4. **Two Pointer Method (In-place for char array)**

If done **in-place** (char array format):

1. Trim spaces
2. Reverse the entire string
3. Reverse individual words in place

This technique is often asked when optimizing space.

---

### 5. **Edge Cases**

* Empty string → return `""`
* All spaces → return `""`
* One word → return the word

---

## ✅ Example

**Input**: `"  smart  "`
**Output**: `"smart"`

**Input**: `"the sky is blue"`
**Output**: `"blue is sky the"`

---

## ⏱️ Time and Space Complexity

* **Time**: `O(n)`
* **Space**:

  * `O(n)` for extra array
  * `O(1)` if modifying in-place (char array)

---
Here are the **interview-crucial pointers** from the **“Reverse Words in a String”** problem solution, based on the final solution breakdown:

---

## ✅ Interview Pointers to Remember

### ❓ Problem Summary

You're given a string `sentence` which:

* May contain **leading**, **trailing**, or **multiple spaces**
* You must **reverse the order of the words**, not the characters
* Ensure that the final result has:

  * No extra spaces
  * Only **single spaces** between words

---

## 🔧 Key Concepts and Steps

### 1. **Clean Extra Spaces**

* Trim **leading/trailing spaces**
* Reduce multiple spaces between words to a **single space**
* Convert to a list of words: `sentence.split()`

---

### 2. **Use Two-Pointer Reversal**

* Store words in a list called `result`
* Use two pointers:

  * `left = 0`, `right = len(result) - 1`
  * Swap elements at `left` and `right`
  * Move inward until `left >= right`
* Join list with `" ".join(result)`

---

### 3. **Why Use Two Pointers**

* Efficient for reversing in-place (especially when using a mutable list)
* Mimics low-level manipulation seen in C/C++ interviews
* Avoids unnecessary temp variables or extra list creations

---

### 🧪 Sample Example

Input: `"reverse word"`
Output: `"word reverse"`

Illustrated swap:

```
Before: ['reverse', 'word']
Swap:   ['word', 'reverse']
```

---

## ⏱️ Time & Space Complexity

* **Time**: `O(n)`

  * `split()` → O(n)
  * reversal loop → O(n)
  * `join()` → O(n)
* **Space**: `O(n)`

  * Because we store words in a list (`result`)


---

## 🔄 Reverse Words in a String — Two-Pointer Approach

### 🧠 Goal:

Reverse the **order of words** in a given sentence while:

* Removing extra spaces (leading, trailing, multiple between words)
* Keeping the **letters within each word intact**

---

### 📋 Steps to Follow

1. **Clean up the string**
   Remove any extra spaces — this includes:

   * Leading spaces
   * Trailing spaces
   * Multiple spaces between words

2. **Initialize two pointers**

   * `left` → start of the cleaned word list
   * `right` → end of the cleaned word list

3. **Loop until pointers meet**
   Continue the loop **until `left` is greater than or equal to `right`**

4. **Swap words**
   In each iteration, **swap the words** at the `left` and `right` positions

5. **Move the pointers**
   After each swap:

   * Increment `left` by 1
   * Decrement `right` by 1

6. **Return the final result**
   Once all the words are swapped, **reconstruct the string** from the list and return it

---
