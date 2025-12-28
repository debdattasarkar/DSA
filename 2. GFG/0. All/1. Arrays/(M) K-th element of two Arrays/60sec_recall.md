### 5-line pseudo-code template (memorize)

```
if len(a) > len(b): swap(a,b)                 // BS on smaller
lo = max(0, k-len(b)); hi = min(k, len(a))    // cutA bounds
while lo <= hi:
    cutA=(lo+hi)//2; cutB=k-cutA
    if leftA<=rightB and leftB<=rightA: return max(leftA,leftB)
    elif leftA>rightB: hi=cutA-1 else lo=cutA+1
```

*(Sentinels: left of empty = -∞, right of empty = +∞)*

---

## Mnemonic (30-sec)

**“CUT → CHECK → SHIFT → MAX”**

* **CUT** (choose cutA, cutB)
* **CHECK** boundary order
* **SHIFT** binary search left/right
* **MAX** of lefts is the answer

---

## 60-second recall script (what to say)

1. “This is k-th in merged sorted order, but merging is too slow.”
2. “Use partition: take `cutA` from A, `cutB=k-cutA` from B (left side has k elems).”
3. “Valid when `leftA<=rightB` and `leftB<=rightA`.”
4. “Binary search `cutA` on the smaller array; handle edges with ±∞.”
5. “Then answer is `max(leftA,leftB)`; complexity `O(log(min(n,m)))`, space `O(1)`.”
