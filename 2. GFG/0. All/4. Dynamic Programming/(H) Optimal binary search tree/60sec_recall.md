Here’s a little “index card” for Optimal BST that you can replay before interviews.

---

## 5-line pseudo-code template (Optimal BST DP)

```text
build prefixFreq[] so sum(i..j) = prefixFreq[j+1] - prefixFreq[i]
for i in 0..n-1: dp[i][i] = freq[i]
for len in 2..n:
    for i in 0..n-len:
        j = i + len - 1
        dp[i][j] = min over r in [i..j] of (dp[i][r-1] + dp[r+1][j] + sum(i..j))
return dp[0][n-1]
```

From this, you can rebuild full Python/C++/Java code very quickly.

---

## Easy mnemonic (60-second recall)

Think:

> **“Interval DP: [i..j], try each root, add total freq.”**

Break it into 3 micro-steps:

1. **Prefix sums** – “precompute `sum(i..j)` in O(1)”
   → `prefixFreq` so you don’t recompute sums.

2. **Interval DP** – “`dp[i][j]` = best cost for keys i..j”
   → fill by length (`len`) so smaller subproblems are ready.

3. **Root loop** – “for each root r, cost = left + right + totalFreq”
   → left = `dp[i][r-1]`, right = `dp[r+1][j]`, `totalFreq = sum(i..j)`.

If, right before the interview, you say to yourself:

> “`dp[i][j]` over intervals, prefix sums for freq, each root r → left + right + sum(i..j); answer = dp[0][n-1].”

you’ll have everything you need to reconstruct the full Optimal BST solution.
