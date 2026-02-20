### 5-line pseudo-code template (memorize)

```text
convert numbers to strings
sort strings with rule: a before b if (a+b) > (b+a)     # "AB vs BA"
join sorted strings into ans
if ans starts with '0': return "0"
return ans
```

### Easy mnemonic (very sticky)

**“AB > BA ⇒ A first”**
Say it like a chant: **“Compare AB, Compare BA, Bigger goes first.”**

### 60-second recall script (what you say before/inside interview)

1. “Goal: arrange numbers so concatenation is maximum.”
2. “Normal numeric sort fails, so I’ll use a custom rule on pairs.”
3. “For any two numbers `a,b` (as strings), decide order by comparing `ab` vs `ba`.”
4. “Sort using that comparator, then join the strings.”
5. “Edge case: if result starts with `0`, all are zeros → return `0`.”
6. “Complexity: `O(n log n)` comparisons; each comparison is `O(k)` digits → `O(n log n * k)`.”
