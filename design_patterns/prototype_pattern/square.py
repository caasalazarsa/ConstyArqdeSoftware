# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:44:07 2020

@author: carlo
"""
from shape import *

class Square(Shape):
    def __init__(self):
        self.type="Square"
        
    def draw(self):
        print("pinta un Cuadrado")