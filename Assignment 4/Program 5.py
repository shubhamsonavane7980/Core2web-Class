
#  Print the number divisible by 7 but not divisible by 3 between 1 to 100

x = int(input("Enter the Start of Range : "))
y = int(input("Enter the End of   Range : "))

for i in range(x, y + 1):
   if i % 7 == 0 and i % 3 != 0:

        print(i)

# Good tricky que
