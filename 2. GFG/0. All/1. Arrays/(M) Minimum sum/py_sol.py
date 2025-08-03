import sys
sys.set_int_max_str_digits(int(1e9))
class Solution:
    def minSum(self, arr):
        # code here
        # Step 1: Sort the digits to build smallest numbers
        arr.sort()
        num1, num2 = "", ""
        
        # Step 2: Distribute digits alternately
        for i, digit in enumerate(arr):
            if i % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)
                
        if num2=="":
                return num1
            
        # Step 3: Convert strings to integers and return the sum as string
        return str(int(num1) + int(num2))
