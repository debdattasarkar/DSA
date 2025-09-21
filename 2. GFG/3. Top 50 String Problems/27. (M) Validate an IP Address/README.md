# Validate an IP Address

**Difficulty:** Medium
**Accuracy:** 11.22%  **Submissions:** 299K+  **Points:** 4  **Average Time:** 20m

You are given a string `s` in the form of an IPv4 Address. Your task is to validate an **IPv4 Address**; if it is valid return **true** otherwise return **false**.

**IPv4 addresses** are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., `"172.16.254.1"`.

A **valid IPv4 Address** is of the form `x1.x2.x3.x4` where `0 ≤ (x1, x2, x3, x4) ≤ 255`. Thus, we can write the generalized form of an IPv4 address as `(0–255).(0–255).(0–255).(0–255)`.

> **Note:** Here we are considering numbers only from 0 to 255 and **any additional leading zeroes will be considered invalid**.

---

## Examples

**Input:** `s = "222.111.111.111"`
**Output:** `true`
**Explanation:** Here, the IPv4 address is as per the criteria mentioned and also all four decimal numbers lie in the mentioned range.

---

**Input:** `s = "5555..555"`
**Output:** `false`
**Explanation:** `"5555..555"` is not a valid IPv4 address, as the middle two portions are missing.

---

**Input:** `s = "0.0.0.255"`
**Output:** `true`

---

## Constraints

* `1 ≤ |s| ≤ 15`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Zoho, Amazon, Microsoft, Qualcomm

## Topic Tags

Strings, Data Structures

## Related Articles

Program To Validate An Ip Address

---

---

Here’s a crisp interview-ready pack for **“Validate IPv4 address”** 👇

---

## 2) Clear explanation + step-by-step dry runs

### What makes a valid IPv4?

* Exactly **4 groups** (octets) separated by dots `.`
* Each group is **only digits**, no leading/trailing spaces or signs
* Value range **0…255**
* **No leading zeros** unless the value is exactly `"0"` (so `"0"` ✅, `"00"` ❌, `"01"` ❌)
* No empty groups (so no `..`, no leading/trailing dot)

### Dry run 1 — Valid

`"0.0.0.255"`

* Split → `["0","0","0","255"]` → 4 parts ✅
* `"0"` → digits ✅ → value 0 in \[0,255] ✅ and no leading zero issue ✅
* `"0"` → ✅
* `"0"` → ✅
* `"255"` → digits ✅ → 255 in \[0,255] ✅ and not `"0255"` ✅
* All checks pass → **valid**

### Dry run 2 — Invalid (leading zero)

`"192.168.001.1"`

* Parts: `["192","168","001","1"]` → 4 parts ✅
* `"192"` → digits, 192 in range, no leading zero ✅
* `"168"` → ✅
* `"001"` → digits ✅ but **leading zeros** (length > 1 and startswith '0') ❌
* Can stop → **invalid**

### Dry run 3 — Invalid (missing groups)

`"5555..555"`

* Split → `["5555", "", "555"]` → **3 parts** ❌
* Not exactly 4 → **invalid**

---

## 3) Python solutions (two ways)

### A) “Brute/easy” (split & check) — simple and expected in interviews

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Split by '.' and ensure exactly 4 groups
        parts = s.split('.')
        if len(parts) != 4:
            return False

        for p in parts:
            # 1) non-empty, 2) digits only
            if not p or not p.isdigit():
                return False

            # 3) no leading zeros unless the group is exactly "0"
            if len(p) > 1 and p[0] == '0':
                return False

            # 4) numeric range 0..255
            val = int(p)
            if val < 0 or val > 255:
                return False

        # All 4 parts passed validation
        return True
```

**Time:** `O(n)` (single pass through characters)
**Space:** `O(1)` (ignoring the split list overhead; no extra data structures)

### B) “Optimized one-pass” (manual parse without `split`) — robust & space-tight

```python
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        groups = 0
        i = 0

        while i < n:
            # Each group must start with a digit
            if not s[i].isdigit():
                return False

            # Leading zero rule: if '0' starts a group, the group is "0" only
            if s[i] == '0':
                num_len = 1
                i += 1
            else:
                # Parse up to 3 digits (max 255)
                num_len = 0
                val = 0
                while i < n and num_len < 3 and s[i].isdigit():
                    val = val * 10 + (ord(s[i]) - 48)  # fast digit to int
                    num_len += 1
                    i += 1
                # We parsed 1..3 digits; check range
                if val > 255:
                    return False

            groups += 1
            if groups > 4:
                return False

            # After a group: expect dot if not last group
            if groups < 4:
                if i >= n or s[i] != '.':
                    return False
                i += 1  # skip the dot

        # Must have consumed all chars and formed exactly 4 groups
        return groups == 4 and i == n
