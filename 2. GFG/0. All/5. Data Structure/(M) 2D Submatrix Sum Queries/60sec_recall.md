Here’s a compact “interview index card” for 2D prefix sums.

---

## 5-line pseudo-code template (2D Submatrix Sum)

```text
build pref:
    pref[i][j] = mat[i][j] + top + left - diag
for each query (r1,c1,r2,c2):
    ans = pref[r2][c2]
    if r1>0: ans -= pref[r1-1][c2]
    if c1>0: ans -= pref[r2][c1-1]
    if r1>0 and c1>0: ans += pref[r1-1][c1-1]
return all ans
```

Where:

* `top  = pref[i-1][j]   if i>0 else 0`
* `left = pref[i][j-1]   if j>0 else 0`
* `diag = pref[i-1][j-1] if i>0 and j>0 else 0`

From this skeleton you can write full Python/C++/Java quickly.

---

## Easy mnemonic (60-second recall)

Think two short phrases:

1. **“Prefix = self + top + left − diag.”**
   (That’s the build step.)

2. **“Submatrix = S22 − S12 − S21 + S11.”**

   * `S22 = pref[r2][c2]`
   * `S12 = pref[r1-1][c2]` (top strip)
   * `S21 = pref[r2][c1-1]` (left strip)
   * `S11 = pref[r1-1][c1-1]` (overlap you add back)

Repeat before the interview:

> **“Build: self + top + left − diag.
> Query: S22 − S12 − S21 + S11.”**

If you remember just that, the rest of the code falls into place.
