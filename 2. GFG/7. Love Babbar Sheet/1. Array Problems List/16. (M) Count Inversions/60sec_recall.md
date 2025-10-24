**5-line pseudo-code template** and **60-second recall mnemonic** for **Count Inversions**, built exactly for fast recall before or during interviews (usable in **Python / C++ / Java / Go / JS**).

---

## 🧩 5-Line Pseudo-Code Template (Universal Skeleton)

```text
function countInversions(arr):
    if len(arr) <= 1: return 0
    mid = len(arr) // 2
    left_inv = countInversions(left half)
    right_inv = countInversions(right half)
    cross_inv = merge_and_count(left, right)
    return left_inv + right_inv + cross_inv
```

### Inside `merge_and_count(left, right)`:

```text
i, j, inv = 0, 0, 0
while i < len(left) and j < len(right):
    if left[i] <= right[j]: take left[i]; i++
    else: take right[j]; inv += (len(left) - i); j++
return inv
```

That’s it — the full logic in **10 lines total**.

---

## 🧠 Mnemonic for 60-second Recall — “SPLIT–SORT–COUNT”

> **S.P.L.I.T →**
> **S** – Split array into halves
> **P** – Process left half recursively
> **L** – Process right half recursively
> **I** – Inversions counted during merge
> **T** – Total inversions = left + right + merge

**OR** think of it like a story:

> “Every time we merge two sorted halves, if a left number jumps over a right number — that’s an inversion.”

---

## 🧮 Visual Cue (Dry-Run Mini Example)

Array = `[2, 4, 1, 3, 5]`

```
Split → [2,4,1] + [3,5]
    Split [2,4,1] → [2,4] + [1]
        Merge [2,4] & [1] → 2 inversions (2>1,4>1)
    Merge [1,2,4] & [3,5] → +1 inversion (4>3)
Total = 3 inversions
```

---

## 🧩 One-Liner Explanation for Interview

> “I use merge sort; during merge, whenever left[i] > right[j],
> all remaining elements from left[i..] form inversions — so I add (mid - i + 1).
> The total is O(n log n) time and O(n) space.”

---

## ⚡ 60-Second Interview Recall Plan

| Time   | What to Recall / Say                                      | Mnemonic                            |
| ------ | --------------------------------------------------------- | ----------------------------------- |
| 0–10s  | “Need pairs (i < j, arr[i] > arr[j]). Brute is O(n²).”    | “Compare everything = slow.”        |
| 10–25s | “Use merge sort — count inversions while merging.”        | “Divide & conquer counts swaps.”    |
| 25–40s | “During merge, if left[i] > right[j], add (mid - i + 1).” | “Left block dominates right block.” |
| 40–50s | “Time O(n log n), space O(n). Works for large n ≤ 1e5.”   | “Merge sort rules.”                 |
| 50–60s | “Edge cases: sorted=0, reverse= n*(n-1)/2, equal=0.”      | “Sorted = calm, reversed = chaos.”  |

---

## 🧠 Bonus Trick — “Dance Floor Analogy 💃”

Imagine each number as a dancer.
When a taller dancer (left[i]) jumps **ahead** of a shorter one (right[j]) during merging,
we count how many taller ones are still waiting to dance — **that’s (mid - i + 1) inversions**.

→ This picture helps you **never forget the counting logic.**