```

**Why this version?**

* Avoids creating intermediate strings; checks leading zeros and range on the fly
* **Time:** `O(n)`; **Space:** `O(1)`

### C) (Optional) Regex solution — concise but less instructive in interviews

Regex that enforces 0…255 and no leading zeros:

```python
import re

class Solution:
    _pat = re.compile(r"""
        ^(
            (25[0-5]|2[0-4]\d|1?\d?\d)   # 0-255 without leading plus/minus
            \.
        ){3}
        (25[0-5]|2[0-4]\d|1?\d?\d)$
    """, re.X)

    def isValid(self, s: str) -> bool:
        # Reject leading zeros like "01" (regex allows "00" to "09", so we add a check)
        if self._pat.match(s) is None:
            return False
        # Enforce "no leading zeros unless the octet is exactly '0'"
        for part in s.split('.'):
            if len(part) > 1 and part[0] == '0':
                return False
        return True
```

> Interviewers often prefer A or B because they show explicit handling and edge-case thinking.

---

## 4) Likely interviewer Q\&A

**Q1. What edge cases should we worry about?**

* Empty parts: `"1..1.1"`, leading/trailing dot: `".1.2.3.4"`, `"1.2.3.4."`
* Non-digit characters: `"1.a.3.4"`, signs: `"-1.2.3.4"`
* Leading zeros: `"01.2.3.4"`, `"00.0.0.0"` (invalid except `"0"`)
* Range overflow: `"256.0.0.1"`, `"999.0.0.1"`
* Wrong number of groups: `"1.2.3"`, `"1.2.3.4.5"`

**Q2. Why disallow leading zeros?**
To avoid ambiguity (octal interpretation in some contexts) and because the problem statement explicitly forbids “additional leading zeroes”.

**Q3. Complexity?**
Both split-based and one-pass solutions are **O(n)** time and **O(1)** extra space (besides the small array from `split` in the first).

**Q4. Would your solution accept spaces?**
No. Per spec, IPv4 groups must be digits only. Inputs like `" 1.2.3.4"` or `"1.2. 3.4"` are invalid.

**Q5. How would you extend to IPv6?**
Change the grammar to 8 groups of 1–4 hex digits separated by `:`, allow leading zeros, and handle `::` compression rules (trickier).

**Q6. Is regex a good idea here?**
It can be concise but is harder to read/maintain and easy to get subtly wrong (esp. with leading-zero rules). For interviews, a clear procedural check is preferred.

---

---

Below is a complete, runnable Python program that:

* Implements **Validate IPv4** (two methods: straightforward split-check and a one-pass parser)
* Includes **inline time & space complexity comments at each step**
* Demonstrates the functions on a set of **sample inputs** and prints **outputs**
* Uses **`timeit`** in `__main__` to time the end-to-end validation over a batch of test cases

---

```python
"""
Validate IPv4 Address — Full Program

Two implementations:
  1) isValid (split & check) — simple and interview-friendly
  2) isValid_one_pass (single scan without split) — constant space & robust

Both run in O(n) time (n = len(s)) and O(1) auxiliary space.
"""

from timeit import timeit


class Solution:
    # ------------------------------------------------------------
    # Method A: Split & Check (interview favorite)
    # ------------------------------------------------------------
    def isValid(self, s: str) -> bool:
        """
        Time:  O(n) — single pass across characters while checking 4 parts
        Space: O(1) — aside from the small list from split (constant #parts)
        """
        # Split by '.' and ensure exactly 4 octets
        parts = s.split('.')                              # O(n) to split
        if len(parts) != 4:                               # constant check
            return False

        for p in parts:                                   # 4 iterations max
            # 1) non-empty and all digits
            if not p or not p.isdigit():                  # O(len(p))
                return False

            # 2) leading-zero rule: only "0" can start with zero
            if len(p) > 1 and p[0] == '0':               # constant ops
                return False

            # 3) numeric range 0..255
            val = int(p)                                  # O(len(p)) parse
            if val < 0 or val > 255:                      # constant ops
                return False

        return True

    # ------------------------------------------------------------
    # Method B: One-pass parse (no split)
    # ------------------------------------------------------------
    def isValid_one_pass(self, s: str) -> bool:
        """
        Time:  O(n) — single linear scan
        Space: O(1) — no allocations proportional to input size
        """
        n = len(s)
        groups = 0
        i = 0

        while i < n:
            # Each group must begin with a digit
            if not s[i].isdigit():
                return False

            # If it starts with '0', group must be exactly "0"
            if s[i] == '0':
                i += 1                                   # consumed "0"
            else:
                # Parse up to 3 digits; enforce <= 255
                num_len = 0
                val = 0
                while i < n and num_len < 3 and s[i].isdigit():
                    # Build the number incrementally (avoid int(...) of slice)
                    val = val * 10 + (ord(s[i]) - 48)    # constant ops
                    num_len += 1
                    i += 1
                # Must have consumed 1..3 digits and value in range
                if num_len == 0 or val > 255:
                    return False

            groups += 1
            if groups > 4:
                return False

            # After a group: expect a dot if not the last group
            if groups < 4:
                if i >= n or s[i] != '.':
                    return False
                i += 1                                    # skip '.'

        # Must form exactly 4 groups and consume all chars
        return groups == 4 and i == n


