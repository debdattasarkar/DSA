class Solution:
    def substrCount(self, s, k):
        # code here
        from collections import defaultdict

        n = len(s)
        if k > n:
            return 0

        char_count = defaultdict(int)
        distinct = 0
        result = 0

        # Initialize the first window
        for i in range(k):
            if char_count[s[i]] == 0:
                distinct += 1
            char_count[s[i]] += 1

        if distinct == k - 1:
            result += 1

        # Slide the window
        for i in range(k, n):
            left_char = s[i - k]
            right_char = s[i]

            # Remove leftmost character
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                distinct -= 1

            # Add rightmost character
            if char_count[right_char] == 0:
                distinct += 1
            char_count[right_char] += 1

            if distinct == k - 1:
                result += 1

        return result