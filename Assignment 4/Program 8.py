
# Print no. divisible by 3 and 5 both in given range take input from user

x = int(input("Enter Start : "))
y = int(input("Enter End   : "))

for i in range(x,y+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)