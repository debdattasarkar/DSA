## 5-line pseudo-code template (Bus Conductor / Min moves)

```text
if len(chairs) != len(passengers): return error/0
sort(chairs)
sort(passengers)
moves = 0
for i in 0..n-1: moves += abs(chairs[i] - passengers[i])
return moves
```

That’s the entire solution.

---

## Easy mnemonic (60-second recall)

**Phrase:** ✅ **“Sort both, zip, sum abs.”**

Think of it like matching two queues in order:

1. **Sort chairs** (seats in line)
2. **Sort passengers** (people in line)
3. **Pair same index** (closest by order)
4. **Sum absolute distance**

One-liner memory:

> **“Minimum walking on a line = sorted pairing.”**

If you remember that sentence, you can rebuild the code in any language in under 30 seconds.
