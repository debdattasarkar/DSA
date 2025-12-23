### 5-line pseudo-code template (memorize)

```
p = findPivotMinIndex(arr)              // O(log n)
c1 = upperBound(arr, p, n-1, x) - p     // count in right sorted part
c2 = upperBound(arr, 0, p-1, x) - 0     // count in left sorted part
return c1 + c2
```

*(Where `upperBound(l..r,x)` = first index in that range with value `> x`.)*

---

## Mnemonic (30-sec)

**“Pivot → Two Sorted Pieces → UpperBound → Add.”**
Or even shorter: **“P-2-U-A”** (Pivot, 2 parts, UpperBound, Add)

---

## 60-second recall script (what to say + think)

1. “Rotated sorted distinct array = **two sorted blocks** split at the **pivot (minimum)**.”
2. “First, I’ll find pivot using binary search comparing `arr[mid]` vs `arr[high]`.”
3. “Then each block is sorted, so I can count `≤ x` with **upper_bound** (first `> x`).”
4. “Count in block = `upperBoundIndex - leftIndex`.”
5. “Add both counts. Complexity: **O(log n)**, space **O(1)**.”

---

### Micro off-by-one check (super important)

* Want **≤ x** → use **upper_bound(x)** (first `> x`)
* Count = `pos - left`

