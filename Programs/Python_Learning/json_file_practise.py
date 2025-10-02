# using json.dumps() and json.loads()
"""
# writing to file
from pathlib import Path
import json

numbers = [2,3,4,5,6,7,8,9]

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/numbers.json')
content = json.dumps(numbers)
path.write_text(content)
"""

# Reading from file
"""
from pathlib import Path
import json

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
"""

# Saving and Reading user generated data

from pathlib import Path
import json

usrname = input("What is your name : ")

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/username.json')
content = json.dumps(usrname)
path.write_text(content)

print(f"We will remember you when you are back, {usrname}")

