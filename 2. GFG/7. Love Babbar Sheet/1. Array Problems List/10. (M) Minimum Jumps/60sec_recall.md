**“60-second recall kit”** and **5-line pseudo-code skeleton** for the **Minimum Jumps (Greedy – Ladder & Stairs)** problem — a very common Amazon / Flipkart / Adobe favorite.

---

## 🧠 5-Line Pseudo-Code Template (universal)

```
function minJumps(arr):
    if n <= 1: return 0                   # already at end
    if arr[0] == 0: return -1             # can't move
    jumps = 1; ladder = arr[0]; stairs = arr[0]
    for i from 1 to n-1:
        if i == n-1: return jumps         # reached end
        ladder = max(ladder, i + arr[i])  # best future reach
        stairs -= 1                       # step used
        if stairs == 0:                   # jump window ends
            jumps += 1
            if i >= ladder: return -1     # stuck
            stairs = ladder - i           # reset stairs
```

✅ This exact 5-line logic is **greedy**, **O(n)**, and **space O(1)**.

---

## 🧩 Mnemonic (to recall easily)

> **“Climb ladder, count stairs.”**

1️⃣ **Ladder** = farthest reachable point so far (global best).
2️⃣ **Stairs** = steps remaining within current jump (local window).
3️⃣ **Each step:**

* update **ladder** with `max(ladder, i + arr[i])`
* use one **stair** (`stairs -= 1`)
* if **stairs == 0** → take a jump → reset window (`stairs = ladder - i`).
  4️⃣ Stop once you hit the end.

So the mental rhythm is:

> **“Step, Update, Jump, Reset.”**

---

## ⚙️ Quick Dry-Run Example

```
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
```

|                                              i | arr[i] | ladder | stairs | jumps | action                                   |
| ---------------------------------------------: | -----: | -----: | -----: | ----: | :--------------------------------------- |
|                                              0 |      1 |      1 |      1 |     1 | initialize                               |
|                                              1 |      3 |      4 |      0 |     2 | stairs=0 → jump, reset stairs=ladder-i=3 |
|                                              2 |      5 |      7 |      2 |     2 |                                          |
|                                              3 |      8 |     11 |      1 |     2 |                                          |
|                                              4 |      9 |     13 |      0 |     3 | stairs=0 → jump                          |
| ✅ Reaches end inside 3rd jump → **Answer = 3** |        |        |        |       |                                          |

---

## 🧠 60-Second Pre-Interview Recall Routine

When interviewer asks:

> “Find minimum jumps to reach array end.”

You immediately say:

1️⃣ If `n <= 1`, return 0.
2️⃣ If first element is 0, return -1.
3️⃣ Initialize:

* `jumps = 1`
* `ladder = arr[0]`
* `stairs = arr[0]`
  4️⃣ For each index:
* Update `ladder = max(ladder, i + arr[i])`
* Use a stair (`stairs -= 1`)
* If stairs exhausted → jump (`jumps += 1`, `stairs = ladder - i`)
  5️⃣ Return `jumps` if reach end, else -1.

---

## 💬 10-Second “Why It Works” Answer

> “Each window of reachable indices acts like a BFS level.
> When stairs (steps) run out, you’ve finished one jump window — taking a new jump extends reach to the farthest `ladder`.
> That’s why the first time we run out of stairs, we make the minimum possible jumps.”

---

## ✅ Quick Summary Table

| Step | Meaning                                 | Keyword          |
| ---- | --------------------------------------- | ---------------- |
| 1️⃣  | `ladder` = farthest reach so far        | **Ladder**       |
| 2️⃣  | `stairs` = steps left in current window | **Stairs**       |
| 3️⃣  | `stairs--` each step                    | **Step**         |
| 4️⃣  | When `stairs==0` → `jumps++`, reset     | **Jump & Reset** |
| 5️⃣  | Return `jumps` when reach end           | **Answer**       |

🧩 **Mnemonic:**

> **“Ladder climbs, stairs count — step, jump, reset.”**

This 5-line skeleton can be rebuilt in **any language in under 30 seconds**.
