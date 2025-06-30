#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        # Traverse from right to left
        for ch in reversed(s):
            val = roman[ch]
            if val < prev:
                total -= val  # Subtract if smaller than next numeral
            else:
                total += val  # Add otherwise
            prev = val

        return total