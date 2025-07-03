from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where the key is the sorted version of the string,
        # and the value is a list of all anagrams with that sorted signature.
        anagram_map = defaultdict(list)  # O(1) space per key/value init

        for word in strs:
            # Step 1: Sort the characters in the word to form the key
            sorted_key = ''.join(sorted(word))  # O(K log K), K = len(word)

            # Step 2: Append the word to its anagram group in the hashmap
            anagram_map[sorted_key].append(word)  # O(1) per append

        # Step 3: Return the grouped anagrams as a list of lists
        return list(anagram_map.values())  # O(N) to gather all groups
    
# Input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Execution
sol = Solution()
output = sol.groupAnagrams(strs)

# Output (Order may vary)
print(output)
# Possible Output:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]