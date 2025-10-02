"""
# Add two numbers:
a = 10
b = 20
add_num = a + b
print(add_num)

# Find Square Root: 8
num = float(input('Enter Number: '))
num_sqrt = num ** 0.5
print('Square root of 8 is %0.3f is %0.3f'%(num, num_sqrt))
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
# New way
import math
sqrt = math.sqrt(num)
print('The sqrt of %0.2f is %0.2f'%(num, sqrt))
"""
# Area of Triangle
"""
import math
a = 5
b = 6
c = 7

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))
sq_area = math.sqrt(area)
print('The area of triangle is %0.2f' %sq_area)
"""
"""
# swap two variables:
x = 5
y = 10

temp = x
x = y
y = temp

print(x)
print(y)
"""
# With out using variable
"""
x = 5
y = 10

x = x + y
#print(x)
y = x - y
#print(y)
x = x - y

print(x)
print(y)
"""
# Random number
"""
import random
print(random.randint(0,9))
"""
# KM to Miles
"""
kilm = 5.5
#kilm = input('Enter value :')
conv = 0.621371
miles = kilm * conv
print('%0.3f kilometers is equal to %0.3f miles' %(kilm,miles))
"""
# Celsius to Fahrenheit
"""
#cels = 37.5
cels = int(input('Enter value :'))
far = (cels * 1.8) + 32
print('%0.1f if degree of Celsius is equal to %0.1f Fahrenheit' %(cels,far))
"""
# check number +ve or -ve
"""
num = float(input("Enter a number :"))
if num > 0:
    print('Positive number')
elif num == 0:
    print("Zero")
else:
    print('Negative')
"""
# Print Even or Odd
"""
num = int(input("Enter number :"))
if(num % 2) == 0:
    print(f"{num} is 'Even")
else:
    print(f"{num} is 'Odd")
"""
# check leap year
"""
year = int(input("Enter Year :"))
if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
"""
# Largest among 3 numbers
num1 = 10
num2 = 14
num3 = 12
if(num1 >= num2) and (num1 >= num3):
    largest = num1
elif(num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
    print(f"The largest number between numbers is", largest)