Here’s a tiny “cheat card” version you can replay before interviews.

---

## 5-line pseudo-code template (bitmask DP TSP)

```text
dp[1<<0][0] = 0
for mask in 0..(1<<n)-1 with bit0 set:
    for u in 0..n-1 where dp[mask][u] < INF:
        for v in 0..n-1 where v not in mask:
            dp[mask | (1<<v)][v] = min(dp[mask | (1<<v)][v], dp[mask][u] + cost[u][v])
answer = min over u of dp[(1<<n)-1][u] + cost[u][0]
```

That’s literally all you need. From this you can rebuild the full code in Python/C++/Java in under a minute.

---

## Easy mnemonic (60-second recall)

Think:

> **“0 fixed, MASK grows, LAST moves.”**

Break it into a 3-step chant:

1. **State = (mask, last):**
   `mask` = visited set, `last` = current city.

2. **Transition = add unvisited:**
   For each `(mask, last)`, try every `next` not in `mask`:
   `new_mask = mask | (1<<next)` and relax
   `dp[new_mask][next] = min(dp[new_mask][next], dp[mask][last] + cost[last][next])`.

3. **Finish = all visited + back to 0:**
   When `mask = ALL`, answer is
   `min over last: dp[ALL][last] + cost[last][0]`.

Right before the interview, say to yourself:

> “State (mask, last); loop masks, then last, then next; at end, min over last + back to 0.”

That anchors both the DP idea and the exact loops you need to write.
