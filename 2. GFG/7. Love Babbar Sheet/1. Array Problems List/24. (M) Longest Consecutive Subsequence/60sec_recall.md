**5-line pseudo-code + 60-second recall kit** for
🧩 **Longest Consecutive Subsequence** (most frequently asked hash-set logic).

---

## ⚙️ 5-Line Pseudo-Code Template (Universal Skeleton)

```
S = set(arr)
longest = 0
for x in S:
    if (x-1) not in S:
        y = x
        while y in S: y += 1
        longest = max(longest, y-x)
return longest
```

✅ **O(n)** time (each element visited once)
✅ **O(n)** space (hash set for quick membership test)

---

## 🧠 Easy Mnemonic — “**S-S-C-G-M**”

(*Set, Start, Count, Grow, Max*)

| Step  | Meaning                               | Visual Cue                  |
| ----- | ------------------------------------- | --------------------------- |
| **S** | Build **Set** of all numbers          | 🧺 dump array into a bucket |
| **S** | Find **Start** → number with no (x−1) | 🚩 flag start of streak     |
| **C** | **Count** upward while (x+1) exists   | ⏱️ counting chain links     |
| **G** | **Grow** till break                   | ➕ climb consecutive ladder  |
| **M** | Update **Max length**                 | 🏆 keep best streak length  |

> 💡 **Catchphrase:**
> “Find starts, grow streaks, keep max.”

---

## 🕒 60-Second Interview Recall Routine

1. **Say the core concept:**
   “We use a set for O(1) lookup and only expand from starts where (x−1) isn’t present.”

2. **Visualize loop:**

   * `if x−1 not in set → grow upward`
   * `while y in set → y++`
   * `update max_length = max(max_length, y−x)`

3. **State complexity aloud:**
   “O(n) time, O(n) space — each element expanded once.”

4. **Handle edge cases mentally:**

   * Empty array → 0
   * Duplicates → handled by set
   * All consecutive → returns `len(arr)`
   * Disjoint numbers → returns 1

5. **Wrap up key phrase:**

   > 🧩 “**Set–Start–Grow–Max: each run only once.**”

---

So before any interview, just recall this one line:

> ✨ “Put numbers in a set, expand only from starts, count till gap, track max.”
