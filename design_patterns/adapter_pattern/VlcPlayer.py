# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:10:27 2020

@author: carlo
"""

from AdvancedMediaPlayer import *

class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self,filename):
        print("Reproduciendo el archivo de nombre "+str(filename))
        