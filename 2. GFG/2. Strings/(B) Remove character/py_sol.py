#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        # Convert str2 into a set for O(1) lookups
        to_remove = set(str2)
        
        # Build result string by filtering out chars
        result = [ch for ch in str1 if ch not in to_remove]
        
        return ''.join(result)