### 5-line pseudo-code template (memorize this)

```
freq = countFrequency(arr)
stack = empty              // stores indices
for i from n-1 downto 0:
    while stack not empty AND freq[arr[stack.top]] <= freq[arr[i]]: stack.pop
    ans[i] = (stack empty) ? -1 : arr[stack.top]
    stack.push(i)
```

That’s the whole solution.

---

## Easy mnemonic to recall fast

**“Count → Right → Pop ≤ → Answer Top → Push”**

* **Count** frequencies first
* Go from **Right** to left
* **Pop ≤** (pop while right candidate’s freq is ≤ current freq)
* **Answer Top** (top is next greater frequency)
* **Push** current index

If you remember just: **“Count + NGE on frequency”**, you’ll rebuild it.

---

## 60-second recall script (what you mentally rehearse)

1. “Frequency is global, so build `freq[value]`.”
2. “Now each position has a key = `freq[arr[i]]`.”
3. “I need next element to the right with a strictly greater key.”
4. “That’s Next Greater Element, but compare by frequency.”
5. “Traverse from right with stack of indices.”
6. “While top’s frequency ≤ current frequency: pop.”
7. “After pops: top (if exists) is answer value; else -1.”
8. “Push current index.”

That’s enough to code it in any language in under 30 seconds.
