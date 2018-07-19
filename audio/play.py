from os import system, path
# https://stackoverflow.com/questions/33162820/adjust-audio-volume-level-with-cli-omxplayer-raspberry-pi
# volume 1%, XXX=0.01 and YYY=-4000 (10^(-4000/2000)=10^-2=0.01
# volume 10%, XXX=0.1 and YYY=-2000 (10^(-2000/2000)=10^-1=0.1
# volume 50%, XXX=0.5 and YYY=-602  (10^(-602/2000))~=0.5
# volume 100%, XXX=1 and YYY=0 (10^(0/2000)=10^0=1)
# volume 150%, XXX=1.5 and YYY=352 ... (for boost test, normal values are <=100%)
def play_mp3(filename, volume=-602):
    """uses omxplayer to play file over rpi audio jack"""
    system(f"omxplayer --vol {volume} -o local {filename}")

def play_shush(volume=-602):
    play_asset(name='shhhh.mp3', volume=volume)

def play_arnold_shut_up(volume=-602):
    play_asset(name='arnold_shut_up.mp3', volume=volume)

def play_asset(name, volume=-602):
    assets_dir = path.join(path.dirname(path.dirname(__file__)), 'assets')
    asset_filename = path.join(assets_dir, name)
    play_mp3(filename=asset_filename, volume=volume)

