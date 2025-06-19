
---

# Case-specific Sorting of Strings

**Difficulty:** Medium
**Accuracy:** 69.88%
**Submissions:** 72K+
**Points:** 4
**Average Time:** 45m

---

## 🧠 Problem Statement

Given a string `s` consisting of **only uppercase and lowercase** characters, the task is to **sort uppercase and lowercase letters separately** such that if the *i*<sup>th</sup> place in the original string had an uppercase character, then it should **not** have a lowercase character after being sorted — and vice versa.

---

## 💡 Examples

### Example 1:

**Input:**
`s = "GEeKS"`

**Output:**
`EGekS`

**Explanation:**
Sorted form of given string with the same case of character will result in output as `EGekS`.

---

### Example 2:

**Input:**
`s = "XWMSPQ"`

**Output:**
`MPQSWX`

**Explanation:**
Since all characters are of the same case, we can simply perform a sorting operation on the entire string.

---

## 🔒 Constraints

* `1 ≤ s.length() ≤ 10⁵`

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## 🏷 Tags

* Strings
* Sorting
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Case Specific Sorting Of Strings](https://www.geeksforgeeks.org/case-specific-sorting-of-strings/)

---
