# This program checks if a two-digit number is happy or sad. A happy number is a number that
# reaches '1' when replaced by the sum of the square of each number repeatedly. A sad number is a
# number that will never reach '1'.

# Asks for user's input and validates it to a two-digit number.
i = input("Choose any two digit number: ")
if len(i) != 2:
    print("Please enter a two digit number.")

else:
    # Splits input into separate digits.
    i = int(i)
    digit_one = int(str(i)[0])
    digit_two = int(str(i)[1])
    digit_three = 0
    # Creates a list which will later search for endless loops (sad numbers).
    numbers = [i, ]
    # Calculates the sum of squared digits.
    while True:
        digit_one_sq = digit_one * digit_one
        digit_two_sq = digit_two * digit_two
        digit_three_sq = digit_three * digit_three
        result = digit_one_sq + digit_two_sq + digit_three_sq
        # Checks if number is happy.
        if result == 1:
            print("This number is happy.")
            numbers.append(result)
            print(numbers)
            break
        # Checks if number is sad.
        elif result in numbers:
            print("This number is sad.")
            numbers.append(result)
            print(numbers)
            break
        # Continues if happiness or sadness is not yet proven.
        else:
            numbers.append(result)
            # Replaces original digits with digits of new result.
            result_str = str(result)
            # For one digit results:
            if result < 10:
                digit_one = result
                digit_two = 0
                digit_three = 0
            # For three digit results:
            elif len(result_str) == 3:
                digit_one = int(str(result)[0])
                digit_two = int(str(result)[1])
                digit_three = int(str(result)[2])
            # For two digit results:
            else:
                digit_one = int(str(result)[0])
                digit_two = int(str(result)[1])
                digit_three = 0






