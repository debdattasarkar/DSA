# 🔁 Exactly One Swap

---

## 🧾 Problem Statement

Given a string `s`, return the **number of distinct strings** that can be obtained by performing **exactly one swap** of two different indices (`i < j`).

---

## 🧪 Examples

### Example 1:

```text
Input: s = "geek"
Output: 6

Explanation:
After one swap, there are only 6 distinct strings possible:
- "egek", "eegk", "geek", "geke", "gkee", "keeg"
```

### Example 2:

```text
Input: s = "aaaa"
Output: 1

Explanation:
All characters are the same. So only one distinct string ("aaaa") is possible after any swap.
```

---

## 📌 Constraints

* 2 ≤ `s.length` ≤ 10⁴

---

## ⏱ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

`Strings` `Data Structures`

---

## 📚 Related Articles

* [Count of Distinct Strings That Can Be Obtained After Performing Exactly One Swap](#)

---

✅ You're referring to this elegant and efficient **mathematical solution**:

```python
from collections import Counter
cnt = Counter(s)
rem = len(s)
ret = dup = 0
for c in cnt:
    dup += cnt[c] > 1
    rem -= cnt[c]
    ret += cnt[c] * rem
return ret + (dup > 0)
```

---

## 🔍 Why This Works

### 🎯 Goal:

Count the number of **distinct strings** that can be made by exactly **one swap of two different indices**.

---

## 🧠 Logic Breakdown

### Step-by-step:

* `cnt[c] * rem`:
  For each character `c`, multiply its frequency with the **number of other characters to its right**
  This gives all **distinct character swaps** between `c` and the remaining characters.

* `ret`:
  Total number of swaps that **change** the string.

* `dup > 0`:
  If any character appears **more than once**, there exists **at least one swap** that does **not change the string** (e.g., swap same characters in different positions).
  So we must **include the original string** as a valid distinct result in that case.

---

## ✅ Example: `"geek"`

* Frequencies: `{'g':1, 'e':2, 'k':1}`
* Valid swaps that change string = 5
* Since `'e'` is repeated → `dup > 0` → we can produce original string via a swap → add `+1`
* Output = `5 + 1 = 6` ✅

---

## ✅ Example: `"aaa"`

* Frequencies: `{'a': 3}`
* `ret = 0`
* `dup > 0` → `+1`
* Output = 1 ✅

---

## ✅ Example: `"jej"`

* Frequencies: `{'j': 2, 'e': 1}`
* ret = `2 * 1 = 2`
* dup = 1 → `+1`
* Output = 3 ✅

---

## ⏱ Time & Space Complexity

| Metric           | Value                 |
| ---------------- | --------------------- |
| Time Complexity  | O(n)                  |
| Space Complexity | O(1) (fixed alphabet) |

---

## 🔁 Final Return Statement:

```python
return ret + (dup > 0)
```

✔️ Correctly accounts for:

* All swaps that change the string
* Plus the **original** string if at least one **duplicate** allows swap to reproduce it

---
