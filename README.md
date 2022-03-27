# terrainGen

The purpose of this code is to allow the user to generate terrain for hex maps.
The user will input the seed biome and the program will traverse the terrain
and return a map in a txt file.

The honeybees.py file creates the base object while the hexgen file fills a dictionary with these hexes
and then prints the dictionary in a txt file. Functions are contained in the honeybees file.

The hex object presently contains a biome string. In the future, other parameters such as water sources
and special locations

The inspiration for the coordinate system comes from Red Blob Games: https://www.redblobgames.com/grids/hexagons/