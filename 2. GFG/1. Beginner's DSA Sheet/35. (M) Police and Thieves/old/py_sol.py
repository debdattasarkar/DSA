class Solution:
    def catchThieves(self, arr, k):
        #code  here
        n = len(arr)
        thieves = []
        police = []
        count = 0

        for i in range(n):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thieves.append(i)

        i = j = 0
        while i < len(thieves) and j < len(police):
            if abs(thieves[i] - police[j]) <= k:
                count += 1
                i += 1
                j += 1
            elif thieves[i] < police[j]:
                i += 1
            else:
                j += 1

        return count