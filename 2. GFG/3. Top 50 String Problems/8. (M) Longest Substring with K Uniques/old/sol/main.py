class Solution:
    def longestKSubstr(self, s, k):
        from collections import defaultdict

        n = len(s)
        left = 0               # Left pointer of the sliding window
        max_len = -1           # To track the length of the longest valid substring
        char_freq = defaultdict(int)  # Stores frequency of characters in the window

        for right in range(n):
            # Expand window by adding the right character
            char_freq[s[right]] += 1  # Time: O(1)

            # If we have more than k distinct characters, shrink from the left
            while len(char_freq) > k:
                char_freq[s[left]] -= 1  # Shrink from the left
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]  # Remove character if its count is 0
                left += 1  # Move left pointer forward

            # If the window has exactly k distinct characters, update max_len
            if len(char_freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1 = "aabacbebebe"
    k1 = 3
    print("Input:", s1, "| k =", k1)
    print("Output:", sol.longestKSubstr(s1, k1))  # Expected: 7 ("cbebebe")

    # Test Case 2
    s2 = "aaaa"
    k2 = 2
    print("\nInput:", s2, "| k =", k2)
    print("Output:", sol.longestKSubstr(s2, k2))  # Expected: -1

    # Test Case 3
    s3 = "abcbaa"
    k3 = 2
    print("\nInput:", s3, "| k =", k3)
    print("Output:", sol.longestKSubstr(s3, k3))  # Expected: 4 ("bcba")