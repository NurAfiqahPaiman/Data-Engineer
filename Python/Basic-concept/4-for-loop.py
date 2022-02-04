# 'for loop' is for prossecing the list which keeps more than one value.
number = [5,6,7,8,9] # this is a list
total = 0

for i in number:      # i is a varieble that we executed in loop
    total = total + i
    print(total)
    
print("Total is ",total)

#another example
number1 = [2, 4, 6, 8, 10]
total1 = 0

print("Let's start a loop")

for n in number1:
    total1 += n
    print("number=",n, "numbers=",number1, "total=",total1)
    
print("Total is", total1)