**“5-line pseudo-code template + 60-second recall kit”** for
🧩 **Factorial of Large Numbers (Digit Array Simulation)**

---

## ⚙️ 5-Line Pseudo-Code Template (universal skeleton)

```
res = [1]
for x in 2..n:
    carry = 0
    for i in 0..len(res)-1:
        prod = res[i]*x + carry
        res[i] = prod % 10
        carry = prod // 10
    while carry: append(carry%10); carry//=10
reverse(res); return res
```

✅ **O(n × D)** (≈ O(n²)) time ✅ **O(D)** space ✅ Works for n ≤ 1000

---

## 🧠 Mnemonic — “**M-C-D**” → *Multiply, Carry, Dump*

| Step  | Action                                      | Picture it                       |
| ----- | ------------------------------------------- | -------------------------------- |
| **M** | Multiply each stored digit by the current x | Like doing `× x` on paper        |
| **C** | Carry over tens to next digit               | Pass overflow to the next column |
| **D** | Dump leftover carry digits at the end       | Extend number length             |

> 🧩 **Catchphrase:**
> “Multiply digit-by-digit, Carry forward, Dump carry out, Reverse at end.”

---

## 🕒 60-Second Recall Routine (before interview)

1. **Say the problem:**
   “We need to simulate long multiplication for n! digit by digit.”

2. **Visualize the logic:**

   * Store digits reversed (`[1]` = 1).
   * For each x in 2..n: multiply, carry, append carry.
   * Reverse to get final digits (MSD first).

3. **Core loop mental image:**
   `prod = digit * x + carry → res[i]=prod%10 → carry=prod//10`.

4. **Complexity line:**
   “O(n×digits) ≈ O(n²) time, O(digits) space.”

5. **Edge recall:**
   n = 0 or 1 → [1]; works for n up to 1000.

---

### 🎯 One-line Sticky Phrase

> **“Multiply-Carry-Dump—Reverse to Reveal n!”**
