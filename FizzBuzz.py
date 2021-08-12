# Task : Print the Fizz Buzz numbers.

# Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz",
# print the rest of the numbers unchanged.
# Output each value on a separate line.

1.Solution

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:  
        print(i)
        
2.Solution

def fizzBuzz(s):
    if s % 3 == 0 and s % 5 == 0:
        print("FizzBuzz")
    elif s % 3 == 0:
        print("Fizz")
    elif s % 5 == 0:
        print("Buzz")
    elif s % 3 == 0 and s % 5 == 0:
        print("FizzBuzz")
    else:
        print(s)
for i in range(1, 101):
    fizzBuzz(i)
