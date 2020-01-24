import os

os.chdir("../src")
os.system("python setup.py clean --all")
os.system("rm hello_wrap.c")
print("staging area cleaned")


