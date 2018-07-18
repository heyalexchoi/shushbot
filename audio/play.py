from os import system, path

def play_mp3(filename):
    """uses omxplayer to play file over rpi audio jack"""
    system(f"omxplayer -o local {filename}")

def play_shush():
    play_asset('arnold_shut_up.mp3')

def play_arnold_shut_up():
    play_asset('shhh.mp3')

def play_asset(name):
    assets_dir = path.join('..', path.dirname(__file__), 'assets')
    asset_filename = path.join(assets_dir, name)
    play_mp3(asset_filename)

