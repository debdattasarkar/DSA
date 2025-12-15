Here’s your tiny “brain card” for this problem ❤️

---

## 5-line pseudo-code template (balance after removing one index)

```text
precompute right_even, right_odd from array
left_even = left_odd = 0; ans = 0
for i from 0..n-1:
    subtract arr[i] from (right_even or right_odd) based on i%2
    if left_even + right_odd == left_odd + right_even: ans++
    add arr[i] to (left_even or left_odd) based on i%2
return ans
```

That’s all the logic. From this you can write full code in any language.

---

## Easy mnemonic (60-second recall)

Think of **two buckets on the left and two on the right**:

* `LE` = left even sum
* `LO` = left odd sum
* `RE` = right even sum
* `RO` = right odd sum

Key rule:

> After removing `i`: **`new_even = LE + RO`, `new_odd = LO + RE`**

So the check per index is:

> **`LE + RO == LO + RE`**

And the flow is:

1. **Init** totals on right (`RE`, `RO`).
2. For each `i`:

   * Remove `arr[i]` from `RE` or `RO`.
   * Check `LE + RO == LO + RE`.
   * Move `arr[i]` into `LE` or `LO`.

If you remember just:

> **“LE+RO vs LO+RE, move current from right to left each step”**

you can reconstruct the whole O(n), O(1) solution during the interview in under a minute.
