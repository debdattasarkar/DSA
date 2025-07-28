class Solution:
    def asciirange(self, s):
        # code here
        # Store first and last occurrence of each character
        first = [-1] * 26
        last = [-1] * 26
        n = len(s)
        
        # Fill in first and last occurrence
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        result = []

        # For each character, calculate the ASCII sum between its first and last index
        for i in range(26):
            if first[i] != -1 and last[i] > first[i] + 1:
                total = 0
                for j in range(first[i] + 1, last[i]):
                    total += ord(s[j])
                if total > 0:
                    result.append(total)
        
        return result