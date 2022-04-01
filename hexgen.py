"""
Image code was taken from:
    https://variable-scope.com/posts/hexagon-tilings-with-python
"""

import honeybees as hb
import random
import hextile
from PIL import Image
from aggdraw import Draw, Brush, Pen

coordset = []
for i in range(25):
    for j in range(10):
        coordset.append((i,j))
    
hexdict = {}
seed = random.randint(0,256)
for el in coordset:
    hexdict[el] = hb.Hex((el[0],el[1]),seed)

image = Image.new('RGB', (2480, 2480), 'white') #Draws the base canvas
draw = Draw(image)
hexagon_generator = hextile.HexagonGenerator(80) #Hexagon Generator is initialized
#with a side length of 40 pixels. The column width will be 140 pixels and the
# row height is Sqrt[3]/2 * 40 pixels. 
for row in range(25):
  #color = row * 10, row * 20, row * 30 #Sets the color for the row with RGB values
  for col in range(10):
    hexagon = hexagon_generator(row, col) #Passes the row and column into the call function
    coords = (row, col)
    if hexdict[coords].biome == "wetland":
        color = 9, 82, 86
    else:
        if hexdict[coords].biome == 'mountain':
            color = 232, 235, 247
        else:
            if hexdict[coords].biome == 'forest':
                color = 20, 153, 17
            else:
                if hexdict[coords].biome == 'plain':
                    color = 220, 247, 99
                else: 
                    if hexdict[coords].biome == 'desert':
                        color = 242, 100, 25
                    else:
                        if hexdict[coords].biome == 'tundra':
                            color = 217, 208, 222
    draw.polygon(list(hexagon), Brush(color)) #Paints inside the vertices using the color determined by the row
draw.flush() 
image.save("map.jpg")
"""
# path = [x for x in range(0,20)]

seed = input('Input the seed biome: \n0: Desert\n1: Hill\n2: Mountain\n3: Plain\n4: Wetland\n5: Forest\n')
while seed != '0' and seed != '1' and seed != '2' and seed != '3' and seed != '4' and seed != '5':
    seed = input('Invalid input.\nInput the seed biome: \n0: Desert\n1: Hill\n2: Mountain\n3: Plain\n4: Wetland\n5: Forest\n')

seed = int(seed)

if seed == 0:
    seedb = 'desert'
if seed == 1:
    seedb = 'hill'
if seed == 2:
    seedb = 'mountain'
if seed == 3:
    seedb = 'plain'
if seed == 4:
    seedb = 'wetland'
if seed == 5:
    seedb = 'forest'
    
start = hb.Hex(seedb)

hexmap ={(0,0,0) : start}
while True:
    maxit = input('Input number of layers for the map\n')
    try:
        maxit = int(maxit)
        break
    except:
        print('Invalid input.\n')

hb.genNeighbors(0, 0, 0, hexmap, 0, maxit)
print("about to manually add hexes\n")
# hexmap[(maxit, -maxit, 0)] = hb.helperGen(hexmap[(maxit-1,-maxit+1,0)].biome)
# hexmap[(0,maxit,-maxit)] = hb.helperGen(hexmap[(0,maxit-1,-maxit+1)].biome)
# hexmap[(-maxit, 0, maxit)] = hb.helperGen(hexmap[(-maxit+1,0,maxit-1)].biome)
#print('Done generating map.\nPrinting')

    
hb.printMap(hexmap)
"""