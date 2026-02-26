### ✅ 5-line pseudo-code template (memorize)

```text
build 2D prefix sum P
ans = 0
for size = 1 .. min(n,m):
  for each top-left (r,c) where square fits:
     if sumSquare(r,c,size) using P == x: ans++
return ans
```

### 🧠 Easy mnemonic

**“P-S-S” = Prefix → Squares → Sum-check**

* **P**refix: preprocess sums once
* **S**quares: try all sizes + positions
* **S**um-check: O(1) query using prefix

### ⏱ 60-second recall script (say this before/inside interview)

1. “We need count of **square** submatrices with sum = x.”
2. “Direct summing each square is too slow, so I’ll build a **2D prefix sum**.”
3. “With prefix, any square sum becomes an **O(1) rectangle sum query**.”
4. “Then I’ll enumerate square sizes `1..min(n,m)` and all valid top-left positions.”
5. “If computed square sum equals x, increment answer.”
6. “Complexity: build prefix `O(n*m)`, checks `O(n*m*min(n,m))`, space `O(n*m)`.”
