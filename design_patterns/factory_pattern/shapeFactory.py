# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:52:33 2020

@author: carlo
"""

from circle import *
from rectangle import *
from square import *
from triangle import *


class shapeFactory():
    
    def getShape(self,shapeType):
        
        if shapeType==None:
            return None
        
        if shapeType=="CIRCLE":
            return circle()
        if shapeType=="RECTANGLE":
            return rectangle() 
        if shapeType=="SQUARE":
            return square() 
        if shapeType=="TRIANGLE":
            return triangle()
        
        
        return None
