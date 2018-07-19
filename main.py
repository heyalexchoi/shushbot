from audio import play, listen

def too_loud_callback(rms):
    print(f"too_loud_callback rms: {rms}")

    if rms > 2000:
        play.play_arnold_shut_up(volume=0)
        print('-------------------------------------------------------------------------1200')
    elif rms > 1200:
        play.play_shush(volume=0)
        print('-------------------------------------------------------------------------900')
    elif rms > 600:
        play.play_shush(volume=-600)
        print('-------------------------------------------------------------------------600')
    elif rms > 300:
        play.play_shush(volume=-2000)
        print('-------------------------------------------------------------------------300')

print('shushbot listening to shush')
listen.listen(threshold=0, too_loud_callback=too_loud_callback)
