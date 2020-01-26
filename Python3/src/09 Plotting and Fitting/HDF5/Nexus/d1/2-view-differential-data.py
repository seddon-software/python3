import scisoftpy as dnp

hdf5FileName = '/dls/science/groups/das/ExampleData/training/14763.dat'
data = dnp.io.load(hdf5FileName)
print data
print data.keys()

dnp.plot.setdefname('Differential Data Plot')
lo = 0
hi = -400
x = data['gonx'][lo:hi-1]
dy = dnp.diff(data['i_pin'][lo:hi])
print x.shape, dy.shape
dnp.plot.line(x, dy)



