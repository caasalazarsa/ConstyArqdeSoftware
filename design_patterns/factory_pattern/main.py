# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:10:31 2020

@author: carlo
"""

from shapeFactory import *

def main():
    shapeFact = shapeFactory()
    
    fig1=shapeFact.getShape("CIRCLE")
    fig1.draw()
    
    fig2=shapeFact.getShape("RECTANGLE")
    fig2.draw()
    
    fig3=shapeFact.getShape("SQUARE")
    fig3.draw()
    
    fig4=shapeFact.getShape("TRIANGLE")
    fig4.draw()

if __name__ == '__main__':
    main()
    