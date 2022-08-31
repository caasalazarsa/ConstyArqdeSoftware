# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:02:11 2020

@author: carlo
"""

from SingleObject import *

def main():    
    
    single=SingleObject().get_instance()
    
    single.show_message()
    

if __name__ == '__main__':
    main()