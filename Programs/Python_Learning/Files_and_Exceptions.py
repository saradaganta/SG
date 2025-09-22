# Reading the file:
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/pi_digits.txt/')
contents = path.read_text()
contents = contents.rstrip() # To remove extra blank line at last in text file.
print(contents)
"""
# print using for loop line by line.
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/pi_digits.txt/')
contents = path.read_text().rstrip()

lines = contents.splitlines()
for line in lines:
    if '.' in line:
        print("*",line)
    else:
        print(line)
"""
# print lenght of lines
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/pi_digits.txt/')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
"""

  # print lenght of lines  without front spaces for two lines
"""
from pathlib import Path
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/pi_digits.txt/')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
"""
# Reading 1 Million digits file with limit of 45...
"""
from pathlib import Path
import PyPDF2
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/Million_digits.txt')
content = path.read_text()

lines = content.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:45]}...")
print(len(pi_string))
"""
# find some ones birthday appears in file.
"""
from pathlib import Path
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/Million_digits.txt')
content = path.read_text()

lines = content.splitlines()
pi_stirng = ''
for line in lines:
    pi_stirng += line.strip()

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_stirng:
    print(birthday)
    print('Your birthday appears in the first million digits of pi.')
else:
    print('Your birthday not appear in the first million digits of pi.')
"""
print("********** Exercise 10.1/10.2/10.3 ***********")

# Priniting content by reeading entire file:
"""
from pathlib import Path
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/learn_python.txt')
text = path.read_text()
print(text)

# Priniting content by storing in the list and loop:
print("printing content by looping")
content = text.replace('Python', 'Tython')
#lines = content.splitlines()
pi_string = ''

for line in content.splitlines():
    pi_string += line
print(pi_string)
print(len(pi_string))

# Writing result to target folder
output_path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/like_to_learn_python.txt')
output_path.write_text(pi_string)
"""
# write multiple lines to file.
"""
from pathlib import Path

content = "I love programming. \n"
content += "I am learning programming. \n"
content += "I will become master in programming. \n"

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/writing_multiple_lines.txt')
path.write_text(content)
"""

print("***** Exercise 10.4 ******")
# Guest
"""
from pathlib import Path

content = input("Please Enter the Guest Name: ")
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/writing_guests.txt')
path.write_text(content)
"""
print("***** Exercise 10.4 ******")
# Guest list
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/enter_names.txt')
names = []

while True:
    name = input("Enter Guest Name :")
    if name.lower() == "quit":
        break
    names.append(name)
    print(f"Hello {name}, you have been added to guest book.")

path.write_text("\n".join(names))
print(f"\nGuest book saved to {path.resolve()}")
"""
# Countries list
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/countries_list.txt')
names = []

while True:
    name = input("Enter country Name :")
    if name.lower() == "quit":
        break
    names.append(name)
    print(f"Hello {name}, you have been added to guest book.")

path.write_text("\n".join(names))
print(f"\nGuest book saved to {path.resolve()}")
"""
######## Exceptions #########
# Handling zero division error exception:
# Division calculator.
#print(5/0)

# use try-except Blocks.
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# use exceptions to prevent crashes:
#division_calc.
print("Give me two numbers and i will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Enter First Number : ")
    if first_number == 'q':
        break
    second_number = input("Enter Second Number : ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0 ...!")
    else:
        print(answer)
"""
# Handling File not found Error:
"""
from pathlib import Path

path = Path('random.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, file {path} does not exist..!")
"""

# Analyse Text file:
from pathlib import Path
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/source/random.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"The file {path} is not available..!")
else:
    # count words in file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
