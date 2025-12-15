Here’s a tiny “rotation cheat card” you can glance at before interviews.

---

## 5-line pseudo-code template (String Rotations)

```text
if len(s1) != len(s2): return False
if s1 == "" and s2 == "": return True
doubled = s1 + s1
if s2 is substring of doubled: return True
else: return False
```

That’s literally the whole algorithm.

---

## Easy mnemonic (60-second recall)

Just remember the phrase:

> **“Same length, concat & find.”**

Break it into 3 micro-steps:

1. **Same length?**
   If not → `False`.

2. **Concat:**
   Make `doubled = s1 + s1`.

3. **Find:**
   Check if `s2` occurs inside `doubled`.

If in your head you can say:

> **“Check length, then s2 in s1+s1.”**

you’ll be able to recreate the full function in any language in under a minute.
