"""
TODO:
    -Implement random locations
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
        self.setPrecipitation()
        self.setTemperature()
        self.setBiome()
        self.setWater()
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
        if self.ele > 80:
            self.biome = 'mountain'
        else:
            if self.pre < 50 and self.temp >50
                self.biome = 'plain'
            else:
                if self.pre < 50 and self.temp < 50:
                    self.biome = 'tundra'
                else:
                    if self.pre >=50 and self.temp >=50:
                        self.biome = 'wetland'
                    else:
                        if self.pre >= 50 and self.temp < 50:
                            self.biome = 'forest'
                        
    
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
        coordstring = '('+str(self.coords[0])+ ',' + str(self.coords[1]) + ')\n'
        return coordstring
    
    #I want to modify this so that it uses an excel sheet.
    #Can I do that really quickly?
    def setLocation(self):
        location = random.randint(1,16)
        if location == 16:
            locseed = random.randint(1,15)
            if locseed == 1:
                self.location = 'Pit/Crater'
            if locseed == 2:
                self.location = 'Tomb'
            if locseed == 3:
                self.location = 'Bandit encampment'
            if locseed == 4:
                self.location = 'Small village'
            if locseed == 5:
                self.location = 'Deserted camp'
            if locseed == 6:
                self.location = 'Ancient Battleground'
            if locseed == 7:
                self.location = 'Overgrown Road'
            if locseed == 8:
                self.location = 'Fossil'
            if locseed == 9:
                self.location = 'Abandoned Military Outpost'
            if locseed == 10:
                self.location = 'Wizard\' Tower'
            if locseed == 11:
                self.location = 'Magic Wellspring'
            if locseed == 12:
                self.location = 'Witch\'s Hutch'
            if locseed == 13:
                self.location = 'Ruins'
            if locseed == 14:
                self.location = 'Monster Lair'
            if locseed == 15:
                self.location = 'Ancient Military Cache'
            
            print(self.location + 'at ' + coordsToString())
        else:
            self.location = 'none'