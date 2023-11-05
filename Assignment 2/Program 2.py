# right angled triangle

a1 = int(input("Enter Size  first  angle : "))

a2 = int(input("Enter Size  Second angle : "))

a3 = int(input("Enter Size  Third  angle : "))


if a1+a2+a3 == 180:
    if a1 or a2 or a3 == 90:
        print("It is right angled triangle")

else:
    print("It is not Right angled Triangle")