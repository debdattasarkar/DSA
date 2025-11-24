
---

# ✅ **5-Line Pseudo-Code Template (Universal, Works in Any Language)**

```
answer = 0
for each index i in array:
    count = (i + 1) * (n - i)
    if count is odd:
        answer = answer XOR arr[i]
return answer
```

That’s the whole optimized solution.

You can rewrite this in **any language in under 20 seconds**.

---

# 🎯 **The 3-Word Mnemonic: “Position Product Parity”**

Breakdown:

* **Position** → index `i`
* **Product** → `(i+1) * (n-i)`
* **Parity** → odd or even?

If `(i+1)*(n-i)` is **odd**, include the number in the final XOR.
If **even**, ignore (it cancels out).

Memorize **PPP = Position · Product · Parity**.

---

# ⏱ **60-Second Interview Recall Script (Say this before entering the room)**

> “Every subarray XOR is just the XOR of its elements.
> Instead of iterating all subarrays, I analyze **each element**.
>
> An element `arr[i]` appears in `(i+1)*(n-i)` subarrays.
> XOR cancels values that appear an even number of times.
> So I only XOR `arr[i]` into the answer when that product is **odd**.
>
> Thus I compute `(i+1)*(n-i) % 2` in O(1) for each element.
> The final answer is XOR of all elements whose contribution count is odd.
>
> Time complexity is O(n), space is O(1).”

This takes < 1 minute to rehearse and makes you sound extremely polished.

---
