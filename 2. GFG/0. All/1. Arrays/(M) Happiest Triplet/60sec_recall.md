## 5-line pseudo-code template (Sort + 3 pointers)

```text
sort(a); sort(b); sort(c)
i=j=k=0; bestDiff=INF; bestSum=INF; bestTriplet=[]
while i<n and j<n and k<n:
  x=a[i], y=b[j], z=c[k]; diff=max(x,y,z)-min(x,y,z); sum=x+y+z; update(best by diff then sum)
  move pointer of the minimum among (x,y,z)
return bestTriplet sorted decreasing
```

### Mnemonic

**“Sort → Scan → Shrink Range (move MIN)”**
or even shorter: **“MIN moves, range improves.”**

---

## 60-second recall script (what to say + do)

1. **Goal (5s):** “Pick one from each array to minimize `max-min`.”
2. **Trigger (10s):** “This is a smallest-range problem → sort arrays.”
3. **Mechanism (15s):** “Use 3 pointers; current range = `max-min`.”
4. **Greedy move (15s):** “To reduce range, only option is to increase the current minimum → move pointer of MIN.”
5. **Tie-break (10s):** “If diff same, choose smaller sum.”
6. **Finish (5s):** “Return triplet in decreasing order.”

