import pandas as pd
import numpy as np
import bokeh.plotting as bp
from bokeh.models import HoverTool


bp.output_file("html/08.html")

# Read the data from a csv into a dataframe
flights = pd.read_csv('data/flights.csv', index_col=0)
print(type(flights))
print(flights.shape)
print(flights.columns)
# Summary stats for the column of interest
print(flights['arr_delay'].describe())
print("done")

arr_hist, edges = np.histogram(flights['arr_delay'], 
                               bins = int(180/5), 
                               range = [-60, 120])
# Put the information in a dataframe
delays = pd.DataFrame({'arr_delay': arr_hist, 
                       'left': edges[:-1], 
                       'right': edges[1:]})
print(delays)

p = bp.figure(plot_height = 600, plot_width = 600, 
           title = 'Histogram of Arrival Delays',
          x_axis_label = 'Delay (min)]', 
           y_axis_label = 'Number of Flights')



# Import the ColumnDataSource class
from bokeh.models import ColumnDataSource
# Convert dataframe to column data source
src = ColumnDataSource(delays)
print(src.data.keys())

# Add a quad glyph with source this time
p.quad(source=src, bottom=0, top='arr_delay', 
       left='left', right='right', 
       fill_color='red', line_color='black')

# Add a hover tool referring to the formatted columns
hover = HoverTool(tooltips = [('Delay', '@left'),
                             ('Num of Flights', '@arr_delay')])

# Style the plot
#p = bp.style()

# Add the hover tool to the graph
p.add_tools(hover)
# Show the plot
bp.show(p)
