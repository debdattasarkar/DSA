#User function template for Python 3

class Solution:
    def convertToRoman(self, n):
        #Code here
        # List of Roman numeral mappings in descending order
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman = ""
        i = 0
        
        # Loop until the number becomes 0
        while n > 0:
            # Subtract value[i] as many times as it fits
            while n >= val[i]:
                roman += sym[i]
                n -= val[i]
            i += 1
        
        return roman
    
if __name__ == "__main__":
    n = int(input())
    ob = Solution()
    print(ob.convertToRoman(n))