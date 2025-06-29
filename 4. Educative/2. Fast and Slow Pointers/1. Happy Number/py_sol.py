def is_happy_number(n):

    # Helper function that calculates the sum of squared digits.
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        print("\t\tSum of squared digits: ", total_sum)
        return total_sum

    slow_pointer = n  # The slow pointer value
    print("\tSetting slow pointer = input number", slow_pointer)
    print("\tSetting fast pointer = sum of squared digits of ", n, sep="")
    fast_pointer = sum_of_squared_digits(n)  # The fast pointer value
    print("\tFast pointer:", fast_pointer)
    while fast_pointer != 1 and slow_pointer != fast_pointer:  # Terminating condition
        print("\n\tRepeatedly updating slow and fast pointers\n")
        # Incrementing the slow pointer by 1 iteration
        slow_pointer = sum_of_squared_digits(slow_pointer)
        print("\t\tThe updated slow pointer is", slow_pointer, "\n")
        # Incrementing the fast pointer by 2 iterations
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))
        print("\t\tThe updated fast pointer is ", fast_pointer, "\n")
    # If 1 is found then it returns True, otherwise False
    if(fast_pointer == 1):
        print("\tSince fast pointer has converged to 1, the input number is a happy number.\n")
        return True
    print("\tFast pointer has not converged to 1, the input number is not happy number.\n")
    return False


def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i+1, ".\tInput Number: ", inputs[i], sep="")
        print("\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
