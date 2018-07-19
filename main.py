from audio import play, listen

def too_loud_callback(rms):
    print(f"too_loud_callback rms: {rms}")

    if rms > 600:
        play.play_arnold_shut_up(volume=0)
        print('------arnold')
    elif rms > 400:
        play.play_shush(volume=0)
        print('------400')
    elif rms > 200:
        play.play_shush(volume=-600)
        print('------200')
    elif rms > 100:
        play.play_shush(volume=-2000)
        print('------100')

print('shushbot listening to shush')
listen.listen(threshold=0, too_loud_callback=too_loud_callback)
