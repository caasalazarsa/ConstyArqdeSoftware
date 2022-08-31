# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:45:26 2020

@author: carlo
"""

class SingleObject():
    
    instance=None
    
    def __new__(cls):
        if SingleObject.instance is None:
            SingleObject.instance=object.__new__(cls)
        return SingleObject.instance
    
    def get_instance(self):
        return self.instance
    
    def show_message(self):
        print("Hola desde la instancia")


    