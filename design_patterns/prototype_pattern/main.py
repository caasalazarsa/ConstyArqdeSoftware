# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:56:11 2020

@author: carlo
"""

from shapecache import *

def main():
    shapecache=ShapeCache()
    shapecache.loadCache()
    
    cloneshape=shapecache.getShape('1')
    print("Shape : "+cloneshape.type)
    
    
    cloneshape=shapecache.getShape('2')
    print("Shape : "+cloneshape.type)
    
    cloneshape=shapecache.getShape('3')
    print("Shape : "+cloneshape.type)
    
if __name__=='__main__':
    main()