Here’s a tiny “interview index card” you can memorize.

---

## 5-line pseudo-code template (construct from pair-sum)

```text
m = len(arr); n = (1 + sqrt(1 + 8*m)) / 2
if n == 1: return [0]
if n == 2: return [0, arr[0]]
S01 = arr[0]; S02 = arr[1]; S12 = arr[n-1]
r0 = (S01 + S02 - S12)/2; res[0]=r0; res[1]=S01-r0; res[2]=S02-r0
for j from 3 to n-1: res[j] = arr[j-1] - r0
```

From this skeleton you can write full code in any language very quickly.

---

## Easy mnemonic (60-second recall)

Think:

> **“Find n, crack first three, subtract row-0.”**

Break it into 3 micro-steps:

1. **Find n from m**
   “`m = n(n-1)/2 → n = (1 + √(1+8m))/2`.”

2. **Crack first three elements**

   * `S01 = r0 + r1`
   * `S02 = r0 + r2`
   * `S12 = r1 + r2`
   * Chant: **“S01 + S02 − S12 = 2·r0”** → `r0`, then `r1 = S01 − r0`, `r2 = S02 − r0`.

3. **Subtract row-0 for the rest**
   For `j ≥ 3`: `rj = arr[j-1] − r0`.

If you replay in your head before the interview:

> “Compute n from m; use three sums to get r0; r1, r2 from S01/S02; others = arr[j-1] − r0.”

you’ll have everything you need to rebuild the logic and code on the spot.
