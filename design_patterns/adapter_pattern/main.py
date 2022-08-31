# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:34:28 2020

@author: carlo
"""

from AudioPlayer import *

def main():
    audioPlayer=AudioPlayer()
    
    audioPlayer.play("mp3", "beyond the horizon.mp3")
    audioPlayer.play("mp4", "alone.mp4")
    audioPlayer.play("vlc", "far far away.vlc")
    audioPlayer.play("avi", "mind me.avi")
    
if __name__=='__main__':
    main()