**5-line skeleton + mnemonic** for
🧩 **Maximum Product Subarray** (Kadane-for-product)

---

## ⚙️ 5-Line Pseudo-code (universal skeleton)

```
max_end = min_end = ans = arr[0]
for x in arr[1:]:
    if x < 0: swap(max_end, min_end)        # negative flips roles
    max_end = max(x, max_end * x)           # best ending here
    min_end = min(x, min_end * x)           # worst (most negative) ending here
    ans = max(ans, max_end)
return ans
```

✅ **O(n)** time, **O(1)** space, handles negatives & zeros.

---

## 🧠 Easy mnemonic — “**S-W-U-T**”

* **S**tart: `max=min=ans=arr[0]`
* **W**hen negative → **swap** `max_end` & `min_end`
* **U**pdate both: `max_end = max(x, max_end*x)`, `min_end = min(x, min_end*x)`
* **T**rack best: `ans = max(ans, max_end)`

> Pocket phrase: **“Negatives swap, update both, track best.”**

---

## ⏱️ 60-second recall (pre-interview)

1. **State** the twist: “Products need both max & min because negatives flip signs; zeros break runs.”
2. **Initialize** `max_end=min_end=ans=arr[0]`.
3. **Loop** items:

   * If **x<0 → swap**.
   * **Update both** max/min with either extend or restart at x.
   * **Update ans** with `max_end`.
4. **Complexity**: O(n) time, O(1) space.
5. **Edge checks**: single element, zeros anywhere, all negatives (odd/even count).

