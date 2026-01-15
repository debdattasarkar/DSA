### 5-line pseudo-code template (memorize)

```
candies = [1]*n
for i=1..n-1: if a[i] > a[i-1]: candies[i] = candies[i-1] + 1
for i=n-2..0: if a[i] > a[i+1]: candies[i] = max(candies[i], candies[i+1] + 1)
return sum(candies)
```

---

## Mnemonic (30-sec)

**“LEFT raises, RIGHT fixes.”**
(or **“Two passes for two neighbors.”**)

---

## 60-second recall script (what to say in interview)

1. “Each child gets at least 1 candy.”
2. “Left-to-right pass enforces: higher than left ⇒ more candies.”
3. “Right-to-left pass enforces: higher than right ⇒ more candies.”
4. “Use max in second pass so we don’t break the first constraint.”
5. “Sum candies. O(n) time, O(n) space (or O(1) with slope trick if needed).”
