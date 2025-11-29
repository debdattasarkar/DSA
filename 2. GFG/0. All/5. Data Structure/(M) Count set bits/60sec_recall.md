Here’s a version you can literally rehearse in under a minute before interviews.

---

## 5-Line Pseudo-Code (for `countSetBits(n)`)

```text
if n == 0: return 0
x = floor(log2(n))                     // largest exponent s.t. 2^x ≤ n
bits_before = x * 2^(x-1)             // bits in 1..(2^x - 1)
msb_bits    = n - 2^x + 1             // MSB set in [2^x..n]
return bits_before + msb_bits + f(n - 2^x)
```

That’s all you need – from this you can rebuild the full solution in any language.

---

## Easy Mnemonic (to recall the logic)

Think: **“Big Power → Three Parts”**

1. **Big Power** – find biggest `2^x` ≤ `n`.
2. **Three Parts**:

   * **Before**: `x * 2^(x-1)`  (all numbers before `2^x`)
   * **MSB**: `n - 2^x + 1`     (numbers with top bit set)
   * **Rest**: `f(n - 2^x)`     (same problem on remaining lower bits)

Say to yourself right before the interview:

> “Highest power of 2, then **Before + MSB + Rest**.”

From that sentence you can instantly reconstruct the 5 lines above.
