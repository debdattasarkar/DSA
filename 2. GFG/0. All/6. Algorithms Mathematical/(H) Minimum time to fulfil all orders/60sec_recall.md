### 5-line pseudo-code template (memorize)

```
lo = 0; hi = minRank * n*(n+1)/2
while lo < hi:
    mid = (lo+hi)//2
    if donuts(mid) >= n: hi = mid
    else: lo = mid + 1
return lo
```

Where `donuts(T)` is:

```
total = 0
for each rank r:
    time = 0; k = 1
    while time + r*k <= T: time += r*k; k++; total++
return total
```

---

## Mnemonic (30-sec)

**“BS TIME → COUNT DONUTS → SHRINK.”**
or **“Lo-Hi-Mid, Make? Move.”**

* **Make?** (feasible) → move **Hi** left
* **Not** feasible → move **Lo** right

---

## 60-second recall script (what to say in interview)

1. “We need **minimum time** to make `n` donuts; feasibility is monotonic → **binary search on time**.”
2. “For a fixed time `T`, each chef with rank `r` spends `r,2r,3r...` per donut; simulate until exceeding `T` (n ≤ 1000).”
3. “Sum donuts across chefs; if total ≥ n, `T` works.”
4. “Bounds: `lo=0`, `hi = minRank * n*(n+1)/2` (fastest chef alone).”
5. “Return `lo`. Complexity: about `O(m log hi)` with constant-time-ish checks.”

If you want, I can also generate a **sticky-note sketchnote** for this one: “BS on Time” + “Triangle numbers r*k(k+1)/2” + “Feasible? shrink”.
