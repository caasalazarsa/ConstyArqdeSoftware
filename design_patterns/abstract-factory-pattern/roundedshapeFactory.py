# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:31:18 2020

@author: carlo
"""

from roundedsquare import *
from roundedrectangle import *
from AbstractFactory import *

class roundedshapeFactory(AbstractFactory):
    
    def getShape(self,shapeType):
        
        if shapeType==None:
            return None
    
        if shapeType=="RECTANGLE":
            return roundedrectangle() 
        if shapeType=="SQUARE":
            return roundedsquare() 
        
        return None
