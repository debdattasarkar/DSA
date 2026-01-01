### 5-line pseudo-code template (memorize)

```
slow=head; fast=head
while fast && fast.next: slow=slow.next; fast=fast.next.next
if fast: slow=slow.next              // skip middle (odd length)
rev = reverse(slow)
for p=head, q=rev while q: if p.val!=q.val return False; p=p.next; q=q.next
reverse(rev) (optional); return True
```

---

## Mnemonic (30-sec)

**“MID → REV → MATCH → RESTORE”**

* **MID**: find middle (slow/fast)
* **REV**: reverse second half
* **MATCH**: compare halves
* **RESTORE**: reverse back (optional)

---

## 60-second recall script (what to say in interview)

1. “Palindrome means same forward and backward; linked list can’t go backward.”
2. “Find the middle using slow/fast pointers.”
3. “If odd length, skip the middle node.”
4. “Reverse the second half and compare node-by-node with the first half.”
5. “Optionally reverse back to restore. Time O(n), space O(1).”
