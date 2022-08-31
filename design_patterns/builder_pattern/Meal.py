# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:32:50 2020

@author: carlo
"""



class Meal():
    
    def __init__(self):
        self.items=[]
    
    def add_item(self,item):
        self.items.append(item)
        
    def get_cost(self):
        cost =0.0
        for item in self.items:
            cost+=item.price()
        
        return cost
        
    def showItems(self):
        for item in self.items:
            print("Item: "+item.name())
            print("Empaque: "+item.packing().pack())
            print("Precio: " +str(item.price()))