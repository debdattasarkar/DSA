Here’s something you can literally rehearse in under a minute before interviews.

---

## 5-Line Pseudo-Code Template (Language-Agnostic)

```text
t = xor_1_to_n(n)                  // XOR of 1..n (use n%4 trick)
if t == n: return [1..n]           // if already n, take all numbers
x = t XOR n                        // single element to REMOVE
ans = [1..n]                       // start with full list
remove x from ans; return ans      // answer = all except x
```

That’s it. From this skeleton you can expand in any language in ~30 seconds.

---

## Easy Mnemonic to Remember the Logic

Think: **“All → XOR → Fix One → Done”**

1. **All** – Start from **all numbers** `1..n`.
2. **XOR** – Compute `t = XOR(1..n)` (use the `n % 4` pattern).
3. **Fix One** –

   * If `t == n` → nothing to fix, return all.
   * Else remove **one** element `x = t XOR n`.
4. **Done** – Return “all except x”.

Or as 4 keywords you can run through in your head:

> **All, XOR, Compare, Remove**

Right before the interview, just recall:

1. *All*: I’m trying to take `[1..n]`.
2. *XOR*: Get `t = xor_1_to_n(n)` using `n % 4`.
3. *Compare*: If `t == n` → result is `[1..n]`.
4. *Remove*: Else remove `t ^ n` from `[1..n]`.

Once you say those 4 words to yourself, the 5-line pseudo-code practically writes itself.
