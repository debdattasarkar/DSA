#User function Template for python3

from collections import defaultdict
class Solution:
    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        '''
        Group words that are anagrams.
        Maintain order of appearance inside each group by appending as we scan.
        Time  : O(n * m log m)  (n words, each sorted)
        Space : O(n * m)        (to store groups/keys)
        '''
        buckets = defaultdict(list)  # key -> list of words (order preserved)
        for w in arr:                # O(n)
            key = ''.join(sorted(w)) # O(m log m)
            buckets[key].append(w)   # O(1) amortized
        # Driver may sort outer list; inner lists already in input order
        return list(buckets.values())
