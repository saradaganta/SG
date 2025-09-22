# Reading the file:
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/pi_digits.txt/')
contents = path.read_text()
contents = contents.rstrip() # To remove extra blank line at last in text file.
print(contents)
"""
# print using for loop line by line.
"""
from pathlib import Path

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/pi_digits.txt/')
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

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/pi_digits.txt/')
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
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/pi_digits.txt/')
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
path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/Million_digits.txt')
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
print("********** Exercise 10.1 ***********")

