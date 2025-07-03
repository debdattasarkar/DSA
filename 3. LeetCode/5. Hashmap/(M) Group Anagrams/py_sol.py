class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # key: sorted string, value: list of anagrams

        for word in strs:
            sorted_key = ''.join(sorted(word))  # Sorting characters in word
            anagram_map[sorted_key].append(word)  # Append word under its sorted key
        
        return list(anagram_map.values())  # Return grouped anagrams