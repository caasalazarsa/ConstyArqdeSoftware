# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:19:16 2020

@author: carlo
"""

from Botella import *
from item import *

class ColdDrink(item):
    def packing(self):
        return Botella()
    
    def price(self):
        pass
