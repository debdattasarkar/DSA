### 5-line pseudo-code template (memorize)

```
build intervals [max(0,i-r), min(n-1,i+r)] for each r != -1
sort intervals by start
cur = 0; i = 0; ans = 0
while cur <= n-1: choose max_end among intervals with start <= cur
if max_end < cur: return -1; ans++; cur = max_end + 1
return ans
```

---

## Easy mnemonic (30 seconds)

**“START ≤ cur → pick FARTHEST END → JUMP.”**

or

**“Cover line greedily: extend as far as possible each step.”**

---

## 60-second interview recall script (say this out loud)

1. “Each worker defines a time interval `[i−r, i+r]`.”
2. “The task reduces to minimum interval cover of `[0..n−1]`.”
3. “Sort by start; keep current uncovered hour `cur`.”
4. “Among all intervals starting before `cur`, choose the one reaching farthest.”
5. “Jump to `farthest+1`; if stuck, return −1; count workers.”

That’s the entire logic you can rebuild in **any language in under 30 seconds**.
