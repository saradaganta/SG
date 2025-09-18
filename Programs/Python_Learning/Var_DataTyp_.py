# Variables
# a - Variable, 10 - Data or Value, '='- operator. Python variables are not required to declared explicitly for their datatypes.

a = 10
b = 20
c = a+b
print(a); print(b); print(c)
print(type(a))
# -------------------------------------------
# DataTypes

# Int,
a = 10; print(a) ; print(type(a))
# str,
x = 'Python'; print(x) ; print(type(x))
# bool,
y = True ; print(y) ; print(type(y))
# float,
z = 24.5 ; print(z) ; print(type(z))

# -------------------------------------------
# Convert Datatypes
# Float to Int, Str, bool
a = 24.5
b = 36.5
c = a + b
print(a, b, c)
print(type(a), type(b), type(c))
d = int(c)
e = str(c)
f = bool(c)
print(d, e, f)
print(type(d), type(e), type(f))

# String ------------------------------------
a = '10'
b = '20'
c = a + b
Fname = 'Siva'
Lname = 'Gurram'
Fullname = Fname +' '+ Lname
print(a,b,c)
print(type(a), type(b), type(c))
print(Fname, Lname, Fullname)
# - Type conversion
# str to Int
d = int(a) + int(b)
print(d, type(d))
# - Str to Float
e = float(a) + float(b)
print(e, type(e))
# Boolean ------------------------------------
# True or False

"""
Complex DataTypes,
List,
Tuple,
set,
dict
"""
# ------------------------------------------