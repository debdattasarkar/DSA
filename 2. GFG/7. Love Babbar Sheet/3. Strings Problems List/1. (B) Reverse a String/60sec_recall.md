## 5-line pseudo-code template (Reverse a String)

```text
chars = list(s)
left = 0, right = len(chars) - 1
while left < right: swap(chars[left], chars[right]); left++; right--
return join(chars)
```

That’s the whole solution.

---

## Easy mnemonic (60-second recall)

### Phrase to remember ✅

> **“Swap ends, walk in.”**

### Quick mental steps

1. **Strings immutable** → convert to list
2. **Two pointers** → left & right
3. **Swap** until they meet
4. **Join** back to string

### 10-second interview line

> “Use two pointers from both ends, swap inward, then join. O(n) time.”
