def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
    
def main():
    
    test_cases = [
        ("A man, a plan, a canal: Panama"),
        ("race a car"),
        ("1A@2!3 23!2@a1"),
        ("No 'x' in Nixon"),
        ("12321"),
    ]

    for i in test_cases:
        print("\tstring: ", i)
        result = is_palindrome(i)
        print("\n\tResult:", result)
        print("-"*100)

if __name__ == "__main__":
    main()