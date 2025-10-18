**“60-second recall kit”** and **5-line pseudo-code skeleton** for **Kadane’s Algorithm (Maximum Subarray Sum)** — the one-liner every interviewer loves you to know by heart.

---

## 🧠 5-Line Pseudo-Code Template (universal)

```
function maxSubarraySum(arr):
    cur = best = arr[0]              # start with first element
    for each x in arr[1:]:           
        cur = max(x, cur + x)        # extend or start new subarray
        best = max(best, cur)        # update global best
    return best
```

✅ Works in any language (Python / C++ / Java / JS).
Only needs `O(n)` time and `O(1)` space.

---

## 🧩 Mnemonic (to instantly recall)

> **“Extend or Restart, then Compare.”**

1️⃣ **Extend:** Add current element to previous sum (`cur + x`).
2️⃣ **Restart:** If previous sum was negative, start fresh with current `x`.
3️⃣ **Compare:** Update the global best so far.

Say it like a mantra before interviews:

> “Extend or Restart → Compare → Done.”

---

## ⚙️ Why it Works (Mental Picture)

Imagine walking through numbers:

* You keep a “running sum” (`cur`) that resets whenever it goes below zero.
* `best` always stores the **highest sum seen so far**.
* When all numbers are negative, initialization with `arr[0]` ensures the *least negative* is returned.

---

## 🧩 10-Second Example to Verify Logic

```
arr = [2, 3, -8, 7, -1, 2, 3]
```

| i | x  | cur = max(x, cur+x) | best |
| - | -- | ------------------- | ---- |
| 0 | 2  | 2                   | 2    |
| 1 | 3  | 5                   | 5    |
| 2 | -8 | -3                  | 5    |
| 3 | 7  | 7                   | 7    |
| 4 | -1 | 6                   | 7    |
| 5 | 2  | 8                   | 8    |
| 6 | 3  | 11                  | 11   |

✅ Output = **11** (`[7, -1, 2, 3]`)

---

## 🧠 60-Second Pre-Interview Recall Routine

When interviewer says:

> “Find the maximum subarray sum.”

You immediately say:
1️⃣ “Kadane’s Algorithm — O(n) time, O(1) space.”
2️⃣ “I track two sums: `cur` (best ending here) and `best` (global best).”
3️⃣ “At each step, either extend the previous subarray or restart fresh.”
4️⃣ “Return `best` at the end.”

✅ Speak it out once — then code in 30 seconds.

---

## 💬 Interview Sound Bite

> “Kadane’s Algorithm greedily builds the best subarray ending at each index; if the current sum becomes negative, it restarts.
> This guarantees an O(n) scan and O(1) space.”

---

## 🧩 Quick Summary Table

| Step | Action                         | Purpose              | Keyword |
| ---- | ------------------------------ | -------------------- | ------- |
| 1️⃣  | Initialize `cur=best=arr[0]`   | Handle all-negatives | Init    |
| 2️⃣  | For each x: `cur=max(x,cur+x)` | Extend or Restart    | Extend  |
| 3️⃣  | `best=max(best,cur)`           | Track global max     | Compare |
| 4️⃣  | Return `best`                  | Final result         | Return  |

> **Mnemonic:** “Init → Extend → Compare → Return.”

Remember that rhythm — it’s the heartbeat of Kadane’s Algorithm ❤️
