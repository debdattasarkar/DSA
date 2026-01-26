Here’s a **5-line skeleton** + a **60-second recall script** you can run in your head before interviews.

---

## 5-line pseudo-code template (Catalan via formula, easiest to rebuild)

```text
if n is odd: return 0
k = n / 2
binom = 1
for i = 1..k: binom = binom * (k + i) / i      // C(2k, k)
return binom / (k + 1)                         // Catalan(k)
```

### Mnemonic

**“Odd → Zero, Half → k, Build Choose, Divide by (k+1)”**
(O-Z / H-K / Choose / k+1)

---

## Alternative 5-line template (DP Catalan, most explainable)

```text
if n is odd: return 0
k = n / 2
dp[0] = 1
for i = 1..k: dp[i] = sum(dp[j] * dp[i-1-j] for j=0..i-1)
return dp[k]
```

### Mnemonic

**“Odd→0, Half→k, dp0=1, Split-Multiply-Sum, Answer dp[k]”**

---

## 60-second recall (what to say + do)

1. **Parity check (5s):**
   “Valid strings need equal opens/closes ⇒ length must be even.”

2. **Convert (5s):**
   “Let `k = n/2` pairs.”

3. **Recognize (10s):**
   “This is Catalan number: count of balanced parentheses.”

4. **Pick method (10s):**

* If interviewer likes math/optimization: **formula** `C(2k,k)/(k+1)`
* If interviewer wants reasoning: **DP split by first matching bracket**

5. **Code shape (20s):**

* Formula: loop i=1..k multiply/divide for binomial, then divide by k+1
* DP: nested loop `dp[i] += dp[j]*dp[i-1-j]`

6. **Close (10s):**
   “Odd → 0; even → compute Catalan(k). Complexity: formula O(n), O(1). DP O(k^2), O(k).”
