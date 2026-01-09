### 5-line pseudo-code template (most common: Prefix + Hash)

```
freq[0] = 1; odd = 0; ans = 0
for x in arr:
    odd += (x % 2)              // +1 if odd else +0
    ans += freq.get(odd - k, 0) // count previous prefixes
    freq[odd] = freq.get(odd, 0) + 1
return ans
```

---

## Mnemonic (30-sec)

**“ODD-PREFIX → NEED (odd−k) → ADD freq”**
(also: **“diff = k”**)

---

## 60-second recall script (say this in interview)

1. “Subarray odds count equals difference of prefix odd counts.”
2. “Maintain `odd` = odds so far and a hashmap `freq` of seen prefix odd counts.”
3. “For each element, update `odd` by +1 if it’s odd.”
4. “All subarrays ending here with exactly k odds start where prefix was `odd-k`; add `freq[odd-k]`.”
5. “Update `freq[odd]`. Complexity O(n) time, O(n) space (or O(1) via atMost trick).”