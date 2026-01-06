Here’s a **super-memorizable 5-line skeleton** + a **60-second recall script** you can run in your head.

---

## 5-line pseudo-code template (fixed-size window XOR)

```text
if k invalid: return 0
xor = XOR of first k elements
ans = xor
for i from k to n-1:
    xor = xor XOR arr[i-k] XOR arr[i]   # out then in
    ans = max(ans, xor)
return ans
```

### Mnemonic (easy)

**“Build → Best → Slide (Out^In) → Best → Return”**
Or even shorter: **“First window, then OUT^IN.”**

---

## 60-second recall (what to say/do before interview)

1. **Problem type check:** “Max over all subarrays of length `k`.”
2. **Choose technique:** “Fixed window ⇒ sliding window.”
3. **Key property:** “XOR removes itself: `x ^ x = 0`.”
4. **Window update line:**

   * “NewXor = OldXor ^ outgoing ^ incoming”
   * outgoing index = `i-k`, incoming index = `i`
5. **Complexities:** “O(n) time, O(1) space.”

That’s it. If you remember just one line, remember:
✅ **`window_xor ^= arr[i-k] ^ arr[i]`** (or as two XOR lines).
