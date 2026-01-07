### 5-line pseudo-code template (memorize)

```
freq = counts of first k elements
ans = [ size(freq) ]
for r in k..n-1:
    freq[arr[r]]++ ; freq[arr[r-k]]-- ; if freq[arr[r-k]]==0: delete it
    ans.append(size(freq))
return ans
```

---

## Mnemonic (30-sec)

**“IN++, OUT--, ZERO → DELETE”**
and **“#keys = #distinct”**

---

## 60-second recall script (say this in interview)

1. “Need distinct count in every fixed window of size k.”
2. “Use a hashmap of frequencies for the current window.”
3. “Build counts for first k elements; distinct = number of keys.”
4. “Slide window: increment incoming, decrement outgoing, delete if count becomes 0.”
5. “Append `len(map)` each step. Complexity: O(n) time, O(k) space.”
