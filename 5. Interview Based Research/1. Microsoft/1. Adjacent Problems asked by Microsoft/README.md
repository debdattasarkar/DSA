Awesome — here are **direct practice links** for the ~15 Microsoft-style string problems we picked. I’ve mapped each item to a canonical HackerRank/LeetCode problem (closest equivalent where the exact prompt isn’t public).

1. Circular “roll the prefix” operation → **Shifting Letters (LC 848)**. ([LeetCode][1])
2. Decode nested repetition → **Decode String (LC 394)**. ([LeetCode][2])
3. “k-th char in substring” style → closest canonical: **Decoded String at Index (LC 880)** (practice kth-character logic). ([LeetCode][3])
4. Make string lexicographically larger via ops → **Bigger is Greater (HR)**. ([HackerRank][4])
5. Valid string after removing ≤1 char → **Sherlock and the Valid String (HR)**. ([HackerRank][5])
6. Convert A→B by deleting/capitalizing → **Abbreviation (HR)**. ([HackerRank][6])
7. Run-length compression → **String Compression (LC 443)** (or HR variant below). ([LeetCode][7])
8. Balanced parentheses/brackets → **Balanced Brackets (HR)**. ([HackerRank][8])
9. Minimum window covering all chars → **Minimum Window Substring (LC 76)**. ([LeetCode][9])
10. Longest palindromic substring → **Longest Palindromic Substring (LC 5)**. ([LeetCode][10])
11. Rotate string by left/right steps → **Perform String Shifts (LC 1427)**. ([LeetCode][11])
12. Check if one string is a rotation of another → **Rotate String (LC 796)**. ([LeetCode][12])
13. One-to-one char mapping → **Isomorphic Strings (LC 205)**. ([LeetCode][13])
14. Are two strings anagrams? → **Valid Anagram (LC 242)**. ([LeetCode][14])
15. Min deletions to make strings equal → **Delete Operation for Two Strings (LC 583)**. ([LeetCode][15])
    Bonus HR picks you’ll likely see: **Making Anagrams**, **Alternating Characters**, **Common Child**, **(HR) String Compression/Compress the String!**. ([HackerRank][16])

[1]: https://leetcode.com/problems/shifting-letters/ "Shifting Letters"
[2]: https://leetcode.com/problems/decode-string/ "Decode String"
[3]: https://leetcode.com/problems/decoded-string-at-index/ "Decoded String at Index"
[4]: https://www.hackerrank.com/challenges/bigger-is-greater/problem "Bigger is Greater"
[5]: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem "Sherlock and the Valid String"
[6]: https://www.hackerrank.com/challenges/abbr/problem "Abbreviation"
[7]: https://leetcode.com/problems/string-compression/ "String Compression"
[8]: https://www.hackerrank.com/challenges/balanced-brackets/problem "Balanced Brackets"
[9]: https://leetcode.com/problems/minimum-window-substring/ "Minimum Window Substring"
[10]: https://leetcode.com/problems/longest-palindromic-substring/ "Longest Palindromic Substring"
[11]: https://leetcode.com/problems/perform-string-shifts/ "Perform String Shifts"
[12]: https://leetcode.com/problems/rotate-string/ "Rotate String"
[13]: https://leetcode.com/problems/isomorphic-strings/ "Isomorphic Strings"
[14]: https://leetcode.com/problems/valid-anagram/ "Valid Anagram"
[15]: https://leetcode.com/problems/delete-operation-for-two-strings/ "583. Delete Operation for Two Strings"
[16]: https://www.hackerrank.com/challenges/making-anagrams/problem "Making Anagrams - HackerRank"

---

---

Here’s the full mapping so you can practice both on **HackerRank/LeetCode** *and* on **GFG**.

---

### 🔁 GFG Equivalents for Microsoft-Style String Problems

