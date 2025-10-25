**Mentally rehearse in the last 60 seconds before an interview**.

---

## 🧠 **5-Line Pseudo-Code Template (Universal Skeleton)**

```
profit = 0
for i = 1 to n-1:
    if price[i] > price[i-1]:
        profit += price[i] - price[i-1]
return profit
```

✅ **That’s it.**
Same in **C++**, **Python**, **Java**, or even **pseudocode** — just the “add the rises” logic.
It runs in **O(n)** time and **O(1)** space.

---

## 💡 **Easy Mnemonic (to lock it in your brain)**

> **“If it goes up, add the gap.”**

or

> **“Climb = Cash.”**

So while scanning prices, every *climb* adds to your *cash (profit)*.
You don’t care where the climb starts or ends — just sum every up-step.

---

## 🧩 **Mental Walk-through (60-second recall drill)**

1. **Restate problem:** “We can trade unlimited times, but hold one share at a time.”
2. **Optimal idea:** “Sum every positive difference — because splitting peaks and valleys doesn’t lose profit.”
3. **One loop:** Compare today vs yesterday, add if higher.
4. **Complexity:** Time O(n), Space O(1).
5. **Edge check:** All decreasing → profit = 0.

---

### ⚙️ “Language Snapshot” (for fast recreation)

**Python:**

```python
profit = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        profit += arr[i] - arr[i-1]
return profit
```

**C++:**

```cpp
int profit = 0;
for (int i = 1; i < n; i++)
    if (price[i] > price[i-1])
        profit += price[i] - price[i-1];
return profit;
```

**Java:**

```java
int profit = 0;
for (int i = 1; i < n; i++)
    if (arr[i] > arr[i-1])
        profit += arr[i] - arr[i-1];
return profit;
```

---

✅ **Summary for your brain:**

> “Loop once. If tomorrow’s price is higher, add the difference. Done.”
> That’s the *entire logic* you need to recall instantly under pressure.
