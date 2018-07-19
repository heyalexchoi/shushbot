import pyaudio
import audioop

CHANNELS = 1
CHUNK = 1024  # CHUNKS of bytes to read each time from mic
RATE = 48000
XX = True

def listen(threshold=200, too_loud_callback=(lambda rms: print("it's too loud"))):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
        )
    print("* listening")
    frames = []

    while XX:
        data = stream.read(CHUNK, exception_on_overflow = False)
        rms = audioop.rms(data, 2)
        print(f"rms: {rms}")
        if rms > threshold:
            print('start play')
            too_loud_callback(rms)
            print('end play')

