"""
Write a program that inputs a 4 digit year and then 
calculates whether or not it is a leap year.
"""

def isLeap(year):
    result = False
    if year %   4 == 0: result = True
    if year % 100 == 0: result = False
    if year % 400 == 0: result = True
    return result


year = int(input("Enter a year: "))

if isLeap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

1