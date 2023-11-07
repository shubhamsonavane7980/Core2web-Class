
# Print the count of all negative numbers from given numbers .. take input from user

x = int(input("Enter Start : "))
y = int(input("Enter End   : "))

count = 0
for i in range(x,y+1):
    if i < 0 :
        count+= 1
print(count)