import os

os.system("wc data/zen.txt")
f = open("data/zen.txt")
text = f.read()
print(f"characters = {len(text)}")
print(f"words = {len(text.split())}")
print(f"lines = {len(text.split(chr(10)))-1}")

