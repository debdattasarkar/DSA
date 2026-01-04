### 5-line pseudo-code template (memorize)

```
sum = 0
for i in 0..k-1: sum += arr[i]
best = sum
for r in k..n-1: sum += arr[r] - arr[r-k]; best = max(best, sum)
return best
```

---

## Mnemonic (30-sec)

**“IN − OUT = NEW SUM”**
(or **“ADD right, DROP left”**)

---

## 60-second recall script (what to say in interview)

1. “Need maximum sum of any contiguous subarray of fixed size k.”
2. “Brute is O(n*k), too slow.”
3. “Compute sum of first k elements as the initial window.”
4. “Slide window: add incoming element, subtract outgoing element.”
5. “Track max window sum. O(n) time, O(1) space.”
