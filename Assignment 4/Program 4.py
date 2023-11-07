

x = int(input("Enter Start ASCII Range :"))
y = int(input("Enter End ASCII Range   :"))


for i in range(x,y+1):
    print("The Character of ASCII value",i,"'is",chr(i))