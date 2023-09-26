intro = ("hello world")
print(intro)

first_name = input(f"what is your first name? ")
print(f"hello {first_name}")

age = input(f"what is your age? ")
print(f"you are {age} years old.")

too_hot = (f"It's way too hot!")
too_cold = (f"Im boutta be like the end scene of 'The Shining' out here")
temp = float(input(f"what is the current temp? "))


if temp <= -5:
  print(too_cold)
elif temp >= 95:
  print(too_hot)
else:
  print(f"nice")

num1 = float(age)
num2 = float(temp)

print(age + temp)

def addition(add1, add2):
  the_sum = add1 + add2
  print(the_sum)

addition(age, temp)

def subtraction(sub1, sub2):
  the_diff = sub1 - sub2
  print(the_diff)

subtraction(age, temp)

num1 = float(age)
num2 = float(temp)

print(age * temp)

num1 = float(age)
num2 = float(temp)

print(age / temp)

num1 = float(age)
num2 = float(temp)

print(age ** temp)