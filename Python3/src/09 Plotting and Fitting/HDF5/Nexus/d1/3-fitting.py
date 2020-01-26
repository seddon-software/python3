import scisoftpy as dnp


data = dnp.io.load('/dls/science/groups/das/ExampleData/training/14763.dat')
print data
print data.keys()

dnp.plot.setdefname('Fitting Data')
x = data['gonx'][120:-371]
dy = dnp.diff(data['i_pin'][120:-370])
dnp.plot.line(x, dy)

dnp.plot.setdefname('Fitting Result')
fr = dnp.fit.fit(dnp.fit.function.gaussian, x, dy, (-1.3, 0.05, 0.001), optimizer='local')
fr.plot()
print fr.parameters

