**“5-line pseudo-code + 60-second recall kit”** for
🧩 **Common Elements in 3 Sorted Arrays** — the exact mental skeleton interviewers expect.

---

## ⚙️ 5-Line Pseudo-Code Template (universal skeleton)

```
i = j = k = 0
while i<n1 and j<n2 and k<n3:
    if arr1[i] == arr2[j] == arr3[k]: add to result; skip duplicates; move all
    elif arr1[i] < arr2[j]: i++
    elif arr2[j] < arr3[k]: j++
    else: k++
return result or [-1]
```

✅ Works in **Python, C++, Java, or pseudocode** — just expand `while` and `if`.
✅ Single pass: **O(n1 + n2 + n3)** time, **O(1)** extra space.

---

## 🧠 Mnemonic: “**3C Rule** – Compare, Catch, Climb**”

| Step        | Meaning                                     | Memory Hook                |
| ----------- | ------------------------------------------- | -------------------------- |
| **Compare** | Look at current 3 values                    | 🧩 “Look at 3 corners”     |
| **Catch**   | If all equal → record & skip dups           | 🎯 “Caught one!”           |
| **Climb**   | Else climb (increment) the smallest pointer | 🪜 “Smallest climbs first” |

So you remember:

> **“Compare → Catch → Climb (smallest)”**

---

## 🕒 60-Second Recall Routine (before the interview)

1. **Say the goal:**
   “Find distinct elements common to all 3 sorted arrays.”

2. **Recall the key pattern:**
   “Three pointers, advance the smallest — add when all equal.”

3. **Run through the logic mentally:**

   * `if a==b==c → add → move all`
   * `elif a<b → i++`
   * `elif b<c → j++`
   * `else → k++`
   * (skip duplicates each time)

4. **Say the complexity out loud:**
   “Time O(n1+n2+n3), space O(1).”

5. **Edge note:**
   “No common → return [-1]. Handle duplicates in-place.”

---

## 🧩 “Sticky Phrase” (fastest recall)

> 💭 “**3 arrays walk together — smallest moves, equals collect.**”

Keep that one line in your mind; you’ll be able to reconstruct the full logic in 30 seconds during any interview.
