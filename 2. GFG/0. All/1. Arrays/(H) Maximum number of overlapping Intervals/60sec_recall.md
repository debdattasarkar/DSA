### 5-line pseudo-code template (memorize)

```text
events = []
for each [s,e]: add (s,+1), add (e,-1)
sort events by (time, start-before-end)   # inclusive trick
active = 0; best = 0
for (t,delta) in events: active += delta; best = max(best, active)
return best
```

### Easy mnemonic (sticky + interview-friendly)

**“E-S-W-M-R” → Events, Sort, Walk, Max, Return**

* **E**vents: make (start +1), (end -1)
* **S**ort: by time (**start before end** if same time)
* **W**alk: sweep through events updating `active`
* **M**ax: keep best peak
* **R**eturn: `best`

### 60-second recall script (what you say before/inside interview)

1. “I need the **peak concurrency** (max overlaps).”
2. “Convert intervals into **events**: start = +1, end = -1.”
3. “Because intervals are **inclusive**, if times tie, **process start before end**.”
4. “Sort events, then sweep left→right maintaining `active` overlaps.”
5. “Update `best = max(best, active)` each step.”
6. “Complexity: `O(n log n)` for sorting, `O(n)` sweep, space `O(n)`.”
