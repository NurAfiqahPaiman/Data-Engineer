#type of variable in Python

# int -- Integer. Round number.
# float -- Float. Number with decimals
# str -- String. A sequence of characters.
# bool -- Boolean. Either True or False
# list -- List. A sequence of items.
# tuple -- Tuple. An immutable list.
# dict -- Dictionary. Collection of key-value pairs. Used to look up things.
# set -- Set. A set is a collection which is unordered, unindexed and each element is unique.
# None -- NoneType.

# int
num = 2343
type(num)

# float
num1 = 345.65
type(num1)

# string
a = "Haloo"
print(a)
print('haloo\nAfiqah')  #\n for new line
print('haloo\tAfiqah')  #\t for new tab
name = "afiqah"
age = 26
print("Name: {}, Age: {}".format(name,age))
# String also can be in sequence. this can be done by access a character by indexing
# 0   1   2   3   4   5
# a   f   i   q   a   h
#-6  -5  -4  -3  -2  -1
name_string = "afiqah"
print(name_string[-4])
print(name_string[1])
print(name_string[1:4])  #by slicing with index number

# boolean / bool
print( 4 > 10 )
print( ( 13 > 10) or (74 > 34) )
print( ( 24 > 87) and (61 > 113) )

# list
j = [1, 2, 3, 4, "string", True, None, [1,2,3], {"name":"Afiqah"}]
print(j)
len(j)

# tuple
d = (1, 2, 3, "string", [1,2,3])
print(d)

# dict / dictionary
v = {"a":2, "b":3}
info = {"name":"afiqah", "age":26, "hobbies":["music", "dancing"] }
print(info)

for p, o in info.items():
    print(p,o)

for item in info.items():
    print(item)

# set
# No duplicate values
w = {"a", "b", "c", "c"}
print(w)
print(type(w))

# none 
x = None
print(type(x))