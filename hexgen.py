"""
Image code was taken from:
    https://variable-scope.com/posts/hexagon-tilings-with-python
"""

import honeybees as hb
import random
import hextile
from PIL import Image
from aggdraw import Draw, Brush, Pen
import pandas as pd

coordset = []
rows = 34
columns = 10 #remember this is twice as many as you think
for i in range(rows):
    for j in range(columns):
        coordset.append((i,j))
    
hexdict = {}
seed = random.randint(0,256)
locationList =  pd.DataFrame([['Location', 'Coordinates']])
for el in coordset:
    hexdict[el] = hb.Hex((el[0],el[1]))
    if hexdict[el].location != 'none':
        locationpd = pd.DataFrame([[hexdict[el].location, hexdict[el].coordsToString()]])
        locationList = pd.concat([locationList,locationpd])
        
with open("locationList.txt", 'w') as file:
        textDummy = locationList.to_string(header=False, index = False)
        file.write(textDummy)
        
def color_from_biome(Hex):
    if Hex.biome == "wetland":
        color = 9, 82, 86
    else:
        if Hex.biome == 'mountain':
            color = 51, 30, 54
        else:
            if Hex.biome == 'forest':
                color = 20, 153, 17
            else:
                if Hex.biome == 'plain':
                    color = 220, 247, 99
                else: 
                    if Hex.biome == 'desert':
                        color = 242, 100, 25
                    else:
                        if Hex.biome == 'tundra':
                            color = 217, 208, 222
    return color

def color_from_el(Hex):
    if Hex.ele < 10:
        color = 41, 63, 20
    else:
        if Hex.ele < 20:
            color = 56, 108, 11
        else:
            if Hex.ele < 30:
                color = 56, 167, 0
            else:
                if Hex.ele < 40:
                    color = 49, 216, 67
                else: 
                    color = 62, 255, 139
    return color
    
def color_from_water(Hex):
    if Hex.water == 'river':
        color = 71, 168, 189
    if Hex.water == 'lake':
        color = 30, 56, 136
    if Hex.water == 'none':
        color = 217, 208, 222
    return color

def color_from_pre(Hex):
    if Hex.pre < 10:
        color = 218, 227, 229
    else:
        if Hex.pre < 20:
            color = 187, 209, 234
        else:
            if Hex.pre < 30:
                color = 161, 198, 234
            else:
                if Hex.pre < 40:
                    color = 80, 125, 188
                else: 
                    color = 4, 8, 15
    return color

def color_from_temp(Hex):
    if Hex.temp < 10:
        color = 255, 207, 153
    else:
        if Hex.temp < 20:
            color = 255, 192, 127
        else:
            if Hex.temp < 30:
                color = 241, 81, 86
            else:
                if Hex.temp < 40:
                    color = 165, 64, 45
                else: 
                    color = 114, 17, 33
    return color

image = Image.new('RGB', (2480, 2480), 'white') #Draws the base canvas
draw = Draw(image)
hexagon_generator = hextile.HexagonGenerator(80) #Hexagon Generator is initialized
#with a side length of 40 pixels. The column width will be 140 pixels and the
# row height is Sqrt[3]/2 * 40 pixels. 
for row in range(rows):
  #color = row * 10, row * 20, row * 30 #Sets the color for the row with RGB values
  for col in range(columns):
    hexagon = hexagon_generator(row, col) #Passes the row and column into the call function
    coords = (row, col)
    color = color_from_biome(hexdict[coords])
    draw.polygon(list(hexagon), Brush(color)) #Paints inside the vertices using the color determined by the row
draw.flush() 
image.save("biomeMap.jpg")

# for row in range(rows):
#   #color = row * 10, row * 20, row * 30 #Sets the color for the row with RGB values
#   for col in range(columns):
#     hexagon = hexagon_generator(row, col) #Passes the row and column into the call function
#     coords = (row, col)
#     color = color_from_el(hexdict[coords])
#     draw.polygon(list(hexagon), Brush(color)) #Paints inside the vertices using the color determined by the row
# draw.flush() 
# image.save("elMap.jpg")

# for row in range(rows):
#   #color = row * 10, row * 20, row * 30 #Sets the color for the row with RGB values
#   for col in range(columns):
#     hexagon = hexagon_generator(row, col) #Passes the row and column into the call function
#     coords = (row, col)
#     color = color_from_water(hexdict[coords])
#     draw.polygon(list(hexagon), Brush(color)) #Paints inside the vertices using the color determined by the row
# draw.flush() 
# image.save("waterMap.jpg")

# for row in range(rows):
#   #color = row * 10, row * 20, row * 30 #Sets the color for the row with RGB values
#   for col in range(columns):
#     hexagon = hexagon_generator(row, col) #Passes the row and column into the call function
#     coords = (row, col)
#     color = color_from_temp(hexdict[coords])
#     draw.polygon(list(hexagon), Brush(color)) #Paints inside the vertices using the color determined by the row
# draw.flush() 
# image.save("tempMap.jpg")

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