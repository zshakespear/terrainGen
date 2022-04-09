# terrainGen

This code generates randomly generated hex maps. The hexgen.py file does most of the heavy lifting
while the honeybees file declares the hex class and the functions called by hexgen.

The user will input the size of the map as an integer representing the number of layers around the
center point. Hexgen generates a set of possible q,r,s coordinates and then initializes a set of hexes
with the coordinates. 

When a hex is initialized, three values are generated using Perlin noise. Depending on the constellation
of values, a biome is assigned to each hex. 

Hexgen finishes by generating a jpg map of the world generated. The code was adapted from this website:
https://variable-scope.com/posts/hexagon-tilings-with-python

The inspiration for the coordinate system comes from Red Blob Games: https://www.redblobgames.com/grids/hexagons/

The inspiration for the use of Perlin noise comes from the following videos:
https://www.youtube.com/watch?v=wZXW_nzJotc
https://www.youtube.com/watch?v=fjZAgoxFKiQ

TO-DO:
-Toy with the biome limits
-Add more random locations
-Find way to mark on map where the locations are