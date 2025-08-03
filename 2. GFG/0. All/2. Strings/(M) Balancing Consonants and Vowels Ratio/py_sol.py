class Solution:
    def countBalanced(self, arr):
        # code here
        # Helper function to compute the net vowel-consonant score
        def net_score(s):
            vowels = set("aeiou")
            score = 0
            for ch in s:
                if ch in vowels:
                    score += 1
                else:
                    score -= 1
            return score

        n = len(arr)
        prefix = 0
        freq = defaultdict(int)  # To count prefix frequency
        freq[0] = 1  # Base case for prefix[0]
        count = 0

        for i in range(n):
            prefix += net_score(arr[i])
            count += freq[prefix]  # Count how many times this prefix seen
            freq[prefix] += 1

        return count
