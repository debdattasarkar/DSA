## 5-line pseudo-code template (Queue + Frequency)

```text
freq[26]=0, q=empty, ans=""
for ch in s: freq[ch]++, q.push(ch)
while q not empty and freq[q.front] > 1: q.pop()
ans += (q.front if q else '#')
return ans
```

### Mnemonic

**“Count + Queue + Clean + Peek”**
(or **“Push → Count → Pop repeats → Print front”**)

---

## 60-second recall (what to say + do)

1. **Goal (5s):** “For each prefix, output first char with frequency 1; else #.”

2. **Why queue (10s):** “Need earliest candidate in arrival order → use queue.”

3. **What to store (10s):** “Maintain freq[26] (counts) + queue of seen chars.”

4. **Per character step (20s):**

* increment frequency
* push to queue
* while front is repeated (freq>1), pop it
* answer = front else '#'

5. **Complexities (15s):**

* “Each char pushed once, popped at most once → O(n) time.”
* “freq is O(1); queue can be up to O(n) (output excluded).”

