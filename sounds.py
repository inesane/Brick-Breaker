import os


def play_sound():
    os.system("aplay -q shoot.wav &")