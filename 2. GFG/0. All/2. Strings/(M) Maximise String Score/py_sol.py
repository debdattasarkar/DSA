class Solution:
    def maxScore(self, s, jumps):
        """
        Optimized solution using per-character DP and streaming prefix data.

        Idea:
        - Let dp[i] be the best score when we land at index i.
        - For character c at index j, we can show:

            dp[j] = prefix_ascii(j) - count_c(j) * ASCII(c)
                    + best_for_target[c]

          where best_for_target[c] is:

            best_for_target[c] = max over earlier indices i that can jump to c of    
                                 dp[i] - prefix_ascii(i)
                                 + count_c(i) * ASCII(c)

        - While we scan the string left to right, we maintain:
            * ascii_sum: sum ASCII of characters before current index
            * count_char[26]: frequency of each letter before current index
            * best_for_target[26]: value above for each letter as target

        - For each index i:
            1. Compute dp[i] from best_for_target[ s[i] ].
            2. Use dp[i] to update best_for_target for all characters that
               can be jumped TO from s[i].
            3. Update ascii_sum and count_char with s[i].

        Complexity:
            Let B = 26 (letters)

            - For each of n indices:
                * O(1) work to compute dp[i]
                * O(#allowed_targets) ≤ O(26) work to update best_for_target
            => O(B * n) time  (≈ O(n)).
            - Space: O(B) for best_for_target + O(B) for counts + O(n) for dp.
              So O(B + n) auxiliary space.
        """

        n = len(s)
        if n == 0:
            return 0

        # Helper to map 'a'..'z' -> 0..25
        def char_index(ch):
            return ord(ch) - ord('a')

        # ---------- Build allowed target list for each source character ----------
        # Start with self-jumps: char -> same char
        allowed_targets_from = [[] for _ in range(26)]
        for c in range(26):
            allowed_targets_from[c].append(c)

        # Add directed jumps from input list
        for c1, c2 in jumps:
            i1 = char_index(c1)
            i2 = char_index(c2)
            allowed_targets_from[i1].append(i2)

        # ---------- DP and helpers ----------
        NEG_INF = -10**18

        # best_for_target[c]: the "bracket" term for character c as target
        best_for_target = [NEG_INF] * 26

        # prefix info (before current index)
        ascii_sum = 0                     # sum of ASCII of s[0..i-1]
        count_char = [0] * 26             # count_char[c] = # of c in s[0..i-1]

        # dp[i]: best score when landing at index i
        dp = [NEG_INF] * n

        # ---------- Handle index 0 specially ----------
        dp[0] = 0  # we start at index 0 with score 0

        idx0 = char_index(s[0])

        # index 0 can be a start of jumps to all its allowed targets
        for tgt in allowed_targets_from[idx0]:
            # Here ascii_sum = 0, count_char[*] = 0
            cand = dp[0] - ascii_sum + count_char[tgt] * ord(chr(tgt + ord('a')))
            if cand > best_for_target[tgt]:
                best_for_target[tgt] = cand

        # Update prefix after index 0
        ascii_sum += ord(s[0])
        count_char[idx0] += 1

        # ---------- Process remaining indices 1..n-1 ----------
        for i in range(1, n):
            current_char = s[i]
            c_idx = char_index(current_char)
            ascii_c = ord(current_char)

            # Step 1: compute dp[i] if there is any valid way to land here
            if best_for_target[c_idx] != NEG_INF:
                dp[i] = (
                    ascii_sum
                    - count_char[c_idx] * ascii_c
                    + best_for_target[c_idx]
                )
                # otherwise stays NEG_INF (unreachable)

            # Step 2: use dp[i] to update future best_for_target values
            if dp[i] != NEG_INF:
                for tgt in allowed_targets_from[c_idx]:
                    target_char_ascii = ord(chr(tgt + ord('a')))
                    cand = (
                        dp[i]
                        - ascii_sum
                        + count_char[tgt] * target_char_ascii
                    )
                    if cand > best_for_target[tgt]:
                        best_for_target[tgt] = cand

            # Step 3: update prefix information for next iteration
            ascii_sum += ascii_c
            count_char[c_idx] += 1

        # We can always choose to make no jumps, so answer is at least 0
        best_score = max(0, max(dp))
        return best_score