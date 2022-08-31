# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:44:07 2020

@author: carlo
"""
from shape import *

class Circle(Shape):
    def __init__(self):
        self.type="Circle"
        
    def draw(self):
        print("pinta un Círculo")