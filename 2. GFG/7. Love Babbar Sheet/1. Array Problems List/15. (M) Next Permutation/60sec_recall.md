**“5-line pseudo-code template”** and **60-second recall guide** for **Next Permutation** — optimized for quick memory, intuitive recall, and multi-language rebuilding.

---

## 🧩 5-LINE PSEUDO-CODE TEMPLATE (universal version)

```
1. Find i = rightmost index where arr[i] < arr[i+1]
2. If i == -1 → reverse(arr); return
3. Find j = rightmost index where arr[j] > arr[i]
4. Swap(arr[i], arr[j])
5. Reverse(arr[i+1 ... end])
```

✅ Works for **Python**, **C++**, **Java**, **C**, **Go**, **JS**, etc.

---

## 🧠 MNEMONIC — “F.R.S.R.R.”

> **Find → Reverse → Swap → Reverse → Return**

Each letter represents a step:

| Step  | Action                     | Intuition                                                         |
| ----- | -------------------------- | ----------------------------------------------------------------- |
| **F** | **Find pivot (i)**         | Find where ascending pattern breaks (rightmost arr[i] < arr[i+1]) |
| **R** | **Reverse if none**        | If entire array descending → reset to lowest permutation          |
| **S** | **Swap with next greater** | Swap arr[i] with smallest element greater than it in the suffix   |
| **R** | **Reverse suffix**         | Make the tail the smallest possible order after swap              |
| **R** | **Return**                 | You’re done!                                                      |

---

## ⚙️ WHY IT WORKS — “Rightmost Rise Rule”

When you find the **rightmost rise** (arr[i] < arr[i+1]),
you know everything to the right is **descending** (maximal permutation of that suffix).
So to get the *next* permutation:

* increase arr[i] **minimally** by swapping with the next greater number,
* then **minimize the tail** by sorting/reversing it into ascending order.

---

## 🧮 DRY-RUN SNAPSHOT (in head)

```
arr = [2,4,1,7,5,0]
find i = 2 (1<7)
find j = 4 (arr[4]=5 > 1)
swap(1,5) → [2,4,5,7,1,0]
reverse after i → [2,4,5,0,1,7]
✅ done
```

---

## ⚡ 60-SECOND INTERVIEW RECALL PLAN

| Time   | Step                   | What to Recall / Say                                                 |
| ------ | ---------------------- | -------------------------------------------------------------------- |
| 0–10s  | **Identify pattern**   | “We need lexicographically next permutation (next larger ordering).” |
| 10–20s | **Rightmost pivot**    | “Find the rightmost index where arr[i] < arr[i+1].”                  |
| 20–30s | **Reverse check**      | “If none, reverse whole array → first permutation.”                  |
| 30–40s | **Swap logic**         | “Else find rightmost element > pivot and swap them.”                 |
| 40–50s | **Suffix reverse**     | “Then reverse suffix arr[i+1:] for minimal next order.”              |
| 50–60s | **Explain complexity** | “O(n) time, O(1) extra space — in place.”                            |

---

## 🗣️ 10-SECOND SUMMARY TO SAY TO INTERVIEWER

> “I’ll find the rightmost index where arr[i] < arr[i+1].
> If none, reverse all.
> Otherwise, swap arr[i] with the smallest greater element to its right,
> then reverse the suffix to make it the smallest next order — O(n) in-place.”

---

## 🧩 Bonus Trick — Remember with **“Ice Cream” Analogy 🍦**

Imagine the array as a **cone melting from the right**:

* You find the **first drip point** (where order breaks).
* Swap with the next biggest **scoop above** it.
* Then **re-freeze the rest (reverse)** into perfect shape.

→ You’ll *never forget* “Find–Swap–Reverse”.
