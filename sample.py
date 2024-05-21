from pygame import mixer as mix
mix.init()
def songPlayer(path):
    mix.music.load(path)
    mix.music.play()
    mix.music.set_volume(0.5)

def songControl(var):
    if var=="stop":
        mix.music.stop()
    elif var=="pause":
        mix.music.pause()
    elif var=="play":
        mix.music.play()
    elif var=="continue":
        mix.music.unpause()