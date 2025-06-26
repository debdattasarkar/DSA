def reverse_words(sentence):
    # Remove leading and trailing spaces
    sentence = sentence.strip()
    
    # Split the sentence into words using whitespace as delimiter
    result = sentence.split()
    
    # Initialize two pointers for reversing the words in-place
    left, right = 0, len(result) - 1

    # Reverse the words by swapping elements using two pointers
    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    # Join the words back into a single string with a space separator
    return " ".join(result)


def main():
    string_to_reverse = ["Hello World",
                        "a   string   with   multiple   spaces",
                        "Case Sensitive Test Case 1234",
                        "a 1 b 2 c 3 d 4 e 5",
                        "     trailing spaces",
                        "case test interesting an is this"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\tOriginal string: '" + "".join(string_to_reverse[i]), "'", sep='')
        result = reverse_words(string_to_reverse[i])

        print("\tReversed string: '" + "".join(result), "'", sep='')
        print("-" * 100)


if __name__ == '__main__':
    main()