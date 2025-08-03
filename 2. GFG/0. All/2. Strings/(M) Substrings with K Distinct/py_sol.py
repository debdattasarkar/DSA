class Solution:
    def countSubstr (self, s, k):
        # Code here
        # Helper function to count substrings with at most k distinct chars
        def atMostK(s, k):
            count = [0] * 26  # For lowercase a-z
            left = 0
            result = 0
            distinct = 0

            for right in range(len(s)):
                if count[ord(s[right]) - ord('a')] == 0:
                    distinct += 1
                count[ord(s[right]) - ord('a')] += 1

                # Shrink window if more than k distinct characters
                while distinct > k:
                    count[ord(s[left]) - ord('a')] -= 1
                    if count[ord(s[left]) - ord('a')] == 0:
                        distinct -= 1
                    left += 1

                # Add all substrings ending at right
                result += right - left + 1
            return result

        return atMostK(s, k) - atMostK(s, k - 1)