def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer forward if it's on a non-alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer backward if it's on a non-alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        print(f"\tComparing '{s[left].lower()}' and '{s[right].lower()}'")  # Debugging output
        if s[left].lower() != s[right].lower():
            print("\tNot a palindrome!")
            return False

        # Move pointers inward
        left += 1
        right -= 1

    print("\tIt's a palindrome!")
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
        print("\tstring: ", i,"\n")
        result = is_palindrome(i)
        print("\n\tResult:", result)
        print("-"*100)

if __name__ == "__main__":
    main()