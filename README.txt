# terrainGen

This code generates randomly generated hex maps. The hexgen.py file does most of the heavy lifting
while the honeybees file declares the hex class and the functions called by hexgen.

When the user runs the program, hexgen creates a dictionary of coordinates and then uses the coordinates
to initialize hex objects. When a hex is initialized, three values are generated using Perlin noise. Depending on the constellation
of values, a biome is assigned to each hex. In addition, a random number of hexes are assigned as hosts
to special locations. These coordinates and associated locations are printed in a text file called
locationList.

Hexgen finishes by generating a jpg map of the world generated, along with a map of the water features
on the map. The code was adapted from this website:
https://variable-scope.com/posts/hexagon-tilings-with-python

The inspiration for the coordinate system comes from Red Blob Games: https://www.redblobgames.com/grids/hexagons/

The inspiration for the use of Perlin noise comes from the following videos:
https://www.youtube.com/watch?v=wZXW_nzJotc
https://www.youtube.com/watch?v=fjZAgoxFKiQ

TO-DO:
-Add more random locations, especially for the beach
-Find way to mark on map where the locations/water features are
-Create a function to reshuffle locations