I couldn’t reliably find a canonical “top 25” list of **HackerRank string problems asked by Microsoft**. But I can do two useful things:

1. **Gather** several (≈ 10–20) string or string-adjacent problems that have been *reported* in Microsoft / Hackerrank / interviews.
2. **Suggest a study list of ~25 string problems** (from HackerRank + general interview prep) that are good preparation for Microsoft or high-difficulty rounds.

---

## 1. Reported / anecdotal string problems from Microsoft / HackerRank interviews

Here are some string or string-pattern problems that candidates have reported encountering (or which are plausible in those settings):

| Problem / Description                                                                                          | Comments / source                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Circular Character Roll Operation                                                                              | One interviewee said: “for each element in array roll, cyclically increment the first roll[i] characters of the string (wrapping ‘z’ → ‘a’).” ([linkjob.ai][1])               |
| Decompress / Expand encoded string (e.g. `"a2[bc]" → "abcbc"`)                                                 | A candidate said this was asked in a Microsoft interview. ([Medium][2])                                                                                                       |
| Given a string and queries (l, r, k), find the k-th smallest (lexicographically) character in substring [l..r] | Also from the same interview report. ([Medium][2])                                                                                                                            |
| String Conversion — Lexicographically Maximum Possible                                                         | A HackerRank interview string problem: reorder string `s` to maximize a constructed string `b` by repeated “append + reverse” operations. ([Medium][3])                       |
| Regular expression substring matching with `^` and `$` markers                                                 | In a reported Microsoft Hackerrank test, problem: “given pattern string and test string, implement regex substring matching” with `^` and `$` anchoring. ([GeeksforGeeks][4]) |

These are more “stories” / examples; they help highlight the flavor of string problems Microsoft might use.

---

## 2. Suggested list: 25 string problems to practice (HackerRank + general)

Below is a sample list of string / string-algorithm problems you should practice. Many are from HackerRank (Interview Preparation Kit) or classic interview sets. This will prepare you for Microsoft / any high-tier coding round.

Each problem is good to know (increasing in difficulty). I also group by theme to help you focus.

| Theme / Type                        | Problem Name / Description                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Basic / Frequency / Counting        | 1. **Making Anagrams** (how many deletions to make two strings anagrams) — HackerRank ([HackerRank][5])                   |
|                                     | 2. **Alternating Characters** — remove minimal chars so no two identical adjacent characters ([HackerRank][5])            |
|                                     | 3. **Sherlock and the Valid String** (check if string can be “valid” by removing one char) — HackerRank ([HackerRank][5]) |
|                                     | 4. **Common Child** (longest common subsequence variant) — HackerRank ([HackerRank][5])                                   |
| Two-pointer / Sliding Window        | 5. Longest substring without repeating characters                                                                         |
|                                     | 6. Longest substring with at most K distinct characters                                                                   |
|                                     | 7. Longest palindromic substring                                                                                          |
|                                     | 8. Minimum window substring (smallest window in s containing all chars of t)                                              |
| String transformations / operations | 9. String Compression / Run Length Encoding                                                                               |
|                                     | 10. String rotation / check if one string is rotation of another                                                          |
|                                     | 11. Reverse words in a string                                                                                             |
|                                     | 12. Left rotation / right rotation by k positions                                                                         |
|                                     | 13. Shift / Caesar cipher / rotate characters                                                                             |
| Pattern matching / search           | 14. Implement strstr / indexOf                                                                                            |
|                                     | 15. KMP algorithm / pattern matching                                                                                      |
|                                     | 16. Regex matching (with `.` and `*`, or anchors `^`, `$`)                                                                |
|                                     | 17. Wildcard matching (`?` and `*`)                                                                                       |
| Encodings / bracket / stack         | 18. Decode string (e.g. “a2[bc]” → “abcbc”)                                                                               |
|                                     | 19. Valid parentheses / bracket matching                                                                                  |
|                                     | 20. Evaluate expression with parentheses / operators in a string                                                          |
|                                     | 21. Infix to postfix / prefix conversion / evaluate                                                                       |
| Advanced / Miscellaneous            | 22. Edit distance (Levenshtein distance)                                                                                  |
|                                     | 23. Longest common substring / subsequence between two strings                                                            |
|                                     | 24. String number addition / large integer addition in string                                                             |
|                                     | 25. Lexicographically maximum string via transformations (e.g. the “String Conversion” problem above)                     |

If you master these 25 (and their variations), you’ll be well-prepared for most string problems in Microsoft interviews or in HackerRank coding rounds.

---

If you like, I can curate **actual HackerRank links** (with problem statements & solutions) for all 25, or filter down to **top 10 Microsoft-asked ones**. Do you want me to send you that?

[1]: https://www.linkjob.ai/interview-questions/microsoft-hackerrank-test/ "How I Passed 2025 Microsoft HackerRank Test on My First Try"
[2]: https://medium.com/%40shubhamanand_36797/microsoft-interview-experience-9d7cc5e7ac6e "Microsoft Interview Experience - Medium"
[3]: https://takeitoutamber.medium.com/hackerrank-coding-interview-string-conversion-lexicographically-maximum-possible-90756b82c184 "String Conversion — Lexicographically Maximum Possible"
[4]: https://www.geeksforgeeks.org/interview-experiences/microsoft-interview-experience-set-102-on-campus-for-idc/ "Microsoft Interview experience | Set 102 (On Campus for IDC)"
[5]: https://www.hackerrank.com/interview/interview-preparation-kit/strings/challenges "String Manipulation Interview Questions"
