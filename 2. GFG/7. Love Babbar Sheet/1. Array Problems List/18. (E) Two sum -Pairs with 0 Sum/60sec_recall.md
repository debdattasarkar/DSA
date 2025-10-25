**“5-line pseudo-code template + recall trick”** for the
🧩 **Two Sum – Pairs with 0 Sum** problem.

---

## ⚙️ 5-Line Pseudo-Code Template

```
sort(arr)
left = 0; right = n-1
while left < right:
    if arr[left] + arr[right] == 0: add [arr[left], arr[right]], skip dups, move both
    elif arr[left] + arr[right] < 0: left++
    else: right--
return result
```

✅ That’s the **entire skeleton** — you can rebuild it in **any language (C++ / Python / Java)** instantly.

---

## 🧠 Easy Mnemonic — “**S A M**” rule

> **S – Sort**,
> **A – Add when zero**,
> **M – Move pointers smartly**

So before coding, just recall:

> “Sort first, then Add-zero pairs, Move left/right to balance.”

### How to remember pointer moves:

* **Sum < 0 → need bigger → move `Left++`**
* **Sum > 0 → need smaller → move `Right--`**
* **Sum = 0 → record pair → skip duplicates → move both**

---

## 🧩 60-Second Interview Recall Routine

**When interviewer says “find pairs with 0 sum”:**

1. 🧠 *Restate*: “We want unique pairs (x, y) with x + y = 0.”
2. 🪶 *Plan*: Sort array → two-pointer → sum check → skip duplicates.
3. ⏱ *Sketch mentally*:

   * while `L < R`:

     * if sum==0 → record → move both.
     * elif sum<0 → `L++`.
     * else → `R--`.
4. ⚙️ *Complexity check*:

   * Time = O(n log n) (sort)
   * Space = O(1)
5. 🧩 *Edge memory cue*: handle `[0,0]` case once.

---

### Bonus “pocket phrase” to recall logic fast:

> 🗯️ “**Sort and Slide** — if sum’s low, go right; if sum’s high, go left; if zero, save and skip dups.**”

---
