Here’s a **5-line pseudo-code skeleton** + a **60-second recall script** you can mentally run right before the interview.

---

## 5-line pseudo-code template (memorize this)

```
l=0, r=m-1
while l<=r:
  mid=(l+r)//2; row = argmax(mat[*][mid])     # scan rows in mid column
  if mat[row][mid] >= left(row,mid) and >= right(row,mid): return (row,mid)
  elif right(row,mid) > mat[row][mid]: l = mid+1
  else: r = mid-1
```

**Helper rule:** `left/right` out of bounds ⇒ `-∞`.

---

## Mnemonic (super short)

**“Mid column → Column MAX → Check sides → Go bigger side.”**

Or even shorter:
**“Mid–Max–Sides–Shift.”**

---

## 60-second recall (what you say to yourself)

1. “I’ll binary search **columns**.”
2. “In the mid column, I pick the **max element** (scan rows).”
3. “Since it’s column max, it already beats **up/down**.”
4. “So I only compare **left/right**.”
5. “If both sides are smaller/equal → peak.”
6. “Else move toward the **bigger neighbor** (that side must contain a peak).”
7. “Complexity: each step scans rows `O(n)`, steps `log m` ⇒ `O(n log m)`, space `O(1)`.”

That’s it—you can rebuild the full code from that in ~30 seconds in any language.
