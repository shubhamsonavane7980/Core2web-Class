
# print sum of given number start and end take from user

x = int(input("Enter Start : "))
y = int(input("Enter End   : "))

sum = 0
for i in range (x,y):
    sum = sum + i

print("Sum of",x,"To",y,"Is",sum)

