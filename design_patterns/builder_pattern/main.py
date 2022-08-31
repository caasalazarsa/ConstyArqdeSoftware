# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:48:55 2020

@author: carlo
"""

from Meal_builder import *

def main():
    
    meal_builder = Meal_builder()
    
    vegMeal = meal_builder.prepareVegMeal()
    print("Comida Vegetariana")
    vegMeal.showItems()
    print("Costo total: "+str(vegMeal.get_cost()) )
    
    print('\n')

    nonvegMeal = meal_builder.prepareNonVegMeal()
    print("Comida NO Vegetariana")
    nonvegMeal.showItems()
    print("Costo total: "+str(nonvegMeal.get_cost()) )
    

if __name__ == '__main__':
    main()

    
    