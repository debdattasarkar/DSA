# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    """
    Check each number's string representation equals its reverse.
    Time  : O(n * d) where d is average digit count (<= 6 given constraints)
    Space : O(1) extra (ignoring small temporary strings per number)
    Short-circuits on first non-palindrome.
    """
    for num in arr:
        s = str(num)           # O(d)
        if s != s[::-1]:       # O(d)
            return False
    return True