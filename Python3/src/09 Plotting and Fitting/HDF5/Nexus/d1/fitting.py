import scisoftpy as dnp
import sys
sys.executable = ""

dnp.plot.line(dnp.random.rand(100))
dnp.plot.line(dnp.random.rand(100), title='random numbers', name='ex1')
dnp.plot.setdefname('Plot 2')
dnp.plot.image(dnp.random.rand(100,100))

dnp.plot.setdefname('Plot 3')
dnp.plot.surface(dnp.random.rand(100,100))

data = dnp.io.load('/dls/science/groups/das/ExampleData/training/14763.dat')
print data
print data.keys()

dnp.plot.setdefname('Plot 4')
dnp.plot.line(data['i_pin'])
# dnp.plot.line(data[1])
dnp.plot.line(data['gonx'], data['i_pin'])

dnp.plot.setdefname('Plot 5')
# dnp.plot.line(data['gonx'][100:-401,10], dnp.diff(data['i_pin'][100:-400,10]))
x = data['gonx'][120:-371]
dy = dnp.diff(data['i_pin'][120:-370])
dnp.plot.line(x, dy)

dnp.plot.setdefname('Plot 6')
# from scisoftpy.jython.function import gaussian as g
# fr = dnp.fit.fit(g, x, dy, (-1.4, 0.02, 0.002))
fr = dnp.fit.fit(dnp.fit.function.gaussian, x, dy, (-1.0, 0.05, 0.001), optimizer='nm_simplex')
fr.plot()
print fr.parameters

