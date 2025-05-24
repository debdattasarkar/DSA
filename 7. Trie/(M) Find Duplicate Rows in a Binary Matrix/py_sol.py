#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        seen = set()
        result = []
        
        for i in range(m):
            row_tuple = tuple(arr[i])
            if row_tuple in seen:
                result.append(i)
            else:
                seen.add(row_tuple)
        
        return result