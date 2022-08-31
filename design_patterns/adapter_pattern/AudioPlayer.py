# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:27:00 2020

@author: carlo
"""

from MediaPlayer import *
from MediaAdapter import *

class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.mediaadapter= None
        
    def play(self,audiotype,filename):
        if(audiotype.casefold()=='mp3'):
            print("Reproduciendo el archivo de nombre "+str(filename))  
            
        elif(audiotype.casefold()=='vlc' or audiotype.casefold()=='mp4' or audiotype.casefold()=="avi"):
            self.mediaadapter= MediaAdapter(audiotype)  
            self.mediaadapter.play(audiotype,filename)
        else:
            print("Formato "+str(audiotype)+" no válido")