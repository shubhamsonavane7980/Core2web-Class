# to print months with days in that month

x = int(input(" Enter number 1 - 12 as months : "))

months = {
    1: "January has 31 days",
    2: "February has 28 days (or 29 in a leap year)",
    3: "March has 31 days",
    4: "April has 30 days",
    5: "May has 31 days",
    6: "June has 30 days",
    7: "July has 31 days",
    8: "August has 31 days",
    9: "September has 30 days",
    10: "October has 31 days",
    11: "November has 30 days",
    12: "December has 31 days"
}

if x in months:
    print(months[x])
else:
    print("Invalid input enter number between 1 - 12 as months")