Memorizable kit for **“Move all negative elements to the end (stable)”**.

---

## ⚡ 5-line universal pseudo-code (stable O(n) / O(n))

```
1. pos ← empty list
2. neg ← empty list
3. for each x in arr:
4.     if x ≥ 0 then append x to pos else append x to neg
5. arr[:] ← pos + neg
```

### 🧠 Mnemonic

**“Scan → Split → Stitch.”**
Say it out loud: *scan the array, split into pos/neg, stitch back with `pos` first*.

---

## ⏱️ 60-second recall script (what to say before coding)

> “This is a **stable partition**: keep order within positives and within negatives.
> I’ll do one linear scan, collect `pos` and `neg`, then overwrite the array:
> **Time O(n)**, **Space O(n)**. If they insist on in-place and stable, it becomes **O(n²)** by shifting (or **O(n log n)** with block rotations).”

---

## 30-second rebuild in 4 languages

* **Python:** `pos=[x for x in arr if x>=0]; neg=[x for x in arr if x<0]; arr[:]=pos+neg`
* **C++:**

  ```cpp
  vector<int> pos, neg;
  for (int x: arr) (x>=0?pos:neg).push_back(x);
  int i=0; for (int x: pos) arr[i++]=x; for (int x: neg) arr[i++]=x;
  ```
* **Java:**

  ```java
  List<Integer> pos=new ArrayList<>(), neg=new ArrayList<>();
  for (int x: arr) if (x>=0) pos.add(x); else neg.add(x);
  int i=0; for (int x: pos) arr[i++]=x; for (int x: neg) arr[i++]=x;
  ```
* **JavaScript:**

  ```js
  const pos = arr.filter(x=>x>=0), neg = arr.filter(x=>x<0);
  arr.splice(0, arr.length, ...pos, ...neg);
  ```

---

## Quick interviewer Q&A you can rattle off

* **Q:** Why not two-pointer swaps?
  **A:** That’s **unstable**; order within groups changes.
* **Q:** In-place + stable?
  **A:** Yes, but **O(n²)** by shifting blocks; or **O(n log n)** via divide-and-conquer + rotations.
* **Q:** How do you treat zero?
  **A:** As **non-negative** (goes with positives).

Memorize **Scan → Split → Stitch**, and you’ll rebuild this in any language in seconds.
