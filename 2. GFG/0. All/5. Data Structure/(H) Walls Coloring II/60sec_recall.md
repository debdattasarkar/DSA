Here’s a tiny “cheat card” you can replay just before interviews.

---

## 5-line pseudo-code template (O(n·k) DP)

```text
if k == 1 and n > 1: return -1
prev[c] = costs[0][c] for all colors c
for each wall i from 1 to n-1:
    find (min1_val, min1_color, min2_val) from prev[]
    curr[c] = costs[i][c] + (min1_val if c != min1_color else min2_val) for all c
    prev = curr
return min(prev)
```

From this you can reconstruct the full solution in any language very quickly.

---

## Easy mnemonic (60-second recall)

Think:

> **“Row DP with two bests: best, second-best, avoid best’s color.”**

In your head, step through:

1. **Base row** – “First wall: `prev[c] = cost[0][c]`.”
2. **Two bests** – “Each new wall: scan previous row → `min1`, its `color`, and `min2`.”
3. **Transition** – “For each color `c`:

   * if `c == min1_color` → use `min2`,
   * else → use `min1`.”
4. **Update** – “Set `prev = curr`.”
5. **Answer** – “Return `min(prev)`.”

Repeat the phrase before you go in:

> **“Per wall: find two minima, use best unless same color, otherwise second-best.”**

That’s enough to rebuild the full DP and explain it clearly to the interviewer.
