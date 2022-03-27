"""
TODO:
    -Implement water sources, rivers, lakes
    -Implement random locations
"""

import random

class Hex:

    def __init__(self, b):
        if b != 'forest' and b!= 'plain' and b != 'desert' and b != 'mountain' and b != 'hill' and b != 'wetland':
                print('invalid initializer')
                return
        
        self.biome = b
    
    def setBiome(self, b):
        self.biome = b
        
    
def printMap(hexmap):
    coord = hexmap.keys()
    for el in coord:
        print(el, ': ', hexmap[el].biome,'\n')
        
def genNeighbors(qcoord, rcoord, scoord, hexmap, it, maxit):
    print('On the ', it,"th iteration\n")
    seedcoord = (qcoord, rcoord, scoord)
    neigh1 = (qcoord, rcoord - 1, scoord + 1)
    neigh2 = (qcoord + 1, rcoord - 1, scoord)
    neigh3 = (qcoord +1, rcoord, scoord -1)
    neigh4 = (qcoord, rcoord +1, scoord -1)
    neigh5 = (qcoord -1, rcoord +1, scoord)
    neigh6 = (qcoord -1, rcoord, scoord +1)
    seedb = hexmap[seedcoord].biome
    if neigh1 in hexmap.keys():
        pass
    else:
        if it < maxit :
            hexmap[neigh1] = helperGen(seedb)
            genNeighbors(neigh1[0],neigh1[1],neigh1[2], hexmap, it+1, maxit)
    if neigh2 in hexmap.keys():
        pass
    else:
        
        if it < maxit :
            hexmap[neigh2] = helperGen(seedb)
            genNeighbors(neigh2[0],neigh2[1],neigh2[2], hexmap, it+1, maxit)
    if neigh3 in hexmap.keys():
        pass
    else:
        if it < maxit :
            hexmap[neigh3] = helperGen(seedb)
            genNeighbors(neigh3[0],neigh3[1],neigh3[2], hexmap, it+1, maxit)
    if neigh4 in hexmap.keys():
        pass
    else:
        if it < maxit :
            hexmap[neigh4] = helperGen(seedb)
            genNeighbors(neigh4[0],neigh4[1],neigh4[2], hexmap, it+1, maxit)
    if neigh5 in hexmap.keys():
        pass
    else:
        if it < maxit :
            hexmap[neigh5] = helperGen(seedb)
            genNeighbors(neigh5[0],neigh5[1],neigh5[2], hexmap, it+1, maxit)
    if neigh6 in hexmap.keys():
        pass
    else:
        if it < maxit :
            hexmap[neigh6] = helperGen(seedb)
            genNeighbors(neigh6[0],neigh6[1],neigh6[2], hexmap, it+1, maxit)
    
# 
def helperGen(seedb):
    if seedb == "forest" :
        #print("This is a forest")
        seed = random.randint(0, 3)
        if seed == 0:
            seedb = 'forest'
        if seed == 1:
            seedb = 'hill'
        if seed == 2:
            seedb = 'plain'
        if seed == 3:
            seedb = 'wetland'
        #return seedb
                
    if seedb == "desert" :
        #print("This is a desert")
        seed = random.randint(0,2)
        if seed == 0:
            seedb = 'desert'
        if seed == 1:
            seedb = 'plain'
        if seed == 2:
            seedb = 'hill'
        #return seedb
        
    if seedb == "hill" :
        #print("This is a hill")
        seed = random.randint(0,8)
        if seed == 0:
            seedb = 'mountain'
        if seed == 1 or seed == 2:
            seedb = 'hill'
        if seed == 3 or seed == 4:
            seedb = 'plain'
        if seed == 5 or seed == 6:
            seedb = 'forest'
        if seed == 7 or seed == 8:
            seedb = 'wetland'
        #return seedb
        
    if seedb == "mountain" :
        #print("This is a mountain")
        seed = random.randint(0,5)
        if seed == 0:
            seedb = 'mountain'
        else:
            seedb = 'hill'
        #return seedb

    if seedb == "plain" :
        #print("This is a plain")
        seed = random.randint(0, 4)
        if seed == 0:
            seedb = 'plain'
        if seed == 1:
            seedb = 'wetland'
        if seed == 2:
            seedb = 'hill'
        if seed == 3:
            seedb = 'forest'
        if seed == 4:
            seedb = 'desert'
        #sreturn seedb
        
    if seedb == "wetland" :
        #print("This is a wetland")
        seed = random.randint(0,1)
        if seed == 0:
            seedb = 'wetland'
        if seed == 1:
            seedb = 'plain'
        
    return Hex(seedb)