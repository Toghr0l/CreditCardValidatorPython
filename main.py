# Initialize variables to store the sum of odd and even digits
sum_odd_digits = 0
sum_even_digits = 0
# Initialize variable to store the total sum
total = 0

# Prompt the user to enter a credit card number
card_number = input("Enter a credit card: ")
# Remove any dashes or spaces from the credit card number
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
# Reverse the order of the digits in the credit card number
card_number = card_number[::-1]

# Calculate the sum of the odd digits
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Calculate the sum of the even digits
for x in card_number[1::2]:
    # Double the value of each even digit
    x = int(x) * 2
    # If the result is greater than 10, add the individual digits together
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Calculate the total sum of the odd and even digits
total = sum_odd_digits + sum_even_digits

# Check if the total sum is divisible by 10
if total % 10 == 0:
    # If it is, print "Valid" to indicate that the credit card number is valid
    print("Valid")
else:
    # Otherwise, print "InValid" to indicate that the credit card number is not valid
    print("InValid")

# Wait for user input before exiting
input()