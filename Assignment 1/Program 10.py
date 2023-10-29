#to check leap year or not

year = int(input("Enter the year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes",year," Is leap year")
else:
    print("No", year, "is not leap year ")