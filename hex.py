"""
TODO:
    -Implement water sources, rivers, lakes
    -Implement random locations
"""

# import random

class Hex:

    def __init__(self, b):
        if b != 'forest' and b!= 'plain' and b != 'desert' and b != 'mountain' and b != 'hill' and b != 'wetland':
                print('invalid initializer')
                return
        
        self.biome = b
        # self.neigh1 = None
        # self.neigh2 = None
        # self.neigh3 = None
        # self.neigh4 = None
        # self.neigh5 = None
        # self.neigh6 = None
    
    def setBiome(self, b):
        self.biome = b
        
    # def setNeigh1(self, neighbor):
    #     self.neigh1 = neighbor
        
    # def setNeigh2(self, neighbor):
    #     self.neigh2 = neighbor
    
    # def setNeigh3(self, neighbor):
    #     self.neigh3 = neighbor
        
    # def setNeigh4(self, neighbor):
    #     self.neigh4 = neighbor
        
    # def setNeigh5(self, neighbor):
    #     self.neigh5 = neighbor
            
    # def setNeigh6(self, neighbor):
    #     self.neigh6 = neighbor
    
    # def genNeighbors(self):
    #     if self.neigh1 == None:
    #         print("Initializing neighbor 1\n")
    #         seedb = self.helperBiome()
    #         self.setNeigh1(Hex(seedb))
            
    #     if self.neigh2 == None:
    #         print("Initializing neighbor 2\n")
    #         seedb = self.helperBiome()
    #         self.setNeigh2(Hex(seedb))
            
    #     if self.neigh3 == None:
    #         print("Initializing neighbor 3\n")
    #         seedb = self.helperBiome()
    #         self.setNeigh3(Hex(seedb))
            
    #     if self.neigh4 == None:
    #         print("Initializing neighbor 4\n")
    #         seedb = self.helperBiome()
    #         self.setNeigh4(Hex(seedb))
            
    #     if self.neigh5 == None:
    #         print("Initializing neighbor 5\n")
    #         seedb = self.helperBiome()
    #         self.setNeigh5(Hex(seedb))
            
    #     if self.neigh6 == None:
    #         print("Initializing neighbor 6\n")
    #         seedb = self.helperBiome()
    #         self.setNeigh6(Hex(seedb))
    #     self.helperLink()
            
    # def helperLink(self):
    #     self.neigh1.setNeigh3(self.neigh2)
    #     self.neigh1.setNeigh5(self.neigh6)
    #     self.neigh1.setNeigh4(self)
        
    #     self.neigh2.setNeigh4(self.neigh3)
    #     self.neigh2.setNeigh6(self.neigh1)
    #     self.neigh2.setNeigh5(self)
        
    #     self.neigh3.setNeigh1(self.neigh2)
    #     self.neigh3.setNeigh5(self.neigh4)
    #     self.neigh3.setNeigh6(self)
        
    #     self.neigh4.setNeigh2(self.neigh3)
    #     self.neigh4.setNeigh6(self.neigh5)
    #     self.neigh4.setNeigh1(self)
        
    #     self.neigh5.setNeigh1(self.neigh6)
    #     self.neigh5.setNeigh3(self.neigh4)
    #     self.neigh5.setNeigh2(self)
        
    #     self.neigh6.setNeigh2(self.neigh1)
    #     self.neigh6.setNeigh4(self.neigh5)
    #     self.neigh6.setNeigh3(self)
    
    # def helperBiome(self):
    #     if self.biome == "forest" :
    #         #print("This is a forest")
    #         seed = random.randint(0, 3)
    #         if seed == 0:
    #             seedb = 'forest'
    #         if seed == 1:
    #             seedb = 'hill'
    #         if seed == 2:
    #             seedb = 'plain'
    #         if seed == 3:
    #             seedb = 'wetland'
    #         return seedb
                
    #     if self.biome == "desert" :
    #         #print("This is a desert")
    #         seed = random.randint(0,2)
    #         if seed == 0:
    #             seedb = 'desert'
    #         if seed == 1:
    #             seedb = 'plain'
    #         if seed == 2:
    #             seedb = 'hill'
    #         return seedb
        
    #     if self.biome == "hill" :
    #         #print("This is a hill")
    #         seed = random.randint(0,8)
    #         if seed == 0:
    #             seedb = 'mountain'
    #         if seed == 1 or seed == 2:
    #             seedb = 'hill'
    #         if seed == 3 or seed == 4:
    #             seedb = 'plain'
    #         if seed == 5 or seed == 6:
    #             seedb = 'forest'
    #         if seed == 7 or seed == 8:
    #             seedb = 'wetland'
    #         return seedb
        
    #     if self.biome == "mountain" :
    #         #print("This is a mountain")
    #         seed = random.randint(0,5)
    #         if seed == 0:
    #             seedb = 'mountain'
    #         else:
    #             seedb = 'hill'
    #         return seedb

    #     if self.biome == "plain" :
    #         #print("This is a plain")
    #         seed = random.randint(0, 4)
    #         if seed == 0:
    #             seedb = 'plain'
    #         if seed == 1:
    #             seedb = 'wetland'
    #         if seed == 2:
    #             seedb = 'hill'
    #         if seed == 3:
    #             seedb = 'forest'
    #         if seed == 4:
    #             seedb = 'desert'
    #         return seedb
        
    #     if self.biome == "wetland" :
    #         #print("This is a wetland")
    #         seed = random.randint(0,1)
    #         if seed == 0:
    #             seedb = 'wetland'
    #         if seed == 1:
    #             seedb = 'plain'
    #         return seedb