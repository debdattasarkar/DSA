**5-line pseudo-code template** 🧠 for **“Minimum Steps to Halve Sum”**, plus a **simple mnemonic trick (H→H→H)** to recall it in **under 60 seconds** before an interview.

---

## ⚡️ The 5-Line Pseudo-code Template

This is language-agnostic (works for Python / C++ / Java):

```
sum0 = SUM(arr)
target = sum0 / 2
make maxHeap from arr
while sum0 > target:
    x = pop maxHeap; sum0 -= x/2; push x/2 back; count++
return count
```

✅ **That’s literally the whole logic.**
You can rebuild the full function around it in *any* language within 30 seconds.

---

## 🧠 60-Second Recall Trick — Mnemonic: **“H → H → H”**

### Step-by-step breakdown:

| Symbol        | Meaning                   | Action                            | Think of it as             |
| :------------ | :------------------------ | :-------------------------------- | :------------------------- |
| **H₁ → Heap** | Build a max heap          | Fast access to the largest number | “Who’s the heaviest?”      |
| **H₂ → Half** | Pop the largest, halve it | Reduces total sum quickly         | “Cut the biggest in half!” |
| **H₃ → Halt** | Stop when sum ≤ half      | Check target condition            | “We’ve done enough!”       |

So:

> **Heap → Half → Halt**

Repeat that mentally once, and the code pattern will instantly resurface.

---

## 🧩 Quick Example (Mentally Dry Run)

Input: `[8, 6, 2]`

| Step             | Largest | Halved | New Sum | Action   |
| ---------------- | ------- | ------ | ------- | -------- |
| Start            | —       | —      | 16      | target=8 |
| 1                | 8       | 4      | 12      | push 4   |
| 2                | 6       | 3      | 9       | push 3   |
| 3                | 4       | 2      | 8       | stop     |
| ✅ **Answer = 3** |         |        |         |          |

---

## 💬 Interview-ready Summary (30-second verbal answer)

> “I use a greedy approach with a max-heap.
> At each step, I halve the largest element — that gives the biggest drop in total sum.
> I keep pushing the halved values back into the heap until the total sum becomes ≤ half of the original.
> The time complexity is O(n + k log n), and space is O(n).
> Mnemonically: *Heap → Half → Halt*.”

---

## 🎯 5-Second Visual Cue (to recall)

```
  ┌─────────────┐
  │  Max Heap   │  ← biggest element
  └─────┬───────┘
        │  pop()
        ▼
   halve → push_back
        │
   repeat until sum ≤ half
```

---
