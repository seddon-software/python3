import numpy as np
from bokeh.plotting import figure, output_file, show

x = np.arange(-5, 5, 0.01)
y = np.cosh(x) - np.sinh(x)


# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)
