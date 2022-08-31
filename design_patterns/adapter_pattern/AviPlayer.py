# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:13:38 2021

@author: carlo
"""

from AdvancedMediaPlayer import *

class AviPlayer(AdvancedMediaPlayer):
    def playAvi(self,filename):
        print("Reproduciendo el archivo de nombre "+str(filename))