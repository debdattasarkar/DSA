## 5-line pseudo-code template (Meet-in-the-Middle)

```text
split arr into L and R
LS = all subset sums of L
freq = hashmap counts of all subset sums of R
ans = 0; for s in LS: ans += freq[k - s]
return ans
```

### Mnemonic (super easy)

**“Split → Sums → Store → Subtract → Sum”**
(SSSSS 😄)

* **Split** array
* **Sums** of left
* **Store** right sums in hashmap
* **Subtract**: need = k - leftSum
* **Sum** counts

---

## 60-second recall script (what to say + do)

1. **Spot the trigger (10s):**
   “n ≤ 40 and values can be negative → classic DP by sum range is hard.”

2. **State the plan (10s):**
   “Use Meet-in-the-Middle: split into two halves.”

3. **Compute (15s):**
   “Generate all subset sums of each half: LS and RS (each size up to 2^(n/2)).”

4. **Count complements (15s):**
   “Put RS into a frequency map. For each left sum `s`, add `freq[k-s]`.”

5. **Close with complexity (10s):**
   “Time `O(2^(n/2))`, space `O(2^(n/2))`. Works well for n=40.”
