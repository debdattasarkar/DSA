## 5-line pseudo-code template (most memorable)

```text
half = n/2
A = dequeue first half from q
ans = empty queue
repeat half times: ans.push(A.pop()); ans.push(q.pop())
q = ans
```

### Mnemonic

**“Split → Store first half → Alternate A & Q → Done”**
(or shorter: **“Store-Alternate-StoreBack”**)

---

## 60-second recall (what to say + do)

1. **Trigger (5s):** “Even-sized queue → split into equal halves.”
2. **Extract (10s):** “Move first `n/2` elements into temp queue `A`.”
3. **Interleave (20s):** “For `half` times: push `A.front`, then push `q.front` (second half) into result.”
4. **Restore (10s):** “Copy result back to original queue.”
5. **Complexity (15s):** “Each element moved constant times → `O(n)` time; temp storage `O(n)` space.”

If you want a one-word cue: **“A-Q-A-Q…”** (take from temp first-half, then from remaining second-half).
