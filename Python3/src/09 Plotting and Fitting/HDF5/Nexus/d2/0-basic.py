import scisoftpy as dnp

dnp.plot.setdefname('Random Numbers')
dnp.plot.line(dnp.random.rand(100))

dnp.plot.setdefname('Random Image')
dnp.plot.image(dnp.random.rand(100,100))

dnp.plot.setdefname('Random Surface')
dnp.plot.surface(dnp.random.rand(100,100))