| #      | Problem                                                        | GFG Equivalent / Closest Title                                                      | GFG Link                                                                                                                                            |
| ------ | -------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1️⃣    | **Circular “roll the prefix”** (`Shifting Letters`)            | **Shift all characters by K positions** *(variant)*                                 | [GFG: Shift all characters by K positions](https://www.geeksforgeeks.org/shift-all-characters-by-k-positions-in-the-alphabet/)                      |
| 2️⃣    | **Decode String (nested repetition)**                          | **Decode the string (Recursively decode nested patterns)**                          | [GFG: Decode a string recursively](https://www.geeksforgeeks.org/decode-a-string-recursively-encoded-string/)                                       |
| 3️⃣    | **K-th char in substring** (`Decoded String at Index`)         | **Find K-th character in decrypted string**                                         | [GFG: Find K-th character in decrypted string](https://www.geeksforgeeks.org/find-k-th-character-in-decrypted-string/)                              |
| 4️⃣    | **Lexicographically next/larger string** (`Bigger is Greater`) | **Next Greater Lexicographic String**                                               | [GFG: Lexicographically next string](https://www.geeksforgeeks.org/lexicographically-next-string/)                                                  |
| 5️⃣    | **Valid String (Sherlock)**                                    | **Check if frequency of all characters can become same**                            | [GFG: Valid string problem](https://www.geeksforgeeks.org/check-if-frequency-of-all-characters-can-become-same-by-one-removal/)                     |
| 6️⃣    | **Abbreviation (convert A→B)**                                 | **Abbreviation using capital letters (DP)**                                         | [GFG: Abbreviation problem](https://www.geeksforgeeks.org/abbreviation-using-dynamic-programming/)                                                  |
| 7️⃣    | **String Compression**                                         | **Run Length Encoding**                                                             | [GFG: Run Length Encoding](https://www.geeksforgeeks.org/run-length-encoding/)                                                                      |
| 8️⃣    | **Balanced Brackets**                                          | **Balanced Parentheses / Bracket Matching**                                         | [GFG: Balanced Parentheses](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/)                                         |
| 9️⃣    | **Minimum Window Substring**                                   | **Smallest window containing all characters of another string**                     | [GFG: Minimum Window Substring](https://www.geeksforgeeks.org/smallest-window-in-a-string-containing-all-the-characters-of-another-string/)         |
| 🔟     | **Longest Palindromic Substring**                              | **Longest Palindromic Substring (DP or expand-center)**                             | [GFG: Longest Palindromic Substring](https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/)                                             |
| 1️⃣1️⃣ | **Rotate String by K**                                         | **Left and Right Rotate a String by K**                                             | [GFG: Rotate a String](https://www.geeksforgeeks.org/left-rotation-and-right-rotation-of-a-string/)                                                 |
| 1️⃣2️⃣ | **Check if One String is Rotation of Another**                 | **Check if strings are rotations of each other**                                    | [GFG: Rotation Check](https://www.geeksforgeeks.org/check-if-a-string-is-rotation-of-another-string/)                                               |
| 1️⃣3️⃣ | **Isomorphic Strings**                                         | **Check if two strings are isomorphic**                                             | [GFG: Isomorphic Strings](https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/)                                   |
| 1️⃣4️⃣ | **Valid Anagram**                                              | **Anagram Check**                                                                   | [GFG: Check if two strings are anagram of each other](https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/)           |
| 1️⃣5️⃣ | **Delete Operation for Two Strings**                           | **Minimum number of deletions and insertions to transform one string into another** | [GFG: Min deletions/insertions to convert strings](https://www.geeksforgeeks.org/minimum-number-deletions-insertions-transform-one-string-another/) |

---

### ✅ Bonus HackerRank → GFG Mappings

| HackerRank Problem             | GFG Equivalent                                                                                                                          |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Making Anagrams**            | [Minimum deletions to make two strings anagram](https://www.geeksforgeeks.org/minimum-number-of-deletions-to-make-two-strings-anagram/) |
| **Alternating Characters**     | [Remove adjacent duplicates in string](https://www.geeksforgeeks.org/remove-consecutive-duplicates-string/)                             |
| **Common Child (LCS variant)** | [Longest Common Subsequence](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/)                                            |
| **Compress the String!**       | [Run Length Encoding](https://www.geeksforgeeks.org/run-length-encoding/)                                                               |

---