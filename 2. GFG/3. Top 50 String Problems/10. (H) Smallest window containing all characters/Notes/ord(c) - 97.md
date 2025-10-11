Great catch—let’s unpack this line:

```python
def idx(c):           # map 'a'..'z' -> 0..25
    return ord(c) - 97
```

### What it’s doing

* `ord(c)` gives the **Unicode code point** (think: number) for the character `c`.
* For lowercase English letters:

  * `ord('a') == 97`
  * `ord('b') == 98`
  * …
  * `ord('z') == 122`
* So `ord(c) - 97` converts:

  * `'a' -> 97 - 97 = 0`
  * `'b' -> 98 - 97 = 1`
  * …
  * `'z' -> 122 - 97 = 25`

That’s why we can use a **fixed array of size 26** where index 0 counts `'a'`, index 1 counts `'b'`, …, index 25 counts `'z'`. It’s fast and O(1) space.

### Safer / clearer variant

Instead of hard-coding `97`, use `ord('a')` so it’s self-explanatory:

```python
A = ord('a')  # 97
def idx(c):
    return ord(c) - A
```

### Examples

```python
>>> idx('a'), idx('m'), idx('z')
(0, 12, 25)
```

### What if the input isn’t lowercase?

* For **uppercase** letters, you could map `'A'..'Z'` similarly with `ord('A')`, or normalize first:

  ```python
  c = c.lower()  # then use the same idx
  ```
* If `c` is not a letter (e.g., `'#'`), `ord(c) - ord('a')` will be **outside 0..25**, so you should guard/validate:

```python
def idx_lower(c):
    if 'a' <= c <= 'z':             # fast ASCII check
        return ord(c) - ord('a')
    raise ValueError("expected lowercase a-z")
```

### Why this matters here

The problem states strings are **lowercase English letters**, so a 26-length array is perfect:

* Faster than dict/Counter (pure index arithmetic).
* Constant auxiliary space (`O(1)`), since 26 never changes.

That’s the whole story behind `ord(c) - 97`: it’s a quick, numeric mapping from `'a'..'z'` → `0..25`.


---

---

totally — here’s what each line is doing and **why** it matters in the sliding-window algorithm.

```python
# Build "need" counts from p; O(m)
need = [0] * 26
for ch in p:
    need[idx(ch)] += 1
```

* **Goal:** record how many copies of each character we **need** from `p` (including duplicates).
* `need` is a fixed-size array of length **26** because the problem says lowercase letters only (`'a'..'z'`).
* `idx(ch)` maps a char to an index `0..25` (e.g., `'a'→0`, `'z'→25`).
* After the loop, `need[i]` tells you **how many of letter `i`** are required.
  Example: `p = "ozaa"` → `need['a']=2`, `need['o']=1`, `need['z']=1`.

```python
have = [0] * 26   # current window counts; O(1)
```

* **Goal:** track how many copies of each character we **currently have** inside the sliding window `[l..r]` on `s`.
* Same 26-length array; it updates as we move `l` and `r`.

```python
missing = m       # how many total characters we still need; O(1)
```

* `m = len(p)`.
* **Key idea:** instead of tracking only *distinct* chars left to match, we count **every required occurrence**.
  Each time we add a character `c` to the window and `have[c]` does **not exceed** `need[c]`, we’ve satisfied **one** required occurrence → `missing -= 1`.
* When `missing == 0`, the current window **contains all characters** of `p` (with duplicates), so we can try to **shrink** it from the left to make it minimal.

```python
best_len = float("inf")
```

* We want the **shortest** valid window. Start with “no answer” as **infinity** so any real window length will be smaller.
* Whenever we have a valid window, compute its length and do:

  * if `curr_len < best_len`, update `best_len` and remember its start index;
  * if `curr_len == best_len`, tie-break by **smaller start index**.

---

### Tiny example to cement it

`p = "aab"`

* After building `need`: `need['a']=2`, `need['b']=1`, others 0.
* Start: `have = [0]*26`, `missing = 3`, `best_len = inf`.

Scan `s` with a right pointer `r`:

* When you add `'a'` and `have['a']` goes from 0→1 (≤ 2), `missing` becomes 2.
* Add another `'a'`, `have['a']` 1→2 (≤ 2) → `missing` becomes 1.
* Add `'b'`, `have['b']` 0→1 (≤ 1) → `missing` becomes 0 ⇒ window valid.
* Now **shrink from left** while `missing == 0`; each time you drop a char from the left, if `have[left_char]` becomes **less than** `need[left_char]`, you just broke validity → increment `missing` and stop shrinking.

That’s the whole pattern:

* `need` = what we must cover,
* `have` = what’s in the current window,
* `missing` = how many required occurrences still not covered,
* `best_len` = best (shortest) window seen so far.
