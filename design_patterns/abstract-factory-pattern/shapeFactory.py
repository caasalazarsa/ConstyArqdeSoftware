# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:52:33 2020

@author: carlo
"""

from AbstractFactory import *

from circle import *
from rectangle import *
from square import *

class shapeFactory(AbstractFactory):
    
    def getShape(self,shapeType):
        
        if shapeType==None:
            return None
        
        if shapeType=="CIRCLE":
            return circle()
        if shapeType=="RECTANGLE":
            return rectangle() 
        if shapeType=="SQUARE":
            return square() 
        
        return None
