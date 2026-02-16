### 5-line pseudo-code template (memorize)

```text
sort intervals by start time
prevEnd = intervals[0].end
for each interval (s,e) from 2nd to last:
    if s < prevEnd: return false
    prevEnd = e
return true
```

### Easy mnemonic (super sticky)

**“Sort → Start vs End → Scan”**
Or even shorter: **“SSS: Sort, Scan, Stop(if overlap)”**

* **Sort** by start time
* **Scan** left→right keeping `prevEnd`
* **Stop** when `start < prevEnd`

### 60-second recall script (what you say in interview)

1. “If meetings overlap, you can’t attend all. So detect overlaps.”
2. “I’ll sort by start time so meetings are chronological.”
3. “Track `prevEnd` of the last meeting.”
4. “For each next meeting: if `start < prevEnd`, overlap → return false.”
5. “Otherwise update `prevEnd = end`. If finished, return true.”
6. “Complexity: sorting `O(n log n)`, scan `O(n)`, aux space `O(1)` (ignoring sort).”
