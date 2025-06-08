class Solution:
    def isSumString (self, s):
        # code here 
        # Helper to validate the recursive sum string from current first and second
        def isValid(first, second, rest):
            if not rest:
                return True
            sum_str = str(int(first) + int(second))
            if rest.startswith(sum_str):
                return isValid(second, sum_str, rest[len(sum_str):])
            return False

        n = len(s)
        for i in range(1, n):
            for j in range(i + 1, n):
                first = s[:i]
                second = s[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if isValid(first, second, s[j:]):
                    return True
        return False