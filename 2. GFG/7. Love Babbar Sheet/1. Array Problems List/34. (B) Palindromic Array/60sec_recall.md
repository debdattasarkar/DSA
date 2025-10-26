**5-line pseudo-code + memory trick system** for
🧩 **Palindromic Array**

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
for each num in arr:
    temp = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    if rev != temp: return False
return True
```

✅ **Time:** O(n × d) (d = digits per number)
✅ **Space:** O(1)
✅ Works in any language — Python, C++, Java, Go, etc.

---

## 🧠 Easy Mnemonic — “**C-R-M**” → *Check, Reverse, Match*

| Step  | Meaning                       | Icon | Memory Hook                    |
| ----- | ----------------------------- | ---- | ------------------------------ |
| **C** | **Check** each number         | 🔍   | Loop through array             |
| **R** | **Reverse** digits            | 🔄   | Multiply by 10 & add remainder |
| **M** | **Match** original & reversed | ✅    | Return False if mismatch       |

> 💬 **Catchphrase:**
> “Check → Reverse → Match; one fail → False, all good → True.”

---

## 🕒 60-Second Recall Routine (Before Interview)

1. **Say the goal aloud:**
   “Verify if every element in the array is a palindrome.”

2. **Visualize:**
   Each number flips backward digit-by-digit (reverse build).

3. **Think the math quickly:**

   * Initialize `rev = 0`.
   * While number > 0:
     `rev = rev * 10 + (num % 10)` → remove last digit.
   * Compare `rev` and original.

4. **Rebuild the skeleton mentally:**
   `for num → reverse → compare → break on fail.`

5. **Complexity mantra:**
   “O(n × digits), constant space, short-circuit early.”

---

### 🎯 One-line sticky recall:

> **“Flip digits, then compare — fail fast on first non-palindrome.”**

This phrase alone lets you **rebuild the entire function in under 30 seconds** in any language during an interview.
