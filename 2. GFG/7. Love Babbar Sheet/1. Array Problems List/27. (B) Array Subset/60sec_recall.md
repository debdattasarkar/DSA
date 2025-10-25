**5-line pseudo-code template + 60-second recall mnemonic** for
🧩 **Array Subset Problem** (check if `b[]` is a subset of `a[]` — duplicates matter).

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
freqA = Counter(a)
for x in b:
    if freqA[x] == 0: return False
    freqA[x] -= 1
return True
```

✅ **O(n + m)** time
✅ **O(n)** space (hash for frequency)
✅ Works for duplicates and all integer ranges

---

## 🧠 Easy Mnemonic — “**C-C-M**” → *Count, Check, Match*

| Step   | Action                          | Visual cue             |
| ------ | ------------------------------- | ---------------------- |
| **C₁** | **Count** elements of `a`       | 🧮 build frequency map |
| **C₂** | **Check** each element of `b`   | 🔍 verify existence    |
| **M**  | **Match** by decrementing count | ✅ consume copies       |

> 💬 **Catchphrase:**
> “Count in A, Check in B, Match till empty — else fail fast!”

---

## 🕒 60-Second Interview Recall Routine

1. **State the problem:**
   “Need to confirm if `b[]` is a multiset subset of `a[]` — duplicates matter.”

2. **Say the key insight:**
   “Each element in `b` must appear ≤ its count in `a`. So, frequency counting works in O(n+m).”

3. **Outline steps aloud:**

   * Make hash/frequency map for `a`
   * For each `x` in `b`, check and decrement
   * If any check fails → return False
   * Otherwise True

4. **Edge checks:**

   * If `len(b) > len(a)` → False immediately
   * Empty `b` → True
   * Duplicates handled by frequency logic

5. **Complexity recall:**

   * Time: O(n+m)
   * Space: O(n)

---

### 🧩 Sticky-line Summary (for 10s recall)

> “**Count A → Check each in B → Decrement → Fail if zero.**”
