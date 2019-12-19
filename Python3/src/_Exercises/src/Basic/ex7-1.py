"""
Write a program that counts the number of lines in a file.
"""

inFile = None
count = 0

try:
    inFile = open("data/original.txt", "r")

    for line in inFile:
        count += 1
except IOError as reason:
    print(reason)
finally:        
    if inFile: inFile.close()

print(f"Line count = {count}")


1