# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:43:24 2020

@author: carlo
"""

from Meal import *
from VegBurger import *
from ChickenBurger import *
from Cocacola import *
from Pepsi import *

class Meal_builder():
    
    def prepareVegMeal(self):
        vegmeal= Meal()
        vegmeal.add_item(VegBurger())
        vegmeal.add_item(Cocacola())
        return vegmeal
    
    def prepareNonVegMeal(self):
        meal= Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal