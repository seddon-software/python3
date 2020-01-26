import scisoftpy as dnp

# create a 40x40 array with values between 0 and 16
x = dnp.arange(0, 16, 0.01).reshape(40,40)

dnp.plot.setdefname('Image Plot')
dnp.plot.image(x)

dnp.plot.setdefname('Surface Plot')
dnp.plot.surface(x)

