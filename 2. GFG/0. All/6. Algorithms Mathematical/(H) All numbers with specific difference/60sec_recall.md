## 5-line pseudo-code template (Binary Search “first true”)

```text
f(x) = x - digitSum(x)
binary search smallest x in [1..n] with f(x) >= d
if not found: return 0
return n - x + 1
```

### Mnemonic

**“Monotonic → First True → Count Suffix”**
(or shorter: **“First-OK, then n-x+1”**)

---

## 60-second recall (what to say + do)

1. **Define score (10s):**
   “Let `f(x)=x - digitSum(x)`; we need `f(x) >= d`.”

2. **Monotonic claim (10s):**
   “As x increases, `x` grows by 1, digit sum changes small / drops on carry → `f(x)` is non-decreasing.”

3. **Binary search (15s):**
   “Find the smallest `x` such that predicate is true.”

4. **Count quickly (15s):**
   “Once true at `x`, it stays true → answer is all numbers from `x..n` → `n-x+1`.”

5. **Complexity (10s):**
   “`O(log n)` checks; each check digit-sum `O(digits)` (≤ 10). Space O(1).”
