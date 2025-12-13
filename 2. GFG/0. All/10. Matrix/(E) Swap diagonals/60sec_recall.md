Here’s a tiny “index card” you can replay before interviews.

---

## 5-line pseudo-code template (Swap Diagonals)

```text
n = size of matrix
for i from 0 to n-1:
    j_major = i
    j_minor = n-1-i
    swap( mat[i][j_major], mat[i][j_minor] )
return mat
```

That’s literally all the logic.

---

## Easy mnemonic (60-second recall)

Think:

> **“Row i: swap i with n-1-i.”**

Repeat in your head:

1. **Square matrix** → diagonals only.
2. For each **row i**,
3. **Major col = i**, **minor col = n-1-i**,
4. Swap those two cells.

If you can remember the phrase:

> **“For each row i, swap (i, i) with (i, n-1-i)”**

you’ll be able to write the full solution in any language in under a minute.
