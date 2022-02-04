# Lets see how we can identify number is even or odd

number = 11
if number % 2 == 0:
    print(number," is an even number")
else:
    print(number," is an odd number")

#lets add if the number is larger than 43
number = 59
if number % 2 == 0:
    print(number," is an even number")
elif number > 10:
    print(number,"is an odd number, its larger than 10")
else:
    print(number," is an odd number")

# lets add for loop with if else statement
number1 = [13, 26, 45, 79]
total_even = 0
total_odd = 0

for t in number1:
    if t % 2 == 0:
        total_even = total_even + t  
    else:
        total_odd = total_odd + t
print("total of even number is",total_even)
print("total of odd number is",total_odd)

#other version
number2 = [13, 26, 45, 79]
total_even1 = 0
total_odd1 = 0

for p in number2:
    if p % 2 == 0:
        print("{} is an even number".format(p))
        total_even1 += p 
    else:
        print("{} is an odd number".format(p))
        total_odd1 += p
print("total of even number is",total_even1)
print("total of odd number is",total_odd1)