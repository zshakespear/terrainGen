"""
TODO:
    
"""

import random
import noise
import pandas as pd
import os

boundaryscale = 2

class Hex:
    #Need to add error handling
    def __init__(self, coords):
        self.coords = coords
        self.setElevation()
        # self.setPrecipitation()
        # self.setTemperature()
        self.setBiome()
        # self.setWater()
        self.setLocation()
    
    def setElevation(self):
        maxel = 100
        base = 50
        noiseval = noise.pnoise2(self.coords[0]/34,self.coords[1]/10,octaves = 1, base = random.randint(0,100))
        self.ele = maxel * noiseval + base
        
    def setPrecipitation(self):
        maxpre = 100
        base = 50
        noiseval = noise.pnoise2(self.coords[0]/34,self.coords[1]/10,octaves = 1, base = random.randint(0,100))
        self.pre = maxpre * noiseval + base
        
    def setTemperature(self):
        maxtemp = 100
        base = 50
        noiseval = noise.pnoise2(self.coords[0]/34,self.coords[1]/10, octaves = 1, base = random.randint(0,100))
        self.temp = maxtemp * noiseval + base
    
    def setBiome(self):
        if self.ele > 75:
            self.biome = 'mountain'
        else:
            if self.ele > 50:
                self.biome = 'forest'
            else:
                if self.ele > 25:
                    self.biome = 'plain'
                else:
                    self.biome = 'wetland'
                        
                        
    
    #Will want to add springs somehow 
    def setWater(self):
        if self.ele < 10 and self.pre > 60:
            self.water = 'lake'
        else: 
            if self.ele < 60 and self.pre > 60:
                self.water = 'river'
            else:
                self.water = 'none'
    
    def coordsToString(self):
        coordstring = '('+str(self.coords[0])+ ',' + str(self.coords[1]) + ')'
        return coordstring
    
    def setLocation(self):
        location = random.randint(1,16)
        if location == 16:
            wd = os.getcwd()
            wd+='\GenLoc.xlsx'
            locgen = pd.read_excel(wd)
            loclimit = locgen.size - 1
            locseed = random.randint(0, loclimit)
            self.location = locgen.at[locseed, 'Locations']
            
            # print(self.location + ' at ' + self.coordsToString())
        else:
            self.location = 'none'