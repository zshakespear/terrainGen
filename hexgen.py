"""
TO-DO:
    - Change hexgen to work on a dictionary.
    - Find someway to print the hex map to the terminal
    - Print to txt
    - New traversal patterns
"""

import hex
#Borrowed imports

def printMap(hexmap):
    coord = hexmap.keys()
    for el in coord:
        print(el, ': ', hexmap[el].biome,'\n')
        
def genNeighbors(qcoord, rcoord, scoord, hexmap):
    seedcoord = (qcoord, rcoord, scoord)
    neigh1 = (qcoord, rcoord - 1, scoord + 1)
    neigh2 = (qcoord + 1, rcoord - 1, scoord)
    neigh3 = (qcoord +1, rcoord, scoord -1)
    neigh4 = (qcoord, rcoord +1, scoord -1)
    neigh5 = (qcoord -1, rcoord +1, scoord)
    neigh6 = (qcoord -1, rcoord, scoord +1)
    seedb = hexmap[seedcoord].biome
    if(hexmap[neigh1] == None):
        hexmap[neigh1] = helperGen(seedb)
    if(hexmap[neigh2] == None):
        hexmap[neigh2] = helperGen(seedb)
    if(hexmap[neigh3] == None):
        hexmap[neigh3] = helperGen(seedb)
    if(hexmap[neigh4] == None):
        hexmap[neigh4] = helperGen(seedb)
    if(hexmap[neigh5] == None):
        hexmap[neigh5] = helperGen(seedb)
    if(hexmap[neigh6] == None):
        hexmap = helperGen(seedb)
    
def helperGen(seedb):
    print('helperGen')
    return hex.Hex('plain')

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
    
start = hex.Hex(seedb)

hexmap ={(0,0,0) : start}


    
printMap(hexmap)