# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:35:22 2020

@author: carlo
"""

from roundedshapeFactory import *
from shapeFactory import *

class FactoryProducer():
    def getFactory(self,rounded):
        if rounded:
            return roundedshapeFactory()
        else:
            return shapeFactory()