def _demo_and_time():
    sol = Solution()

    # -------------------------------
    # Demo inputs (covering edge cases)
    # -------------------------------
    tests = [
        "222.111.111.111",   # True
        "5555..555",         # False (wrong groups, empty middle)
        "0.0.0.255",         # True
        "192.168.001.001",   # False (leading zeros)
        "1.2.3.4",           # True
        "1.2.3",             # False (only 3 groups)
        ".1.2.3.4",          # False (leading dot)
        "1.2.3.4.",          # False (trailing dot)
        "256.0.0.1",         # False (>255)
        "01.2.3.4",          # False (leading zero)
        "0.0.0.0",           # True
        "123.045.067.089",   # False (leading zeros in groups)
        "10.20.30.40",       # True
        "abc.def.ghi.jkl",   # False (non-digits)
    ]

    print("== Demo: Split & Check ==")
    for s in tests:
        print(f"{s:>18}  ->  {sol.isValid(s)}")

    print("\n== Demo: One-pass Parser ==")
    for s in tests:
        print(f"{s:>18}  ->  {sol.isValid_one_pass(s)}")

    # --------------------------------
    # Timings for both implementations
    # --------------------------------
    # Note: We time across the whole batch of test strings to be realistic.
    def run_split():
        for s in tests:
            sol.isValid(s)

    def run_one_pass():
        for s in tests:
            sol.isValid_one_pass(s)

    # Warmup iteration counts
    iters = 2000

    t_split = timeit(run_split, number=iters)
    t_onep = timeit(run_one_pass, number=iters)

    print("\n== Timings (smaller is better) ==")
    print(f"Split & Check : {t_split:.6f} sec for {iters} iterations")
    print(f"One-pass      : {t_onep:.6f} sec for {iters} iterations")


if __name__ == "__main__":
    _demo_and_time()
```

### What this prints (expected)

```
== Demo: Split & Check ==
  222.111.111.111  ->  True
         5555..555  ->  False
          0.0.0.255 ->  True
  192.168.001.001  ->  False
            1.2.3.4 ->  True
              1.2.3 ->  False
          .1.2.3.4  ->  False
          1.2.3.4.  ->  False
          256.0.0.1 ->  False
           01.2.3.4 ->  False
            0.0.0.0 ->  True
 123.045.067.089   ->  False
         10.20.30.40 -> True
 abc.def.ghi.jkl   ->  False

== Demo: One-pass Parser ==
... (same True/False results as above) ...

== Timings (smaller is better) ==
Split & Check : X.XXXXXX sec for 2000 iterations
One-pass      : Y.YYYYYY sec for 2000 iterations
```

(The exact timing numbers will depend on your machine.)

---

## 6) Real-World Use Cases (a few important ones)

1. **Network configuration validation**
   Ensuring user-entered IPv4 addresses (e.g., static IPs, DNS servers, gateways) are structurally valid before applying network settings.

2. **Firewall / ACL rule parsing**
   Validating IPs in access-control lists or firewall rule files to prevent malformed entries that could break enforcement.

3. **Log ingestion & ETL pipelines**
   Cleaning and validating IP fields from web/app logs before indexing or aggregating, avoiding corrupt data downstream.

4. **Form validation in admin panels**
   Backend checks for monitoring systems, reverse proxies, or load balancers where operators input whitelists/blacklists of IPs.

5. **Security tooling**
   Sanitizing feeds of indicators of compromise (IOCs) to ensure all IPs conform to IPv4 syntax before correlation.
