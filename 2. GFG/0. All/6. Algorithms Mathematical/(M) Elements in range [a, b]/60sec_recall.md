### 5-line pseudo-code template (memorize)

```
sort(arr)
for each (a,b) in queries:
    L = lower_bound(arr, a)      // first idx with val >= a
    R = upper_bound(arr, b)      // first idx with val >  b
    ans.append(R - L)
return ans
```

### 30-second mnemonic

**“Sort → Left for a → Right for b → Subtract.”**

* **Left** boundary uses **≥ a**
* **Right** boundary uses **> b**
* **Count = Right − Left**

### 60-second recall script (what to say + think)

1. “This is many range count queries on a static array → preprocess.”
2. “Sort once: `O(n log n)`.”
3. “For each query `[a,b]`, find indices with two binary searches.”
4. “`L = first >= a`, `R = first > b`.”
5. “Answer is `R-L`, total `O(q log n)`.”

### Micro-check (to avoid off-by-one mistakes)

* If query is **inclusive** `[a,b]` → use **upper_bound(b)** (first `> b`)
* If it were exclusive `(a,b)` you’d shift bounds accordingly.
