intro = "hello world"
print(intro)

first_name = input("What is your first name? ")
print(f"Hello {first_name}")

age = input("What is your age? ")
print(f"You are {age} years old.")

too_hot = "It's way too hot!"
too_cold = "I'm boutta be like the end scene of 'The Shining' out here"
temp = float(input("What is the current temp? "))

if temp <= -5:
    print(too_cold)
elif temp >= 95:
    print(too_hot)
else:
    print("Nice")

# Convert age to float
num1 = float(age)
num2 = float(temp)

# Sum
def addition(add1, add2):
    the_sum = add1 + add2
    print(the_sum)

addition(num1, num2)

# Subtract
def subtraction(sub1, sub2):
    the_diff = sub1 - sub2
    print(the_diff)

subtraction(num1, num2)

# Multiply
result_multiply = num1 * num2
print(result_multiply)

# Divide
result_divide = num1 / num2
print(result_divide)

# Exponentiation
result_power = num1 ** num2
print(result_power)

#part 2
def calculate_area(length, width):
    area = length * width
    return area

# Example usage:
length1 = 5
width1 = 10
area1 = calculate_area(length1, width1)
print(f"The area of the rectangle with length {length1} and width {width1} is: {area1}")

length2 = 7
width2 = 3
area2 = calculate_area(length2, width2)
print(f"The area of the rectangle with length {length2} and width {width2} is: {area2}")

#part 3
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#part 4
import math  # Import the math module for square root

# Create a list of 5 different numbers
numbers = [16, 25, 9, 36, 64]

# Use a for loop to print the square root of each number
print("Square Roots:")
for number in numbers:
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")

# Use a while loop to calculate and print the cubed value of each number
print("\nCubed Values:")
index = 0
while index < len(numbers):
    cubed_value = numbers[index] ** 3
    print(f"The cubed value of {numbers[index]} is {cubed_value}")
    index += 1
