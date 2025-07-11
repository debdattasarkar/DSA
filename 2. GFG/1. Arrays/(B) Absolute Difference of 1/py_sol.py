class Solution:
    
    def isAbsoluteDiff1(self, num):
        digits = list(map(int, str(num)))
        if len(digits) < 2:
            return False  # must have at least 2 digits

        for i in range(1, len(digits)):
            if abs(digits[i] - digits[i - 1]) != 1:
                return False
        return True
    
    def getDigitDiff1AndLessK(self, arr, k):
        # code here
        result = []
        for num in arr:
            if num < k and num >= 10 and self.isAbsoluteDiff1(num):
                result.append(num)
        return result