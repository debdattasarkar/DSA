Here’s a **30-second, 5-line pseudo-code skeleton** + a **60-second recall script** you can run in your head.

---

## 5-line pseudo-code template (memorize)

```
ans = sumSubarrayMax(arr) - sumSubarrayMin(arr)

sumSubarrayMin: stack increasing of (val,count), cur=0,total=0
for x in arr: cnt=1; while stack not empty and top.val > x: cur -= top.val*top.cnt; cnt += top.cnt; pop
push (x,cnt); cur += x*cnt; total += cur

sumSubarrayMax: stack decreasing of (val,count), cur=0,total=0
for x in arr: cnt=1; while stack not empty and top.val < x: cur -= top.val*top.cnt; cnt += top.cnt; pop
push (x,cnt); cur += x*cnt; total += cur
```

That’s it. Rebuilds the full O(n) solution.

---

## Easy mnemonic (super sticky)

### **“MAX pops smaller, MIN pops bigger.”**

* For **minimums**, you pop **bigger** elements (`>`).
* For **maximums**, you pop **smaller** elements (`<`).

### **“cur = sum of mins/maxs of all subarrays ending here.”**

* `cur` is the running contribution for subarrays that **end at current index**.
* `total += cur` accumulates across all endings → all subarrays.

### **“count = how many subarrays this value becomes the min/max for.”**

* When you pop, you **merge counts** (`cnt += popped_cnt`).

---

## 60-second recall script (before interview)

1. **Goal rewrite (5 sec):**
   “Sum of ranges = sum of subarray max − sum of subarray min.”

2. **What I compute (10 sec):**
   “Compute `sumSubarrayMax` and `sumSubarrayMin` independently in O(n).”

3. **Core invariant (15 sec):**
   “Maintain monotonic stack of (value,count).
   `count` = how many consecutive subarrays ending here where this value is the min/max.
   `cur` = sum of mins/maxs for subarrays ending at this index.”

4. **Update rule (15 sec):**

   * MIN: while top.val > x → pop, subtract `top.val*top.cnt` from `cur`, add `top.cnt` to `cnt`
   * push (x,cnt), add `x*cnt` to `cur`, then `total += cur`

5. **Sign + finish (10 sec):**
   “Do same for MAX but pop `<`. Final answer = maxTotal − minTotal.”

