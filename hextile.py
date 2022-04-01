# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:29:50 2022

this code was adapted from this website:
    https://variable-scope.com/posts/hexagon-tilings-with-python
    
To-do:
"""
import math
from PIL import Image
import honeybees as hb
from aggdraw import Draw, Brush, Pen
  
class HexagonGenerator(object):
  """Returns a hexagon generator for hexagons of the specified size."""
  def __init__(self, edge_length):
    self.edge_length = edge_length

  @property
  def col_width(self):
    return self.edge_length * 3

  @property
  def row_height(self):
    return math.sin(math.pi / 3) * self.edge_length

  def __call__(self, row, col): #as far as I can tell, this function takes the
  #row and column and then returns a list of x and y coordinates for the vertices
  #An important note is that for some reason, rows are not offset, but columns are
  #So you have a row in between two rows, but the column is always refering to
  #nth element in that row. 
    x = (col + 0.5 * (row % 2)) * self.col_width
    y = row * self.row_height
    for angle in range(0, 360, 60):
      x += math.cos(math.radians(angle)) * self.edge_length
      y += math.sin(math.radians(angle)) * self.edge_length
      yield x
      yield y
      
def roffset_to_cube(offset, col, row):
    q = col - (row + offset * (row & 1)) // 2
    r = row
    #s = -q - r
    if offset != 1 and offset != -1:
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return (r, q)
