# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:10:31 2020

@author: carlo
"""

from FactoryProducer import*

def main():
    shapeFact = FactoryProducer().getFactory(False)
    
    fig1=shapeFact.getShape("CIRCLE")
    fig1.draw()
    
    fig2=shapeFact.getShape("RECTANGLE")
    fig2.draw()
    
    fig3=shapeFact.getShape("SQUARE")
    fig3.draw()

    shapeFact1 = FactoryProducer().getFactory(True)
    
    fig4=shapeFact1.getShape("RECTANGLE")
    fig4.draw()
    
    fig5=shapeFact1.getShape("SQUARE")
    fig5.draw()

if __name__ == '__main__':
    main()
    