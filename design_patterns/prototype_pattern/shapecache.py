# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:48:33 2020

@author: carlo
"""

from circle import *
from square import *
from rectangle import *

class ShapeCache():   
    def __init__(self):
        self.shapemap={}
    
    def getShape(self,sid):
        cachedShape=self.shapemap[sid]
        return copy.copy(cachedShape)        
    
    def loadCache(self):
        circle=Circle()
        circle.id='1'
        self.shapemap[circle.id]=circle
        
        square=Square()
        square.id='2'
        self.shapemap[square.id]=square
        
        rectangle=Rectangle()
        rectangle.id='3'
        self.shapemap[rectangle.id]=rectangle
        
        