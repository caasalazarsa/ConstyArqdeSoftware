# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:34:19 2020

@author: carlo
"""

import copy

class Shape():
    def __init__(self):
        self.id=None
        self.type=None
        self.parent=None
    
    def draw(self):
        pass
    
    def set_parent(self,parent):
        self.parent=parent
    
    def __copy__(self):
#        cid=copy.copy(self.id)
#        ctype=copy.copy(self.type)
        
        clone=self.__class__()
        clone.__dict__.update(self.__dict__)
        return clone

        
    
    