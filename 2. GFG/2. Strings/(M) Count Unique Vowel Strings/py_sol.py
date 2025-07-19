from math import factorial
from collections import Counter
class Solution:
    def vowelCount(self, s):
        #code here
        # Step 1: Define vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 2: Count only vowels in the string
        count = Counter([ch for ch in s if ch in vowels])

        # Step 3: Extract unique vowel counts
        unique_vowels = list(count.keys())
        k = len(unique_vowels)  # Number of distinct vowels

        if k == 0:
            return 0  # No vowels, no permutations possible

        # Step 4: Number of permutations of unique vowels = k!
        perm = factorial(k)

        # Step 5: For each vowel, how many positions can we pick from?
        choices = 1
        for v in unique_vowels:
            choices *= count[v]  # pick 1 occurrence per vowel

        return perm * choices