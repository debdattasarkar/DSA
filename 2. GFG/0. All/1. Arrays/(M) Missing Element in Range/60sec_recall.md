### 5-line pseudo-code template (memorize)

```text
make a set S from arr
ans = empty list
for x from low to high:
    if x not in S: append x to ans
return ans   # already sorted because x increases
```

### Easy mnemonic

**“Set + Sweep + Spit”**

* **Set**: store existing numbers in a hash set
* **Sweep**: walk from `low → high`
* **Spit**: output the ones not found (missing)

### 60-second recall script (say this before/inside interview)

1. “We need all numbers in `[low, high]` that are not in the array, in sorted order.”
2. “I’ll put all array values into a **set** for O(1) average membership checks.”
3. “Then I’ll **iterate from low to high**; if a value isn’t in the set, it’s missing.”
4. “Because I iterate in increasing order, the result is automatically **sorted**.”
5. “Complexity: building set `O(n)`, scanning the range `O(high-low+1)`, space `O(n)`.”
