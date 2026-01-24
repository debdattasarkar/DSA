## 5-line pseudo-code template (30-second rebuild)

```
winner = 0                       // 0-based, f(1)=0
for size = 2 to n:
    winner = (winner + k) % size // shift by k, wrap by size
return winner + 1                // convert to 1-based
```

(That’s essentially the entire solution.)

---

## Easy mnemonic (super easy to remember)

### **“Shift by k, wrap by size.”**

* Each time the circle grows from `size-1` to `size`,
* the winner index shifts by `k`,
* then wrap using modulo `size`.

---

## 60-second recall script (before interview)

1. **State the known recurrence (10s):**
   “Josephus winner in 0-based: `f(1)=0`.”

2. **Explain the shrink/shift idea (15s):**
   “After eliminating every k-th, the problem reduces to size `n-1`.
   Mapping winner back shifts indices by `k` in the larger circle.”

3. **Say the formula (10s):**
   “So: `f(n) = (f(n-1) + k) % n`.”

4. **Implementation plan (15s):**
   “Compute iteratively from 2..n using one variable `winner`.”

5. **Return format (10s):**
   “Convert 0-based to 1-based: `winner + 1`.”

That’s the full interview-ready explanation + coding plan.
