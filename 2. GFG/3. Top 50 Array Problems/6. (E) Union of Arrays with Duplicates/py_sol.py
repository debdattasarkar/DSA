class Solution:    
    def findUnion(self, a, b):
        # If inputs aren’t guaranteed sorted, sort copies:
        a = sorted(a)
        b = sorted(b)

        i = j = 0
        res = []
        last = None  # last value we appended

        # Merge step with de-duplication
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                x = a[i]; i += 1
            elif b[j] < a[i]:
                x = b[j]; j += 1
            else:
                x = a[i]; i += 1; j += 1
            if x != last:
                res.append(x); last = x

        while i < len(a):
            if a[i] != last:
                res.append(a[i]); last = a[i]
            i += 1

        while j < len(b):
            if b[j] != last:
                res.append(b[j]); last = b[j]
            j += 1

        return res