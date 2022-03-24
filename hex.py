import random

class Hex:
    #Will want to prohibit the creation of hexes without standard biome types
    def __init__(self, b):
        self.biome = b
        self.neigh1 = None
        self.neigh2 = None
        self.neigh3 = None
        self.neigh4 = None
        self.neigh5 = None
        self.neigh6 = None
    
    def setBiome(self, b):
        self.biome = b
        
    def setNeigh1(self, neighbor):
        self.neigh1 = neighbor
        
    def setNeigh2(self, neighbor):
        self.neigh2 = neighbor
    
    def setNeigh3(self, neighbor):
        self.neigh3 = neighbor
        
    def setNeigh4(self, neighbor):
        self.neigh4 = neighbor
        
    def setNeigh5(self, neighbor):
        self.neigh5 = neighbor
            
    def setNeigh6(self, neighbor):
        self.neigh6 = neighbor
    """
    Each branch will generate a new biome based off the current biome
    and then pass the new biome into a new hex located in the neighbor
    and link the new hex to the self. 
    After initializing each of the neighbors, the function will link them
    all together.
    I think I could create a helperfunction to generate the biome since
    genNeighbors will be doing the heavy lifting of creating new hexes
    and chaining them together.
    genNeighbors tests to see if there is already a neighbor and then
    generates a new one at each location there is not already a neighbor. 
    """
    def genNeighbors(self):
        if self.neigh1 == None:
            print("Initializing neighbor 1")
        if self.neigh2 == None:
            print("Initializing neighbor 2")
        if self.neigh3 == None:
            print("Initializing neighbor 3")
        if self.neigh4 == None:
            print("Initializing neighbor 4")
        if self.neigh5 == None:
            print("Initializing neighbor 5")
        if self.neigh6 == None:
            print("Initializing neighbor 6")
            
    def helperBiome(self):
        if self.biome == "forest" :
            print("This is a forest")
        if self.biome == "desert" :
            print("This is a desert")
        if self.biome == "hill" :
            print("This is a hill")
        if self.biome == "mountain" :
            print("This is a mountain")
        if self.biome == "plain" :
            print("This is a plain")
        if self.biome == "wetland" :
            print("This is a wetland")