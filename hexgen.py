"""
TO-DO:
    - Print to txt
"""

import honeybees as hb
#Borrowed imports

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