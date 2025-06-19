class Solution:
    def caseSort(self,s):
        #code here
        # Separate characters based on case
        upper = sorted([ch for ch in s if ch.isupper()])
        lower = sorted([ch for ch in s if ch.islower()])

        # Pointers for each list
        ui, li = 0, 0
        result = []

        for ch in s:
            if ch.isupper():
                result.append(upper[ui])
                ui += 1
            else:
                result.append(lower[li])
                li += 1

        return ''.join(result)
