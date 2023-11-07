
# Print All ASCII values from the given Character Range  Take start and end from User

start = ord(input("Enter The Start In Character : "))

end = ord(input("Enter The End In Character : "))

for i in range(start,end+1):
    print("Ascii value of ",chr(i),"is",i)

    # Quite good Que ...