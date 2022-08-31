# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:19:16 2020

@author: carlo
"""

from Wrapper import *
from item import *

class Burger(item):
    def packing(self):
        return Wrapper()
    
    def price(self):
        pass
