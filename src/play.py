#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 01 Mar 2016 19:37:53
#
#

import pygame as pg
import os
import random
import time
from mutagen.mp3 import MP3

def play(music):

    pg.init()
    pg.mixer.init()
    pg.mixer.music.load(music)
    pg.mixer.music.play()

    time.sleep(MP3(music).info.length)

def get_list(path):

    files = os.listdir(path)
    return [name for name in files if name.endswith(('.mp3'))]


if __name__ == '__main__':

    path = '/media/root/Local Disk1/Music/'
    
    files = get_list(path)
    
    random.shuffle(files)

    for music in files:
        play(path + music)


