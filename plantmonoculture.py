#!/usr/bin/env python
'''
This is a python planting algorithm which grabs the data about a certain plant and shows an optimal monoculture plot of that plant.
You can also use it directly as a Python module in your code.

usage:

 $ python plantmonoculture.py "carrot"

sample output:
graphical display of hexagons with scale.

notes: this does not have any complex algorithmic optimisation, just data -> geometric modifiers-> graph

task 1: plot in a grid (square)
input: grid_rows, grid_cols, "carrot"
output: standard graph + "scale: " overlay

task 2: plot on a plot (square)
input: size_x, sixe_y, "carrot"
output: standard graph + "scale: " overlay

geomrtry question: how does the plant spacing value get changed when (square -> hex)?

task 3: plot on a hexgrid (hex)
input: hexgrid_rows, hexgrid_columns, "carrot"
output: standard graph + "scale: " overlay

'''