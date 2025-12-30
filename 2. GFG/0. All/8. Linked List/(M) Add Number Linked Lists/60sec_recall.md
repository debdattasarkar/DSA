### 5-line pseudo-code template (memorize)

```
h1 = reverse(h1);  h2 = reverse(h2)
carry = 0; dummy = Node(0); tail = dummy
while h1 or h2 or carry: sum = d(h1)+d(h2)+carry; tail.next = Node(sum%10); carry = sum//10; advance
ans = reverse(dummy.next)
return stripLeadingZeros(ans)
```

*(where `d(h)=h.data if h else 0`)*

---

## Mnemonic (30-sec)

**“REV → ADD → REV → TRIM”**
Reverse inputs → Add with carry → Reverse result → Trim leading zeros

---

## 60-second recall script (what to say in interview)

1. “Digits are in forward order, but addition needs LSD first.”
2. “So I reverse both lists.”
3. “Then I do classic digit addition with a `carry`, building a result list.”
4. “Reverse the result to restore forward order.”
5. “Remove leading zeros (keep one zero if result is 0). Complexity: O(n+m), space O(1) auxiliary.”
