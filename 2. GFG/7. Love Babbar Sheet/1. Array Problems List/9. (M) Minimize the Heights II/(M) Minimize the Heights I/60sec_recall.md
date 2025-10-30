
---

## 🧠 5-Line Pseudo-code Template (Greedy — most expected solution)

```
sort(arr)
ans = arr[n-1] - arr[0]
for i in 1..n-1:
    small = min(arr[0] + k, arr[i] - k)
    big   = max(arr[i-1] + k, arr[n-1] - k)
    ans = min(ans, big - small)
return ans
```

That’s the **entire logic** in 6 short lines.
Every interviewer expects you to recall this shape — it’s a standard pattern.

---

## 🧩 Mnemonic: **“Sort → Split → Shrink”**

| Step  | Keyword    | Meaning                                                |
| ----- | ---------- | ------------------------------------------------------ |
| **S** | **Sort**   | Sort towers ascending — always the first move          |
| **S** | **Split**  | Choose a split index `i` (left gets +k, right gets -k) |
| **S** | **Shrink** | Compute new min & max; update smallest difference      |

So the **3 S’s = Sort → Split → Shrink**
Easy to chant before the interview. 🧘‍♂️

---

## ⚙️ 60-Second Recall Routine

🕐 **0–10s:**
Recognize the pattern — "Minimize range by adding/subtracting k".
Say aloud: “Greedy, must sort and try all cut points.”

🕐 **10–30s:**
Write the **baseline difference**:

```
ans = arr[-1] - arr[0]
```

🕐 **30–50s:**
Remember **split logic**:

```
small = min(arr[0] + k, arr[i] - k)
big   = max(arr[i-1] + k, arr[-1] - k)
```

Then shrink:

```
ans = min(ans, big - small)
```

🕐 **50–60s:**
Close with complexity:

> “Time O(n log n) from sort, Space O(1). Works even if heights become negative.”

---

## 🔁 Visual Mental Hook

Think of **mountain peaks** 🏔️:

* You **push up small hills** by +k,
* You **grind down tall peaks** by -k,
* You look for the **narrowest mountain range** left.

> Sort → Push up left → Push down right → Check gap.

---

## ✅ Quick recap you can say to interviewer

> “I’ll sort the heights first.
> Then for each index `i`, treat everything before it as +k and after it as -k.
> Compute new min and max at boundaries, and keep the smallest difference.
> Time O(n log n), Space O(1).”

---
