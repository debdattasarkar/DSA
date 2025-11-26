
---

# ✅ **5-Line Pseudo-Code Template (Universal & Memorizable)**

```
shift = 0
while l < r:
    l = l >> 1
    r = r >> 1
    shift += 1
return l << shift
```

This is the entire optimal solution.
You can rewrite this in *any* language in under 30 seconds.

---

# 🎯 **Easy Mnemonic: “Shift Until Same”**

Three words only:

### **Shift → Match → Restore**

* **Shift** both `l` and `r` right until **they match**
* The matched value = **common prefix**
* **Restore** it by left-shifting back

Alternate mnemonic:

### 🔑 **CPR = Common Prefix Result**

* **C**ommon
* **P**refix (by shifting)
* **R**esult → shift back

---

# ⏱ **Your 60-Second Interview Recall Script**

Before entering the interview, say this to yourself:

> “Bitwise AND across `[l, r]` keeps only the common binary prefix.
> Any bit that changes anywhere in the interval becomes 0 in the final AND.
>
> To find the common prefix, I repeatedly right-shift both numbers until they become equal.
> Each shift removes one non-stable bit position.
>
> Once `l == r`, that value is exactly the common prefix.
> Then I left-shift that prefix back by the number of removed bits, padding zeros.
>
> Complexity is `O(log(max(l,r)))`, since integers ~10⁹ have ≤30 bits.
> Space is `O(1)`.”

This script is short, clear, and makes you sound extremely confident.

---
