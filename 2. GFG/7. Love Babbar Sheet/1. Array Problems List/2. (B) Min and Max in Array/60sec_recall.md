
Here’s how to **lock it into memory** for quick recall under pressure.

---

## ⚡ The “5-Line Universal Pseudo-Code Template”

```
1. min_val ← +∞, max_val ← -∞
2. for each x in arr:
3.     if x < min_val: min_val ← x
4.     if x > max_val: max_val ← x
5. return (min_val, max_val)
```

---

### 🧠 Mnemonic to remember it:

> **“MIN–MAX–SCAN–COMPARE–RETURN”**

Or visualize it like:

> “Start with infinity and minus infinity,
> scan each element, update min and max,
> and return both.”

---

## 🪄 60-Second Recall Routine (before interview)

Say aloud:

> “Initialize min to +∞, max to –∞.
> For every number, if smaller → update min;
> if larger → update max;
> return the pair.”

Now you can **rebuild in any language** in ~30 seconds:

| Language       | 1-pass rebuild                                                       |
| -------------- | -------------------------------------------------------------------- |
| **Python**     | `for x in arr: min_val=min(min_val,x); max_val=max(max_val,x)`       |
| **C++**        | `for(int x: arr){ if(x<min_val)min_val=x; if(x>max_val)max_val=x; }` |
| **Java**       | `for(int x: arr){ if(x<minVal)minVal=x; if(x>maxVal)maxVal=x; }`     |
| **JavaScript** | `for(let x of arr){ if(x<min)min=x; if(x>max)max=x; }`               |

---

## 🧩 Pattern Link — Use this Template For:

* Finding **min/max** (this one ✅)
* Finding **second min/max** (extend with one extra variable)
* Maintaining running **range / normalization bounds**
* **Streaming min/max updates** in data processing
* Finding **min difference** by extending logic with prev element

---

## 💡 Super-Quick Visualization Hook

Imagine you’re walking through the array holding two sticky notes:

* 🟩 “MIN” — replace if you see a smaller number
* 🟥 “MAX” — replace if you see a larger number

At the end, you’re holding the smallest and largest — done!

---

✅ **TL;DR to say to yourself before interview:**

> “Start at +∞ and –∞, scan once, update min and max as I go — one loop, O(n) time, O(1) space.”
