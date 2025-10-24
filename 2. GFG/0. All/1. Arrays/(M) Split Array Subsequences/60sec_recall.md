Perfect — let’s build your **5-line pseudo-code skeleton + mnemonic** for
✅ **Split Array into Consecutive Subsequences (min length ≥ k)**

This is the **“60-second recall” version** you can rebuild in any language (Python, C++, Java) before or during an interview.

---

## 🧠 5-Line Pseudo-Code Template

```
count freq of each number
for x in array:
    if freq[x] == 0: continue
    use one x  (freq[x]--)
    if need[x] > 0: extend chain → need[x]-- ; need[x+1]++
    else if can start k-length chain from x → consume next k-1 ; need[x+k]++
    else return False
return True
```

---

## 🧩 Mnemonic to Remember in 60 Seconds

### 🔑 "C-U-E-S"  → **Count → Use → Extend → Start**

| Step  | Action     | Description                                                                                                                      |
| ----- | ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **C** | **Count**  | Make frequency table of numbers (`freq[x]`).                                                                                     |
| **U** | **Use**    | For each number, if already used up, skip (`freq[x]==0`).                                                                        |
| **E** | **Extend** | If some subsequence needs this number (`need[x]>0`), extend it → now needs next (`need[x+1]++`).                                 |
| **S** | **Start**  | If no chain to extend, try to start a new one of size `k`. Consume next `k−1` numbers → mark `need[x+k]++`. If impossible, fail. |

**Fail-Safe Rule**
If you can’t extend **and** can’t start → return **False** immediately.

✅ If you process all numbers successfully → return **True**.

---

## 🧩 Quick Example Walkthrough (mental picture)

`arr = [2, 2, 3, 3, 4, 5], k = 2`

| Step                                         | x | Action                            | Reason      |
| -------------------------------------------- | - | --------------------------------- | ----------- |
| 1                                            | 2 | Start chain [2,3]                 | `need[4]++` |
| 2                                            | 2 | Start chain [2,3]                 | `need[4]++` |
| 3                                            | 3 | Skip (used)                       | –           |
| 4                                            | 4 | Extend → `need[4]--`, `need[5]++` |             |
| 5                                            | 5 | Extend → `need[5]--`, `need[6]++` |             |
| ✅ Return True — all subsequences valid (≥2). |   |                                   |             |

---

## ⚙️ Why This Mnemonic Works

* **C (Count)** keeps the supply (like inventory).
* **U (Use)** ensures we don’t double-use elements.
* **E (Extend)** prevents leaving short subsequences unfinished.
* **S (Start)** ensures new subsequences meet min length `k`.

Once you memorize **C-U-E-S**, you can reconstruct the entire logic from memory in ~30 seconds in **any language**.

---

## 🗣️ What to Say if Asked “Can you explain your thought process?”

> “I’ll count how many of each number I have.
> Then for each number in order, I’ll use it either to **extend** an existing chain that’s waiting for it,
> or if that’s not possible, I’ll **start** a new chain by consuming the next `k−1` consecutive numbers.
> If I can’t do either, the split is impossible.”

---

Would you like me to make a **visual “sticky-note” version (diagram/mind-map)** of this mnemonic (C-U-E-S) for quick recall before interviews?
