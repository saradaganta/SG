# using json.dumps() and json.loads()
"""
from pathlib import Path
import json

numbers = [2,3,4,5,6,7,8,9]

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/numbers.json')
content = json.dumps(numbers)
path.write_text(content)
"""
from pathlib import Path
import json

path = Path('/Users/sg/Documents/Python_Learning/SG/Programs/Data Files/target/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)