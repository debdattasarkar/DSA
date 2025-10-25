
🧩 **Trapping Rain Water** — built for 30-second rebuild + 60-second mental recall.

---

## ⚙️ 5-Line Pseudo-Code Template (Universal, works in any language)

```
l, r = 0, n-1
leftMax, rightMax = arr[l], arr[r]
water = 0
while l < r:
    if leftMax <= rightMax:
        l += 1
        leftMax = max(leftMax, arr[l])
        water += max(0, leftMax - arr[l])
    else:
        r -= 1
        rightMax = max(rightMax, arr[r])
        water += max(0, rightMax - arr[r])
return water
```

✅ **Time:** O(n)
✅ **Space:** O(1)
✅ **Each bar visited once**

---

## 🧠 Easy Mnemonic — “**S-B-C**” → *Smaller Boundary Controls*

| Step  | Meaning                                                 | Visual Cue                    |
| ----- | ------------------------------------------------------- | ----------------------------- |
| **S** | Move the pointer with **Smaller boundary height**       | 📉 shorter wall decides limit |
| **B** | Update that side’s **Boundary max**                     | 🧱 growing barrier            |
| **C** | **Count trapped water** = boundary max − current height | 💧 filling gap                |

> 💬 **Catchphrase:**
> “Move the smaller wall — update max — add difference.”

---

## 🕒 60-Second Interview Recall Routine

1. **State the idea aloud:**
   “Water at any index depends on min(leftMax, rightMax).
   Move the side with the smaller max, since that limits the height.”

2. **Picture it visually:**

   * Bars = walls 🧱
   * Water sits only where a taller wall blocks the other side 💧

3. **Walk through core logic mentally:**

   * If `leftMax <= rightMax`: handle left side
   * Else handle right side
   * Accumulate trapped water

4. **Edge cases:**

   * Fewer than 3 bars → 0
   * Monotonic arrays (↑ or ↓) → 0
   * Equal bars fine (≤ ensures both handled properly)

5. **Complexities mantra:**

   * Time O(n): one linear pass
   * Space O(1): only four scalars

---

## 🧩 Sticky-Line Summary (for 10-second rebuild)

> **“Move smaller wall → update max → add trapped difference.”**
