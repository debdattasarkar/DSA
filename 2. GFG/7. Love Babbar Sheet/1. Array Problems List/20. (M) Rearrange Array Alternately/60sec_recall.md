**“5-line pseudo-code template + 60-second recall kit”** for
🧩 **Rearrange Array Alternately (max–min–max–min)**

---

## ⚙️ 5-Line Pseudo-Code Template (universal skeleton)

*(Easy to rebuild in Python, C++, or Java)*

```
sort(arr)
base = max(arr) + 1
left, right = 0, n-1
for i in range(n):
    arr[i] += ((arr[right] if i%2==0 else arr[left]) % base) * base
    right -= (i%2==0); left += (i%2!=0)
for i in range(n): arr[i] //= base
```

✅ **O(n log n)** time (sort)
✅ **O(1)** extra space
✅ **Works for positives** since base > max

---

## 🧠 Mnemonic — “**S B L H E D**” → *Sort → Base → Left/Right → Encode → Decode***

| Step    | What you do                          | Quick mental image                      |
| ------- | ------------------------------------ | --------------------------------------- |
| **S**   | **Sort** array                       | Line up cards smallest→largest          |
| **B**   | Compute `base = max + 1`             | Choose a “taller box” for encoding      |
| **L H** | Set **left** & **right** pointers      | Two fingers: left (min), right (max)    |
| **E**   | **Encode** alternately `max, min, …` | Stuff both old & new values in one slot |
| **D**   | **Decode** by `//= base`             | Remove wrapper → reveal final order     |

> 💭 Quick phrase:
> **“Sort – pick Max Min Max Min – Encode then Decode.”**

---

## 🕒 60-Second Recall Routine (pre-interview quick-drill)

1. **Say the goal aloud:**
   “Reorder array as max, min, 2nd max, 2nd min … in-place.”

2. **Recall key trick:**
   “Use one variable to hold old + new via `base = max+1`.”

3. **Visualize loop logic:**

   * Even → pick from end (`right--`)
   * Odd → pick from start (`left++`)
   * Encode using `arr[i] += (chosen%base)*base`

4. **Decode:**
   `arr[i] //= base`

5. **Say complexity:**
   “O(n log n) time, O(1) space.”

---

**Sticky-note summary (1-liner)**

> 🧩 “Sort → Alternate Max/Min → Encode → Decode.”

That’s the 30-second rebuild blueprint for any language during an interview.
