import bokeh.plotting as bp
import numpy as np

bp.output_file("categories.html")

teams = ['Juventus', 'Atletico Madrid', 'Leverkusen', 'Lokomotive Moscow']
points = [13, 7, 6, 3]
fig = bp.figure(x_range=teams, 
              plot_height=250, 
              title="Champions League Table",
              toolbar_location=None, 
              tools="")

fig.vbar(x=teams, top=points, width=0.9)

fig.xgrid.grid_line_color = 'red'
fig.y_range.start = 0

bp.show(fig)
