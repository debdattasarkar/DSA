### 5-line pseudo-code template (memorize)

```
best = INF, ans = ""
i = 0
while i < n:
    move i forward to match s2 fully (j reaches m) -> end = i
    move i backward matching s2 from back (j=m-1..0) -> start = i+1
    update best/ans; set i = start + 1 and repeat
return ans
```

---

## Mnemonic (30-sec)

**“MATCH → BACKTRACK → MIN”**
(or **“Forward to FIND, backward to SHRINK.”**)

---

## 60-second recall script (what to say in interview)

1. “We need the smallest substring of `s1` where `s2` appears as a subsequence (order matters).”
2. “I scan forward in `s1` to find an `end` where I can match all of `s2`.”
3. “Once matched, I scan backward to shrink the window to the minimum possible `start` for that `end`.”
4. “Track the best (shortest, and leftmost by first-found).”
5. “Continue from `start+1`. Worst-case around `O(n*m)`, constant extra space.”
