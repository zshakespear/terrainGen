# terrainGen

This code generates randomly generated hex maps. The hexgen.py file does most of the heavy lifting
while the honeybees file declares the hex class and the functions called by hexgen.

The user will input the size of the map as an integer representing the number of layers around the
center point. Hexgen generates a list of possible q,r,s coordinates and then initializes a dictionary
with keys equal to these coordinates. The program then assigns a hex to each of these keys, initialzing
the hex with the coordinate values.

When a hex is initialized, three values are generated using Perlin noise. Depending on the constellation
of values, a biome is assigned to each hex. 

Hexgen finishes by printing the dictionary to a txt file.

The inspiration for the coordinate system comes from Red Blob Games: https://www.redblobgames.com/grids/hexagons/

The inspiration for the use of Perlin noise comes from the following videos:
https://www.youtube.com/watch?v=wZXW_nzJotc
https://www.youtube.com/watch?v=fjZAgoxFKiQ