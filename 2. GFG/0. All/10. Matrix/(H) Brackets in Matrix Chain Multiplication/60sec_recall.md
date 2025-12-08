Here’s a **5-line sliding-window template** you can memorize and then “expand” into any language in seconds.

---

### 5-Line Sliding Window Pseudo-Code (variable or fixed size)

```text
1. start = 0; best = INIT; window_state = EMPTY
2. for end in [0 .. n-1]:
3.     add A[end] to window_state        // expand window
4.     while window_is_invalid():        // or while window_size > K for fixed-size
           remove A[start] from window_state; start += 1   // shrink
5.     best = update_answer(best, window_state)
```

That’s it. You just plug in what **window_state**, **window_is_invalid()**, and **update_answer()** mean for each problem.

---

### How this maps to common problems

* **Fixed-size sum (max sum of size K)**

  * `window_is_invalid(): window_size > K`
  * `window_state = current_sum`
  * `best = max(best, current_sum)` when `window_size == K`.

* **Longest substring without repeating chars**

  * `window_state = counts of chars`
  * `window_is_invalid(): some char count > 1`
  * `best = max(best, window_length)`.

* **Smallest subarray with sum ≥ S**

  * `window_state = current_sum`
  * `window_is_invalid(): current_sum >= S` (shrink while still valid)
  * `best = min(best, window_length)` inside the `while`.

---

### 60-Second Recall / Mnemonic

Think: **“GROW → FIX → RECORD”**

1. **GROW** – move `end` forward, **add** `A[end]` to your window.
2. **FIX** – while window “breaks the rule”, **remove** `A[start]`, move `start`.
3. **RECORD** – update `best` from the current window.

Or as a chant you can say to yourself:

> **“Expand, while-bad shrink, then update answer.”**

If you remember those 5 lines + the “Grow → Fix → Record” mantra, you can rebuild sliding-window code in any language in under a minute before (or during) an interview.
