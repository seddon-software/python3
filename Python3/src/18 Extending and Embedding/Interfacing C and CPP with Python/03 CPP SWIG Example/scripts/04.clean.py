import os

os.chdir("../src")
os.system("python setup.py clean --all")
os.system("rm myexample_wrap.cpp")
print("staging area cleaned")


