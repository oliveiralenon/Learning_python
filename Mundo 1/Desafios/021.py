"""
Faça um programa em Python que abra e reproduza
o áudio de um arquivo MP3.
"""
#import os
#os.startfile('C:\\Users\\julianamatthis\\Downloads\\song.mp3')

from pygame import mixer
mixer.init()
mixer.music.load('021.mp3')
mixer.music.play()
input('Agora você escuta?')
