import os


def play_sound():
    os.system("aplay -q shoot.wav &")

def play_sound2():
    os.system("aplay -q boss.wav &")