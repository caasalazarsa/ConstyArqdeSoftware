# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:26:30 2020

@author: carlo
"""
from Burger import *


class ChickenBurger(Burger):
    def price(self):
        return 50.0
    
    def name(self):
        return "Hamburguesa de Pollo"
