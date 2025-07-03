
---

## ✅ Full Python Program with Inline Comments

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings are isomorphic.
        A character in string s must map uniquely to a character in t and vice versa.

        Time Complexity: O(n)
        Space Complexity: O(1)  (since mappings are limited to 256 ASCII characters)
        """

        # Dictionary to store mapping from characters in s to characters in t
        map_s_t = {}  # e.g., {'a': 'x'}
        # Dictionary to store reverse mapping from t to s
        map_t_s = {}  # e.g., {'x': 'a'}

        # Iterate over both strings in parallel
        for cs, ct in zip(s, t):  # O(n) where n = len(s)

            # If cs is already mapped, ensure it maps to ct
            if cs in map_s_t:
                if map_s_t[cs] != ct:
                    return False  # Mismatch in mapping

            # If not already mapped, add mapping cs → ct
            else:
                map_s_t[cs] = ct

            # Similarly, check reverse mapping for ct → cs
            if ct in map_t_s:
                if map_t_s[ct] != cs:
                    return False  # Mismatch in reverse mapping
            else:
                map_t_s[ct] = cs

        return True  # All mappings are consistent
```

---

## 🧠 Time & Space Complexity (Step-by-Step)

| Step                           | Time      | Space      | Explanation                                        |
| ------------------------------ | --------- | ---------- | -------------------------------------------------- |
| `zip(s, t)` iteration          | O(n)      | -          | Loop through both strings once                     |
| Dictionary lookups and inserts | O(1) each | O(1) total | Up to 256 unique ASCII characters → constant space |
| Overall                        | **O(n)**  | **O(1)**   | n = length of string                               |

---

## 🧪 Sample Inputs and Outputs

### 🔹 Example 1

```python
s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t))  # Output: True
```

Explanation:

* 'e' → 'a'
* 'g' → 'd'

---

### 🔹 Example 2

```python
s = "foo"
t = "bar"
print(Solution().isIsomorphic(s, t))  # Output: False
```

Explanation:

* 'o' is mapped to both 'a' and 'r' → invalid mapping.

---

### 🔹 Example 3

```python
s = "paper"
t = "title"
print(Solution().isIsomorphic(s, t))  # Output: True
```

Explanation:

* p → t
* a → i
* e → l
* r → e

---

## ✅ Summary

* **Core idea:** Use two hash maps (forward + reverse) to ensure bijective mapping.
* **Why both maps?** Prevent multiple keys mapping to the same value (injectivity check).
* **Efficient:** Single pass, constant space, works even with large strings (up to 50,000 chars).
