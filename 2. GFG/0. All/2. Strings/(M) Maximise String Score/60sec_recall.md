Here’s a compact “cheat card” you can replay quickly before interviews.

---

## 5-Line Pseudo-Code Template

```text
build allowed_targets_from[c] for all characters (include self)
init best_for_target[c] = -INF, dp[0] = 0, ascii_sum = ord(s[0]), count_char[ s[0] ] = 1
update best_for_target[ t ] from i=0 for all t in allowed_targets_from[ s[0] ]
for i = 1..n-1:
    dp[i] = ascii_sum - count_char[s[i]]*ord(s[i]) + best_for_target[s[i]]   // if reachable
    update best_for_target[ t ] = max(best_for_target[ t ],
        dp[i] - ascii_sum + count_char[t]*ord(t)) for all t in allowed_targets_from[ s[i] ]
    ascii_sum += ord(s[i]); count_char[s[i]] += 1
answer = max(0, max(dp))
```

From this skeleton you can rebuild full code in any language in ~30 seconds.

---

## Easy Mnemonic (60-second recall)

Think of the phrase:

> **“Prefix + Per-Char Best: LAND, UPDATE, MOVE.”**

Break it into steps:

1. **Prefix** – keep running `ascii_sum` and `count_char[26]` as you scan `s` left-to-right.
2. **Per-Char Best** – for each character `c`, store `best_for_target[c]` (the best previous place to jump *into* `c`).
3. At index `i` with char `c`:

   * **LAND**:
     `dp[i] = prefix_sum - count_c * ASCII(c) + best_for_target[c]`.
   * **UPDATE**: for every target `t` we can jump TO from `c`, update
     `best_for_target[t] = max(best_for_target[t], dp[i] - prefix_sum + count_t * ASCII(t))`.
   * **MOVE**: advance prefix (`ascii_sum += ASCII(c)`, `count_char[c]++`).

Repeat that chant in your head:

> **“For each char: LAND with (sum − count*ASCII + best), UPDATE all its targets, then MOVE prefix.”**

If you remember that, the formulas and the 5-line pseudo-code will fall back into place when you sit down to code.
