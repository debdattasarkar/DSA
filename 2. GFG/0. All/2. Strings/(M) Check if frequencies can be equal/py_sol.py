from collections import Counter
class Solution:
    def sameFreq(self, s: str) -> bool:
        #code here
        # Step 1: Count frequency of each character
        freq = Counter(s)
        
        # Step 2: Count frequencies of these frequencies
        freq_count = Counter(freq.values())
        
        # If all frequencies are same
        if len(freq_count) == 1:
            return True
        
        # If there are exactly 2 different frequencies
        if len(freq_count) == 2:
            keys = list(freq_count.keys())
            f1, f2 = keys[0], keys[1]
            
            # Check if one of them occurs once and is either 1 or one more than the other
            if (freq_count[f1] == 1 and (f1 - 1 == f2 or f1 == 1)):
                return True
            if (freq_count[f2] == 1 and (f2 - 1 == f1 or f2 == 1)):
                return True
        
        return False
