# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:13:20 2020

@author: carlo
"""

from AdvancedMediaPlayer import *

class Mp4Player(AdvancedMediaPlayer):
        
    def playMp4(self,filename):
        print("Reproduciendo el archivo de nombre "+str(filename))