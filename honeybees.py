"""
TODO:
    -Implement random locations
"""

import random
import noise

boundaryscale = 2

class Hex:
    #Need to add error handling
    def __init__(self, coords):
        self.coords = coords
        self.setElevation()
        self.setPrecipitation()
        self.setTemperature()
        #self.ele = 100 * abs(noise.pnoise2(coords[0]/20,coords[1]/25,base = random.randint(0,100)))
        #self.pre = 100 * abs(noise.pnoise2(coords[0]/20,coords[1]/25,base = random.randint(0,100)))
        #self.temp = 100 * abs(noise.pnoise2(coords[0]/20,coords[1]/25,base = random.randint(0,100)))
        self.setBiome()
        self.setWater()
        self.setLocation()
    
    def setElevation(self):
        maxel = 100
        base = 20
        noiseval = noise.pnoise2(self.coords[0]/20,self.coords[1]/25,base = random.randint(0,100))
        self.ele = maxel * noiseval + base
        
    def setPrecipitation(self):
        maxpre = 100
        base = 20
        noiseval = noise.pnoise2(self.coords[0]/20,self.coords[1]/25,base = random.randint(0,100))
        self.pre = maxpre * noiseval + base
        
    def setTemperature(self):
        maxtemp = 100
        base = 40
        noiseval = noise.pnoise2(self.coords[0]/20,self.coords[1]/25,base = random.randint(0,100))
        self.temp = maxtemp * noiseval + base
    
    def setBiome(self):
        if self.temp <= 10  and self.pre <= 40:
            self.biome = 'tundra'
        else: 
            if 10 < self.temp and self.temp <= 75 and self.pre <=40:
                self.biome = 'plain'
            else:
                if 75 < self.temp and self.pre <= 30:
                    self.biome = 'desert'
                else:
                    if 75 < self.temp and self.pre > 30 and self.pre < 40:
                        self.biome = 'plain'
                    else: 
                        if self.pre > 40 and self.temp <= 50:
                            self.biome = 'forest'
                        else:
                            if self.pre > 40 and self.temp > 50:
                                self.biome = 'wetland'
                        
        if self.ele > 80:
            self.biome = 'mountain'
    
    #Will want to add springs somehow 
    def setWater(self):
        if self.ele < 10 and self.pre > 60 and self.biome != 'desert':
            self.water = 'lake'
        else: 
            if self.ele < 10 and self.pre > 60 and self.biome == 'desert':
                self.water = 'oasis'
            else:
                if self.ele < 60 and self.pre > 60:
                    self.water = 'river'
                else:
                    self.water = 'none'

    def setLocation(self):
        location = random.randint(1,16)
        if location == 16:
            if self.biome == 'mountain':
                print('this is a mountain\n')
            if self.biome == 'wetland':
                print('this is a wetland\n')
            if self.biome == 'forest':
                print('this is a forest\n')
            if self.biome == 'tundra':
                print('this is a tundra\n')
            if self.biome == 'plain':
                print('this is a plain\n')
            if self.biome == 'desert':
                print('this is a desert\n')