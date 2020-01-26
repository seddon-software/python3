import scisoftpy as dnp

# create a 40x40 array with values between 0 and 16
x = dnp.arange(0, 16, 0.01).reshape(40,40)
print "----- x ------"
print x
# create a 40x40 array with values between 0(black) and 256(white) 
y = x * x
print "----- y ------"
print y

dnp.plot.setdefname('Image Plot')
dnp.plot.image(y)


