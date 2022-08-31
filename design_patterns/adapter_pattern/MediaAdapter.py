# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:15:49 2020

@author: carlo
"""

from MediaPlayer import *
from VlcPlayer import *
from Mp4Player import *
from AviPlayer import *

class MediaAdapter(MediaPlayer):
    
    
    
    def __init__(self,audiotype):
        self.advancedmediaplayer=None
        if(audiotype.casefold()=='vlc'):
            self.advancedmediaplayer=VlcPlayer()
        elif(audiotype.casefold()=='mp4'):
            self.advancedmediaplayer=Mp4Player()
        elif(audiotype.casefold()=='avi'):
            self.advancedmediaplayer=AviPlayer()
            
    def play(self,audiotype,filename):
        if(audiotype.casefold()=='vlc'):
            self.advancedmediaplayer.playVlc(filename)
        elif(audiotype.casefold()=='mp4'):
            self.advancedmediaplayer.playMp4(filename)
        elif(audiotype.casefold()=='avi'):
            self.advancedmediaplayer.playAvi(filename)
