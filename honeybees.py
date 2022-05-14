"""
TODO:
    
"""

import random
import noise
import pandas as pd
import os

boundaryscale = 1
elseed = random.randint(0,100)
print(elseed)
# preseed = random.randint(0,100)
# tempseed = random.randint(0,100)

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
        noiseval = noise.pnoise2(self.coords[0]/8.5,self.coords[1]/5,octaves = 1, base = elseed)
        self.ele = maxel * noiseval + base
        
    def setPrecipitation(self):
        maxpre = 100
        base = 50
        noiseval = noise.pnoise2(self.coords[0]/8.5,self.coords[1]/5,octaves = 1, base = preseed )
        self.pre = maxpre * noiseval + base
        
    def setTemperature(self):
        maxtemp = 100
        base = 50
        noiseval = noise.pnoise2(self.coords[0]/8.5,self.coords[1]/5, octaves = 1, base = random.randint(0,100))
        self.temp = maxtemp * noiseval + base
    
    def setBiome(self):
        if self.ele > 95:
            self.biome = 'mountain'
        else:
            if self.ele > 80:
                self.biome = 'rainforest'
            else:
                if self.ele > 70:
                    self.biome = 'beach'
                else:
                    self.biome = 'ocean'
                        
                        
    
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
            locgen = pd.read_excel(wd, sheet_name = 'Sheet2')
            
            r0 = random.randint(0,1)
            if r0 == 0:
                locgen = locgen['General']
            else:
                if self.biome == 'mountain':
                    locgen = locgen['Mountain']
                    
                if self.biome == 'rainforest':
                    locgen = locgen['Forest']
                   
                if self.biome == 'beach':
                    locgen = locgen['Plain']
                    
                if self.biome == 'ocean':
                    locgen = locgen['Ocean']
                    
            
            locgen = locgen[locgen.notna()]
            loclimit = locgen.size - 1
            locseed = random.randint(0, loclimit)
            self.location = locgen.at[locseed]
            
            # print(self.location + ' at ' + self.coordsToString())
        else:
            self.location = 'none'